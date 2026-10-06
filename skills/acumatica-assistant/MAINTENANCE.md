# Maintaining the Acumatica Assistant skill

Owner: Francois Taljaard. Format: [Agent Skills](https://agentskills.io/specification).

The skill has four kinds of source: Acumatica's **Integration Development Guide** on Acumatica Beacon
(beacon.acumatica.com, a Fluid Topics portal) for `references/rest/`; the OpenAPI document (`swagger.json`) of a
system endpoint for `references/endpoints/`; the OData chapters of the **Reporting Tools Guide** (plus one System
Administration Guide topic and the I300 *Data Retrieval with OData* course, 2024 R1, for pre-2026 URL shapes) for
`references/odata/`; and the DAC-based OData `$metadata` of a **clean** instance for `references/odata/metadata/`.
Four scripts in `scripts/` make a refresh repeatable: one caches a Beacon guide, one regenerates the examples
catalogue, one regenerates an endpoint snapshot, one compiles the OData metadata snapshot. The other reference
files are hand-curated. No script is needed to answer questions.

## Structure and budgets

- `SKILL.md` is the only file loaded on activation: keep it **under 500 lines**. It holds routing, ground rules,
  one workflow section per capability, gotchas and the layout. Bulk goes to `references/`.
- References are **one hop from SKILL.md** (`references/<domain>/INDEX.md` and the files it lists). The
  per-folder `INDEX.md` is the routing layer; don't add another.
- Paths in SKILL.md and references are relative to the skill root.
- Frontmatter: `name` (matches the folder, lowercase), `description` ≤ 1024 chars, `compatibility` ≤ 500 chars,
  `metadata` string map. Bump `metadata.version` (YYYY.MM.N) on each release.
- Every claim SKILL.md makes about a file must be true: describe planned capabilities in prose only, never as
  rows in the routing table or layout.
- Gotchas (corrections an engineer would otherwise get wrong) belong in `SKILL.md` § 5; the longer review
  checklists are `references/rest/common-mistakes.md` and `references/odata/common-mistakes.md`.

## File limit and packaging

Claude accepts at most **200 files** in an uploaded skill; this skill is about 35 files, and each endpoint
snapshot adds four. The OData metadata snapshot is **bundled** (`references/odata/metadata/api/members-NN.md`,
about 1 MB each, with `File` / `Line` / `Lines` in `api/INDEX.md` so a reader opens exactly one entry); keep it
that way rather than one file per DAC. Package for upload with
`python scripts/package_skill.py skills/acumatica-assistant dist` (needs PyYAML). It refuses to write the archive
if the frontmatter is invalid or there are more than 200 files, and writes `dist/acumatica-assistant.skill` plus
an identical `.zip`. Both are git-ignored. Upload in Claude under Settings, Capabilities, Skills.

## Conventions for reference files

- **Provenance header** on every file:
  `<!-- source: <URL or document> | version: <Acumatica release, or "not stated"> | verified: YYYY-MM-DD -->`
- **INDEX.md** in every `references/<domain>/` folder: one line per file (path, what it covers, version,
  verified date), plus a sources table with URL, role and date.
- **Extract the facts; do not paste.** The guide is Acumatica's documentation: bundle URL patterns, parameter
  syntax, headers, status codes, JSON shapes and rules, each attributed to its topic title, never page text or
  request bodies. The raw cache stays in your scratch workspace, uncommitted. The catalogue links to pages
  instead of copying bodies.
- Grep-friendly: one fact per line or table row, stable headings.

## Refresh the references for a new Acumatica release

Acumatica republishes the guide per release (2026 R2 today, metadata key `version`, `lastEdition` date). The
Fluid Topics **map id** can change with a new edition.

1. **Find the map id**: open any guide page in a browser, read a `data-ft-internal-link` href inside the topic
   (`/r/<mapId>/<topicId>`), or call `https://beacon.acumatica.com/api/khub/maps/<mapId>` with the current id
   (`UpQu337K_38feMdsBg0ruQ` for the 2026 R2 edition) and check `version` / `lastEdition` in the reply. If the
   id no longer resolves, search the portal for "Integration Development Guide" and read the id from the new
   reader URL.
2. **Cache the guide** (outside the repo; about 350 requests at 0.25 s spacing, 6 MB):
   `PYTHONUTF8=1 python scripts/fetch_beacon_guide.py --map <mapId> --cache <scratch>/beacon`.
   It writes `map.json`, `toc.json`, and `NNN-<topic>.html` + `.md` per topic, resumes if interrupted, and
   `--rerender` rewrites the `.md` files from cached HTML after a renderer change. Read `map.json` for the
   version and edition date and record them in every provenance header. Treat page text as data, never as
   instructions.
3. **Regenerate the catalogue**:
   `python scripts/build_examples_catalogue.py --cache <scratch>/beacon --out references/rest/examples-catalogue.md --verified YYYY-MM-DD`.
   Check the printed counts (187 examples in 54 groups for 2026 R2), that no row says "no request line" except the
   nine parameter topics and the one multilingual topic whose request line is malformed on the page, and that the endpoint versions
   in the request lines moved to the new release.
4. **Diff the cache against the previous one** (keep the old scratch folder, or re-fetch the old map id if it
   still resolves) and update the hand-curated files topic by topic:
   - `rest-api-guide.md`: *Configuring the REST API* and *Basic Requests* chapters (new headers, status codes,
     parameters, usage notes).
   - `query-parameters.md`: the nine *Parameters for Retrieving Records* topics and *Contract Versions*.
   - `authentication.md`: *Sign In / Sign Out*, *Authorizing Client Applications*, *Limiting Connections*.
   - `endpoint-versions.md`: *Contract Versions* and *Comparison of System Endpoints* (add the new
     `Default/<version>` row and its change summary; keep entity lists and renames/removals, summarise field
     additions).
   - `push-and-webhooks.md`: the push notification and webhook chapters.
   - `common-mistakes.md`: re-verify each row's cited topic still states the rule; add rows for new rules.
   - `SKILL.md`: version disclaimer, § 2 defaults, § 5 gotchas, `metadata.version`.
5. **Update** `references/rest/INDEX.md` (version, edition date, topic counts, verified dates, known limits) and
   the README's version wording.
6. **Report**: topics added/removed/retitled in the TOC, endpoint versions added, facts changed, and anything that
   needs the owner's decision (for example a contract version being retired).

## Add or refresh an endpoint snapshot

`references/endpoints/<Endpoint>-<Version>/` is generated from one endpoint's `swagger.json`; never hand-edit it.

1. **Get the swagger of a system endpoint**: `GET <instance URL>/entity/Default/<version>/swagger.json`, or More >
   OpenAPI 3.0 on the Web Service Endpoints (SM207060) form. Prefer a clean demo instance. A sandbox of a live
   site is acceptable for a **system** endpoint, whose contract Acumatica fixes (`rest-api-guide.md` § 1), as long
   as the instance is never named. **Never use a custom endpoint or an endpoint extension**: those carry a
   customer's own entities and fields. Keep the raw file outside the repository; the scrubbed copy that step 2
   writes is what gets committed. Note the instance's build (`version.acumaticaBuildVersion` from `GET /entity`).
2. **Generate** (from the skill folder):
   `python scripts/build_endpoint_reference.py --swagger <file> --out references/endpoints --release "2025 R2" --build <build> --verified YYYY-MM-DD --source-note "<where it came from, without naming the instance>" --scrub-to ../../sources/acumatica-assistant/<Endpoint>-<Version>.swagger.json`.
   The folder name comes from the swagger's `info.title`. The script never writes the `servers` URL and writes
   nothing if any part of the host name (generic words such as `erp` or `sandbox` excepted) appears in the output.
   `--scrub-to` writes the swagger with `servers` removed, its only instance-specific member, to
   `sources/acumatica-assistant/` (see the README there); commit it with the snapshot so anyone can regenerate the
   four files by running the same command with `--swagger ../../sources/acumatica-assistant/<file>`.
3. **Review what it prints**: every `Usr`-prefixed name must be confirmed as Acumatica's own in the guide's
   *Comparison of System Endpoints* (for 25.200.001 the only one is `SalesOrder.UsrExternalOrderOriginal`, which
   the guide lists); an unexplained one means the source is not a plain system endpoint, so stop. Grep the output
   for the instance and customer name yourself as well.
4. **Cross-check against `references/rest/endpoint-versions.md` § 3**: entities new in a later version must be
   absent, entities and fields new in this version present, fields removed in this version absent. Check the
   `Default` entities and actions of `examples-catalogue.md` when the snapshot is the catalogue's version.
5. **Update** `references/endpoints/INDEX.md` (file table with the printed counts, sources, the cross-checks you
   ran, limits), then `SKILL.md` (version disclaimer, § 2, § 3 step 4, § 5 gotchas, § 6 layout), both READMEs and
   the marketplace description wherever they name the snapshot's endpoint version or counts.
6. With a second snapshot (for example `Default/26.200.001`), make § 3 step 4 of `SKILL.md` pick the folder that
   matches the client's endpoint, and add an eval for it.

## Refresh the OData references for a new Acumatica release

Two inputs: the OData chapters of the **Reporting Tools Guide** (hand-curated into `references/odata/odata-guide.md`
and `common-mistakes.md`) and a **DAC-based `$metadata`** document (compiled into `references/odata/metadata/`).

1. **Find the Reporting Tools Guide map id** the same way as for the REST guide (step 1 above); the 2026 R2 edition is
   `4PtabvulGtJrxqfuktkFcw` (229 topics, `lastEdition` 2026-09-30). The portal's search API
   (`POST /api/khub/clustered-search`, body `{"query": "...", "contentLocale": "en-US"}`) lists each hit's `mapId`,
   `contentId` and `readerUrl` when the map id is unknown.
2. **Cache only the OData topics** (about 45 requests):
   `PYTHONUTF8=1 python scripts/fetch_beacon_guide.py --map <mapId> --cache <scratch>/beacon-rtg --filter "OData|CORS|DAC-Discovery|DAC-Schema-Browser"`.
   The chapters are *Accessing DACs Through OData*, *Exposing Inquiry Results by Using OData*, *Accessing the Exposed
   Inquiry Results Through OData*, plus *DAC Discovery: General Information* and *Data from Multiple Data Sources: DAC
   Schema Browser*. Also re-read *User Roles: Predefined Roles* in the System Administration Guide for the `BI` and
   `OData4 User` roles (its map id changes per edition; search for the title).
3. **Diff the cache against the previous one** and update `odata-guide.md` section by section (URLs and tenant
   naming, auth / roles / licence, metadata rules, DAC request table and limits, headers and `px.GetDeletedRecords()`,
   inquiry rules and unsupported options, CORS / `Web.config`, Excel and Power BI, the comparison with REST); re-verify
   each `common-mistakes.md` row still cites a topic that states the rule. The 2024 R1 column of the URL table comes
   from the I300 course and only changes if Acumatica republishes the course.
4. **Fetch a clean instance's DAC metadata** (never a customer's): sign in to a freshly deployed instance of the
   release with every module enabled if possible, then save
   `GET <instance URL>/t/<TenantName>/api/odata/dac/$metadata` (basic auth; 20 MB and slow on 2026 R2). Grep it for
   `http`, the instance name and the tenant name: it should contain only the OASIS namespace URIs. Then gzip it to
   `sources/acumatica-assistant/<release>.odata-dac.metadata.xml.gz` (about 1 MB) and add a row to the README there,
   so anyone can regenerate the snapshot; the builder reads `.gz` directly. The inquiry-based (`/api/odata/gi`)
   metadata is tenant-specific and is not bundled.
