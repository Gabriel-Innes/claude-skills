#!/usr/bin/env python3
"""Fetch a SAP Business One schema from erpref.com into a local cache (maintenance only).

erpref.com serves its schema pages as empty shells and fills them from JSON POST endpoints, so scraping the
HTML gets nothing. This script uses the same endpoints the site's own pages call:

  POST <base>/Schema/GetModule  moduleid=1..12  -> table list per module (name, description, column/index counts)
  POST <base>/Schema/GetTable   table=<NAME>    -> every column (type, length, description, relation, valid values)
  GET  <base>/Table/Detail/<NAME>               -> HTML; the index list is only here

Raw responses are cached (cache/tables.json, cache/cols/<T>.json, cache/idx/<T>.html) so a run can be
resumed and the build step never refetches. Requests are sequential with a delay: ~2 requests per table,
~2,500 tables, about 2-3 hours at the defaults. Be gentle; this is a small third-party site.

    python fetch_erpref_schema.py --cache <dir> [--site-version BusinessOne9.3] [--module MRP] [--delay 0.5]
"""
import argparse, json, os, random, re, sys, time, urllib.error, urllib.parse, urllib.request

UA = "sapb1-assistant-schema-fetch/1.0 (personal reference compilation)"
HOST = "https://erpref.com"
MODULES = range(1, 13)


def request(req, tries=6):
    for attempt in range(tries):
        try:
            return urllib.request.urlopen(req, timeout=60).read()
        except (urllib.error.URLError, TimeoutError) as e:
            wait = 2 ** attempt * 2 + random.random()
            print(f"  retry {attempt + 1}/{tries} after {e}; sleeping {wait:.0f}s", flush=True)
            time.sleep(wait)
    raise RuntimeError("giving up after repeated failures")


def post_json(url, data):
    body = urllib.parse.urlencode(data).encode()
    headers = {"User-Agent": UA, "X-Requested-With": "XMLHttpRequest"}
    raw = request(urllib.request.Request(url, body, headers))
    return raw, json.loads(raw)


def fetch_listing(base, cache, delay):
    path = os.path.join(cache, "tables.json")
    if os.path.exists(path):
        return json.load(open(path, encoding="utf-8"))
    tables = []
    for m in MODULES:
        _, j = post_json(f"{base}/Schema/GetModule", {"draw": 1, "start": 0, "length": -1, "moduleid": m})
        if len(j["data"]) != j["recordsTotal"]:
            sys.exit(f"module {m}: got {len(j['data'])} of {j['recordsTotal']} rows")
        for d in j["data"]:
            d.pop("schema", None)
            d["table"] = re.sub(r"<[^>]+>", "", d["table"])
            tables.append(d)
        time.sleep(delay)
    json.dump(tables, open(path, "w", encoding="utf-8"))
    print(f"listing: {len(tables)} tables, {sum(t['cols'] for t in tables)} columns", flush=True)
    return tables


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cache", required=True, help="cache folder (created; resumable)")
    ap.add_argument("--site-version", default="BusinessOne9.3", help="erpref.com path segment, e.g. BusinessOne9.3")
    ap.add_argument("--module", help="only this module name, e.g. MRP or 'Inventory and Production'")
    ap.add_argument("--delay", type=float, default=0.5, help="seconds between requests (default 0.5)")
    a = ap.parse_args()

    base = f"{HOST}/{a.site_version}"
    for sub in ("cols", "idx"):
        os.makedirs(os.path.join(a.cache, sub), exist_ok=True)
    tables = fetch_listing(base, a.cache, a.delay)
    if a.module:
        tables = [t for t in tables if t["module"].lower() == a.module.lower()]
        if not tables:
            sys.exit(f"no tables in module {a.module!r}")

    failed = []
    for n, t in enumerate(tables, 1):
        name = t["table"]
        cols_path = os.path.join(a.cache, "cols", f"{name}.json")
        idx_path = os.path.join(a.cache, "idx", f"{name}.html")
        try:
            if not os.path.exists(cols_path):
                raw, j = post_json(f"{base}/Schema/GetTable", {"table": name, "draw": 1, "start": 0, "length": -1})
                if not len(j["data"]) == j["recordsTotal"] == t["cols"]:
                    raise RuntimeError(f"column count {len(j['data'])}/{j['recordsTotal']} != listed {t['cols']}")
                open(cols_path, "wb").write(raw)
                time.sleep(a.delay)
            if not os.path.exists(idx_path):
                raw = request(urllib.request.Request(f"{base}/Table/Detail/{name}", headers={"User-Agent": UA}))
                open(idx_path, "wb").write(raw)
                time.sleep(a.delay)
        except Exception as e:
            print(f"FAIL {name}: {e}", flush=True)
            failed.append(name)
        if n % 50 == 0:
            print(f"{n}/{len(tables)} {name}", flush=True)
    print(f"done: {len(tables)} tables, {len(failed)} failed {failed}", flush=True)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
