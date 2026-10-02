# Sage 200 Evolution - how the database is laid out, and how to write SQL against it

Read this before writing SQL. Every table and column still has to be verified in `dict/` (SKILL.md § 3); this file
explains the patterns so you look in the right place and join correctly.

## 1. One company database, plus EvolutionCommon

- Each Evolution **company** is one SQL Server database (`dbo` schema throughout). The scripted sample is `EVO`.
  A second database, **`EvolutionCommon`**, holds shared data (agents/users, company registration). It is not in
  this dictionary; the SDK opens both (`references/sdk/sdk-guide.md`).
- Table and column names are mixed case in the catalog (`Client`, `StkItem`, `_btblInvoiceLines`); SSMS and Evolution's
  own browser sometimes show the core tables upper-case (`CLIENT`, `STKITEM`). SQL Server compares case-insensitively
  under the default collation, so either spelling works; the dictionary uses the catalog spelling.
- The script contains **tables only** - no views, stored procedures or data. Evolution's own metadata lives in
  `_atblTables` / `_atblColumns` / `_atblTableRelationships` (Data Import module), which can be queried on a live
  database for relationships this dictionary does not carry.

## 2. Table-name prefixes = module

| Prefix | Module (what the tables cover) | Example |
|---|---|---|
| *(none)* | Core Evolution, inherited from Pastel Evolution: masters, documents, posting | `Client`, `Vendor`, `StkItem`, `Accounts`, `InvNum`, `PostGL`, `PostAR`, `PostAP`, `PostST`, `WhseMst`, `WhseStk`, `TrCodes`, `Entities`, `Project`, `Currency`, `TaxRate` |
| `_etbl` | Evolution extended: allocations, GL segments/budgets, lots, units of measure, price lists, remittances, tax, warehouses/IBT, requisitions | `_etblAccBlnc`, `_etblLotTracking`, `_etblUnits`, `_etblPriceListPrices`, `_etblWhseIBT`, `_etblPOPRequisitions` |
| `_btbl` | Business modules: Fixed Assets (`_btblFA*`), Contact Management events/workflow (`_btblCM*`), Job Costing (`_btblJC*`), journal/cashbook batches (`_btblJr*`, `_btblCb*`), inventory counts, **invoice lines**, POS, Tax Manager (`_btblTM*`) | `_btblInvoiceLines`, `_btblJCMaster`, `_btblFAAsset`, `_btblJrBatches` |
| `_rtbl` | Contact Management / CRM: agents, incidents, knowledge base, opportunities, contracts, people, UDF dictionary | `_rtblAgents`, `_rtblIncidents`, `_rtblPeople`, `_rtblUserDict` |
| `_ret` | Retail Point of Sale | `_retPOSTransaction`, `_retTill` |
| `_mtbl` | Municipal Billing (undocumented in Evolution's browser) | `_mtblMeters`, `_mtblTransactions` |
| `_atbl` | Application metadata/tooling: import/export templates, bulk e-mail, Evolution's table/column dictionary | `_atblTables`, `_atblColumns` |
| `_dtbl` | Delivery Management | `_dtblDeliveryNote` |
| `_smtbl`, `_simtbl`, `_iotbl`, `RFQ_`, `WHT_`, `PR_`, `NT_` | Add-on modules present in this database (service management, requisitions/stock issues, reorder, request-for-quotation, withholding tax, vouchers, supplier audit). Names inferred from the tables; not every site has them | `_smtblServiceRequest`, `RFQ_RecordTender`, `WHT_Batch` |
| `_as_`, `Thyme_`, `*20250825`, `*_20260417` | **Site-specific**: custom integration tables and dated snapshot copies of standard tables. Not Evolution; never report on them as if they were | `_as_IntegrationLog_Granite`, `Accounts20250825` |

`INDEX.md` has the group → file map; grep `^## ` in `dict/` for the table list.

## 3. Column naming

- **Newer tables use Hungarian prefixes** (observed over 15,400 columns): `i` int (`iAgentID`), `c` char/varchar
  (`cDescription`), `b` bit (`bIsSerialItem`), `f` float (`fQuantity`), `d` datetime (`dTimeStamp`), `id` identity
  primary key (`idInvoiceLines`), `x` xml (`xAttribute`), `dt` datetime, `uc`/`ul`/`uf` user-defined-field columns.
- **Core tables use plain names** inherited from Pastel (`Account`, `Name`, `Debit`, `Credit`, `TxDate`, `InvNumber`,
  `DocType`) and the historic key names in § 4.
- **Audit columns** on many tables: `<Table>_dCreatedDate`, `<Table>_dModifiedDate`, `<Table>_iCreatedAgentID`,
  `<Table>_iModifiedAgentID`, `<Table>_iBranchID`, `<Table>_iChangeSetID`, `<Table>_Checksum` (e.g. `PostGL_dCreatedDate`).
- **User-defined fields** are added to the table they belong to with `uc`/`ul`/`uf`-style prefixed names and are
  catalogued in `_rtblUserDict`. Evolution's browser note on that table says which table each UDF group lives on:
  Customers → `Client`, Suppliers → `Vendor`, Inventory items → `StkItem`, Inventory documents → `InvNum`,
  General Ledger → `Accounts`, Employees → `EmplMain`, Fixed Assets → `_btblFAAssets`, Job Cards → `_btblJCMaster`,
  Incidents → `_rtblIncidents`, Contracts → `_rtblContracts`, People → `_rtblPeople` (that note names `EmplMain` and
  `_btblFAAssets`, which do not exist in the scripted database - the asset table there is `_btblFAAsset`). UDF
  columns are site-specific: read them from the client's `sys.columns`, never assume them.

## 4. Keys and joins (no declared foreign keys)

Evolution declares a primary key on almost every table but **no foreign keys** on standard tables (the only 12 FKs are
in the RFQ add-on). Relationships follow naming. Primary keys of the tables most SQL touches:

| Table | PK (identity) | What it is |
|---|---|---|
| `Client` | `DCLink` | customer |
| `Vendor` | `DCLink` | supplier (separate numbering from `Client`) |
| `StkItem` | `StockLink` | inventory item |
| `Accounts` | `AccountLink` | GL account (`Master_Sub_Account` is the display code per the browser) |
| `InvNum` | `AutoIndex` | document header (invoices, orders, quotes, GRVs, purchase orders - all document types share this table; browser alias "Invoice", Freedom Name `DocumentHeader`) |
| `_btblInvoiceLines` | `idInvoiceLines` | document lines (Freedom Name `DocumentLines`) |
| `PostGL` | `AutoIdx` | GL transactions |
| `PostAR` / `PostAP` | `AutoIdx` | customer / supplier transactions |
| `PostST` | `AutoIdx` | inventory (stock) transactions |
| `WhseMst` / `WhseStk` | `WhseLink` / `IdWhseStk` | warehouses / item-per-warehouse |
| `TrCodes` | `idTrCodes` | transaction codes |
| `Project` | `ProjectLink` | projects |
| `_rtblAgents` | `idAgents` | Evolution users (agents) |
| `_etblPeriod` | `idPeriod` | accounting periods (not identity) |

Starter join map. Column pairs below exist in the scripted schema; the **meaning** column is Evolution's documented
behaviour where the browser notes say so, otherwise an inference from the names that must be confirmed on the client's
data before shipping (run the sanity query in § 6).

| From | To | On | Basis |
|---|---|---|---|
| `_btblInvoiceLines.iInvoiceID` | `InvNum.AutoIndex` | line → header | naming; confirm |
| `_btblInvoiceLines.iStockCodeID` | `StkItem.StockLink` | line → item | naming; confirm |
| `_btblInvoiceLines.iWarehouseID` | `WhseMst.WhseLink` | line → warehouse | naming; confirm |
| `InvNum.AccountID` | `Client.DCLink` **or** `Vendor.DCLink` | header → customer (sales documents) or supplier (purchase documents), decided by `InvNum.DocType` | naming; the DocType values that separate sales from purchase documents are not in this dictionary - confirm on the client's data |
| `PostGL.AccountLink` | `Accounts.AccountLink` | GL line → account | naming; confirm |
| `PostGL.TrCodeID`, `PostAR.TrCodeID`, `PostAP.TrCodeID`, `PostST.TrCodeID` | `TrCodes.idTrCodes` | transaction → transaction code | naming; confirm |
| `PostAR.AccountLink` | `Client.DCLink` | customer transaction → customer | naming; confirm |
| `PostAP.AccountLink` | `Vendor.DCLink` | supplier transaction → supplier | naming; confirm |
| `PostAR` / `PostAP` | `PostGL` | every AR/AP record has a matching GL record | **Evolution's own browser note** ("Records in this table should always have a link to the POSTGL table"); the linking column is not named in the note - confirm |
| `PostST.AccountLink` | `StkItem.StockLink` | stock transaction → item | naming; confirm |
| `PostST.WarehouseID` | `WhseMst.WhseLink` | stock transaction → warehouse | naming; confirm |
| `WhseStk.WHStockLink` / `WhseStk.WHWhseID` | `StkItem.StockLink` / `WhseMst.WhseLink` | item per warehouse | naming; confirm the column names in `dict/Core.md` |
| any `iAgentID` (45 tables) | `_rtblAgents.idAgents` | who did it | naming |
| any `iProjectID` (31 tables), `PostGL.Project` | `Project.ProjectLink` | project | naming; confirm |
| any `iCurrencyID` (30 tables) | `Currency.CurrencyLink` | currency | naming; confirm |
| any `iLotID` (14 tables) | `_etblLotTracking.idLotTracking` | lot | naming; confirm |
| any `iUnitsOfMeasure*ID` | `_etblUnits.idUnits` | unit of measure | naming; confirm |
| `Client.iAreasID`, `Vendor.iAreasID` | `Areas.idAreas` | area | naming; confirm |
| `Client.iClassID` / `Vendor.iClassID` | `CliClass.IdCliClass` / `VenClass.idVenClass` | customer / supplier group | naming; confirm |

Rules of thumb that follow from the schema:

- `Client` and `Vendor` are **separate tables with overlapping `DCLink` values**; never union them on `DCLink` without a
  type discriminator.
- One `InvNum` row is any document type; always filter on `DocType` (and usually `DocState`/`DocFlag`) and state in the
  delivered SQL which values you assumed and that they were confirmed on the client's data.
- Balance tables mirror masters one-to-one per Evolution's notes: `_etblAccBlnc` / `AccPrev` should hold one row per
  `Accounts` row.
- `PostGL` writes one row per account in the transaction code: Evolution's note gives the example that an `INV`
  transaction linked to `IS` produces 5 balancing rows. Do not sum `PostGL` by document without filtering the account.
- `_etblPostGLHist` holds archived `PostGL` rows (browser note "Archived postgl transactions"); include it when a
  report spans purged years.

## 5. Types, NULLs and defaults

- Types are plain SQL Server: `int`, `varchar(n)`, `bit`, `datetime`, `float`, with `nvarchar`, `bigint`, `decimal`,
  `xml`, `text`/`image` on a minority. Money is mostly `float` (`Debit`, `Credit`, `fUnitPriceExcl`) - round in output.
- **NULLs are allowed almost everywhere** (core master columns are `NULL`-able); wrap with `ISNULL()` in sums and
  comparisons. Columns created with a default are mostly `(0)`, `(1)`, `'0'` or `getdate()`; only two columns default to
  `'1900/01/01'`. There is no system-wide "empty date" sentinel in the schema - test for `IS NULL` and, where a client
  stores `1900-01-01`, for that value as well.
- `bit` flags are 0/1 (`bIsSerialItem`, `On_Hold`); some older flag columns are `int` or `char` (`ServiceItem`,
  `ItemActive` on `StkItem`) - check the type in `dict/` before writing `= 1` vs `= '1'`.
- `float` quantities on `_btblInvoiceLines` come in families: `fQuantity`, `fQtyToProcess`, `fQtyProcessed`,
  `fQtyReserved`, each with `…LineTotIncl/Excl/TaxAmount` totals; pick the family that matches the question
  (ordered vs. processed) and say which.

## 6. View-writing rules

1. `CREATE OR ALTER VIEW rpt.<name>` in a **reporting schema or separate database**, never in `dbo` of the company DB,
   and never any INSERT/UPDATE/DELETE/TRIGGER on Evolution tables - the SDK is the write path.
2. Verify every column in `dict/` and cite the file; verify a join's **meaning** (the "confirm" rows above) with a
   sanity query on the client's data before shipping, for example:

   ```sql
   -- confirm the line->header link and that every line resolves
   SELECT TOP 20 h.AutoIndex, h.InvNumber, h.DocType, l.idInvoiceLines, l.iStockCodeID
   FROM dbo.InvNum h
   JOIN dbo._btblInvoiceLines l ON l.iInvoiceID = h.AutoIndex
   ORDER BY h.AutoIndex DESC;
   SELECT COUNT(*) AS orphan_lines FROM dbo._btblInvoiceLines l
   WHERE NOT EXISTS (SELECT 1 FROM dbo.InvNum h WHERE h.AutoIndex = l.iInvoiceID);
   ```

3. Filter documents on `DocType` (and state flags) with values confirmed on the client's data, and say so.
4. `ISNULL()` numeric columns, `ROUND()` float money, and alias columns with business names.
5. Exclude site-specific and snapshot tables (§ 2) and user-defined columns unless the requirement names them.

## 7. Worked example - sales document lines with customer and item

```sql
CREATE OR ALTER VIEW rpt.SalesDocumentLines AS
SELECT  h.AutoIndex            AS DocumentID,
        h.DocType,                                   -- filter in the consumer once values are confirmed
        h.InvNumber            AS DocumentNumber,
        h.InvDate              AS DocumentDate,
        c.Account              AS CustomerCode,
        c.Name                 AS CustomerName,
        s.Code                 AS ItemCode,
        s.Description_1        AS ItemDescription,
        l.fQuantity            AS Quantity,
        ROUND(ISNULL(l.fUnitPriceExcl, 0), 2)              AS UnitPriceExcl,
        ROUND(ISNULL(l.fQuantityLineTotExcl, 0), 2)        AS LineTotalExcl,
        ROUND(ISNULL(l.fQuantityLineTaxAmount, 0), 2)      AS LineTax,
        w.Code                 AS WarehouseCode
FROM    dbo.InvNum h
JOIN    dbo._btblInvoiceLines l ON l.iInvoiceID   = h.AutoIndex      -- naming-based join, confirmed with § 6 query
JOIN    dbo.Client            c ON c.DCLink       = h.AccountID      -- valid for sales DocTypes only
LEFT JOIN dbo.StkItem         s ON s.StockLink    = l.iStockCodeID
LEFT JOIN dbo.WhseMst         w ON w.WhseLink     = l.iWarehouseID;
```

Every column above is in `dict/Core.md` (`InvNum`, `Client`, `StkItem`, `WhseMst`) and `dict/Business-modules.md`
(`_btblInvoiceLines`); the `Client` join is only correct for sales document types, so the consumer must filter
`DocType` to the values confirmed on the client's data.
