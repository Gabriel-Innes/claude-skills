# Sage 200 Evolution data dictionary - index

Read this first, then open only what the request needs. The dictionary is hand-maintained: the files below are
the single copy of what we know about the Evolution company database (schema of a scripted company database plus
Sage's own table descriptions). Edit them directly when new information arrives; there is nothing to rebuild.

| Path | Covers |
|---|---|
| `conventions.md` | How Evolution stores data in SQL: table-name prefixes, column-name prefixes, identity primary keys, how tables link (no declared foreign keys - joins follow naming), posting tables, NULL/default behaviour, the two databases, view rules, worked example |
| `dict/Core.md` | 73 core tables (no prefix): `Client`, `Vendor`, `StkItem`, `Accounts`, `InvNum`, `PostGL`, `PostAR`, `PostAP`, `PostST`, `WhseMst`, `WhseStk`, `TrCodes`, `Entities`, `Project`, `Currency`, `TaxRate`, job costing (`JobNum`, `JobDef`), BOM, credit control, discounts, serial numbers, recurring billing … |
| `dict/Evolution-extended.md` | 208 `_etbl*` tables: GL balances/budgets/segments, allocations, AR/AP batches, lot tracking, units of measure, price lists, remittances, requisitions, tax, warehouses and inter-branch transfers, bin locations, attributes, EFT, Sage Pay, VAT submission … |
| `dict/Business-modules.md` | 82 `_btbl*` tables: Fixed Assets (`_btblFA*`), Contact Management events/workflow (`_btblCM*`), Job Costing (`_btblJC*`), journal and cashbook batches, inventory counts, **document lines** (`_btblInvoiceLines`), POS, Tax Manager (`_btblTM*`), agent security |
| `dict/Contact-Management.md` | 58 `_rtbl*` tables: agents, incidents, knowledge base, opportunities, contracts, people, business classifications, the user-defined-field dictionary (`_rtblUserDict`) |
| `dict/Retail-POS.md` | 34 `_ret*` tables: tills, tenders, trading sessions, cash pickups, petty cash, lay-bys |
| `dict/Municipal-Billing.md` | 51 `_mtbl*` tables (+ `_tAudit`): properties, meters, tariffs, billing runs. Sage ships no descriptions for these |
| `dict/Application-metadata.md` | 23 `_atbl*` tables: data import/export templates, bulk e-mail, Evolution's own table/column dictionary (`_atblTables`, `_atblColumns`, `_atblTableRelationships`) |
| `dict/Delivery-Management.md` | 5 `_dtbl*` tables and `_dReportLayout` |
| `dict/Add-on-modules.md` | 133 tables of add-on modules present in the scripted database: `_smtbl*` (service management), `_simtbl*` (requisitions / stock issues), `_iotbl*` (reorder), `RFQ*` (request for quotation - the only tables with declared foreign keys), `WHT_*` (withholding tax), `PR_*` (vouchers), `NT_*` (supplier audit). Not every site has them |
| `dict/Site-specific-and-snapshots.md` | 22 tables that are **not Evolution**: custom integration tables (`_as_*`), sync helpers, and dated snapshot copies of standard tables (`Accounts20250825`, `StkItem_20260417`, `Thyme_StkItemBackup` …). Never report on these as Evolution data |

689 tables in all, 15,404 columns. Ten tables (for example `_etblGLProjectBalances`, `_etblFAAssetBarCode`,
`_retEOD`, `ACCBLNC`) were seen in another Evolution database but are not in the scripted one; their entries say
`Columns: none recorded yet`. The scripted database's Evolution version is not recorded - confirm the client's
version before relying on columns that other releases add or drop.

## Entry format (same in every `dict/` file)

```
## Client - Customer (Customer)                      <- TABLE - alias (Freedom Name = SDK class it backs)
Alias: Customer | Freedom Name: Customer | Record Identifier: Account
Notes: <Sage's own description of the table>
PK: DCLink | UNIQUE: ... | FK: col -> Table(col)     <- declared keys only; Evolution declares almost no FKs
Columns (103):
  DCLink int NOT NULL identity PK - <description>    <- Name type(size) NULL|NOT NULL [identity] [PK] [default X] - description
  Account varchar(20) NULL - <description>
```

A column line without ` - text` has no description yet. Column casing is as the catalog has it; SQL Server
compares names case-insensitively.

## How to use (SKILL.md § 3)

1. Find the table: grep `^## ` across `dict/` by table name, alias or Freedom Name, or grep `Notes:` for a topic
   in Sage's wording. The group table above says which file holds which prefix.
2. Read the entry: Notes, the `PK` line, and **every column you intend to use** (name, type, nullability).
3. Join by `conventions.md` § 4; where a join rests on naming rather than a declared key, say so in the delivered
   SQL and include a sanity query.
4. Never write to these tables with SQL; the SDK (`../sdk/`) is the write path.

## Maintaining this dictionary

- **New or corrected table description** (from Evolution's Database Object browser): edit the `Alias | Freedom
  Name | Record Identifier` and `Notes` lines of the entry. Add those two lines if the entry lacks them.
- **Column description**: append ` - text` to the column line. Keep Sage's wording where it exists; add
  value lists inline (`- document type: 1=…, 2=…`) when confirmed on data.
- **New table**: add a `## TABLE` entry to the file of its prefix, in alphabetical order, with the columns from
  `sys.columns` or an SSMS script, in the format above. Update the count in the group table here.
- **New Evolution version**: when a client database shows a column the dictionary lacks, add it and note the
  version in the column description (`- added in 11.x`).
- Keep `conventions.md` in step: every table and column it names must exist in `dict/`.