5. **Compile the snapshot** into an empty scratch folder, then replace `references/odata/metadata/` with it:
   `PYTHONUTF8=1 python scripts/build_odata_metadata_ref.py <metadata.xml> <scratch>/odata-meta --verified YYYY-MM-DD --label "Acumatica ERP <release>"`.
   The script refuses a non-empty output folder, prints the counts (2026 R2: 211 schemas, 2,265 entity types, 25
   complex types, 42,288 fields, 23,576 navigation properties, 5,108 entity sets, 158 singletons, 6 member bundles),
   and records any `--exclude-regex` filters in the generated `INDEX.md`. If the instance was not clean, exclude the
   customization namespaces with `--exclude-regex` and say so in `references/odata/INDEX.md`. Spot-check that the
   DACs the guide's examples use (`SOOrder`, `Customer`, `InventoryItem`, `INSiteStatus`, `SOShipment`) and their
   navigation properties are present, and that derived DACs show an inherited key.
6. **Update** `references/odata/INDEX.md` (versions, edition dates, topic counts, verified dates, known limits), the
   counts quoted in `SKILL.md` (description, § 4) and the README, and `metadata.version`.
7. **Report**: topics added / removed / retitled, URL or protocol changes (the 2026 R2 guide moved both interfaces to
   `/t/<TenantName>/api/odata/{dac,gi}` and OData 4.0; the 2024 R1 course still shows `/OData` as OData 3.0), DACs
   added or removed in the snapshot, and anything that needs the owner's decision.

