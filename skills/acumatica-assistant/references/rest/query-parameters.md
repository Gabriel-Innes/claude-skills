<!-- source: Acumatica Integration Development Guide, "REST API Examples > Parameters for Retrieving Records" ($filter/$expand/$select per contract version, $top, $skip, $custom) and "Contract Versions"; URLs in INDEX.md | version: Acumatica ERP 2026 R2 (guide edition 2026-09-30) | verified: 2026-10-03 -->

# Query parameters ($filter, $expand, $select, $custom, $top, $skip)

The parameters are the same names in both contract versions but the **syntax differs**: Contract Version 5
(the `Default/26.200.001` endpoint and custom endpoints created from scratch in 2026 R2) follows **OData 4.01**
URL conventions; Contract Version 4 (`Default/25.200.001` and earlier system endpoints) follows **OData 3.0**.
Know the endpoint's contract version before writing a URL (`endpoint-versions.md`).

## 1. $filter

Both versions: combine conditions with `and` / `or`; comparison operators as in OData (`eq`, `ne`, `gt`, `ge`,
`lt`, `le`, `not`); conditions on a **linked** entity use a path (`MainContact/Email eq 'demo@gmail.com'`);
**filtering on detail entities is not supported** (results are unpredictable); URL-encode date-time values.

| | Contract Version 5 (OData 4.01) | Contract Version 4 (OData 3.0) |
|---|---|---|
| String functions | `contains`, `startswith`, `endswith` | `substringof`, `startswith`, `endswith` |
| Drop-down value | the internal **ID**: `ItemStatus eq 'AC'` | the plain value as the contract exposes it (guide shows both `'Active'` and `'AC'`) |
| Date-time literal | bare: `LastModifiedDateTime gt 2024-07-15T10%3A31%3A28.402%2B03%3A00` | `datetimeoffset'2024-07-15T10%3A31%3A28.402%2B03%3A00'` |
| Date-only literal | bare: `Date gt 2025-06-17` | `date'2025-06-17'` |
| Multi-select field | `Ownership/any()`, `not Ownership/any()`, `Ownership/any(x: x eq 'MO')`, `Ownership/all(x: x eq 'MO')`, `Ownership/all(x: x eq null)`, `Ownership/all(x: x ne 'MO')` | `any()`/`all()` not supported |
| Custom field | `cf.<Type>('<View>.<Field>')`, e.g. `cf.StringSingleSelect('ItemSettings.UsrRepairItemType') eq 'BT'`, `cf.Decimal('Document.CuryBalanceWOTotal') eq 0`, `cf.DateTime('Document.DiscDate') gt 2024-02-18T...` | `cf.<Type>(f='<View>.<Field>')`, e.g. `cf.StringSingleSelect(f='ItemSettings.UsrRepairItemType') eq 'BT'` |

Custom-field filter types seen in the guide: `cf.String`, `cf.Decimal`, `cf.DateTime`, `cf.StringSingleSelect`,
`cf.IntSingleSelect`. There is **no `cf.StringMultiSelect`**: filter an unmapped custom multi-select with a
substring search, `contains(cf.String('Document.AttributeOWNERSHIP'), 'MO')`, or map the field in an endpoint
extension as `StringMultiSelectValue` to get collection filtering.

Encoding tip from the guide (C#): `WebUtility.UrlEncode(new DateTimeOffset(DateTime.Now).ToString("yyyy-MM-ddTHH:mm:ss.fffK"))`.

## 2. $expand

Nothing nested is returned unless listed. Every linked or detail entity you want in the response must be named,
including in PUT/PATCH responses. Using `$expand` does not consume the license's concurrent-request or
rate limits faster.

| | Contract Version 5 | Contract Version 4 |
|---|---|---|
| Detail entity | `$expand=WarehouseDetails` | `$expand=WarehouseDetails` |
| Nested linked entity | `$expand=MainContact($expand=Address)` | `$expand=MainContact,MainContact/Address` |
| Files of the top-level record | `$expand=files` | `$expand=files` |
| Files of detail lines | `$expand=WarehouseDetails($expand=files)` | `$expand=WarehouseDetails/files` |
| Several expansions | comma-separated: `$expand=Details($expand=Allocations),Packages($expand=PackageContents)` | comma-separated paths |

## 3. $select

| | Contract Version 5 | Contract Version 4 |
|---|---|---|
| Top-level fields | `$select=OrderType,OrderNbr` | `$select=OrderType,OrderNbr` |
| Fields of nested entities | selected **inside the matching `$expand`**, options separated by `;`: `$expand=MainContact($select=Email;$expand=Address($select=City))&$select=CustomerName` | paths in the top-level `$select`: `$expand=MainContact,MainContact/Address&$select=CustomerName,MainContact/Email,MainContact/Address/City` |
| All contract fields plus a custom field | `$select=*,Document.AttributePRODUCT` | contract fields in `$select`, custom fields in `$custom` |
| Custom field of a top-level entity | `$select=ItemSettings.UsrRepairItemType` | `$custom=ItemSettings.UsrRepairItemType` |
| Custom field of a detail entity | `$expand=Details($select=Transactions.UsrRepairItemType)` | `$custom=Details/Transactions.UsrRepairItemType&$expand=Details` |
| User-defined field | `$select=Document.AttributeOPERATSYST` | `$custom=Document.AttributeOPERATSYST` |

`$select` on a PUT/PATCH limits what the response echoes back; the guide's examples use it to keep write
responses small (`$select=OrderNbr,OrderType&$expand=Details($select=OrderQty,InventoryID)`).

## 4. $custom (Contract Version 4 only)

Lists custom fields to return: `<View>.<Field>` for the top-level entity, `<Entity>/<View>.<Field>` for a
linked or detail entity (that entity must also be in `$expand`), `<View>.Attribute<AttributeID>` for a
user-defined field; several separated by commas. In Contract Version 5 the same things go in `$select`.

## 5. $top and $skip

- `$top=N` returns the first N records; without it all records are returned (and a SQL Server Resource
  Governor limit can turn that into an error).
- `$skip=N` skips N records; with both, `$skip` is applied first.
- **No parameter returns the total count**; paginate until a page is shorter than `$top`.
- Example from the guide: `GET .../SalesOrder?$top=5&$skip=5&$select=CustomerID,LocationID,OrderNbr,OrderType`.

## 6. Where each parameter is accepted

| Request | $filter | $expand | $select | $custom (CV4) | $top / $skip |
|---|---|---|---|---|---|
| GET list | yes | yes | yes | yes | yes |
| GET by keys / by ID | no | yes | yes | yes | no |
| PUT create | no | yes | yes | yes | no |
| PUT / PATCH update | yes (to identify the record) | yes | yes | yes | no |
| PUT inquiry / processing filter | no | yes (the result entity, required) | yes | | no |
| POST action | no parameters | | | | |

(From the Parameters sections of the *Basic Requests* topics.)
