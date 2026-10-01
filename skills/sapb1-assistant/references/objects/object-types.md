<!-- source: https://sapbusinessone.in/list-of-object-types-sap-business-one.html (authoritative), cross-checked against https://sap-b1-blog.com/en/glossary/list-of-object-types-in-sap-business-one/ | version: not stated by either source (community lists, not SAP documentation) | verified: 2026-10-01 -->

# SAP Business One object types

326 object types, sorted by object type number. One line per object: grep `^| 17 |` for a number, or the table name / description for the reverse.

- **Table** = the SAP B1 table for the object. **Primary Key** = the column name(s) as written by the source.
- **Src** = ids of the sources carrying the row (`in` = sapbusinessone.in, `blog` = sap-b1-blog.com; URLs in `INDEX.md`). Multi-source rows agree on the object number.
- Table, description and primary key come from sapbusinessone.in, which uses the real database column names. The blog page is machine-translated and carries corrupted table names; every table-name disagreement is flagged in Notes.
- Table `ODRF` appears under two object numbers (112 Drafts, 1179 Stock Transfer Draft) in both sources.
- Neither source is SAP documentation and neither states a B1 version. Before relying on a number in code (DI API, UDO registration, Service Layer), confirm it against SAP's own reference for the client's version.

| ObjType | Table | Description | Primary Key | Src | Notes |
|---|---|---|---|---|---|
| 1 | OACT | G/L Accounts | AcctCode | in,blog |  |
| 2 | OCRD | Business Partner | CardCode | in,blog |  |
| 3 | ODSC | Bank Codes | AbsEntry | in,blog |  |
| 4 | OITM | Items | ItemCode | in,blog |  |
| 5 | OVTG | Tax Definition | Code | in,blog |  |
| 6 | OPLN | Price Lists | ListNum | in,blog |  |
| 7 | OSPP | Special Prices | CardCode, ItemCode | in,blog |  |
| 8 | OITG | Item Properties | ItmsTypCod | in,blog |  |
| 9 | ORTM | Rate Differences | LineNum, IsSysCurr | in,blog |  |
| 10 | OCRG | Card Groups | GroupCode | in,blog |  |
| 11 | OCPR | Contact Persons | CntctCode | in,blog |  |
| 12 | OUSR | Users | USERID | in,blog |  |
| 13 | OINV | A/R Invoice | DocEntry | in,blog |  |
| 14 | ORIN | A/R Credit Memo | DocEntry | in,blog |  |
| 15 | ODLN | Delivery | DocEntry | in,blog |  |
| 16 | ORDN | Returns | DocEntry | in,blog | blog gives `ORDER` (translation error) |
| 17 | ORDR | Sales Order | DocEntry | in,blog |  |
| 18 | OPCH | A/P Invoice | DocEntry | in,blog |  |
| 19 | ORPC | A/P Credit Memo | DocEntry | in,blog |  |
| 20 | OPDN | Goods Receipt PO | DocEntry | in,blog |  |
| 21 | ORPD | Goods Return | DocEntry | in,blog |  |
| 22 | OPOR | Purchase Order | DocEntry | in,blog |  |
| 23 | OQUT | Sales Quotation | DocEntry | in,blog |  |
| 24 | ORCT | Incoming Payment | DocEntry | in,blog |  |
| 25 | ODPS | Deposit | DeposId | in,blog |  |
| 26 | OMTH | Reconciliation History | MthAcctCod, IsInternal, MatchNum | in,blog |  |
| 27 | OCHH | Check Register | CheckKey | in,blog | blog gives `OHH` (translation error) |
| 28 | OBTF | Journal Voucher Entry | BatchNum, TransId | in,blog |  |
| 29 | OBTD | Journal Vouchers List | BatchNum | in,blog |  |
| 30 | OJDT | Journal Entry | TransId | in,blog |  |
| 31 | OITW | Items - Warehouse | ItemCode, WhsCode | in,blog |  |
| 32 | OADP | Print Preferences | PrintId | in,blog |  |
| 33 | OCLG | Activities | ClgCode | in,blog |  |
| 34 | ORCR | Recurring Postings | RcurCode, Instance | in,blog |  |
| 35 | ONNM | Document Numbering | ObjectCode, DocSubType | in,blog |  |
| 36 | OCRC | Credit Cards | CreditCard | in,blog |  |
| 37 | OCRN | Currency Codes | CurrCode | in,blog |  |
| 38 | OIDX | CPI Codes | IdexCode | in,blog |  |
| 39 | OADM | Administration | Code | in,blog |  |
| 40 | OCTG | Payment Terms | GroupNum | in,blog |  |
| 41 | OPRF | Preferences | FormNumber, UserSign | in,blog |  |
| 42 | OBNK | External Bank Statement Received | AcctCode, Sequence | in,blog |  |
| 43 | OMRC | Manufacturers | FirmCode | in,blog |  |
| 44 | OCQG | Card Properties | GroupCode | in,blog |  |
| 45 | OTRC | Journal Entry Codes | TrnsCode | in,blog |  |
| 46 | OVPM | Outgoing Payments | DocEntry | in,blog |  |
| 47 | OSRL | Serial Numbers | ItemCode, SerialNum | in,blog |  |
| 48 | OALC | Loading Expenses | AlcCode | in,blog |  |
| 49 | OSHP | Delivery Types | TrnspCode | in,blog |  |
| 50 | OLGT | Length Units | UnitCode | in,blog |  |
| 51 | OWGT | Weight Units | UnitCode | in,blog |  |
| 52 | OITB | Item Groups | ItmsGrpCod | in,blog |  |
| 53 | OSLP | Sales Employee | SlpCode | in,blog |  |
| 54 | OFLT | Report - Selection Criteria | FormNum, UserSign, FilterName | in,blog |  |
| 55 | OTRT | Posting Templates | TrtCode | in,blog |  |
| 56 | OARG | Customs Groups | CstGrpCode | in,blog |  |
| 57 | OCHO | Checks for Payment | CheckKey | in,blog |  |
| 58 | OINM | Whse Journal | TransNum, Instance | in,blog |  |
| 59 | OIGN | Goods Receipt | DocEntry | in,blog |  |
| 60 | OIGE | Goods Issue | DocEntry | in,blog |  |
| 61 | OPRC | Cost Center | PrcCode | in,blog |  |
| 62 | OOCR | Cost Rate | OcrCode | in,blog |  |
| 63 | OPRJ | Project Codes | PrjCode | in,blog |  |
| 64 | OWHS | Warehouses | WhsCode | in,blog |  |
| 65 | OCOG | Commission Groups | GroupCode | in,blog |  |
| 66 | OITT | Product Tree | Code | in,blog |  |
| 67 | OWTR | Inventory Transfer | DocEntry | in,blog |  |
| 68 | OWKO | Production Instructions | OrderNum | in,blog |  |
| 69 | OIPF | Landed Costs | DocEntry | in,blog |  |
| 70 | OCRP | Payment Methods | CrTypeCode | in,blog |  |
| 71 | OCDT | Credit Card Payment | Code | in,blog |  |
| 72 | OCRH | Credit Card Management | AbsId, Instance | in,blog |  |
| 73 | OSCN | Customer/Vendor Cat. No. | ItemCode, CardCode, Substitute | in,blog |  |
| 74 | OCRV | Credit Payments | AbsId, PayId, Instance | in,blog |  |
| 75 | ORTT | CPI and FC Rates | RateDate, Currency | in,blog |  |
| 76 | ODPT | Postdated Deposit | DeposId | in,blog |  |
| 77 | OBGT | Budget | AbsId | in,blog |  |
| 78 | OBGD | Budget Cost Assess. Mthd | BgdCode | in,blog |  |
| 79 | ORCN | Retail Chains | ChainCode | in,blog |  |
| 80 | OALT | Alerts Template | Code | in,blog |  |
| 81 | OALR | Alerts | Code | in,blog |  |
| 82 | OAIB | Received Alerts | AlertCode, UserSign | in,blog |  |
| 83 | OAOB | Message Sent | AlertCode, UserSign | in,blog |  |
| 84 | OCLS | Activity Subjects | Code | in,blog |  |
| 85 | OSPG | Special Prices for Groups | CardCode, ObjType, ObjKey | in,blog |  |
| 86 | SPRG | Application Start | LineNum, UserCode | in,blog |  |
| 87 | OMLS | Distribution List | Code | in,blog |  |
| 88 | OENT | Shipping Types | DocEntry | in,blog |  |
| 89 | OSAL | Outgoing | DocEntry | in,blog |  |
| 90 | OTRA | Transition | DocEntry | in,blog |  |
| 91 | OBGS | Budget Scenario | AbsId | in,blog |  |
| 92 | OIRT | Interest Prices | Numerator | in,blog |  |
| 93 | OUDG | User Defaults | Code | in,blog |  |
| 94 | OSRI | Serial Numbers for Items | ItemCode, SysSerial | in,blog |  |
| 95 | OFRT | Financial Report Templates | AbsId | in,blog |  |
| 96 | OFRC | Financial Report Categories | TemplateId, CatId | in,blog |  |
| 97 | OOPR | Opportunity | OpprId | in,blog |  |
| 98 | OOIN | Interest | Num | in,blog |  |
| 99 | OOIR | Interest Level | Num | in,blog |  |
| 100 | OOSR | Information Source | Num | in,blog |  |
| 101 | OOST | Opportunity Stage | Num | in,blog |  |
| 102 | OOFR | Defect Cause | Num | in,blog |  |
| 103 | OCLT | Activity Types | Code | in,blog |  |
| 104 | OCLO | Meetings Location | Code | in,blog |  |
| 105 | OISR | Service Calls | RequestNum | in,blog |  |
| 106 | OIBT | Batch No. for Item | ItemCode, BatchNum, WhsCode | in,blog |  |
| 107 | OALI | Alternative Items 2 | OrigItem, AltItem | in,blog |  |
| 108 | OPRT | Partners | PrtId | in,blog |  |
| 109 | OCMT | Competitors | CompetId | in,blog |  |
| 110 | OUVV | User Validations | IndexID, LineNum | in,blog |  |
| 111 | OFPR | Posting Period | AbsEntry | in,blog |  |
| 112 | ODRF | Drafts | DocEntry | in,blog |  |
| 113 | OSRD | Batches and Serial Numbers | ItemCode, DocType, DocEntry, DocLineNum | in,blog |  |
| 114 | OUDC | User Display Cat. | CodeID | in,blog |  |
| 115 | OPVL | Lender - Pelecard | Code | in,blog |  |
| 116 | ODDT | Withholding Tax Deduction Hierarchy | Numerator | in,blog |  |
| 117 | ODDG | Withholding Tax Deduction Groups | Numerator | in,blog |  |
| 118 | OUBR | Branches | Code | in,blog |  |
| 119 | OUDP | Departments | Code | in,blog |  |
| 120 | OWST | Confirmation Level | WstCode | in,blog |  |
| 121 | OWTM | Approval Templates | WtmCode | in,blog |  |
| 122 | OWDD | Docs. for Confirmation | WddCode | in,blog |  |
| 123 | OCHD | Checks for Payment Drafts | CheckKey | in,blog |  |
| 124 | CINF | Company Info | Version | in,blog |  |
| 125 | OEXD | Freight Setup | ExpnsCode | in,blog |  |
| 126 | OSTA | Sales Tax Authorities | Code, Type | in,blog |  |
| 127 | OSTT | Sales Tax Authorities Type | AbsId | in,blog | blog gives `OST` (translation error) |
| 128 | OSTC | Sales Tax Codes | Code | in,blog |  |
| 129 | OCRY | Countries | Code | in,blog |  |
| 130 | OCST | States | Country, Code | in,blog |  |
| 131 | OADF | Address Formats | Code | in,blog |  |
| 132 | OCIN | A/R Correction Invoice | DocEntry | in,blog |  |
| 133 | OCDC | Cash Discount | Code | in,blog |  |
| 134 | OQCN | Query Catagories | CategoryId | in,blog |  |
| 135 | OIND | Triangular Deal | Code | in,blog |  |
| 136 | ODMW | Data Migration | Code | in,blog |  |
| 137 | OCSTN | Workstation ID | Code | in,blog |  |
| 138 | OIDC | Indicator | Code | in,blog |  |
| 139 | OGSP | Goods Shipment | Code | in,blog |  |
| 140 | OPDF | Payment Draft | DocEntry | in,blog |  |
| 141 | OQWZ | Query Wizard | Code | in,blog |  |
| 142 | OASG | Account Segmentation | AbsId | in,blog |  |
| 143 | OASC | Account Segmentation Categories | SegmentId, Code | in,blog | blog gives `OSC` (translation error) |
| 144 | OLCT | Location | Code | in,blog |  |
| 145 | OTNN | 1099 Forms | FormCode | in,blog |  |
| 146 | OCYC | Cycle | Code | in,blog |  |
| 147 | OPYM | Payment Methods for Payment Wizard | PayMethCod | in,blog |  |
| 148 | OTOB | 1099 Opening Balance | VendCode, Form1099, Box1099 | in,blog |  |
| 149 | ORIT | Dunning Interest Rate | Code | in,blog |  |
| 150 | OBPP | BP Priorities | PrioCode | in,blog |  |
| 151 | ODUN | Dunning Letters | LineNum | in,blog |  |
| 152 | CUFD | User Fields - Description | TableID, FieldID | in,blog |  |
| 153 | OUTB | User Tables | TableName | in,blog |  |
| 154 | OCUMI | My Menu Items | UserSign , Id_ | in,blog |  |
| 155 | OPYD | Payment Run | Code | in,blog |  |
| 156 | OPKL | Pick List | AbsEntry | in,blog |  |
| 157 | OPWZ | Payment Wizard | IdNumber | in,blog |  |
| 158 | OPEX | Payment Results Table | AbsEntry | in,blog |  |
| 159 | OPYB | Payment Block | AbsEntry | in,blog |  |
| 160 | OUQR | Queries | IntrnalKey, Qcategory | in,blog |  |
| 161 | OCBI | Central Bank Ind. | Indicator | in,blog |  |
| 162 | OMRV | Inventory Revaluation | DocEntry | in,blog |  |
| 163 | OCPI | A/P Correction Invoice | DocEntry | in,blog |  |
| 164 | OCPV | A/P Correction Invoice Reversal | DocEntry | in,blog |  |
| 165 | OCSI | A/R Correction Invoice | DocEntry | in,blog |  |
| 166 | OCSV | A/R Correction Invoice Reversal | DocEntry | in,blog |  |
| 167 | OSCS | Service Call Statuses | statusID | in,blog |  |
| 168 | OSCT | Service Call Types | callTypeID | in,blog |  |
| 169 | OSCP | Service Call Problem Types | prblmTypID | in,blog |  |
| 170 | OCTT | Contract Template | TmpltName | in,blog |  |
| 171 | OHEM | Employees | empID | in,blog |  |
| 172 | OHTY | Employee Types | typeID | in,blog |  |
| 173 | OHST | Employee Status | statusID | in,blog |  |
| 174 | OHTR | Termination Reason | reasonID | in,blog |  |
| 175 | OHED | Education Types | edType | in,blog |  |
| 176 | OINS | Customer Equipment Card | insID | in,blog |  |
| 177 | OAGP | Agent Name | AgentCode | in,blog |  |
| 178 | OWHT | Withholding Tax | WTCode | in,blog |  |
| 179 | ORFL | Already Displayed 347, 349 and WTax Reports | DocEntry, ReportType, DocType, LineNum, TaxCode, OrdinalNum | in,blog |  |
| 180 | OVTR | Tax Report | AbsEntry | in,blog |  |
| 181 | OBOE | Bill of Exchange for Payment | BoeKey | in,blog |  |
| 182 | OBOT | Bill Of Exchang Transaction | AbsEntry | in,blog |  |
| 183 | OFRM | File Format | AbsEntry | in,blog |  |
| 184 | OPID | Period Indicator | Indicator | in,blog |  |
| 185 | ODOR | Doubtful Debts | AbsEntry | in,blog |  |
| 186 | OHLD | Holiday Table | HldCode | in,blog |  |
| 187 | OCRB | BP - Bank Account | Country, BankCode, Account, CardCode | in,blog |  |
| 188 | OSST | Service Call Solution Statuses | Number | in,blog |  |
| 189 | OSLT | Service Call Solutions | SltCode | in,blog |  |
| 190 | OCTR | Service Contracts | ContractID | in,blog |  |
| 191 | OSCL | Service Calls | callID | in,blog |  |
| 192 | OSCO | Service Call Origins | originID | in,blog |  |
| 193 | OUKD | User Key Description | TableName, KeyId | in,blog |  |
| 194 | OQUE | Queue | queueID | in,blog |  |
| 195 | OIWZ | Inflation Wizard | AbsEntry | in,blog |  |
| 196 | ODUT | Dunning Terms | TermCode | in,blog |  |
| 197 | ODWZ | Dunning Wizard | WizardId | in,blog |  |
| 198 | OFCT | Sales Forecast | AbsID | in,blog |  |
| 199 | OMSN | MRP Scenarios | AbsEntry | in,blog |  |
| 200 | OTER | Territories | territryID | in,blog |  |
| 201 | OOND | Industries | IndCode | in,blog |  |
| 202 | OWOR | Production Order | DocEntry | in,blog |  |
| 203 | ODPI | A/R Down Payment | DocEntry | in,blog |  |
| 204 | ODPO | A/P Down Payment | DocEntry | in,blog |  |
| 205 | OPKG | Package Types | PkgCode | in,blog |  |
| 206 | OUDO | User-Defined Object | Code | in,blog |  |
| 207 | ODOW | Data Ownership - Objects | Object, SubObject | in,blog |  |
| 208 | ODOX | Data Ownership - Exceptions | QueryId, Object, SubObject | in,blog |  |
| 209 |  |  |  | in | no data in source |
| 210 | OHPS | Employee Position | posID | in,blog |  |
| 211 | OHTM | Employee Teams | teamID | in,blog |  |
| 212 | OORL | Relationships | OrlCode | in,blog |  |
| 213 | ORCM | Recommendation Data | DocEntry | in,blog |  |
| 214 | OUPT | User Autorization Tree | AbsId | in,blog |  |
| 215 | OPDT | Predefined Text | AbsEntry | in,blog |  |
| 216 | OBOX | Box Definition | BoxCode, ReportType, BosCode | in,blog |  |
| 217 | OCLA | Activity Status | statusID | in,blog |  |
| 218 | OCHF | 312 | ObjName | in,blog |  |
| 219 | OCSHS | User-Defined Values | IndexID | in,blog |  |
| 220 | OACP | Periods Category | AbsEntry | in,blog |  |
| 221 | OATC | Attachments | AbsEntry | in,blog |  |
| 222 | OGFL | Grid Filter | FormID, GridID, UserCode | in,blog |  |
| 223 | OLNG | User Language Table | Code | in,blog |  |
| 224 | OMLT | Multi-Language Translation | TranEntry | in,blog |  |
| 225 | OAPA3 |  |  | in | description blank in source; primary key blank in source |
| 226 | OAPA4 |  |  | in | description blank in source; primary key blank in source |
| 227 | OAPA5 |  |  | in | description blank in source; primary key blank in source |
| 229 | SDIS | Dynamic Interface (Strings) | FormId, ItemId, ColumnId, Language | in,blog |  |
| 230 | OSVR | Saved Reconciliations | acctCode | in,blog |  |
| 231 | DSC1 | House Bank Accounts | AbsEntry | in,blog |  |
| 232 | RDOC | Document | DocCode | in,blog |  |
| 233 | ODGP | Document Generation Parameter Sets | AbsEntry | in,blog |  |
| 234 | OMHD | #740 | AlertCode | in,blog |  |
| 238 | OACG | Account Category | AbsId | in,blog |  |
| 239 | OBCA | Bank Charges Allocation Codes | Code | in,blog |  |
| 241 | OCFT | Cash Flow Transactions - Rows | CFTId | in,blog |  |
| 242 | OCFW | Cash Flow Line Item | CFWId | in,blog |  |
| 247 | OBPL | Business Place | BPLId | in,blog |  |
| 250 | OJPE | Local Era Calendar | Code | in,blog |  |
| 251 | ODIM | Cost Accounting Dimension | DimCode | in,blog |  |
| 254 | OSCD | Service Code Table | AbsEntry | in,blog |  |
| 255 | OSGP | Service Group for Brazil | AbsEntry | in,blog |  |
| 256 | OMGP | Material Group | AbsEntry | in,blog |  |
| 257 | ONCM | NCM Code | AbsEntry | in,blog |  |
| 258 | OCFP | CFOP for Nota Fiscal | ID | in,blog |  |
| 259 | OTSC | CST Code for Nota Fiscal | ID | in,blog |  |
| 260 | OUSG | Usage of Nota Fiscal | ID | in,blog |  |
| 261 | OCDP | Closing Date Procedure | ClsDateNum | in,blog |  |
| 263 | ONFN | Nota Fiscal Numbering | ObjectCode, DocSubType | in,blog |  |
| 264 | ONFT | Nota Fiscal Tax Category (Brazil) | AbsId | in,blog |  |
| 265 | OCNT | Counties | AbsId | in,blog |  |
| 266 | OTCD | Tax Code Determination | AbsId | in,blog | blog gives `OTC` (translation error) |
| 267 | ODTY | BoE Document Type | AbsEntry | in,blog |  |
| 268 | OPTF | BoE Portfolio | AbsEntry | in,blog |  |
| 269 | OIST | BoE Instruction | AbsEntry | in,blog |  |
| 271 | OTPS | Tax Parameter | AbsId | in,blog |  |
| 275 | OTFC | Tax Type Combination | AbsId | in,blog |  |
| 276 | OFML | Tax Formula Master Table | AbsId | in,blog |  |
| 278 | OCNA | CNAE Code | AbsId | in,blog |  |
| 280 | OTSI | Sales Tax Invoice | DocEntry | in,blog |  |
| 281 | OTPI | Purchase Tax Invoice | DocEntry | in,blog |  |
| 283 | OCCD | Cargo Customs Declaration Numbers | CCDNum | in,blog |  |
| 290 | ORSC | Resources | ResCode | in,blog |  |
| 291 | ORSG | Resource Properties | ResTypCod | in,blog |  |
| 292 | ORSB | ResGrpCod | ResGrpCod | in,blog |  |
| 300 |  | RecordSet |  | in | table unnamed in source; primary key blank in source |
| 305 |  | Bridge |  | in | table unnamed in source; primary key blank in source |
| 321 | OITR | Internal Reconciliation | ReconNum | in,blog |  |
| 541 | OPOS | POS Master Data | EquipNo | in,blog |  |
| 1179 | ODRF | Stock Transfer Draft | DocEntry | in,blog |  |
| 10000044 | OBTN | Batch Numbers Master Data | AbsEntry | in,blog |  |
| 10000045 | OSRN | Serial Numbers Master Data | AbsEntry | in,blog |  |
| 10000062 | OIVK | IVL Vs OINM Keys | TransSeq | in,blog |  |
| 10000071 | OIQR | Inventory Posting | DocEntry | in,blog |  |
| 10000073 | OFYM | Financial Year Master | AbsId | in,blog |  |
| 10000074 | OSEC | Sections | AbsId | in,blog |  |
| 10000075 | OCSN | Certificate Series | AbsId | in,blog |  |
| 10000077 | ONOA | Nature of Assessee | AbsId | in,blog |  |
| 10000105 | OMSG | Messaging Service Settings | USERID | in,blog |  |
| 10000196 | RTYP | Document Type List | CODE | in,blog | blog gives `TYPE` (translation error) |
| 10000197 | OUGP | UoM Group | UgpEntry | in,blog |  |
| 10000199 | OUOM | UoM Master Data | UomEntry | in,blog |  |
| 10000203 | OBFC | Bin Field Configuration | AbsEntry | in,blog |  |
| 10000204 | OBAT | Bin Location Attribute | AbsEntry | in,blog |  |
| 10000205 | OBSL | Warehouse Sublevel | AbsEntry | in,blog |  |
| 10000206 | OBIN | Bin Location | AbsEntry | in,blog | blog gives `WHETHER IN` (translation error) |
| 140000041 | ODNF | DNF Code | AbsEntry | in,blog |  |
| 231000000 | OUGR | Authorization Group | GroupId | in,blog |  |
| 234000004 | OEGP | E-Mail Group | EmlGrpCode | in,blog |  |
| 243000001 | OGPC | Government Payment Code | AbsId | in,blog |  |
| 310000001 | OIQI | Inventory Opening Balance | DocEntry | in,blog |  |
| 310000008 | OBTW | Batch Attributes in Location | AbsEntry | in,blog |  |
| 410000005 | OLLF | Legal List Format | AbsEntry | in,blog |  |
| 480000001 | OHET | Object: HR Employee Transfer | TransferID | in,blog |  |
| 540000005 | OTCX | Tax Code Determination | DocEntry | in,blog |  |
| 540000006 | OPQT | Purchase Quotation | DocEntry | in,blog |  |
| 540000040 | ORCP | Recurring Transaction Template | AbsEntry | in,blog |  |
| 540000042 | OCCT | Cost Center Type | CctCode | in,blog |  |
| 540000048 | OACR | Accrual Type | Code | in,blog |  |
| 540000056 | ONFM | Nota Fiscal Model | AbsEntry | in,blog |  |
| 540000067 | OBFI | Brazil Fuel Indexer | ID | in,blog |  |
| 540000068 | OBBI | Brazil Beverage Indexer | ID | in,blog |  |
| 1210000000 | OCPT | Cockpit Main Table | AbsEntry | in,blog |  |
| 1250000001 | OWTQ | Inventory Transfer Request | DocEntry | in,blog |  |
| 1250000025 | OOAT | Blanket Agreement | AbsID | in,blog |  |
| 1320000000 | OKPI | Key Performance Indicator Package | AbsEntry | in,blog |  |
| 1320000002 | OTGG | Target Group | TargetCode | in,blog |  |
| 1320000012 | OCPN | Campaign | CpnNo | in,blog |  |
| 1320000028 | OROC | Retorno Operation Codes | AbsEntry | in,blog |  |
| 1320000039 | OPSC | Product Source Code | Code | in,blog |  |
| 1470000000 | ODTP | Fixed Assets Depreciation Types | Code | in,blog |  |
| 1470000002 | OADT | Fixed Assets Account Determination | Code | in,blog | blog gives `OADDT` (translation error) |
| 1470000003 | ODPA | Fixed Asset Depreciation Areas | Code | in,blog |  |
| 1470000004 | ODPP | Depreciation Type Pools | Code | in,blog |  |
| 1470000032 | OACS | Asset Classes | Code | in,blog |  |
| 1470000046 | OAGS | Asset Groups | Code | in,blog |  |
| 1470000048 | ODMC | G/L Account Determination Criteria - Inventory | DmcId | in,blog |  |
| 1470000049 | OACQ | Capitalization | DocEntry | in,blog |  |
| 1470000057 | OGAR | G/L Account Advanced Rules | AbsEntry | in,blog |  |
| 1470000060 | OACD | Credit Memo | DocEntry | in,blog |  |
| 1470000062 | OBCD | Bar Code Master Data | BcdEntry | in,blog |  |
| 1470000065 | OINC | Inventory Counting | DocEntry | in,blog |  |
| 1470000077 | OEDG | Discount Groups | AbsEntry | in,blog |  |
| 1470000092 | OCCS | Cycle Count Determination | WhsCode | in,blog |  |
| 1470000113 | OPRQ | Purchase Request | DocEntry | in,blog |  |
| 1620000000 | OWLS | Workflow - Task Details | TaskID | in,blog |  |