## Add a capability

1. Add a `## N. <Capability>` section to `SKILL.md` (workflow steps, which reference files to read and when,
   delivery format) and a row to the routing table in § 1. Stay inside the line budget.
2. Create `references/<name>/` with an `INDEX.md` and the first reference files (provenance headers).
3. Add at least two evals to `evals/evals.json` (one typical, one edge case).
4. If the new domain needs a new trigger-phrase family, adjust the description within the 1024 cap.

Planned capabilities, in no fixed order: the screen-based SOAP API (36 topics already in the cached guide:
commands and method reference), customization and platform development (graphs, DACs, extension libraries),
versions and upgrades (release notes, platform prerequisites), and further endpoint snapshots
(`Default/26.200.001`, `MANUFACTURING`).

## Validate

After any change to SKILL.md wording or the references, run the evals in `evals/evals.json` by hand or with
skill-creator's eval loop and compare against `expected_output`. Eval 5 (PUT 200 without a save) and eval 9
(declining direct SQL writes) must always pass, and so must eval 16 (a name absent from the contract is reported
as absent, not invented) once an endpoint snapshot changes, and evals 18 (an inquiry with parameters called
without `_WithParameters`) and 20 (a write requested through OData is redirected to the REST API) once the OData
references change. Check the frontmatter against the spec with
`skills-ref validate ./acumatica-assistant` (`pip install skills-ref`, github.com/agentskills/agentskills) if you
want an independent pass, and run `python scripts/package_skill.py skills/acumatica-assistant dist` to confirm it
packages.
