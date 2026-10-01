<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->

# POR6 - Purchase Order - Installments
Module: Marketing Documents | 65 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, InstlmntID
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPOR
  InstlmntID Int(6) Installment ID default=1
  ObjType nVarChar(20) Object Type default=22 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DueDate Date(8) Due Date
  Status VarChar(1) Installment Status default=O [O=Open, C=Closed]
  DunnLevel Int(11) Dunning Level default=0
  InsTotal Num(19,6) Total Installment
  InsTotalFC Num(19,6) Total Installment (FC)
  InsTotalSy Num(19,6) Total Installment (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  VatSum Num(19,6) Total Tax
  VatSumFC Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  VatPaid Num(19,6) Tax Paid to Date
  VatPaidFC Num(19,6) Tax Paid (FC)
  VatPaidSys Num(19,6) Tax Paid (SC)
  TotalExpns Num(19,6) Total Freight Charges
  TotalExpFC Num(19,6) Total Freight Charges (FC)
  TotalExpSC Num(19,6) Total Freight Charges (SC)
  ExpAppl Num(19,6) Applied Freight Charges
  ExpApplFC Num(19,6) Applied Freight Charges (FC)
  ExpApplSC Num(19,6) Applied Freight Charges (SC)
  WTSum Num(19,6) WTax Amount
  WTSumFC Num(19,6) WTax Amount (FC)
  WTSumSC Num(19,6) WTax Amount (SC)
  WTApplied Num(19,6) Applied WTax
  WTAppliedF Num(19,6) Applied WTax (FC)
  WTAppliedS Num(19,6) Applied WTax (SC)
  TotalBlck Num(19,6) Total Reserved Amount
  TotalBlckF Num(19,6) Total Reserved Amount (FC)
  TotalBlckS Num(19,6) Total Reserved Amount (SC)
  VATBlck Num(19,6) Reserved Tax
  VATBlckFC Num(19,6) Reserved Tax (FC)
  VATBlckSC Num(19,6) Reserved Tax (SC)
  ExpnsBlck Num(19,6) Reserved Freight Charges
  ExpnsBlckF Num(19,6) Reserved Freight Charges (FC)
  ExpnsBlckS Num(19,6) Reserved Freight Charges (SC)
  WTBlocked Num(19,6) Reserved WTax Amount
  WTBlockedF Num(19,6) Reserved WTax Amount (FC)
  WTBlockedS Num(19,6) Reserved WTax Amount (SC)
  InstPrcnt Num(19,6) Installment %
  DunWizBlck VarChar(1) Wizard dunning block default=N [N=No, Y=Yes]
  DunDate Date(8) Last Dunning Date
  Paid Num(19,6) Paid
  PaidFrgn Num(19,6) Paid (FC)
  PaidSc Num(19,6) Paid (SC)
  reserved VarChar(1) Reserved default=N [N=No, Y=Yes]
  TaxOnExp Num(19,6) Tax on Expenses
  TaxOnExpFc Num(19,6) Tax on Expenses (FC)
  TaxOnExpSc Num(19,6) Tax on Expenses (SC)
  TaxOnExpAp Num(19,6) Applied Tax on Expenses
  TaxOnExApF Num(19,6) Applied Tax on Expenses (FC)
  TaxOnExApS Num(19,6) Applied Tax on Expenses (SC)
  TaxOnExBlo Num(19,6) Reserved Tax on Freight Amount
  TaxOnExBlF Num(19,6) Reserved Tax on Freight Amt FC
  TaxOnExBlS Num(19,6) Reserved Tax on Freight Amt SC
  LvlUpdDate Date(8) Dunning Level Update Date
  Ordered VarChar(1) Payment Ordered default=N [Y=Yes, N=No]
  PaidDpm Num(19,6) Paid by Down Payment
  PaidDpmFc Num(19,6) Paid by Down Payment (FC)
  PaidDpmSc Num(19,6) Paid by Down Payment (SC)
  EncryptIV nVarChar(100) Encrypt IV

# POR7 - Delivery Packages - Purchase Order
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPOR
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type default=22 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV

# POR8 - Items in Package - Purchase Order
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum, ItemCode, UomEntry, NumPerMsr
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPOR
  PackageNum Int(11) Package Number
  ItemCode nVarChar(50) Item Code ->OITM
  Quantity Num(19,6) Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=22 ->ADP1
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value default=0

# POR9 - Purchase Order - Drawn Dpm
Module: Marketing Documents | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPOR
  LineNum Int(11) Row Number
  BaseAbs Int(11) Base Document Internal ID
  BaseLine Int(11) Base Document Row
  TargetBase VarChar(1) Target or Base Document default=B [B=Base, T=Target]
  ObjType nVarChar(20) Base Object Type
  DrawnSum Num(19,6) Net LC
  DrawnSumFc Num(19,6) Net FC
  DrawnSumSc Num(19,6) Net SC
  LogInstanc Int(11) Log Instance default=0
  ObjCode nVarChar(20) Object Type default=22 ->ADP1
  ApplDrawn Num(19,6) Applied Net LC
  ApplDrawnF Num(19,6) Applied Net FC
  ApplDrawnS Num(19,6) Applied Net SC
  BaseDocNum Int(11) Base Document Number
  BsDocDate Date(8) Base Posting Date
  BsDueDate Date(8) Base Due Date
  BsCardName nVarChar(100) Base BP Name
  BsComments nVarChar(254) Base Remarks
  Posted VarChar(1) Base Document Posted default=Y [Y=Yes, N=No]
  Vat Num(19,6) Tax LC
  VatFc Num(19,6) Tax FC
  VatSc Num(19,6) Tax SC
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  IsGross VarChar(1) Is Gross Line default=N [N=Net Line, Y=Gross Line]

# PQT1 - Purchase Quotation - Rows
Module: Marketing Documents | 317 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  STATUS: LineStatus
  CURRENCY: Currency
  ACCOUNT: AcctCode
  BASE_ENTRY: BaseEntry, BaseType, BaseLine
  VIS_ORDER: DocEntry, VisOrder
  OWNER_CODE: OwnerCode
  ITM_WHS_OQ: ItemCode, WhsCode, OpenQty
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OPQT
  LineNum Int(11) Row Number
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=, 20=Goods Receipt, 18=A/P Invoice, 22=Purchase Order, 204=A/P Down Payment]
  TrgetEntry Int(11) Target Document Internal ID
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 17=Sales Order, 1470000113=Purchase Request, 23=Sales Quotation, 202=Production Order]
  BaseEntry Int(11) Base Document Internal ID
  BaseLine Int(11) Base Row
  LineStatus VarChar(1) Row Status default=O [O=Open, C=Closed]
  ItemCode nVarChar(50) Item No. ->OITM
  Dscription nVarChar(200) Item/Service Description
  Quantity Num(19,6) Quantity
  ShipDate Date(8) Row Delivery Date
  OpenQty Num(19,6) Remaining Open Quantity
  Price Num(19,6) Price
  Currency nVarChar(3) Price Currency ->OCRN
  Rate Num(19,6) Currency Rate
  DiscPrcnt Num(19,6) Discount % per Row
  LineTotal Num(19,6) Row Total
  TotalFrgn Num(19,6) Row Total (FC)
  OpenSum Num(19,6) Open Amount
  OpenSumFC Num(19,6) Open Amount (FC)
  VendorNum nVarChar(50) Vendor Catalog No.
  SerialNum nVarChar(17) Serial Number
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  SlpCode Int(11) Sales Employee Code default=-1 ->OSLP
  Commission Num(19,6) Commission Percentage
  TreeType VarChar(1) BOM Type default=N [N=Not a BOM, A=Assembly, S=Sales, I=Sales BOM Component, P=Production, T=Template]
  AcctCode nVarChar(15) Account Code ->OACT
  TaxStatus VarChar(1) Tax Definition [Y=Yes, N=No]
  GrossBuyPr Num(19,6) Gross Profit Base Price
  PriceBefDi Num(19,6) Unit Price
  DocDate Date(8) Posting Date
  Flags Int(11) Flags default=0
  OpenCreQty Num(19,6) Credit Memo Amount
  UseBaseUn VarChar(1) Inventory UoM default=N [Y=Yes, N=No]
  SubCatNum nVarChar(50) BP Catalog No. ->OSCN
  BaseCard nVarChar(15) Base BP Code ->OCRD
  TotalSumSy Num(19,6) Row Total (SC)
  OpenSumSys Num(19,6) Open Amount (SC)
  InvntSttus VarChar(1) Warehouse Status default=O [O=Open, C=Closed]
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  CodeBars nVarChar(254) Bar Code
  VatPrcnt Num(19,6) Tax Rate per Row
  VatGroup nVarChar(8) Tax Definition ->OVTG
  PriceAfVAT Num(19,6) Gross Price after Discount
  Height1 Num(19,6) Height 1
  Hght1Unit Int(6) Unit of Height 1
  Height2 Num(19,6) Height 2
  Hght2Unit Int(6) Unit of Height 2
  Width1 Num(19,6) Width 1
  Wdth1Unit Int(6) Unit of Width 1
  Width2 Num(19,6) Width 2
  Wdth2Unit Int(6) Unit of Width 2
  Length1 Num(19,6) Length 1
  Len1Unit Int(6) Unit of Length 1
  length2 Num(19,6) Length 2
  Len2Unit Int(6) Unit of Length 2
  Volume Num(19,6) Quantity
  VolUnit Int(6) Vol. Unit
  Weight1 Num(19,6) Weight 1
  Wght1Unit Int(6) Unit of Weight 1
  Weight2 Num(19,6) Weight 2
  Wght2Unit Int(6) Unit of Weight 2
  Factor1 Num(19,6) Factor 1
  Factor2 Num(19,6) Factor 2
  Factor3 Num(19,6) Factor 3
  Factor4 Num(19,6) Factor 4
  PackQty Num(19,6) Packing Quantity
  UpdInvntry VarChar(1) Warehouse Update default=Y [Y=Yes, N=No]
  BaseDocNum Int(11) Base Document No.
  BaseAtCard nVarChar(100) Customer/Vendor Base Document
  SWW nVarChar(16) Additional Identifier
  VatSum Num(19,6) Total Tax
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  FinncPriod Int(11) Posting Period ->OFPR
  ObjType nVarChar(20) Object Type default=540000006 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BlockNum nVarChar(100) Block Number
  ImportLog nVarChar(20) Import Log
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAqcuistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  DistribSum Num(19,6) Distributed Amount
  DstrbSumFC Num(19,6) Distributed Amount (FC)
  DstrbSumSC Num(19,6) Distributed Amount (SC)
  GrssProfit Num(19,6) Row Gross Profit
  GrssProfSC Num(19,6) Row Gross Profit (SC)
  GrssProfFC Num(19,6) Row Gross Profit (FC)
  VisOrder Int(11) Visual Order
  INMPrice Num(19,6) Item's Last Sales Price (OINM)
  PoTrgNum Int(11) PO Target No.
  PoTrgEntry nVarChar(11) PO Target Internal ID
  DropShip VarChar(1) Drop-Ship default=N [Y=Yes, N=No]
  PoLineNum Int(11) PO Target Row No.
  Address nVarChar(254) Address
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type [Y=Regular Tax, N=No Tax, U=Use Tax]
  OrigItem nVarChar(50) Original Item ->OITM
  BackOrdr VarChar(1) Allow Backorder [Y=Yes, N=No]
  FreeTxt nVarChar(100) Free Text
  PickStatus VarChar(1) Pick Status default=N [Y=Picked, N=Not Picked, R=Released for Picking, P=Partially Picked]
  PickOty Num(19,6) Pick Quantity
  PickIdNo Int(11) Pick ID
  TrnsCode Int(6) Shipping Method default=-1 ->OSHP
  VatAppld Num(19,6) Applied Tax
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  BaseQty Num(19,6) Base Quantity
  BaseOpnQty Num(19,6) Base Open Quantity
  VatDscntPr Num(19,6) Tax Discount %
  WtLiable VarChar(1) Withholding Tax Liable [Y=Yes, N=No]
  DeferrTax VarChar(1) Deferred Tax default=N [Y=Yes, N=No]
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatlF Num(19,6) Net Tax Amount
  LineVatS Num(19,6) Net Tax Amount
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value
  CEECFlag VarChar(1) Correction Invoice Was/Should Be default=S [W=Was, S=Should Be]
  ToStock Num(19,6) Corr. Invoice Amt to Inventory
  ToDiff Num(19,6) Corr. Invoice Amount to Diff.
  ExciseAmt Num(19,6) Excise Amount
  TaxPerUnit Num(19,6) Tax per Unit
  TotInclTax Num(19,6) Total Including Tax
  CountryOrg nVarChar(3) Country/Region of Origin
  StckDstSum Num(19,6) Stock Distribution Sum
  ReleasQtty Num(19,6) Released Quantity
  LineType VarChar(1) Row Type default=R [R=Regular]
  TranType VarChar(1) Transaction Type [C=Complete, R=Reject]
  Text Text(16) Text
  OwnerCode Int(11) Document Owner
  StockPrice Num(19,6) Inventory Price
  ConsumeFCT VarChar(1) Consumer Sales Forecast [Y=Yes, N=No]
  LstByDsSum Num(19,6) Last Buy Distribute Sum
  StckINMPr Num(19,6) Stock Inm Price
  LstBINMPr Num(19,6) Last Buy Inventory Journal Pr.
  StckDstFc Num(19,6) Stock Distribution Sum (FC)
  StckDstSc Num(19,6) Stock Distribution Sum (SC)
  LstByDsFc Num(19,6) Last Buy Distribute Sum (FC)
  LstByDsSc Num(19,6) Last Buy Distribute Sum (SC)
  StockSum Num(19,6) Stock Sum
  StockSumFc Num(19,6) Stock Sum FC
  StockSumSc Num(19,6) Stock Sum SC
  StckSumApp Num(19,6) Stock Sum Applied
  StckAppFc Num(19,6) Stock Sum Applied FC
  StckAppSc Num(19,6) Stock Sum Applied SC
  ShipToCode nVarChar(50) Ship-to Code
  ShipToDesc nVarChar(254) Ship-to Description
  StckAppD Num(19,6) Stock Distrib. - Applied Sum
  StckAppDFC Num(19,6) Stock Dist. - Applied Sum (FC)
  StckAppDSC Num(19,6) Stock Dist. - Applied Sum (SC)
  BasePrice VarChar(1) Price for Total Calculation default=E [E=Exclude Tax, I=Include Tax]
  GTotal Num(19,6) Gross Total
  GTotalFC Num(19,6) Gross Total (FC)
  GTotalSC Num(19,6) Gross Total (SC)
  DistribExp VarChar(1) Distribute Freight [Y=Yes, N=No]
  DescOW VarChar(1) Description Overwritten default=N [Y=Yes, N=No]
  DetailsOW VarChar(1) Details Overwritten default=N [Y=Yes, N=No]
  GrossBase Int(6) Base Method for Gross Profit
  VatWoDpm Num(19,6) Tax Before DPM Applied
  VatWoDpmFc Num(19,6) Tax Before DPM Applied (FC)
  VatWoDpmSc Num(19,6) Tax Before DPM Applied (SC)
  CFOPCode nVarChar(6) CFOP Code for Document ->OCFP
  CSTCode nVarChar(6) CST Code for ICMS
  Usage Int(11) Usage Code for Document ->OUSG
  TaxOnly VarChar(1) Tax Only [Y=Yes, N=No]
  WtCalced VarChar(1) Withholding Tax Calculated default=N [N=No, Y=Yes]
  QtyToShip Num(19,6) Quantity to Ship
  DelivrdQty Num(19,6) Delivered Quantity
  OrderedQty Num(19,6) Ordered Quantity
  CogsOcrCod nVarChar(8) COGS Distribution Rule Code ->OOCR
  CiOppLineN Int(11) Line Number of Opposite Line default=-1
  CogsAcct nVarChar(15) COGS Account Code ->OACT
  ChgAsmBoMW VarChar(1) Change Whs for Asm BoM Child [Y=Yes, N=No]
  ActDelDate Date(8) Actual Delivery Date
  OcrCode2 nVarChar(8) Costing Code 2 ->OOCR
  OcrCode3 nVarChar(8) Costing Code 3 ->OOCR
  OcrCode4 nVarChar(8) Costing Code 4 ->OOCR
  OcrCode5 nVarChar(8) Costing Code 5 ->OOCR
  TaxDistSum Num(19,6) Tax Distributed Amount
  TaxDistSFC Num(19,6) Tax Distributed Amount (FC)
  TaxDistSSC Num(19,6) Tax Distributed Amount (SC)
  PostTax VarChar(1) Post Tax in Price to Stock default=Y [Y=Yes, N=No]
  Excisable VarChar(1) Excisable [Yes/No] [Y=Yes, N=No]
  AssblValue Num(19,6) Assessable Value
  RG23APart1 Int(11) RG23A Part1 Number
  RG23APart2 Int(11) RG23A Part2 Number
  RG23CPart1 Int(11) RG23C Part1 Number
  RG23CPart2 Int(11) RG23C Part2 Number
  CogsOcrCo2 nVarChar(8) COGS Distribution Rule Code2 ->OOCR
  CogsOcrCo3 nVarChar(8) COGS Distribution Rule Code3 ->OOCR
  CogsOcrCo4 nVarChar(8) COGS Distribution Rule Code4 ->OOCR
  CogsOcrCo5 nVarChar(8) COGS Distribution Rule Code5 ->OOCR
  LnExcised VarChar(1) Line Excised [O=Open, C=Closed, P=Copied to OEI]
  LocCode Int(11) Location Code ->OLCT
  StockValue Num(19,6) Total COGS Value
  GPTtlBasPr Num(19,6) Total Base Price for Profit
  unitMsr2 nVarChar(100) Pur/Sal UoM if BaseUnit
  NumPerMsr2 Num(19,6) Pur/Sal UoM Value if Base Unit
  SpecPrice VarChar(1) Price Source Type default=N [Y=Special Prices for Business Partner, N=Manual, W=Active Price List, Discount Groups, R=Active Price List, U=Inactive Price List, A=Blanket Agreement, P=Period and Volume Discounts, Q=Period and Volume Discounts, Discount Groups, V=Inactive Price List, Discount Groups, 9=Special Prices for Business Partner, !=Blanket Agreement, 0=Period and Volume Discounts, 1=Period and Volume Discounts, Discount Groups, 2=Active Price List, 7=Active Price List, Discount Groups, 5=Inactive Price List, 6=Inactive Price List, Discount Groups]
  CSTfIPI nVarChar(2) CST for IPI Code
  CSTfPIS nVarChar(2) CST for PIS Code
  CSTfCOFINS nVarChar(2) CST for COFINS Code
  ExLineNo nVarChar(10) ExLineNo
  isSrvCall VarChar(1) Created from Service Call default=N [Y=Yes, N=No]
  PQTReqQty Num(19,6) Pur Quotation: Required Qty
  PQTReqDate Date(8) Pur Quotation: Required Date
  PcDocType Int(11) Purchase Confirmation Doc Type default=-1 [-1=No Type, 22=Purchase Order, 540000006=Purchase Quotation]
  PcQuantity Num(19,6) Purchase Confirmation Quantity
  LinManClsd VarChar(1) Line Was Closed Manually default=N [Y=Yes, N=No, U=Unknown]
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  NoInvtryMv VarChar(1) Without Inventory Movement default=N [Y=Yes, N=No]
  ActBaseEnt Int(11) Actual Base Document Entry
  ActBaseLn Int(11) Actual Base Line Number
  ActBaseNum Int(11) Actual Base Document No.
  OpenRtnQty Num(19,6) Quantity Open for Return
  AgrNo Int(11) Agreement No. ->OOAT
  AgrLnNum Int(11) Agreement Row Number
  CredOrigin VarChar(1) Credit Origin ->OBSI
  Surpluses Num(19,6) Surpluses
  DefBreak Num(19,6) Defect and Breakup
  Shortages Num(19,6) Shortages
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  UomEntry2 Int(11) UoM Entry if Base Unit default=0 ->OUOM
  UomCode nVarChar(20) UoM Code
  UomCode2 nVarChar(20) UoM Code if Base Unit
  FromWhsCod nVarChar(8) From Warehouse Code ->OWHS
  NeedQty VarChar(1) Consider Quantity of Items default=N [Y=Yes, N=No]
  PartRetire VarChar(1) Partial Retirement default=N [Y=Yes, N=No]
  RetireQty Num(19,6) Retirement Quantity
  RetireAPC Num(19,6) Retirement APC
  RetirAPCFC Num(19,6) Retirement APC FC
  RetirAPCSC Num(19,6) Retirement APC SC
  InvQty Num(19,6) Quantity - Inventory UoM
  OpenInvQty Num(19,6) Open Quantity (Inventory UoM)
  EnSetCost VarChar(1) Enable Set Item Cost in Return default=N [Y=Yes, N=No]
  RetCost Num(19,6) Return Cost in A/R Return
  Incoterms Int(11) Incoterms default=0 ->ODCI
  TransMod Int(11) Transport Mode default=0 ->ODCI
  LineVendor nVarChar(15) Line Vendor Code ->OCRD
  DistribIS VarChar(1) Distribute Intrastat Freight default=N [Y=Yes, N=No]
  ISDistrb Num(19,6) Intrastat Distrib. Amount
  ISDistrbFC Num(19,6) Intrastat Distrib. Amount (FC)
  ISDistrbSC Num(19,6) Intrastat Distrib. Amount (SC)
  IsByPrdct VarChar(1) Item Is By-Product default=N [N=No, Y=Yes]
  ItemType Int(11) Item Type default=4 [4=Item]
  PriceEdit VarChar(1) Price Was Edited by User default=N [N=No, Y=Yes]
  PrntLnNum Int(11) Parent Line Number
  LinePoPrss VarChar(1) Line PO Process default=N [Y=Yes, N=No]
  FreeChrgBP VarChar(1) Free of Charge (BP) default=N [Y=Yes, N=No]
  TaxRelev VarChar(1) Tax Relevant Row default=Y [Y=Yes, N=No]
  LegalText nVarChar(254) Legal Text
  ThirdParty VarChar(1) Third Party default=N [Y=Yes, N=No]
  LicTradNum nVarChar(32) Federal Tax ID
  InvQtyOnly VarChar(1) Change Qty (Inv. UoM) Only default=N [Y=Yes, N=No]
  UnencReasn Int(11) Reason for Unencumbered ICMS
  ShipFromCo nVarChar(50) Ship-From Code
  ShipFromDe nVarChar(254) Ship-From Description
  FisrtBin nVarChar(228) First Bin Location
  AllocBinC nVarChar(11) Allocated Bin Location Count
  ExpType nVarChar(4) Expense Type ->OEXD
  ExpUUID nVarChar(50) Expense UUID
  ExpOpType VarChar(1) Expense Operation Type [P=Professional Services, R=Renting Assets, O=Others]
  DIOTNat nVarChar(3) DIOT Nationality ->OCRY
  MYFtype nVarChar(2) MYF type [S1=MYF Wholesale Sales, S2=Retail Sales, P1=MYF Wholesale Purchases, P3=Other Expense Transactions]
  GPBefDisc Num(19,6) Gross Price
  ReturnRsn Int(6) Return Reason default=-1
  ReturnAct Int(6) Return Action default=-1
  StgSeqNum Int(11) Stage Sequence Number
  StgEntry Int(11) Stage Entry ->ORST
  StgDesc nVarChar(100) Stage Description
  ItmTaxType nVarChar(2) Item GST Tax Category [GR=GST Regular, GN=GST Nil Rated, GE=GST Exempt, NE=Excisable, NN=Non-GST Non-Excisable]
  SacEntry Int(11) SAC Entry ->OSAC
  NCMCode Int(11) NCM Code default=-1 ->ONCM
  HsnEntry Int(11) HSN Entry
  OriBAbsEnt Int(11) Original Base Document Internal ID
  OriBLinNum Int(11) Original Base Document Line Number
  OriBDocTyp Int(11) Original Base Document Type
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No, U=Use]
  EncryptIV nVarChar(100) Encrypt IV
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  StdItemId Int(11) Standard Item Identification ->OUNCL
  CommClass Int(11) Commodity Classification ->OUNCL
  VatExEntry Int(11) VAT Exemption AbsEntry ->OVEB
  VatExLN Int(6) VAT Exemption LineNum
  NatOfTrans Int(11) Nature of Transaction ->ODCI
  ISDtCryImp nVarChar(3) Destination Country/Region for Import ->OCRY
  ISDtRgnImp Int(11) Destination Region for Import ->ODCI
  ISOrCryExp nVarChar(3) Country/Region of Origin for Export ->OCRY
  ISOrRgnExp Int(11) Region of Origin for Export ->ODCI
  NVECode nVarChar(6) NVE Code
  PoNum nVarChar(20) Customer's Purchase Order Number
  PoItmNum Int(11) Customer's Purchase Order Item Number
  IndEscala VarChar(1) Indicator for Relevant Scale default=N [Y=Yes, N=No]
  CESTCode Int(11) CEST Code ->OCEST
  CtrSealQty Num(19,6) Control Seal Quantity
  CNJPMan nVarChar(14) CNPJ of Manufacturer
  UFFiscBene nVarChar(10) UF Fiscal Benefit Code
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]
  LegalTIMD nVarChar(250) Legal Text from Item Master Data
  LegalTTCA nVarChar(250) Legal Text from Tax Code Attributes
  LegalTW nVarChar(250) Legal Text from Warehouse
  LegalTCD nVarChar(250) Legal Text from Tax Code Determination
  RevCharge VarChar(1) Reverse Charge default=N [Y=Yes, N=No]
  ListNum Int(6) Price List No. ->OPLN

# PQT10 - Purchase Quotation - Row Structure
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SECONDARY U: DocEntry, AftLineNum, OrderNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OPQT
  LineSeq Int(11) Row Sequence
  AftLineNum Int(11) After Row Number
  OrderNum Int(11) Order Number
  LineType VarChar(1) Row Type [T=Text, S=Subtotal]
  LineText Text(16) Row Text
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=540000006 ->ADP1

# PQT11 - PQ - Drawn DPM Detail
Module: Marketing Documents | 70 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LineSeq
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OPQT
  LineNum Int(11) Row Number
  LineSeq Int(11) Sequence Number
  BaseAbs Int(11) Base Document Internal ID
  BaseType Int(11) Base Object Type default=-1 [-1=]
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  VatPrcnt Num(19,6) VAT Percent
  LineTotal Num(19,6) Net LC
  TotalFrgn Num(19,6) Net FC
  TotalSumSy Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFrgn Num(19,6) Tax FC
  VatSumSys Num(19,6) Tax SC
  ObjType nVarChar(20) Object Type default=540000006 ->ADP1
  LogInstanc Int(11) Log Instance
  IsAcq VarChar(1) Acquisition Tax-Liable default=N [N=No, Y=Yes]
  IsAllDrawn VarChar(1) Remaining Amount Drawn default=N [Y=Yes, N=No]
  IsGross VarChar(1) Is Gross Line default=N [N=Net Line, Y=Gross Line]
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  ApplNet Num(19,6) Applied Net LC
  ApplNetFc Num(19,6) Applied Net FC
  ApplNetSc Num(19,6) Applied Net SC
  ApplVat Num(19,6) Applied Tax LC
  ApplVatFc Num(19,6) Applied Tax FC
  ApplVatSc Num(19,6) Applied Tax SC
  BaseNet Num(19,6) Base Net LC
  BaseNetFc Num(19,6) Base Net FC
  BaseNetSc Num(19,6) Base Net SC
  BaseVat Num(19,6) Base Tax LC
  BaseVatFc Num(19,6) Base Tax FC
  BaseVatSc Num(19,6) Base Tax SC
  BaseGross Num(19,6) Base Gross LC
  BaseGrossF Num(19,6) Base Gross FC
  BaseGrossS Num(19,6) Base Gross SC
  LineType VarChar(1) Line Type default=D [D=Document Row, R=Currency Rounding, H=Down Payment Document Rounding]
  DctSum Num(19,6) Deductible Sum LC
  DctSumFc Num(19,6) Deductible Sum FC
  DctSumSc Num(19,6) Deductible Sum SC
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplDct Num(19,6) Applied Deductible Sum LC
  ApplDctFc Num(19,6) Applied Deductible Sum FC
  ApplDctSc Num(19,6) Applied Deductible Sum SC
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  BaseDct Num(19,6) Base Deductible Sum LC
  BaseDctFc Num(19,6) Base Deductible Sum FC
  BaseDctSc Num(19,6) Base Deductible Sum SC
  BaseEq Num(19,6) Base Equalization Sum LC
  BaseEqFc Num(19,6) Base Equalization Sum FC
  BaseEqSc Num(19,6) Base Equalization Sum SC
  TaxCode nVarChar(8) Tax Code ->OSTC
  ApplGross Num(19,6) Applied Gross LC
  ApplGrossF Num(19,6) Applied Gross FC
  ApplGrossS Num(19,6) Applied Gross SC
  TaxAdjust VarChar(1) Manual Tax Adjustment default=N [Y=Yes, N=No]
  RvsChrgSum Num(19,6) Reverse Charge Sum LC
  RvsChrgFc Num(19,6) Reverse Charge Sum FC
  RvsChrgSc Num(19,6) Reverse Charge Sum SC
  BasRvsChrg Num(19,6) Base Reverse Charge LC
  BasRvsFc Num(19,6) Base Reverse Charge FC
  BasRvsSc Num(19,6) Base Reverse Charge SC
  ApplRvs Num(19,6) Applied Reverse Charge LC
  ApplRvsFc Num(19,6) Applied Reverse Charge FC
  ApplRvsSc Num(19,6) Applied Reverse Charge SC
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# PQT12 - Purchase Quotation - Tax Extension
Module: Marketing Documents | 117 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OPQT
  TaxId0 nVarChar(100) Tax ID 0
  TaxId1 nVarChar(100) Tax ID 1
  TaxId2 nVarChar(100) Tax ID 2
  TaxId3 nVarChar(100) Tax ID 3
  TaxId4 nVarChar(100) Tax ID 4
  TaxId5 nVarChar(100) Tax ID 5
  TaxId6 nVarChar(100) Tax ID 6
  TaxId7 nVarChar(100) Tax ID 7
  TaxId8 nVarChar(100) Tax ID 8
  TaxId9 nVarChar(100) Tax ID 9
  State nVarChar(3) State Code
  County nVarChar(7) County Code
  Incoterms nVarChar(3) Incoterms
  Vehicle nVarChar(10) Vehicle ID
  VidState nVarChar(3) Vehicle ID (State)
  NfRef nVarChar(254) Nota Fiscal Reference
  Carrier nVarChar(15) Carrier Code
  QoP Int(11) Quantity of Packs
  PackDesc nVarChar(10) Pack Description
  Brand nVarChar(20) Brand
  NoSU Int(11) Number of Shipping Unit
  NetWeight Num(19,6) Net Weight
  GrsWeight Num(19,6) Gross Weight
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=540000006 ->ADP1
  TaxId10 nVarChar(100) Tax ID 10
  TransCat nVarChar(100) Transaction Category
  FormNo nVarChar(100) Form No.
  TaxId11 nVarChar(100) Tax ID 11
  StreetS nVarChar(100) Street
  BlockS nVarChar(100) Block
  BuildingS Text(16) Building/Floor/Room
  CityS nVarChar(100) City
  ZipCodeS nVarChar(20) Zip Code
  CountyS nVarChar(100) County
  StateS nVarChar(3) State ->OCST
  CountryS nVarChar(3) Country/Region ->OCRY
  AddrTypeS nVarChar(100) Address Type
  StreetNoS nVarChar(100) Street No.
  StreetB nVarChar(100) Street
  BlockB nVarChar(100) Block
  BuildingB Text(16) Building/Floor/Room
  CityB nVarChar(100) City
  ZipCodeB nVarChar(20) Zip Code
  CountyB nVarChar(100) County
  StateB nVarChar(3) State ->OCST
  CountryB nVarChar(3) Country/Region ->OCRY
  AddrTypeB nVarChar(100) Address Type
  StreetNoB nVarChar(100) Street No.
  ImpORExp VarChar(1) Import or Export [N=, Y=]
  Vat VarChar(1) VAT default=N [N=No VAT Support, Y=VAT Support]
  AltCrdNamB nVarChar(100) Alternative BP Name
  AltTaxIdB nVarChar(32) Alternative Tax ID
  Address2S nVarChar(50) Address Name 2
  Address3S nVarChar(50) Address Name 3
  Address2B nVarChar(50) Address Name 2
  Address3B nVarChar(50) Address Name 3
  MainUsage Int(11) Main Usage Code of Document ->OUSG
  GlbLocNumS nVarChar(50) Global Location Number
  GlbLocNumB nVarChar(50) Global Location Number
  CollectDT nVarChar(20) Date and Time of Collection
  TransprtDT Date(8) Transport Starting Date
  TransprtRS nVarChar(100) Transport Reason
  TaxId12 nVarChar(50) Tax ID 12
  TaxId13 nVarChar(100) Deductee Ref. No. in India
  ImpExpNo nVarChar(100) Import/Export Bill No.
  ImpExpDate Date(8) Import/Export Date
  BpGSTType Int(11) GST Regn Type of BP
  BpGSTN nVarChar(15) GST Regn No of BP
  BpStateCod nVarChar(3) State Code of Business Partner ->OCST
  BPStatGSTN nVarChar(2) GST State Code of BP
  LocGSTType Int(11) GST Regn Type of Location
  LocGSTN nVarChar(15) GST Regn No of Location
  LocStatCod nVarChar(3) State Code of Location ->OCST
  LocStaGSTN nVarChar(2) GST State Code of Location
  BpCountry nVarChar(3) Country/Region Code of BP ->OCRY
  OrigImpNo nVarChar(100) Original Bill of Entry No.
  OrigImpDat Date(8) Original Bill of Entry Date
  ExportType VarChar(1) Exporting Type default=E [E=Imports/Exports, S=SEZ Developer, U=SEZ Unit, D=Deemed Imports/Exports]
  PortCode nVarChar(100) Port Code
  BoEValue Num(19,6) Bill of Entry Value
  IsIGSTAct VarChar(1) Supply under IGST Account [Y=Yes, N=No]
  ClaimRefun VarChar(1) Claim Refund [Y=Yes, N=No]
  TaxRateDif Int(11) Differential % of Tax Rate [65=, 100=]
  BPGdsIssP nVarChar(15) Goods Issue Place BP
  CNPJGIP nVarChar(100) Goods Issue Place CNPJ
  CPFGIP nVarChar(100) Goods Issue Place CPF
  StreetGIP nVarChar(100) Goods Issue Place Street
  StrtNoGIP nVarChar(100) Goods Issue Place Street No.
  BldngGIP Text(16) Goods Issue Place Building
  ZipGIP nVarChar(20) Goods Issue Place Zip Code
  BlockGIP nVarChar(100) Goods Issue Place Block
  CityGIP nVarChar(100) Goods Issue Place City
  CountyGIP nVarChar(100) Goods Issue Place County
  StateGIP nVarChar(3) Goods Issue Place State ->OCST
  CountryGIP nVarChar(3) Goods Issue Place Country/Region ->OCRY
  PhoneGIP nVarChar(20) Goods Issue Place Phone
  EMailGIP nVarChar(100) Goods Issue Place E-Mail
  DptDateGIP Date(8) Goods Issue Place Departure Date
  BPDelivryP nVarChar(15) Delivery Place BP
  CNPJDlvryP nVarChar(100) Delivery Place CNPJ
  CPFDlvryP nVarChar(100) Delivery Place CPF
  StrtDlvryP nVarChar(100) Delivery Place Street
  StrNoDlvrP nVarChar(100) Delivery Place Street No.
  BldDlvryP Text(16) Delivery Place Building
  ZipDlvryP nVarChar(20) Delivery Place Zip Code
  BlckDlvryP nVarChar(100) Delivery Place Block
  CityDlvryP nVarChar(100) Delivery Place City
  CntyDlvryP nVarChar(100) Delivery Place County
  StatDlvryP nVarChar(3) Delivery Place State ->OCST
  CtryDlvryP nVarChar(3) Delivery Place Country/Region ->OCRY
  FoneDlvryP nVarChar(20) Delivery Place Phone
  MailDlvryP nVarChar(100) Delivery Place E-Mail
  DpDtDlvryP Date(8) Delivery Place Departure Date
  AuthedCNPJ nVarChar(250) Authorized CNPJ or CPF
  TaxId14 nVarChar(250) ITR Filing

# PQT13 - Purchase Quotation Rows - Distributed Expenses
Module: Marketing Documents | 59 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OPQT
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=540000006 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Aquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Normal Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) VAT Applied Frgn
  VatAppldSC Num(19,6) VAT Applied Sys
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock default=N [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Line No.
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Abs. Entry default=-1
  BaseGroup Int(11) Base Document Group default=-1
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1
  VisOrder Int(11) Visual Order
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DistribExp VarChar(1) Distribute Freights [Y=Yes, N=No]
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ

# PQT14 - Purchase Quotation - Assembly - Rows
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPQT
  LineNum Int(11) Row Number default=-1
  ChildNum Int(11) Child Number default=-1
  ItemCode nVarChar(50) Item no. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  TotalQty Num(19,6) Total Quantity
  OpenQty Num(19,6) Remaining Open Quantity
  ObjectType nVarChar(20) object type default=540000006 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BaseChildN Int(11) Base Child Number default=-1
  EncryptIV nVarChar(100) Encrypt IV

# PQT15 - PQ - Drawn DPM Applied
Module: Marketing Documents | 84 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OPQT
  LineNum Int(11) Row Number
  ObjType nVarChar(20) object type default=540000006 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  StaCode nVarChar(8) Tax Authority Code
  StaType Int(11) Tax Authority Type
  StaIndex Int(11) Tax Authority Seq Index
  BaseNet Num(19,6) Net LC
  BaseNetFc Num(19,6) Net FC
  BaseNetSc Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFc Num(19,6) Tax FC
  VatSumSc Num(19,6) Tax SC
  DctSum Num(19,6) Deductible Sum LC
  DctSumFc Num(19,6) Deductible Sum FC
  DctSumSc Num(19,6) Deductible Sum SC
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplNet Num(19,6) Applied Net LC
  ApplNetFc Num(19,6) Applied Net FC
  ApplNetSc Num(19,6) Applied Net SC
  ApplVat Num(19,6) Applied Tax LC
  ApplVatFc Num(19,6) Applied Tax FC
  ApplVatSc Num(19,6) Applied Tax SC
  ApplDct Num(19,6) Applied Deductible Sum LC
  ApplDctFc Num(19,6) Applied Deductible Sum FC
  ApplDctSc Num(19,6) Applied Deductible Sum SC
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  PaidNet Num(19,6) Paid Net LC
  PaidNetFc Num(19,6) Paid Net FC
  PaidNetSc Num(19,6) Paid Net SC
  PaidVat Num(19,6) Paid Tax LC
  PaidVatFc Num(19,6) Paid Tax FC
  PaidVatSc Num(19,6) Paid Tax SC
  PaidDct Num(19,6) Paid Deductible Sum LC
  PaidDctFc Num(19,6) Paid Deductible Sum FC
  PaidDctSc Num(19,6) Paid Deductible Sum SC
  PaidEq Num(19,6) Paid Equalization Sum LC
  PaidEqFc Num(19,6) Paid Equalization Sum FC
  PaidEqSc Num(19,6) Paid Equalization Sum SC
  DpApplNet Num(19,6) Dpm Appl Net LC
  DpApplNetF Num(19,6) Dpm Appl Net FC
  DpApplNetS Num(19,6) Dpm Appl Net SC
  DpApplVat Num(19,6) Dpm Appl Tax LC
  DpApplVatF Num(19,6) Dpm Appl Tax FC
  DpApplVatS Num(19,6) Dpm Appl Tax SC
  DpApplDct Num(19,6) Dpm Appl Deductible Sum LC
  DpApplDctF Num(19,6) Dpm Appl Deductible Sum FC
  DpApplDctS Num(19,6) Dpm Appl Deductible Sum SC
  DpApplEq Num(19,6) Dpm Appl Equalization Sum LC
  DpApplEqFc Num(19,6) Dpm Appl Equalization Sum FC
  DpApplEqSc Num(19,6) Dpm Appl Equalization Sum SC
  TaxCode nVarChar(8) Tax Code ->OSTC
  LineType VarChar(1) Row Type default=D [D=Document, R=Exchange Rate Rounding, H=Document Header Rounding]
  BaseGrs Num(19,6) Gross LC
  BaseGrsFc Num(19,6) Gross FC
  BaseGrsSc Num(19,6) Gross SC
  ApplGrs Num(19,6) Applied Gross LC
  ApplGrsFc Num(19,6) Applied Gross FC
  ApplGrsSc Num(19,6) Applied Gross SC
  PaidGrs Num(19,6) Paid Gross LC
  PaidGrsFc Num(19,6) Paid Gross FC
  PaidGrsSc Num(19,6) Paid Gross SC
  DpApplGrs Num(19,6) Dpm Appl Gross LC
  DpApplGrsF Num(19,6) Dpm Appl Gross FC
  DpApplGrsS Num(19,6) Dpm Appl Gross SC
  RvsChrgSum Num(19,6) Reverse Charge Sum
  RvsChrgSc Num(19,6) Reverse Charge Sum (SC)
  RvsChrgFc Num(19,6) Reverse Charge Sum (FC)
  ApplRvs Num(19,6) Applied Reverse Charge Sum LC
  ApplRvsSc Num(19,6) Applied Reverse Charge Sum SC
  ApplRvsFc Num(19,6) Applied Reverse Charge Sum FC
  PaidRvs Num(19,6) Paid Reverse Charge Sum LC
  PaidRvsSc Num(19,6) Paid Reverse Charge Sum SC
  PaidRvsFc Num(19,6) Paid Reverse Charge Sum FC
  DpApplRvs Num(19,6) Dpm Applied Reverse Charge LC
  DpApplRvsS Num(19,6) Dpm Applied Reverse Charge SC
  DpApplRvsF Num(19,6) Dpm Applied Reverse Charge FC
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# PQT16 - Purchase Quotation - SnB properties
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, SnBIndex
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) abs entry ->OPQT
  LineNum Int(11) Line Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object id
  ObjAbs Int(11) Object Abs
  DrfWObjAbs Int(11) draft Wobj Abs default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type default=540000006
  LogInstanc Int(11) Log Instance

# PQT17 - Purchase Quotation - Import Process
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPQT
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=540000006 ->ADP1
  ImpDocType VarChar(1) Type of Importation Document ->OBSI
  ImpDocNum nVarChar(10) Importation Document Number
  DateOfReg Date(8) Date of Registry DI/DSI/DA
  CustClrDat Date(8) Date of Customs Clearance
  ConcActNum nVarChar(30) Drawback Concession Acct No.
  AdditNum nVarChar(30) Additional Number
  AddItmDV Num(19,6) Additional Item Discount Value
  tpVTransp Int(6) Overland Transport Route [1=Maritime, 2=Waterway, 3=Lakeside, 4=Air, 5=Post, 6=Train, 7=Road, 8=Network Transmission, 9=Own Means, 10=Input/Output Fictitious, 11=Courier, 12=Hand Carry]
  DrawSReg nVarChar(11) Drawback - Suspension Regime
  AddFrNavyA Num(19,6) Additional Freight to Navy Authority
  TypeOfImp VarChar(1) Type of Import
  nSeqAdic Int(6) Additional Item Sequential Number

# PQT18 - Purchase Quotation - Export Process
Module: Marketing Documents | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPQT
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=540000006 ->ADP1
  ExpDocType Int(11) Type of Exportation Document default=-1 ->OBNI
  ExpDeclNum Int(11) Exportation Declaration Number
  ExpDeclDat Date(8) Exportation Declaration Date
  ExpNature Int(11) Nature of Exportation default=-1 ->OBNI
  ExpRegNum Int(11) Number of Exportation Registry
  ExpRegDate Date(8) Date of Exportation Registry
  LadBillNum nVarChar(19) Bill of Lading Number
  LadBillDat Date(8) Date of Bill of Lading
  MerchLeftD Date(8) Date Merchandise Left Customs
  LadBillTyp Int(11) Type of Bill of Lading default=-1 ->OBNI
  DrawSReg nVarChar(11) Drawback - Suspension Regime
  NatureExp nVarChar(44) Nature of Export
  QultExpItm Num(19,6) Quantity of Exported Items
  nSeqAdic Int(6) Additional Item Sequential Number

# PQT19 - Purchase Quotation - Bin Allocation Data
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, BinAllocSe
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OPQT
  BinAllocSe Int(11) Bin Allocation Sequence
  LineNum Int(11) Line Number
  SubLineNum Int(11) Subline Number default=-1
  SnBType Int(11) SnB Type default=-1
  SnBMDAbs Int(11) SnB Master Data Internal No. default=-1
  BinAbs Int(11) Bin Internal Number ->OBIN
  Quantity Num(19,6) Quantity
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjType nVarChar(20) Object Type default=540000006 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  BinActTyp Int(6) Bin Action Type [1=Transaction In, 2=Transaction Out, 4=SnB Complete, 8=Bin First Then SnB]

# PQT2 - Purchase Quotation - Freight - Rows
Module: Marketing Documents | 64 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OPQT
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=540000006 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) Vat Applied
  VatAppldFC Num(19,6) Vat Applied Frgn
  VatAppldSC Num(19,6) Vat Applied Sys
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report [Y=Yes, N=No]
  BaseGroup Int(11) Base Document Group default=-1 [-1=, 0=, 1=, 2=]
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1 [-1=, 0=, 1=, 2=]
  VisOrder Int(11) Visual Order
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]

# PQT20 - Intrastat Expenses
Module: Marketing Documents | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPQT
  ExpnsCode Int(11) Freight Code ->OEXD
  TotalLC Num(19,6) Total
  TotalFC Num(19,6) Total (FC)
  TotalSC Num(19,6) Total (SC)
  DistribM VarChar(1) Distribution Method default=T [Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DrawnLC Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  LineNum Int(11) Line Number default=-1
  BaseAbsEnt Int(11) Base Abs. Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 16=Return, 13=A/R Invoice, 203=Down Payment Incoming, 204=Down Payment Outgoing, 22=Purchase Order, 20=Goods Receipt PO, 21=Goods Return, 18=A/P Invoice, 540000006=Purchase Quotation, 0=, -1=]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No. default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=540000006 ->ADP1
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  AppliedLC Num(19,6) Applied
  AppliedFC Num(19,6) Applied (FC)
  AppliedSC Num(19,6) Applied (SC)

# PQT21 - Purchase Quotation - Document Reference Information
Module: Marketing Documents | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, RefType
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjectType nVarChar(20) Object Type default=540000006
  LogInstanc Int(11) Log Instance default=0
  RefType VarChar(1) Reference Types default=S [S=System Document, E=External Document]
  LineNum Int(11) Line Number
  RefDocEntr Int(11) Referenced Internal Number
  RefDocNum Int(11) Referenced Document Number
  ExtDocNum nVarChar(100) External Referenced Document Number
  RefObjType nVarChar(20) Referenced Object Type [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 234000031=Return Request, 16=Return, 203=A/R Down Payment, 13=A/R Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 280=A/R Tax Invoice, 1470000113=Purchase Request, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Return Request, 21=Goods Return, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 281=A/P Tax Invoice, 69=Landed Costs, 24=Incoming Payments, 46=Outgoing Payments, 57=Checks for Payment, 321=Internal Reconciliation, 34=Recurring Posting, 30=Journal Entry, 59=Goods Receipt, 60=Goods Issue, 162=Inventory Revaluation, 1470000065=Inventory Counting, 10000071=Inventory Posting, 1250000001=Inventory Transfer Request, 67=Inventory Transfer, 202=Production Order, 13001=Original Invoice, -1=External Document, 20301=Original Down Payment Invoice]
  AccessKey nVarChar(100) Access Key
  IssueDate Date(8) Date of Issue
  IssuerCNPJ nVarChar(100) Issuer CNPJ
  IssuerCode nVarChar(10) Fiscal Document Issuer UF Code
  Model nVarChar(6) Fiscal Document Model
  Series nVarChar(3) Fiscal Document Series
  Number Int(11) Fiscal Document Number
  RefAccKey nVarChar(100) Referenced CT-e Access Key
  RefAmount Num(19,6) Referenced Amount
  SubSeries nVarChar(3) Fiscal Document Subseries
  Remark nVarChar(254) Remarks
  LinkRefTyp nVarChar(20) Link Reference Type default=00 [00=, 01=Nota de cr�dito de los documentos relacionados, 02=Nota de d�bito de los documentos relacionados, 03=Devoluci�n de mercanc�a sobre facturas o traslados previos, 04=Sustituci�n de los CFDI previos, 05=Traslados de mercancias facturados previamente, 06=Factura generada por los traslados previos, 07=CFDI por aplicaci�n de anticipo, 08=Customs, MX_08=Factura generada por pagos en parcialidades, 09=Factura generada por pagos diferidos]

# PQT22 - Purchase Quotation - Resource Costs
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, StdCostNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->PQT1
  LineNum Int(11) Row Number ->PQT1
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=540000006
  LogInstanc Int(11) Log Instance default=0

# PQT23 - A/P Invoice - Selected Asset Master Data
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, VisOrder
  ASSETS: DocEntry, LineNum, AssetCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPQT
  LineNum Int(11) Row Number
  AssetCode nVarChar(50) Selected Asset Code ->OITM
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Remarks nVarChar(100) Remarks
  Amount Num(19,6) Amount
  AmountSC Num(19,6) Amount (SC)
  SerialNo nVarChar(30) Serial Number
  VisOrder Int(11) Visual Order
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=540000006 ->ADP1

# PQT24 - Purchase Quotation - Tracking Note Assignment
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  ItemCCDNum nVarChar(40) Item CCD Number
  CntrOrigin nVarChar(3) Country/Region of Origin
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=540000006 ->ADP1
  SubLineNum Int(11) BOM Line No.

# PQT25 - Purchase Quotation - Amt Per VAT Grp
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, VatGroup, Type
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  VatGroup nVarChar(8) Tax Definition ->OVTG
  VatPrcnt Num(19,6) Tax Rate
  BaseAmnt Num(19,6) Base Amount
  BaseAmntFC Num(19,6) Base Amount (FC)
  BaseAmntSC Num(19,6) Base Amount (SC)
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  Type Int(11) Type default=1 [1=Discount by Tax]
  Currency nVarChar(3) Price Currency
  Rate Num(19,6) Currency Rate
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=540000006 ->ADP1

# PQT26 - Purchase Quotation - E-Way Bill Information
Module: Marketing Documents | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPQT
  SuplyType nVarChar(20) EWB Transaction Type [O=Outward, I=Inward]
  SubSplyTyp Int(11) EWB Sub-Type ->OEST
  DocType nVarChar(3) EWB Doc. Type ->OEDT
  TransMode Int(11) EWB Transportation Mode ->OETM
  Distance Num(19,6) EWB Transport Distance
  TransDocNo nVarChar(16) EWB Transporter Doc. No.
  TransDate Date(8) EWB Transportation Date
  VehicleTyp nVarChar(2) EWB Vehicle Type ->OEVT
  VehicleNo nVarChar(15) EWB Vehicle Number
  EWayBillNo nVarChar(20) EWB No.
  EwbDate Date(8) E-Way Bill Date
  FrmTraName nVarChar(100) EWB Consignor Name
  FrmAddres1 nVarChar(120) EWB Consignor Address 1
  FrmAddres2 nVarChar(120) EWB Consignor Address 2
  FrmZipCode nVarChar(20) EWB Consignor Zip Code
  ActFrmStat nVarChar(2) Dispatch State of EWB Consignor
  ToTraName nVarChar(100) EWB Consignee Name
  ToAddres1 nVarChar(120) EWB Consignee Address 1
  ToAddres2 nVarChar(120) EWB Consignee Address 2
  ToZipCode nVarChar(20) EWB Consignee Zip Code
  ActToState nVarChar(2) Ship-To State of EWB Consignee
  FrmGSTN nVarChar(15) EWB Consignor GSTN
  FrmState nVarChar(2) Bill-To State of EWB Consignor
  ToGSTN nVarChar(15) EWB Consignee GSTN
  ToState nVarChar(2) Bill-To State of EWB Consignee
  MainHsnEnt Int(11) EWB Main HSN Entry ->OCHP
  FrmPlace nVarChar(50) EWB Consignor Place
  ToPlace nVarChar(50) EWB Consignee Place
  TransID nVarChar(15) EWB Transporter ID
  TransName nVarChar(25) EWB Transporter Name
  ExpireDate Date(8) EWB Expiration Date
  ObjectType nVarChar(20) Object Type default=540000006 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TspEntry Int(11) Transporter Abs. Entry ->OTSP
  TspLine Int(11) Transportation Line
  TransType Int(11) Transaction Type [1=Regular, 2=Bill To-Ship To, 3=Bill From-Dispatch From, 4=Combination of 2 and 3]

# PQT27 - Purchase Quotation - E-Books(GR) Rows
Module: Marketing Documents | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  RELATE_ROW: DocEntry, RelateType, RelateLine, GroupNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPQT
  LineNum Int(11) Row Number
  RelateType Int(11) Relation Type default=-1 [1=Row, 2=Row Expenses, 3=Document Expenses, 13=Distributed Freights, -1=Manual]
  RelateLine Int(11) Relation Row Number default=-1
  GroupNum Int(11) Group Number default=-1
  LineTotal Num(19,6) Line Total
  LineTotalF Num(19,6) Line Total (FC)
  LineTotalS Num(19,6) Line Total (SC)
  InClassTyp Int(11) Income Classification Type ->OICP
  InClassCat Int(11) Income Classification Category ->OICC
  ExClassTyp Int(11) Expense Classification Type ->OECP
  ExClassCat Int(11) Expense Classification Cat. ->OECC
  VatCate Int(11) VAT Category
  NetValue Num(19,6) Net Value
  NetValueFC Num(19,6) Net Value (FC)
  NetValueSC Num(19,6) Net Value (SC)
  VatAmount Num(19,6) VAT Amount
  VatAmFC Num(19,6) VAT Amount (FC)
  VatAmSC Num(19,6) VAT Amount (SC)
  WtPercCat Int(11) Withheld Percentage Category
  WtAmount Num(19,6) Withheld Amount
  WtAmountFC Num(19,6) Withheld Amount (FC)
  WtAmountSC Num(19,6) Withheld Amount (SC)
  ObjectType nVarChar(20) Object Type default=13 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  WtCategory VarChar(1) Withheld Category [I=Invoice, P=Payment]
  VATClassTy Int(11) VAT Classification Type ->OECP
  VATClassCa Int(11) VAT Classification Category ->OECC
  EBVatExCau Int(11) VAT Exemption Cause ->OVEC

# PQT28 - Purchase Quotation - Reported Tracking Note
Module: Marketing Documents | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
  TCN_KEY U: DocEntry, LineNum, TrackingNt, TrackiNtLn
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  UnusedQty Num(19,6) Unused Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=540000006 ->ADP1
  SubLineNum Int(11) BOM Line No.

# PQT3 - Purchase Quotation - Freight
Module: Marketing Documents | 80 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  DOCUMENT: DocEntry, BaseAbsEnt
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OPQT
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  Comments nVarChar(100) Remarks
  ObjType nVarChar(20) Object Type default=540000006 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  WTLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  VatApplied Num(19,6) Vat Applied
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatF Num(19,6) Net Tax Amount (FC)
  LineVatS Num(19,6) Net Tax Amount (SC)
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 17=Sales Order]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No.
  LineNum Int(11) line num default=-1
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Doc. Internal No. default=-1
  StDstr Num(19,6) Stock Distributed Sum
  StDstrSC Num(19,6) Stock Distributed Sum (SC)
  StDstrFC Num(19,6) Stock Distributed Sum (FC)
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  TaxDistMtd VarChar(1) Tax Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  GrsAmount Num(19,6) Gross Amount
  GrsFC Num(19,6) Gross Amount (FC)
  GrsSC Num(19,6) Gross Amount (SC)
  BaseTotal VarChar(1) Base Total for Calculation default=N [N=Net Total, G=Gross Total]
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)
  RRVatLC Num(19,6) Return Request VAT Amount
  RRVatFC Num(19,6) Return Request VAT Amount (FC)
  RRVatSC Num(19,6) Return Request VAT Amount (SC)
  EncryptIV nVarChar(100) Encrypt IV
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]

# PQT4 - Purchase Quotation - Tax Amount per Document
Module: Marketing Documents | 61 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SCONDARY: DocEntry, LineNum, GroupNum, ExpnsCode, StcCode, StaCode, staType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OPQT
  LineNum Int(11) Row Number default=-1
  GroupNum Int(11) Group Number default=-1
  ExpnsCode Int(11) Expense Code default=-1 ->OEXD
  RelateType Int(11) Relation Type default=1 [1=Row, 2=Row Freight Charges, 3=Document Expenses, 13=Distributed Freights]
  StcCode nVarChar(8) Tax Code ->OSTC
  StaCode nVarChar(8) Authority Code ->OSTA
  staType Int(11) Authority Type ->OSTT
  TaxRate Num(19,6) Tax Rate
  TaxAcct nVarChar(15) Tax Account ->OACT
  TaxSum Num(19,6) Tax Amount
  TaxSumFrgn Num(19,6) Tax Amount (FC)
  TaxSumSys Num(19,6) Tax Amount (SC)
  BaseSum Num(19,6) Base Amount
  BaseSumFrg Num(19,6) Base Amount (FC)
  BaseSumSys Num(19,6) Base Amount (SC)
  ObjectType nVarChar(20) Object Type default=540000006 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Status default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  LineSeq Int(11) Line Sequence
  DeferrAcct nVarChar(15) Deferred Tax Account ->OACT
  BaseType Int(11) Base Document Type default=-1
  BaseAbs Int(11) Base Doc Abs Entry default=-1
  BaseSeq Int(11) Base Doc. Line Sequence
  DeductTax Num(19,6) Deductible Tax Amount
  DdctTaxFrg Num(19,6) Deductible Tax Amount (FC)
  DdctTaxSys Num(19,6) Deductible Tax Amount (SC)
  BaseAppld Num(19,6) Applied Base Amount
  BaseApldFC Num(19,6) Applied Base Amount (FC)
  BaseApldSC Num(19,6) Applied Base Amount (SC)
  NonDdctPrc Num(19,6) Non Deductible %
  NonDdctAct nVarChar(15) Non Deductible Account ->OACT
  TaxInPrice VarChar(1) Tax Included in Price? default=N [Y=Yes, N=No]
  Exempt VarChar(1) Exempt? default=N [Y=Yes, N=No]
  TaxExpAct nVarChar(15) Expense Account for Tax ->OACT
  OnHoldTax Num(19,6) On Hold Tax Amount
  OnHoldTaxF Num(19,6) On Hold Tax Amount (FC)
  OnHoldTaxS Num(19,6) On Hold Tax Amount (SC)
  InGrossRev VarChar(1) Included in Gross Revenue default=N [Y=Yes, N=No]
  TaxSumOrg Num(19,6) Tax Amount Original
  TaxSumOrgF Num(19,6) Tax Amount Original (FC)
  TaxSumOrgS Num(19,6) Tax Amount Original (SC)
  OpenTax Num(19,6) Open Service Tax
  OpenTaxFC Num(19,6) Open Service Tax (FC)
  OpenTaxSC Num(19,6) Open Service Tax (SC)
  Unencumbrd VarChar(1) Unencumbered default=N [Y=Yes, N=No]
  TaxOnRI VarChar(1) Tax On Reserve Invoice default=N [Y=Yes, N=No]
  RvsChrgPrc Num(19,6) Reverse Charge %
  RvsChrgTax Num(19,6) Reverse Charge Tax Amount
  RvsChrgSC Num(19,6) Reverse Charge Tax Amount (SC)
  RvsChrgFC Num(19,6) Reverse Charge Tax Amount (FC)
  InFirstIns VarChar(1) Included in First Installment default=N [Y=Yes, N=No]
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CESTrel VarChar(1) CEST Relevant default=N [Y=, N=]

# PQT5 - Purchase Quotation - Withholding Tax
Module: Marketing Documents | 158 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  SECONDERY U: AbsEntry, WTCode, BaseAbsEnt, Doc1LineNo
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator ->OPQT
  WTCode nVarChar(4) WT Code ->OWHT
  Rate Num(19,6) Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntSC Num(19,6) Taxable Amount in SC
  TxblAmntFC Num(19,6) Taxable Amount in FC
  WTAmnt Num(19,6) WT Amount
  WTAmntSC Num(19,6) WT Amount (SC)
  WTAmntFC Num(19,6) WT Amount (FC)
  ApplAmnt Num(19,6) Applied WT Amount
  ApplAmntSC Num(19,6) Applied WTax Amount (SC)
  ApplAmntFC Num(19,6) Applied WTax Amount (FC)
  Category VarChar(1) Category [P=Payment, I=Invoice]
  Criteria VarChar(1) Criteria [Y=Accrual, N=Cash]
  Account nVarChar(15) G/L Account ->OACT
  Type VarChar(1) Withholding Type [V=VAT Withholding, I=Income Tax Withholding]
  RoundType VarChar(1) Rounding Type [T=Truncated, C=Commercial Values, N=No Rounding]
  BaseType VarChar(1) Base Type [G=Gross, N=Net, V=VAT, U=UoM]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseLine Int(11) Base Line
  BaseNum Int(11) Base Document Type default=-1 [-1=, 0=, 17=Sales Order]
  LineNum Int(11) Line Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Abs. Entry default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=540000006 ->ADP1
  Doc1LineNo Int(11) DOC1 Line Number default=-1
  WtLineType VarChar(1) WT Line Type default=D [D=Document Level WTax, L=Row Level WTax]
  TxblCurr nVarChar(3) Taxable Currency from Doc Line
  DtblCurr nVarChar(3) Deductible Currency
  DtblRate Num(19,6) Rate for Deductible Amount
  txblRate Num(19,6) Rate for Taxable Amount
  DtblAmount Num(19,6) Deductible Amount
  TdsAcc nVarChar(15) TDS Account ->OACT
  SurAcc nVarChar(15) Surcharge Account ->OACT
  CessAcc nVarChar(15) Cess Account ->OACT
  HscAcc nVarChar(15) HSC Account ->OACT
  TdsRate Num(19,6) TDS Rate
  SurRate Num(19,6) Surcharge Rate
  CessRate Num(19,6) Cess Rate
  HscRate Num(19,6) HSC Rate
  TdsBAmt Num(19,6) TDS Base Amount
  TdsBAmtSC Num(19,6) TDS Base Amount (SC)
  TdsBAmtFC Num(19,6) TDS Base Amount (FC)
  SurBAmt Num(19,6) Surcharge Base Amount
  SurBAmtSC Num(19,6) Surcharge Base Amount (SC)
  SurBAmtFC Num(19,6) Surcharge Base Amount (FC)
  CessBAmt Num(19,6) Cess Base Amount
  CessBAmtSC Num(19,6) Cess Base Amount (SC)
  CessBAmtFC Num(19,6) Cess Base Amount (FC)
  HscBAmt Num(19,6) HSC Base Amount
  HscBAmtSC Num(19,6) HSC Base Amount (SC)
  HscBAmtFC Num(19,6) HSC Base Amount (FC)
  TdsAmnt Num(19,6) TDS Tax Amount
  TdsAmntSC Num(19,6) TDS Tax Amount (SC)
  TdsAmntFC Num(19,6) TDS Tax Amount (FC)
  SurAmnt Num(19,6) Surcharge Tax Amount
  SurAmntSC Num(19,6) Surcharge Tax Amount (SC)
  SurAmntFC Num(19,6) Surcharge Tax Amount (FC)
  CessAmnt Num(19,6) Cess Tax Amount
  CessAmntSC Num(19,6) Cess Tax Amount (SC)
  CessAmntFC Num(19,6) Cess Tax Amount (FC)
  HscAmnt Num(19,6) HSC Tax Amount
  HscAmntSC Num(19,6) HSC Tax Amount (SC)
  HscAmntFC Num(19,6) HSC Tax Amount (FC)
  TdsAppl Num(19,6) Applied TDS Amount
  TdsApplSC Num(19,6) Applied TDS Amount (SC)
  TdsApplFC Num(19,6) Applied TDS Amount (FC)
  SurAppl Num(19,6) Applied Surcharge Amount
  SurApplSC Num(19,6) Applied Surcharge Amount (SC)
  SurApplFC Num(19,6) Applied Surcharge Amount (FC)
  CessAppl Num(19,6) Applied Cess Amount
  CessApplSC Num(19,6) Applied Cess Amount (SC)
  CessApplFC Num(19,6) Applied Cess Amount (FC)
  HscAppl Num(19,6) Applied HSC Amount
  HscApplSC Num(19,6) Applied HSC Amount (SC)
  HscApplFC Num(19,6) Applied HSC Amount (FC)
  BatchNum Int(11) Journal Voucher No.
  InCSTCode nVarChar(2) CST Code Incoming
  OutCSTCode nVarChar(2) CST Code Outgoing
  DpmWTApl Num(19,6) DPM WT Applied Amount
  DpmWTAplSC Num(19,6) DPM WT Applied Amount (SC)
  DpmWTAplFC Num(19,6) DPM WT Applied Amount (FC)
  WTTypeId Int(11) WT Type Id ->OWTT
  LnBsAmt Num(19,6) BR Line WT Base Amount
  LnBsAmtSC Num(19,6) BR Line WT Base Amount(SC)
  LnBsAmtFC Num(19,6) BR Line WT Base Amount(FC)
  LnCmTAmt Num(19,6) BR Line Cumulated Taxable Amount
  LnCmTAmtSC Num(19,6) BR Line Cumulated Taxable Amount(SC)
  LnCmTAmtFC Num(19,6) BR Line Cumulated Taxable Amount(FC)
  TDSType VarChar(1) TDS Type [E=eTDS, D=GST TDS, C=GST TCS, S=SALES TCS]
  IgstAcc nVarChar(15) IGST Account ->OACT
  CgstAcc nVarChar(15) CGST Account ->OACT
  SgstAcc nVarChar(15) SGST Account ->OACT
  IgstAmnt Num(19,6) IGST Tax Amount
  IgstAmntSC Num(19,6) IGST Tax Amount (SC)
  IgstAmntFC Num(19,6) IGST Tax Amount (FC)
  CgstAmnt Num(19,6) CGST Tax Amount
  CgstAmntSC Num(19,6) CGST Tax Amount (SC)
  CgstAmntFC Num(19,6) CGST Tax Amount (FC)
  SgstAmnt Num(19,6) SGST Tax Amount
  SgstAmntSC Num(19,6) SGST Tax Amount (SC)
  SgstAmntFC Num(19,6) SGST Tax Amount (FC)
  IgstRate Num(19,6) IGST Rate
  CgstRate Num(19,6) CGST Rate
  SgstRate Num(19,6) SGST Rate
  IgstBAmt Num(19,6) IGST Base Amount
  IgstBAmtSC Num(19,6) IGST Base Amount (SC)
  IgstBAmtFC Num(19,6) IGST Base Amount (FC)
  CgstBAmt Num(19,6) CGST Base Amount
  CgstBAmtSC Num(19,6) CGST Base Amount (SC)
  CgstBAmtFC Num(19,6) CGST Base Amount (FC)
  SgstBAmt Num(19,6) SGST Base Amount
  SgstBAmtSC Num(19,6) SGST Base Amount (SC)
  SgstBAmtFC Num(19,6) SGST Base Amount (FC)
  IgstAppl Num(19,6) Applied IGST Amount
  IgstApplSC Num(19,6) Applied IGST Amount (SC)
  IgstApplFC Num(19,6) Applied IGST Amount (FC)
  CgstAppl Num(19,6) Applied CGST Amount
  CgstApplSC Num(19,6) Applied CGST Amount (SC)
  CgstApplFC Num(19,6) Applied CGST Amount (FC)
  SgstAppl Num(19,6) Applied SGST Amount
  SgstApplSC Num(19,6) Applied SGST Amount (SC)
  SgstApplFC Num(19,6) Applied SGST Amount (FC)
  UtgstAcc nVarChar(15) UTGST Account ->OACT
  CsgstAcc nVarChar(15) Cess GST Account ->OACT
  UtgstAmt Num(19,6) UTGST Tax Amount
  UtgstAmtSC Num(19,6) UTGST Tax Amount (SC)
  UtgstAmtFC Num(19,6) UTGST Tax Amount (FC)
  CsgstAmt Num(19,6) Cess GST Tax Amount
  CsgstAmtSC Num(19,6) Cess GST Tax Amount (SC)
  CsgstAmtFC Num(19,6) Cess GST Tax Amount (FC)
  UtgstRate Num(19,6) UTGST Rate
  CsgstRate Num(19,6) Cess GST Rate
  UtgstBAmt Num(19,6) UTGST Base Amount
  UtgstBAmtS Num(19,6) UTGST Base Amount (SC)
  UtgstBAmtF Num(19,6) UTGST Base Amount (FC)
  CsgstBAmt Num(19,6) Cess GST Base Amount
  CsgstBAmtS Num(19,6) Cess GST Base Amount (SC)
  CsgstBAmtF Num(19,6) Cess GST Base Amount (FC)
  UtgstAppl Num(19,6) Applied UTGST Amount
  UtgstApplS Num(19,6) Applied UTGST Amount (SC)
  UtgstApplF Num(19,6) Applied UTGST Amount (FC)
  CsgstAppl Num(19,6) Applied Cess GST Amount
  CsgstApplS Num(19,6) Applied Cess GST Amount (SC)
  CsgstApplF Num(19,6) Applied Cess GST Amount (FC)
  EncryptIV nVarChar(100) Encrypt IV
  TcsIntAcct nVarChar(15) TCS Interim Account ->OACT
  SurIntAcct nVarChar(15) Surcharge Interim Account ->OACT
  CesIntAcct nVarChar(15) Cess Interim Account ->OACT
  HscIntAcct nVarChar(15) HSC interim Account ->OACT
  LnIntAcct nVarChar(15) Interim Account for Tax ->OACT
  FixedAmnt Num(19,6) Fixed Amount
  FixedAmtSC Num(19,6) Fixed Amount (SC)
  FixedAmtFC Num(19,6) Fixed Amount (FC)
  BaseQty Num(19,6) Base Quantity

# PQT6 - Purchase Quotation - Installments
Module: Marketing Documents | 65 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, InstlmntID
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OPQT
  InstlmntID Int(6) Installment ID default=1
  ObjType nVarChar(20) Object Type default=540000006 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DueDate Date(8) Due Date
  Status VarChar(1) Installment Status default=O [O=Open, C=Closed]
  DunnLevel Int(11) Dunning Level default=0
  InsTotal Num(19,6) Total Installment
  InsTotalFC Num(19,6) Total Installment (FC)
  InsTotalSy Num(19,6) Total Installment (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  VatSum Num(19,6) Total Tax
  VatSumFC Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  VatPaid Num(19,6) Tax Paid to Date
  VatPaidFC Num(19,6) Tax Paid (FC)
  VatPaidSys Num(19,6) Tax Paid (SC)
  TotalExpns Num(19,6) Total Freight Charges
  TotalExpFC Num(19,6) Total Freight Charges (FC)
  TotalExpSC Num(19,6) Total Freight Charges (SC)
  ExpAppl Num(19,6) Applied Freight Charges
  ExpApplFC Num(19,6) Applied Freight Charges (FC)
  ExpApplSC Num(19,6) Applied Freight Charges (SC)
  WTSum Num(19,6) WTax Amount
  WTSumFC Num(19,6) WTax Amount (FC)
  WTSumSC Num(19,6) WTax Amount (SC)
  WTApplied Num(19,6) Applied WTax
  WTAppliedF Num(19,6) Applied WTax (FC)
  WTAppliedS Num(19,6) Applied WTax (SC)
  TotalBlck Num(19,6) Total Reserved Amount
  TotalBlckF Num(19,6) Total Reserved Amount (FC)
  TotalBlckS Num(19,6) Total Reserved Amount (SC)
  VATBlck Num(19,6) Reserved Tax
  VATBlckFC Num(19,6) Reserved Tax (FC)
  VATBlckSC Num(19,6) Reserved Tax (SC)
  ExpnsBlck Num(19,6) Reserved Freight Charges
  ExpnsBlckF Num(19,6) Reserved Freight Charges (FC)
  ExpnsBlckS Num(19,6) Reserved Freight Charges (SC)
  WTBlocked Num(19,6) Reserved WTax Amount
  WTBlockedF Num(19,6) Reserved WTax Amount (FC)
  WTBlockedS Num(19,6) Reserved WTax Amount (SC)
  InstPrcnt Num(19,6) Installment %
  DunWizBlck VarChar(1) Wizard dunning block default=N [N=No, Y=Yes]
  DunDate Date(8) Last Dunning Date
  Paid Num(19,6) Paid
  PaidFrgn Num(19,6) Paid (FC)
  PaidSc Num(19,6) Paid (SC)
  reserved VarChar(1) Reserved default=N [N=No, Y=Yes]
  TaxOnExp Num(19,6) Tax on Expenses
  TaxOnExpFc Num(19,6) Tax on Expenses (FC)
  TaxOnExpSc Num(19,6) Tax on Expenses (SC)
  TaxOnExpAp Num(19,6) Applied Tax on Expenses
  TaxOnExApF Num(19,6) Applied Tax on Expenses (FC)
  TaxOnExApS Num(19,6) Applied Tax on Expenses (SC)
  TaxOnExBlo Num(19,6) Reserved Tax on Freight Amount
  TaxOnExBlF Num(19,6) Reserved Tax on Freight Amt FC
  TaxOnExBlS Num(19,6) Reserved Tax on Freight Amt SC
  LvlUpdDate Date(8) Dunning Level Update Date
  Ordered VarChar(1) Payment Ordered default=N [Y=Yes, N=No]
  PaidDpm Num(19,6) Paid by Down Payment
  PaidDpmFc Num(19,6) Paid by Down Payment (FC)
  PaidDpmSc Num(19,6) Paid by Down Payment (SC)
  EncryptIV nVarChar(100) Encrypt IV

# PQT7 - Delivery Packages - Purchase Quotation
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OPQT
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type default=540000006 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV

# PQT8 - Items in Package - Purchase Quotation
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum, ItemCode, UomEntry, NumPerMsr
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OPQT
  PackageNum Int(11) Package Number
  ItemCode nVarChar(50) Item Code ->OITM
  Quantity Num(19,6) Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=540000006 ->ADP1
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value default=0

# PQT9 - Purchase Quotation - Drawn DPM
Module: Marketing Documents | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OPQT
  LineNum Int(11) Row Number
  BaseAbs Int(11) Base Document Internal ID
  BaseLine Int(11) Base Document Row
  TargetBase VarChar(1) Target or Base Document default=B [B=Base, T=Target]
  ObjType nVarChar(20) Base Object Type
  DrawnSum Num(19,6) Net LC
  DrawnSumFc Num(19,6) Net FC
  DrawnSumSc Num(19,6) Net SC
  LogInstanc Int(11) Log Instance default=0
  ObjCode nVarChar(20) Object Type default=540000006 ->ADP1
  ApplDrawn Num(19,6) Applied Net LC
  ApplDrawnF Num(19,6) Applied Net FC
  ApplDrawnS Num(19,6) Applied Net SC
  BaseDocNum Int(11) Base Document Number
  BsDocDate Date(8) Base Posting Date
  BsDueDate Date(8) Base Due Date
  BsCardName nVarChar(100) Base BP Name
  BsComments nVarChar(254) Base Remarks
  Posted VarChar(1) Base Document Posted default=Y [Y=Yes, N=No]
  Vat Num(19,6) Tax LC
  VatFc Num(19,6) Tax FC
  VatSc Num(19,6) Tax SC
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  IsGross VarChar(1) Is Gross Line default=N [N=Net Line, Y=Gross Line]

# PRQ1 - Purchase Request - Rows
Module: Marketing Documents | 317 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  STATUS: LineStatus
  CURRENCY: Currency
  ACCOUNT: AcctCode
  BASE_ENTRY: BaseEntry, BaseType, BaseLine
  VIS_ORDER: DocEntry, VisOrder
  OWNER_CODE: OwnerCode
  ITM_WHS_OQ: ItemCode, WhsCode, OpenQty
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OPRQ
  LineNum Int(11) Row Number
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=, 20=Goods Receipt, 18=A/P Invoice, 22=Purchase Order, 204=A/P Down Payment, 540000006=Purchase Quotation]
  TrgetEntry Int(11) Target Document Internal ID
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 17=Sales Order, 23=Sales Quotation, 202=Production Order]
  BaseEntry Int(11) Base Document Internal ID
  BaseLine Int(11) Base Row
  LineStatus VarChar(1) Row Status default=O [O=Open, C=Closed]
  ItemCode nVarChar(50) Item No. ->OITM
  Dscription nVarChar(200) Item/Service Description
  Quantity Num(19,6) Quantity
  ShipDate Date(8) Row Delivery Date
  OpenQty Num(19,6) Remaining Open Quantity
  Price Num(19,6) Price after Discount
  Currency nVarChar(3) Price Currency ->OCRN
  Rate Num(19,6) Currency Rate
  DiscPrcnt Num(19,6) Discount % per Row
  LineTotal Num(19,6) Row Total
  TotalFrgn Num(19,6) Row Total (FC)
  OpenSum Num(19,6) Open Amount
  OpenSumFC Num(19,6) Open Amount (FC)
  VendorNum nVarChar(50) Vendor Catalog No.
  SerialNum nVarChar(17) Serial Number
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  SlpCode Int(11) Sales Employee Code default=-1 ->OSLP
  Commission Num(19,6) Commission Percentage
  TreeType VarChar(1) BOM Type default=N [N=Not a BOM, A=Assembly, S=Sales, I=Sales BOM Component, P=Production, T=Template]
  AcctCode nVarChar(15) Account Code ->OACT
  TaxStatus VarChar(1) Tax Definition [Y=Yes, N=No]
  GrossBuyPr Num(19,6) Gross Profit Base Price
  PriceBefDi Num(19,6) Unit Price
  DocDate Date(8) Posting Date
  Flags Int(11) Flags default=0
  OpenCreQty Num(19,6) Credit Memo Amount
  UseBaseUn VarChar(1) Inventory UoM default=N [Y=Yes, N=No]
  SubCatNum nVarChar(50) BP Catalog No. ->OSCN
  BaseCard nVarChar(15) Base BP Code ->OCRD
  TotalSumSy Num(19,6) Row Total (SC)
  OpenSumSys Num(19,6) Open Amount (SC)
  InvntSttus VarChar(1) Warehouse Status default=O [O=Open, C=Closed]
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  CodeBars nVarChar(254) Bar Code
  VatPrcnt Num(19,6) Tax Rate per Row
  VatGroup nVarChar(8) Tax Definition ->OVTG
  PriceAfVAT Num(19,6) Gross Price after Discount
  Height1 Num(19,6) Height 1
  Hght1Unit Int(6) Unit of Height 1
  Height2 Num(19,6) Height 2
  Hght2Unit Int(6) Unit of Height 2
  Width1 Num(19,6) Width 1
  Wdth1Unit Int(6) Unit of Width 1
  Width2 Num(19,6) Width 2
  Wdth2Unit Int(6) Unit of Width 2
  Length1 Num(19,6) Length 1
  Len1Unit Int(6) Unit of Length 1
  length2 Num(19,6) Length 2
  Len2Unit Int(6) Unit of Length 2
  Volume Num(19,6) Quantity
  VolUnit Int(6) Vol. Unit
  Weight1 Num(19,6) Weight 1
  Wght1Unit Int(6) Unit of Weight 1
  Weight2 Num(19,6) Weight 2
  Wght2Unit Int(6) Unit of Weight 2
  Factor1 Num(19,6) Factor 1
  Factor2 Num(19,6) Factor 2
  Factor3 Num(19,6) Factor 3
  Factor4 Num(19,6) Factor 4
  PackQty Num(19,6) Packing Quantity
  UpdInvntry VarChar(1) Warehouse Update default=Y [Y=Yes, N=No]
  BaseDocNum Int(11) Base Document No.
  BaseAtCard nVarChar(100) Customer/Vendor Base Document
  SWW nVarChar(16) Additional Identifier
  VatSum Num(19,6) Total Tax
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  FinncPriod Int(11) Posting Period ->OFPR
  ObjType nVarChar(20) Object Type default=1470000113 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BlockNum nVarChar(100) Block Number
  ImportLog nVarChar(20) Import Log
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAqcuistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  DistribSum Num(19,6) Distributed Amount
  DstrbSumFC Num(19,6) Distributed Amount (FC)
  DstrbSumSC Num(19,6) Distributed Amount (SC)
  GrssProfit Num(19,6) Row Gross Profit
  GrssProfSC Num(19,6) Row Gross Profit (SC)
  GrssProfFC Num(19,6) Row Gross Profit (FC)
  VisOrder Int(11) Visual Order
  INMPrice Num(19,6) Item's Last Sales Price (OINM)
  PoTrgNum Int(11) PO Target No.
  PoTrgEntry nVarChar(11) PO Target Internal ID
  DropShip VarChar(1) Drop-Ship default=N [Y=Yes, N=No]
  PoLineNum Int(11) PO Target Row No.
  Address nVarChar(254) Address
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type [Y=Regular Tax, N=No Tax, U=Use Tax]
  OrigItem nVarChar(50) Original Item ->OITM
  BackOrdr VarChar(1) Allow Back Order [Y=Yes, N=No]
  FreeTxt nVarChar(100) Free Text
  PickStatus VarChar(1) Pick Status default=N [Y=Picked, N=Not Picked, R=Released for Picking, P=Partially Picked]
  PickOty Num(19,6) Pick Quantity
  PickIdNo Int(11) Pick ID
  TrnsCode Int(6) Shipping Method default=-1 ->OSHP
  VatAppld Num(19,6) Applied Tax
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  BaseQty Num(19,6) Base Quantity
  BaseOpnQty Num(19,6) Base Open Quantity
  VatDscntPr Num(19,6) Tax Discount %
  WtLiable VarChar(1) Withholding Tax Liable [Y=Yes, N=No]
  DeferrTax VarChar(1) Deferred Tax default=N [Y=Yes, N=No]
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatlF Num(19,6) Net Tax Amount
  LineVatS Num(19,6) Net Tax Amount
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value
  CEECFlag VarChar(1) Correction Invoice Was/Should Be default=S [W=Was, S=Should Be]
  ToStock Num(19,6) Corr. Invoice Amt to Inventory
  ToDiff Num(19,6) Corr. Invoice Amount to Diff.
  ExciseAmt Num(19,6) Excise Amount
  TaxPerUnit Num(19,6) Tax per Unit
  TotInclTax Num(19,6) Total Including Tax
  CountryOrg nVarChar(3) Country/Region of Origin
  StckDstSum Num(19,6) Stock Distribution Sum
  ReleasQtty Num(19,6) Released Quantity
  LineType VarChar(1) Row Type default=R [R=Regular]
  TranType VarChar(1) Transaction Type [C=Complete, R=Reject]
  Text Text(16) Text
  OwnerCode Int(11) Document Owner
  StockPrice Num(19,6) Inventory Price
  ConsumeFCT VarChar(1) Consumer Sales Forecast [Y=Yes, N=No]
  LstByDsSum Num(19,6) Last Buy Distribute Sum
  StckINMPr Num(19,6) Stock Inm Price
  LstBINMPr Num(19,6) Last Buy Inventory Journal Pr.
  StckDstFc Num(19,6) Stock Distribution Sum (FC)
  StckDstSc Num(19,6) Stock Distribution Sum (SC)
  LstByDsFc Num(19,6) Last Buy Distribute Sum (FC)
  LstByDsSc Num(19,6) Last Buy Distribute Sum (SC)
  StockSum Num(19,6) Stock Sum
  StockSumFc Num(19,6) Stock Sum FC
  StockSumSc Num(19,6) Stock Sum SC
  StckSumApp Num(19,6) Stock Sum Applied
  StckAppFc Num(19,6) Stock Sum Applied FC
  StckAppSc Num(19,6) Stock Sum Applied SC
  ShipToCode nVarChar(50) Ship-to Code
  ShipToDesc nVarChar(254) Ship-To Description
  StckAppD Num(19,6) Stock Distrib. - Applied Sum
  StckAppDFC Num(19,6) Stock Dist. - Applied Sum (FC)
  StckAppDSC Num(19,6) Stock Dist. - Applied Sum (SC)
  BasePrice VarChar(1) Price for Total Calculation default=E [E=Exclude Tax, I=Include Tax]
  GTotal Num(19,6) Gross Total
  GTotalFC Num(19,6) Gross Total (FC)
  GTotalSC Num(19,6) Gross Total (SC)
  DistribExp VarChar(1) Distribute Freight [Y=Yes, N=No]
  DescOW VarChar(1) Description Overwritten default=N [Y=Yes, N=No]
  DetailsOW VarChar(1) Details Overwritten default=N [Y=Yes, N=No]
  GrossBase Int(6) Base Method for Gross Profit
  VatWoDpm Num(19,6) Tax Before DPM Applied
  VatWoDpmFc Num(19,6) Tax Before DPM Applied (FC)
  VatWoDpmSc Num(19,6) Tax Before DPM Applied (SC)
  CFOPCode nVarChar(6) CFOP Code for Document ->OCFP
  CSTCode nVarChar(6) CST Code for ICMS
  Usage Int(11) Usage Code for Document ->OUSG
  TaxOnly VarChar(1) Tax Only [Y=Yes, N=No]
  WtCalced VarChar(1) Withholding Tax Calculated default=N [N=No, Y=Yes]
  QtyToShip Num(19,6) Quantity to Ship
  DelivrdQty Num(19,6) Delivered Quantity
  OrderedQty Num(19,6) Ordered Quantity
  CogsOcrCod nVarChar(8) COGS Distribution Rule Code ->OOCR
  CiOppLineN Int(11) Line Number of Opposite Line default=-1
  CogsAcct nVarChar(15) COGS Account Code ->OACT
  ChgAsmBoMW VarChar(1) Change Whse for Asm. BoM Child [Y=Yes, N=No]
  ActDelDate Date(8) Actual Delivery Date
  OcrCode2 nVarChar(8) Costing Code 2 ->OOCR
  OcrCode3 nVarChar(8) Costing Code 3 ->OOCR
  OcrCode4 nVarChar(8) Costing Code 4 ->OOCR
  OcrCode5 nVarChar(8) Costing Code 5 ->OOCR
  TaxDistSum Num(19,6) Tax Distributed Amount
  TaxDistSFC Num(19,6) Tax Distributed Amount (FC)
  TaxDistSSC Num(19,6) Tax Distributed Amount (SC)
  PostTax VarChar(1) Post Tax in Price to Stock default=Y [Y=Yes, N=No]
  Excisable VarChar(1) Excisable [Yes/No] [Y=Yes, N=No]
  AssblValue Num(19,6) Assessable Value
  RG23APart1 Int(11) RG23A Part 1 Number
  RG23APart2 Int(11) RG23A Part 2 Number
  RG23CPart1 Int(11) RG23C Part 1 Number
  RG23CPart2 Int(11) RG23C Part 2 Number
  CogsOcrCo2 nVarChar(8) COGS Distribution Rule Code 2 ->OOCR
  CogsOcrCo3 nVarChar(8) COGS Distribution Rule Code 3 ->OOCR
  CogsOcrCo4 nVarChar(8) COGS Distribution Rule Code 4 ->OOCR
  CogsOcrCo5 nVarChar(8) COGS Distribution Rule Code 5 ->OOCR
  LnExcised VarChar(1) Line Excised [O=Open, C=Closed, P=Copied to OEI]
  LocCode Int(11) Location Code ->OLCT
  StockValue Num(19,6) Total COGS Value
  GPTtlBasPr Num(19,6) Total Base Price for Profit
  unitMsr2 nVarChar(100) Purch./Sales UoM if Base Unit
  NumPerMsr2 Num(19,6) Purch./Sls UoM Val. if Bse Unt
  SpecPrice VarChar(1) Price Source Type default=N [Y=Special Prices for Business Partner, N=Manual, W=Active Price List, Discount Groups, R=Active Price List, U=Inactive Price List, A=Blanket Agreement, P=Period and Volume Discounts, Q=Period and Volume Discounts, Discount Groups, V=Inactive Price List, Discount Groups, 9=Special Prices for Business Partner, !=Blanket Agreement, 0=Period and Volume Discounts, 1=Period and Volume Discounts, Discount Groups, 2=Active Price List, 7=Active Price List, Discount Groups, 5=Inactive Price List, 6=Inactive Price List, Discount Groups]
  CSTfIPI nVarChar(2) CST for IPI Code
  CSTfPIS nVarChar(2) CST for PIS Code
  CSTfCOFINS nVarChar(2) CST for COFINS Code
  ExLineNo nVarChar(10) Ex. Line No.
  isSrvCall VarChar(1) Created from Service Call default=N [Y=Yes, N=No]
  PQTReqQty Num(19,6) Purch. Quotation: Required Qty
  PQTReqDate Date(8) Purch. Quotation Required Date
  PcDocType Int(11) Purchase Confirmation Doc Type default=-1 [-1=No Type, 22=Purchase Order, 540000006=Purchase Quotation]
  PcQuantity Num(19,6) Purchase Confirmation Quantity
  LinManClsd VarChar(1) Line Was Closed Manually default=N [Y=Yes, N=No, U=Unknown]
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  NoInvtryMv VarChar(1) Without Inventory Movement default=N [Y=Yes, N=No]
  ActBaseEnt Int(11) Actual Base Document Entry
  ActBaseLn Int(11) Actual Base Line Number
  ActBaseNum Int(11) Actual Base Document No.
  OpenRtnQty Num(19,6) Quantity Open for Return
  AgrNo Int(11) Agreement No. ->OOAT
  AgrLnNum Int(11) Agreement Row Number
  CredOrigin VarChar(1) Credit Origin ->OBSI
  Surpluses Num(19,6) Surpluses
  DefBreak Num(19,6) Defect and Breakup
  Shortages Num(19,6) Shortages
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  UomEntry2 Int(11) UoM Entry if Base Unit default=0 ->OUOM
  UomCode nVarChar(20) UoM Code
  UomCode2 nVarChar(20) UoM Code if Base Unit
  FromWhsCod nVarChar(8) From Warehouse Code ->OWHS
  NeedQty VarChar(1) Consider Quantity of Items default=N [Y=Yes, N=No]
  PartRetire VarChar(1) Partial Retirement default=N [Y=Yes, N=No]
  RetireQty Num(19,6) Retirement Quantity
  RetireAPC Num(19,6) Retirement APC
  RetirAPCFC Num(19,6) Retirement APC FC
  RetirAPCSC Num(19,6) Retirement APC SC
  InvQty Num(19,6) Quantity - Inventory UoM
  OpenInvQty Num(19,6) Open Quantity (Inventory UoM)
  EnSetCost VarChar(1) Enable Set Item Cost in Return default=N [Y=Yes, N=No]
  RetCost Num(19,6) Return Cost in A/R Return
  Incoterms Int(11) Incoterms default=0 ->ODCI
  TransMod Int(11) Transport Mode default=0 ->ODCI
  LineVendor nVarChar(15) Line Vendor Code ->OCRD
  DistribIS VarChar(1) Distribute Intrastat Freight default=N [Y=Yes, N=No]
  ISDistrb Num(19,6) Intrastat Distrib. Amount
  ISDistrbFC Num(19,6) Intrastat Distrib. Amount (FC)
  ISDistrbSC Num(19,6) Intrastat Distrib. Amount (SC)
  IsByPrdct VarChar(1) Item Is By-Product default=N [N=No, Y=Yes]
  ItemType Int(11) Item Type default=4 [4=Item]
  PriceEdit VarChar(1) Price Was Edited by User default=N [N=No, Y=Yes]
  PrntLnNum Int(11) Parent Line Number
  LinePoPrss VarChar(1) Line PO Process default=N [Y=Yes, N=No]
  FreeChrgBP VarChar(1) Free of Charge (BP) default=N [Y=Yes, N=No]
  TaxRelev VarChar(1) Tax Relevant Row default=Y [Y=Yes, N=No]
  LegalText nVarChar(254) Legal Text
  ThirdParty VarChar(1) Third Party default=N [Y=Yes, N=No]
  LicTradNum nVarChar(32) Federal Tax ID
  InvQtyOnly VarChar(1) Change Qty (Inv. UoM) Only default=N [Y=Yes, N=No]
  UnencReasn Int(11) Reason for Unencumbered ICMS
  ShipFromCo nVarChar(50) Ship-From Code
  ShipFromDe nVarChar(254) Ship-From Description
  FisrtBin nVarChar(228) First Bin Location
  AllocBinC nVarChar(11) Allocated Bin Location Count
  ExpType nVarChar(4) Expense Type ->OEXD
  ExpUUID nVarChar(50) Expense UUID
  ExpOpType VarChar(1) Expense Operation Type [P=Professional Services, R=Renting Assets, O=Others]
  DIOTNat nVarChar(3) DIOT Nationality ->OCRY
  MYFtype nVarChar(2) MYF type [S1=MYF Wholesale Sales, S2=Retail Sales, P1=MYF Wholesale Purchases, P3=Other Expense Transactions]
  GPBefDisc Num(19,6) Gross Price
  ReturnRsn Int(6) Return Reason default=-1
  ReturnAct Int(6) Return Action default=-1
  StgSeqNum Int(11) Stage Sequence Number
  StgEntry Int(11) Stage Entry ->ORST
  StgDesc nVarChar(100) Stage Description
  ItmTaxType nVarChar(2) Item GST Tax Category [GR=GST Regular, GN=GST Nil Rated, GE=GST Exempt, NE=Excisable, NN=Non-GST Non-Excisable]
  SacEntry Int(11) SAC Entry ->OSAC
  NCMCode Int(11) NCM Code default=-1 ->ONCM
  HsnEntry Int(11) HSN Entry
  OriBAbsEnt Int(11) Original Base Document Internal ID
  OriBLinNum Int(11) Original Base Document Line Number
  OriBDocTyp Int(11) Original Base Document Type
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No, U=Use]
  EncryptIV nVarChar(100) Encrypt IV
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  StdItemId Int(11) Standard Item Identification ->OUNCL
  CommClass Int(11) Commodity Classification ->OUNCL
  VatExEntry Int(11) VAT Exemption AbsEntry ->OVEB
  VatExLN Int(6) VAT Exemption LineNum
  NatOfTrans Int(11) Nature of Transaction ->ODCI
  ISDtCryImp nVarChar(3) Destination Country/Region for Import ->OCRY
  ISDtRgnImp Int(11) Destination Region for Import ->ODCI
  ISOrCryExp nVarChar(3) Country/Region of Origin for Export ->OCRY
  ISOrRgnExp Int(11) Region of Origin for Export ->ODCI
  NVECode nVarChar(6) NVE Code
  PoNum nVarChar(20) Customer's Purchase Order Number
  PoItmNum Int(11) Customer's Purchase Order Item Number
  IndEscala VarChar(1) Indicator for Relevant Scale default=N [Y=Yes, N=No]
  CESTCode Int(11) CEST Code ->OCEST
  CtrSealQty Num(19,6) Control Seal Quantity
  CNJPMan nVarChar(14) CNPJ of Manufacturer
  UFFiscBene nVarChar(10) UF Fiscal Benefit Code
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]
  LegalTIMD nVarChar(250) Legal Text from Item Master Data
  LegalTTCA nVarChar(250) Legal Text from Tax Code Attributes
  LegalTW nVarChar(250) Legal Text from Warehouse
  LegalTCD nVarChar(250) Legal Text from Tax Code Determination
  RevCharge VarChar(1) Reverse Charge default=N [Y=Yes, N=No]
  ListNum Int(6) Price List No. ->OPLN

# PRQ10 - Purchase Request - Row Structure
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SECONDARY U: DocEntry, AftLineNum, OrderNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OPRQ
  LineSeq Int(11) Row Sequence
  AftLineNum Int(11) After Row Number
  OrderNum Int(11) Order Number
  LineType VarChar(1) Row Type [T=Text, S=Subtotal]
  LineText Text(16) Row Text
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=1470000113 ->ADP1

# PRQ11 - PR - Drawn DPM Detail
Module: Marketing Documents | 70 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LineSeq
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OPRQ
  LineNum Int(11) Row Number
  LineSeq Int(11) Sequence Number
  BaseAbs Int(11) Base Document Internal ID
  BaseType Int(11) Base Object Type default=-1 [-1=]
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  VatPrcnt Num(19,6) VAT Percent
  LineTotal Num(19,6) Net LC
  TotalFrgn Num(19,6) Net FC
  TotalSumSy Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFrgn Num(19,6) Tax FC
  VatSumSys Num(19,6) Tax SC
  ObjType nVarChar(20) Object Type default=1470000113 ->ADP1
  LogInstanc Int(11) Log Instance
  IsAcq VarChar(1) Acquisition Tax-Liable default=N [N=No, Y=Yes]
  IsAllDrawn VarChar(1) Remaining Amount Drawn default=N [Y=Yes, N=No]
  IsGross VarChar(1) IS Gross Line default=N [N=Net Line, Y=Gross Line]
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  ApplNet Num(19,6) Applied Net LC
  ApplNetFc Num(19,6) Applied Net FC
  ApplNetSc Num(19,6) Applied Net SC
  ApplVat Num(19,6) Applied Tax LC
  ApplVatFc Num(19,6) Applied Tax FC
  ApplVatSc Num(19,6) Applied Tax SC
  BaseNet Num(19,6) Base Net LC
  BaseNetFc Num(19,6) Base Net FC
  BaseNetSc Num(19,6) Base Net SC
  BaseVat Num(19,6) Base Tax LC
  BaseVatFc Num(19,6) Base Tax FC
  BaseVatSc Num(19,6) Base Tax SC
  BaseGross Num(19,6) Base Gross LC
  BaseGrossF Num(19,6) Base Gross FC
  BaseGrossS Num(19,6) Base Gross SC
  LineType VarChar(1) Line Type default=D [D=Document Row, R=Currency Rounding, H=Down Payment Document Rounding]
  DctSum Num(19,6) Deductible Sum LC
  DctSumFc Num(19,6) Deductible Sum FC
  DctSumSc Num(19,6) Deductible Sum SC
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplDct Num(19,6) Applied Deductible Sum LC
  ApplDctFc Num(19,6) Applied Deductible Sum FC
  ApplDctSc Num(19,6) Applied Deductible Sum SC
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  BaseDct Num(19,6) Base Deductible Sum LC
  BaseDctFc Num(19,6) Base Deductible Sum FC
  BaseDctSc Num(19,6) Base Deductible Sum SC
  BaseEq Num(19,6) Base Equalization Sum LC
  BaseEqFc Num(19,6) Base Equalization Sum FC
  BaseEqSc Num(19,6) Base Equalization Sum SC
  TaxCode nVarChar(8) Tax Code ->OSTC
  ApplGross Num(19,6) Applied Gross LC
  ApplGrossF Num(19,6) Applied Gross FC
  ApplGrossS Num(19,6) Applied Gross SC
  TaxAdjust VarChar(1) Manual Tax Adjustment default=N [Y=Yes, N=No]
  RvsChrgSum Num(19,6) Reverse Charge Sum LC
  RvsChrgFc Num(19,6) Reverse Charge Sum FC
  RvsChrgSc Num(19,6) Reverse Charge Sum SC
  BasRvsChrg Num(19,6) Base Reverse Charge LC
  BasRvsFc Num(19,6) Base Reverse Charge FC
  BasRvsSc Num(19,6) Base Reverse Charge SC
  ApplRvs Num(19,6) Applied Reverse Charge LC
  ApplRvsFc Num(19,6) Applied Reverse Charge FC
  ApplRvsSc Num(19,6) Applied Reverse Charge SC
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# PRQ12 - Purchase Request - Tax Extension
Module: Marketing Documents | 117 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OPRQ
  TaxId0 nVarChar(100) Tax ID 0
  TaxId1 nVarChar(100) Tax ID 1
  TaxId2 nVarChar(100) Tax ID 2
  TaxId3 nVarChar(100) Tax ID 3
  TaxId4 nVarChar(100) Tax ID 4
  TaxId5 nVarChar(100) Tax ID 5
  TaxId6 nVarChar(100) Tax ID 6
  TaxId7 nVarChar(100) Tax ID 7
  TaxId8 nVarChar(100) Tax ID 8
  TaxId9 nVarChar(100) Tax ID 9
  State nVarChar(3) State Code
  County nVarChar(7) County Code
  Incoterms nVarChar(3) Incoterms
  Vehicle nVarChar(10) Vehicle ID
  VidState nVarChar(3) Vehicle ID (State)
  NfRef nVarChar(254) Nota Fiscal Reference
  Carrier nVarChar(15) Carrier Code
  QoP Int(11) Quantity of Packs
  PackDesc nVarChar(10) Package Description
  Brand nVarChar(20) Brand
  NoSU Int(11) Number of Shipping Unit
  NetWeight Num(19,6) Net Weight
  GrsWeight Num(19,6) Gross Weight
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=1470000113 ->ADP1
  TaxId10 nVarChar(100) Tax ID 10
  TransCat nVarChar(100) Transaction Category
  FormNo nVarChar(100) Form No.
  TaxId11 nVarChar(100) Tax ID 11
  StreetS nVarChar(100) Street
  BlockS nVarChar(100) Block
  BuildingS Text(16) Building/Floor/Room
  CityS nVarChar(100) City
  ZipCodeS nVarChar(20) Zip Code
  CountyS nVarChar(100) County
  StateS nVarChar(3) State ->OCST
  CountryS nVarChar(3) Country/Region ->OCRY
  AddrTypeS nVarChar(100) Address Type
  StreetNoS nVarChar(100) Street No.
  StreetB nVarChar(100) Street
  BlockB nVarChar(100) Block
  BuildingB Text(16) Building/Floor/Room
  CityB nVarChar(100) City
  ZipCodeB nVarChar(20) Zip Code
  CountyB nVarChar(100) County
  StateB nVarChar(3) State ->OCST
  CountryB nVarChar(3) Country/Region ->OCRY
  AddrTypeB nVarChar(100) Address Type
  StreetNoB nVarChar(100) Street No.
  ImpORExp VarChar(1) Import or Export [N=, Y=]
  Vat VarChar(1) VAT default=N [N=No VAT Support, Y=VAT Support]
  AltCrdNamB nVarChar(100) Alternative BP Name
  AltTaxIdB nVarChar(32) Alternative Tax ID
  Address2S nVarChar(50) Address Name 2
  Address3S nVarChar(50) Address Name 3
  Address2B nVarChar(50) Address Name 2
  Address3B nVarChar(50) Address Name 3
  MainUsage Int(11) Main Usage Code of Document ->OUSG
  GlbLocNumS nVarChar(50) Global Location Number
  GlbLocNumB nVarChar(50) Global Location Number
  CollectDT nVarChar(20) Date and Time of Collection
  TransprtDT Date(8) Transport Starting Date
  TransprtRS nVarChar(100) Transport Reason
  TaxId12 nVarChar(50) Tax ID 12
  TaxId13 nVarChar(100) Deductee Ref. No. in India
  ImpExpNo nVarChar(100) Import/Export Bill No.
  ImpExpDate Date(8) Import/Export Date
  BpGSTType Int(11) GST Regn Type of BP
  BpGSTN nVarChar(15) GST Regn No of BP
  BpStateCod nVarChar(3) State Code of Business Partner ->OCST
  BPStatGSTN nVarChar(2) GST State Code of BP
  LocGSTType Int(11) GST Regn Type of Location
  LocGSTN nVarChar(15) GST Regn No of Location
  LocStatCod nVarChar(3) State Code of Location ->OCST
  LocStaGSTN nVarChar(2) GST State Code of Location
  BpCountry nVarChar(3) Country/Region Code of BP ->OCRY
  OrigImpNo nVarChar(100) Original Bill of Entry No.
  OrigImpDat Date(8) Original Bill of Entry Date
  ExportType VarChar(1) Exporting Type default=E [E=Imports/Exports, S=SEZ Developer, U=SEZ Unit, D=Deemed Imports/Exports]
  PortCode nVarChar(100) Port Code
  BoEValue Num(19,6) Bill of Entry Value
  IsIGSTAct VarChar(1) Supply under IGST Account [Y=Yes, N=No]
  ClaimRefun VarChar(1) Claim Refund [Y=Yes, N=No]
  TaxRateDif Int(11) Differential % of Tax Rate [65=, 100=]
  BPGdsIssP nVarChar(15) Goods Issue Place BP
  CNPJGIP nVarChar(100) Goods Issue Place CNPJ
  CPFGIP nVarChar(100) Goods Issue Place CPF
  StreetGIP nVarChar(100) Goods Issue Place Street
  StrtNoGIP nVarChar(100) Goods Issue Place Street No.
  BldngGIP Text(16) Goods Issue Place Building
  ZipGIP nVarChar(20) Goods Issue Place Zip Code
  BlockGIP nVarChar(100) Goods Issue Place Block
  CityGIP nVarChar(100) Goods Issue Place City
  CountyGIP nVarChar(100) Goods Issue Place County
  StateGIP nVarChar(3) Goods Issue Place State ->OCST
  CountryGIP nVarChar(3) Goods Issue Place Country/Region ->OCRY
  PhoneGIP nVarChar(20) Goods Issue Place Phone
  EMailGIP nVarChar(100) Goods Issue Place E-Mail
  DptDateGIP Date(8) Goods Issue Place Departure Date
  BPDelivryP nVarChar(15) Delivery Place BP
  CNPJDlvryP nVarChar(100) Delivery Place CNPJ
  CPFDlvryP nVarChar(100) Delivery Place CPF
  StrtDlvryP nVarChar(100) Delivery Place Street
  StrNoDlvrP nVarChar(100) Delivery Place Street No.
  BldDlvryP Text(16) Delivery Place Building
  ZipDlvryP nVarChar(20) Delivery Place Zip Code
  BlckDlvryP nVarChar(100) Delivery Place Block
  CityDlvryP nVarChar(100) Delivery Place City
  CntyDlvryP nVarChar(100) Delivery Place County
  StatDlvryP nVarChar(3) Delivery Place State ->OCST
  CtryDlvryP nVarChar(3) Delivery Place Country/Region ->OCRY
  FoneDlvryP nVarChar(20) Delivery Place Phone
  MailDlvryP nVarChar(100) Delivery Place E-Mail
  DpDtDlvryP Date(8) Delivery Place Departure Date
  AuthedCNPJ nVarChar(250) Authorized CNPJ or CPF
  TaxId14 nVarChar(250) ITR Filing

# PRQ13 - Purchase Request Rows - Distributed Expenses
Module: Marketing Documents | 59 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OPRQ
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=1470000113 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Aquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Normal Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) VAT Applied Foreign
  VatAppldSC Num(19,6) VAT Applied System
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock default=N [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs. Entry default=-1
  BaseType Int(11) Base Document Type
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Line No.
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Abs. Entry default=-1
  BaseGroup Int(11) Base Document Group default=-1
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1
  VisOrder Int(11) Visual Order
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DistribExp VarChar(1) Distribute Freights [Y=Yes, N=No]
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ

# PRQ14 - Purchase Request - Assembly - Rows
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPRQ
  LineNum Int(11) Row Number default=-1
  ChildNum Int(11) Child Number default=-1
  ItemCode nVarChar(50) Item No. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  TotalQty Num(19,6) Total Quantity
  OpenQty Num(19,6) Remaining Open Quantity
  ObjectType nVarChar(20) Object Type default=1470000113 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BaseChildN Int(11) Base Child Number default=-1
  EncryptIV nVarChar(100) Encrypt IV

# PRQ15 - PR - Drawn DPM Applied
Module: Marketing Documents | 84 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OPRQ
  LineNum Int(11) Row Number
  ObjType nVarChar(20) Object Type default=1470000113 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  StaCode nVarChar(8) Tax Authority Code
  StaType Int(11) Tax Authority Type
  StaIndex Int(11) Tax Authority Seq Index
  BaseNet Num(19,6) Net LC
  BaseNetFc Num(19,6) Net FC
  BaseNetSc Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFc Num(19,6) Tax FC
  VatSumSc Num(19,6) Tax SC
  DctSum Num(19,6) Deductible Sum LC
  DctSumFc Num(19,6) Deductible Sum FC
  DctSumSc Num(19,6) Deductible Sum SC
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplNet Num(19,6) Applied Net LC
  ApplNetFc Num(19,6) Applied Net FC
  ApplNetSc Num(19,6) Applied Net SC
  ApplVat Num(19,6) Applied Tax LC
  ApplVatFc Num(19,6) Applied Tax FC
  ApplVatSc Num(19,6) Applied Tax SC
  ApplDct Num(19,6) Applied Deductible Sum LC
  ApplDctFc Num(19,6) Applied Deductible Sum FC
  ApplDctSc Num(19,6) Applied Deductible Sum SC
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  PaidNet Num(19,6) Paid Net LC
  PaidNetFc Num(19,6) Paid Net FC
  PaidNetSc Num(19,6) Paid Net SC
  PaidVat Num(19,6) Paid Tax LC
  PaidVatFc Num(19,6) Paid Tax FC
  PaidVatSc Num(19,6) Paid Tax SC
  PaidDct Num(19,6) Paid Deductible Sum LC
  PaidDctFc Num(19,6) Paid Deductible Sum FC
  PaidDctSc Num(19,6) Paid Deductible Sum SC
  PaidEq Num(19,6) Paid Equalization Sum LC
  PaidEqFc Num(19,6) Paid Equalization Sum FC
  PaidEqSc Num(19,6) Paid Equalization Sum SC
  DpApplNet Num(19,6) Dpm Appl Net LC
  DpApplNetF Num(19,6) Dpm Appl Net FC
  DpApplNetS Num(19,6) Dpm Appl Net SC
  DpApplVat Num(19,6) Dpm Appl Tax LC
  DpApplVatF Num(19,6) Dpm Appl Tax FC
  DpApplVatS Num(19,6) Dpm Appl Tax SC
  DpApplDct Num(19,6) Dpm Appl Deductible Sum LC
  DpApplDctF Num(19,6) Dpm Appl Deductible Sum FC
  DpApplDctS Num(19,6) Dpm Appl Deductible Sum SC
  DpApplEq Num(19,6) Dpm Appl Equalization Sum LC
  DpApplEqFc Num(19,6) Dpm Appl Equalization Sum FC
  DpApplEqSc Num(19,6) Dpm Appl Equalization Sum SC
  TaxCode nVarChar(8) Tax Code ->OSTC
  LineType VarChar(1) Row Type default=D [D=Document, R=Exchange Rate Rounding, H=Document Header Rounding]
  BaseGrs Num(19,6) Gross LC
  BaseGrsFc Num(19,6) Gross FC
  BaseGrsSc Num(19,6) Gross SC
  ApplGrs Num(19,6) Applied Gross LC
  ApplGrsFc Num(19,6) Applied Gross FC
  ApplGrsSc Num(19,6) Applied Gross SC
  PaidGrs Num(19,6) Paid Gross LC
  PaidGrsFc Num(19,6) Paid Gross FC
  PaidGrsSc Num(19,6) Paid Gross SC
  DpApplGrs Num(19,6) Dpm Appl Gross LC
  DpApplGrsF Num(19,6) Dpm Appl Gross FC
  DpApplGrsS Num(19,6) Dpm Appl Gross SC
  RvsChrgSum Num(19,6) Reverse Charge Sum
  RvsChrgSc Num(19,6) Reverse Charge Sum (SC)
  RvsChrgFc Num(19,6) Reverse Charge Sum (FC)
  ApplRvs Num(19,6) Applied Reverse Charge Sum LC
  ApplRvsSc Num(19,6) Applied Reverse Charge Sum SC
  ApplRvsFc Num(19,6) Applied Reverse Charge Sum FC
  PaidRvs Num(19,6) Paid Reverse Charge Sum LC
  PaidRvsSc Num(19,6) Paid Reverse Charge Sum SC
  PaidRvsFc Num(19,6) Paid Reverse Charge Sum FC
  DpApplRvs Num(19,6) Dpm Applied Reverse Charge LC
  DpApplRvsS Num(19,6) Dpm Applied Reverse Charge SC
  DpApplRvsF Num(19,6) Dpm Applied Reverse Charge FC
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# PRQ16 - Purchase Request - SnB Properties
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, SnBIndex
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Abs. Entry ->OPRQ
  LineNum Int(11) Line Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object ID
  ObjAbs Int(11) Object Abs.
  DrfWObjAbs Int(11) Draft Wobj. Abs. default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Sub-Row Number default=-1
  ObjType nVarChar(20) Object Type default=1470000113
  LogInstanc Int(11) Log Instance

# PRQ17 - Purchase Request - Bin Allocation Data
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OPRQ
  LineNum Int(11) Bin Allocation Sequence
  LogInstanc Int(11) Line Number default=0
  ObjectType nVarChar(20) Subline Number default=1470000113 ->ADP1
  ImpDocType VarChar(1) SnB Type ->OBSI
  ImpDocNum nVarChar(10) SnB Master Data Internal No.
  DateOfReg Date(8) Bin Internal Number
  CustClrDat Date(8) Quantity
  ConcActNum nVarChar(30) Item Code
  AdditNum nVarChar(30) Warehouse Code
  AddItmDV Num(19,6) Object Type
  tpVTransp Int(6) Overland Transport Route [1=Maritime, 2=Waterway, 3=Lakeside, 4=Air, 5=Post, 6=Train, 7=Road, 8=Network Transmission, 9=Own Means, 10=Input/Output Fictitious, 11=Courier, 12=Hand Carry]
  DrawSReg nVarChar(11) Drawback - Suspension Regime
  AddFrNavyA Num(19,6) Additional Freight to Navy Authority
  TypeOfImp VarChar(1) Type of Import
  nSeqAdic Int(6) Additional Item Sequential Number

# PRQ18 - Purchase Request - Export Process
Module: Marketing Documents | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPRQ
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=1470000113 ->ADP1
  ExpDocType Int(11) Exportation Document Type default=-1 ->OBNI
  ExpDeclNum Int(11) Exportation Declaration Number
  ExpDeclDat Date(8) Exportation Declaration Date
  ExpNature Int(11) Exportation Nature default=-1 ->OBNI
  ExpRegNum Int(11) Exportation Registry Number
  ExpRegDate Date(8) Exportation Registry Date
  LadBillNum nVarChar(19) Bill of Lading Number
  LadBillDat Date(8) Bill of Lading Date
  MerchLeftD Date(8) Date Merchandise Left Customs
  LadBillTyp Int(11) Bill of Lading Type default=-1 ->OBNI
  DrawSReg nVarChar(11) Drawback - Suspension Regime
  NatureExp nVarChar(44) Nature of Export
  QultExpItm Num(19,6) Quantity of Exported Items
  nSeqAdic Int(6) Additional Item Sequential Number

# PRQ19 - Purchase Request - Bin Allocation Data
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, BinAllocSe
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OPRQ
  BinAllocSe Int(11) Bin Allocation Sequence
  LineNum Int(11) Line Number
  SubLineNum Int(11) Subline Number default=-1
  SnBType Int(11) SnB Type default=-1
  SnBMDAbs Int(11) SnB Master Data Internal No. default=-1
  BinAbs Int(11) Bin Internal Number ->OBIN
  Quantity Num(19,6) Quantity
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjType nVarChar(20) Object Type default=1470000113 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  BinActTyp Int(6) Bin Action Type [1=Transaction In, 2=Transaction Out, 4=SnB Complete, 8=Bin First Then SnB]

# PRQ2 - Purchase Request - Freight - Rows
Module: Marketing Documents | 64 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OPRQ
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=1470000113 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) VAT Applied Foreign
  VatAppldSC Num(19,6) VAT Applied System
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report [Y=Yes, N=No]
  BaseGroup Int(11) Base Document Group default=-1 [-1=, 0=, 1=, 2=]
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1 [-1=, 0=, 1=, 2=]
  VisOrder Int(11) Visual Order
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]

# PRQ20 - Intrastat Expenses
Module: Marketing Documents | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPRQ
  ExpnsCode Int(11) Freight Code ->OEXD
  TotalLC Num(19,6) Total
  TotalFC Num(19,6) Total (FC)
  TotalSC Num(19,6) Total (SC)
  DistribM VarChar(1) Distribution Method default=T [Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DrawnLC Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  LineNum Int(11) Line Number default=-1
  BaseAbsEnt Int(11) Base Abs. Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 16=Return, 13=A/R Invoice, 203=Down Payment Incoming, 204=Down Payment Outgoing, 22=Purchase Order, 20=Goods Receipt PO, 21=Goods Return, 18=A/P Invoice, 540000006=Purchase Quotation, 0=, -1=]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No. default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=1470000113 ->ADP1
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  AppliedLC Num(19,6) Applied
  AppliedFC Num(19,6) Applied (FC)
  AppliedSC Num(19,6) Applied (SC)

# PRQ21 - Purchase Request - Document Reference Information
Module: Marketing Documents | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, RefType
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjectType nVarChar(20) Object Type default=1470000113
  LogInstanc Int(11) Log Instance default=0
  RefType VarChar(1) Reference Types default=S [S=System Document, E=External Document]
  LineNum Int(11) Line Number
  RefDocEntr Int(11) Referenced Internal Number
  RefDocNum Int(11) Referenced Document Number
  ExtDocNum nVarChar(100) External Referenced Document Number
  RefObjType nVarChar(20) Referenced Object Type [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 234000031=Return Request, 16=Return, 203=A/R Down Payment, 13=A/R Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 280=A/R Tax Invoice, 1470000113=Purchase Request, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Return Request, 21=Goods Return, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 281=A/P Tax Invoice, 69=Landed Costs, 24=Incoming Payments, 46=Outgoing Payments, 57=Checks for Payment, 321=Internal Reconciliation, 34=Recurring Posting, 30=Journal Entry, 59=Goods Receipt, 60=Goods Issue, 162=Inventory Revaluation, 1470000065=Inventory Counting, 10000071=Inventory Posting, 1250000001=Inventory Transfer Request, 67=Inventory Transfer, 202=Production Order, 13001=Original Invoice, -1=External Document, 20301=Original Down Payment Invoice]
  AccessKey nVarChar(100) Access Key
  IssueDate Date(8) Date of Issue
  IssuerCNPJ nVarChar(100) Issuer CNPJ
  IssuerCode nVarChar(10) Fiscal Document Issuer UF Code
  Model nVarChar(6) Fiscal Document Model
  Series nVarChar(3) Fiscal Document Series
  Number Int(11) Fiscal Document Number
  RefAccKey nVarChar(100) Referenced CT-e Access Key
  RefAmount Num(19,6) Referenced Amount
  SubSeries nVarChar(3) Fiscal Document Subseries
  Remark nVarChar(254) Remarks
  LinkRefTyp nVarChar(20) Link Reference Type default=00 [00=, 01=Nota de cr�dito de los documentos relacionados, 02=Nota de d�bito de los documentos relacionados, 03=Devoluci�n de mercanc�a sobre facturas o traslados previos, 04=Sustituci�n de los CFDI previos, 05=Traslados de mercancias facturados previamente, 06=Factura generada por los traslados previos, 07=CFDI por aplicaci�n de anticipo, 08=Customs, MX_08=Factura generada por pagos en parcialidades, 09=Factura generada por pagos diferidos]

# PRQ22 - Purchase Request - Resource Costs
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, StdCostNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->PRQ1
  LineNum Int(11) Row Number ->PRQ1
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=1470000113
  LogInstanc Int(11) Log Instance default=0

# PRQ23 - A/P Invoice - Selected Asset Master Data
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, VisOrder
  ASSETS: DocEntry, LineNum, AssetCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPRQ
  LineNum Int(11) Row Number
  AssetCode nVarChar(50) Selected Asset Code ->OITM
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Remarks nVarChar(100) Remarks
  Amount Num(19,6) Amount
  AmountSC Num(19,6) Amount (SC)
  SerialNo nVarChar(30) Serial Number
  VisOrder Int(11) Visual Order
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=1470000113 ->ADP1

# PRQ24 - Purchase Request - Tracking Note Assignment
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  ItemCCDNum nVarChar(40) Item CCD Number
  CntrOrigin nVarChar(3) Country/Region of Origin
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=1470000113 ->ADP1
  SubLineNum Int(11) BOM Line No.

# PRQ25 - Purchase Request - Amt Per VAT Grp
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, VatGroup, Type
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  VatGroup nVarChar(8) Tax Definition ->OVTG
  VatPrcnt Num(19,6) Tax Rate
  BaseAmnt Num(19,6) Base Amount
  BaseAmntFC Num(19,6) Base Amount (FC)
  BaseAmntSC Num(19,6) Base Amount (SC)
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  Type Int(11) Type default=1 [1=Discount by Tax]
  Currency nVarChar(3) Price Currency
  Rate Num(19,6) Currency Rate
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=1470000113 ->ADP1

# PRQ26 - Purchase Request - E-Way Bill Information
Module: Marketing Documents | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPRQ
  SuplyType nVarChar(20) EWB Transaction Type [O=Outward, I=Inward]
  SubSplyTyp Int(11) EWB Sub-Type ->OEST
  DocType nVarChar(3) EWB Doc. Type ->OEDT
  TransMode Int(11) EWB Transportation Mode ->OETM
  Distance Num(19,6) EWB Transport Distance
  TransDocNo nVarChar(16) EWB Transporter Doc. No.
  TransDate Date(8) EWB Transportation Date
  VehicleTyp nVarChar(2) EWB Vehicle Type ->OEVT
  VehicleNo nVarChar(15) EWB Vehicle Number
  EWayBillNo nVarChar(20) EWB No.
  EwbDate Date(8) E-Way Bill Date
  FrmTraName nVarChar(100) EWB Consignor Name
  FrmAddres1 nVarChar(120) EWB Consignor Address 1
  FrmAddres2 nVarChar(120) EWB Consignor Address 2
  FrmZipCode nVarChar(20) EWB Consignor Zip Code
  ActFrmStat nVarChar(2) Dispatch State of EWB Consignor
  ToTraName nVarChar(100) EWB Consignee Name
  ToAddres1 nVarChar(120) EWB Consignee Address 1
  ToAddres2 nVarChar(120) EWB Consignee Address 2
  ToZipCode nVarChar(20) EWB Consignee Zip Code
  ActToState nVarChar(2) Ship-To State of EWB Consignee
  FrmGSTN nVarChar(15) EWB Consignor GSTN
  FrmState nVarChar(2) Bill-To State of EWB Consignor
  ToGSTN nVarChar(15) EWB Consignee GSTN
  ToState nVarChar(2) Bill-To State of EWB Consignee
  MainHsnEnt Int(11) EWB Main HSN Entry ->OCHP
  FrmPlace nVarChar(50) EWB Consignor Place
  ToPlace nVarChar(50) EWB Consignee Place
  TransID nVarChar(15) EWB Transporter ID
  TransName nVarChar(25) EWB Transporter Name
  ExpireDate Date(8) EWB Expiration Date
  ObjectType nVarChar(20) Object Type default=1470000113 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TspEntry Int(11) Transporter Abs. Entry ->OTSP
  TspLine Int(11) Transportation Line
  TransType Int(11) Transaction Type [1=Regular, 2=Bill To-Ship To, 3=Bill From-Dispatch From, 4=Combination of 2 and 3]

# PRQ27 - Purchase Request - E-Books(GR) Rows
Module: Marketing Documents | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  RELATE_ROW: DocEntry, RelateType, RelateLine, GroupNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPRQ
  LineNum Int(11) Row Number
  RelateType Int(11) Relation Type default=-1 [1=Row, 2=Row Expenses, 3=Document Expenses, 13=Distributed Freights, -1=Manual]
  RelateLine Int(11) Relation Row Number default=-1
  GroupNum Int(11) Group Number default=-1
  LineTotal Num(19,6) Line Total
  LineTotalF Num(19,6) Line Total (FC)
  LineTotalS Num(19,6) Line Total (SC)
  InClassTyp Int(11) Income Classification Type ->OICP
  InClassCat Int(11) Income Classification Category ->OICC
  ExClassTyp Int(11) Expense Classification Type ->OECP
  ExClassCat Int(11) Expense Classification Cat. ->OECC
  VatCate Int(11) VAT Category
  NetValue Num(19,6) Net Value
  NetValueFC Num(19,6) Net Value (FC)
  NetValueSC Num(19,6) Net Value (SC)
  VatAmount Num(19,6) VAT Amount
  VatAmFC Num(19,6) VAT Amount (FC)
  VatAmSC Num(19,6) VAT Amount (SC)
  WtPercCat Int(11) Withheld Percentage Category
  WtAmount Num(19,6) Withheld Amount
  WtAmountFC Num(19,6) Withheld Amount (FC)
  WtAmountSC Num(19,6) Withheld Amount (SC)
  ObjectType nVarChar(20) Object Type default=13 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  WtCategory VarChar(1) Withheld Category [I=Invoice, P=Payment]
  VATClassTy Int(11) VAT Classification Type ->OECP
  VATClassCa Int(11) VAT Classification Category ->OECC
  EBVatExCau Int(11) VAT Exemption Cause ->OVEC

# PRQ28 - Purchase Request - Reported Tracking Note
Module: Marketing Documents | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
  TCN_KEY U: DocEntry, LineNum, TrackingNt, TrackiNtLn
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  UnusedQty Num(19,6) Unused Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=1470000113 ->ADP1
  SubLineNum Int(11) BOM Line No.

# PRQ3 - Purchase Request - Freight
Module: Marketing Documents | 80 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  DOCUMENT: DocEntry, BaseAbsEnt
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OPRQ
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  Comments nVarChar(100) Remarks
  ObjType nVarChar(20) Object Type default=1470000113 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  WTLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatF Num(19,6) Net Tax Amount (FC)
  LineVatS Num(19,6) Net Tax Amount (SC)
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs. Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 17=Sales Order]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No.
  LineNum Int(11) Line Number default=-1
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Doc. Internal No. default=-1
  StDstr Num(19,6) Stock Distributed Sum
  StDstrSC Num(19,6) Stock Distributed Sum (SC)
  StDstrFC Num(19,6) Stock Distributed Sum (FC)
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  TaxDistMtd VarChar(1) Tax Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  GrsAmount Num(19,6) Gross Amount
  GrsFC Num(19,6) Gross Amount (FC)
  GrsSC Num(19,6) Gross Amount (SC)
  BaseTotal VarChar(1) Base Total for Calculation default=N [N=Net Total, G=Gross Total]
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)
  RRVatLC Num(19,6) Return Request VAT Amount
  RRVatFC Num(19,6) Return Request VAT Amount (FC)
  RRVatSC Num(19,6) Return Request VAT Amount (SC)
  EncryptIV nVarChar(100) Encrypt IV
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]

# PRQ4 - Purchase Request - Tax Amount per Document
Module: Marketing Documents | 61 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SCONDARY: DocEntry, LineNum, GroupNum, ExpnsCode, StcCode, StaCode, staType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OPRQ
  LineNum Int(11) Row Number default=-1
  GroupNum Int(11) Group Number default=-1
  ExpnsCode Int(11) Expense Code default=-1 ->OEXD
  RelateType Int(11) Relation Type default=1 [1=Row, 2=Row Freight Charges, 3=Document Expenses, 13=Distributed Freights]
  StcCode nVarChar(8) Tax Code ->OSTC
  StaCode nVarChar(8) Authority Code ->OSTA
  staType Int(11) Authority Type ->OSTT
  TaxRate Num(19,6) Tax Rate
  TaxAcct nVarChar(15) Tax Account ->OACT
  TaxSum Num(19,6) Tax Amount
  TaxSumFrgn Num(19,6) Tax Amount (FC)
  TaxSumSys Num(19,6) Tax Amount (SC)
  BaseSum Num(19,6) Base Amount
  BaseSumFrg Num(19,6) Base Amount (FC)
  BaseSumSys Num(19,6) Base Amount (SC)
  ObjectType nVarChar(20) Object Type default=1470000113 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Status default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  LineSeq Int(11) Line Sequence
  DeferrAcct nVarChar(15) Deferred Tax Account ->OACT
  BaseType Int(11) Base Document Type default=-1
  BaseAbs Int(11) Base Doc. Abs. Entry default=-1
  BaseSeq Int(11) Base Doc. Line Sequence
  DeductTax Num(19,6) Deductible Tax Amount
  DdctTaxFrg Num(19,6) Deductible Tax Amount (FC)
  DdctTaxSys Num(19,6) Deductible Tax Amount (SC)
  BaseAppld Num(19,6) Applied Base Amount
  BaseApldFC Num(19,6) Applied Base Amount (FC)
  BaseApldSC Num(19,6) Applied Base Amount (SC)
  NonDdctPrc Num(19,6) Non Deductible %
  NonDdctAct nVarChar(15) Non Deductible Account ->OACT
  TaxInPrice VarChar(1) Tax Included in Price default=N [Y=Yes, N=No]
  Exempt VarChar(1) Exempt default=N [Y=Yes, N=No]
  TaxExpAct nVarChar(15) Expense Account for Tax ->OACT
  OnHoldTax Num(19,6) On Hold Tax Amount
  OnHoldTaxF Num(19,6) On Hold Tax Amount (FC)
  OnHoldTaxS Num(19,6) On-Hold Tax Amount (SC)
  InGrossRev VarChar(1) Included in Gross Revenue default=N [Y=Yes, N=No]
  TaxSumOrg Num(19,6) Tax Amount Original
  TaxSumOrgF Num(19,6) Tax Amount Original (FC)
  TaxSumOrgS Num(19,6) Tax Amount Original (SC)
  OpenTax Num(19,6) Open Service Tax
  OpenTaxFC Num(19,6) Open Service Tax (FC)
  OpenTaxSC Num(19,6) Open Service Tax (SC)
  Unencumbrd VarChar(1) Unencumbered default=N [Y=Yes, N=No]
  TaxOnRI VarChar(1) Tax On Reserve Invoice default=N [Y=Yes, N=No]
  RvsChrgPrc Num(19,6) Reverse Charge %
  RvsChrgTax Num(19,6) Reverse Charge Tax Amount
  RvsChrgSC Num(19,6) Reverse Charge Tax Amount (SC)
  RvsChrgFC Num(19,6) Reverse Charge Tax Amount (FC)
  InFirstIns VarChar(1) Included in First Installment default=N [Y=Yes, N=No]
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CESTrel VarChar(1) CEST Relevant default=N [Y=, N=]

# PRQ5 - Purchase Request - Withholding Tax
Module: Marketing Documents | 158 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  SECONDERY U: AbsEntry, WTCode, BaseAbsEnt, Doc1LineNo
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator ->OPRQ
  WTCode nVarChar(4) WT Code ->OWHT
  Rate Num(19,6) Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntSC Num(19,6) Taxable Amount in SC
  TxblAmntFC Num(19,6) Taxable Amount in FC
  WTAmnt Num(19,6) WT Amount
  WTAmntSC Num(19,6) WT Amount (SC)
  WTAmntFC Num(19,6) WT Amount (FC)
  ApplAmnt Num(19,6) Applied WT Amount
  ApplAmntSC Num(19,6) Applied WTax Amount (SC)
  ApplAmntFC Num(19,6) Applied WTax Amount (FC)
  Category VarChar(1) Category [P=Payment, I=Invoice]
  Criteria VarChar(1) Criteria [Y=Accrual, N=Cash]
  Account nVarChar(15) G/L Account ->OACT
  Type VarChar(1) Withholding Type [V=VAT Withholding, I=Income Tax Withholding]
  RoundType VarChar(1) Rounding Type [T=Truncated, C=Commercial Values]
  BaseType VarChar(1) Base Type [G=Gross, N=Net, V=VAT, U=UoM]
  BaseAbsEnt Int(11) Base Abs. Entry default=-1
  BaseLine Int(11) Base Line
  BaseNum Int(11) Base Document Type default=-1 [-1=, 0=, 17=Sales Order]
  LineNum Int(11) Line Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Abs. Entry default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=1470000113 ->ADP1
  Doc1LineNo Int(11) Doc. 1 - Line Number default=-1
  WtLineType VarChar(1) WT Line Type default=D [D=Document Level WTax, L=Row Level WTax]
  TxblCurr nVarChar(3) Taxable Currency from Doc Line
  DtblCurr nVarChar(3) Deductible Currency
  DtblRate Num(19,6) Rate for Deductible Amount
  txblRate Num(19,6) Rate for Taxable Amount
  DtblAmount Num(19,6) Deductible Amount
  TdsAcc nVarChar(15) TDS Account ->OACT
  SurAcc nVarChar(15) Surcharge Account ->OACT
  CessAcc nVarChar(15) Cess Account ->OACT
  HscAcc nVarChar(15) HSC Account ->OACT
  TdsRate Num(19,6) TDS Rate
  SurRate Num(19,6) Surcharge Rate
  CessRate Num(19,6) Cess Rate
  HscRate Num(19,6) HSC Rate
  TdsBAmt Num(19,6) TDS Base Amount
  TdsBAmtSC Num(19,6) TDS Base Amount (SC)
  TdsBAmtFC Num(19,6) TDS Base Amount (FC)
  SurBAmt Num(19,6) Surcharge Base Amount
  SurBAmtSC Num(19,6) Surcharge Base Amount (SC)
  SurBAmtFC Num(19,6) Surcharge Base Amount (FC)
  CessBAmt Num(19,6) Cess Base Amount
  CessBAmtSC Num(19,6) Cess Base Amount (SC)
  CessBAmtFC Num(19,6) Cess Base Amount (FC)
  HscBAmt Num(19,6) HSC Base Amount
  HscBAmtSC Num(19,6) HSC Base Amount (SC)
  HscBAmtFC Num(19,6) HSC Base Amount (FC)
  TdsAmnt Num(19,6) TDS Tax Amount
  TdsAmntSC Num(19,6) TDS Tax Amount (SC)
  TdsAmntFC Num(19,6) TDS Tax Amount (FC)
  SurAmnt Num(19,6) Surcharge Tax Amount
  SurAmntSC Num(19,6) Surcharge Tax Amount (SC)
  SurAmntFC Num(19,6) Surcharge Tax Amount (FC)
  CessAmnt Num(19,6) Cess Tax Amount
  CessAmntSC Num(19,6) Cess Tax Amount (SC)
  CessAmntFC Num(19,6) Cess Tax Amount (FC)
  HscAmnt Num(19,6) HSC Tax Amount
  HscAmntSC Num(19,6) HSC Tax Amount (SC)
  HscAmntFC Num(19,6) HSC Tax Amount (FC)
  TdsAppl Num(19,6) Applied TDS Amount
  TdsApplSC Num(19,6) Applied TDS Amount (SC)
  TdsApplFC Num(19,6) Applied TDS Amount (FC)
  SurAppl Num(19,6) Applied Surcharge Amount
  SurApplSC Num(19,6) Applied Surcharge Amount (SC)
  SurApplFC Num(19,6) Applied Surcharge Amount (FC)
  CessAppl Num(19,6) Applied Cess Amount
  CessApplSC Num(19,6) Applied Cess Amount (SC)
  CessApplFC Num(19,6) Applied Cess Amount (FC)
  HscAppl Num(19,6) Applied HSC Amount
  HscApplSC Num(19,6) Applied HSC Amount (SC)
  HscApplFC Num(19,6) Applied HSC Amount (FC)
  BatchNum Int(11) Journal Voucher No.
  InCSTCode nVarChar(2) CST Code Incoming
  OutCSTCode nVarChar(2) CST Code Outgoing
  DpmWTApl Num(19,6) DPM WT Applied Amount
  DpmWTAplSC Num(19,6) DPM WT Applied Amount (SC)
  DpmWTAplFC Num(19,6) DPM WT Applied Amount (FC)
  WTTypeId Int(11) WT Type Id ->OWTT
  LnBsAmt Num(19,6) BR Line WT Base Amount
  LnBsAmtSC Num(19,6) BR Line WT Base Amount(SC)
  LnBsAmtFC Num(19,6) BR Line WT Base Amount(FC)
  LnCmTAmt Num(19,6) BR Line Cumulated Taxable Amount
  LnCmTAmtSC Num(19,6) BR Line Cumulated Taxable Amount(SC)
  LnCmTAmtFC Num(19,6) BR Line Cumulated Taxable Amount(FC)
  TDSType VarChar(1) TDS Type [E=eTDS, D=GST TDS, C=GST TCS, S=SALES TCS]
  IgstAcc nVarChar(15) IGST Account ->OACT
  CgstAcc nVarChar(15) CGST Account ->OACT
  SgstAcc nVarChar(15) SGST Account ->OACT
  IgstAmnt Num(19,6) IGST Tax Amount
  IgstAmntSC Num(19,6) IGST Tax Amount (SC)
  IgstAmntFC Num(19,6) IGST Tax Amount (FC)
  CgstAmnt Num(19,6) CGST Tax Amount
  CgstAmntSC Num(19,6) CGST Tax Amount (SC)
  CgstAmntFC Num(19,6) CGST Tax Amount (FC)
  SgstAmnt Num(19,6) SGST Tax Amount
  SgstAmntSC Num(19,6) SGST Tax Amount (SC)
  SgstAmntFC Num(19,6) SGST Tax Amount (FC)
  IgstRate Num(19,6) IGST Rate
  CgstRate Num(19,6) CGST Rate
  SgstRate Num(19,6) SGST Rate
  IgstBAmt Num(19,6) IGST Base Amount
  IgstBAmtSC Num(19,6) IGST Base Amount (SC)
  IgstBAmtFC Num(19,6) IGST Base Amount (FC)
  CgstBAmt Num(19,6) CGST Base Amount
  CgstBAmtSC Num(19,6) CGST Base Amount (SC)
  CgstBAmtFC Num(19,6) CGST Base Amount (FC)
  SgstBAmt Num(19,6) SGST Base Amount
  SgstBAmtSC Num(19,6) SGST Base Amount (SC)
  SgstBAmtFC Num(19,6) SGST Base Amount (FC)
  IgstAppl Num(19,6) Applied IGST Amount
  IgstApplSC Num(19,6) Applied IGST Amount (SC)
  IgstApplFC Num(19,6) Applied IGST Amount (FC)
  CgstAppl Num(19,6) Applied CGST Amount
  CgstApplSC Num(19,6) Applied CGST Amount (SC)
  CgstApplFC Num(19,6) Applied CGST Amount (FC)
  SgstAppl Num(19,6) Applied SGST Amount
  SgstApplSC Num(19,6) Applied SGST Amount (SC)
  SgstApplFC Num(19,6) Applied SGST Amount (FC)
  UtgstAcc nVarChar(15) UTGST Account ->OACT
  CsgstAcc nVarChar(15) Cess GST Account ->OACT
  UtgstAmt Num(19,6) UTGST Tax Amount
  UtgstAmtSC Num(19,6) UTGST Tax Amount (SC)
  UtgstAmtFC Num(19,6) UTGST Tax Amount (FC)
  CsgstAmt Num(19,6) Cess GST Tax Amount
  CsgstAmtSC Num(19,6) Cess GST Tax Amount (SC)
  CsgstAmtFC Num(19,6) Cess GST Tax Amount (FC)
  UtgstRate Num(19,6) UTGST Rate
  CsgstRate Num(19,6) Cess GST Rate
  UtgstBAmt Num(19,6) UTGST Base Amount
  UtgstBAmtS Num(19,6) UTGST Base Amount (SC)
  UtgstBAmtF Num(19,6) UTGST Base Amount (FC)
  CsgstBAmt Num(19,6) Cess GST Base Amount
  CsgstBAmtS Num(19,6) Cess GST Base Amount (SC)
  CsgstBAmtF Num(19,6) Cess GST Base Amount (FC)
  UtgstAppl Num(19,6) Applied UTGST Amount
  UtgstApplS Num(19,6) Applied UTGST Amount (SC)
  UtgstApplF Num(19,6) Applied UTGST Amount (FC)
  CsgstAppl Num(19,6) Applied Cess GST Amount
  CsgstApplS Num(19,6) Applied Cess GST Amount (SC)
  CsgstApplF Num(19,6) Applied Cess GST Amount (FC)
  EncryptIV nVarChar(100) Encrypt IV
  TcsIntAcct nVarChar(15) TCS Interim Account ->OACT
  SurIntAcct nVarChar(15) Surcharge Interim Account ->OACT
  CesIntAcct nVarChar(15) Cess Interim Account ->OACT
  HscIntAcct nVarChar(15) HSC interim Account ->OACT
  LnIntAcct nVarChar(15) Interim Account for Tax ->OACT
  FixedAmnt Num(19,6) Fixed Amount
  FixedAmtSC Num(19,6) Fixed Amount (SC)
  FixedAmtFC Num(19,6) Fixed Amount (FC)
  BaseQty Num(19,6) Base Quantity

# PRQ6 - Purchase Request - Installments
Module: Marketing Documents | 65 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, InstlmntID
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OPRQ
  InstlmntID Int(6) Installment ID default=1
  ObjType nVarChar(20) Object Type default=1470000113 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DueDate Date(8) Due Date
  Status VarChar(1) Installment Status default=O [O=Open, C=Closed]
  DunnLevel Int(11) Dunning Level default=0
  InsTotal Num(19,6) Total Installment
  InsTotalFC Num(19,6) Total Installment (FC)
  InsTotalSy Num(19,6) Total Installment (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  VatSum Num(19,6) Total Tax
  VatSumFC Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  VatPaid Num(19,6) Tax Paid to Date
  VatPaidFC Num(19,6) Tax Paid (FC)
  VatPaidSys Num(19,6) Tax Paid (SC)
  TotalExpns Num(19,6) Total Freight Charges
  TotalExpFC Num(19,6) Total Freight Charges (FC)
  TotalExpSC Num(19,6) Total Freight Charges (SC)
  ExpAppl Num(19,6) Applied Freight Charges
  ExpApplFC Num(19,6) Applied Freight Charges (FC)
  ExpApplSC Num(19,6) Applied Freight Charges (SC)
  WTSum Num(19,6) WTax Amount
  WTSumFC Num(19,6) WTax Amount (FC)
  WTSumSC Num(19,6) WTax Amount (SC)
  WTApplied Num(19,6) Applied WTax
  WTAppliedF Num(19,6) Applied WTax (FC)
  WTAppliedS Num(19,6) Applied WTax (SC)
  TotalBlck Num(19,6) Total Reserved Amount
  TotalBlckF Num(19,6) Total Reserved Amount (FC)
  TotalBlckS Num(19,6) Total Reserved Amount (SC)
  VATBlck Num(19,6) Reserved Tax
  VATBlckFC Num(19,6) Reserved Tax (FC)
  VATBlckSC Num(19,6) Reserved Tax (SC)
  ExpnsBlck Num(19,6) Reserved Freight Charges
  ExpnsBlckF Num(19,6) Reserved Freight Charges (FC)
  ExpnsBlckS Num(19,6) Reserved Freight Charges (SC)
  WTBlocked Num(19,6) Reserved WTax Amount
  WTBlockedF Num(19,6) Reserved WTax Amount (FC)
  WTBlockedS Num(19,6) Reserved WTax Amount (SC)
  InstPrcnt Num(19,6) Installment %
  DunWizBlck VarChar(1) Wizard Dunning Block default=N [N=No, Y=Yes]
  DunDate Date(8) Last Dunning Date
  Paid Num(19,6) Paid
  PaidFrgn Num(19,6) Paid (FC)
  PaidSc Num(19,6) Paid (SC)
  reserved VarChar(1) Reserved default=N [N=No, Y=Yes]
  TaxOnExp Num(19,6) Tax on Expenses
  TaxOnExpFc Num(19,6) Tax on Expenses (FC)
  TaxOnExpSc Num(19,6) Tax on Expenses (SC)
  TaxOnExpAp Num(19,6) Applied Tax on Expenses
  TaxOnExApF Num(19,6) Applied Tax on Expenses (FC)
  TaxOnExApS Num(19,6) Applied Tax on Expenses (SC)
  TaxOnExBlo Num(19,6) Reserved Tax on Freight Amount
  TaxOnExBlF Num(19,6) Reserved Tax on Freight Amt FC
  TaxOnExBlS Num(19,6) Reserved Tax on Freight Amt SC
  LvlUpdDate Date(8) Dunning Level Update Date
  Ordered VarChar(1) Payment Ordered default=N [Y=Yes, N=No]
  PaidDpm Num(19,6) Paid by Down Payment
  PaidDpmFc Num(19,6) Paid by Down Payment (FC)
  PaidDpmSc Num(19,6) Paid by Down Payment (SC)
  EncryptIV nVarChar(100) Encrypt IV

# PRQ7 - Delivery Packages - Purchase Request
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OPRQ
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type default=1470000113 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV

# PRQ8 - Items in Package - Purchase Request
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum, ItemCode, UomEntry, NumPerMsr
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OPRQ
  PackageNum Int(11) Package Number
  ItemCode nVarChar(50) Item Code ->OITM
  Quantity Num(19,6) Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=1470000113 ->ADP1
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value default=0

# PRQ9 - Purchase Request - Drawn DPM
Module: Marketing Documents | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OPRQ
  LineNum Int(11) Row Number
  BaseAbs Int(11) Base Document Internal ID
  BaseLine Int(11) Base Document Row
  TargetBase VarChar(1) Target or Base Document default=B [B=Base, T=Target]
  ObjType nVarChar(20) Base Object Type
  DrawnSum Num(19,6) Net LC
  DrawnSumFc Num(19,6) Net FC
  DrawnSumSc Num(19,6) Net SC
  LogInstanc Int(11) Log Instance default=0
  ObjCode nVarChar(20) Object Type default=1470000113 ->ADP1
  ApplDrawn Num(19,6) Applied Net LC
  ApplDrawnF Num(19,6) Applied Net FC
  ApplDrawnS Num(19,6) Applied Net SC
  BaseDocNum Int(11) Base Document Number
  BsDocDate Date(8) Base Posting Date
  BsDueDate Date(8) Base Due Date
  BsCardName nVarChar(100) Base BP Name
  BsComments nVarChar(254) Base Remarks
  Posted VarChar(1) Base Document Posted default=Y [Y=Yes, N=No]
  Vat Num(19,6) Tax LC
  VatFc Num(19,6) Tax FC
  VatSc Num(19,6) Tax SC
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  IsGross VarChar(1) IS Gross Line default=N [N=Net Line, Y=Gross Line]

# PRR1 - A/P Return Request - Rows
Module: Marketing Documents | 317 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  STATUS: LineStatus
  CURRENCY: Currency
  ACCOUNT: AcctCode
  BASE_ENTRY: BaseEntry, BaseType, BaseLine
  VIS_ORDER: DocEntry, VisOrder
  OWNER_CODE: OwnerCode
  ITM_WHS_OQ: ItemCode, WhsCode, OpenQty
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPRR
  LineNum Int(11) Row Number
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=, 19=A/P Credit Memo, 21=Goods Return]
  TrgetEntry Int(11) Target Document Internal ID
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 18=A/P Invoice, 20=Purchase Delivery Notes]
  BaseEntry Int(11) Base Document Internal ID
  BaseLine Int(11) Base Row
  LineStatus VarChar(1) Row Status default=O [O=Open, C=Closed]
  ItemCode nVarChar(50) Item No. ->OITM
  Dscription nVarChar(200) Item/Service Description
  Quantity Num(19,6) Quantity
  ShipDate Date(8) Row Delivery Date
  OpenQty Num(19,6) Remaining Open Quantity
  Price Num(19,6) Price after Discount
  Currency nVarChar(3) Price Currency ->OCRN
  Rate Num(19,6) Currency Rate
  DiscPrcnt Num(19,6) Discount % per Row
  LineTotal Num(19,6) Row Total
  TotalFrgn Num(19,6) Row Total (FC)
  OpenSum Num(19,6) Open Amount
  OpenSumFC Num(19,6) Open Amount (FC)
  VendorNum nVarChar(50) Vendor Catalog No.
  SerialNum nVarChar(17) Serial Number
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  SlpCode Int(11) Sales Employee Code default=-1 ->OSLP
  Commission Num(19,6) Commission Percentage
  TreeType VarChar(1) BOM Type default=N [N=Not a BOM, A=Assembly, S=Sales, I=Sales BOM Component, P=Production, T=Template]
  AcctCode nVarChar(15) Account Code ->OACT
  TaxStatus VarChar(1) Tax Definition [Y=Yes, N=No]
  GrossBuyPr Num(19,6) Gross Profit Base Price
  PriceBefDi Num(19,6) Unit Price
  DocDate Date(8) Posting Date
  Flags Int(11) Flags default=0
  OpenCreQty Num(19,6) Credit Memo Amount
  UseBaseUn VarChar(1) Inventory UoM default=N [Y=Yes, N=No]
  SubCatNum nVarChar(50) BP Catalog No. ->OSCN
  BaseCard nVarChar(15) Base BP Code ->OCRD
  TotalSumSy Num(19,6) Row Total (SC)
  OpenSumSys Num(19,6) Open Amount (SC)
  InvntSttus VarChar(1) Warehouse Status default=O [O=Open, C=Closed]
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  CodeBars nVarChar(254) Bar Code
  VatPrcnt Num(19,6) Tax Rate per Row
  VatGroup nVarChar(8) Tax Definition ->OVTG
  PriceAfVAT Num(19,6) Gross Price after Discount
  Height1 Num(19,6) Height 1
  Hght1Unit Int(6) Unit of Height 1
  Height2 Num(19,6) Height 2
  Hght2Unit Int(6) Unit of Height 2
  Width1 Num(19,6) Width 1
  Wdth1Unit Int(6) Unit of Width 1
  Width2 Num(19,6) Width 2
  Wdth2Unit Int(6) Unit of Width 2
  Length1 Num(19,6) Length 1
  Len1Unit Int(6) Unit of Length 1
  length2 Num(19,6) Length 2
  Len2Unit Int(6) Unit of Length 2
  Volume Num(19,6) Volume
  VolUnit Int(6) Vol. Unit
  Weight1 Num(19,6) Weight 1
  Wght1Unit Int(6) Unit of Weight 1
  Weight2 Num(19,6) Weight 2
  Wght2Unit Int(6) Unit of Weight 2
  Factor1 Num(19,6) Factor 1
  Factor2 Num(19,6) Factor 2
  Factor3 Num(19,6) Factor 3
  Factor4 Num(19,6) Factor 4
  PackQty Num(19,6) Packing Quantity
  UpdInvntry VarChar(1) Whse Update default=Y [Y=Yes, N=No]
  BaseDocNum Int(11) Base Document No.
  BaseAtCard nVarChar(100) Customer/Vendor Base Document
  SWW nVarChar(16) Additional Identifier
  VatSum Num(19,6) Total Tax
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  FinncPriod Int(11) Posting Period ->OFPR
  ObjType nVarChar(20) Object Type default=234000032 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BlockNum nVarChar(100) Block Number
  ImportLog nVarChar(20) Import Log
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAqcuistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  DistribSum Num(19,6) Distributed Amount
  DstrbSumFC Num(19,6) Distributed Amount (FC)
  DstrbSumSC Num(19,6) Distributed Amount (SC)
  GrssProfit Num(19,6) Row Gross Profit
  GrssProfSC Num(19,6) Row Gross Profit (SC)
  GrssProfFC Num(19,6) Row Gross Profit (FC)
  VisOrder Int(11) Visual Order
  INMPrice Num(19,6) Item's Last Sales Price (OINM)
  PoTrgNum Int(11) PO Target No.
  PoTrgEntry nVarChar(11) PO Target Internal ID
  DropShip VarChar(1) Drop-Ship default=N [Y=Yes, N=No]
  PoLineNum Int(11) PO Target Row No.
  Address nVarChar(254) Address
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type [Y=Regular Tax, N=No Tax, U=Use Tax]
  OrigItem nVarChar(50) Original Item ->OITM
  BackOrdr VarChar(1) Allow Backorder [Y=Yes, N=No]
  FreeTxt nVarChar(100) Free Text
  PickStatus VarChar(1) Pick Status default=N [Y=Picked, N=Not Picked, R=Released for Picking, P=Partially Picked]
  PickOty Num(19,6) Pick Quantity
  PickIdNo Int(11) Pick ID
  TrnsCode Int(6) Shipping Method default=-1 ->OSHP
  VatAppld Num(19,6) Applied Tax
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  BaseQty Num(19,6) Base Quantity
  BaseOpnQty Num(19,6) Base Open Quantity
  VatDscntPr Num(19,6) Tax Discount %
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  DeferrTax VarChar(1) Deferred Tax default=N [Y=Yes, N=No]
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatlF Num(19,6) Net Tax Amount (FC)
  LineVatS Num(19,6) Net Tax Amount (SC)
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value
  CEECFlag VarChar(1) Correction Invoice Was/Should Be default=S [W=Was, S=Should Be]
  ToStock Num(19,6) Corr. Invoice Amt to Inventory
  ToDiff Num(19,6) Corr. Invoice Amount to Diff.
  ExciseAmt Num(19,6) Excise Amount
  TaxPerUnit Num(19,6) Tax per Unit
  TotInclTax Num(19,6) Total Including Tax
  CountryOrg nVarChar(3) Country/Region of Origin
  StckDstSum Num(19,6) Stock Distribution Sum
  ReleasQtty Num(19,6) Released Quantity
  LineType VarChar(1) Row Type default=R [R=Regular]
  TranType VarChar(1) Transaction Type [C=Complete, R=Reject]
  Text Text(16) Text
  OwnerCode Int(11) Document Owner
  StockPrice Num(19,6) Item Cost
  ConsumeFCT VarChar(1) Consumer Sales Forecast [Y=Yes, N=No]
  LstByDsSum Num(19,6) Last Buy Distribute Sum
  StckINMPr Num(19,6) Stock Inm Price
  LstBINMPr Num(19,6) Last Buy Inventory Journal Pr.
  StckDstFc Num(19,6) Stock Distribution Sum (FC)
  StckDstSc Num(19,6) Stock Distribution Sum (SC)
  LstByDsFc Num(19,6) Last Buy Distribute Sum (FC)
  LstByDsSc Num(19,6) Last Buy Distribute Sum (SC)
  StockSum Num(19,6) Stock Sum
  StockSumFc Num(19,6) Stock Sum FC
  StockSumSc Num(19,6) Stock Sum SC
  StckSumApp Num(19,6) Stock Sum Applied
  StckAppFc Num(19,6) Stock Sum Applied FC
  StckAppSc Num(19,6) Stock Sum Applied SC
  ShipToCode nVarChar(50) Ship-to Code
  ShipToDesc nVarChar(254) Ship-to Description
  StckAppD Num(19,6) Stock Distrib. - Applied Sum
  StckAppDFC Num(19,6) Stock Dist. - Applied Sum (FC)
  StckAppDSC Num(19,6) Stock Dist. - Applied Sum (SC)
  BasePrice VarChar(1) Price for Total Calculation default=E [E=Exclude Tax, I=Include Tax]
  GTotal Num(19,6) Gross Total
  GTotalFC Num(19,6) Gross Total (FC)
  GTotalSC Num(19,6) Gross Total (SC)
  DistribExp VarChar(1) Distribute Freight Charges [Y=Yes, N=No]
  DescOW VarChar(1) Description overwritten default=N [Y=Yes, N=No]
  DetailsOW VarChar(1) Remarks overwritten default=N [Y=Yes, N=No]
  GrossBase Int(6) Base Method for Gross Profit
  VatWoDpm Num(19,6) Tax Before DPM Applied
  VatWoDpmFc Num(19,6) Tax Before DPM Applied (FC)
  VatWoDpmSc Num(19,6) Tax Before DPM Applied (SC)
  CFOPCode nVarChar(6) CFOP Code for Document ->OCFP
  CSTCode nVarChar(6) CST Code for ICMS
  Usage Int(11) Usage Code for Document ->OUSG
  TaxOnly VarChar(1) Tax Only [Y=Yes, N=No]
  WtCalced VarChar(1) Withholding Tax Calculated default=N [N=No, Y=Yes]
  QtyToShip Num(19,6) Quantity to Ship
  DelivrdQty Num(19,6) Delivered Quantity
  OrderedQty Num(19,6) Ordered Quantity
  CogsOcrCod nVarChar(8) COGS Distribution Rule Code ->OOCR
  CiOppLineN Int(11) Row Number of Associated Row default=-1
  CogsAcct nVarChar(15) COGS Account Code ->OACT
  ChgAsmBoMW VarChar(1) Change Whs for Asm BoM Child [Y=Yes, N=No]
  ActDelDate Date(8) Actual Delivery Date
  OcrCode2 nVarChar(8) Costing Code 2 ->OOCR
  OcrCode3 nVarChar(8) Costing Code 3 ->OOCR
  OcrCode4 nVarChar(8) Costing Code 4 ->OOCR
  OcrCode5 nVarChar(8) Costing Code 5 ->OOCR
  TaxDistSum Num(19,6) Tax Distributed Amount
  TaxDistSFC Num(19,6) Tax Distributed Amount (FC)
  TaxDistSSC Num(19,6) Tax Distributed Amount (SC)
  PostTax VarChar(1) Post Tax in Price to Stock default=Y [Y=Yes, N=No]
  Excisable VarChar(1) Excisable [Yes/No] [Y=Yes, N=No]
  AssblValue Num(19,6) Assessable Value
  RG23APart1 Int(11) RG23A Part1 Number
  RG23APart2 Int(11) RG23A Part2 Number
  RG23CPart1 Int(11) RG23C Part1 Number
  RG23CPart2 Int(11) RG23C Part2 Number
  CogsOcrCo2 nVarChar(8) COGS Distribution Rule Code2 ->OOCR
  CogsOcrCo3 nVarChar(8) COGS Distribution Rule Code3 ->OOCR
  CogsOcrCo4 nVarChar(8) COGS Distribution Rule Code4 ->OOCR
  CogsOcrCo5 nVarChar(8) COGS Distribution Rule Code5 ->OOCR
  LnExcised VarChar(1) Line Excised [O=Open, C=Closed, P=Copied to OEI]
  LocCode Int(11) Location Code ->OLCT
  StockValue Num(19,6) Total COGS Value
  GPTtlBasPr Num(19,6) Total Base Price for Profit
  unitMsr2 nVarChar(100) Pur/Sal UoM if BaseUnit
  NumPerMsr2 Num(19,6) Pur/Sal UoM Value if Base Unit
  SpecPrice VarChar(1) Price Source Type default=N [Y=Special Prices for Business Partner, N=Manual, W=Active Price List, Discount Groups, R=Active Price List, U=Inactive Price List, A=Blanket Agreement, P=Period and Volume Discounts, Q=Period and Volume Discounts, Discount Groups, V=Inactive Price List, Discount Groups, 9=Special Prices for Business Partner, !=Blanket Agreement, 0=Period and Volume Discounts, 1=Period and Volume Discounts, Discount Groups, 2=Active Price List, 7=Active Price List, Discount Groups, 5=Inactive Price List, 6=Inactive Price List, Discount Groups]
  CSTfIPI nVarChar(2) CST for IPI Code
  CSTfPIS nVarChar(2) CST for PIS Code
  CSTfCOFINS nVarChar(2) CST for COFINS Code
  ExLineNo nVarChar(10) ExLineNo
  isSrvCall VarChar(1) Created from Service Call default=N [Y=Yes, N=No]
  PQTReqQty Num(19,6) Pur Quotation: Required Qty
  PQTReqDate Date(8) Pur Quotation: Required Date
  PcDocType Int(11) Purchase Confirmation Doc Type default=-1 [-1=No Type, 22=Purchase Order, 540000006=Purchase Quotation]
  PcQuantity Num(19,6) Purchase Confirmation Quantity
  LinManClsd VarChar(1) Line Was Closed Manually default=N [Y=Yes, N=No, U=Unknown]
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  NoInvtryMv VarChar(1) Without Inventory Movement default=N [Y=Yes, N=No]
  ActBaseEnt Int(11) Actual Base Document Entry
  ActBaseLn Int(11) Actual Base Line Number
  ActBaseNum Int(11) Actual Base Document No.
  OpenRtnQty Num(19,6) Quantity Open for Return
  AgrNo Int(11) Agreement No. ->OOAT
  AgrLnNum Int(11) Agreement Row Number
  CredOrigin VarChar(1) Credit Origin ->OBSI
  Surpluses Num(19,6) Surpluses
  DefBreak Num(19,6) Defect and Breakup
  Shortages Num(19,6) Shortages
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  UomEntry2 Int(11) UoM Entry if Base Unit default=0 ->OUOM
  UomCode nVarChar(20) UoM Code
  UomCode2 nVarChar(20) UoM Code if Base Unit
  FromWhsCod nVarChar(8) From Warehouse Code ->OWHS
  NeedQty VarChar(1) Consider Quantity of Items default=N [Y=Yes, N=No]
  PartRetire VarChar(1) Partial Retirement default=N [Y=Yes, N=No]
  RetireQty Num(19,6) Retirement Quantity
  RetireAPC Num(19,6) Retirement APC
  RetirAPCFC Num(19,6) Retirement APC FC
  RetirAPCSC Num(19,6) Retirement APC SC
  InvQty Num(19,6) Quantity - Inventory UoM
  OpenInvQty Num(19,6) Open Quantity (Inventory UoM)
  EnSetCost VarChar(1) Enable Set Item Cost in Return default=N [Y=Yes, N=No]
  RetCost Num(19,6) Return Cost in A/R Return
  Incoterms Int(11) Incoterms default=0 ->ODCI
  TransMod Int(11) Transport Mode default=0 ->ODCI
  LineVendor nVarChar(15) Line Vendor Code ->OCRD
  DistribIS VarChar(1) Distribute Intrastat Freight default=N [Y=Yes, N=No]
  ISDistrb Num(19,6) Intrastat Distrib. Amount
  ISDistrbFC Num(19,6) Intrastat Distrib. Amount (FC)
  ISDistrbSC Num(19,6) Intrastat Distrib. Amount (SC)
  IsByPrdct VarChar(1) Item Is By-Product default=N [N=No, Y=Yes]
  ItemType Int(11) Item Type default=4 [4=Item]
  PriceEdit VarChar(1) Price Was Edited by User default=N [N=No, Y=Yes]
  PrntLnNum Int(11) Parent Line Number
  LinePoPrss VarChar(1) Line PO Process default=N [Y=Yes, N=No]
  FreeChrgBP VarChar(1) Free of Charge (BP) default=N [Y=Yes, N=No]
  TaxRelev VarChar(1) Tax Relevant Row default=Y [Y=Yes, N=No]
  LegalText nVarChar(254) Legal Text
  ThirdParty VarChar(1) Third Party default=N [Y=Yes, N=No]
  LicTradNum nVarChar(32) Federal Tax ID
  InvQtyOnly VarChar(1) Change Qty (Inv. UoM) Only default=N [Y=Yes, N=No]
  UnencReasn Int(11) Reason for Unencumbered ICMS
  ShipFromCo nVarChar(50) Ship-From Code
  ShipFromDe nVarChar(254) Ship-From Description
  FisrtBin nVarChar(228) First Bin Location
  AllocBinC nVarChar(11) Allocated Bin Location Count
  ExpType nVarChar(4) Expense Type ->OEXD
  ExpUUID nVarChar(50) Expense UUID
  ExpOpType VarChar(1) Expense Operation Type [P=Professional Services, R=Renting Assets, O=Others]
  DIOTNat nVarChar(3) DIOT Nationality
  MYFtype nVarChar(2) MYF type [S1=MYF Wholesale Sales, S2=Retail Sales, P1=MYF Wholesale Purchases, P3=Other Expense Transactions]
  GPBefDisc Num(19,6) Gross Price
  ReturnRsn Int(6) Return Reason default=-1
  ReturnAct Int(6) Return Action default=-1
  StgSeqNum Int(11) Stage Sequence Number
  StgEntry Int(11) Stage Entry ->ORST
  StgDesc nVarChar(100) Stage Description
  ItmTaxType nVarChar(2) Item GST Tax Category [GR=GST Regular, GN=GST Nil Rated, GE=GST Exempt, NE=Excisable, NN=Non-GST Non-Excisable]
  SacEntry Int(11) SAC Entry ->OSAC
  NCMCode Int(11) NCM Code default=-1
  HsnEntry Int(11) HSN Entry
  OriBAbsEnt Int(11) Original Base Document Internal ID
  OriBLinNum Int(11) Original Base Document Line Number
  OriBDocTyp Int(11) Original Base Document Type
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No, U=Use]
  EncryptIV nVarChar(100) Encrypt IV
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  StdItemId Int(11) Standard Item Identification ->OUNCL
  CommClass Int(11) Commodity Classification ->OUNCL
  VatExEntry Int(11) VAT Exemption AbsEntry ->OVEB
  VatExLN Int(6) VAT Exemption LineNum
  NatOfTrans Int(11) Nature of Transaction ->ODCI
  ISDtCryImp nVarChar(3) Destination Country/Region for Import ->OCRY
  ISDtRgnImp Int(11) Destination Region for Import ->ODCI
  ISOrCryExp nVarChar(3) Country/Region of Origin for Export ->OCRY
  ISOrRgnExp Int(11) Region of Origin for Export ->ODCI
  NVECode nVarChar(6) NVE Code
  PoNum nVarChar(20) Customer's Purchase Order Number
  PoItmNum Int(11) Customer's Purchase Order Item Number
  IndEscala VarChar(1) Indicator for Relevant Scale default=N [Y=Yes, N=No]
  CESTCode Int(11) CEST Code ->OCEST
  CtrSealQty Num(19,6) Control Seal Quantity
  CNJPMan nVarChar(14) CNPJ of Manufacturer
  UFFiscBene nVarChar(10) UF Fiscal Benefit Code
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]
  LegalTIMD nVarChar(250) Legal Text from Item Master Data
  LegalTTCA nVarChar(250) Legal Text from Tax Code Attributes
  LegalTW nVarChar(250) Legal Text from Warehouse
  LegalTCD nVarChar(250) Legal Text from Tax Code Determination
  RevCharge VarChar(1) Reverse Charge default=N [Y=Yes, N=No]
  ListNum Int(6) Price List No. ->OPLN

# PRR10 - A/P Return Request - Row Structure
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SECONDERY U: DocEntry, AftLineNum, OrderNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPRR
  LineSeq Int(11) Row Sequence
  AftLineNum Int(11) After Row Number
  OrderNum Int(11) Order Number
  LineType VarChar(1) Row Type [T=Text, S=Subtotal]
  LineText Text(16) Row Text
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=234000032 ->ADP1

# PRR11 - A/P Return Request - Drawn Dpm Detail
Module: Marketing Documents | 70 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LineSeq
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPRR
  LineNum Int(11) Row Number
  LineSeq Int(11) Sequence Number
  BaseAbs Int(11) Base Document Internal ID default=-1 ->ODPI
  BaseType Int(11) Base Object Type default=203 [203=A/R Down Payment]
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  VatPrcnt Num(19,6) VAT Percent
  LineTotal Num(19,6) Net LC
  TotalFrgn Num(19,6) Net FC
  TotalSumSy Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFrgn Num(19,6) Tax FC
  VatSumSys Num(19,6) Tax SC
  ObjType nVarChar(20) Object Type default=234000032 ->ADP1
  LogInstanc Int(11) Log Instance
  IsAcq VarChar(1) Acquisition Tax Liable default=N [N=No, Y=Yes]
  IsAllDrawn VarChar(1) Remaining Amount Drawn default=N [Y=Yes, N=No]
  IsGross VarChar(1) Is Gross Line default=N [N=Net Line, Y=Gross Line]
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  ApplNet Num(19,6) Applied Net LC
  ApplNetFc Num(19,6) Applied Net FC
  ApplNetSc Num(19,6) Applied Net SC
  ApplVat Num(19,6) Applied Tax LC
  ApplVatFc Num(19,6) Applied Tax FC
  ApplVatSc Num(19,6) Applied Tax SC
  BaseNet Num(19,6) Base Net LC
  BaseNetFc Num(19,6) Base Net FC
  BaseNetSc Num(19,6) Base Net SC
  BaseVat Num(19,6) Base Tax LC
  BaseVatFc Num(19,6) Base Tax FC
  BaseVatSc Num(19,6) Base Tax SC
  BaseGross Num(19,6) Base Gross LC
  BaseGrossF Num(19,6) Base Gross FC
  BaseGrossS Num(19,6) Base Gross SC
  LineType VarChar(1) Line Type default=D [D=Document Row, R=Currency Rounding, H=Down Payment Document Rounding]
  DctSum Num(19,6) Deductible Sum LC
  DctSumFc Num(19,6) Deductible Sum FC
  DctSumSc Num(19,6) Deductible Sum SC
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplDct Num(19,6) Applied Deductible Sum LC
  ApplDctFc Num(19,6) Applied Deductible Sum FC
  ApplDctSc Num(19,6) Applied Deductible Sum SC
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  BaseDct Num(19,6) Base Deductible Sum LC
  BaseDctFc Num(19,6) Base Deductible Sum FC
  BaseDctSc Num(19,6) Base Deductible Sum SC
  BaseEq Num(19,6) Base Equalization Sum LC
  BaseEqFc Num(19,6) Base Equalization Sum FC
  BaseEqSc Num(19,6) Base Equalization Sum SC
  TaxCode nVarChar(8) Tax Code ->OSTC
  ApplGross Num(19,6) Applied Gross LC
  ApplGrossF Num(19,6) Applied Gross FC
  ApplGrossS Num(19,6) Applied Gross SC
  TaxAdjust VarChar(1) Manual Tax Adjustment default=N [Y=Yes, N=No]
  RvsChrgSum Num(19,6) Reverse Charge Sum LC
  RvsChrgFc Num(19,6) Reverse Charge Sum FC
  RvsChrgSc Num(19,6) Reverse Charge Sum SC
  BasRvsChrg Num(19,6) Base Reverse Charge LC
  BasRvsFc Num(19,6) Base Reverse Charge FC
  BasRvsSc Num(19,6) Base Reverse Charge SC
  ApplRvs Num(19,6) Applied Reverse Charge LC
  ApplRvsFc Num(19,6) Applied Reverse Charge FC
  ApplRvsSc Num(19,6) Applied Reverse Charge SC
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# PRR12 - A/P Return Request - Tax Extension
Module: Marketing Documents | 117 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPRR
  TaxId0 nVarChar(100) Tax ID 0
  TaxId1 nVarChar(100) Tax ID 1
  TaxId2 nVarChar(100) Tax ID 2
  TaxId3 nVarChar(100) Tax ID 3
  TaxId4 nVarChar(100) Tax ID 4
  TaxId5 nVarChar(100) Tax ID 5
  TaxId6 nVarChar(100) Tax ID 6
  TaxId7 nVarChar(100) Tax ID 7
  TaxId8 nVarChar(100) Tax ID 8
  TaxId9 nVarChar(100) Tax ID 9
  State nVarChar(3) State Code
  County nVarChar(7) County Code
  Incoterms nVarChar(3) Incoterms
  Vehicle nVarChar(10) Vehicle ID
  VidState nVarChar(3) Vehicle ID (State)
  NfRef nVarChar(254) NF Reference
  Carrier nVarChar(15) Carrier Code ->OCRD
  QoP Int(11) Quantity of Packs
  PackDesc nVarChar(10) Pack Description
  Brand nVarChar(20) Brand
  NoSU Int(11) Number of Shipping Unit
  NetWeight Num(19,6) Net Weight
  GrsWeight Num(19,6) Gross Weight
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=234000032 ->ADP1
  TaxId10 nVarChar(100) Tax ID 10
  TransCat nVarChar(100) Transaction Category
  FormNo nVarChar(100) Form No.
  TaxId11 nVarChar(100) Tax ID 11
  StreetS nVarChar(100) Street
  BlockS nVarChar(100) Block
  BuildingS Text(16) Building/Floor/Room
  CityS nVarChar(100) City
  ZipCodeS nVarChar(20) Zip Code
  CountyS nVarChar(100) County
  StateS nVarChar(3) State ->OCST
  CountryS nVarChar(3) Country/Region ->OCRY
  AddrTypeS nVarChar(100) Address Type
  StreetNoS nVarChar(100) Street No.
  StreetB nVarChar(100) Street
  BlockB nVarChar(100) Block
  BuildingB Text(16) Building/Floor/Room
  CityB nVarChar(100) City
  ZipCodeB nVarChar(20) Zip Code
  CountyB nVarChar(100) County
  StateB nVarChar(3) State ->OCST
  CountryB nVarChar(3) Country/Region ->OCRY
  AddrTypeB nVarChar(100) Address Type
  StreetNoB nVarChar(100) Street No.
  ImpORExp VarChar(1) Import or Export [N=, Y=]
  Vat VarChar(1) VAT default=N [N=No VAT Support, Y=VAT Support]
  AltCrdNamB nVarChar(100) Alternative BP Name
  AltTaxIdB nVarChar(32) Alternative Tax ID
  Address2S nVarChar(50) Address Name 2
  Address3S nVarChar(50) Address Name 3
  Address2B nVarChar(50) Address Name 2
  Address3B nVarChar(50) Address Name 3
  MainUsage Int(11) Main Usage Code of Document ->OUSG
  GlbLocNumS nVarChar(50) Global Location Number
  GlbLocNumB nVarChar(50) Global Location Number
  CollectDT nVarChar(20) Date and Time of Collection
  TransprtDT Date(8) Transport Starting Date
  TransprtRS nVarChar(100) Transport Reason
  TaxId12 nVarChar(50) Tax ID 12
  TaxId13 nVarChar(100) Deductee Ref. No. in India
  ImpExpNo nVarChar(100) Import/Export Bill No.
  ImpExpDate Date(8) Import/Export Date
  BpGSTType Int(11) GST Regn Type of BP
  BpGSTN nVarChar(15) GST Regn No of BP
  BpStateCod nVarChar(3) State Code of Business Partner ->OCST
  BPStatGSTN nVarChar(2) GST State Code of BP
  LocGSTType Int(11) GST Regn Type of Location
  LocGSTN nVarChar(15) GST Regn No of Location
  LocStatCod nVarChar(3) State Code of Location ->OCST
  LocStaGSTN nVarChar(2) GST State Code of Location
  BpCountry nVarChar(3) Country/Region Code of BP ->OCRY
  OrigImpNo nVarChar(100) Original Bill of Entry No.
  OrigImpDat Date(8) Original Bill of Entry Date
  ExportType VarChar(1) Exporting Type default=E [E=Imports/Exports, S=SEZ Developer, U=SEZ Unit, D=Deemed Imports/Exports]
  PortCode nVarChar(100) Port Code
  BoEValue Num(19,6) Bill of Entry Value
  IsIGSTAct VarChar(1) Supply under IGST Account [Y=Yes, N=No]
  ClaimRefun VarChar(1) Claim Refund [Y=Yes, N=No]
  TaxRateDif Int(11) Differential % of Tax Rate [65=, 100=]
  BPGdsIssP nVarChar(15) Goods Issue Place BP
  CNPJGIP nVarChar(100) Goods Issue Place CNPJ
  CPFGIP nVarChar(100) Goods Issue Place CPF
  StreetGIP nVarChar(100) Goods Issue Place Street
  StrtNoGIP nVarChar(100) Goods Issue Place Street No.
  BldngGIP Text(16) Goods Issue Place Building
  ZipGIP nVarChar(20) Goods Issue Place Zip Code
  BlockGIP nVarChar(100) Goods Issue Place Block
  CityGIP nVarChar(100) Goods Issue Place City
  CountyGIP nVarChar(100) Goods Issue Place County
  StateGIP nVarChar(3) Goods Issue Place State ->OCST
  CountryGIP nVarChar(3) Goods Issue Place Country/Region ->OCRY
  PhoneGIP nVarChar(20) Goods Issue Place Phone
  EMailGIP nVarChar(100) Goods Issue Place E-Mail
  DptDateGIP Date(8) Goods Issue Place Departure Date
  BPDelivryP nVarChar(15) Delivery Place BP
  CNPJDlvryP nVarChar(100) Delivery Place CNPJ
  CPFDlvryP nVarChar(100) Delivery Place CPF
  StrtDlvryP nVarChar(100) Delivery Place Street
  StrNoDlvrP nVarChar(100) Delivery Place Street No.
  BldDlvryP Text(16) Delivery Place Building
  ZipDlvryP nVarChar(20) Delivery Place Zip Code
  BlckDlvryP nVarChar(100) Delivery Place Block
  CityDlvryP nVarChar(100) Delivery Place City
  CntyDlvryP nVarChar(100) Delivery Place County
  StatDlvryP nVarChar(3) Delivery Place State ->OCST
  CtryDlvryP nVarChar(3) Delivery Place Country/Region ->OCRY
  FoneDlvryP nVarChar(20) Delivery Place Phone
  MailDlvryP nVarChar(100) Delivery Place E-Mail
  DpDtDlvryP Date(8) Delivery Place Departure Date
  AuthedCNPJ nVarChar(250) Authorized CNPJ or CPF
  TaxId14 nVarChar(250) ITR Filing

# PRR13 - A/P Return Request - Distributed Freights
Module: Marketing Documents | 59 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPRR
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=234000032 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Aquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Normal Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) VAT Applied Frgn
  VatAppldSC Num(19,6) VAT Applied Sys
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock default=N [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Line No.
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Abs. Entry default=-1
  BaseGroup Int(11) Base Document Group default=-1
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1
  VisOrder Int(11) Visual Order
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DistribExp VarChar(1) Distribute Freights [Y=Yes, N=No]
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ

# PRR14 - A/P Return Request - Assembly - Rows
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPRR
  LineNum Int(11) Row Number default=-1
  ChildNum Int(11) Child Number default=-1
  ItemCode nVarChar(50) Item no. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  TotalQty Num(19,6) Total Quantity
  OpenQty Num(19,6) Remaining Open Quantity
  ObjectType nVarChar(20) object type default=234000032 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BaseChildN Int(11) Base Child Number default=-1
  EncryptIV nVarChar(100) Encrypt IV

# PRR15 - A/P Return Request - Drawn Dpm Applied
Module: Marketing Documents | 84 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPRR
  LineNum Int(11) Row Number
  ObjType nVarChar(20) object type default=234000032 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  StaCode nVarChar(8) Tax Authority Code
  StaType Int(11) Tax Authority Type
  StaIndex Int(11) Tax Authority Seq Index
  BaseNet Num(19,6) Net LC
  BaseNetFc Num(19,6) Net FC
  BaseNetSc Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFc Num(19,6) Tax FC
  VatSumSc Num(19,6) Tax SC
  DctSum Num(19,6) Deductible Sum LC
  DctSumFc Num(19,6) Deductible Sum FC
  DctSumSc Num(19,6) Deductible Sum SC
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplNet Num(19,6) Applied Net LC
  ApplNetFc Num(19,6) Applied Net FC
  ApplNetSc Num(19,6) Applied Net SC
  ApplVat Num(19,6) Applied Tax LC
  ApplVatFc Num(19,6) Applied Tax FC
  ApplVatSc Num(19,6) Applied Tax SC
  ApplDct Num(19,6) Applied Deductible Sum LC
  ApplDctFc Num(19,6) Applied Deductible Sum FC
  ApplDctSc Num(19,6) Applied Deductible Sum SC
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  PaidNet Num(19,6) Paid Net LC
  PaidNetFc Num(19,6) Paid Net FC
  PaidNetSc Num(19,6) Paid Net SC
  PaidVat Num(19,6) Paid Tax LC
  PaidVatFc Num(19,6) Paid Tax FC
  PaidVatSc Num(19,6) Paid Tax SC
  PaidDct Num(19,6) Paid Deductible Sum LC
  PaidDctFc Num(19,6) Paid Deductible Sum FC
  PaidDctSc Num(19,6) Paid Deductible Sum SC
  PaidEq Num(19,6) Paid Equalization Sum LC
  PaidEqFc Num(19,6) Paid Equalization Sum FC
  PaidEqSc Num(19,6) Paid Equalization Sum SC
  DpApplNet Num(19,6) Dpm Appl Net LC
  DpApplNetF Num(19,6) Dpm Appl Net FC
  DpApplNetS Num(19,6) Dpm Appl Net SC
  DpApplVat Num(19,6) Dpm Appl Tax LC
  DpApplVatF Num(19,6) Dpm Appl Tax FC
  DpApplVatS Num(19,6) Dpm Appl Tax SC
  DpApplDct Num(19,6) Dpm Appl Deductible Sum LC
  DpApplDctF Num(19,6) Dpm Appl Deductible Sum FC
  DpApplDctS Num(19,6) Dpm Appl Deductible Sum SC
  DpApplEq Num(19,6) Dpm Appl Equalization Sum LC
  DpApplEqFc Num(19,6) Dpm Appl Equalization Sum FC
  DpApplEqSc Num(19,6) Dpm Appl Equalization Sum SC
  TaxCode nVarChar(8) Tax Code ->OSTC
  LineType VarChar(1) Row Type default=D [D=Document, R=Exchange Rate Rounding, H=Document Header Rounding]
  BaseGrs Num(19,6) Gross LC
  BaseGrsFc Num(19,6) Gross FC
  BaseGrsSc Num(19,6) Gross SC
  ApplGrs Num(19,6) Applied Gross LC
  ApplGrsFc Num(19,6) Applied Gross FC
  ApplGrsSc Num(19,6) Applied Gross SC
  PaidGrs Num(19,6) Paid Gross LC
  PaidGrsFc Num(19,6) Paid Gross FC
  PaidGrsSc Num(19,6) Paid Gross SC
  DpApplGrs Num(19,6) Dpm Appl Gross LC
  DpApplGrsF Num(19,6) Dpm Appl Gross FC
  DpApplGrsS Num(19,6) Dpm Appl Gross SC
  RvsChrgSum Num(19,6) Reverse Charge Sum
  RvsChrgSc Num(19,6) Reverse Charge Sum (SC)
  RvsChrgFc Num(19,6) Reverse Charge Sum (FC)
  ApplRvs Num(19,6) Applied Reverse Charge Sum LC
  ApplRvsSc Num(19,6) Applied Reverse Charge Sum SC
  ApplRvsFc Num(19,6) Applied Reverse Charge Sum FC
  PaidRvs Num(19,6) Paid Reverse Charge Sum LC
  PaidRvsSc Num(19,6) Paid Reverse Charge Sum SC
  PaidRvsFc Num(19,6) Paid Reverse Charge Sum FC
  DpApplRvs Num(19,6) Dpm Applied Reverse Charge LC
  DpApplRvsS Num(19,6) Dpm Applied Reverse Charge SC
  DpApplRvsF Num(19,6) Dpm Applied Reverse Charge FC
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# PRR16 - A/P Return Request - SnB properties
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, SnBIndex
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) abs entry ->OPRR
  LineNum Int(11) Line Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object id
  ObjAbs Int(11) Object Abs
  DrfWObjAbs Int(11) draft Wobj Abs default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type default=234000032
  LogInstanc Int(11) Log Instance

# PRR17 - A/P Return Request - Import Process
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPRR
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=234000032 ->ADP1
  ImpDocType VarChar(1) Type of Importation Document ->OBSI
  ImpDocNum nVarChar(10) Importation Document Number
  DateOfReg Date(8) Date of Registry DI/DSI/DA
  CustClrDat Date(8) Date of Customs Clearance
  ConcActNum nVarChar(30) Drawback Concession Acct No.
  AdditNum nVarChar(30) Additional Number
  AddItmDV Num(19,6) Additional Item Discount Value
  tpVTransp Int(6) Overland Transport Route [1=Maritime, 2=Waterway, 3=Lakeside, 4=Air, 5=Post, 6=Train, 7=Road, 8=Network Transmission, 9=Own Means, 10=Input/Output Fictitious, 11=Courier, 12=Hand Carry]
  DrawSReg nVarChar(11) Drawback - Suspension Regime
  AddFrNavyA Num(19,6) Additional Freight to Navy Authority
  TypeOfImp VarChar(1) Type of Import
  nSeqAdic Int(6) Additional Item Sequential Number

# PRR18 - A/P Return Request - Export Process
Module: Marketing Documents | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPRR
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=234000032 ->ADP1
  ExpDocType Int(11) Type of Exportation Document default=-1 ->OBNI
  ExpDeclNum Int(11) Exportation Declaration Number
  ExpDeclDat Date(8) Exportation Declaration Date
  ExpNature Int(11) Nature of Exportation default=-1 ->OBNI
  ExpRegNum Int(11) Number of Exportation Registry
  ExpRegDate Date(8) Date of Exportation Registry
  LadBillNum nVarChar(19) Bill of Lading Number
  LadBillDat Date(8) Date of Bill of Lading
  MerchLeftD Date(8) Date Merchandise Left Customs
  LadBillTyp Int(11) Type of Bill of Lading default=-1 ->OBNI
  DrawSReg nVarChar(11) Drawback - Suspension Regime
  NatureExp nVarChar(44) Nature of Export
  QultExpItm Num(19,6) Quantity of Exported Items
  nSeqAdic Int(6) Additional Item Sequential Number

# PRR19 - A/P Return Request - Bin Allocation Data
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, BinAllocSe
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OPRR
  BinAllocSe Int(11) Bin Allocation Sequence
  LineNum Int(11) Line Number
  SubLineNum Int(11) Subline Number default=-1
  SnBType Int(11) SnB Type default=-1
  SnBMDAbs Int(11) SnB Master Data Internal No. default=-1
  BinAbs Int(11) Bin Internal Number ->OBIN
  Quantity Num(19,6) Quantity
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjType nVarChar(20) Object Type default=234000032 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  BinActTyp Int(6) Bin Action Type [1=Transaction In, 2=Transaction Out, 4=SnB Complete, 8=Bin First Then SnB]

# PRR2 - A/P Return Request - Freight - Rows
Module: Marketing Documents | 64 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPRR
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=234000032 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) Vat Applied
  VatAppldFC Num(19,6) Vat Applied Frgn
  VatAppldSC Num(19,6) Vat Applied Sys
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report [Y=Yes, N=No]
  BaseGroup Int(11) Base Document Group default=-1 [-1=, 0=, 1=, 2=]
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1 [-1=, 0=, 1=, 2=]
  VisOrder Int(11) Visual Order
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]

# PRR20 - Intrastat Expenses
Module: Marketing Documents | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPRR
  ExpnsCode Int(11) Freight Code ->OEXD
  TotalLC Num(19,6) Total
  TotalFC Num(19,6) Total (FC)
  TotalSC Num(19,6) Total (SC)
  DistribM VarChar(1) Distribution Method default=T [Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DrawnLC Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  LineNum Int(11) Line Number default=-1
  BaseAbsEnt Int(11) Base Abs. Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 16=Return, 13=A/R Invoice, 203=Down Payment Incoming, 204=Down Payment Outgoing, 22=Purchase Order, 20=Goods Receipt PO, 21=Goods Return, 18=A/P Invoice, 540000006=Purchase Quotation, 0=, -1=]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No. default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=234000032 ->ADP1
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  AppliedLC Num(19,6) Applied
  AppliedFC Num(19,6) Applied (FC)
  AppliedSC Num(19,6) Applied (SC)

# PRR21 - A/P Return Request - Document Reference Information
Module: Marketing Documents | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, RefType
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjectType nVarChar(20) Object Type default=234000032
  LogInstanc Int(11) Log Instance default=0
  RefType VarChar(1) Reference Types default=S [S=System Document, E=External Document]
  LineNum Int(11) Line Number
  RefDocEntr Int(11) Referenced Internal Number
  RefDocNum Int(11) Referenced Document Number
  ExtDocNum nVarChar(100) External Referenced Document Number
  RefObjType nVarChar(20) Referenced Object Type [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 234000031=Return Request, 16=Return, 203=A/R Down Payment, 13=A/R Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 280=A/R Tax Invoice, 1470000113=Purchase Request, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Return Request, 21=Goods Return, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 281=A/P Tax Invoice, 69=Landed Costs, 24=Incoming Payments, 46=Outgoing Payments, 57=Checks for Payment, 321=Internal Reconciliation, 34=Recurring Posting, 30=Journal Entry, 59=Goods Receipt, 60=Goods Issue, 162=Inventory Revaluation, 1470000065=Inventory Counting, 10000071=Inventory Posting, 1250000001=Inventory Transfer Request, 67=Inventory Transfer, 202=Production Order, 13001=Original Invoice, -1=External Document, 20301=Original Down Payment Invoice]
  AccessKey nVarChar(100) Access Key
  IssueDate Date(8) Date of Issue
  IssuerCNPJ nVarChar(100) Issuer CNPJ
  IssuerCode nVarChar(10) Fiscal Document Issuer UF Code
  Model nVarChar(6) Fiscal Document Model
  Series nVarChar(3) Fiscal Document Series
  Number Int(11) Fiscal Document Number
  RefAccKey nVarChar(100) Referenced CT-e Access Key
  RefAmount Num(19,6) Referenced Amount
  SubSeries nVarChar(3) Fiscal Document Subseries
  Remark nVarChar(254) Remarks
  LinkRefTyp nVarChar(20) Link Reference Type default=00 [00=, 01=Nota de cr�dito de los documentos relacionados, 02=Nota de d�bito de los documentos relacionados, 03=Devoluci�n de mercanc�a sobre facturas o traslados previos, 04=Sustituci�n de los CFDI previos, 05=Traslados de mercancias facturados previamente, 06=Factura generada por los traslados previos, 07=CFDI por aplicaci�n de anticipo, 08=Customs, MX_08=Factura generada por pagos en parcialidades, 09=Factura generada por pagos diferidos]

# PRR22 - A/P Return Request - Resource Costs
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, StdCostNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->PRR1
  LineNum Int(11) Row Number
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=234000032
  LogInstanc Int(11) Log Instance default=0

# PRR23 - A/P Return Request - Selected Asset Master Data
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, VisOrder
  ASSETS: DocEntry, LineNum, AssetCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPRR
  LineNum Int(11) Row Number
  AssetCode nVarChar(50) Selected Asset Code ->OITM
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Remarks nVarChar(100) Remarks
  Amount Num(19,6) Amount
  AmountSC Num(19,6) Amount (SC)
  SerialNo nVarChar(30) Serial Number
  VisOrder Int(11) Visual Order
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=234000032 ->ADP1

# PRR24 - Goods Return Request - Tracking Note Assignment
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  ItemCCDNum nVarChar(40) Item CCD Number
  CntrOrigin nVarChar(3) Country/Region of Origin
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=234000032 ->ADP1
  SubLineNum Int(11) BOM Line No.

# PRR25 - Goods Return Request - Amt Per VAT Grp
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, VatGroup, Type
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  VatGroup nVarChar(8) Tax Definition ->OVTG
  VatPrcnt Num(19,6) Tax Rate
  BaseAmnt Num(19,6) Base Amount
  BaseAmntFC Num(19,6) Base Amount (FC)
  BaseAmntSC Num(19,6) Base Amount (SC)
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  Type Int(11) Type default=1 [1=Discount by Tax]
  Currency nVarChar(3) Price Currency
  Rate Num(19,6) Currency Rate
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=234000032 ->ADP1

# PRR26 - A/P Return Request - E-Way Bill Information
Module: Marketing Documents | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPRR
  SuplyType nVarChar(20) EWB Transaction Type [O=Outward, I=Inward]
  SubSplyTyp Int(11) EWB Sub-Type ->OEST
  DocType nVarChar(3) EWB Doc. Type ->OEDT
  TransMode Int(11) EWB Transportation Mode ->OETM
  Distance Num(19,6) EWB Transport Distance
  TransDocNo nVarChar(16) EWB Transporter Doc. No.
  TransDate Date(8) EWB Transportation Date
  VehicleTyp nVarChar(2) EWB Vehicle Type ->OEVT
  VehicleNo nVarChar(15) EWB Vehicle Number
  EWayBillNo nVarChar(20) EWB No.
  EwbDate Date(8) E-Way Bill Date
  FrmTraName nVarChar(100) EWB Consignor Name
  FrmAddres1 nVarChar(120) EWB Consignor Address 1
  FrmAddres2 nVarChar(120) EWB Consignor Address 2
  FrmZipCode nVarChar(20) EWB Consignor Zip Code
  ActFrmStat nVarChar(2) Dispatch State of EWB Consignor
  ToTraName nVarChar(100) EWB Consignee Name
  ToAddres1 nVarChar(120) EWB Consignee Address 1
  ToAddres2 nVarChar(120) EWB Consignee Address 2
  ToZipCode nVarChar(20) EWB Consignee Zip Code
  ActToState nVarChar(2) Ship-To State of EWB Consignee
  FrmGSTN nVarChar(15) EWB Consignor GSTN
  FrmState nVarChar(2) Bill-To State of EWB Consignor
  ToGSTN nVarChar(15) EWB Consignee GSTN
  ToState nVarChar(2) Bill-To State of EWB Consignee
  MainHsnEnt Int(11) EWB Main HSN Entry ->OCHP
  FrmPlace nVarChar(50) EWB Consignor Place
  ToPlace nVarChar(50) EWB Consignee Place
  TransID nVarChar(15) EWB Transporter ID
  TransName nVarChar(25) EWB Transporter Name
  ExpireDate Date(8) EWB Expiration Date
  ObjectType nVarChar(20) Object Type default=234000032 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TspEntry Int(11) Transporter Abs. Entry ->OTSP
  TspLine Int(11) Transportation Line
  TransType Int(11) Transaction Type [1=Regular, 2=Bill To-Ship To, 3=Bill From-Dispatch From, 4=Combination of 2 and 3]

# PRR27 - A/P Return Request - E-Books(GR) Rows
Module: Marketing Documents | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  RELATE_ROW: DocEntry, RelateType, RelateLine, GroupNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPRR
  LineNum Int(11) Row Number
  RelateType Int(11) Relation Type default=-1 [1=Row, 2=Row Expenses, 3=Document Expenses, 13=Distributed Freights, -1=Manual]
  RelateLine Int(11) Relation Row Number default=-1
  GroupNum Int(11) Group Number default=-1
  LineTotal Num(19,6) Line Total
  LineTotalF Num(19,6) Line Total (FC)
  LineTotalS Num(19,6) Line Total (SC)
  InClassTyp Int(11) Income Classification Type ->OICP
  InClassCat Int(11) Income Classification Category ->OICC
  ExClassTyp Int(11) Expense Classification Type ->OECP
  ExClassCat Int(11) Expense Classification Cat. ->OECC
  VatCate Int(11) VAT Category
  NetValue Num(19,6) Net Value
  NetValueFC Num(19,6) Net Value (FC)
  NetValueSC Num(19,6) Net Value (SC)
  VatAmount Num(19,6) VAT Amount
  VatAmFC Num(19,6) VAT Amount (FC)
  VatAmSC Num(19,6) VAT Amount (SC)
  WtPercCat Int(11) Withheld Percentage Category
  WtAmount Num(19,6) Withheld Amount
  WtAmountFC Num(19,6) Withheld Amount (FC)
  WtAmountSC Num(19,6) Withheld Amount (SC)
  ObjectType nVarChar(20) Object Type default=13 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  WtCategory VarChar(1) Withheld Category [I=Invoice, P=Payment]
  VATClassTy Int(11) VAT Classification Type ->OECP
  VATClassCa Int(11) VAT Classification Category ->OECC
  EBVatExCau Int(11) VAT Exemption Cause ->OVEC

# PRR28 - Goods Return Request - Reported Tracking Note
Module: Marketing Documents | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
  TCN_KEY U: DocEntry, LineNum, TrackingNt, TrackiNtLn
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  UnusedQty Num(19,6) Unused Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=234000032 ->ADP1
  SubLineNum Int(11) BOM Line No.

# PRR3 - A/P Return Request - Freight
Module: Marketing Documents | 80 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  DOCUMENT: DocEntry, BaseAbsEnt
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPRR
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  Comments nVarChar(100) Remarks
  ObjType nVarChar(20) Object Type default=234000032 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  WTLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  VatApplied Num(19,6) Vat Applied
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatF Num(19,6) Net Tax Amount (FC)
  LineVatS Num(19,6) Net Tax Amount (SC)
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 20=Goods Receipt PO, 18=A/P Invoice]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No.
  LineNum Int(11) line num default=-1
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Doc. Internal No. default=-1
  StDstr Num(19,6) Stock Distributed Sum
  StDstrSC Num(19,6) Stock Distributed Sum (SC)
  StDstrFC Num(19,6) Stock Distributed Sum (FC)
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  TaxDistMtd VarChar(1) Tax Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  GrsAmount Num(19,6) Gross Amount
  GrsFC Num(19,6) Gross Amount (FC)
  GrsSC Num(19,6) Gross Amount (SC)
  BaseTotal VarChar(1) Base Total for Calculation default=N [N=Net Total, G=Gross Total]
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)
  RRVatLC Num(19,6) Return Request VAT Amount
  RRVatFC Num(19,6) Return Request VAT Amount (FC)
  RRVatSC Num(19,6) Return Request VAT Amount (SC)
  EncryptIV nVarChar(100) Encrypt IV
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]

# PRR4 - A/P Return Request - Tax Amount per Document
Module: Marketing Documents | 61 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SCONDARY: DocEntry, LineNum, GroupNum, ExpnsCode, StcCode, StaCode, staType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPRR
  LineNum Int(11) Row Number default=-1
  GroupNum Int(11) Group Number default=-1
  ExpnsCode Int(11) Expense Code default=-1 ->OEXD
  RelateType Int(11) Relation Type default=1 [1=Row, 2=Row Expenses, 3=Document Expenses, 13=Distributed Freights]
  StcCode nVarChar(8) Tax Code ->OSTC
  StaCode nVarChar(8) Authority Code ->OSTA
  staType Int(11) Authority Type ->OSTT
  TaxRate Num(19,6) Tax Rate
  TaxAcct nVarChar(15) Tax Account ->OACT
  TaxSum Num(19,6) Tax Amount
  TaxSumFrgn Num(19,6) Tax Amount (FC)
  TaxSumSys Num(19,6) Tax Amount (SC)
  BaseSum Num(19,6) Base Amount
  BaseSumFrg Num(19,6) Base Amount (FC)
  BaseSumSys Num(19,6) Base Amount (SC)
  ObjectType nVarChar(20) Object Type default=234000032 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Status default=Y [Y=Normal Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) Applied Tax
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  LineSeq Int(11) Row Sequence
  DeferrAcct nVarChar(15) Deferred Tax Account ->OACT
  BaseType Int(11) Base Document Type default=-1
  BaseAbs Int(11) Base Document Internal No. default=-1
  BaseSeq Int(11) Base Doc. Row Sequence
  DeductTax Num(19,6) Deductible Tax Amount
  DdctTaxFrg Num(19,6) Deductible Tax Amount (FC)
  DdctTaxSys Num(19,6) Deductible Tax Amount (SC)
  BaseAppld Num(19,6) Applied Base Amount
  BaseApldFC Num(19,6) Applied Base Amount (FC)
  BaseApldSC Num(19,6) Applied Base Amount (SC)
  NonDdctPrc Num(19,6) Non Deductible %
  NonDdctAct nVarChar(15) Non Deductible Account ->OACT
  TaxInPrice VarChar(1) Tax Included in Price? default=N [Y=Yes, N=No]
  Exempt VarChar(1) Exempt? default=N [Y=Yes, N=No]
  TaxExpAct nVarChar(15) Expense Account for Tax ->OACT
  OnHoldTax Num(19,6) On Hold Tax Amount
  OnHoldTaxF Num(19,6) On Hold Tax Amount (FC)
  OnHoldTaxS Num(19,6) On Hold Tax Amount (SC)
  InGrossRev VarChar(1) Included in Gross Revenue default=N [Y=Yes, N=No]
  TaxSumOrg Num(19,6) Tax Amount Original
  TaxSumOrgF Num(19,6) Tax Amount Original (FC)
  TaxSumOrgS Num(19,6) Tax Amount Original (SC)
  OpenTax Num(19,6) Open Service Tax
  OpenTaxFC Num(19,6) Open Service Tax (FC)
  OpenTaxSC Num(19,6) Open Service Tax (SC)
  Unencumbrd VarChar(1) Unencumbered default=N [Y=Yes, N=No]
  TaxOnRI VarChar(1) Tax On Reserve Invoice default=N [Y=Yes, N=No]
  RvsChrgPrc Num(19,6) Reverse Charge %
  RvsChrgTax Num(19,6) Reverse Charge Tax Amount
  RvsChrgSC Num(19,6) Reverse Charge Tax Amount (SC)
  RvsChrgFC Num(19,6) Reverse Charge Tax Amount (FC)
  InFirstIns VarChar(1) Included in First Installment default=N [Y=Yes, N=No]
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CESTrel VarChar(1) CEST Relevant default=N [Y=, N=]

# PRR5 - A/P Return Request - Withholding Tax
Module: Marketing Documents | 158 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  SECONDERY U: AbsEntry, WTCode, BaseAbsEnt, Doc1LineNo
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OPRR
  WTCode nVarChar(4) WTax Code ->OWHT
  Rate Num(19,6) Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntSC Num(19,6) Taxable Amount (SC)
  TxblAmntFC Num(19,6) Taxable Amount (FC)
  WTAmnt Num(19,6) WTax Amount
  WTAmntSC Num(19,6) WTax Amount (SC)
  WTAmntFC Num(19,6) WTax Amount (FC)
  ApplAmnt Num(19,6) Applied WTax Amount
  ApplAmntSC Num(19,6) Applied WTax Amount (SC)
  ApplAmntFC Num(19,6) Applied WTax Amount (FC)
  Category VarChar(1) Category [P=Payment, I=Invoice]
  Criteria VarChar(1) Criteria [Y=Accrual, N=Cash]
  Account nVarChar(15) G/L Account ->OACT
  Type VarChar(1) Withholding Tax Type [V=VAT Withholding, I=Income Tax Withholding]
  RoundType VarChar(1) Rounding Type [T=Truncated, C=Commercial Values, N=No Rounding]
  BaseType VarChar(1) Base Type [G=Gross, N=Net, V=VAT, U=UoM]
  BaseAbsEnt Int(11) Base Document Internal No. default=-1
  BaseLine Int(11) Base Row
  BaseNum Int(11) Base Document Type default=-1 [-1=, 0=, 23=Sales Quotation, 17=Sales Order, 15=Delivery]
  LineNum Int(11) Row Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Doc. Internal No. default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=13 ->ADP1
  Doc1LineNo Int(11) DOC1 Line Number default=-1
  WtLineType VarChar(1) WTax Row Type default=D [D=Document Level WTax, L=Row Level WTax]
  TxblCurr nVarChar(3) Taxable Currency from Doc Line
  DtblCurr nVarChar(3) Deductible Currency
  DtblRate Num(19,6) Rate for Deductible Amount
  txblRate Num(19,6) Rate for Taxable Amount
  DtblAmount Num(19,6) Deductible Amount
  TdsAcc nVarChar(15) TDS Account ->OACT
  SurAcc nVarChar(15) Surcharge Account ->OACT
  CessAcc nVarChar(15) Cess Account ->OACT
  HscAcc nVarChar(15) HSC Account ->OACT
  TdsRate Num(19,6) TDS Rate
  SurRate Num(19,6) Surcharge Rate
  CessRate Num(19,6) Cess Rate
  HscRate Num(19,6) HSC Rate
  TdsBAmt Num(19,6) TDS Base Amount
  TdsBAmtSC Num(19,6) TDS Base Amount (SC)
  TdsBAmtFC Num(19,6) TDS Base Amount (FC)
  SurBAmt Num(19,6) Surcharge Base Amount
  SurBAmtSC Num(19,6) Surcharge Base Amount (SC)
  SurBAmtFC Num(19,6) Surcharge Base Amount (FC)
  CessBAmt Num(19,6) Cess Base Amount
  CessBAmtSC Num(19,6) Cess Base Amount (SC)
  CessBAmtFC Num(19,6) Cess Base Amount (FC)
  HscBAmt Num(19,6) HSC Base Amount
  HscBAmtSC Num(19,6) HSC Base Amount (SC)
  HscBAmtFC Num(19,6) HSC Base Amount (FC)
  TdsAmnt Num(19,6) TDS Tax Amount
  TdsAmntSC Num(19,6) TDS Tax Amount (SC)
  TdsAmntFC Num(19,6) TDS Tax Amount (FC)
  SurAmnt Num(19,6) Surcharge Tax Amount
  SurAmntSC Num(19,6) Surcharge Tax Amount (SC)
  SurAmntFC Num(19,6) Surcharge Tax Amount (FC)
  CessAmnt Num(19,6) Cess Tax Amount
  CessAmntSC Num(19,6) Cess Tax Amount (SC)
  CessAmntFC Num(19,6) Cess Tax Amount (FC)
  HscAmnt Num(19,6) HSC Tax Amount
  HscAmntSC Num(19,6) HSC Tax Amount (SC)
  HscAmntFC Num(19,6) HSC Tax Amount (FC)
  TdsAppl Num(19,6) Applied TDS Amount
  TdsApplSC Num(19,6) Applied TDS Amount (SC)
  TdsApplFC Num(19,6) Applied TDS Amount (FC)
  SurAppl Num(19,6) Applied Surcharge Amount
  SurApplSC Num(19,6) Applied Surcharge Amount (SC)
  SurApplFC Num(19,6) Applied Surcharge Amount (FC)
  CessAppl Num(19,6) Applied Cess Amount
  CessApplSC Num(19,6) Applied Cess Amount (SC)
  CessApplFC Num(19,6) Applied Cess Amount (FC)
  HscAppl Num(19,6) Applied HSC Amount
  HscApplSC Num(19,6) Applied HSC Amount (SC)
  HscApplFC Num(19,6) Applied HSC Amount (FC)
  BatchNum Int(11) Journal Voucher No.
  InCSTCode nVarChar(2) CST Code Incoming
  OutCSTCode nVarChar(2) CST Code Outgoing
  DpmWTApl Num(19,6) DPM WT Applied Amount
  DpmWTAplSC Num(19,6) DPM WT Applied Amount (SC)
  DpmWTAplFC Num(19,6) DPM WT Applied Amount (FC)
  WTTypeId Int(11) WT Type Id ->OWTT
  LnBsAmt Num(19,6) BR Line WT Base Amount
  LnBsAmtSC Num(19,6) BR Line WT Base Amount(SC)
  LnBsAmtFC Num(19,6) BR Line WT Base Amount(FC)
  LnCmTAmt Num(19,6) BR Line Cumulated Taxable Amount
  LnCmTAmtSC Num(19,6) BR Line Cumulated Taxable Amount(SC)
  LnCmTAmtFC Num(19,6) BR Line Cumulated Taxable Amount(FC)
  TDSType VarChar(1) TDS Type [E=eTDS, D=GST TDS, C=GST TCS, S=SALES TCS]
  IgstAcc nVarChar(15) IGST Account ->OACT
  CgstAcc nVarChar(15) CGST Account ->OACT
  SgstAcc nVarChar(15) SGST Account ->OACT
  IgstAmnt Num(19,6) IGST Tax Amount
  IgstAmntSC Num(19,6) IGST Tax Amount (SC)
  IgstAmntFC Num(19,6) IGST Tax Amount (FC)
  CgstAmnt Num(19,6) CGST Tax Amount
  CgstAmntSC Num(19,6) CGST Tax Amount (SC)
  CgstAmntFC Num(19,6) CGST Tax Amount (FC)
  SgstAmnt Num(19,6) SGST Tax Amount
  SgstAmntSC Num(19,6) SGST Tax Amount (SC)
  SgstAmntFC Num(19,6) SGST Tax Amount (FC)
  IgstRate Num(19,6) IGST Rate
  CgstRate Num(19,6) CGST Rate
  SgstRate Num(19,6) SGST Rate
  IgstBAmt Num(19,6) IGST Base Amount
  IgstBAmtSC Num(19,6) IGST Base Amount (SC)
  IgstBAmtFC Num(19,6) IGST Base Amount (FC)
  CgstBAmt Num(19,6) CGST Base Amount
  CgstBAmtSC Num(19,6) CGST Base Amount (SC)
  CgstBAmtFC Num(19,6) CGST Base Amount (FC)
  SgstBAmt Num(19,6) SGST Base Amount
  SgstBAmtSC Num(19,6) SGST Base Amount (SC)
  SgstBAmtFC Num(19,6) SGST Base Amount (FC)
  IgstAppl Num(19,6) Applied IGST Amount
  IgstApplSC Num(19,6) Applied IGST Amount (SC)
  IgstApplFC Num(19,6) Applied IGST Amount (FC)
  CgstAppl Num(19,6) Applied CGST Amount
  CgstApplSC Num(19,6) Applied CGST Amount (SC)
  CgstApplFC Num(19,6) Applied CGST Amount (FC)
  SgstAppl Num(19,6) Applied SGST Amount
  SgstApplSC Num(19,6) Applied SGST Amount (SC)
  SgstApplFC Num(19,6) Applied SGST Amount (FC)
  UtgstAcc nVarChar(15) UTGST Account ->OACT
  CsgstAcc nVarChar(15) Cess GST Account ->OACT
  UtgstAmt Num(19,6) UTGST Tax Amount
  UtgstAmtSC Num(19,6) UTGST Tax Amount (SC)
  UtgstAmtFC Num(19,6) UTGST Tax Amount (FC)
  CsgstAmt Num(19,6) Cess GST Tax Amount
  CsgstAmtSC Num(19,6) Cess GST Tax Amount (SC)
  CsgstAmtFC Num(19,6) Cess GST Tax Amount (FC)
  UtgstRate Num(19,6) UTGST Rate
  CsgstRate Num(19,6) Cess GST Rate
  UtgstBAmt Num(19,6) UTGST Base Amount
  UtgstBAmtS Num(19,6) UTGST Base Amount (SC)
  UtgstBAmtF Num(19,6) UTGST Base Amount (FC)
  CsgstBAmt Num(19,6) Cess GST Base Amount
  CsgstBAmtS Num(19,6) Cess GST Base Amount (SC)
  CsgstBAmtF Num(19,6) Cess GST Base Amount (FC)
  UtgstAppl Num(19,6) Applied UTGST Amount
  UtgstApplS Num(19,6) Applied UTGST Amount (SC)
  UtgstApplF Num(19,6) Applied UTGST Amount (FC)
  CsgstAppl Num(19,6) Applied Cess GST Amount
  CsgstApplS Num(19,6) Applied Cess GST Amount (SC)
  CsgstApplF Num(19,6) Applied Cess GST Amount (FC)
  EncryptIV nVarChar(100) Encrypt IV
  TcsIntAcct nVarChar(15) TCS Interim Account ->OACT
  SurIntAcct nVarChar(15) Surcharge Interim Account ->OACT
  CesIntAcct nVarChar(15) Cess Interim Account ->OACT
  HscIntAcct nVarChar(15) HSC interim Account ->OACT
  LnIntAcct nVarChar(15) Interim Account for Tax ->OACT
  FixedAmnt Num(19,6) Fixed Amount
  FixedAmtSC Num(19,6) Fixed Amount (SC)
  FixedAmtFC Num(19,6) Fixed Amount (FC)
  BaseQty Num(19,6) Base Quantity

# PRR6 - A/P Return Request - Installments
Module: Marketing Documents | 65 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, InstlmntID
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPRR
  InstlmntID Int(6) Installment ID default=1
  ObjType nVarChar(20) Object Type default=234000032 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DueDate Date(8) Due Date
  Status VarChar(1) Installment Status default=O [O=Open, C=Closed]
  DunnLevel Int(11) Dunning Level default=0
  InsTotal Num(19,6) Total Installment
  InsTotalFC Num(19,6) Total Installment (FC)
  InsTotalSy Num(19,6) Total Installment (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  VatSum Num(19,6) Total Tax
  VatSumFC Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  VatPaid Num(19,6) Tax Paid to Date
  VatPaidFC Num(19,6) Tax Paid (FC)
  VatPaidSys Num(19,6) Tax Paid (SC)
  TotalExpns Num(19,6) Total Freight Charges
  TotalExpFC Num(19,6) Total Freight Charges (FC)
  TotalExpSC Num(19,6) Total Freight Charges (SC)
  ExpAppl Num(19,6) Applied Freight Charges
  ExpApplFC Num(19,6) Applied Freight Charges (FC)
  ExpApplSC Num(19,6) Applied Freight Charges (SC)
  WTSum Num(19,6) WTax Amount
  WTSumFC Num(19,6) WTax Amount (FC)
  WTSumSC Num(19,6) WTax Amount (SC)
  WTApplied Num(19,6) Applied WTax
  WTAppliedF Num(19,6) Applied WTax (FC)
  WTAppliedS Num(19,6) Applied WTax (SC)
  TotalBlck Num(19,6) Total Reserved Amount
  TotalBlckF Num(19,6) Total Reserved Amount (FC)
  TotalBlckS Num(19,6) Total Reserved Amount (SC)
  VATBlck Num(19,6) Reserved Tax Amount
  VATBlckFC Num(19,6) Reserved Tax Amount (FC)
  VATBlckSC Num(19,6) Reserved Tax Amount (SC)
  ExpnsBlck Num(19,6) Reserved Freight Charges
  ExpnsBlckF Num(19,6) Reserved Freight Charges (FC)
  ExpnsBlckS Num(19,6) Reserved Freight Charges (SC)
  WTBlocked Num(19,6) Reserved WTax Amount
  WTBlockedF Num(19,6) Reserved WTax Amount (FC)
  WTBlockedS Num(19,6) Reserved WTax Amount (SC)
  InstPrcnt Num(19,6) Installment %
  DunWizBlck VarChar(1) Wizard dunning block default=N [N=No, Y=Yes]
  DunDate Date(8) Last Dunning Date
  Paid Num(19,6) Paid
  PaidFrgn Num(19,6) Paid (FC)
  PaidSc Num(19,6) Paid (SC)
  reserved VarChar(1) Reserved default=N [N=No, Y=Yes]
  TaxOnExp Num(19,6) Tax on Freight
  TaxOnExpFc Num(19,6) Tax on Expenses (FC)
  TaxOnExpSc Num(19,6) Tax on Expenses (SC)
  TaxOnExpAp Num(19,6) Applied Tax on Expenses
  TaxOnExApF Num(19,6) Applied Tax on Expenses (FC)
  TaxOnExApS Num(19,6) Applied Tax on Expenses (SC)
  TaxOnExBlo Num(19,6) Reserved Tax on Freight Amount
  TaxOnExBlF Num(19,6) Reserved Tax on Freight Amt FC
  TaxOnExBlS Num(19,6) Reserved Tax on Freight Amt SC
  LvlUpdDate Date(8) Dunning Level Update Date
  Ordered VarChar(1) Payment Ordered default=N [Y=Yes, N=No]
  PaidDpm Num(19,6) Paid by Down Payment
  PaidDpmFc Num(19,6) Paid by Down Payment (FC)
  PaidDpmSc Num(19,6) Paid by Down Payment (SC)
  EncryptIV nVarChar(100) Encrypt IV

# PRR7 - A/P Return Request - Delivery Packages
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OINV
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type default=234000032 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV

# PRR8 - A/P Return Request - Items in Package
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum, ItemCode, UomEntry, NumPerMsr
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPRR
  PackageNum Int(11) Package Number
  ItemCode nVarChar(50) Item Code ->OITM
  Quantity Num(19,6) Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=234000032 ->ADP1
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value default=0

# PRR9 - A/P Return Request - Drawn Dpm
Module: Marketing Documents | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPRR
  LineNum Int(11) Row Number
  BaseAbs Int(11) Base Document Internal ID ->ODPI
  BaseLine Int(11) Base Document Row
  TargetBase VarChar(1) Target or Base Document default=T [B=Base, T=Target]
  ObjType nVarChar(20) Base Object Type default=203 [203=A/R Down Payment]
  DrawnSum Num(19,6) Net LC
  DrawnSumFc Num(19,6) Net FC
  DrawnSumSc Num(19,6) Net SC
  LogInstanc Int(11) Log Instance default=0
  ObjCode nVarChar(20) Object Type default=234000032 ->ADP1
  ApplDrawn Num(19,6) Applied Net LC
  ApplDrawnF Num(19,6) Applied Net FC
  ApplDrawnS Num(19,6) Applied Net SC
  BaseDocNum Int(11) Base Document Number
  BsDocDate Date(8) Base Posting Date
  BsDueDate Date(8) Base Due Date
  BsCardName nVarChar(100) Base BP Name
  BsComments nVarChar(254) Base Remarks
  Posted VarChar(1) Base Document Posted default=Y [Y=Yes, N=No]
  Vat Num(19,6) Tax LC
  VatFc Num(19,6) Tax FC
  VatSc Num(19,6) Tax SC
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  IsGross VarChar(1) Is Gross Line default=N [N=Net Line, Y=Gross Line]

# PWZ7 - Payment Wizard 7-Selected Branches
Module: Marketing Documents | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: IdNumber, BPLId
Fields (name type(len) description [values] ->parent table):
  IdNumber Int(11) ID Number ->OPWZ
  BPLId Int(11) Assigned Branch ->OBPL

# QUT1 - Sales Quotation - Rows
Module: Marketing Documents | 317 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  STATUS: LineStatus
  CURRENCY: Currency
  ACCOUNT: AcctCode
  BASE_ENTRY: BaseEntry, BaseType, BaseLine
  VIS_ORDER: DocEntry, VisOrder
  OWNER_CODE: OwnerCode
  ITM_WHS_OQ: ItemCode, WhsCode, OpenQty
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OQUT
  LineNum Int(11) Row Number
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=, 17=Sales Order, 15=Delivery Notes, 13=A/R Invoice, 203=A/R Down Payment]
  TrgetEntry Int(11) Target Document Internal ID
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=]
  BaseEntry Int(11) Base Document Internal ID
  BaseLine Int(11) Base Row
  LineStatus VarChar(1) Row Status default=O [O=Open, C=Closed]
  ItemCode nVarChar(50) Item No. ->OITM
  Dscription nVarChar(200) Item/Service Description
  Quantity Num(19,6) Quantity
  ShipDate Date(8) Row Delivery Date
  OpenQty Num(19,6) Remaining Open Quantity
  Price Num(19,6) Price
  Currency nVarChar(3) Price Currency ->OCRN
  Rate Num(19,6) Currency Rate
  DiscPrcnt Num(19,6) Discount % per Row
  LineTotal Num(19,6) Row Total
  TotalFrgn Num(19,6) Row Total (FC)
  OpenSum Num(19,6) Open Amount
  OpenSumFC Num(19,6) Open Amount (FC)
  VendorNum nVarChar(50) Vendor Catalog No.
  SerialNum nVarChar(17) Serial Number
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  SlpCode Int(11) Sales Employee Code default=-1 ->OSLP
  Commission Num(19,6) Commission Percentage
  TreeType VarChar(1) BOM Type default=N [N=Not a BOM, A=Assembly, S=Sales, I=Sales BOM Component, P=Production, T=Template]
  AcctCode nVarChar(15) Account Code ->OACT
  TaxStatus VarChar(1) Tax Definition [Y=Yes, N=No]
  GrossBuyPr Num(19,6) Gross Profit Base Price
  PriceBefDi Num(19,6) Price Before Discount
  DocDate Date(8) Posting Date
  Flags Int(11) Flags default=0
  OpenCreQty Num(19,6) Credit Memo Amount
  UseBaseUn VarChar(1) Inventory UoM default=N [Y=Yes, N=No]
  SubCatNum nVarChar(50) BP Catalog No. ->OSCN
  BaseCard nVarChar(15) Base BP Code ->OCRD
  TotalSumSy Num(19,6) Row Total in SC
  OpenSumSys Num(19,6) Open Amount in SC
  InvntSttus VarChar(1) Whse Status default=O [O=Open, C=Closed]
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  CodeBars nVarChar(254) Bar Code
  VatPrcnt Num(19,6) Tax Rate per Row
  VatGroup nVarChar(8) Tax Definition ->OVTG
  PriceAfVAT Num(19,6) Gross Price after Discount
  Height1 Num(19,6) Height 1
  Hght1Unit Int(6) Unit of Height 1
  Height2 Num(19,6) Height 2
  Hght2Unit Int(6) Unit of Height 2
  Width1 Num(19,6) Width 1
  Wdth1Unit Int(6) Unit of Width 1
  Width2 Num(19,6) Width 2
  Wdth2Unit Int(6) Unit of Width 2
  Length1 Num(19,6) Length 1
  Len1Unit Int(6) Unit of Length 1
  length2 Num(19,6) Length 2
  Len2Unit Int(6) Unit of Length 2
  Volume Num(19,6) Quantity
  VolUnit Int(6) Vol. Unit
  Weight1 Num(19,6) Weight 1
  Wght1Unit Int(6) Unit of Weight 1
  Weight2 Num(19,6) Weight 2
  Wght2Unit Int(6) Unit of Weight 2
  Factor1 Num(19,6) Factor 1
  Factor2 Num(19,6) Factor 2
  Factor3 Num(19,6) Factor 3
  Factor4 Num(19,6) Factor 4
  PackQty Num(19,6) Packing Quantity
  UpdInvntry VarChar(1) Whse Update default=Y [Y=Yes, N=No]
  BaseDocNum Int(11) Base Document No.
  BaseAtCard nVarChar(100) Customer/Vendor Base Document
  SWW nVarChar(16) Additional Identifier
  VatSum Num(19,6) Tax Total
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  FinncPriod Int(11) Posting Period ->OFPR
  ObjType nVarChar(20) Object Type default=23 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BlockNum nVarChar(100) Block Number
  ImportLog nVarChar(20) Import Log
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAqcuistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  DistribSum Num(19,6) Distributed Amount
  DstrbSumFC Num(19,6) Distributed Amount (FC)
  DstrbSumSC Num(19,6) Distributed Amount (SC)
  GrssProfit Num(19,6) Row Gross Profit
  GrssProfSC Num(19,6) Row Gross Profit (SC)
  GrssProfFC Num(19,6) Row Gross Profit (FC)
  VisOrder Int(11) Visual Order
  INMPrice Num(19,6) Item's Last Sales Price (OINM)
  PoTrgNum Int(11) PO Target No.
  PoTrgEntry nVarChar(11) PO Target Internal ID
  DropShip VarChar(1) Drop-Ship default=N [Y=Yes, N=No]
  PoLineNum Int(11) PO Target Row No.
  Address nVarChar(254) Address
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type [Y=Regular Tax, N=No Tax, U=Use Tax]
  OrigItem nVarChar(50) Original Item ->OITM
  BackOrdr VarChar(1) Allow Back Order [Y=Yes, N=No]
  FreeTxt nVarChar(100) Free Text
  PickStatus VarChar(1) Pick Status default=N [Y=Picked, N=Not Picked, R=Released for Picking, P=Partially Picked]
  PickOty Num(19,6) Pick Quantity
  PickIdNo Int(11) Pick ID
  TrnsCode Int(6) Shipping Method default=-1 ->OSHP
  VatAppld Num(19,6) Applied Tax
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  BaseQty Num(19,6) Base Quantity
  BaseOpnQty Num(19,6) Base Open Quantity
  VatDscntPr Num(19,6) Tax Discount %
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  DeferrTax VarChar(1) Deferred Tax default=N [Y=Yes, N=No]
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatlF Num(19,6) Net Tax Amount
  LineVatS Num(19,6) Net Tax Amount
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value
  CEECFlag VarChar(1) Correction Invoice Item W/S default=S [W=Was, S=Should be]
  ToStock Num(19,6) Corr. Invoice Amount to Inventory Acct
  ToDiff Num(19,6) Corr. Invoice Amount to Diff.
  ExciseAmt Num(19,6) Excise Amount
  TaxPerUnit Num(19,6) Tax per Unit
  TotInclTax Num(19,6) Total (incl. Tax)
  CountryOrg nVarChar(3) Country/Region of Origin
  StckDstSum Num(19,6) Stock Distribute Sum
  ReleasQtty Num(19,6) Released Quantity
  LineType VarChar(1) Row Type default=R [R=Regular, A=Alternative]
  TranType VarChar(1) Transaction Type [C=Complete, R=Reject]
  Text Text(16) Text
  OwnerCode Int(11) Document Owner
  StockPrice Num(19,6) Item Cost
  ConsumeFCT VarChar(1) Consumer Sales Forecast [Y=Yes, N=No]
  LstByDsSum Num(19,6) Last Buy Distribute Sum
  StckINMPr Num(19,6) Stock Inm Price
  LstBINMPr Num(19,6) Last Buy Inm Price
  StckDstFc Num(19,6) Stock Distribute Sum Foreign
  StckDstSc Num(19,6) Stock Distribute Sum System
  LstByDsFc Num(19,6) Last Buy Distribute Sum (FC)
  LstByDsSc Num(19,6) Last Buy Distribute Sum SC
  StockSum Num(19,6) Stock Sum
  StockSumFc Num(19,6) Stock Sum FC
  StockSumSc Num(19,6) Stock Sum SC
  StckSumApp Num(19,6) Stock Sum Applied
  StckAppFc Num(19,6) Stock Sum Applied FC
  StckAppSc Num(19,6) Stock Sum Applied SC
  ShipToCode nVarChar(50) Ship-to Code
  ShipToDesc nVarChar(254) Ship-to Description
  StckAppD Num(19,6) Stock Distribution Applied Sum
  StckAppDFC Num(19,6) Stock Distribution Applied Sum
  StckAppDSC Num(19,6) Stock Distribution Applied Sum
  BasePrice VarChar(1) Price for Total Calculation default=E [E=Exclude Tax, I=Include Tax]
  GTotal Num(19,6) Gross Total
  GTotalFC Num(19,6) Gross Total FC
  GTotalSC Num(19,6) Gross Total SC
  DistribExp VarChar(1) Distribute Expense [Y=Yes, N=No]
  DescOW VarChar(1) DESC_OVERWRITTEN default=N [Y=Yes, N=No]
  DetailsOW VarChar(1) DETAILS_OVERWRITTEN default=N [Y=Yes, N=No]
  GrossBase Int(6) Base Method for Gross Profit
  VatWoDpm Num(19,6) Tax Before DPM Applied
  VatWoDpmFc Num(19,6) Tax Before DPM Applied FC
  VatWoDpmSc Num(19,6) Tax Before DPM Applied SC
  CFOPCode nVarChar(6) CFOP Code for Document ->OCFP
  CSTCode nVarChar(6) CST Code for ICMS
  Usage Int(11) Usage Code for Document ->OUSG
  TaxOnly VarChar(1) Tax Only [Y=Yes, N=No]
  WtCalced VarChar(1) WTax Calculated default=N [N=No, Y=Yes]
  QtyToShip Num(19,6) Quantity to Ship
  DelivrdQty Num(19,6) Delivered Quantity
  OrderedQty Num(19,6) Ordered Quantity
  CogsOcrCod nVarChar(8) COGS Distribution Rule Code ->OOCR
  CiOppLineN Int(11) Line Number of Opposite Line default=-1
  CogsAcct nVarChar(15) COGS Account Code ->OACT
  ChgAsmBoMW VarChar(1) Change Whs for Asm BoM Child [Y=Yes, N=No]
  ActDelDate Date(8) Actual Delivery Date
  OcrCode2 nVarChar(8) Costing Code 2 ->OOCR
  OcrCode3 nVarChar(8) Costing Code 3 ->OOCR
  OcrCode4 nVarChar(8) Costing Code 4 ->OOCR
  OcrCode5 nVarChar(8) Costing Code 5 ->OOCR
  TaxDistSum Num(19,6) Tax Distributed Amount
  TaxDistSFC Num(19,6) Tax Distributed Amount (FC)
  TaxDistSSC Num(19,6) Tax Distributed Amount (SC)
  PostTax VarChar(1) Post Tax in Price to Stock default=Y [Y=Yes, N=No]
  Excisable VarChar(1) Excisable [Yes/No] [Y=Yes, N=No]
  AssblValue Num(19,6) Assessable Value
  RG23APart1 Int(11) RG23A Part1 Number
  RG23APart2 Int(11) RG23A Part2 Number
  RG23CPart1 Int(11) RG23C Part1 Number
  RG23CPart2 Int(11) RG23C Part2 Number
  CogsOcrCo2 nVarChar(8) COGS Distribution Rule Code2 ->OOCR
  CogsOcrCo3 nVarChar(8) COGS Distribution Rule Code3 ->OOCR
  CogsOcrCo4 nVarChar(8) COGS Distribution Rule Code4 ->OOCR
  CogsOcrCo5 nVarChar(8) COGS Distribution Rule Code5 ->OOCR
  LnExcised VarChar(1) Line Excised [O=Open, C=Closed, P=Copied to OEI]
  LocCode Int(11) Location Code ->OLCT
  StockValue Num(19,6) Total COGS Value
  GPTtlBasPr Num(19,6) Total Base Price for Profit
  unitMsr2 nVarChar(100) Pur/Sal UoM if BaseUnit
  NumPerMsr2 Num(19,6) Pur/Sal UoM Value if Base Unit
  SpecPrice VarChar(1) Price Source Type default=N [Y=Special Prices for Business Partner, N=Manual, W=Active Price List, Discount Groups, R=Active Price List, U=Inactive Price List, A=Blanket Agreement, P=Period and Volume Discounts, Q=Period and Volume Discounts, Discount Groups, V=Inactive Price List, Discount Groups, 9=Special Prices for Business Partner, !=Blanket Agreement, 0=Period and Volume Discounts, 1=Period and Volume Discounts, Discount Groups, 2=Active Price List, 7=Active Price List, Discount Groups, 5=Inactive Price List, 6=Inactive Price List, Discount Groups]
  CSTfIPI nVarChar(2) CST for IPI Code
  CSTfPIS nVarChar(2) CST for PIS Code
  CSTfCOFINS nVarChar(2) CST for COFINS Code
  ExLineNo nVarChar(10) ExLineNo
  isSrvCall VarChar(1) Created from Service Call default=N [Y=Yes, N=No]
  PQTReqQty Num(19,6) Pur Quotation: Required Qty
  PQTReqDate Date(8) Pur Quotation: Required Date
  PcDocType Int(11) Purchase Confirmation Doc Type default=-1 [-1=No Type, 22=Purchase Order, 540000006=Purchase Quotation]
  PcQuantity Num(19,6) Purchase Confirmation Quantity
  LinManClsd VarChar(1) Line Was Closed Manually default=N [Y=Yes, N=No, U=Unknown]
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  NoInvtryMv VarChar(1) Without Inventory Movement default=N [Y=Yes, N=No]
  ActBaseEnt Int(11) Actual Base Document Entry
  ActBaseLn Int(11) Actual Base Line Number
  ActBaseNum Int(11) Actual Base Document No.
  OpenRtnQty Num(19,6) Quantity Open for Return
  AgrNo Int(11) Agreement No. ->OOAT
  AgrLnNum Int(11) Agreement Row Number
  CredOrigin VarChar(1) Credit Origin ->OBSI
  Surpluses Num(19,6) Surpluses
  DefBreak Num(19,6) Defect and Breakup
  Shortages Num(19,6) Shortages
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  UomEntry2 Int(11) UoM Entry if Base Unit default=0 ->OUOM
  UomCode nVarChar(20) UoM Code
  UomCode2 nVarChar(20) UoM Code if Base Unit
  FromWhsCod nVarChar(8) From Warehouse Code ->OWHS
  NeedQty VarChar(1) Consider Quantity of Items default=N [Y=Yes, N=No]
  PartRetire VarChar(1) Partial Retirement default=N [Y=Yes, N=No]
  RetireQty Num(19,6) Retirement Quantity
  RetireAPC Num(19,6) Retirement APC
  RetirAPCFC Num(19,6) Retirement APC FC
  RetirAPCSC Num(19,6) Retirement APC SC
  InvQty Num(19,6) Quantity - Inventory UoM
  OpenInvQty Num(19,6) Open Quantity (Inventory UoM)
  EnSetCost VarChar(1) Enable Set Item Cost in Return default=N [Y=Yes, N=No]
  RetCost Num(19,6) Return Cost in A/R Return
  Incoterms Int(11) Incoterms default=0 ->ODCI
  TransMod Int(11) Transport Mode default=0 ->ODCI
  LineVendor nVarChar(15) Line Vendor Code ->OCRD
  DistribIS VarChar(1) Distribute Intrastat Freight default=N [Y=Yes, N=No]
  ISDistrb Num(19,6) Intrastat Distrib. Amount
  ISDistrbFC Num(19,6) Intrastat Distrib. Amount (FC)
  ISDistrbSC Num(19,6) Intrastat Distrib. Amount (SC)
  IsByPrdct VarChar(1) Item Is By-Product default=N [N=No, Y=Yes]
  ItemType Int(11) Item Type default=4 [4=Item]
  PriceEdit VarChar(1) Price Was Edited by User default=N [N=No, Y=Yes]
  PrntLnNum Int(11) Parent Line Number
  LinePoPrss VarChar(1) Line PO Process default=N [Y=Yes, N=No]
  FreeChrgBP VarChar(1) Free of Charge (BP) default=N [Y=Yes, N=No]
  TaxRelev VarChar(1) Tax Relevant Row default=Y [Y=Yes, N=No]
  LegalText nVarChar(254) Legal Text
  ThirdParty VarChar(1) Third Party default=N [Y=Yes, N=No]
  LicTradNum nVarChar(32) Federal Tax ID
  InvQtyOnly VarChar(1) Change Qty (Inv. UoM) Only default=N [Y=Yes, N=No]
  UnencReasn Int(11) Reason for Unencumbered ICMS
  ShipFromCo nVarChar(50) Ship-From Code
  ShipFromDe nVarChar(254) Ship-From Description
  FisrtBin nVarChar(228) First Bin Location
  AllocBinC nVarChar(11) Allocated Bin Location Count
  ExpType nVarChar(4) Expense Type ->OEXD
  ExpUUID nVarChar(50) Expense UUID
  ExpOpType VarChar(1) Expense Operation Type [P=Professional Services, R=Renting Assets, O=Others]
  DIOTNat nVarChar(3) DIOT Nationality ->OCRY
  MYFtype nVarChar(2) MYF type [S1=MYF Wholesale Sales, S2=Retail Sales, P1=MYF Wholesale Purchases, P3=Other Expense Transactions]
  GPBefDisc Num(19,6) Gross Price
  ReturnRsn Int(6) Return Reason default=-1
  ReturnAct Int(6) Return Action default=-1
  StgSeqNum Int(11) Stage Sequence Number
  StgEntry Int(11) Stage Entry ->ORST
  StgDesc nVarChar(100) Stage Description
  ItmTaxType nVarChar(2) Item GST Tax Category [GR=GST Regular, GN=GST Nil Rated, GE=GST Exempt, NE=Excisable, NN=Non-GST Non-Excisable]
  SacEntry Int(11) SAC Entry ->OSAC
  NCMCode Int(11) NCM Code default=-1 ->ONCM
  HsnEntry Int(11) HSN Entry
  OriBAbsEnt Int(11) Original Base Document Internal ID
  OriBLinNum Int(11) Original Base Document Line Number
  OriBDocTyp Int(11) Original Base Document Type
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No, U=Use]
  EncryptIV nVarChar(100) Encrypt IV
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  StdItemId Int(11) Standard Item Identification ->OUNCL
  CommClass Int(11) Commodity Classification ->OUNCL
  VatExEntry Int(11) VAT Exemption AbsEntry ->OVEB
  VatExLN Int(6) VAT Exemption LineNum
  NatOfTrans Int(11) Nature of Transaction ->ODCI
  ISDtCryImp nVarChar(3) Destination Country/Region for Import ->OCRY
  ISDtRgnImp Int(11) Destination Region for Import ->ODCI
  ISOrCryExp nVarChar(3) Country/Region of Origin for Export ->OCRY
  ISOrRgnExp Int(11) Region of Origin for Export ->ODCI
  NVECode nVarChar(6) NVE Code
  PoNum nVarChar(20) Customer's Purchase Order Number
  PoItmNum Int(11) Customer's Purchase Order Item Number
  IndEscala VarChar(1) Indicator for Relevant Scale default=N [Y=Yes, N=No]
  CESTCode Int(11) CEST Code ->OCEST
  CtrSealQty Num(19,6) Control Seal Quantity
  CNJPMan nVarChar(14) CNPJ of Manufacturer
  UFFiscBene nVarChar(10) UF Fiscal Benefit Code
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]
  LegalTIMD nVarChar(250) Legal Text from Item Master Data
  LegalTTCA nVarChar(250) Legal Text from Tax Code Attributes
  LegalTW nVarChar(250) Legal Text from Warehouse
  LegalTCD nVarChar(250) Legal Text from Tax Code Determination
  RevCharge VarChar(1) Reverse Charge default=N [Y=Yes, N=No]
  ListNum Int(6) Price List No. ->OPLN

# QUT10 - Sales Quotation - Row Structure
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SECONDARY U: DocEntry, AftLineNum, OrderNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OQUT
  LineSeq Int(11) Row Sequence
  AftLineNum Int(11) After Row Number
  OrderNum Int(11) Order Number
  LineType VarChar(1) Row Type [T=Text, S=Subtotal]
  LineText Text(16) Row Text
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=23 ->ADP1

# QUT11 - Sls Quote - Drawn Dpm Detail
Module: Marketing Documents | 70 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LineSeq
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OQUT
  LineNum Int(11) Row Number
  LineSeq Int(11) Sequence Number
  BaseAbs Int(11) Base Document Internal ID
  BaseType Int(11) Base Object Type default=-1 [-1=]
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  VatPrcnt Num(19,6) VAT Percent
  LineTotal Num(19,6) Net LC
  TotalFrgn Num(19,6) Net FC
  TotalSumSy Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFrgn Num(19,6) Tax FC
  VatSumSys Num(19,6) Tax SC
  ObjType nVarChar(20) Object Type default=23 ->ADP1
  LogInstanc Int(11) Log Instance
  IsAcq VarChar(1) Acquisition Tax-Liable default=N [N=No, Y=Yes]
  IsAllDrawn VarChar(1) Remaining Amount Drawn default=N [Y=Yes, N=No]
  IsGross VarChar(1) Is Gross Line default=N [N=Net Line, Y=Gross Line]
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  ApplNet Num(19,6) Applied Net LC
  ApplNetFc Num(19,6) Applied Net FC
  ApplNetSc Num(19,6) Applied Net SC
  ApplVat Num(19,6) Applied Tax LC
  ApplVatFc Num(19,6) Applied Tax FC
  ApplVatSc Num(19,6) Applied Tax SC
  BaseNet Num(19,6) Base Net LC
  BaseNetFc Num(19,6) Base Net FC
  BaseNetSc Num(19,6) Base Net SC
  BaseVat Num(19,6) Base Tax LC
  BaseVatFc Num(19,6) Base Tax FC
  BaseVatSc Num(19,6) Base Tax SC
  BaseGross Num(19,6) Base Gross LC
  BaseGrossF Num(19,6) Base Gross FC
  BaseGrossS Num(19,6) Base Gross SC
  LineType VarChar(1) Line Type default=D [D=Document Row, R=Currency Rounding, H=Down Payment Document Rounding]
  DctSum Num(19,6) Deductible Sum LC
  DctSumFc Num(19,6) Deductible Sum FC
  DctSumSc Num(19,6) Deductible Sum SC
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplDct Num(19,6) Applied Deductible Sum LC
  ApplDctFc Num(19,6) Applied Deductible Sum FC
  ApplDctSc Num(19,6) Applied Deductible Sum SC
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  BaseDct Num(19,6) Base Deductible Sum LC
  BaseDctFc Num(19,6) Base Deductible Sum FC
  BaseDctSc Num(19,6) Base Deductible Sum SC
  BaseEq Num(19,6) Base Equalization Sum LC
  BaseEqFc Num(19,6) Base Equalization Sum FC
  BaseEqSc Num(19,6) Base Equalization Sum SC
  TaxCode nVarChar(8) Tax Code ->OSTC
  ApplGross Num(19,6) Applied Gross LC
  ApplGrossF Num(19,6) Applied Gross FC
  ApplGrossS Num(19,6) Applied Gross SC
  TaxAdjust VarChar(1) Manual Tax Adjustment default=N [Y=Yes, N=No]
  RvsChrgSum Num(19,6) Reverse Charge Sum LC
  RvsChrgFc Num(19,6) Reverse Charge Sum FC
  RvsChrgSc Num(19,6) Reverse Charge Sum SC
  BasRvsChrg Num(19,6) Base Reverse Charge LC
  BasRvsFc Num(19,6) Base Reverse Charge FC
  BasRvsSc Num(19,6) Base Reverse Charge SC
  ApplRvs Num(19,6) Applied Reverse Charge LC
  ApplRvsFc Num(19,6) Applied Reverse Charge FC
  ApplRvsSc Num(19,6) Applied Reverse Charge SC
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# QUT12 - Sales Quotation - Tax Extension
Module: Marketing Documents | 117 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OQUT
  TaxId0 nVarChar(100) Tax ID 0
  TaxId1 nVarChar(100) Tax ID 1
  TaxId2 nVarChar(100) Tax ID 2
  TaxId3 nVarChar(100) Tax ID 3
  TaxId4 nVarChar(100) Tax ID 4
  TaxId5 nVarChar(100) Tax ID 5
  TaxId6 nVarChar(100) Tax ID 6
  TaxId7 nVarChar(100) Tax ID 7
  TaxId8 nVarChar(100) Tax ID 8
  TaxId9 nVarChar(100) Tax ID 9
  State nVarChar(3) State Code
  County nVarChar(7) County Code
  Incoterms nVarChar(3) Incoterms
  Vehicle nVarChar(10) Vehicle ID
  VidState nVarChar(3) Vehicle ID (State)
  NfRef nVarChar(254) Nota Fiscal Reference
  Carrier nVarChar(15) Carrier Code
  QoP Int(11) Quantity of Packs
  PackDesc nVarChar(10) Pack Description
  Brand nVarChar(20) Brand
  NoSU Int(11) Number of Shipping Unit
  NetWeight Num(19,6) Net Weight
  GrsWeight Num(19,6) Gross Weight
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=23 ->ADP1
  TaxId10 nVarChar(100) Tax ID 10
  TransCat nVarChar(100) Transaction Category
  FormNo nVarChar(100) Form No.
  TaxId11 nVarChar(100) Tax ID 11
  StreetS nVarChar(100) Street
  BlockS nVarChar(100) Block
  BuildingS Text(16) Building/Floor/Room
  CityS nVarChar(100) City
  ZipCodeS nVarChar(20) Zip Code
  CountyS nVarChar(100) County
  StateS nVarChar(3) State ->OCST
  CountryS nVarChar(3) Country/Region ->OCRY
  AddrTypeS nVarChar(100) Address Type
  StreetNoS nVarChar(100) Street No.
  StreetB nVarChar(100) Street
  BlockB nVarChar(100) Block
  BuildingB Text(16) Building/Floor/Room
  CityB nVarChar(100) City
  ZipCodeB nVarChar(20) Zip Code
  CountyB nVarChar(100) County
  StateB nVarChar(3) State ->OCST
  CountryB nVarChar(3) Country/Region ->OCRY
  AddrTypeB nVarChar(100) Address Type
  StreetNoB nVarChar(100) Street No.
  ImpORExp VarChar(1) Import or Export [N=, Y=]
  Vat VarChar(1) VAT default=N [N=No VAT Support, Y=VAT Support]
  AltCrdNamB nVarChar(100) Alternative BP Name
  AltTaxIdB nVarChar(32) Alternative Tax ID
  Address2S nVarChar(50) Address Name 2
  Address3S nVarChar(50) Address Name 3
  Address2B nVarChar(50) Address Name 2
  Address3B nVarChar(50) Address Name 3
  MainUsage Int(11) Main Usage Code of Document ->OUSG
  GlbLocNumS nVarChar(50) Global Location Number
  GlbLocNumB nVarChar(50) Global Location Number
  CollectDT nVarChar(20) Date and Time of Collection
  TransprtDT Date(8) Transport Starting Date
  TransprtRS nVarChar(100) Transport Reason
  TaxId12 nVarChar(50) Tax ID 12
  TaxId13 nVarChar(100) Deductee Ref. No. in India
  ImpExpNo nVarChar(100) Import/Export Bill No.
  ImpExpDate Date(8) Import/Export Date
  BpGSTType Int(11) GST Regn Type of BP
  BpGSTN nVarChar(15) GST Regn No of BP
  BpStateCod nVarChar(3) State Code of Business Partner ->OCST
  BPStatGSTN nVarChar(2) GST State Code of BP
  LocGSTType Int(11) GST Regn Type of Location
  LocGSTN nVarChar(15) GST Regn No of Location
  LocStatCod nVarChar(3) State Code of Location ->OCST
  LocStaGSTN nVarChar(2) GST State Code of Location
  BpCountry nVarChar(3) Country/Region Code of BP ->OCRY
  OrigImpNo nVarChar(100) Original Bill of Entry No.
  OrigImpDat Date(8) Original Bill of Entry Date
  ExportType VarChar(1) Exporting Type default=E [E=Imports/Exports, S=SEZ Developer, U=SEZ Unit, D=Deemed Imports/Exports]
  PortCode nVarChar(100) Port Code
  BoEValue Num(19,6) Bill of Entry Value
  IsIGSTAct VarChar(1) Supply under IGST Account [Y=Yes, N=No]
  ClaimRefun VarChar(1) Claim Refund [Y=Yes, N=No]
  TaxRateDif Int(11) Differential % of Tax Rate [65=, 100=]
  BPGdsIssP nVarChar(15) Goods Issue Place BP
  CNPJGIP nVarChar(100) Goods Issue Place CNPJ
  CPFGIP nVarChar(100) Goods Issue Place CPF
  StreetGIP nVarChar(100) Goods Issue Place Street
  StrtNoGIP nVarChar(100) Goods Issue Place Street No.
  BldngGIP Text(16) Goods Issue Place Building
  ZipGIP nVarChar(20) Goods Issue Place Zip Code
  BlockGIP nVarChar(100) Goods Issue Place Block
  CityGIP nVarChar(100) Goods Issue Place City
  CountyGIP nVarChar(100) Goods Issue Place County
  StateGIP nVarChar(3) Goods Issue Place State ->OCST
  CountryGIP nVarChar(3) Goods Issue Place Country/Region ->OCRY
  PhoneGIP nVarChar(20) Goods Issue Place Phone
  EMailGIP nVarChar(100) Goods Issue Place E-Mail
  DptDateGIP Date(8) Goods Issue Place Departure Date
  BPDelivryP nVarChar(15) Delivery Place BP
  CNPJDlvryP nVarChar(100) Delivery Place CNPJ
  CPFDlvryP nVarChar(100) Delivery Place CPF
  StrtDlvryP nVarChar(100) Delivery Place Street
  StrNoDlvrP nVarChar(100) Delivery Place Street No.
  BldDlvryP Text(16) Delivery Place Building
  ZipDlvryP nVarChar(20) Delivery Place Zip Code
  BlckDlvryP nVarChar(100) Delivery Place Block
  CityDlvryP nVarChar(100) Delivery Place City
  CntyDlvryP nVarChar(100) Delivery Place County
  StatDlvryP nVarChar(3) Delivery Place State ->OCST
  CtryDlvryP nVarChar(3) Delivery Place Country/Region ->OCRY
  FoneDlvryP nVarChar(20) Delivery Place Phone
  MailDlvryP nVarChar(100) Delivery Place E-Mail
  DpDtDlvryP Date(8) Delivery Place Departure Date
  AuthedCNPJ nVarChar(250) Authorized CNPJ or CPF
  TaxId14 nVarChar(250) ITR Filing

# QUT13 - Sales Quotation Rows - Distributed Expenses
Module: Marketing Documents | 59 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OQUT
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=23 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Aquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Normal Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) VAT Applied Frgn
  VatAppldSC Num(19,6) VAT Applied Sys
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock default=N [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Line No.
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Abs. Entry default=-1
  BaseGroup Int(11) Base Document Group default=-1
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1
  VisOrder Int(11) Visual Order
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DistribExp VarChar(1) Distribute Freights [Y=Yes, N=No]
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ

# QUT14 - Sales Quotation - Assembly - Rows
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OQUT
  LineNum Int(11) Row Number default=-1
  ChildNum Int(11) Child Number default=-1
  ItemCode nVarChar(50) Item no. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  TotalQty Num(19,6) Total Quantity
  OpenQty Num(19,6) Remaining Open Quantity
  ObjectType nVarChar(20) object type default=23 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BaseChildN Int(11) Base Child Number default=-1
  EncryptIV nVarChar(100) Encrypt IV

# QUT15 - Sls Quote - Drawn Dpm Applied
Module: Marketing Documents | 84 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OQUT
  LineNum Int(11) Row Number
  ObjType nVarChar(20) object type default=23 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  StaCode nVarChar(8) Tax Authority Code
  StaType Int(11) Tax Authority Type
  StaIndex Int(11) Tax Authority Seq Index
  BaseNet Num(19,6) Net LC
  BaseNetFc Num(19,6) Net FC
  BaseNetSc Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFc Num(19,6) Tax FC
  VatSumSc Num(19,6) Tax SC
  DctSum Num(19,6) Deductible Sum LC
  DctSumFc Num(19,6) Deductible Sum FC
  DctSumSc Num(19,6) Deductible Sum SC
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplNet Num(19,6) Applied Net LC
  ApplNetFc Num(19,6) Applied Net FC
  ApplNetSc Num(19,6) Applied Net SC
  ApplVat Num(19,6) Applied Tax LC
  ApplVatFc Num(19,6) Applied Tax FC
  ApplVatSc Num(19,6) Applied Tax SC
  ApplDct Num(19,6) Applied Deductible Sum LC
  ApplDctFc Num(19,6) Applied Deductible Sum FC
  ApplDctSc Num(19,6) Applied Deductible Sum SC
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  PaidNet Num(19,6) Paid Net LC
  PaidNetFc Num(19,6) Paid Net FC
  PaidNetSc Num(19,6) Paid Net SC
  PaidVat Num(19,6) Paid Tax LC
  PaidVatFc Num(19,6) Paid Tax FC
  PaidVatSc Num(19,6) Paid Tax SC
  PaidDct Num(19,6) Paid Deductible Sum LC
  PaidDctFc Num(19,6) Paid Deductible Sum FC
  PaidDctSc Num(19,6) Paid Deductible Sum SC
  PaidEq Num(19,6) Paid Equalization Sum LC
  PaidEqFc Num(19,6) Paid Equalization Sum FC
  PaidEqSc Num(19,6) Paid Equalization Sum SC
  DpApplNet Num(19,6) Dpm Appl Net LC
  DpApplNetF Num(19,6) Dpm Appl Net FC
  DpApplNetS Num(19,6) Dpm Appl Net SC
  DpApplVat Num(19,6) Dpm Appl Tax LC
  DpApplVatF Num(19,6) Dpm Appl Tax FC
  DpApplVatS Num(19,6) Dpm Appl Tax SC
  DpApplDct Num(19,6) Dpm Appl Deductible Sum LC
  DpApplDctF Num(19,6) Dpm Appl Deductible Sum FC
  DpApplDctS Num(19,6) Dpm Appl Deductible Sum SC
  DpApplEq Num(19,6) Dpm Appl Equalization Sum LC
  DpApplEqFc Num(19,6) Dpm Appl Equalization Sum FC
  DpApplEqSc Num(19,6) Dpm Appl Equalization Sum SC
  TaxCode nVarChar(8) Tax Code ->OSTC
  LineType VarChar(1) Row Type default=D [D=Document, R=Exchange Rate Rounding, H=Document Header Rounding]
  BaseGrs Num(19,6) Gross LC
  BaseGrsFc Num(19,6) Gross FC
  BaseGrsSc Num(19,6) Gross SC
  ApplGrs Num(19,6) Applied Gross LC
  ApplGrsFc Num(19,6) Applied Gross FC
  ApplGrsSc Num(19,6) Applied Gross SC
  PaidGrs Num(19,6) Paid Gross LC
  PaidGrsFc Num(19,6) Paid Gross FC
  PaidGrsSc Num(19,6) Paid Gross SC
  DpApplGrs Num(19,6) Dpm Appl Gross LC
  DpApplGrsF Num(19,6) Dpm Appl Gross FC
  DpApplGrsS Num(19,6) Dpm Appl Gross SC
  RvsChrgSum Num(19,6) Reverse Charge Sum
  RvsChrgSc Num(19,6) Reverse Charge Sum (SC)
  RvsChrgFc Num(19,6) Reverse Charge Sum (FC)
  ApplRvs Num(19,6) Applied Reverse Charge Sum LC
  ApplRvsSc Num(19,6) Applied Reverse Charge Sum SC
  ApplRvsFc Num(19,6) Applied Reverse Charge Sum FC
  PaidRvs Num(19,6) Paid Reverse Charge Sum LC
  PaidRvsSc Num(19,6) Paid Reverse Charge Sum SC
  PaidRvsFc Num(19,6) Paid Reverse Charge Sum FC
  DpApplRvs Num(19,6) Dpm Applied Reverse Charge LC
  DpApplRvsS Num(19,6) Dpm Applied Reverse Charge SC
  DpApplRvsF Num(19,6) Dpm Applied Reverse Charge FC
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# QUT16 - Sales Quotation - SnB properties
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, SnBIndex
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) abs entry ->OQUT
  LineNum Int(11) Line Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object id
  ObjAbs Int(11) Object Abs
  DrfWObjAbs Int(11) draft Wobj Abs default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type default=23
  LogInstanc Int(11) Log Instance

# QUT17 - Sales Quotation - Import Process
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OQUT
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=23 ->ADP1
  ImpDocType VarChar(1) Type of Importation Document ->OBSI
  ImpDocNum nVarChar(10) Importation Document Number
  DateOfReg Date(8) Date of Registry DI/DSI/DA
  CustClrDat Date(8) Date of Customs Clearance
  ConcActNum nVarChar(30) Drawback Concession Acct No.
  AdditNum nVarChar(30) Additional Number
  AddItmDV Num(19,6) Additional Item Discount Value
  tpVTransp Int(6) Overland Transport Route [1=Maritime, 2=Waterway, 3=Lakeside, 4=Air, 5=Post, 6=Train, 7=Road, 8=Network Transmission, 9=Own Means, 10=Input/Output Fictitious, 11=Courier, 12=Hand Carry]
  DrawSReg nVarChar(11) Drawback - Suspension Regime
  AddFrNavyA Num(19,6) Additional Freight to Navy Authority
  TypeOfImp VarChar(1) Type of Import
  nSeqAdic Int(6) Additional Item Sequential Number

# QUT18 - Sales Quotation - Export Process
Module: Marketing Documents | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OQUT
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=23 ->ADP1
  ExpDocType Int(11) Type of Exportation Document default=-1 ->OBNI
  ExpDeclNum Int(11) Exportation Declaration Number
  ExpDeclDat Date(8) Exportation Declaration Date
  ExpNature Int(11) Nature of Exportation default=-1 ->OBNI
  ExpRegNum Int(11) Number of Exportation Registry
  ExpRegDate Date(8) Date of Exportation Registry
  LadBillNum nVarChar(19) Bill of Lading Number
  LadBillDat Date(8) Date of Bill of Lading
  MerchLeftD Date(8) Date Merchandise Left Customs
  LadBillTyp Int(11) Type of Bill of Lading default=-1 ->OBNI
  DrawSReg nVarChar(11) Drawback - Suspension Regime
  NatureExp nVarChar(44) Nature of Export
  QultExpItm Num(19,6) Quantity of Exported Items
  nSeqAdic Int(6) Additional Item Sequential Number

# QUT19 - Sales Quotation - Bin Allocation Data
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, BinAllocSe
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OQUT
  BinAllocSe Int(11) Bin Allocation Sequence
  LineNum Int(11) Line Number
  SubLineNum Int(11) Subline Number default=-1
  SnBType Int(11) SnB Type default=-1
  SnBMDAbs Int(11) SnB Master Data Internal No. default=-1
  BinAbs Int(11) Bin Internal Number ->OBIN
  Quantity Num(19,6) Quantity
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjType nVarChar(20) Object Type default=23 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  BinActTyp Int(6) Bin Action Type [1=Transaction In, 2=Transaction Out, 4=SnB Complete, 8=Bin First Then SnB]

# QUT2 - Sales Quotation - Freight - Rows
Module: Marketing Documents | 64 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OQUT
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=23 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) Vat Applied
  VatAppldFC Num(19,6) Vat Applied Frgn
  VatAppldSC Num(19,6) Vat Applied Sys
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report [Y=Yes, N=No]
  BaseGroup Int(11) Base Document Group default=-1 [-1=, 0=, 1=, 2=]
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1 [-1=, 0=, 1=, 2=]
  VisOrder Int(11) Visual Order
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]

# QUT20 - Intrastat Expenses
Module: Marketing Documents | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OQUT
  ExpnsCode Int(11) Freight Code ->OEXD
  TotalLC Num(19,6) Total
  TotalFC Num(19,6) Total (FC)
  TotalSC Num(19,6) Total (SC)
  DistribM VarChar(1) Distribution Method default=T [Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DrawnLC Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  LineNum Int(11) Line Number default=-1
  BaseAbsEnt Int(11) Base Abs. Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 16=Return, 13=A/R Invoice, 203=Down Payment Incoming, 204=Down Payment Outgoing, 22=Purchase Order, 20=Goods Receipt PO, 21=Goods Return, 18=A/P Invoice, 540000006=Purchase Quotation, 0=, -1=]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No. default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=23 ->ADP1
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  AppliedLC Num(19,6) Applied
  AppliedFC Num(19,6) Applied (FC)
  AppliedSC Num(19,6) Applied (SC)

# QUT21 - Sales Quotation - Document Reference Information
Module: Marketing Documents | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, RefType
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjectType nVarChar(20) Object Type default=23
  LogInstanc Int(11) Log Instance default=0
  RefType VarChar(1) Reference Types default=S [S=System Document, E=External Document]
  LineNum Int(11) Line Number
  RefDocEntr Int(11) Referenced Internal Number
  RefDocNum Int(11) Referenced Document Number
  ExtDocNum nVarChar(100) External Referenced Document Number
  RefObjType nVarChar(20) Referenced Object Type [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 234000031=Return Request, 16=Return, 203=A/R Down Payment, 13=A/R Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 280=A/R Tax Invoice, 1470000113=Purchase Request, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Return Request, 21=Goods Return, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 281=A/P Tax Invoice, 69=Landed Costs, 24=Incoming Payments, 46=Outgoing Payments, 57=Checks for Payment, 321=Internal Reconciliation, 34=Recurring Posting, 30=Journal Entry, 59=Goods Receipt, 60=Goods Issue, 162=Inventory Revaluation, 1470000065=Inventory Counting, 10000071=Inventory Posting, 1250000001=Inventory Transfer Request, 67=Inventory Transfer, 202=Production Order, 13001=Original Invoice, -1=External Document, 20301=Original Down Payment Invoice]
  AccessKey nVarChar(100) Access Key
  IssueDate Date(8) Date of Issue
  IssuerCNPJ nVarChar(100) Issuer CNPJ
  IssuerCode nVarChar(10) Fiscal Document Issuer UF Code
  Model nVarChar(6) Fiscal Document Model
  Series nVarChar(3) Fiscal Document Series
  Number Int(11) Fiscal Document Number
  RefAccKey nVarChar(100) Referenced CT-e Access Key
  RefAmount Num(19,6) Referenced Amount
  SubSeries nVarChar(3) Fiscal Document Subseries
  Remark nVarChar(254) Remarks
  LinkRefTyp nVarChar(20) Link Reference Type default=00 [00=, 01=Nota de cr�dito de los documentos relacionados, 02=Nota de d�bito de los documentos relacionados, 03=Devoluci�n de mercanc�a sobre facturas o traslados previos, 04=Sustituci�n de los CFDI previos, 05=Traslados de mercancias facturados previamente, 06=Factura generada por los traslados previos, 07=CFDI por aplicaci�n de anticipo, 08=Customs, MX_08=Factura generada por pagos en parcialidades, 09=Factura generada por pagos diferidos]

# QUT22 - Sales Quotation - Resource Costs
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, StdCostNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->QUT1
  LineNum Int(11) Row Number ->QUT1
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=23
  LogInstanc Int(11) Log Instance default=0

# QUT23 - A/P Invoice - Selected Asset Master Data
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, VisOrder
  ASSETS: DocEntry, LineNum, AssetCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OQUT
  LineNum Int(11) Row Number
  AssetCode nVarChar(50) Selected Asset Code ->OITM
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Remarks nVarChar(100) Remarks
  Amount Num(19,6) Amount
  AmountSC Num(19,6) Amount (SC)
  SerialNo nVarChar(30) Serial Number
  VisOrder Int(11) Visual Order
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=23 ->ADP1

# QUT24 - Sales Quotation - Tracking Note Assignment
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  ItemCCDNum nVarChar(40) Item CCD Number
  CntrOrigin nVarChar(3) Country/Region of Origin
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=23 ->ADP1
  SubLineNum Int(11) BOM Line No.

# QUT25 - Sales Quotation - Amt Per VAT Grp
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, VatGroup, Type
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  VatGroup nVarChar(8) Tax Definition ->OVTG
  VatPrcnt Num(19,6) Tax Rate
  BaseAmnt Num(19,6) Base Amount
  BaseAmntFC Num(19,6) Base Amount (FC)
  BaseAmntSC Num(19,6) Base Amount (SC)
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  Type Int(11) Type default=1 [1=Discount by Tax]
  Currency nVarChar(3) Price Currency
  Rate Num(19,6) Currency Rate
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=23 ->ADP1

# QUT26 - Sales Quotation - E-Way Bill Information
Module: Marketing Documents | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OQUT
  SuplyType nVarChar(20) EWB Transaction Type [O=Outward, I=Inward]
  SubSplyTyp Int(11) EWB Sub-Type ->OEST
  DocType nVarChar(3) EWB Doc. Type ->OEDT
  TransMode Int(11) EWB Transportation Mode ->OETM
  Distance Num(19,6) EWB Transport Distance
  TransDocNo nVarChar(16) EWB Transporter Doc. No.
  TransDate Date(8) EWB Transportation Date
  VehicleTyp nVarChar(2) EWB Vehicle Type ->OEVT
  VehicleNo nVarChar(15) EWB Vehicle Number
  EWayBillNo nVarChar(20) EWB No.
  EwbDate Date(8) E-Way Bill Date
  FrmTraName nVarChar(100) EWB Consignor Name
  FrmAddres1 nVarChar(120) EWB Consignor Address 1
  FrmAddres2 nVarChar(120) EWB Consignor Address 2
  FrmZipCode nVarChar(20) EWB Consignor Zip Code
  ActFrmStat nVarChar(2) Dispatch State of EWB Consignor
  ToTraName nVarChar(100) EWB Consignee Name
  ToAddres1 nVarChar(120) EWB Consignee Address 1
  ToAddres2 nVarChar(120) EWB Consignee Address 2
  ToZipCode nVarChar(20) EWB Consignee Zip Code
  ActToState nVarChar(2) Ship-To State of EWB Consignee
  FrmGSTN nVarChar(15) EWB Consignor GSTN
  FrmState nVarChar(2) Bill-To State of EWB Consignor
  ToGSTN nVarChar(15) EWB Consignee GSTN
  ToState nVarChar(2) Bill-To State of EWB Consignee
  MainHsnEnt Int(11) EWB Main HSN Entry ->OCHP
  FrmPlace nVarChar(50) EWB Consignor Place
  ToPlace nVarChar(50) EWB Consignee Place
  TransID nVarChar(15) EWB Transporter ID
  TransName nVarChar(25) EWB Transporter Name
  ExpireDate Date(8) EWB Expiration Date
  ObjectType nVarChar(20) Object Type default=23 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TspEntry Int(11) Transporter Abs. Entry ->OTSP
  TspLine Int(11) Transportation Line
  TransType Int(11) Transaction Type [1=Regular, 2=Bill To-Ship To, 3=Bill From-Dispatch From, 4=Combination of 2 and 3]

# QUT27 - Sales Quotation - E-Books(GR) Rows
Module: Marketing Documents | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  RELATE_ROW: DocEntry, RelateType, RelateLine, GroupNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OQUT
  LineNum Int(11) Row Number
  RelateType Int(11) Relation Type default=-1 [1=Row, 2=Row Expenses, 3=Document Expenses, 13=Distributed Freights, -1=Manual]
  RelateLine Int(11) Relation Row Number default=-1
  GroupNum Int(11) Group Number default=-1
  LineTotal Num(19,6) Line Total
  LineTotalF Num(19,6) Line Total (FC)
  LineTotalS Num(19,6) Line Total (SC)
  InClassTyp Int(11) Income Classification Type ->OICP
  InClassCat Int(11) Income Classification Category ->OICC
  ExClassTyp Int(11) Expense Classification Type ->OECP
  ExClassCat Int(11) Expense Classification Cat. ->OECC
  VatCate Int(11) VAT Category
  NetValue Num(19,6) Net Value
  NetValueFC Num(19,6) Net Value (FC)
  NetValueSC Num(19,6) Net Value (SC)
  VatAmount Num(19,6) VAT Amount
  VatAmFC Num(19,6) VAT Amount (FC)
  VatAmSC Num(19,6) VAT Amount (SC)
  WtPercCat Int(11) Withheld Percentage Category
  WtAmount Num(19,6) Withheld Amount
  WtAmountFC Num(19,6) Withheld Amount (FC)
  WtAmountSC Num(19,6) Withheld Amount (SC)
  ObjectType nVarChar(20) Object Type default=13 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  WtCategory VarChar(1) Withheld Category [I=Invoice, P=Payment]
  VATClassTy Int(11) VAT Classification Type ->OECP
  VATClassCa Int(11) VAT Classification Category ->OECC
  EBVatExCau Int(11) VAT Exemption Cause ->OVEC

# QUT28 - Sales Quotation - Reported Tracking Note
Module: Marketing Documents | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
  TCN_KEY U: DocEntry, LineNum, TrackingNt, TrackiNtLn
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  UnusedQty Num(19,6) Unused Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=23 ->ADP1
  SubLineNum Int(11) BOM Line No.

# QUT3 - Sales Quotation - Freight
Module: Marketing Documents | 80 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  DOCUMENT: DocEntry, BaseAbsEnt
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OQUT
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  Comments nVarChar(100) Remarks
  ObjType nVarChar(20) Object Type default=23 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  WTLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  VatApplied Num(19,6) Vat Applied
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatF Num(19,6) Net Tax Amount (FC)
  LineVatS Num(19,6) Net Tax Amount (SC)
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No.
  LineNum Int(11) line num default=-1
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Doc. Internal No. default=-1
  StDstr Num(19,6) Stock Distributed Sum
  StDstrSC Num(19,6) Stock Distributed Sum (SC)
  StDstrFC Num(19,6) Stock Distributed Sum (FC)
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  TaxDistMtd VarChar(1) Tax Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  GrsAmount Num(19,6) Gross Amount
  GrsFC Num(19,6) Gross Amount (FC)
  GrsSC Num(19,6) Gross Amount (SC)
  BaseTotal VarChar(1) Base Total for Calculation default=N [N=Net Total, G=Gross Total]
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)
  RRVatLC Num(19,6) Return Request VAT Amount
  RRVatFC Num(19,6) Return Request VAT Amount (FC)
  RRVatSC Num(19,6) Return Request VAT Amount (SC)
  EncryptIV nVarChar(100) Encrypt IV
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]

# QUT4 - Sales Quotation - Tax Amount per Document
Module: Marketing Documents | 61 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SCONDARY: DocEntry, LineNum, GroupNum, ExpnsCode, StcCode, StaCode, staType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OQUT
  LineNum Int(11) Row Number default=-1
  GroupNum Int(11) Group Number default=-1
  ExpnsCode Int(11) Expense Code default=-1 ->OEXD
  RelateType Int(11) Relation Type default=1 [1=Row, 2=Row Freight Charges, 3=Document Expenses, 13=Distributed Freights]
  StcCode nVarChar(8) Tax Code ->OSTC
  StaCode nVarChar(8) Authority Code ->OSTA
  staType Int(11) Authority Type ->OSTT
  TaxRate Num(19,6) Tax Rate
  TaxAcct nVarChar(15) Tax Account ->OACT
  TaxSum Num(19,6) Tax Amount
  TaxSumFrgn Num(19,6) Tax Amount (FC)
  TaxSumSys Num(19,6) Tax Amount (SC)
  BaseSum Num(19,6) Base Amount
  BaseSumFrg Num(19,6) Base Amount (FC)
  BaseSumSys Num(19,6) Base Amount (SC)
  ObjectType nVarChar(20) Object Type default=23 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Status default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  LineSeq Int(11) Line Sequence
  DeferrAcct nVarChar(15) Deferred Tax Account ->OACT
  BaseType Int(11) Base Document Type default=-1
  BaseAbs Int(11) Base Doc Abs Entry default=-1
  BaseSeq Int(11) Base Doc. Line Sequence
  DeductTax Num(19,6) Deductible Tax Amount
  DdctTaxFrg Num(19,6) Deductible Tax Amount (FC)
  DdctTaxSys Num(19,6) Deductible Tax Amount (SC)
  BaseAppld Num(19,6) Applied Base Amount
  BaseApldFC Num(19,6) Applied Base Amount (FC)
  BaseApldSC Num(19,6) Applied Base Amount (SC)
  NonDdctPrc Num(19,6) Non Deductible %
  NonDdctAct nVarChar(15) Non Deductible Account ->OACT
  TaxInPrice VarChar(1) Tax Included in Price? default=N [Y=Yes, N=No]
  Exempt VarChar(1) Exempt? default=N [Y=Yes, N=No]
  TaxExpAct nVarChar(15) Expense Account for Tax ->OACT
  OnHoldTax Num(19,6) On Hold Tax Amount
  OnHoldTaxF Num(19,6) On Hold Tax Amount (FC)
  OnHoldTaxS Num(19,6) On Hold Tax Amount (SC)
  InGrossRev VarChar(1) Included in Gross Revenue default=N [Y=Yes, N=No]
  TaxSumOrg Num(19,6) Tax Amount Original
  TaxSumOrgF Num(19,6) Tax Amount Original (FC)
  TaxSumOrgS Num(19,6) Tax Amount Original (SC)
  OpenTax Num(19,6) Open Service Tax
  OpenTaxFC Num(19,6) Open Service Tax (FC)
  OpenTaxSC Num(19,6) Open Service Tax (SC)
  Unencumbrd VarChar(1) Unencumbered default=N [Y=Yes, N=No]
  TaxOnRI VarChar(1) Tax On Reserve Invoice default=N [Y=Yes, N=No]
  RvsChrgPrc Num(19,6) Reverse Charge %
  RvsChrgTax Num(19,6) Reverse Charge Tax Amount
  RvsChrgSC Num(19,6) Reverse Charge Tax Amount (SC)
  RvsChrgFC Num(19,6) Reverse Charge Tax Amount (FC)
  InFirstIns VarChar(1) Included in First Installment default=N [Y=Yes, N=No]
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CESTrel VarChar(1) CEST Relevant default=N [Y=, N=]

# QUT5 - Sales Quotation - Tax
Module: Marketing Documents | 158 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  SECONDERY U: AbsEntry, WTCode, BaseAbsEnt, Doc1LineNo
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator ->OQUT
  WTCode nVarChar(4) WT Code ->OWHT
  Rate Num(19,6) Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntSC Num(19,6) Taxable Amount in SC
  TxblAmntFC Num(19,6) Taxable Amount in FC
  WTAmnt Num(19,6) WT Amount
  WTAmntSC Num(19,6) WT Amount (SC)
  WTAmntFC Num(19,6) WT Amount (FC)
  ApplAmnt Num(19,6) Applied WT Amount
  ApplAmntSC Num(19,6) Applied WTax Amount (SC)
  ApplAmntFC Num(19,6) Applied WTax Amount (FC)
  Category VarChar(1) Category [P=Payment, I=Invoice]
  Criteria VarChar(1) Criteria [Y=Accrual, N=Cash]
  Account nVarChar(15) G/L Account ->OACT
  Type VarChar(1) Withholding Type [V=VAT Withholding, I=Income Tax Withholding]
  RoundType VarChar(1) Rounding Type [T=Truncated, C=Commercial Values, N=No Rounding]
  BaseType VarChar(1) Base Type [G=Gross, N=Net, V=VAT, U=UoM]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseLine Int(11) Base Line
  BaseNum Int(11) Base Document Type default=-1 [-1=, 0=]
  LineNum Int(11) Line Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Abs. Entry default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=23 ->ADP1
  Doc1LineNo Int(11) DOC1 Line Number default=-1
  WtLineType VarChar(1) WT Line Type default=D [D=Document Level WTax, L=Row Level WTax]
  TxblCurr nVarChar(3) Taxable Currency from Doc Line
  DtblCurr nVarChar(3) Deductible Currency
  DtblRate Num(19,6) Rate for Deductible Amount
  txblRate Num(19,6) Rate for Taxable Amount
  DtblAmount Num(19,6) Deductible Amount
  TdsAcc nVarChar(15) TDS Account ->OACT
  SurAcc nVarChar(15) Surcharge Account ->OACT
  CessAcc nVarChar(15) Cess Account ->OACT
  HscAcc nVarChar(15) HSC Account ->OACT
  TdsRate Num(19,6) TDS Rate
  SurRate Num(19,6) Surcharge Rate
  CessRate Num(19,6) Cess Rate
  HscRate Num(19,6) HSC Rate
  TdsBAmt Num(19,6) TDS Base Amount
  TdsBAmtSC Num(19,6) TDS Base Amount (SC)
  TdsBAmtFC Num(19,6) TDS Base Amount (FC)
  SurBAmt Num(19,6) Surcharge Base Amount
  SurBAmtSC Num(19,6) Surcharge Base Amount (SC)
  SurBAmtFC Num(19,6) Surcharge Base Amount (FC)
  CessBAmt Num(19,6) Cess Base Amount
  CessBAmtSC Num(19,6) Cess Base Amount (SC)
  CessBAmtFC Num(19,6) Cess Base Amount (FC)
  HscBAmt Num(19,6) HSC Base Amount
  HscBAmtSC Num(19,6) HSC Base Amount (SC)
  HscBAmtFC Num(19,6) HSC Base Amount (FC)
  TdsAmnt Num(19,6) TDS Tax Amount
  TdsAmntSC Num(19,6) TDS Tax Amount (SC)
  TdsAmntFC Num(19,6) TDS Tax Amount (FC)
  SurAmnt Num(19,6) Surcharge Tax Amount
  SurAmntSC Num(19,6) Surcharge Tax Amount (SC)
  SurAmntFC Num(19,6) Surcharge Tax Amount (FC)
  CessAmnt Num(19,6) Cess Tax Amount
  CessAmntSC Num(19,6) Cess Tax Amount (SC)
  CessAmntFC Num(19,6) Cess Tax Amount (FC)
  HscAmnt Num(19,6) HSC Tax Amount
  HscAmntSC Num(19,6) HSC Tax Amount (SC)
  HscAmntFC Num(19,6) HSC Tax Amount (FC)
  TdsAppl Num(19,6) Applied TDS Amount
  TdsApplSC Num(19,6) Applied TDS Amount (SC)
  TdsApplFC Num(19,6) Applied TDS Amount (FC)
  SurAppl Num(19,6) Applied Surcharge Amount
  SurApplSC Num(19,6) Applied Surcharge Amount (SC)
  SurApplFC Num(19,6) Applied Surcharge Amount (FC)
  CessAppl Num(19,6) Applied Cess Amount
  CessApplSC Num(19,6) Applied Cess Amount (SC)
  CessApplFC Num(19,6) Applied Cess Amount (FC)
  HscAppl Num(19,6) Applied HSC Amount
  HscApplSC Num(19,6) Applied HSC Amount (SC)
  HscApplFC Num(19,6) Applied HSC Amount (FC)
  BatchNum Int(11) Journal Voucher No.
  InCSTCode nVarChar(2) CST Code Incoming
  OutCSTCode nVarChar(2) CST Code Outgoing
  DpmWTApl Num(19,6) DPM WT Applied Amount
  DpmWTAplSC Num(19,6) DPM WT Applied Amount (SC)
  DpmWTAplFC Num(19,6) DPM WT Applied Amount (FC)
  WTTypeId Int(11) WT Type Id ->OWTT
  LnBsAmt Num(19,6) BR Line WT Base Amount
  LnBsAmtSC Num(19,6) BR Line WT Base Amount(SC)
  LnBsAmtFC Num(19,6) BR Line WT Base Amount(FC)
  LnCmTAmt Num(19,6) BR Line Cumulated Taxable Amount
  LnCmTAmtSC Num(19,6) BR Line Cumulated Taxable Amount(SC)
  LnCmTAmtFC Num(19,6) BR Line Cumulated Taxable Amount(FC)
  TDSType VarChar(1) TDS Type [E=eTDS, D=GST TDS, C=GST TCS, S=SALES TCS]
  IgstAcc nVarChar(15) IGST Account ->OACT
  CgstAcc nVarChar(15) CGST Account ->OACT
  SgstAcc nVarChar(15) SGST Account ->OACT
  IgstAmnt Num(19,6) IGST Tax Amount
  IgstAmntSC Num(19,6) IGST Tax Amount (SC)
  IgstAmntFC Num(19,6) IGST Tax Amount (FC)
  CgstAmnt Num(19,6) CGST Tax Amount
  CgstAmntSC Num(19,6) CGST Tax Amount (SC)
  CgstAmntFC Num(19,6) CGST Tax Amount (FC)
  SgstAmnt Num(19,6) SGST Tax Amount
  SgstAmntSC Num(19,6) SGST Tax Amount (SC)
  SgstAmntFC Num(19,6) SGST Tax Amount (FC)
  IgstRate Num(19,6) IGST Rate
  CgstRate Num(19,6) CGST Rate
  SgstRate Num(19,6) SGST Rate
  IgstBAmt Num(19,6) IGST Base Amount
  IgstBAmtSC Num(19,6) IGST Base Amount (SC)
  IgstBAmtFC Num(19,6) IGST Base Amount (FC)
  CgstBAmt Num(19,6) CGST Base Amount
  CgstBAmtSC Num(19,6) CGST Base Amount (SC)
  CgstBAmtFC Num(19,6) CGST Base Amount (FC)
  SgstBAmt Num(19,6) SGST Base Amount
  SgstBAmtSC Num(19,6) SGST Base Amount (SC)
  SgstBAmtFC Num(19,6) SGST Base Amount (FC)
  IgstAppl Num(19,6) Applied IGST Amount
  IgstApplSC Num(19,6) Applied IGST Amount (SC)
  IgstApplFC Num(19,6) Applied IGST Amount (FC)
  CgstAppl Num(19,6) Applied CGST Amount
  CgstApplSC Num(19,6) Applied CGST Amount (SC)
  CgstApplFC Num(19,6) Applied CGST Amount (FC)
  SgstAppl Num(19,6) Applied SGST Amount
  SgstApplSC Num(19,6) Applied SGST Amount (SC)
  SgstApplFC Num(19,6) Applied SGST Amount (FC)
  UtgstAcc nVarChar(15) UTGST Account ->OACT
  CsgstAcc nVarChar(15) Cess GST Account ->OACT
  UtgstAmt Num(19,6) UTGST Tax Amount
  UtgstAmtSC Num(19,6) UTGST Tax Amount (SC)
  UtgstAmtFC Num(19,6) UTGST Tax Amount (FC)
  CsgstAmt Num(19,6) Cess GST Tax Amount
  CsgstAmtSC Num(19,6) Cess GST Tax Amount (SC)
  CsgstAmtFC Num(19,6) Cess GST Tax Amount (FC)
  UtgstRate Num(19,6) UTGST Rate
  CsgstRate Num(19,6) Cess GST Rate
  UtgstBAmt Num(19,6) UTGST Base Amount
  UtgstBAmtS Num(19,6) UTGST Base Amount (SC)
  UtgstBAmtF Num(19,6) UTGST Base Amount (FC)
  CsgstBAmt Num(19,6) Cess GST Base Amount
  CsgstBAmtS Num(19,6) Cess GST Base Amount (SC)
  CsgstBAmtF Num(19,6) Cess GST Base Amount (FC)
  UtgstAppl Num(19,6) Applied UTGST Amount
  UtgstApplS Num(19,6) Applied UTGST Amount (SC)
  UtgstApplF Num(19,6) Applied UTGST Amount (FC)
  CsgstAppl Num(19,6) Applied Cess GST Amount
  CsgstApplS Num(19,6) Applied Cess GST Amount (SC)
  CsgstApplF Num(19,6) Applied Cess GST Amount (FC)
  EncryptIV nVarChar(100) Encrypt IV
  TcsIntAcct nVarChar(15) TCS Interim Account ->OACT
  SurIntAcct nVarChar(15) Surcharge Interim Account ->OACT
  CesIntAcct nVarChar(15) Cess Interim Account ->OACT
  HscIntAcct nVarChar(15) HSC interim Account ->OACT
  LnIntAcct nVarChar(15) Interim Account for Tax ->OACT
  FixedAmnt Num(19,6) Fixed Amount
  FixedAmtSC Num(19,6) Fixed Amount (SC)
  FixedAmtFC Num(19,6) Fixed Amount (FC)
  BaseQty Num(19,6) Base Quantity

# QUT6 - Sales Quotation - Installments
Module: Marketing Documents | 65 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, InstlmntID
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OQUT
  InstlmntID Int(6) Installment ID default=1
  ObjType nVarChar(20) Object Type default=23 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DueDate Date(8) Due Date
  Status VarChar(1) Installment Status default=O [O=Open, C=Closed]
  DunnLevel Int(11) Dunning Level default=0
  InsTotal Num(19,6) Total Installment
  InsTotalFC Num(19,6) Total Installment (FC)
  InsTotalSy Num(19,6) Total Installment (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  VatSum Num(19,6) Total Tax
  VatSumFC Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  VatPaid Num(19,6) Tax Paid to Date
  VatPaidFC Num(19,6) Tax Paid (FC)
  VatPaidSys Num(19,6) Tax Paid (SC)
  TotalExpns Num(19,6) Total Freight Charges
  TotalExpFC Num(19,6) Total Freight Charges (FC)
  TotalExpSC Num(19,6) Total Freight Charges (SC)
  ExpAppl Num(19,6) Applied Freight Charges
  ExpApplFC Num(19,6) Applied Freight Charges (SC)
  ExpApplSC Num(19,6) Applied Freight Charges (SC)
  WTSum Num(19,6) WTax Amount
  WTSumFC Num(19,6) WTax Amount (FC)
  WTSumSC Num(19,6) WTax Amount (SC)
  WTApplied Num(19,6) Applied WTax
  WTAppliedF Num(19,6) Applied WTax (FC)
  WTAppliedS Num(19,6) Applied WTax (SC)
  TotalBlck Num(19,6) Total Reserved Amount
  TotalBlckF Num(19,6) Total Reserved Amount (FC)
  TotalBlckS Num(19,6) Total Reserved Amount (SC)
  VATBlck Num(19,6) Reserved Tax
  VATBlckFC Num(19,6) Reserved Tax (FC)
  VATBlckSC Num(19,6) Reserved Tax (SC)
  ExpnsBlck Num(19,6) Reserved Freight Charges
  ExpnsBlckF Num(19,6) Reserved Freight Amount (FC)
  ExpnsBlckS Num(19,6) Reserved Freight Charges (SC)
  WTBlocked Num(19,6) Reserved WTax Amount
  WTBlockedF Num(19,6) Reserved WTax Amount (FC)
  WTBlockedS Num(19,6) Reserved WTax Amount (SC)
  InstPrcnt Num(19,6) Installment %
  DunWizBlck VarChar(1) Wizard dunning block default=N [N=No, Y=Yes]
  DunDate Date(8) Last Dunning Date
  Paid Num(19,6) Paid
  PaidFrgn Num(19,6) Paid (FC)
  PaidSc Num(19,6) Paid (SC)
  reserved VarChar(1) Reserved default=N [N=No, Y=Yes]
  TaxOnExp Num(19,6) Tax on Expenses
  TaxOnExpFc Num(19,6) Tax on Expenses (FC)
  TaxOnExpSc Num(19,6) Tax on Expenses (SC)
  TaxOnExpAp Num(19,6) Applied Tax on Expenses
  TaxOnExApF Num(19,6) Applied Tax on Expenses (FC)
  TaxOnExApS Num(19,6) Applied Tax on Expenses (SC)
  TaxOnExBlo Num(19,6) Reserved Tax on Freight Amount
  TaxOnExBlF Num(19,6) Reserved Tax on Freight Amt FC
  TaxOnExBlS Num(19,6) Reserved Tax on Freight Amt SC
  LvlUpdDate Date(8) Dunning Level Update Date
  Ordered VarChar(1) Payment Ordered default=N [Y=Yes, N=No]
  PaidDpm Num(19,6) Paid by Down Payment
  PaidDpmFc Num(19,6) Paid by Down Payment (FC)
  PaidDpmSc Num(19,6) Paid by Down Payment (SC)
  EncryptIV nVarChar(100) Encrypt IV

# QUT7 - Delivery Packages - Sales Quotation
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OQUT
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type default=23 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV

# QUT8 - Sales Quotation - Items in Package
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum, ItemCode, UomEntry, NumPerMsr
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OQUT
  PackageNum Int(11) Package Number
  ItemCode nVarChar(50) Item Code ->OITM
  Quantity Num(19,6) Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=23 ->ADP1
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value default=0

# QUT9 - Sales Quotation - Drawn Dpm
Module: Marketing Documents | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OQUT
  LineNum Int(11) Row Number
  BaseAbs Int(11) Base Document Internal ID
  BaseLine Int(11) Base Document Row
  TargetBase VarChar(1) Target or Base Document default=B [B=Base, T=Target]
  ObjType nVarChar(20) Base Object Type
  DrawnSum Num(19,6) Net LC
  DrawnSumFc Num(19,6) Net FC
  DrawnSumSc Num(19,6) Net SC
  LogInstanc Int(11) Log Instance default=0
  ObjCode nVarChar(20) Object Type default=23 ->ADP1
  ApplDrawn Num(19,6) Applied Net LC
  ApplDrawnF Num(19,6) Applied Net FC
  ApplDrawnS Num(19,6) Applied Net SC
  BaseDocNum Int(11) Base Document Number
  BsDocDate Date(8) Base Posting Date
  BsDueDate Date(8) Base Due Date
  BsCardName nVarChar(100) Base BP Name
  BsComments nVarChar(254) Base Remarks
  Posted VarChar(1) Base Document Posted default=Y [Y=Yes, N=No]
  Vat Num(19,6) Tax LC
  VatFc Num(19,6) Tax FC
  VatSc Num(19,6) Tax SC
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  IsGross VarChar(1) Is Gross Line default=N [N=Net Line, Y=Gross Line]

# RDN1 - Returns - Rows
Module: Marketing Documents | 317 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  STATUS: LineStatus
  CURRENCY: Currency
  ACCOUNT: AcctCode
  BASE_ENTRY: BaseEntry, BaseType, BaseLine
  VIS_ORDER: DocEntry, VisOrder
  OWNER_CODE: OwnerCode
  ITM_WHS_OQ: ItemCode, WhsCode, OpenQty
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDN
  LineNum Int(11) Row Number
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=, 14=A/R Credit Memo, 15=Delivery]
  TrgetEntry Int(11) Target Document Internal ID
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 15=A/R Delivery Note, 16=A/R Returns, 234000031=A/R Return Request]
  BaseEntry Int(11) Base Document Internal ID
  BaseLine Int(11) Base Row
  LineStatus VarChar(1) Row Status default=O [O=Open, C=Closed]
  ItemCode nVarChar(50) Item No. ->OITM
  Dscription nVarChar(200) Item/Service Description
  Quantity Num(19,6) Quantity
  ShipDate Date(8) Row Delivery Date
  OpenQty Num(19,6) Remaining Open Quantity
  Price Num(19,6) Price
  Currency nVarChar(3) Price Currency ->OCRN
  Rate Num(19,6) Currency Rate
  DiscPrcnt Num(19,6) Discount % per Row
  LineTotal Num(19,6) Row Total
  TotalFrgn Num(19,6) Row Total in FC
  OpenSum Num(19,6) Open Amount
  OpenSumFC Num(19,6) Open Amount in FC
  VendorNum nVarChar(50) Vendor Catalog No.
  SerialNum nVarChar(17) Serial Number
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  SlpCode Int(11) Sales Employee Code default=-1 ->OSLP
  Commission Num(19,6) Commission Percentage
  TreeType VarChar(1) BOM Type default=N [N=Not a BOM, A=Assembly, S=Sales, I=Sales BOM Component, P=Production, T=Template]
  AcctCode nVarChar(15) Account Code ->OACT
  TaxStatus VarChar(1) Tax Definition [Y=Yes, N=No]
  GrossBuyPr Num(19,6) Gross Profit Base Price
  PriceBefDi Num(19,6) Price Before Discount
  DocDate Date(8) Posting Date
  Flags Int(11) Flags default=0
  OpenCreQty Num(19,6) Credit Memo Amount
  UseBaseUn VarChar(1) Inventory UoM default=N [Y=Yes, N=No]
  SubCatNum nVarChar(50) BP Catalog No. ->OSCN
  BaseCard nVarChar(15) Base BP Code ->OCRD
  TotalSumSy Num(19,6) Row Total in SC
  OpenSumSys Num(19,6) Open Amount in SC
  InvntSttus VarChar(1) Whse Status default=O [O=Open, C=Closed]
  OcrCode nVarChar(8) Costing Code ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  CodeBars nVarChar(254) EAN Code
  VatPrcnt Num(19,6) Tax Percentage per Row
  VatGroup nVarChar(8) Tax Definition ->OVTG
  PriceAfVAT Num(19,6) Gross Price after Discount
  Height1 Num(19,6) Height 1
  Hght1Unit Int(6) Unit of Height 1
  Height2 Num(19,6) Height 2
  Hght2Unit Int(6) Unit of Height 2
  Width1 Num(19,6) Width 1
  Wdth1Unit Int(6) Unit of Width 1
  Width2 Num(19,6) Width 2
  Wdth2Unit Int(6) Unit of Width 2
  Length1 Num(19,6) Length 1
  Len1Unit Int(6) Unit of Length 1
  length2 Num(19,6) Length 2
  Len2Unit Int(6) Unit of Length 2
  Volume Num(19,6) Quantity
  VolUnit Int(6) Vol. Unit
  Weight1 Num(19,6) Weight 1
  Wght1Unit Int(6) Unit of Weight 1
  Weight2 Num(19,6) Weight 2
  Wght2Unit Int(6) Unit of Weight 2
  Factor1 Num(19,6) Factor 1
  Factor2 Num(19,6) Factor 2
  Factor3 Num(19,6) Factor 3
  Factor4 Num(19,6) Factor 4
  PackQty Num(19,6) Packing Quantity
  UpdInvntry VarChar(1) Whse Update default=Y [Y=Yes, N=No]
  BaseDocNum Int(11) Base Document No.
  BaseAtCard nVarChar(100) Customer/Vendor Base Document
  SWW nVarChar(16) Additional Identifier
  VatSum Num(19,6) Tax Total
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  FinncPriod Int(11) Posting Period ->OFPR
  ObjType nVarChar(20) Object Type default=16 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BlockNum nVarChar(100) Block Number
  ImportLog nVarChar(20) Import Log
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAqcuistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  DistribSum Num(19,6) Distributed Amount
  DstrbSumFC Num(19,6) Distributed Amount (FC)
  DstrbSumSC Num(19,6) Distributed Amount (SC)
  GrssProfit Num(19,6) Row Gross Profit
  GrssProfSC Num(19,6) Row Gross Profit (SC)
  GrssProfFC Num(19,6) Row Gross Profit (FC)
  VisOrder Int(11) Visual Order
  INMPrice Num(19,6) Item's Last Sales Price (OINM)
  PoTrgNum Int(11) PO Target No.
  PoTrgEntry nVarChar(11) PO Target Internal ID
  DropShip VarChar(1) Drop-Ship default=N [Y=Yes, N=No]
  PoLineNum Int(11) PO Target Row No.
  Address nVarChar(254) Address
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type [Y=Regular Tax, N=No Tax, U=Use Tax]
  OrigItem nVarChar(50) Original Item ->OITM
  BackOrdr VarChar(1) Allow Back Order [Y=Yes, N=No]
  FreeTxt nVarChar(100) Free Text
  PickStatus VarChar(1) Pick Status default=N [Y=Picked, N=Not Picked, R=Released for Picking, P=Partially Picked]
  PickOty Num(19,6) Pick Quantity
  PickIdNo Int(11) Pick ID
  TrnsCode Int(6) Shipping Method default=-1 ->OSHP
  VatAppld Num(19,6) Applied Tax
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  BaseQty Num(19,6) Base Quantity
  BaseOpnQty Num(19,6) Base Open Quantity
  VatDscntPr Num(19,6) Tax Discount %
  WtLiable VarChar(1) Withholding Tax Liable [Y=Yes, N=No]
  DeferrTax VarChar(1) Deferred Tax default=N [Y=Yes, N=No]
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatlF Num(19,6) Net Tax Amount
  LineVatS Num(19,6) Net Tax Amount
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value
  CEECFlag VarChar(1) Correction Invoice Item W/S default=S [W=Was, S=Should Be]
  ToStock Num(19,6) Corr. Invoice Amount to Stock
  ToDiff Num(19,6) Corr. Invoice Amount to Diff.
  ExciseAmt Num(19,6) Excise Amount
  TaxPerUnit Num(19,6) Tax per Unit
  TotInclTax Num(19,6) Total (incl. Tax)
  CountryOrg nVarChar(3) Country/Region of Origin
  StckDstSum Num(19,6) Stock Distribute Sum
  ReleasQtty Num(19,6) Released Quantity
  LineType VarChar(1) Line Type default=R [R=Regular]
  TranType VarChar(1) Transaction Type [C=Complete, R=Reject]
  Text Text(16) Text
  OwnerCode Int(11) Document Owner
  StockPrice Num(19,6) Cost Price
  ConsumeFCT VarChar(1) Consumer Sales Forecast [Y=Yes, N=No]
  LstByDsSum Num(19,6) Last Buy Distribute Sum
  StckINMPr Num(19,6) Stock Inm Price
  LstBINMPr Num(19,6) Last Buy Inm Price
  StckDstFc Num(19,6) Stock Distribute Sum Foreign
  StckDstSc Num(19,6) Stock Distribute Sum System
  LstByDsFc Num(19,6) Last Buy Distribute Sum FC
  LstByDsSc Num(19,6) Last Buy Distribute Sum SC
  StockSum Num(19,6) Stock Sum
  StockSumFc Num(19,6) Stock Sum FC
  StockSumSc Num(19,6) Stock Sum SC
  StckSumApp Num(19,6) Stock Sum Applied
  StckAppFc Num(19,6) Stock Sum Applied FC
  StckAppSc Num(19,6) Stock Sum Applied SC
  ShipToCode nVarChar(50) Ship-to Code
  ShipToDesc nVarChar(254) Ship-to Description
  StckAppD Num(19,6) Stock Distribution Applied Sum
  StckAppDFC Num(19,6) Stock Distrib. Applied Sum FC
  StckAppDSC Num(19,6) Stock Distrib. Applied Sum SC
  BasePrice VarChar(1) Price for Total Calculation default=E [E=Exclude Tax, I=Include Tax]
  GTotal Num(19,6) Gross Total
  GTotalFC Num(19,6) Gross Total FC
  GTotalSC Num(19,6) Gross Total SC
  DistribExp VarChar(1) Distribute Expense [Y=Yes, N=No]
  DescOW VarChar(1) DESC_OVERWRITTEN default=N [Y=Yes, N=No]
  DetailsOW VarChar(1) DETAILS_OVERWRITTEN default=N [Y=Yes, N=No]
  GrossBase Int(6) Base Method for Gross Profit
  VatWoDpm Num(19,6) Tax Before DPM Applied
  VatWoDpmFc Num(19,6) Tax Before DPM Applied FC
  VatWoDpmSc Num(19,6) Tax Before DPM Applied SC
  CFOPCode nVarChar(6) CFOP Code for Document ->OCFP
  CSTCode nVarChar(6) CST Code for ICMS
  Usage Int(11) Usage Code for Document ->OUSG
  TaxOnly VarChar(1) Tax Only [Y=Yes, N=No]
  WtCalced VarChar(1) WTax Calculated default=N [N=No, Y=Yes]
  QtyToShip Num(19,6) Quantity to Ship
  DelivrdQty Num(19,6) Delivered Quantity
  OrderedQty Num(19,6) Ordered Quantity
  CogsOcrCod nVarChar(8) COGS Distribution Rule Code ->OOCR
  CiOppLineN Int(11) Line Number of Opposite Line default=-1
  CogsAcct nVarChar(15) COGS Account Code ->OACT
  ChgAsmBoMW VarChar(1) Change Whs for Asm BoM Child [Y=Yes, N=No]
  ActDelDate Date(8) Actual Delivery Date
  OcrCode2 nVarChar(8) Costing Code 2 ->OOCR
  OcrCode3 nVarChar(8) Costing Code 3 ->OOCR
  OcrCode4 nVarChar(8) Costing Code 4 ->OOCR
  OcrCode5 nVarChar(8) Costing Code 5 ->OOCR
  TaxDistSum Num(19,6) Tax Distributed Amount
  TaxDistSFC Num(19,6) Tax Distributed Amount (FC)
  TaxDistSSC Num(19,6) Tax Distributed Amount (SC)
  PostTax VarChar(1) Post Tax in Price to Stock default=Y [Y=Yes, N=No]
  Excisable VarChar(1) Excisable [Yes/No] [Y=Yes, N=No]
  AssblValue Num(19,6) Assessable Value
  RG23APart1 Int(11) RG23A Part1 Number
  RG23APart2 Int(11) RG23A Part2 Number
  RG23CPart1 Int(11) RG23C Part1 Number
  RG23CPart2 Int(11) RG23C Part2 Number
  CogsOcrCo2 nVarChar(8) COGS Distribution Rule Code2 ->OOCR
  CogsOcrCo3 nVarChar(8) COGS Distribution Rule Code3 ->OOCR
  CogsOcrCo4 nVarChar(8) COGS Distribution Rule Code4 ->OOCR
  CogsOcrCo5 nVarChar(8) COGS Distribution Rule Code5 ->OOCR
  LnExcised VarChar(1) Line Excised [O=Open, C=Closed, P=Copied to OEI]
  LocCode Int(11) Location Code ->OLCT
  StockValue Num(19,6) Total COGS Value
  GPTtlBasPr Num(19,6) Total Base Price for Profit
  unitMsr2 nVarChar(100) Pur/Sal UoM if BaseUnit
  NumPerMsr2 Num(19,6) Pur/Sal UoM Value if Base Unit
  SpecPrice VarChar(1) Price Source Type default=N [Y=Special Prices for Business Partner, N=Manual, W=Active Price List, Discount Groups, R=Active Price List, U=Inactive Price List, A=Blanket Agreement, P=Period and Volume Discounts, Q=Period and Volume Discounts, Discount Groups, V=Inactive Price List, Discount Groups, 9=Special Prices for Business Partner, !=Blanket Agreement, 0=Period and Volume Discounts, 1=Period and Volume Discounts, Discount Groups, 2=Active Price List, 7=Active Price List, Discount Groups, 5=Inactive Price List, 6=Inactive Price List, Discount Groups]
  CSTfIPI nVarChar(2) CST for IPI Code
  CSTfPIS nVarChar(2) CST for PIS Code
  CSTfCOFINS nVarChar(2) CST for COFINS Code
  ExLineNo nVarChar(10) ExLineNo
  isSrvCall VarChar(1) Created from Service Call default=N [Y=Yes, N=No]
  PQTReqQty Num(19,6) Pur Quotation: Required Qty
  PQTReqDate Date(8) Pur Quotation: Required Date
  PcDocType Int(11) Purchase Confirmation Doc Type default=-1 [-1=No Type, 22=Purchase Order, 540000006=Purchase Quotation]
  PcQuantity Num(19,6) Purchase Confirmation Quantity
  LinManClsd VarChar(1) Line Was Closed Manually default=N [Y=Yes, N=No, U=Unknown]
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  NoInvtryMv VarChar(1) Without Inventory Movement default=N [Y=Yes, N=No]
  ActBaseEnt Int(11) Actual Base Document Entry
  ActBaseLn Int(11) Actual Base Line Number
  ActBaseNum Int(11) Actual Base Document No.
  OpenRtnQty Num(19,6) Quantity Open for Return
  AgrNo Int(11) Agreement No. ->OOAT
  AgrLnNum Int(11) Agreement Row Number
  CredOrigin VarChar(1) Credit Origin ->OBSI
  Surpluses Num(19,6) Surpluses
  DefBreak Num(19,6) Defect and Breakup
  Shortages Num(19,6) Shortages
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  UomEntry2 Int(11) UoM Entry if Base Unit default=0 ->OUOM
  UomCode nVarChar(20) UoM Code
  UomCode2 nVarChar(20) UoM Code if Base Unit
  FromWhsCod nVarChar(8) From Warehouse Code ->OWHS
  NeedQty VarChar(1) Consider Quantity of Items default=N [Y=Yes, N=No]
  PartRetire VarChar(1) Partial Retirement default=N [Y=Yes, N=No]
  RetireQty Num(19,6) Retirement Quantity
  RetireAPC Num(19,6) Retirement APC
  RetirAPCFC Num(19,6) Retirement APC FC
  RetirAPCSC Num(19,6) Retirement APC SC
  InvQty Num(19,6) Quantity - Inventory UoM
  OpenInvQty Num(19,6) Open Quantity (Inventory UoM)
  EnSetCost VarChar(1) Enable Set Item Cost in Return default=N [Y=Yes, N=No]
  RetCost Num(19,6) Return Cost in A/R Return
  Incoterms Int(11) Incoterms default=0 ->ODCI
  TransMod Int(11) Transport Mode default=0 ->ODCI
  LineVendor nVarChar(15) Line Vendor Code ->OCRD
  DistribIS VarChar(1) Distribute Intrastat Freight default=N [Y=Yes, N=No]
  ISDistrb Num(19,6) Intrastat Distrib. Amount
  ISDistrbFC Num(19,6) Intrastat Distrib. Amount (FC)
  ISDistrbSC Num(19,6) Intrastat Distrib. Amount (SC)
  IsByPrdct VarChar(1) Item Is By-Product default=N [N=No, Y=Yes]
  ItemType Int(11) Item Type default=4 [4=Item]
  PriceEdit VarChar(1) Price Was Edited by User default=N [N=No, Y=Yes]
  PrntLnNum Int(11) Parent Line Number
  LinePoPrss VarChar(1) Line PO Process default=N [Y=Yes, N=No]
  FreeChrgBP VarChar(1) Free of Charge (BP) default=N [Y=Yes, N=No]
  TaxRelev VarChar(1) Tax Relevant Row default=Y [Y=Yes, N=No]
  LegalText nVarChar(254) Legal Text
  ThirdParty VarChar(1) Third Party default=N [Y=Yes, N=No]
  LicTradNum nVarChar(32) Federal Tax ID
  InvQtyOnly VarChar(1) Change Qty (Inv. UoM) Only default=N [Y=Yes, N=No]
  UnencReasn Int(11) Reason for Unencumbered ICMS
  ShipFromCo nVarChar(50) Ship-From Code
  ShipFromDe nVarChar(254) Ship-From Description
  FisrtBin nVarChar(228) First Bin Location
  AllocBinC nVarChar(11) Allocated Bin Location Count
  ExpType nVarChar(4) Expense Type ->OEXD
  ExpUUID nVarChar(50) Expense UUID
  ExpOpType VarChar(1) Expense Operation Type [P=Professional Services, R=Renting Assets, O=Others]
  DIOTNat nVarChar(3) DIOT Nationality ->OCRY
  MYFtype nVarChar(2) MYF type [S1=MYF Wholesale Sales, S2=Retail Sales, P1=MYF Wholesale Purchases, P3=Other Expense Transactions]
  GPBefDisc Num(19,6) Gross Price
  ReturnRsn Int(6) Return Reason default=-1
  ReturnAct Int(6) Return Action default=-1
  StgSeqNum Int(11) Stage Sequence Number
  StgEntry Int(11) Stage Entry ->ORST
  StgDesc nVarChar(100) Stage Description
  ItmTaxType nVarChar(2) Item GST Tax Category [GR=GST Regular, GN=GST Nil Rated, GE=GST Exempt, NE=Excisable, NN=Non-GST Non-Excisable]
  SacEntry Int(11) SAC Entry ->OSAC
  NCMCode Int(11) NCM Code default=-1 ->ONCM
  HsnEntry Int(11) HSN Entry
  OriBAbsEnt Int(11) Original Base Document Internal ID
  OriBLinNum Int(11) Original Base Document Line Number
  OriBDocTyp Int(11) Original Base Document Type
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No, U=Use]
  EncryptIV nVarChar(100) Encrypt IV
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  StdItemId Int(11) Standard Item Identification ->OUNCL
  CommClass Int(11) Commodity Classification ->OUNCL
  VatExEntry Int(11) VAT Exemption AbsEntry ->OVEB
  VatExLN Int(6) VAT Exemption LineNum
  NatOfTrans Int(11) Nature of Transaction ->ODCI
  ISDtCryImp nVarChar(3) Destination Country/Region for Import ->OCRY
  ISDtRgnImp Int(11) Destination Region for Import ->ODCI
  ISOrCryExp nVarChar(3) Country/Region of Origin for Export ->OCRY
  ISOrRgnExp Int(11) Region of Origin for Export ->ODCI
  NVECode nVarChar(6) NVE Code
  PoNum nVarChar(20) Customer's Purchase Order Number
  PoItmNum Int(11) Customer's Purchase Order Item Number
  IndEscala VarChar(1) Indicator for Relevant Scale default=N [Y=Yes, N=No]
  CESTCode Int(11) CEST Code ->OCEST
  CtrSealQty Num(19,6) Control Seal Quantity
  CNJPMan nVarChar(14) CNPJ of Manufacturer
  UFFiscBene nVarChar(10) UF Fiscal Benefit Code
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]
  LegalTIMD nVarChar(250) Legal Text from Item Master Data
  LegalTTCA nVarChar(250) Legal Text from Tax Code Attributes
  LegalTW nVarChar(250) Legal Text from Warehouse
  LegalTCD nVarChar(250) Legal Text from Tax Code Determination
  RevCharge VarChar(1) Reverse Charge default=N [Y=Yes, N=No]
  ListNum Int(6) Price List No. ->OPLN

# RDN10 - Returns - Row Structure
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SECONDARY U: DocEntry, AftLineNum, OrderNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDN
  LineSeq Int(11) Row Sequence
  AftLineNum Int(11) After Row Number
  OrderNum Int(11) Order Number
  LineType VarChar(1) Row Type [T=Text, S=Subtotal]
  LineText Text(16) Row Text
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=16 ->ADP1

# RDN11 - Returns - Drawn Dpm Detail
Module: Marketing Documents | 70 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LineSeq
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDN
  LineNum Int(11) Row Number
  LineSeq Int(11) Sequence Number
  BaseAbs Int(11) Base Document Internal ID
  BaseType Int(11) Base Object Type default=-1 [-1=]
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  VatPrcnt Num(19,6) VAT Percent
  LineTotal Num(19,6) Net LC
  TotalFrgn Num(19,6) Net FC
  TotalSumSy Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFrgn Num(19,6) Tax FC
  VatSumSys Num(19,6) Tax SC
  ObjType nVarChar(20) Object Type default=16 ->ADP1
  LogInstanc Int(11) Log Instance
  IsAcq VarChar(1) Acquisition Tax-Liable default=N [N=No, Y=Yes]
  IsAllDrawn VarChar(1) Remaining Amount Drawn default=N [Y=Yes, N=No]
  IsGross VarChar(1) Is Gross Line default=N [N=Net Line, Y=Gross Line]
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  ApplNet Num(19,6) Applied Net LC
  ApplNetFc Num(19,6) Applied Net FC
  ApplNetSc Num(19,6) Applied Net SC
  ApplVat Num(19,6) Applied Tax LC
  ApplVatFc Num(19,6) Applied Tax FC
  ApplVatSc Num(19,6) Applied Tax SC
  BaseNet Num(19,6) Base Net LC
  BaseNetFc Num(19,6) Base Net FC
  BaseNetSc Num(19,6) Base Net SC
  BaseVat Num(19,6) Base Tax LC
  BaseVatFc Num(19,6) Base Tax FC
  BaseVatSc Num(19,6) Base Tax SC
  BaseGross Num(19,6) Base Gross LC
  BaseGrossF Num(19,6) Base Gross FC
  BaseGrossS Num(19,6) Base Gross SC
  LineType VarChar(1) Line Type default=D [D=Document Row, R=Currency Rounding, H=Down Payment Document Rounding]
  DctSum Num(19,6) Deductible Sum LC
  DctSumFc Num(19,6) Deductible Sum FC
  DctSumSc Num(19,6) Deductible Sum SC
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplDct Num(19,6) Applied Deductible Sum LC
  ApplDctFc Num(19,6) Applied Deductible Sum FC
  ApplDctSc Num(19,6) Applied Deductible Sum SC
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  BaseDct Num(19,6) Base Deductible Sum LC
  BaseDctFc Num(19,6) Base Deductible Sum FC
  BaseDctSc Num(19,6) Base Deductible Sum SC
  BaseEq Num(19,6) Base Equalization Sum LC
  BaseEqFc Num(19,6) Base Equalization Sum FC
  BaseEqSc Num(19,6) Base Equalization Sum SC
  TaxCode nVarChar(8) Tax Code ->OSTC
  ApplGross Num(19,6) Applied Gross LC
  ApplGrossF Num(19,6) Applied Gross FC
  ApplGrossS Num(19,6) Applied Gross SC
  TaxAdjust VarChar(1) Manual Tax Adjustment default=N [Y=Yes, N=No]
  RvsChrgSum Num(19,6) Reverse Charge Sum LC
  RvsChrgFc Num(19,6) Reverse Charge Sum FC
  RvsChrgSc Num(19,6) Reverse Charge Sum SC
  BasRvsChrg Num(19,6) Base Reverse Charge LC
  BasRvsFc Num(19,6) Base Reverse Charge FC
  BasRvsSc Num(19,6) Base Reverse Charge SC
  ApplRvs Num(19,6) Applied Reverse Charge LC
  ApplRvsFc Num(19,6) Applied Reverse Charge FC
  ApplRvsSc Num(19,6) Applied Reverse Charge SC
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# RDN12 - Returns - Tax Extension
Module: Marketing Documents | 117 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDN
  TaxId0 nVarChar(100) Tax ID 0
  TaxId1 nVarChar(100) Tax ID 1
  TaxId2 nVarChar(100) Tax ID 2
  TaxId3 nVarChar(100) Tax ID 3
  TaxId4 nVarChar(100) Tax ID 4
  TaxId5 nVarChar(100) Tax ID 5
  TaxId6 nVarChar(100) Tax ID 6
  TaxId7 nVarChar(100) Tax ID 7
  TaxId8 nVarChar(100) Tax ID 8
  TaxId9 nVarChar(100) Tax ID 9
  State nVarChar(3) State Code
  County nVarChar(7) County Code
  Incoterms nVarChar(3) Incoterms
  Vehicle nVarChar(10) Vehicle ID
  VidState nVarChar(3) Vehicle ID (State)
  NfRef nVarChar(254) Nota Fiscal Reference
  Carrier nVarChar(15) Carrier Code
  QoP Int(11) Quantity of Packs
  PackDesc nVarChar(10) Pack Description
  Brand nVarChar(20) Brand
  NoSU Int(11) Number of Shipping Unit
  NetWeight Num(19,6) Net Weight
  GrsWeight Num(19,6) Gross Weight
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=16 ->ADP1
  TaxId10 nVarChar(100) Tax ID 10
  TransCat nVarChar(100) Transaction Category
  FormNo nVarChar(100) Form No.
  TaxId11 nVarChar(100) Tax ID 11
  StreetS nVarChar(100) Street
  BlockS nVarChar(100) Block
  BuildingS Text(16) Building/Floor/Room
  CityS nVarChar(100) City
  ZipCodeS nVarChar(20) Zip Code
  CountyS nVarChar(100) County
  StateS nVarChar(3) State ->OCST
  CountryS nVarChar(3) Country/Region ->OCRY
  AddrTypeS nVarChar(100) Address Type
  StreetNoS nVarChar(100) Street No.
  StreetB nVarChar(100) Street
  BlockB nVarChar(100) Block
  BuildingB Text(16) Building/Floor/Room
  CityB nVarChar(100) City
  ZipCodeB nVarChar(20) Zip Code
  CountyB nVarChar(100) County
  StateB nVarChar(3) State ->OCST
  CountryB nVarChar(3) Country/Region ->OCRY
  AddrTypeB nVarChar(100) Address Type
  StreetNoB nVarChar(100) Street No.
  ImpORExp VarChar(1) Import or Export [N=, Y=]
  Vat VarChar(1) VAT default=N [N=No VAT Support, Y=VAT Support]
  AltCrdNamB nVarChar(100) Alternative BP Name
  AltTaxIdB nVarChar(32) Alternative Tax ID
  Address2S nVarChar(50) Address Name 2
  Address3S nVarChar(50) Address Name 3
  Address2B nVarChar(50) Address Name 2
  Address3B nVarChar(50) Address Name 3
  MainUsage Int(11) Main Usage Code of Document ->OUSG
  GlbLocNumS nVarChar(50) Global Location Number
  GlbLocNumB nVarChar(50) Global Location Number
  CollectDT nVarChar(20) Date and Time of Collection
  TransprtDT Date(8) Transport Starting Date
  TransprtRS nVarChar(100) Transport Reason
  TaxId12 nVarChar(50) Tax ID 12
  TaxId13 nVarChar(100) Deductee Ref. No. in India
  ImpExpNo nVarChar(100) Import/Export Bill No.
  ImpExpDate Date(8) Import/Export Date
  BpGSTType Int(11) GST Regn Type of BP
  BpGSTN nVarChar(15) GST Regn No of BP
  BpStateCod nVarChar(3) State Code of Business Partner ->OCST
  BPStatGSTN nVarChar(2) GST State Code of BP
  LocGSTType Int(11) GST Regn Type of Location
  LocGSTN nVarChar(15) GST Regn No of Location
  LocStatCod nVarChar(3) State Code of Location ->OCST
  LocStaGSTN nVarChar(2) GST State Code of Location
  BpCountry nVarChar(3) Country/Region Code of BP ->OCRY
  OrigImpNo nVarChar(100) Original Bill of Entry No.
  OrigImpDat Date(8) Original Bill of Entry Date
  ExportType VarChar(1) Exporting Type default=E [E=Imports/Exports, S=SEZ Developer, U=SEZ Unit, D=Deemed Imports/Exports]
  PortCode nVarChar(100) Port Code
  BoEValue Num(19,6) Bill of Entry Value
  IsIGSTAct VarChar(1) Supply under IGST Account [Y=Yes, N=No]
  ClaimRefun VarChar(1) Claim Refund [Y=Yes, N=No]
  TaxRateDif Int(11) Differential % of Tax Rate [65=, 100=]
  BPGdsIssP nVarChar(15) Goods Issue Place BP
  CNPJGIP nVarChar(100) Goods Issue Place CNPJ
  CPFGIP nVarChar(100) Goods Issue Place CPF
  StreetGIP nVarChar(100) Goods Issue Place Street
  StrtNoGIP nVarChar(100) Goods Issue Place Street No.
  BldngGIP Text(16) Goods Issue Place Building
  ZipGIP nVarChar(20) Goods Issue Place Zip Code
  BlockGIP nVarChar(100) Goods Issue Place Block
  CityGIP nVarChar(100) Goods Issue Place City
  CountyGIP nVarChar(100) Goods Issue Place County
  StateGIP nVarChar(3) Goods Issue Place State ->OCST
  CountryGIP nVarChar(3) Goods Issue Place Country/Region ->OCRY
  PhoneGIP nVarChar(20) Goods Issue Place Phone
  EMailGIP nVarChar(100) Goods Issue Place E-Mail
  DptDateGIP Date(8) Goods Issue Place Departure Date
  BPDelivryP nVarChar(15) Delivery Place BP
  CNPJDlvryP nVarChar(100) Delivery Place CNPJ
  CPFDlvryP nVarChar(100) Delivery Place CPF
  StrtDlvryP nVarChar(100) Delivery Place Street
  StrNoDlvrP nVarChar(100) Delivery Place Street No.
  BldDlvryP Text(16) Delivery Place Building
  ZipDlvryP nVarChar(20) Delivery Place Zip Code
  BlckDlvryP nVarChar(100) Delivery Place Block
  CityDlvryP nVarChar(100) Delivery Place City
  CntyDlvryP nVarChar(100) Delivery Place County
  StatDlvryP nVarChar(3) Delivery Place State ->OCST
  CtryDlvryP nVarChar(3) Delivery Place Country/Region ->OCRY
  FoneDlvryP nVarChar(20) Delivery Place Phone
  MailDlvryP nVarChar(100) Delivery Place E-Mail
  DpDtDlvryP Date(8) Delivery Place Departure Date
  AuthedCNPJ nVarChar(250) Authorized CNPJ or CPF
  TaxId14 nVarChar(250) ITR Filing

# RDN13 - Returns Rows - Distributed Expenses
Module: Marketing Documents | 59 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDN
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=16 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Aquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Normal Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) VAT Applied Frgn
  VatAppldSC Num(19,6) VAT Applied Sys
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock default=N [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Line No.
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Abs. Entry default=-1
  BaseGroup Int(11) Base Document Group default=-1
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1
  VisOrder Int(11) Visual Order
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DistribExp VarChar(1) Distribute Freights [Y=Yes, N=No]
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ

# RDN14 - Return - Assembly - Rows
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDN
  LineNum Int(11) Row Number default=-1
  ChildNum Int(11) Child Number default=-1
  ItemCode nVarChar(50) Item no. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  TotalQty Num(19,6) Total Quantity
  OpenQty Num(19,6) Remaining Open Quantity
  ObjectType nVarChar(20) object type default=16 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BaseChildN Int(11) Base Child Number default=-1
  EncryptIV nVarChar(100) Encrypt IV

# RDN15 - Returns - Drawn Dpm Applied
Module: Marketing Documents | 84 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDN
  LineNum Int(11) Row Number
  ObjType nVarChar(20) object type default=16 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  StaCode nVarChar(8) Tax Authority Code
  StaType Int(11) Tax Authority Type
  StaIndex Int(11) Tax Authority Seq Index
  BaseNet Num(19,6) Net LC
  BaseNetFc Num(19,6) Net FC
  BaseNetSc Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFc Num(19,6) Tax FC
  VatSumSc Num(19,6) Tax SC
  DctSum Num(19,6) Deductible Sum LC
  DctSumFc Num(19,6) Deductible Sum FC
  DctSumSc Num(19,6) Deductible Sum SC
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplNet Num(19,6) Applied Net LC
  ApplNetFc Num(19,6) Applied Net FC
  ApplNetSc Num(19,6) Applied Net SC
  ApplVat Num(19,6) Applied Tax LC
  ApplVatFc Num(19,6) Applied Tax FC
  ApplVatSc Num(19,6) Applied Tax SC
  ApplDct Num(19,6) Applied Deductible Sum LC
  ApplDctFc Num(19,6) Applied Deductible Sum FC
  ApplDctSc Num(19,6) Applied Deductible Sum SC
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  PaidNet Num(19,6) Paid Net LC
  PaidNetFc Num(19,6) Paid Net FC
  PaidNetSc Num(19,6) Paid Net SC
  PaidVat Num(19,6) Paid Tax LC
  PaidVatFc Num(19,6) Paid Tax FC
  PaidVatSc Num(19,6) Paid Tax SC
  PaidDct Num(19,6) Paid Deductible Sum LC
  PaidDctFc Num(19,6) Paid Deductible Sum FC
  PaidDctSc Num(19,6) Paid Deductible Sum SC
  PaidEq Num(19,6) Paid Equalization Sum LC
  PaidEqFc Num(19,6) Paid Equalization Sum FC
  PaidEqSc Num(19,6) Paid Equalization Sum SC
  DpApplNet Num(19,6) Dpm Appl Net LC
  DpApplNetF Num(19,6) Dpm Appl Net FC
  DpApplNetS Num(19,6) Dpm Appl Net SC
  DpApplVat Num(19,6) Dpm Appl Tax LC
  DpApplVatF Num(19,6) Dpm Appl Tax FC
  DpApplVatS Num(19,6) Dpm Appl Tax SC
  DpApplDct Num(19,6) Dpm Appl Deductible Sum LC
  DpApplDctF Num(19,6) Dpm Appl Deductible Sum FC
  DpApplDctS Num(19,6) Dpm Appl Deductible Sum SC
  DpApplEq Num(19,6) Dpm Appl Equalization Sum LC
  DpApplEqFc Num(19,6) Dpm Appl Equalization Sum FC
  DpApplEqSc Num(19,6) Dpm Appl Equalization Sum SC
  TaxCode nVarChar(8) Tax Code ->OSTC
  LineType VarChar(1) Row Type default=D [D=Document, R=Exchange Rate Rounding, H=Document Header Rounding]
  BaseGrs Num(19,6) Gross LC
  BaseGrsFc Num(19,6) Gross FC
  BaseGrsSc Num(19,6) Gross SC
  ApplGrs Num(19,6) Applied Gross LC
  ApplGrsFc Num(19,6) Applied Gross FC
  ApplGrsSc Num(19,6) Applied Gross SC
  PaidGrs Num(19,6) Paid Gross LC
  PaidGrsFc Num(19,6) Paid Gross FC
  PaidGrsSc Num(19,6) Paid Gross SC
  DpApplGrs Num(19,6) Dpm Appl Gross LC
  DpApplGrsF Num(19,6) Dpm Appl Gross FC
  DpApplGrsS Num(19,6) Dpm Appl Gross SC
  RvsChrgSum Num(19,6) Reverse Charge Sum
  RvsChrgSc Num(19,6) Reverse Charge Sum (SC)
  RvsChrgFc Num(19,6) Reverse Charge Sum (FC)
  ApplRvs Num(19,6) Applied Reverse Charge Sum LC
  ApplRvsSc Num(19,6) Applied Reverse Charge Sum SC
  ApplRvsFc Num(19,6) Applied Reverse Charge Sum FC
  PaidRvs Num(19,6) Paid Reverse Charge Sum LC
  PaidRvsSc Num(19,6) Paid Reverse Charge Sum SC
  PaidRvsFc Num(19,6) Paid Reverse Charge Sum FC
  DpApplRvs Num(19,6) Dpm Applied Reverse Charge LC
  DpApplRvsS Num(19,6) Dpm Applied Reverse Charge SC
  DpApplRvsF Num(19,6) Dpm Applied Reverse Charge FC
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# RDN16 - Returns - SnB properties
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, SnBIndex
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) abs entry ->ORDN
  LineNum Int(11) Line Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object id
  ObjAbs Int(11) Object Abs
  DrfWObjAbs Int(11) draft Wobj Abs default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type default=16
  LogInstanc Int(11) Log Instance

# RDN17 - Returns - Import Process
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDN
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=16 ->ADP1
  ImpDocType VarChar(1) Type of Importation Document ->OBSI
  ImpDocNum nVarChar(10) Importation Document Number
  DateOfReg Date(8) Date of Registry DI/DSI/DA
  CustClrDat Date(8) Date of Customs Clearance
  ConcActNum nVarChar(30) Drawback Concession Acct No.
  AdditNum nVarChar(30) Additional Number
  AddItmDV Num(19,6) Additional Item Discount Value
  tpVTransp Int(6) Overland Transport Route [1=Maritime, 2=Waterway, 3=Lakeside, 4=Air, 5=Post, 6=Train, 7=Road, 8=Network Transmission, 9=Own Means, 10=Input/Output Fictitious, 11=Courier, 12=Hand Carry]
  DrawSReg nVarChar(11) Drawback - Suspension Regime
  AddFrNavyA Num(19,6) Additional Freight to Navy Authority
  TypeOfImp VarChar(1) Type of Import
  nSeqAdic Int(6) Additional Item Sequential Number

# RDN18 - Returns - Export Process
Module: Marketing Documents | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDN
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=16 ->ADP1
  ExpDocType Int(11) Type of Exportation Document default=-1 ->OBNI
  ExpDeclNum Int(11) Exportation Declaration Number
  ExpDeclDat Date(8) Exportation Declaration Date
  ExpNature Int(11) Nature of Exportation default=-1 ->OBNI
  ExpRegNum Int(11) Number of Exportation Registry
  ExpRegDate Date(8) Date of Exportation Registry
  LadBillNum nVarChar(19) Bill of Lading Number
  LadBillDat Date(8) Date of Bill of Lading
  MerchLeftD Date(8) Date Merchandise Left Customs
  LadBillTyp Int(11) Type of Bill of Lading default=-1 ->OBNI
  DrawSReg nVarChar(11) Drawback - Suspension Regime
  NatureExp nVarChar(44) Nature of Export
  QultExpItm Num(19,6) Quantity of Exported Items
  nSeqAdic Int(6) Additional Item Sequential Number

# RDN19 - Returns - Bin Allocation Data
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, BinAllocSe
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->ORDN
  BinAllocSe Int(11) Bin Allocation Sequence
  LineNum Int(11) Line Number
  SubLineNum Int(11) Subline Number default=-1
  SnBType Int(11) SnB Type default=-1
  SnBMDAbs Int(11) SnB Master Data Internal No. default=-1
  BinAbs Int(11) Bin Internal Number ->OBIN
  Quantity Num(19,6) Quantity
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjType nVarChar(20) Object Type default=16 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  BinActTyp Int(6) Bin Action Type [1=Transaction In, 2=Transaction Out, 4=SnB Complete, 8=Bin First Then SnB]

# RDN2 - Return - Freight - Rows
Module: Marketing Documents | 64 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDN
  LineNum Int(11) Row Number
  GroupNum Int(11) Freight Group
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=16 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) Vat Applied
  VatAppldFC Num(19,6) Vat Applied Frgn
  VatAppldSC Num(19,6) Vat Applied Sys
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report [Y=Yes, N=No]
  BaseGroup Int(11) Base Document Group default=-1 [-1=, 0=, 1=, 2=]
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1 [-1=, 0=, 1=, 2=]
  VisOrder Int(11) Visual Order
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]

# RDN20 - Intrastat Expenses
Module: Marketing Documents | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDN
  ExpnsCode Int(11) Freight Code ->OEXD
  TotalLC Num(19,6) Total
  TotalFC Num(19,6) Total (FC)
  TotalSC Num(19,6) Total (SC)
  DistribM VarChar(1) Distribution Method default=T [Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DrawnLC Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  LineNum Int(11) Line Number default=-1
  BaseAbsEnt Int(11) Base Abs. Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 16=Return, 13=A/R Invoice, 203=Down Payment Incoming, 204=Down Payment Outgoing, 22=Purchase Order, 20=Goods Receipt PO, 21=Goods Return, 18=A/P Invoice, 540000006=Purchase Quotation, 0=, -1=]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No. default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=16 ->ADP1
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  AppliedLC Num(19,6) Applied
  AppliedFC Num(19,6) Applied (FC)
  AppliedSC Num(19,6) Applied (SC)

# RDN21 - Returns - Document Reference Information
Module: Marketing Documents | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, RefType
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjectType nVarChar(20) Object Type default=16
  LogInstanc Int(11) Log Instance default=0
  RefType VarChar(1) Reference Types default=S [S=System Document, E=External Document]
  LineNum Int(11) Line Number
  RefDocEntr Int(11) Referenced Internal Number
  RefDocNum Int(11) Referenced Document Number
  ExtDocNum nVarChar(100) External Referenced Document Number
  RefObjType nVarChar(20) Referenced Object Type [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 234000031=Return Request, 16=Return, 203=A/R Down Payment, 13=A/R Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 280=A/R Tax Invoice, 1470000113=Purchase Request, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Return Request, 21=Goods Return, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 281=A/P Tax Invoice, 69=Landed Costs, 24=Incoming Payments, 46=Outgoing Payments, 57=Checks for Payment, 321=Internal Reconciliation, 34=Recurring Posting, 30=Journal Entry, 59=Goods Receipt, 60=Goods Issue, 162=Inventory Revaluation, 1470000065=Inventory Counting, 10000071=Inventory Posting, 1250000001=Inventory Transfer Request, 67=Inventory Transfer, 202=Production Order, 13001=Original Invoice, -1=External Document, 20301=Original Down Payment Invoice]
  AccessKey nVarChar(100) Access Key
  IssueDate Date(8) Date of Issue
  IssuerCNPJ nVarChar(100) Issuer CNPJ
  IssuerCode nVarChar(10) Fiscal Document Issuer UF Code
  Model nVarChar(6) Fiscal Document Model
  Series nVarChar(3) Fiscal Document Series
  Number Int(11) Fiscal Document Number
  RefAccKey nVarChar(100) Referenced CT-e Access Key
  RefAmount Num(19,6) Referenced Amount
  SubSeries nVarChar(3) Fiscal Document Subseries
  Remark nVarChar(254) Remarks
  LinkRefTyp nVarChar(20) Link Reference Type default=00 [00=, 01=Nota de cr�dito de los documentos relacionados, 02=Nota de d�bito de los documentos relacionados, 03=Devoluci�n de mercanc�a sobre facturas o traslados previos, 04=Sustituci�n de los CFDI previos, 05=Traslados de mercancias facturados previamente, 06=Factura generada por los traslados previos, 07=CFDI por aplicaci�n de anticipo, 08=Customs, MX_08=Factura generada por pagos en parcialidades, 09=Factura generada por pagos diferidos]

# RDN22 - Returns - Resource Costs
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, StdCostNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->RDN1
  LineNum Int(11) Row Number ->RDN1
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=16
  LogInstanc Int(11) Log Instance default=0

# RDN23 - A/P Invoice - Selected Asset Master Data
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, VisOrder
  ASSETS: DocEntry, LineNum, AssetCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDN
  LineNum Int(11) Row Number
  AssetCode nVarChar(50) Selected Asset Code ->OITM
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Remarks nVarChar(100) Remarks
  Amount Num(19,6) Amount
  AmountSC Num(19,6) Amount (SC)
  SerialNo nVarChar(30) Serial Number
  VisOrder Int(11) Visual Order
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=16 ->ADP1

# RDN24 - Returns - Tracking Note Assignment
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  ItemCCDNum nVarChar(40) Item CCD Number
  CntrOrigin nVarChar(3) Country/Region of Origin
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=16 ->ADP1
  SubLineNum Int(11) BOM Line No.

# RDN25 - Returns - Amt Per VAT Grp
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, VatGroup, Type
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  VatGroup nVarChar(8) Tax Definition ->OVTG
  VatPrcnt Num(19,6) Tax Rate
  BaseAmnt Num(19,6) Base Amount
  BaseAmntFC Num(19,6) Base Amount (FC)
  BaseAmntSC Num(19,6) Base Amount (SC)
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  Type Int(11) Type default=1 [1=Discount by Tax]
  Currency nVarChar(3) Price Currency
  Rate Num(19,6) Currency Rate
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=16 ->ADP1

# RDN26 - Returns - E-Way Bill Information
Module: Marketing Documents | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDN
  SuplyType nVarChar(20) EWB Transaction Type [O=Outward, I=Inward]
  SubSplyTyp Int(11) EWB Sub-Type ->OEST
  DocType nVarChar(3) EWB Doc. Type ->OEDT
  TransMode Int(11) EWB Transportation Mode ->OETM
  Distance Num(19,6) EWB Transport Distance
  TransDocNo nVarChar(16) EWB Transporter Doc. No.
  TransDate Date(8) EWB Transportation Date
  VehicleTyp nVarChar(2) EWB Vehicle Type ->OEVT
  VehicleNo nVarChar(15) EWB Vehicle Number
  EWayBillNo nVarChar(20) EWB No.
  EwbDate Date(8) E-Way Bill Date
  FrmTraName nVarChar(100) EWB Consignor Name
  FrmAddres1 nVarChar(120) EWB Consignor Address 1
  FrmAddres2 nVarChar(120) EWB Consignor Address 2
  FrmZipCode nVarChar(20) EWB Consignor Zip Code
  ActFrmStat nVarChar(2) Dispatch State of EWB Consignor
  ToTraName nVarChar(100) EWB Consignee Name
  ToAddres1 nVarChar(120) EWB Consignee Address 1
  ToAddres2 nVarChar(120) EWB Consignee Address 2
  ToZipCode nVarChar(20) EWB Consignee Zip Code
  ActToState nVarChar(2) Ship-To State of EWB Consignee
  FrmGSTN nVarChar(15) EWB Consignor GSTN
  FrmState nVarChar(2) Bill-To State of EWB Consignor
  ToGSTN nVarChar(15) EWB Consignee GSTN
  ToState nVarChar(2) Bill-To State of EWB Consignee
  MainHsnEnt Int(11) EWB Main HSN Entry ->OCHP
  FrmPlace nVarChar(50) EWB Consignor Place
  ToPlace nVarChar(50) EWB Consignee Place
  TransID nVarChar(15) EWB Transporter ID
  TransName nVarChar(25) EWB Transporter Name
  ExpireDate Date(8) EWB Expiration Date
  ObjectType nVarChar(20) Object Type default=16 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TspEntry Int(11) Transporter Abs. Entry ->OTSP
  TspLine Int(11) Transportation Line
  TransType Int(11) Transaction Type [1=Regular, 2=Bill To-Ship To, 3=Bill From-Dispatch From, 4=Combination of 2 and 3]

# RDN27 - Returns - E-Books(GR) Rows
Module: Marketing Documents | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  RELATE_ROW: DocEntry, RelateType, RelateLine, GroupNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDN
  LineNum Int(11) Row Number
  RelateType Int(11) Relation Type default=-1 [1=Row, 2=Row Expenses, 3=Document Expenses, 13=Distributed Freights, -1=Manual]
  RelateLine Int(11) Relation Row Number default=-1
  GroupNum Int(11) Group Number default=-1
  LineTotal Num(19,6) Line Total
  LineTotalF Num(19,6) Line Total (FC)
  LineTotalS Num(19,6) Line Total (SC)
  InClassTyp Int(11) Income Classification Type ->OICP
  InClassCat Int(11) Income Classification Category ->OICC
  ExClassTyp Int(11) Expense Classification Type ->OECP
  ExClassCat Int(11) Expense Classification Cat. ->OECC
  VatCate Int(11) VAT Category
  NetValue Num(19,6) Net Value
  NetValueFC Num(19,6) Net Value (FC)
  NetValueSC Num(19,6) Net Value (SC)
  VatAmount Num(19,6) VAT Amount
  VatAmFC Num(19,6) VAT Amount (FC)
  VatAmSC Num(19,6) VAT Amount (SC)
  WtPercCat Int(11) Withheld Percentage Category
  WtAmount Num(19,6) Withheld Amount
  WtAmountFC Num(19,6) Withheld Amount (FC)
  WtAmountSC Num(19,6) Withheld Amount (SC)
  ObjectType nVarChar(20) Object Type default=13 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  WtCategory VarChar(1) Withheld Category [I=Invoice, P=Payment]
  VATClassTy Int(11) VAT Classification Type ->OECP
  VATClassCa Int(11) VAT Classification Category ->OECC
  EBVatExCau Int(11) VAT Exemption Cause ->OVEC

# RDN28 - Returns - Reported Tracking Note
Module: Marketing Documents | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
  TCN_KEY U: DocEntry, LineNum, TrackingNt, TrackiNtLn
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  UnusedQty Num(19,6) Unused Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=16 ->ADP1
  SubLineNum Int(11) BOM Line No.

# RDN3 - Return - Freight
Module: Marketing Documents | 80 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  DOCUMENT: DocEntry, BaseAbsEnt
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDN
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  Comments nVarChar(100) Remarks
  ObjType nVarChar(20) Object Type default=16 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  WTLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  VatApplied Num(19,6) Vat Applied
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatF Num(19,6) Net Tax Amount (FC)
  LineVatS Num(19,6) Net Tax Amount (SC)
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 15=Delivery, 234000031=A/R Return Request]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No.
  LineNum Int(11) line num default=-1
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Doc. Internal No. default=-1
  StDstr Num(19,6) Stock Distributed Sum
  StDstrSC Num(19,6) Stock Distributed Sum (SC)
  StDstrFC Num(19,6) Stock Distributed Sum (FC)
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  TaxDistMtd VarChar(1) Tax Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  GrsAmount Num(19,6) Gross Amount
  GrsFC Num(19,6) Gross Amount (FC)
  GrsSC Num(19,6) Gross Amount (SC)
  BaseTotal VarChar(1) Base Total for Calculation default=N [N=Net Total, G=Gross Total]
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)
  RRVatLC Num(19,6) Return Request VAT Amount
  RRVatFC Num(19,6) Return Request VAT Amount (FC)
  RRVatSC Num(19,6) Return Request VAT Amount (SC)
  EncryptIV nVarChar(100) Encrypt IV
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]

# RDN4 - Returns - Tax Amount per Document
Module: Marketing Documents | 61 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SCONDARY: DocEntry, LineNum, GroupNum, ExpnsCode, StcCode, StaCode, staType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDN
  LineNum Int(11) Row Number default=-1
  GroupNum Int(11) Group Number default=-1
  ExpnsCode Int(11) Expense Code default=-1 ->OEXD
  RelateType Int(11) Relation Type default=1 [1=Row, 2=Row Freight Charges, 3=Document Expenses, 13=Distributed Freights]
  StcCode nVarChar(8) Tax Code ->OSTC
  StaCode nVarChar(8) Authority Code ->OSTA
  staType Int(11) Authority Type ->OSTT
  TaxRate Num(19,6) Tax Rate
  TaxAcct nVarChar(15) Tax Account ->OACT
  TaxSum Num(19,6) Tax Amount
  TaxSumFrgn Num(19,6) Tax Amount (FC)
  TaxSumSys Num(19,6) Tax Amount (SC)
  BaseSum Num(19,6) Base Amount
  BaseSumFrg Num(19,6) Base Amount (FC)
  BaseSumSys Num(19,6) Base Amount (SC)
  ObjectType nVarChar(20) Object Type default=16 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Status default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  LineSeq Int(11) Line Sequence
  DeferrAcct nVarChar(15) Deferred Tax Account ->OACT
  BaseType Int(11) Base Document Type default=-1
  BaseAbs Int(11) Base Doc Abs Entry default=-1
  BaseSeq Int(11) Base Doc. Line Sequence
  DeductTax Num(19,6) Deductible Tax Amount
  DdctTaxFrg Num(19,6) Deductible Tax Amount (FC)
  DdctTaxSys Num(19,6) Deductible Tax Amount (SC)
  BaseAppld Num(19,6) Applied Base Amount
  BaseApldFC Num(19,6) Applied Base Amount (FC)
  BaseApldSC Num(19,6) Applied Base Amount (SC)
  NonDdctPrc Num(19,6) Non Deductible %
  NonDdctAct nVarChar(15) Non Deductible Account ->OACT
  TaxInPrice VarChar(1) Tax Included in Price? default=N [Y=Yes, N=No]
  Exempt VarChar(1) Exempt? default=N [Y=Yes, N=No]
  TaxExpAct nVarChar(15) Expense Account for Tax ->OACT
  OnHoldTax Num(19,6) On Hold Tax Amount
  OnHoldTaxF Num(19,6) On Hold Tax Amount (FC)
  OnHoldTaxS Num(19,6) On Hold Tax Amount (SC)
  InGrossRev VarChar(1) Included in Gross Revenue default=N [Y=Yes, N=No]
  TaxSumOrg Num(19,6) Tax Amount Original
  TaxSumOrgF Num(19,6) Tax Amount Original (FC)
  TaxSumOrgS Num(19,6) Tax Amount Original (SC)
  OpenTax Num(19,6) Open Service Tax
  OpenTaxFC Num(19,6) Open Service Tax (FC)
  OpenTaxSC Num(19,6) Open Service Tax (SC)
  Unencumbrd VarChar(1) Unencumbered default=N [Y=Yes, N=No]
  TaxOnRI VarChar(1) Tax On Reserve Invoice default=N [Y=Yes, N=No]
  RvsChrgPrc Num(19,6) Reverse Charge %
  RvsChrgTax Num(19,6) Reverse Charge Tax Amount
  RvsChrgSC Num(19,6) Reverse Charge Tax Amount (SC)
  RvsChrgFC Num(19,6) Reverse Charge Tax Amount (FC)
  InFirstIns VarChar(1) Included in First Installment default=N [Y=Yes, N=No]
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CESTrel VarChar(1) CEST Relevant default=N [Y=, N=]

# RDN5 - Returns - Withholding Tax
Module: Marketing Documents | 158 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  SECONDERY U: AbsEntry, WTCode, BaseAbsEnt, Doc1LineNo
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator ->ORDN
  WTCode nVarChar(4) WT Code ->OWHT
  Rate Num(19,6) Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntSC Num(19,6) Taxable Amount in SC
  TxblAmntFC Num(19,6) Taxable Amount in FC
  WTAmnt Num(19,6) WT Amount
  WTAmntSC Num(19,6) WT Amount (SC)
  WTAmntFC Num(19,6) WT Amount (FC)
  ApplAmnt Num(19,6) Applied WT Amount
  ApplAmntSC Num(19,6) Applied WTax Amount (SC)
  ApplAmntFC Num(19,6) Applied WTax Amount (FC)
  Category VarChar(1) Category [P=Payment, I=Invoice]
  Criteria VarChar(1) Criteria [Y=Accrual, N=Cash]
  Account nVarChar(15) G/L Account ->OACT
  Type VarChar(1) Withholding Type [V=VAT Withholding, I=Income Tax Withholding]
  RoundType VarChar(1) Rounding Type [T=Truncated, C=Commercial Values, N=No Rounding]
  BaseType VarChar(1) Base Type [G=Gross, N=Net, V=VAT, U=UoM]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseLine Int(11) Base Line
  BaseNum Int(11) Base Document Type default=-1 [-1=, 0=, 15=Delivery]
  LineNum Int(11) Line Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Abs. Entry default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=16 ->ADP1
  Doc1LineNo Int(11) DOC1 Line Number default=-1
  WtLineType VarChar(1) WT Line Type default=D [D=Document Level WTax, L=Row Level WTax]
  TxblCurr nVarChar(3) Taxable Currency from Doc Line
  DtblCurr nVarChar(3) Deductible Currency
  DtblRate Num(19,6) Rate for Deductible Amount
  txblRate Num(19,6) Rate for Taxable Amount
  DtblAmount Num(19,6) Deductible Amount
  TdsAcc nVarChar(15) TDS Account ->OACT
  SurAcc nVarChar(15) Surcharge Account ->OACT
  CessAcc nVarChar(15) Cess Account ->OACT
  HscAcc nVarChar(15) HSC Account ->OACT
  TdsRate Num(19,6) TDS Rate
  SurRate Num(19,6) Surcharge Rate
  CessRate Num(19,6) Cess Rate
  HscRate Num(19,6) HSC Rate
  TdsBAmt Num(19,6) TDS Base Amount
  TdsBAmtSC Num(19,6) TDS Base Amount (SC)
  TdsBAmtFC Num(19,6) TDS Base Amount (FC)
  SurBAmt Num(19,6) Surcharge Base Amount
  SurBAmtSC Num(19,6) Surcharge Base Amount (SC)
  SurBAmtFC Num(19,6) Surcharge Base Amount (FC)
  CessBAmt Num(19,6) Cess Base Amount
  CessBAmtSC Num(19,6) Cess Base Amount (SC)
  CessBAmtFC Num(19,6) Cess Base Amount (FC)
  HscBAmt Num(19,6) HSC Base Amount
  HscBAmtSC Num(19,6) HSC Base Amount (SC)
  HscBAmtFC Num(19,6) HSC Base Amount (FC)
  TdsAmnt Num(19,6) TDS Tax Amount
  TdsAmntSC Num(19,6) TDS Tax Amount (SC)
  TdsAmntFC Num(19,6) TDS Tax Amount (FC)
  SurAmnt Num(19,6) Surcharge Tax Amount
  SurAmntSC Num(19,6) Surcharge Tax Amount (SC)
  SurAmntFC Num(19,6) Surcharge Tax Amount (FC)
  CessAmnt Num(19,6) Cess Tax Amount
  CessAmntSC Num(19,6) Cess Tax Amount (SC)
  CessAmntFC Num(19,6) Cess Tax Amount (FC)
  HscAmnt Num(19,6) HSC Tax Amount
  HscAmntSC Num(19,6) HSC Tax Amount (SC)
  HscAmntFC Num(19,6) HSC Tax Amount (FC)
  TdsAppl Num(19,6) Applied TDS Amount
  TdsApplSC Num(19,6) Applied TDS Amount (SC)
  TdsApplFC Num(19,6) Applied TDS Amount (FC)
  SurAppl Num(19,6) Applied Surcharge Amount
  SurApplSC Num(19,6) Applied Surcharge Amount (SC)
  SurApplFC Num(19,6) Applied Surcharge Amount (FC)
  CessAppl Num(19,6) Applied Cess Amount
  CessApplSC Num(19,6) Applied Cess Amount (SC)
  CessApplFC Num(19,6) Applied Cess Amount (FC)
  HscAppl Num(19,6) Applied HSC Amount
  HscApplSC Num(19,6) Applied HSC Amount (SC)
  HscApplFC Num(19,6) Applied HSC Amount (FC)
  BatchNum Int(11) Journal Voucher No.
  InCSTCode nVarChar(2) CST Code Incoming
  OutCSTCode nVarChar(2) CST Code Outgoing
  DpmWTApl Num(19,6) DPM WT Applied Amount
  DpmWTAplSC Num(19,6) DPM WT Applied Amount (SC)
  DpmWTAplFC Num(19,6) DPM WT Applied Amount (FC)
  WTTypeId Int(11) WT Type Id ->OWTT
  LnBsAmt Num(19,6) BR Line WT Base Amount
  LnBsAmtSC Num(19,6) BR Line WT Base Amount(SC)
  LnBsAmtFC Num(19,6) BR Line WT Base Amount(FC)
  LnCmTAmt Num(19,6) BR Line Cumulated Taxable Amount
  LnCmTAmtSC Num(19,6) BR Line Cumulated Taxable Amount(SC)
  LnCmTAmtFC Num(19,6) BR Line Cumulated Taxable Amount(FC)
  TDSType VarChar(1) TDS Type [E=eTDS, D=GST TDS, C=GST TCS, S=SALES TCS]
  IgstAcc nVarChar(15) IGST Account ->OACT
  CgstAcc nVarChar(15) CGST Account ->OACT
  SgstAcc nVarChar(15) SGST Account ->OACT
  IgstAmnt Num(19,6) IGST Tax Amount
  IgstAmntSC Num(19,6) IGST Tax Amount (SC)
  IgstAmntFC Num(19,6) IGST Tax Amount (FC)
  CgstAmnt Num(19,6) CGST Tax Amount
  CgstAmntSC Num(19,6) CGST Tax Amount (SC)
  CgstAmntFC Num(19,6) CGST Tax Amount (FC)
  SgstAmnt Num(19,6) SGST Tax Amount
  SgstAmntSC Num(19,6) SGST Tax Amount (SC)
  SgstAmntFC Num(19,6) SGST Tax Amount (FC)
  IgstRate Num(19,6) IGST Rate
  CgstRate Num(19,6) CGST Rate
  SgstRate Num(19,6) SGST Rate
  IgstBAmt Num(19,6) IGST Base Amount
  IgstBAmtSC Num(19,6) IGST Base Amount (SC)
  IgstBAmtFC Num(19,6) IGST Base Amount (FC)
  CgstBAmt Num(19,6) CGST Base Amount
  CgstBAmtSC Num(19,6) CGST Base Amount (SC)
  CgstBAmtFC Num(19,6) CGST Base Amount (FC)
  SgstBAmt Num(19,6) SGST Base Amount
  SgstBAmtSC Num(19,6) SGST Base Amount (SC)
  SgstBAmtFC Num(19,6) SGST Base Amount (FC)
  IgstAppl Num(19,6) Applied IGST Amount
  IgstApplSC Num(19,6) Applied IGST Amount (SC)
  IgstApplFC Num(19,6) Applied IGST Amount (FC)
  CgstAppl Num(19,6) Applied CGST Amount
  CgstApplSC Num(19,6) Applied CGST Amount (SC)
  CgstApplFC Num(19,6) Applied CGST Amount (FC)
  SgstAppl Num(19,6) Applied SGST Amount
  SgstApplSC Num(19,6) Applied SGST Amount (SC)
  SgstApplFC Num(19,6) Applied SGST Amount (FC)
  UtgstAcc nVarChar(15) UTGST Account ->OACT
  CsgstAcc nVarChar(15) Cess GST Account ->OACT
  UtgstAmt Num(19,6) UTGST Tax Amount
  UtgstAmtSC Num(19,6) UTGST Tax Amount (SC)
  UtgstAmtFC Num(19,6) UTGST Tax Amount (FC)
  CsgstAmt Num(19,6) Cess GST Tax Amount
  CsgstAmtSC Num(19,6) Cess GST Tax Amount (SC)
  CsgstAmtFC Num(19,6) Cess GST Tax Amount (FC)
  UtgstRate Num(19,6) UTGST Rate
  CsgstRate Num(19,6) Cess GST Rate
  UtgstBAmt Num(19,6) UTGST Base Amount
  UtgstBAmtS Num(19,6) UTGST Base Amount (SC)
  UtgstBAmtF Num(19,6) UTGST Base Amount (FC)
  CsgstBAmt Num(19,6) Cess GST Base Amount
  CsgstBAmtS Num(19,6) Cess GST Base Amount (SC)
  CsgstBAmtF Num(19,6) Cess GST Base Amount (FC)
  UtgstAppl Num(19,6) Applied UTGST Amount
  UtgstApplS Num(19,6) Applied UTGST Amount (SC)
  UtgstApplF Num(19,6) Applied UTGST Amount (FC)
  CsgstAppl Num(19,6) Applied Cess GST Amount
  CsgstApplS Num(19,6) Applied Cess GST Amount (SC)
  CsgstApplF Num(19,6) Applied Cess GST Amount (FC)
  EncryptIV nVarChar(100) Encrypt IV
  TcsIntAcct nVarChar(15) TCS Interim Account ->OACT
  SurIntAcct nVarChar(15) Surcharge Interim Account ->OACT
  CesIntAcct nVarChar(15) Cess Interim Account ->OACT
  HscIntAcct nVarChar(15) HSC interim Account ->OACT
  LnIntAcct nVarChar(15) Interim Account for Tax ->OACT
  FixedAmnt Num(19,6) Fixed Amount
  FixedAmtSC Num(19,6) Fixed Amount (SC)
  FixedAmtFC Num(19,6) Fixed Amount (FC)
  BaseQty Num(19,6) Base Quantity

# RDN6 - Returns - Installments
Module: Marketing Documents | 65 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, InstlmntID
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDN
  InstlmntID Int(6) Installment ID default=1
  ObjType nVarChar(20) Object Type default=16 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DueDate Date(8) Due Date
  Status VarChar(1) Installment Status default=O [O=Open, C=Closed]
  DunnLevel Int(11) Dunning Level default=0
  InsTotal Num(19,6) Total Installment
  InsTotalFC Num(19,6) Total Installment (FC)
  InsTotalSy Num(19,6) Total Installment (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  VatSum Num(19,6) Total Tax
  VatSumFC Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  VatPaid Num(19,6) Tax Paid to Date
  VatPaidFC Num(19,6) Tax Paid (FC)
  VatPaidSys Num(19,6) Tax Paid (SC)
  TotalExpns Num(19,6) Total Freight Charges
  TotalExpFC Num(19,6) Total Freight Charges (FC)
  TotalExpSC Num(19,6) Total Freight Charges (SC)
  ExpAppl Num(19,6) Applied Freight Charges
  ExpApplFC Num(19,6) Applied Freight Charges (SC)
  ExpApplSC Num(19,6) Applied Freight Charges (SC)
  WTSum Num(19,6) WTax Amount
  WTSumFC Num(19,6) WTax Amount (FC)
  WTSumSC Num(19,6) WTax Amount (SC)
  WTApplied Num(19,6) Applied WTax
  WTAppliedF Num(19,6) Applied WTax (FC)
  WTAppliedS Num(19,6) Applied WTax (SC)
  TotalBlck Num(19,6) Total Reserved Amount
  TotalBlckF Num(19,6) Total Reserved Amount (FC)
  TotalBlckS Num(19,6) Total Reserved Amount (SC)
  VATBlck Num(19,6) Reserved Tax
  VATBlckFC Num(19,6) Reserved Tax (FC)
  VATBlckSC Num(19,6) Reserved Tax (SC)
  ExpnsBlck Num(19,6) Reserved Freight Charges
  ExpnsBlckF Num(19,6) Reserved Freight Charges (FC)
  ExpnsBlckS Num(19,6) Reserved Freight Charges (SC)
  WTBlocked Num(19,6) Reserved WTax Amount
  WTBlockedF Num(19,6) Reserved WTax Amount (FC)
  WTBlockedS Num(19,6) Reserved WTax Amount (SC)
  InstPrcnt Num(19,6) Installment %
  DunWizBlck VarChar(1) Wizard dunning block default=N [N=No, Y=Yes]
  DunDate Date(8) Last Dunning Date
  Paid Num(19,6) Paid
  PaidFrgn Num(19,6) Paid (FC)
  PaidSc Num(19,6) Paid (SC)
  reserved VarChar(1) Reserved default=N [N=No, Y=Yes]
  TaxOnExp Num(19,6) Tax on Expenses
  TaxOnExpFc Num(19,6) Tax on Expenses (FC)
  TaxOnExpSc Num(19,6) Tax on Expenses (SC)
  TaxOnExpAp Num(19,6) Applied Tax on Expenses
  TaxOnExApF Num(19,6) Applied Tax on Expenses (FC)
  TaxOnExApS Num(19,6) Applied Tax on Expenses (SC)
  TaxOnExBlo Num(19,6) Reserved Tax on Freight Amount
  TaxOnExBlF Num(19,6) Reserved Tax on Freight Amt FC
  TaxOnExBlS Num(19,6) Reserved Tax on Freight Amt SC
  LvlUpdDate Date(8) Dunning Level Update Date
  Ordered VarChar(1) Payment Ordered default=N [Y=Yes, N=No]
  PaidDpm Num(19,6) Paid by Down Payment
  PaidDpmFc Num(19,6) Paid by Down Payment (FC)
  PaidDpmSc Num(19,6) Paid by Down Payment (SC)
  EncryptIV nVarChar(100) Encrypt IV

# RDN7 - Delivery Packages - Returns
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDN
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type default=16 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV

# RDN8 - Returns - Items in Package
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum, ItemCode, UomEntry, NumPerMsr
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDN
  PackageNum Int(11) Package Number
  ItemCode nVarChar(50) Item Code ->OITM
  Quantity Num(19,6) Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=16 ->ADP1
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value default=0

# RDN9 - Returns - Drawn Dpm
Module: Marketing Documents | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDN
  LineNum Int(11) Row Number
  BaseAbs Int(11) Base Document Internal ID
  BaseLine Int(11) Base Document Row
  TargetBase VarChar(1) Target or Base Document default=B [B=Base, T=Target]
  ObjType nVarChar(20) Base Object Type
  DrawnSum Num(19,6) Net LC
  DrawnSumFc Num(19,6) Net FC
  DrawnSumSc Num(19,6) Net SC
  LogInstanc Int(11) Log Instance default=0
  ObjCode nVarChar(20) Object Type default=16 ->ADP1
  ApplDrawn Num(19,6) Applied Net LC
  ApplDrawnF Num(19,6) Applied Net FC
  ApplDrawnS Num(19,6) Applied Net SC
  BaseDocNum Int(11) Base Document Number
  BsDocDate Date(8) Base Posting Date
  BsDueDate Date(8) Base Due Date
  BsCardName nVarChar(100) Base BP Name
  BsComments nVarChar(254) Base Remarks
  Posted VarChar(1) Base Document Posted default=Y [Y=Yes, N=No]
  Vat Num(19,6) Tax LC
  VatFc Num(19,6) Tax FC
  VatSc Num(19,6) Tax SC
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  IsGross VarChar(1) Is Gross Line default=N [N=Net Line, Y=Gross Line]

# RDR1 - Sales Order - Rows
Module: Marketing Documents | 317 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  STATUS: LineStatus
  CURRENCY: Currency
  ACCOUNT: AcctCode
  BASE_ENTRY: BaseEntry, BaseType, BaseLine
  VIS_ORDER: DocEntry, VisOrder
  OWNER_CODE: OwnerCode
  ITM_WHS_OQ: ItemCode, WhsCode, OpenQty
  ITM_WHS_SH: ItemCode, WhsCode, ShipDate
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDR
  LineNum Int(11) Row Number
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=, 15=Delivery, 13=A/R Invoice, 203=A/R Down Payment]
  TrgetEntry Int(11) Target Document Internal ID
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 23=Sales Quotation]
  BaseEntry Int(11) Base Document Internal ID
  BaseLine Int(11) Base Row
  LineStatus VarChar(1) Row Status default=O [O=Open, C=Closed]
  ItemCode nVarChar(50) Item No. ->OITM
  Dscription nVarChar(200) Item/Service Description
  Quantity Num(19,6) Quantity
  ShipDate Date(8) Row Delivery Date
  OpenQty Num(19,6) Remaining Open Quantity
  Price Num(19,6) Price after Discount
  Currency nVarChar(3) Price Currency ->OCRN
  Rate Num(19,6) Currency Rate
  DiscPrcnt Num(19,6) Discount % per Row
  LineTotal Num(19,6) Row Total
  TotalFrgn Num(19,6) Row Total (FC)
  OpenSum Num(19,6) Open Amount
  OpenSumFC Num(19,6) Open Amount (FC)
  VendorNum nVarChar(50) Vendor Catalog No.
  SerialNum nVarChar(17) Serial Number
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  SlpCode Int(11) Sales Employee Code default=-1 ->OSLP
  Commission Num(19,6) Commission Percentage
  TreeType VarChar(1) BOM Type default=N [N=Not a BOM, A=Assembly, S=Sales, I=Sales BOM Component, P=Production, T=Template]
  AcctCode nVarChar(15) Account Code ->OACT
  TaxStatus VarChar(1) Tax Definition [Y=Yes, N=No]
  GrossBuyPr Num(19,6) Gross Profit Base Price
  PriceBefDi Num(19,6) Unit Price
  DocDate Date(8) Posting Date
  Flags Int(11) Flags default=0
  OpenCreQty Num(19,6) Credit Memo Amount
  UseBaseUn VarChar(1) Inventory UoM default=N [Y=Yes, N=No]
  SubCatNum nVarChar(50) BP Catalog No. ->OSCN
  BaseCard nVarChar(15) Base BP Code ->OCRD
  TotalSumSy Num(19,6) Row Total (SC)
  OpenSumSys Num(19,6) Open Amount (SC)
  InvntSttus VarChar(1) Whse Status default=O [O=Open, C=Closed]
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  CodeBars nVarChar(254) Bar Code
  VatPrcnt Num(19,6) Tax Rate per Row
  VatGroup nVarChar(8) Tax Definition ->OVTG
  PriceAfVAT Num(19,6) Gross Price after Discount
  Height1 Num(19,6) Height 1
  Hght1Unit Int(6) Unit of Height 1
  Height2 Num(19,6) Height 2
  Hght2Unit Int(6) Unit of Height 2
  Width1 Num(19,6) Width 1
  Wdth1Unit Int(6) Unit of Width 1
  Width2 Num(19,6) Width 2
  Wdth2Unit Int(6) Unit of Width 2
  Length1 Num(19,6) Length 1
  Len1Unit Int(6) Unit of Length 1
  length2 Num(19,6) Length 2
  Len2Unit Int(6) Unit of Length 2
  Volume Num(19,6) Volume
  VolUnit Int(6) Vol. Unit
  Weight1 Num(19,6) Weight 1
  Wght1Unit Int(6) Unit of Weight 1
  Weight2 Num(19,6) Weight 2
  Wght2Unit Int(6) Unit of Weight 2
  Factor1 Num(19,6) Factor 1
  Factor2 Num(19,6) Factor 2
  Factor3 Num(19,6) Factor 3
  Factor4 Num(19,6) Factor 4
  PackQty Num(19,6) Packing Quantity
  UpdInvntry VarChar(1) Whse Update default=Y [Y=Yes, N=No]
  BaseDocNum Int(11) Base Document No.
  BaseAtCard nVarChar(100) Customer/Vendor Base Document
  SWW nVarChar(16) Additional Identifier
  VatSum Num(19,6) Total Tax - Row
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  FinncPriod Int(11) Posting Period ->OFPR
  ObjType nVarChar(20) Object Type default=17 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BlockNum nVarChar(100) Block Number
  ImportLog nVarChar(20) Import Log
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAqcuistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  DistribSum Num(19,6) Distributed Amount
  DstrbSumFC Num(19,6) Distributed Amount (FC)
  DstrbSumSC Num(19,6) Distributed Amount (SC)
  GrssProfit Num(19,6) Row Gross Profit
  GrssProfSC Num(19,6) Row Gross Profit (SC)
  GrssProfFC Num(19,6) Row Gross Profit (FC)
  VisOrder Int(11) Visual Order
  INMPrice Num(19,6) Item's Last Sales Price (OINM)
  PoTrgNum Int(11) PO Target No.
  PoTrgEntry nVarChar(11) PO Target Internal ID
  DropShip VarChar(1) Drop-Ship default=N [Y=Yes, N=No]
  PoLineNum Int(11) PO Target Row No.
  Address nVarChar(254) Address
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type [Y=Regular Tax, N=No Tax, U=Use Tax]
  OrigItem nVarChar(50) Original Item ->OITM
  BackOrdr VarChar(1) Allow Backorder [Y=Yes, N=No]
  FreeTxt nVarChar(100) Free Text
  PickStatus VarChar(1) Pick Status default=N [Y=Picked, N=Not Picked, R=Release for Picking, P=Partially Picked]
  PickOty Num(19,6) Pick Quantity
  PickIdNo Int(11) Pick ID
  TrnsCode Int(6) Shipping Method default=-1 ->OSHP
  VatAppld Num(19,6) Applied Tax
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  BaseQty Num(19,6) Base Quantity
  BaseOpnQty Num(19,6) Base Open Quantity
  VatDscntPr Num(19,6) Tax Discount %
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  DeferrTax VarChar(1) Deferred Tax default=N [Y=Yes, N=No]
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatlF Num(19,6) Net Tax Amount (FC)
  LineVatS Num(19,6) Net Tax Amount (SC)
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value
  CEECFlag VarChar(1) Correction Invoice Item W/S default=S [W=Was, S=Should be]
  ToStock Num(19,6) Corr. Invoice Amount to Inventory Acct
  ToDiff Num(19,6) Corr. Invoice Amount to Diff.
  ExciseAmt Num(19,6) Excise Amount
  TaxPerUnit Num(19,6) Tax per Unit
  TotInclTax Num(19,6) Total (incl. Tax)
  CountryOrg nVarChar(3) Country/Region of Origin
  StckDstSum Num(19,6) Stock Distribute Sum
  ReleasQtty Num(19,6) Released Quantity
  LineType VarChar(1) Row Type default=R [R=Regular]
  TranType VarChar(1) Transaction Type [C=Complete, R=Reject]
  Text Text(16) Text
  OwnerCode Int(11) Document Owner
  StockPrice Num(19,6) Item Cost
  ConsumeFCT VarChar(1) Consumer Sales Forecast [Y=Yes, N=No]
  LstByDsSum Num(19,6) Last Buy Distribute Sum
  StckINMPr Num(19,6) Stock Inm Price
  LstBINMPr Num(19,6) Last Buy Inm Price
  StckDstFc Num(19,6) Stock Distribute Sum Foreign
  StckDstSc Num(19,6) Stock Distributed Sum System
  LstByDsFc Num(19,6) Last Buy Distribute Sum (FC)
  LstByDsSc Num(19,6) Last Buy Distribute Sum SC
  StockSum Num(19,6) Stock Sum
  StockSumFc Num(19,6) Stock Sum FC
  StockSumSc Num(19,6) Stock Sum SC
  StckSumApp Num(19,6) Stock Sum Applied
  StckAppFc Num(19,6) Stock Sum Applied FC
  StckAppSc Num(19,6) Stock Sum Applied SC
  ShipToCode nVarChar(50) Ship-to Code
  ShipToDesc nVarChar(254) Ship-to Description
  StckAppD Num(19,6) Stock Distribution Applied Sum
  StckAppDFC Num(19,6) Stock Distribution Applied Sum
  StckAppDSC Num(19,6) Stock Distribution Applied Sum
  BasePrice VarChar(1) Price for Total Calculation default=E [E=Exclude Tax, I=Include Tax]
  GTotal Num(19,6) Gross Total
  GTotalFC Num(19,6) Gross Total FC
  GTotalSC Num(19,6) Gross Total SC
  DistribExp VarChar(1) Distribute Freight Charges [Y=Yes, N=No]
  DescOW VarChar(1) DESC_OVERWRITTEN default=N [Y=Yes, N=No]
  DetailsOW VarChar(1) DETAILS_OVERWRITTEN default=N [Y=Yes, N=No]
  GrossBase Int(6) Base Method for Gross Profit
  VatWoDpm Num(19,6) Tax Before DPM Applied
  VatWoDpmFc Num(19,6) Tax Before DPM Applied FC
  VatWoDpmSc Num(19,6) Tax Before DPM Applied SC
  CFOPCode nVarChar(6) CFOP Code for Document ->OCFP
  CSTCode nVarChar(6) CST Code for ICMS
  Usage Int(11) Usage Code for Document ->OUSG
  TaxOnly VarChar(1) Tax Only [Y=Yes, N=No]
  WtCalced VarChar(1) WTax Calculated default=N [N=No, Y=Yes]
  QtyToShip Num(19,6) Quantity to Ship
  DelivrdQty Num(19,6) Delivered Quantity
  OrderedQty Num(19,6) Ordered Quantity
  CogsOcrCod nVarChar(8) COGS Distribution Rule Code ->OOCR
  CiOppLineN Int(11) Line Number of Opposite Line default=-1
  CogsAcct nVarChar(15) COGS Account Code ->OACT
  ChgAsmBoMW VarChar(1) Change Whs for Asm BoM Child [Y=Yes, N=No]
  ActDelDate Date(8) Actual Delivery Date
  OcrCode2 nVarChar(8) Costing Code 2 ->OOCR
  OcrCode3 nVarChar(8) Costing Code 3 ->OOCR
  OcrCode4 nVarChar(8) Costing Code 4 ->OOCR
  OcrCode5 nVarChar(8) Costing Code 5 ->OOCR
  TaxDistSum Num(19,6) Tax Distributed Amount
  TaxDistSFC Num(19,6) Tax Distributed Amount (FC)
  TaxDistSSC Num(19,6) Tax Distributed Amount (SC)
  PostTax VarChar(1) Post Tax in Price to Stock default=Y [Y=Yes, N=No]
  Excisable VarChar(1) Excisable [Yes/No] [Y=Yes, N=No]
  AssblValue Num(19,6) Assessable Value
  RG23APart1 Int(11) RG23A Part1 Number
  RG23APart2 Int(11) RG23A Part2 Number
  RG23CPart1 Int(11) RG23C Part1 Number
  RG23CPart2 Int(11) RG23C Part2 Number
  CogsOcrCo2 nVarChar(8) COGS Distribution Rule Code2 ->OOCR
  CogsOcrCo3 nVarChar(8) COGS Distribution Rule Code3 ->OOCR
  CogsOcrCo4 nVarChar(8) COGS Distribution Rule Code4 ->OOCR
  CogsOcrCo5 nVarChar(8) COGS Distribution Rule Code5 ->OOCR
  LnExcised VarChar(1) Line Excised [O=Open, C=Closed, P=Copied to OEI]
  LocCode Int(11) Location Code ->OLCT
  StockValue Num(19,6) Total COGS Value
  GPTtlBasPr Num(19,6) Total Base Price for Profit
  unitMsr2 nVarChar(100) Pur/Sal UoM if BaseUnit
  NumPerMsr2 Num(19,6) Pur/Sal UoM Value if Base Unit
  SpecPrice VarChar(1) Price Source Type default=N [Y=Special Prices for Business Partner, N=Manual, W=Active Price List, Discount Groups, R=Active Price List, U=Inactive Price List, A=Blanket Agreement, P=Period and Volume Discounts, Q=Period and Volume Discounts, Discount Groups, V=Inactive Price List, Discount Groups, 9=Special Prices for Business Partner, !=Blanket Agreement, 0=Period and Volume Discounts, 1=Period and Volume Discounts, Discount Groups, 2=Active Price List, 7=Active Price List, Discount Groups, 5=Inactive Price List, 6=Inactive Price List, Discount Groups]
  CSTfIPI nVarChar(2) CST for IPI Code
  CSTfPIS nVarChar(2) CST for PIS Code
  CSTfCOFINS nVarChar(2) CST for COFINS Code
  ExLineNo nVarChar(10) ExLineNo
  isSrvCall VarChar(1) Created from Service Call default=N [Y=Yes, N=No]
  PQTReqQty Num(19,6) Pur Quotation: Required Qty
  PQTReqDate Date(8) Pur Quotation: Required Date
  PcDocType Int(11) Purchase Confirmation Doc Type default=-1 [-1=No Type, 22=Purchase Order, 540000006=Purchase Quotation]
  PcQuantity Num(19,6) Purchase Confirmation Quantity
  LinManClsd VarChar(1) Line Was Closed Manually default=N [Y=Yes, N=No, U=Unknown]
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  NoInvtryMv VarChar(1) Without Inventory Movement default=N [Y=Yes, N=No]
  ActBaseEnt Int(11) Actual Base Document Entry
  ActBaseLn Int(11) Actual Base Line Number
  ActBaseNum Int(11) Actual Base Document No.
  OpenRtnQty Num(19,6) Quantity Open for Return
  AgrNo Int(11) Agreement No. ->OOAT
  AgrLnNum Int(11) Agreement Row Number
  CredOrigin VarChar(1) Credit Origin ->OBSI
  Surpluses Num(19,6) Surpluses
  DefBreak Num(19,6) Defect and Breakup
  Shortages Num(19,6) Shortages
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  UomEntry2 Int(11) UoM Entry if Base Unit default=0 ->OUOM
  UomCode nVarChar(20) UoM Code
  UomCode2 nVarChar(20) UoM Code if Base Unit
  FromWhsCod nVarChar(8) From Warehouse Code ->OWHS
  NeedQty VarChar(1) Consider Quantity of Items default=N [Y=Yes, N=No]
  PartRetire VarChar(1) Partial Retirement default=N [Y=Yes, N=No]
  RetireQty Num(19,6) Retirement Quantity
  RetireAPC Num(19,6) Retirement APC
  RetirAPCFC Num(19,6) Retirement APC FC
  RetirAPCSC Num(19,6) Retirement APC SC
  InvQty Num(19,6) Quantity - Inventory UoM
  OpenInvQty Num(19,6) Open Quantity (Inventory UoM)
  EnSetCost VarChar(1) Enable Set Item Cost in Return default=N [Y=Yes, N=No]
  RetCost Num(19,6) Return Cost in A/R Return
  Incoterms Int(11) Incoterms default=0 ->ODCI
  TransMod Int(11) Transport Mode default=0 ->ODCI
  LineVendor nVarChar(15) Line Vendor Code ->OCRD
  DistribIS VarChar(1) Distribute Intrastat Freight default=N [Y=Yes, N=No]
  ISDistrb Num(19,6) Intrastat Distrib. Amount
  ISDistrbFC Num(19,6) Intrastat Distrib. Amount (FC)
  ISDistrbSC Num(19,6) Intrastat Distrib. Amount (SC)
  IsByPrdct VarChar(1) Item Is By-Product default=N [N=No, Y=Yes]
  ItemType Int(11) Item Type default=4 [4=Item]
  PriceEdit VarChar(1) Price Was Edited by User default=N [N=No, Y=Yes]
  PrntLnNum Int(11) Parent Line Number
  LinePoPrss VarChar(1) Line PO Process default=N [Y=Yes, N=No]
  FreeChrgBP VarChar(1) Free of Charge (BP) default=N [Y=Yes, N=No]
  TaxRelev VarChar(1) Tax Relevant Row default=Y [Y=Yes, N=No]
  LegalText nVarChar(254) Legal Text
  ThirdParty VarChar(1) Third Party default=N [Y=Yes, N=No]
  LicTradNum nVarChar(32) Federal Tax ID
  InvQtyOnly VarChar(1) Change Qty (Inv. UoM) Only default=N [Y=Yes, N=No]
  UnencReasn Int(11) Reason for Unencumbered ICMS
  ShipFromCo nVarChar(50) Ship-From Code
  ShipFromDe nVarChar(254) Ship-From Description
  FisrtBin nVarChar(228) First Bin Location
  AllocBinC nVarChar(11) Allocated Bin Location Count
  ExpType nVarChar(4) Expense Type ->OEXD
  ExpUUID nVarChar(50) Expense UUID
  ExpOpType VarChar(1) Expense Operation Type [P=Professional Services, R=Renting Assets, O=Others]
  DIOTNat nVarChar(3) DIOT Nationality ->OCRY
  MYFtype nVarChar(2) MYF type [S1=MYF Wholesale Sales, S2=Retail Sales, P1=MYF Wholesale Purchases, P3=Other Expense Transactions]
  GPBefDisc Num(19,6) Gross Price
  ReturnRsn Int(6) Return Reason default=-1
  ReturnAct Int(6) Return Action default=-1
  StgSeqNum Int(11) Stage Sequence Number
  StgEntry Int(11) Stage Entry ->ORST
  StgDesc nVarChar(100) Stage Description
  ItmTaxType nVarChar(2) Item GST Tax Category [GR=GST Regular, GN=GST Nil Rated, GE=GST Exempt, NE=Excisable, NN=Non-GST Non-Excisable]
  SacEntry Int(11) SAC Entry ->OSAC
  NCMCode Int(11) NCM Code default=-1 ->ONCM
  HsnEntry Int(11) HSN Entry
  OriBAbsEnt Int(11) Original Base Document Internal ID
  OriBLinNum Int(11) Original Base Document Line Number
  OriBDocTyp Int(11) Original Base Document Type
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No, U=Use]
  EncryptIV nVarChar(100) Encrypt IV
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  StdItemId Int(11) Standard Item Identification ->OUNCL
  CommClass Int(11) Commodity Classification ->OUNCL
  VatExEntry Int(11) VAT Exemption AbsEntry ->OVEB
  VatExLN Int(6) VAT Exemption LineNum
  NatOfTrans Int(11) Nature of Transaction ->ODCI
  ISDtCryImp nVarChar(3) Destination Country/Region for Import ->OCRY
  ISDtRgnImp Int(11) Destination Region for Import ->ODCI
  ISOrCryExp nVarChar(3) Country/Region of Origin for Export ->OCRY
  ISOrRgnExp Int(11) Region of Origin for Export ->ODCI
  NVECode nVarChar(6) NVE Code
  PoNum nVarChar(20) Customer's Purchase Order Number
  PoItmNum Int(11) Customer's Purchase Order Item Number
  IndEscala VarChar(1) Indicator for Relevant Scale default=N [Y=Yes, N=No]
  CESTCode Int(11) CEST Code ->OCEST
  CtrSealQty Num(19,6) Control Seal Quantity
  CNJPMan nVarChar(14) CNPJ of Manufacturer
  UFFiscBene nVarChar(10) UF Fiscal Benefit Code
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]
  LegalTIMD nVarChar(250) Legal Text from Item Master Data
  LegalTTCA nVarChar(250) Legal Text from Tax Code Attributes
  LegalTW nVarChar(250) Legal Text from Warehouse
  LegalTCD nVarChar(250) Legal Text from Tax Code Determination
  RevCharge VarChar(1) Reverse Charge default=N [Y=Yes, N=No]
  ListNum Int(6) Price List No. ->OPLN

# RDR10 - Sales Order - Row Structure
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SECONDARY U: DocEntry, AftLineNum, OrderNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDR
  LineSeq Int(11) Row Sequence
  AftLineNum Int(11) After Row Number
  OrderNum Int(11) Order Number
  LineType VarChar(1) Row Type [T=Text, S=Subtotal]
  LineText Text(16) Row Text
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=17 ->ADP1

# RDR11 - Sls Ord. - Drawn Dpm Detail
Module: Marketing Documents | 70 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LineSeq
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDR
  LineNum Int(11) Row Number
  LineSeq Int(11) Sequence Number
  BaseAbs Int(11) Base Document Internal ID
  BaseType Int(11) Base Object Type default=-1 [-1=]
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  VatPrcnt Num(19,6) VAT Percent
  LineTotal Num(19,6) Net LC
  TotalFrgn Num(19,6) Net FC
  TotalSumSy Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFrgn Num(19,6) Tax FC
  VatSumSys Num(19,6) Tax SC
  ObjType nVarChar(20) Object Type default=17 ->ADP1
  LogInstanc Int(11) Log Instance
  IsAcq VarChar(1) Acquisition Tax-Liable default=N [N=No, Y=Yes]
  IsAllDrawn VarChar(1) Remaining Amount Drawn default=N [Y=Yes, N=No]
  IsGross VarChar(1) Is Gross Line default=N [N=Net Line, Y=Gross Line]
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  ApplNet Num(19,6) Applied Net LC
  ApplNetFc Num(19,6) Applied Net FC
  ApplNetSc Num(19,6) Applied Net SC
  ApplVat Num(19,6) Applied Tax LC
  ApplVatFc Num(19,6) Applied Tax FC
  ApplVatSc Num(19,6) Applied Tax SC
  BaseNet Num(19,6) Base Net LC
  BaseNetFc Num(19,6) Base Net FC
  BaseNetSc Num(19,6) Base Net SC
  BaseVat Num(19,6) Base Tax LC
  BaseVatFc Num(19,6) Base Tax FC
  BaseVatSc Num(19,6) Base Tax SC
  BaseGross Num(19,6) Base Gross LC
  BaseGrossF Num(19,6) Base Gross FC
  BaseGrossS Num(19,6) Base Gross SC
  LineType VarChar(1) Line Type default=D [D=Document Row, R=Currency Rounding, H=Down Payment Document Rounding]
  DctSum Num(19,6) Deductible Sum LC
  DctSumFc Num(19,6) Deductible Sum FC
  DctSumSc Num(19,6) Deductible Sum SC
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplDct Num(19,6) Applied Deductible Sum LC
  ApplDctFc Num(19,6) Applied Deductible Sum FC
  ApplDctSc Num(19,6) Applied Deductible Sum SC
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  BaseDct Num(19,6) Base Deductible Sum LC
  BaseDctFc Num(19,6) Base Deductible Sum FC
  BaseDctSc Num(19,6) Base Deductible Sum SC
  BaseEq Num(19,6) Base Equalization Sum LC
  BaseEqFc Num(19,6) Base Equalization Sum FC
  BaseEqSc Num(19,6) Base Equalization Sum SC
  TaxCode nVarChar(8) Tax Code ->OSTC
  ApplGross Num(19,6) Applied Gross LC
  ApplGrossF Num(19,6) Applied Gross FC
  ApplGrossS Num(19,6) Applied Gross SC
  TaxAdjust VarChar(1) Manual Tax Adjustment default=N [Y=Yes, N=No]
  RvsChrgSum Num(19,6) Reverse Charge Sum LC
  RvsChrgFc Num(19,6) Reverse Charge Sum FC
  RvsChrgSc Num(19,6) Reverse Charge Sum SC
  BasRvsChrg Num(19,6) Base Reverse Charge LC
  BasRvsFc Num(19,6) Base Reverse Charge FC
  BasRvsSc Num(19,6) Base Reverse Charge SC
  ApplRvs Num(19,6) Applied Reverse Charge LC
  ApplRvsFc Num(19,6) Applied Reverse Charge FC
  ApplRvsSc Num(19,6) Applied Reverse Charge SC
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# RDR12 - Sales Order - Tax Extension
Module: Marketing Documents | 117 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDR
  TaxId0 nVarChar(100) Tax ID 0
  TaxId1 nVarChar(100) Tax ID 1
  TaxId2 nVarChar(100) Tax ID 2
  TaxId3 nVarChar(100) Tax ID 3
  TaxId4 nVarChar(100) Tax ID 4
  TaxId5 nVarChar(100) Tax ID 5
  TaxId6 nVarChar(100) Tax ID 6
  TaxId7 nVarChar(100) Tax ID 7
  TaxId8 nVarChar(100) Tax ID 8
  TaxId9 nVarChar(100) Tax ID 9
  State nVarChar(3) State Code
  County nVarChar(7) County Code
  Incoterms nVarChar(3) Incoterms
  Vehicle nVarChar(10) Vehicle ID
  VidState nVarChar(3) Vehicle ID (State)
  NfRef nVarChar(254) Nota Fiscal Reference
  Carrier nVarChar(15) Carrier Code
  QoP Int(11) Quantity of Packs
  PackDesc nVarChar(10) Pack Description
  Brand nVarChar(20) Brand
  NoSU Int(11) Number of Shipping Unit
  NetWeight Num(19,6) Net Weight
  GrsWeight Num(19,6) Gross Weight
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=17 ->ADP1
  TaxId10 nVarChar(100) Tax ID 10
  TransCat nVarChar(100) Transaction Category
  FormNo nVarChar(100) Form No.
  TaxId11 nVarChar(100) Tax ID 11
  StreetS nVarChar(100) Street
  BlockS nVarChar(100) Block
  BuildingS Text(16) Building/Floor/Room
  CityS nVarChar(100) City
  ZipCodeS nVarChar(20) Zip Code
  CountyS nVarChar(100) County
  StateS nVarChar(3) State ->OCST
  CountryS nVarChar(3) Country/Region ->OCRY
  AddrTypeS nVarChar(100) Address Type
  StreetNoS nVarChar(100) Street No.
  StreetB nVarChar(100) Street
  BlockB nVarChar(100) Block
  BuildingB Text(16) Building/Floor/Room
  CityB nVarChar(100) City
  ZipCodeB nVarChar(20) Zip Code
  CountyB nVarChar(100) County
  StateB nVarChar(3) State ->OCST
  CountryB nVarChar(3) Country/Region ->OCRY
  AddrTypeB nVarChar(100) Address Type
  StreetNoB nVarChar(100) Street No.
  ImpORExp VarChar(1) Import or Export [N=, Y=]
  Vat VarChar(1) VAT default=N [N=No VAT Support, Y=VAT Support]
  AltCrdNamB nVarChar(100) Alternative BP Name
  AltTaxIdB nVarChar(32) Alternative Tax ID
  Address2S nVarChar(50) Address Name 2
  Address3S nVarChar(50) Address Name 3
  Address2B nVarChar(50) Address Name 2
  Address3B nVarChar(50) Address Name 3
  MainUsage Int(11) Main Usage Code of Document ->OUSG
  GlbLocNumS nVarChar(50) Global Location Number
  GlbLocNumB nVarChar(50) Global Location Number
  CollectDT nVarChar(20) Date and Time of Collection
  TransprtDT Date(8) Transport Starting Date
  TransprtRS nVarChar(100) Transport Reason
  TaxId12 nVarChar(50) Tax ID 12
  TaxId13 nVarChar(100) Deductee Ref. No. in India
  ImpExpNo nVarChar(100) Import/Export Bill No.
  ImpExpDate Date(8) Import/Export Date
  BpGSTType Int(11) GST Regn Type of BP
  BpGSTN nVarChar(15) GST Regn No of BP
  BpStateCod nVarChar(3) State Code of Business Partner ->OCST
  BPStatGSTN nVarChar(2) GST State Code of BP
  LocGSTType Int(11) GST Regn Type of Location
  LocGSTN nVarChar(15) GST Regn No of Location
  LocStatCod nVarChar(3) State Code of Location ->OCST
  LocStaGSTN nVarChar(2) GST State Code of Location
  BpCountry nVarChar(3) Country/Region Code of BP ->OCRY
  OrigImpNo nVarChar(100) Original Bill of Entry No.
  OrigImpDat Date(8) Original Bill of Entry Date
  ExportType VarChar(1) Exporting Type default=E [E=Imports/Exports, S=SEZ Developer, U=SEZ Unit, D=Deemed Imports/Exports]
  PortCode nVarChar(100) Port Code
  BoEValue Num(19,6) Bill of Entry Value
  IsIGSTAct VarChar(1) Supply under IGST Account [Y=Yes, N=No]
  ClaimRefun VarChar(1) Claim Refund [Y=Yes, N=No]
  TaxRateDif Int(11) Differential % of Tax Rate [65=, 100=]
  BPGdsIssP nVarChar(15) Goods Issue Place BP
  CNPJGIP nVarChar(100) Goods Issue Place CNPJ
  CPFGIP nVarChar(100) Goods Issue Place CPF
  StreetGIP nVarChar(100) Goods Issue Place Street
  StrtNoGIP nVarChar(100) Goods Issue Place Street No.
  BldngGIP Text(16) Goods Issue Place Building
  ZipGIP nVarChar(20) Goods Issue Place Zip Code
  BlockGIP nVarChar(100) Goods Issue Place Block
  CityGIP nVarChar(100) Goods Issue Place City
  CountyGIP nVarChar(100) Goods Issue Place County
  StateGIP nVarChar(3) Goods Issue Place State ->OCST
  CountryGIP nVarChar(3) Goods Issue Place Country/Region ->OCRY
  PhoneGIP nVarChar(20) Goods Issue Place Phone
  EMailGIP nVarChar(100) Goods Issue Place E-Mail
  DptDateGIP Date(8) Goods Issue Place Departure Date
  BPDelivryP nVarChar(15) Delivery Place BP
  CNPJDlvryP nVarChar(100) Delivery Place CNPJ
  CPFDlvryP nVarChar(100) Delivery Place CPF
  StrtDlvryP nVarChar(100) Delivery Place Street
  StrNoDlvrP nVarChar(100) Delivery Place Street No.
  BldDlvryP Text(16) Delivery Place Building
  ZipDlvryP nVarChar(20) Delivery Place Zip Code
  BlckDlvryP nVarChar(100) Delivery Place Block
  CityDlvryP nVarChar(100) Delivery Place City
  CntyDlvryP nVarChar(100) Delivery Place County
  StatDlvryP nVarChar(3) Delivery Place State ->OCST
  CtryDlvryP nVarChar(3) Delivery Place Country/Region ->OCRY
  FoneDlvryP nVarChar(20) Delivery Place Phone
  MailDlvryP nVarChar(100) Delivery Place E-Mail
  DpDtDlvryP Date(8) Delivery Place Departure Date
  AuthedCNPJ nVarChar(250) Authorized CNPJ or CPF
  TaxId14 nVarChar(250) ITR Filing

# RDR13 - Sales Order Rows - Distributed Expenses
Module: Marketing Documents | 59 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDR
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=17 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Aquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Normal Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) VAT Applied Frgn
  VatAppldSC Num(19,6) VAT Applied Sys
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock default=N [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Line No.
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Abs. Entry default=-1
  BaseGroup Int(11) Base Document Group default=-1
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1
  VisOrder Int(11) Visual Order
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DistribExp VarChar(1) Distribute Freights [Y=Yes, N=No]
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ

# RDR14 - Sales Order - Assembly - Rows
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDR
  LineNum Int(11) Row Number default=-1
  ChildNum Int(11) Child Number default=-1
  ItemCode nVarChar(50) Item no. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  TotalQty Num(19,6) Total Quantity
  OpenQty Num(19,6) Remaining Open Quantity
  ObjectType nVarChar(20) object type default=17 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BaseChildN Int(11) Base Child Number default=-1
  EncryptIV nVarChar(100) Encrypt IV

# RDR15 - Sls Ord. - Drawn Dpm Applied
Module: Marketing Documents | 84 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDR
  LineNum Int(11) Row Number
  ObjType nVarChar(20) object type default=17 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  StaCode nVarChar(8) Tax Authority Code
  StaType Int(11) Tax Authority Type
  StaIndex Int(11) Tax Authority Seq Index
  BaseNet Num(19,6) Net LC
  BaseNetFc Num(19,6) Net FC
  BaseNetSc Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFc Num(19,6) Tax FC
  VatSumSc Num(19,6) Tax SC
  DctSum Num(19,6) Deductible Sum LC
  DctSumFc Num(19,6) Deductible Sum FC
  DctSumSc Num(19,6) Deductible Sum SC
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplNet Num(19,6) Applied Net LC
  ApplNetFc Num(19,6) Applied Net FC
  ApplNetSc Num(19,6) Applied Net SC
  ApplVat Num(19,6) Applied Tax LC
  ApplVatFc Num(19,6) Applied Tax FC
  ApplVatSc Num(19,6) Applied Tax SC
  ApplDct Num(19,6) Applied Deductible Sum LC
  ApplDctFc Num(19,6) Applied Deductible Sum FC
  ApplDctSc Num(19,6) Applied Deductible Sum SC
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  PaidNet Num(19,6) Paid Net LC
  PaidNetFc Num(19,6) Paid Net FC
  PaidNetSc Num(19,6) Paid Net SC
  PaidVat Num(19,6) Paid Tax LC
  PaidVatFc Num(19,6) Paid Tax FC
  PaidVatSc Num(19,6) Paid Tax SC
  PaidDct Num(19,6) Paid Deductible Sum LC
  PaidDctFc Num(19,6) Paid Deductible Sum FC
  PaidDctSc Num(19,6) Paid Deductible Sum SC
  PaidEq Num(19,6) Paid Equalization Sum LC
  PaidEqFc Num(19,6) Paid Equalization Sum FC
  PaidEqSc Num(19,6) Paid Equalization Sum SC
  DpApplNet Num(19,6) Dpm Appl Net LC
  DpApplNetF Num(19,6) Dpm Appl Net FC
  DpApplNetS Num(19,6) Dpm Appl Net SC
  DpApplVat Num(19,6) Dpm Appl Tax LC
  DpApplVatF Num(19,6) Dpm Appl Tax FC
  DpApplVatS Num(19,6) Dpm Appl Tax SC
  DpApplDct Num(19,6) Dpm Appl Deductible Sum LC
  DpApplDctF Num(19,6) Dpm Appl Deductible Sum FC
  DpApplDctS Num(19,6) Dpm Appl Deductible Sum SC
  DpApplEq Num(19,6) Dpm Appl Equalization Sum LC
  DpApplEqFc Num(19,6) Dpm Appl Equalization Sum FC
  DpApplEqSc Num(19,6) Dpm Appl Equalization Sum SC
  TaxCode nVarChar(8) Tax Code ->OSTC
  LineType VarChar(1) Row Type default=D [D=Document, R=Exchange Rate Rounding, H=Document Header Rounding]
  BaseGrs Num(19,6) Gross LC
  BaseGrsFc Num(19,6) Gross FC
  BaseGrsSc Num(19,6) Gross SC
  ApplGrs Num(19,6) Applied Gross LC
  ApplGrsFc Num(19,6) Applied Gross FC
  ApplGrsSc Num(19,6) Applied Gross SC
  PaidGrs Num(19,6) Paid Gross LC
  PaidGrsFc Num(19,6) Paid Gross FC
  PaidGrsSc Num(19,6) Paid Gross SC
  DpApplGrs Num(19,6) Dpm Appl Gross LC
  DpApplGrsF Num(19,6) Dpm Appl Gross FC
  DpApplGrsS Num(19,6) Dpm Appl Gross SC
  RvsChrgSum Num(19,6) Reverse Charge Sum
  RvsChrgSc Num(19,6) Reverse Charge Sum (SC)
  RvsChrgFc Num(19,6) Reverse Charge Sum (FC)
  ApplRvs Num(19,6) Applied Reverse Charge Sum LC
  ApplRvsSc Num(19,6) Applied Reverse Charge Sum SC
  ApplRvsFc Num(19,6) Applied Reverse Charge Sum FC
  PaidRvs Num(19,6) Paid Reverse Charge Sum LC
  PaidRvsSc Num(19,6) Paid Reverse Charge Sum SC
  PaidRvsFc Num(19,6) Paid Reverse Charge Sum FC
  DpApplRvs Num(19,6) Dpm Applied Reverse Charge LC
  DpApplRvsS Num(19,6) Dpm Applied Reverse Charge SC
  DpApplRvsF Num(19,6) Dpm Applied Reverse Charge FC
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# RDR16 - Sales Order - SnB properties
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, SnBIndex
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) abs entry ->ORDR
  LineNum Int(11) Line Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object id
  ObjAbs Int(11) Object Abs
  DrfWObjAbs Int(11) draft Wobj Abs default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type default=17
  LogInstanc Int(11) Log Instance

# RDR17 - Sales Order - Import Process
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDR
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=17 ->ADP1
  ImpDocType VarChar(1) Type of Importation Document ->OBSI
  ImpDocNum nVarChar(10) Importation Document Number
  DateOfReg Date(8) Date of Registry DI/DSI/DA
  CustClrDat Date(8) Date of Customs Clearance
  ConcActNum nVarChar(30) Drawback Concession Acct No.
  AdditNum nVarChar(30) Additional Number
  AddItmDV Num(19,6) Additional Item Discount Value
  tpVTransp Int(6) Overland Transport Route [1=Maritime, 2=Waterway, 3=Lakeside, 4=Air, 5=Post, 6=Train, 7=Road, 8=Network Transmission, 9=Own Means, 10=Input/Output Fictitious, 11=Courier, 12=Hand Carry]
  DrawSReg nVarChar(11) Drawback - Suspension Regime
  AddFrNavyA Num(19,6) Additional Freight to Navy Authority
  TypeOfImp VarChar(1) Type of Import
  nSeqAdic Int(6) Additional Item Sequential Number

# RDR18 - Sales Order - Export Process
Module: Marketing Documents | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDR
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=17 ->ADP1
  ExpDocType Int(11) Type of Exportation Document default=-1 ->OBNI
  ExpDeclNum Int(11) Exportation Declaration Number
  ExpDeclDat Date(8) Exportation Declaration Date
  ExpNature Int(11) Nature of Exportation default=-1 ->OBNI
  ExpRegNum Int(11) Number of Exportation Registry
  ExpRegDate Date(8) Date of Exportation Registry
  LadBillNum nVarChar(19) Bill of Lading Number
  LadBillDat Date(8) Date of Bill of Lading
  MerchLeftD Date(8) Date Merchandise Left Customs
  LadBillTyp Int(11) Type of Bill of Lading default=-1 ->OBNI
  DrawSReg nVarChar(11) Drawback - Suspension Regime
  NatureExp nVarChar(44) Nature of Export
  QultExpItm Num(19,6) Quantity of Exported Items
  nSeqAdic Int(6) Additional Item Sequential Number

# RDR19 - Sales Order - Bin Allocation Data
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, BinAllocSe
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->ORDR
  BinAllocSe Int(11) Bin Allocation Sequence
  LineNum Int(11) Line Number
  SubLineNum Int(11) Subline Number default=-1
  SnBType Int(11) SnB Type default=-1
  SnBMDAbs Int(11) SnB Master Data Internal No. default=-1
  BinAbs Int(11) Bin Internal Number ->OBIN
  Quantity Num(19,6) Quantity
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjType nVarChar(20) Object Type default=17 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  BinActTyp Int(6) Bin Action Type [1=Transaction In, 2=Transaction Out, 4=SnB Complete, 8=Bin First Then SnB]

# RDR2 - Sales Order - Freight - Rows
Module: Marketing Documents | 64 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDR
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=17 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) Vat Applied
  VatAppldFC Num(19,6) Vat Applied Frgn
  VatAppldSC Num(19,6) Vat Applied Sys
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report [Y=Yes, N=No]
  BaseGroup Int(11) Base Document Group default=-1 [-1=, 0=, 1=, 2=]
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1 [-1=, 0=, 1=, 2=]
  VisOrder Int(11) Visual Order
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]

# RDR20 - Intrastat Expenses
Module: Marketing Documents | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDR
  ExpnsCode Int(11) Freight Code ->OEXD
  TotalLC Num(19,6) Total
  TotalFC Num(19,6) Total (FC)
  TotalSC Num(19,6) Total (SC)
  DistribM VarChar(1) Distribution Method default=T [Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DrawnLC Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  LineNum Int(11) Line Number default=-1
  BaseAbsEnt Int(11) Base Abs. Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 16=Return, 13=A/R Invoice, 203=Down Payment Incoming, 204=Down Payment Outgoing, 22=Purchase Order, 20=Goods Receipt PO, 21=Goods Return, 18=A/P Invoice, 540000006=Purchase Quotation, 0=, -1=]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No. default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=17 ->ADP1
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  AppliedLC Num(19,6) Applied
  AppliedFC Num(19,6) Applied (FC)
  AppliedSC Num(19,6) Applied (SC)

# RDR21 - Sales Order - Document Reference Information
Module: Marketing Documents | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, RefType
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjectType nVarChar(20) Object Type default=17
  LogInstanc Int(11) Log Instance default=0
  RefType VarChar(1) Reference Types default=S [S=System Document, E=External Document]
  LineNum Int(11) Line Number
  RefDocEntr Int(11) Referenced Internal Number
  RefDocNum Int(11) Referenced Document Number
  ExtDocNum nVarChar(100) External Referenced Document Number
  RefObjType nVarChar(20) Referenced Object Type [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 234000031=Return Request, 16=Return, 203=A/R Down Payment, 13=A/R Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 280=A/R Tax Invoice, 1470000113=Purchase Request, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Return Request, 21=Goods Return, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 281=A/P Tax Invoice, 69=Landed Costs, 24=Incoming Payments, 46=Outgoing Payments, 57=Checks for Payment, 321=Internal Reconciliation, 34=Recurring Posting, 30=Journal Entry, 59=Goods Receipt, 60=Goods Issue, 162=Inventory Revaluation, 1470000065=Inventory Counting, 10000071=Inventory Posting, 1250000001=Inventory Transfer Request, 67=Inventory Transfer, 202=Production Order, 13001=Original Invoice, -1=External Document, 20301=Original Down Payment Invoice]
  AccessKey nVarChar(100) Access Key
  IssueDate Date(8) Date of Issue
  IssuerCNPJ nVarChar(100) Issuer CNPJ
  IssuerCode nVarChar(10) Fiscal Document Issuer UF Code
  Model nVarChar(6) Fiscal Document Model
  Series nVarChar(3) Fiscal Document Series
  Number Int(11) Fiscal Document Number
  RefAccKey nVarChar(100) Referenced CT-e Access Key
  RefAmount Num(19,6) Referenced Amount
  SubSeries nVarChar(3) Fiscal Document Subseries
  Remark nVarChar(254) Remarks
  LinkRefTyp nVarChar(20) Link Reference Type default=00 [00=, 01=Nota de cr�dito de los documentos relacionados, 02=Nota de d�bito de los documentos relacionados, 03=Devoluci�n de mercanc�a sobre facturas o traslados previos, 04=Sustituci�n de los CFDI previos, 05=Traslados de mercancias facturados previamente, 06=Factura generada por los traslados previos, 07=CFDI por aplicaci�n de anticipo, 08=Customs, MX_08=Factura generada por pagos en parcialidades, 09=Factura generada por pagos diferidos]

# RDR22 - Sales Order - Resource Costs
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, StdCostNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->RDR1
  LineNum Int(11) Row Number ->RDR1
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=17
  LogInstanc Int(11) Log Instance default=0

# RDR23 - A/P Invoice - Selected Asset Master Data
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, VisOrder
  ASSETS: DocEntry, LineNum, AssetCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDR
  LineNum Int(11) Row Number
  AssetCode nVarChar(50) Selected Asset Code ->OITM
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Remarks nVarChar(100) Remarks
  Amount Num(19,6) Amount
  AmountSC Num(19,6) Amount (SC)
  SerialNo nVarChar(30) Serial Number
  VisOrder Int(11) Visual Order
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=17 ->ADP1

# RDR24 - Sales Order - Tracking Note Assignment
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  ItemCCDNum nVarChar(40) Item CCD Number
  CntrOrigin nVarChar(3) Country/Region of Origin
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=17 ->ADP1
  SubLineNum Int(11) BOM Line No.

# RDR25 - Sales Order - Amt Per VAT Grp
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, VatGroup, Type
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  VatGroup nVarChar(8) Tax Definition ->OVTG
  VatPrcnt Num(19,6) Tax Rate
  BaseAmnt Num(19,6) Base Amount
  BaseAmntFC Num(19,6) Base Amount (FC)
  BaseAmntSC Num(19,6) Base Amount (SC)
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  Type Int(11) Type default=1 [1=Discount by Tax]
  Currency nVarChar(3) Price Currency
  Rate Num(19,6) Currency Rate
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=17 ->ADP1

# RDR26 - Sales Order - E-Way Bill Information
Module: Marketing Documents | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDR
  SuplyType nVarChar(20) EWB Transaction Type [O=Outward, I=Inward]
  SubSplyTyp Int(11) EWB Sub-Type ->OEST
  DocType nVarChar(3) EWB Doc. Type ->OEDT
  TransMode Int(11) EWB Transportation Mode ->OETM
  Distance Num(19,6) EWB Transport Distance
  TransDocNo nVarChar(16) EWB Transporter Doc. No.
  TransDate Date(8) EWB Transportation Date
  VehicleTyp nVarChar(2) EWB Vehicle Type ->OEVT
  VehicleNo nVarChar(15) EWB Vehicle Number
  EWayBillNo nVarChar(20) EWB No.
  EwbDate Date(8) E-Way Bill Date
  FrmTraName nVarChar(100) EWB Consignor Name
  FrmAddres1 nVarChar(120) EWB Consignor Address 1
  FrmAddres2 nVarChar(120) EWB Consignor Address 2
  FrmZipCode nVarChar(20) EWB Consignor Zip Code
  ActFrmStat nVarChar(2) Dispatch State of EWB Consignor
  ToTraName nVarChar(100) EWB Consignee Name
  ToAddres1 nVarChar(120) EWB Consignee Address 1
  ToAddres2 nVarChar(120) EWB Consignee Address 2
  ToZipCode nVarChar(20) EWB Consignee Zip Code
  ActToState nVarChar(2) Ship-To State of EWB Consignee
  FrmGSTN nVarChar(15) EWB Consignor GSTN
  FrmState nVarChar(2) Bill-To State of EWB Consignor
  ToGSTN nVarChar(15) EWB Consignee GSTN
  ToState nVarChar(2) Bill-To State of EWB Consignee
  MainHsnEnt Int(11) EWB Main HSN Entry ->OCHP
  FrmPlace nVarChar(50) EWB Consignor Place
  ToPlace nVarChar(50) EWB Consignee Place
  TransID nVarChar(15) EWB Transporter ID
  TransName nVarChar(25) EWB Transporter Name
  ExpireDate Date(8) EWB Expiration Date
  ObjectType nVarChar(20) Object Type default=17 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TspEntry Int(11) Transporter Abs. Entry ->OTSP
  TspLine Int(11) Transportation Line
  TransType Int(11) Transaction Type [1=Regular, 2=Bill To-Ship To, 3=Bill From-Dispatch From, 4=Combination of 2 and 3]

# RDR27 - Sales Order - E-Books(GR) Rows
Module: Marketing Documents | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  RELATE_ROW: DocEntry, RelateType, RelateLine, GroupNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDR
  LineNum Int(11) Row Number
  RelateType Int(11) Relation Type default=-1 [1=Row, 2=Row Expenses, 3=Document Expenses, 13=Distributed Freights, -1=Manual]
  RelateLine Int(11) Relation Row Number default=-1
  GroupNum Int(11) Group Number default=-1
  LineTotal Num(19,6) Line Total
  LineTotalF Num(19,6) Line Total (FC)
  LineTotalS Num(19,6) Line Total (SC)
  InClassTyp Int(11) Income Classification Type ->OICP
  InClassCat Int(11) Income Classification Category ->OICC
  ExClassTyp Int(11) Expense Classification Type ->OECP
  ExClassCat Int(11) Expense Classification Cat. ->OECC
  VatCate Int(11) VAT Category
  NetValue Num(19,6) Net Value
  NetValueFC Num(19,6) Net Value (FC)
  NetValueSC Num(19,6) Net Value (SC)
  VatAmount Num(19,6) VAT Amount
  VatAmFC Num(19,6) VAT Amount (FC)
  VatAmSC Num(19,6) VAT Amount (SC)
  WtPercCat Int(11) Withheld Percentage Category
  WtAmount Num(19,6) Withheld Amount
  WtAmountFC Num(19,6) Withheld Amount (FC)
  WtAmountSC Num(19,6) Withheld Amount (SC)
  ObjectType nVarChar(20) Object Type default=13 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  WtCategory VarChar(1) Withheld Category [I=Invoice, P=Payment]
  VATClassTy Int(11) VAT Classification Type ->OECP
  VATClassCa Int(11) VAT Classification Category ->OECC
  EBVatExCau Int(11) VAT Exemption Cause ->OVEC

# RDR28 - Sales Order - Reported Tracking Note
Module: Marketing Documents | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
  TCN_KEY U: DocEntry, LineNum, TrackingNt, TrackiNtLn
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  UnusedQty Num(19,6) Unused Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=17 ->ADP1
  SubLineNum Int(11) BOM Line No.

# RDR3 - Sales Order - Freight
Module: Marketing Documents | 80 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  DOCUMENT: DocEntry, BaseAbsEnt
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDR
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  Comments nVarChar(100) Remarks
  ObjType nVarChar(20) Object Type default=17 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  WTLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  VatApplied Num(19,6) Vat Applied
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatF Num(19,6) Net Tax Amount (FC)
  LineVatS Num(19,6) Net Tax Amount (SC)
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 23=Sales Quotation]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No.
  LineNum Int(11) line num default=-1
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Doc. Internal No. default=-1
  StDstr Num(19,6) Stock Distributed Sum
  StDstrSC Num(19,6) Stock Distributed Sum (SC)
  StDstrFC Num(19,6) Stock Distributed Sum (FC)
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  TaxDistMtd VarChar(1) Tax Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  GrsAmount Num(19,6) Gross Amount
  GrsFC Num(19,6) Gross Amount (FC)
  GrsSC Num(19,6) Gross Amount (SC)
  BaseTotal VarChar(1) Base Total for Calculation default=N [N=Net Total, G=Gross Total]
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)
  RRVatLC Num(19,6) Return Request VAT Amount
  RRVatFC Num(19,6) Return Request VAT Amount (FC)
  RRVatSC Num(19,6) Return Request VAT Amount (SC)
  EncryptIV nVarChar(100) Encrypt IV
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]

# RDR4 - Sales Order - Tax Amount per Document
Module: Marketing Documents | 61 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SCONDARY: DocEntry, LineNum, GroupNum, ExpnsCode, StcCode, StaCode, staType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDR
  LineNum Int(11) Row Number default=-1
  GroupNum Int(11) Group Number default=-1
  ExpnsCode Int(11) Expense Code default=-1 ->OEXD
  RelateType Int(11) Relation Type default=1 [1=Row, 2=Row Freight Charges, 3=Document Expenses, 13=Distributed Freights]
  StcCode nVarChar(8) Tax Code ->OSTC
  StaCode nVarChar(8) Authority Code ->OSTA
  staType Int(11) Authority Type ->OSTT
  TaxRate Num(19,6) Tax Rate
  TaxAcct nVarChar(15) Tax Account ->OACT
  TaxSum Num(19,6) Tax Amount
  TaxSumFrgn Num(19,6) Tax Amount (FC)
  TaxSumSys Num(19,6) Tax Amount (SC)
  BaseSum Num(19,6) Base Amount
  BaseSumFrg Num(19,6) Base Amount (FC)
  BaseSumSys Num(19,6) Base Amount (SC)
  ObjectType nVarChar(20) Object Type default=17 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Status default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  LineSeq Int(11) Line Sequence
  DeferrAcct nVarChar(15) Deferred Tax Account ->OACT
  BaseType Int(11) Base Document Type default=-1
  BaseAbs Int(11) Base Doc Abs Entry default=-1
  BaseSeq Int(11) Base Doc. Line Sequence
  DeductTax Num(19,6) Deductible Tax Amount
  DdctTaxFrg Num(19,6) Deductible Tax Amount (FC)
  DdctTaxSys Num(19,6) Deductible Tax Amount (SC)
  BaseAppld Num(19,6) Applied Base Amount
  BaseApldFC Num(19,6) Applied Base Amount (FC)
  BaseApldSC Num(19,6) Applied Base Amount (SC)
  NonDdctPrc Num(19,6) Non Deductible %
  NonDdctAct nVarChar(15) Non Deductible Account ->OACT
  TaxInPrice VarChar(1) Tax Included in Price? default=N [Y=Yes, N=No]
  Exempt VarChar(1) Exempt? default=N [Y=Yes, N=No]
  TaxExpAct nVarChar(15) Expense Account for Tax ->OACT
  OnHoldTax Num(19,6) On Hold Tax Amount
  OnHoldTaxF Num(19,6) On Hold Tax Amount (FC)
  OnHoldTaxS Num(19,6) On Hold Tax Amount (SC)
  InGrossRev VarChar(1) Included in Gross Revenue default=N [Y=Yes, N=No]
  TaxSumOrg Num(19,6) Tax Amount Original
  TaxSumOrgF Num(19,6) Tax Amount Original (FC)
  TaxSumOrgS Num(19,6) Tax Amount Original (SC)
  OpenTax Num(19,6) Open Service Tax
  OpenTaxFC Num(19,6) Open Service Tax (FC)
  OpenTaxSC Num(19,6) Open Service Tax (SC)
  Unencumbrd VarChar(1) Unencumbered default=N [Y=Yes, N=No]
  TaxOnRI VarChar(1) Tax On Reserve Invoice default=N [Y=Yes, N=No]
  RvsChrgPrc Num(19,6) Reverse Charge %
  RvsChrgTax Num(19,6) Reverse Charge Tax Amount
  RvsChrgSC Num(19,6) Reverse Charge Tax Amount (SC)
  RvsChrgFC Num(19,6) Reverse Charge Tax Amount (FC)
  InFirstIns VarChar(1) Included in First Installment default=N [Y=Yes, N=No]
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CESTrel VarChar(1) CEST Relevant default=N [Y=, N=]

# RDR5 - Sales Order - Withholding Tax
Module: Marketing Documents | 158 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  SECONDERY U: AbsEntry, WTCode, BaseAbsEnt, Doc1LineNo
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator ->ORDR
  WTCode nVarChar(4) WT Code ->OWHT
  Rate Num(19,6) Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntSC Num(19,6) Taxable Amount in SC
  TxblAmntFC Num(19,6) Taxable Amount in FC
  WTAmnt Num(19,6) WT Amount
  WTAmntSC Num(19,6) WT Amount (SC)
  WTAmntFC Num(19,6) WT Amount (FC)
  ApplAmnt Num(19,6) Applied WT Amount
  ApplAmntSC Num(19,6) Applied WTax Amount (SC)
  ApplAmntFC Num(19,6) Applied WTax Amount (FC)
  Category VarChar(1) Category [P=Payment, I=Invoice]
  Criteria VarChar(1) Criteria [Y=Accrual, N=Cash]
  Account nVarChar(15) G/L Account ->OACT
  Type VarChar(1) Withholding Type [V=VAT Withholding, I=Income Tax Withholding]
  RoundType VarChar(1) Rounding Type [T=Truncated, C=Commercial Values, N=No Rounding]
  BaseType VarChar(1) Base Type [G=Gross, N=Net, V=VAT, U=UoM]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseLine Int(11) Base Line
  BaseNum Int(11) Base Document Type default=-1 [-1=, 0=, 23=Sales Quotation]
  LineNum Int(11) Line Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Abs. Entry default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=17 ->ADP1
  Doc1LineNo Int(11) DOC1 Line Number default=-1
  WtLineType VarChar(1) WT Line Type default=D [D=Document Level WTax, L=Row Level WTax]
  TxblCurr nVarChar(3) Taxable Currency from Doc Line
  DtblCurr nVarChar(3) Deductible Currency
  DtblRate Num(19,6) Rate for Deductible Amount
  txblRate Num(19,6) Rate for Taxable Amount
  DtblAmount Num(19,6) Deductible Amount
  TdsAcc nVarChar(15) TDS Account ->OACT
  SurAcc nVarChar(15) Surcharge Account ->OACT
  CessAcc nVarChar(15) Cess Account ->OACT
  HscAcc nVarChar(15) HSC Account ->OACT
  TdsRate Num(19,6) TDS Rate
  SurRate Num(19,6) Surcharge Rate
  CessRate Num(19,6) Cess Rate
  HscRate Num(19,6) HSC Rate
  TdsBAmt Num(19,6) TDS Base Amount
  TdsBAmtSC Num(19,6) TDS Base Amount (SC)
  TdsBAmtFC Num(19,6) TDS Base Amount (FC)
  SurBAmt Num(19,6) Surcharge Base Amount
  SurBAmtSC Num(19,6) Surcharge Base Amount (SC)
  SurBAmtFC Num(19,6) Surcharge Base Amount (FC)
  CessBAmt Num(19,6) Cess Base Amount
  CessBAmtSC Num(19,6) Cess Base Amount (SC)
  CessBAmtFC Num(19,6) Cess Base Amount (FC)
  HscBAmt Num(19,6) HSC Base Amount
  HscBAmtSC Num(19,6) HSC Base Amount (SC)
  HscBAmtFC Num(19,6) HSC Base Amount (FC)
  TdsAmnt Num(19,6) TDS Tax Amount
  TdsAmntSC Num(19,6) TDS Tax Amount (SC)
  TdsAmntFC Num(19,6) TDS Tax Amount (FC)
  SurAmnt Num(19,6) Surcharge Tax Amount
  SurAmntSC Num(19,6) Surcharge Tax Amount (SC)
  SurAmntFC Num(19,6) Surcharge Tax Amount (FC)
  CessAmnt Num(19,6) Cess Tax Amount
  CessAmntSC Num(19,6) Cess Tax Amount (SC)
  CessAmntFC Num(19,6) Cess Tax Amount (FC)
  HscAmnt Num(19,6) HSC Tax Amount
  HscAmntSC Num(19,6) HSC Tax Amount (SC)
  HscAmntFC Num(19,6) HSC Tax Amount (FC)
  TdsAppl Num(19,6) Applied TDS Amount
  TdsApplSC Num(19,6) Applied TDS Amount (SC)
  TdsApplFC Num(19,6) Applied TDS Amount (FC)
  SurAppl Num(19,6) Applied Surcharge Amount
  SurApplSC Num(19,6) Applied Surcharge Amount (SC)
  SurApplFC Num(19,6) Applied Surcharge Amount (FC)
  CessAppl Num(19,6) Applied Cess Amount
  CessApplSC Num(19,6) Applied Cess Amount (SC)
  CessApplFC Num(19,6) Applied Cess Amount (FC)
  HscAppl Num(19,6) Applied HSC Amount
  HscApplSC Num(19,6) Applied HSC Amount (SC)
  HscApplFC Num(19,6) Applied HSC Amount (FC)
  BatchNum Int(11) Journal Voucher No.
  InCSTCode nVarChar(2) CST Code Incoming
  OutCSTCode nVarChar(2) CST Code Outgoing
  DpmWTApl Num(19,6) DPM WT Applied Amount
  DpmWTAplSC Num(19,6) DPM WT Applied Amount (SC)
  DpmWTAplFC Num(19,6) DPM WT Applied Amount (FC)
  WTTypeId Int(11) WT Type Id ->OWTT
  LnBsAmt Num(19,6) BR Line WT Base Amount
  LnBsAmtSC Num(19,6) BR Line WT Base Amount(SC)
  LnBsAmtFC Num(19,6) BR Line WT Base Amount(FC)
  LnCmTAmt Num(19,6) BR Line Cumulated Taxable Amount
  LnCmTAmtSC Num(19,6) BR Line Cumulated Taxable Amount(SC)
  LnCmTAmtFC Num(19,6) BR Line Cumulated Taxable Amount(FC)
  TDSType VarChar(1) TDS Type [E=eTDS, D=GST TDS, C=GST TCS, S=SALES TCS]
  IgstAcc nVarChar(15) IGST Account ->OACT
  CgstAcc nVarChar(15) CGST Account ->OACT
  SgstAcc nVarChar(15) SGST Account ->OACT
  IgstAmnt Num(19,6) IGST Tax Amount
  IgstAmntSC Num(19,6) IGST Tax Amount (SC)
  IgstAmntFC Num(19,6) IGST Tax Amount (FC)
  CgstAmnt Num(19,6) CGST Tax Amount
  CgstAmntSC Num(19,6) CGST Tax Amount (SC)
  CgstAmntFC Num(19,6) CGST Tax Amount (FC)
  SgstAmnt Num(19,6) SGST Tax Amount
  SgstAmntSC Num(19,6) SGST Tax Amount (SC)
  SgstAmntFC Num(19,6) SGST Tax Amount (FC)
  IgstRate Num(19,6) IGST Rate
  CgstRate Num(19,6) CGST Rate
  SgstRate Num(19,6) SGST Rate
  IgstBAmt Num(19,6) IGST Base Amount
  IgstBAmtSC Num(19,6) IGST Base Amount (SC)
  IgstBAmtFC Num(19,6) IGST Base Amount (FC)
  CgstBAmt Num(19,6) CGST Base Amount
  CgstBAmtSC Num(19,6) CGST Base Amount (SC)
  CgstBAmtFC Num(19,6) CGST Base Amount (FC)
  SgstBAmt Num(19,6) SGST Base Amount
  SgstBAmtSC Num(19,6) SGST Base Amount (SC)
  SgstBAmtFC Num(19,6) SGST Base Amount (FC)
  IgstAppl Num(19,6) Applied IGST Amount
  IgstApplSC Num(19,6) Applied IGST Amount (SC)
  IgstApplFC Num(19,6) Applied IGST Amount (FC)
  CgstAppl Num(19,6) Applied CGST Amount
  CgstApplSC Num(19,6) Applied CGST Amount (SC)
  CgstApplFC Num(19,6) Applied CGST Amount (FC)
  SgstAppl Num(19,6) Applied SGST Amount
  SgstApplSC Num(19,6) Applied SGST Amount (SC)
  SgstApplFC Num(19,6) Applied SGST Amount (FC)
  UtgstAcc nVarChar(15) UTGST Account ->OACT
  CsgstAcc nVarChar(15) Cess GST Account ->OACT
  UtgstAmt Num(19,6) UTGST Tax Amount
  UtgstAmtSC Num(19,6) UTGST Tax Amount (SC)
  UtgstAmtFC Num(19,6) UTGST Tax Amount (FC)
  CsgstAmt Num(19,6) Cess GST Tax Amount
  CsgstAmtSC Num(19,6) Cess GST Tax Amount (SC)
  CsgstAmtFC Num(19,6) Cess GST Tax Amount (FC)
  UtgstRate Num(19,6) UTGST Rate
  CsgstRate Num(19,6) Cess GST Rate
  UtgstBAmt Num(19,6) UTGST Base Amount
  UtgstBAmtS Num(19,6) UTGST Base Amount (SC)
  UtgstBAmtF Num(19,6) UTGST Base Amount (FC)
  CsgstBAmt Num(19,6) Cess GST Base Amount
  CsgstBAmtS Num(19,6) Cess GST Base Amount (SC)
  CsgstBAmtF Num(19,6) Cess GST Base Amount (FC)
  UtgstAppl Num(19,6) Applied UTGST Amount
  UtgstApplS Num(19,6) Applied UTGST Amount (SC)
  UtgstApplF Num(19,6) Applied UTGST Amount (FC)
  CsgstAppl Num(19,6) Applied Cess GST Amount
  CsgstApplS Num(19,6) Applied Cess GST Amount (SC)
  CsgstApplF Num(19,6) Applied Cess GST Amount (FC)
  EncryptIV nVarChar(100) Encrypt IV
  TcsIntAcct nVarChar(15) TCS Interim Account ->OACT
  SurIntAcct nVarChar(15) Surcharge Interim Account ->OACT
  CesIntAcct nVarChar(15) Cess Interim Account ->OACT
  HscIntAcct nVarChar(15) HSC interim Account ->OACT
  LnIntAcct nVarChar(15) Interim Account for Tax ->OACT
  FixedAmnt Num(19,6) Fixed Amount
  FixedAmtSC Num(19,6) Fixed Amount (SC)
  FixedAmtFC Num(19,6) Fixed Amount (FC)
  BaseQty Num(19,6) Base Quantity

# RDR6 - Sales Order - Installments
Module: Marketing Documents | 65 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, InstlmntID
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDR
  InstlmntID Int(6) Installment ID default=1
  ObjType nVarChar(20) Object Type default=17 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DueDate Date(8) Due Date
  Status VarChar(1) Installment Status default=O [O=Open, C=Closed]
  DunnLevel Int(11) Dunning Level default=0
  InsTotal Num(19,6) Total Installment
  InsTotalFC Num(19,6) Total Installment (FC)
  InsTotalSy Num(19,6) Total Installment (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  VatSum Num(19,6) Total Tax
  VatSumFC Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  VatPaid Num(19,6) Tax Paid to Date
  VatPaidFC Num(19,6) Tax Paid (FC)
  VatPaidSys Num(19,6) Tax Paid (SC)
  TotalExpns Num(19,6) Total Freight Charges
  TotalExpFC Num(19,6) Total Freight Charges (FC)
  TotalExpSC Num(19,6) Total Freight Charges (SC)
  ExpAppl Num(19,6) Applied Freight Charges
  ExpApplFC Num(19,6) Applied Freight Charges (SC)
  ExpApplSC Num(19,6) Applied Freight Charges (SC)
  WTSum Num(19,6) WTax Amount
  WTSumFC Num(19,6) WTax Amount (FC)
  WTSumSC Num(19,6) WTax Amount (SC)
  WTApplied Num(19,6) Applied WTax
  WTAppliedF Num(19,6) Applied WTax (FC)
  WTAppliedS Num(19,6) Applied WTax (SC)
  TotalBlck Num(19,6) Total Reserved Amount
  TotalBlckF Num(19,6) Total Reserved Amount (FC)
  TotalBlckS Num(19,6) Total Reserved Amount (SC)
  VATBlck Num(19,6) Reserved Tax
  VATBlckFC Num(19,6) Reserved Tax (FC)
  VATBlckSC Num(19,6) Reserved Tax (SC)
  ExpnsBlck Num(19,6) Reserved Freight Charges
  ExpnsBlckF Num(19,6) Reserved Freight Charges (FC)
  ExpnsBlckS Num(19,6) Reserved Freight Charges (SC)
  WTBlocked Num(19,6) Reserved WTax Amount
  WTBlockedF Num(19,6) Reserved WTax Amount (FC)
  WTBlockedS Num(19,6) Reserved WTax Amount (SC)
  InstPrcnt Num(19,6) Installment %
  DunWizBlck VarChar(1) Wizard dunning block default=N [N=No, Y=Yes]
  DunDate Date(8) Last Dunning Date
  Paid Num(19,6) Paid
  PaidFrgn Num(19,6) Paid (FC)
  PaidSc Num(19,6) Paid (SC)
  reserved VarChar(1) Reserved default=N [N=No, Y=Yes]
  TaxOnExp Num(19,6) Tax on Expenses
  TaxOnExpFc Num(19,6) Tax on Expenses (FC)
  TaxOnExpSc Num(19,6) Tax on Expenses (SC)
  TaxOnExpAp Num(19,6) Applied Tax on Expenses
  TaxOnExApF Num(19,6) Applied Tax on Expenses (FC)
  TaxOnExApS Num(19,6) Applied Tax on Expenses (SC)
  TaxOnExBlo Num(19,6) Reserved Tax on Freight Amount
  TaxOnExBlF Num(19,6) Reserved Tax on Freight Amt FC
  TaxOnExBlS Num(19,6) Reserved Tax on Freight Amt SC
  LvlUpdDate Date(8) Dunning Level Update Date
  Ordered VarChar(1) Payment Ordered default=N [Y=Yes, N=No]
  PaidDpm Num(19,6) Paid by Down Payment
  PaidDpmFc Num(19,6) Paid by Down Payment (FC)
  PaidDpmSc Num(19,6) Paid by Down Payment (SC)
  EncryptIV nVarChar(100) Encrypt IV

# RDR7 - Delivery Packages - Sales Order
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDR
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type default=17 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV

# RDR8 - Sales Order - Items in Package
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum, ItemCode, UomEntry, NumPerMsr
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDR
  PackageNum Int(11) Package Number
  ItemCode nVarChar(50) Item Code ->OITM
  Quantity Num(19,6) Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=17 ->ADP1
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value default=0

# RDR9 - Order - Drawn Dpm
Module: Marketing Documents | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDR
  LineNum Int(11) Row Number
  BaseAbs Int(11) Base Document Internal ID
  BaseLine Int(11) Base Document Row
  TargetBase VarChar(1) Target or Base Document default=B [B=Base, T=Target]
  ObjType nVarChar(20) Base Object Type
  DrawnSum Num(19,6) Net LC
  DrawnSumFc Num(19,6) Net FC
  DrawnSumSc Num(19,6) Net SC
  LogInstanc Int(11) Log Instance default=0
  ObjCode nVarChar(20) Object Type default=17 ->ADP1
  ApplDrawn Num(19,6) Applied Net LC
  ApplDrawnF Num(19,6) Applied Net FC
  ApplDrawnS Num(19,6) Applied Net SC
  BaseDocNum Int(11) Base Document Number
  BsDocDate Date(8) Base Posting Date
  BsDueDate Date(8) Base Due Date
  BsCardName nVarChar(100) Base BP Name
  BsComments nVarChar(254) Base Remarks
  Posted VarChar(1) Base Document Posted default=Y [Y=Yes, N=No]
  Vat Num(19,6) Tax LC
  VatFc Num(19,6) Tax FC
  VatSc Num(19,6) Tax SC
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  IsGross VarChar(1) Is Gross Line default=N [N=Net Line, Y=Gross Line]

# RIN1 - A/R Credit Memo - Rows
Module: Marketing Documents | 317 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  STATUS: LineStatus
  CURRENCY: Currency
  ACCOUNT: AcctCode
  BASE_ENTRY: BaseEntry, BaseType, BaseLine
  VIS_ORDER: DocEntry, VisOrder
  OWNER_CODE: OwnerCode
  ITM_WHS_OQ: ItemCode, WhsCode, OpenQty
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORIN
  LineNum Int(11) Row Number
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=]
  TrgetEntry Int(11) Target Document Internal ID
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 16=A/R Returns, 13=A/R Invoice, 203=A/R Down Payment, 14=A/R Credit Note, 234000031=A/R Return Request]
  BaseEntry Int(11) Base Document Internal ID
  BaseLine Int(11) Base Row
  LineStatus VarChar(1) Row Status default=O [O=Open, C=Closed]
  ItemCode nVarChar(50) Item No. ->OITM
  Dscription nVarChar(200) Item/Service Description
  Quantity Num(19,6) Quantity
  ShipDate Date(8) Row Delivery Date
  OpenQty Num(19,6) Remaining Open Quantity
  Price Num(19,6) Price
  Currency nVarChar(3) Price Currency ->OCRN
  Rate Num(19,6) Currency Rate
  DiscPrcnt Num(19,6) Discount % per Row
  LineTotal Num(19,6) Row Total
  TotalFrgn Num(19,6) Row Total (FC)
  OpenSum Num(19,6) Open Amount
  OpenSumFC Num(19,6) Open Amount (FC)
  VendorNum nVarChar(50) Vendor Catalog No.
  SerialNum nVarChar(17) Serial Number
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  SlpCode Int(11) Sales Employee Code default=-1 ->OSLP
  Commission Num(19,6) Commission Percentage
  TreeType VarChar(1) BOM Type default=N [N=Not a BOM, A=Assembly, S=Sales, I=Sales BOM Component, P=Production, T=Template]
  AcctCode nVarChar(15) Account Code ->OACT
  TaxStatus VarChar(1) Tax Definition [Y=Yes, N=No]
  GrossBuyPr Num(19,6) Gross Profit Base Price
  PriceBefDi Num(19,6) Unit Price
  DocDate Date(8) Posting Date
  Flags Int(11) Flags default=0
  OpenCreQty Num(19,6) Credit Memo Amount
  UseBaseUn VarChar(1) Inventory UoM default=N [Y=Yes, N=No]
  SubCatNum nVarChar(50) BP Catalog No. ->OSCN
  BaseCard nVarChar(15) Base BP Code ->OCRD
  TotalSumSy Num(19,6) Row Total (SC)
  OpenSumSys Num(19,6) Open Amount (SC)
  InvntSttus VarChar(1) Warehouse Status default=O [O=Open, C=Closed]
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  CodeBars nVarChar(254) Bar Code
  VatPrcnt Num(19,6) Tax Rate per Row
  VatGroup nVarChar(8) Tax Definition ->OVTG
  PriceAfVAT Num(19,6) Gross Price after Discount
  Height1 Num(19,6) Height 1
  Hght1Unit Int(6) Unit of Height 1
  Height2 Num(19,6) Height 2
  Hght2Unit Int(6) Unit of Height 2
  Width1 Num(19,6) Width 1
  Wdth1Unit Int(6) Unit of Width 1
  Width2 Num(19,6) Width 2
  Wdth2Unit Int(6) Unit of Width 2
  Length1 Num(19,6) Length 1
  Len1Unit Int(6) Unit of Length 1
  length2 Num(19,6) Length 2
  Len2Unit Int(6) Unit of Length 2
  Volume Num(19,6) Quantity
  VolUnit Int(6) Vol. Unit
  Weight1 Num(19,6) Weight 1
  Wght1Unit Int(6) Unit of Weight 1
  Weight2 Num(19,6) Weight 2
  Wght2Unit Int(6) Unit of Weight 2
  Factor1 Num(19,6) Factor 1
  Factor2 Num(19,6) Factor 2
  Factor3 Num(19,6) Factor 3
  Factor4 Num(19,6) Factor 4
  PackQty Num(19,6) Packing Quantity
  UpdInvntry VarChar(1) Warehouse Update default=Y [Y=Yes, N=No]
  BaseDocNum Int(11) Base Document No.
  BaseAtCard nVarChar(100) Customer/Vendor Base Document
  SWW nVarChar(16) Additional Identifier
  VatSum Num(19,6) Total Tax
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  FinncPriod Int(11) Posting Period ->OFPR
  ObjType nVarChar(20) Object Type default=14 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BlockNum nVarChar(100) Block Number
  ImportLog nVarChar(20) Import Log
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAqcuistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  DistribSum Num(19,6) Distributed Amount
  DstrbSumFC Num(19,6) Distributed Amount (FC)
  DstrbSumSC Num(19,6) Distributed Amount (SC)
  GrssProfit Num(19,6) Row Gross Profit
  GrssProfSC Num(19,6) Row Gross Profit (SC)
  GrssProfFC Num(19,6) Row Gross Profit (FC)
  VisOrder Int(11) Visual Order
  INMPrice Num(19,6) Item's Last Sales Price (OINM)
  PoTrgNum Int(11) PO Target No.
  PoTrgEntry nVarChar(11) PO Target Internal ID
  DropShip VarChar(1) Drop-Ship default=N [Y=Yes, N=No]
  PoLineNum Int(11) PO Target Row No.
  Address nVarChar(254) Address
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type [Y=Regular Tax, N=No Tax, U=Use Tax, O=Offset Tax]
  OrigItem nVarChar(50) Original Item ->OITM
  BackOrdr VarChar(1) Allow Backorder [Y=Yes, N=No]
  FreeTxt nVarChar(100) Free Text
  PickStatus VarChar(1) Pick Status default=N [Y=Picked, N=Not Picked, R=Released for Picking, P=Partially Picked]
  PickOty Num(19,6) Pick Quantity
  PickIdNo Int(11) Pick ID
  TrnsCode Int(6) Shipping Method default=-1 ->OSHP
  VatAppld Num(19,6) Applied Tax
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  BaseQty Num(19,6) Base Quantity
  BaseOpnQty Num(19,6) Base Open Quantity
  VatDscntPr Num(19,6) Tax Discount %
  WtLiable VarChar(1) Withholding Tax Liable [Y=Yes, N=No]
  DeferrTax VarChar(1) Deferred Tax default=N [Y=Yes, N=No]
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatlF Num(19,6) Net Tax Amount
  LineVatS Num(19,6) Net Tax Amount
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value
  CEECFlag VarChar(1) Correction Invoice Was/Should Be default=S [W=Was, S=Should Be]
  ToStock Num(19,6) Corr. Invoice Amt to Inventory
  ToDiff Num(19,6) Corr. Invoice Amount to Diff.
  ExciseAmt Num(19,6) Excise Amount
  TaxPerUnit Num(19,6) Tax per Unit
  TotInclTax Num(19,6) Total Including Tax
  CountryOrg nVarChar(3) Country/Region of Origin
  StckDstSum Num(19,6) Stock Distribution Sum
  ReleasQtty Num(19,6) Released Quantity
  LineType VarChar(1) Row Type default=R [R=Regular]
  TranType VarChar(1) Transaction Type [C=Complete, R=Reject]
  Text Text(16) Text
  OwnerCode Int(11) Document Owner
  StockPrice Num(19,6) Item Cost
  ConsumeFCT VarChar(1) Consumer Sales Forecast [Y=Yes, N=No]
  LstByDsSum Num(19,6) Last Buy Distribute Sum
  StckINMPr Num(19,6) Stock Inm Price
  LstBINMPr Num(19,6) Last Buy Inventory Journal Pr.
  StckDstFc Num(19,6) Stock Distribution Sum (FC)
  StckDstSc Num(19,6) Stock Distribution Sum (SC)
  LstByDsFc Num(19,6) Last Buy Distribute Sum (FC)
  LstByDsSc Num(19,6) Last Buy Distribute Sum (SC)
  StockSum Num(19,6) Stock Sum
  StockSumFc Num(19,6) Stock Sum FC
  StockSumSc Num(19,6) Stock Sum SC
  StckSumApp Num(19,6) Stock Sum Applied
  StckAppFc Num(19,6) Stock Sum Applied FC
  StckAppSc Num(19,6) Stock Sum Applied SC
  ShipToCode nVarChar(50) Ship-to Code
  ShipToDesc nVarChar(254) Ship-to Description
  StckAppD Num(19,6) Stock Distrib. - Applied Sum
  StckAppDFC Num(19,6) Stock Dist. - Applied Sum (FC)
  StckAppDSC Num(19,6) Stock Dist. - Applied Sum (SC)
  BasePrice VarChar(1) Price for Total Calculation default=E [E=Exclude Tax, I=Include Tax]
  GTotal Num(19,6) Gross Total
  GTotalFC Num(19,6) Gross Total (FC)
  GTotalSC Num(19,6) Gross Total (SC)
  DistribExp VarChar(1) Distribute Freight [Y=Yes, N=No]
  DescOW VarChar(1) Description Overwritten default=N [Y=Yes, N=No]
  DetailsOW VarChar(1) Details Overwritten default=N [Y=Yes, N=No]
  GrossBase Int(6) Base Method for Gross Profit
  VatWoDpm Num(19,6) Tax Before DPM Applied
  VatWoDpmFc Num(19,6) Tax Before DPM Applied (FC)
  VatWoDpmSc Num(19,6) Tax Before DPM Applied (SC)
  CFOPCode nVarChar(6) CFOP Code for Document ->OCFP
  CSTCode nVarChar(6) CST Code for ICMS
  Usage Int(11) Usage Code for Document ->OUSG
  TaxOnly VarChar(1) Tax Only [Y=Yes, N=No]
  WtCalced VarChar(1) Withholding Tax Calculated default=N [N=No, Y=Yes]
  QtyToShip Num(19,6) Quantity to Ship
  DelivrdQty Num(19,6) Delivered Quantity
  OrderedQty Num(19,6) Ordered Quantity
  CogsOcrCod nVarChar(8) COGS Distribution Rule Code ->OOCR
  CiOppLineN Int(11) Line Number of Opposite Line default=-1
  CogsAcct nVarChar(15) COGS Account Code ->OACT
  ChgAsmBoMW VarChar(1) Change Whs for Asm BoM Child [Y=Yes, N=No]
  ActDelDate Date(8) Actual Delivery Date
  OcrCode2 nVarChar(8) Costing Code 2 ->OOCR
  OcrCode3 nVarChar(8) Costing Code 3 ->OOCR
  OcrCode4 nVarChar(8) Costing Code 4 ->OOCR
  OcrCode5 nVarChar(8) Costing Code 5 ->OOCR
  TaxDistSum Num(19,6) Tax Distributed Amount
  TaxDistSFC Num(19,6) Tax Distributed Amount (FC)
  TaxDistSSC Num(19,6) Tax Distributed Amount (SC)
  PostTax VarChar(1) Post Tax in Price to Stock default=Y [Y=Yes, N=No]
  Excisable VarChar(1) Excisable [Yes/No] [Y=Yes, N=No]
  AssblValue Num(19,6) Assessable Value
  RG23APart1 Int(11) RG23A Part1 Number
  RG23APart2 Int(11) RG23A Part2 Number
  RG23CPart1 Int(11) RG23C Part1 Number
  RG23CPart2 Int(11) RG23C Part2 Number
  CogsOcrCo2 nVarChar(8) COGS Distribution Rule Code2 ->OOCR
  CogsOcrCo3 nVarChar(8) COGS Distribution Rule Code3 ->OOCR
  CogsOcrCo4 nVarChar(8) COGS Distribution Rule Code4 ->OOCR
  CogsOcrCo5 nVarChar(8) COGS Distribution Rule Code5 ->OOCR
  LnExcised VarChar(1) Line Excised [O=Open, C=Closed, P=Copied to OEI]
  LocCode Int(11) Location Code ->OLCT
  StockValue Num(19,6) Total COGS Value
  GPTtlBasPr Num(19,6) Total Base Price for Profit
  unitMsr2 nVarChar(100) Pur/Sal UoM if BaseUnit
  NumPerMsr2 Num(19,6) Pur/Sal UoM Value if Base Unit
  SpecPrice VarChar(1) Price Source Type default=N [Y=Special Prices for Business Partner, N=Manual, W=Active Price List, Discount Groups, R=Active Price List, U=Inactive Price List, A=Blanket Agreement, P=Period and Volume Discounts, Q=Period and Volume Discounts, Discount Groups, V=Inactive Price List, Discount Groups, 9=Special Prices for Business Partner, !=Blanket Agreement, 0=Period and Volume Discounts, 1=Period and Volume Discounts, Discount Groups, 2=Active Price List, 7=Active Price List, Discount Groups, 5=Inactive Price List, 6=Inactive Price List, Discount Groups]
  CSTfIPI nVarChar(2) CST for IPI Code
  CSTfPIS nVarChar(2) CST for PIS Code
  CSTfCOFINS nVarChar(2) CST for COFINS Code
  ExLineNo nVarChar(10) ExLineNo
  isSrvCall VarChar(1) Created from Service Call default=N [Y=Yes, N=No]
  PQTReqQty Num(19,6) Pur Quotation: Required Qty
  PQTReqDate Date(8) Pur Quotation: Required Date
  PcDocType Int(11) Purchase Confirmation Doc Type default=-1 [-1=No Type, 22=Purchase Order, 540000006=Purchase Quotation]
  PcQuantity Num(19,6) Purchase Confirmation Quantity
  LinManClsd VarChar(1) Line Was Closed Manually default=N [Y=Yes, N=No, U=Unknown]
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  NoInvtryMv VarChar(1) Without Inventory Movement default=N [Y=Yes, N=No]
  ActBaseEnt Int(11) Actual Base Document Entry
  ActBaseLn Int(11) Actual Base Line Number
  ActBaseNum Int(11) Actual Base Document No.
  OpenRtnQty Num(19,6) Quantity Open for Return
  AgrNo Int(11) Agreement No. ->OOAT
  AgrLnNum Int(11) Agreement Row Number
  CredOrigin VarChar(1) Credit Origin ->OBSI
  Surpluses Num(19,6) Surpluses
  DefBreak Num(19,6) Defect and Breakup
  Shortages Num(19,6) Shortages
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  UomEntry2 Int(11) UoM Entry if Base Unit default=0 ->OUOM
  UomCode nVarChar(20) UoM Code
  UomCode2 nVarChar(20) UoM Code if Base Unit
  FromWhsCod nVarChar(8) From Warehouse Code ->OWHS
  NeedQty VarChar(1) Consider Quantity of Items default=N [Y=Yes, N=No]
  PartRetire VarChar(1) Partial Retirement default=N [Y=Yes, N=No]
  RetireQty Num(19,6) Retirement Quantity
  RetireAPC Num(19,6) Retirement APC
  RetirAPCFC Num(19,6) Retirement APC FC
  RetirAPCSC Num(19,6) Retirement APC SC
  InvQty Num(19,6) Quantity - Inventory UoM
  OpenInvQty Num(19,6) Open Quantity (Inventory UoM)
  EnSetCost VarChar(1) Enable Set Item Cost in Return default=N [Y=Yes, N=No]
  RetCost Num(19,6) Return Cost in A/R Return
  Incoterms Int(11) Incoterms default=0 ->ODCI
  TransMod Int(11) Transport Mode default=0 ->ODCI
  LineVendor nVarChar(15) Line Vendor Code ->OCRD
  DistribIS VarChar(1) Distribute Intrastat Freight default=N [Y=Yes, N=No]
  ISDistrb Num(19,6) Intrastat Distrib. Amount
  ISDistrbFC Num(19,6) Intrastat Distrib. Amount (FC)
  ISDistrbSC Num(19,6) Intrastat Distrib. Amount (SC)
  IsByPrdct VarChar(1) Item Is By-Product default=N [N=No, Y=Yes]
  ItemType Int(11) Item Type default=4 [4=Item]
  PriceEdit VarChar(1) Price Was Edited by User default=N [N=No, Y=Yes]
  PrntLnNum Int(11) Parent Line Number
  LinePoPrss VarChar(1) Line PO Process default=N [Y=Yes, N=No]
  FreeChrgBP VarChar(1) Free of Charge (BP) default=N [Y=Yes, N=No]
  TaxRelev VarChar(1) Tax Relevant Row default=Y [Y=Yes, N=No]
  LegalText nVarChar(254) Legal Text
  ThirdParty VarChar(1) Third Party default=N [Y=Yes, N=No]
  LicTradNum nVarChar(32) Federal Tax ID
  InvQtyOnly VarChar(1) Change Qty (Inv. UoM) Only default=N [Y=Yes, N=No]
  UnencReasn Int(11) Reason for Unencumbered ICMS
  ShipFromCo nVarChar(50) Ship-From Code
  ShipFromDe nVarChar(254) Ship-From Description
  FisrtBin nVarChar(228) First Bin Location
  AllocBinC nVarChar(11) Allocated Bin Location Count
  ExpType nVarChar(4) Expense Type ->OEXD
  ExpUUID nVarChar(50) Expense UUID
  ExpOpType VarChar(1) Expense Operation Type [P=Professional Services, R=Renting Assets, O=Others]
  DIOTNat nVarChar(3) DIOT Nationality ->OCRY
  MYFtype nVarChar(2) MYF type [S1=MYF Wholesale Sales, S2=Retail Sales, P1=MYF Wholesale Purchases, P3=Other Expense Transactions]
  GPBefDisc Num(19,6) Gross Price
  ReturnRsn Int(6) Return Reason default=-1
  ReturnAct Int(6) Return Action default=-1
  StgSeqNum Int(11) Stage Sequence Number
  StgEntry Int(11) Stage Entry ->ORST
  StgDesc nVarChar(100) Stage Description
  ItmTaxType nVarChar(2) Item GST Tax Category [GR=GST Regular, GN=GST Nil Rated, GE=GST Exempt, NE=Excisable, NN=Non-GST Non-Excisable]
  SacEntry Int(11) SAC Entry ->OSAC
  NCMCode Int(11) NCM Code default=-1 ->ONCM
  HsnEntry Int(11) HSN Entry
  OriBAbsEnt Int(11) Original Base Document Internal ID
  OriBLinNum Int(11) Original Base Document Line Number
  OriBDocTyp Int(11) Original Base Document Type
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No, U=Use]
  EncryptIV nVarChar(100) Encrypt IV
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  StdItemId Int(11) Standard Item Identification ->OUNCL
  CommClass Int(11) Commodity Classification ->OUNCL
  VatExEntry Int(11) VAT Exemption AbsEntry ->OVEB
  VatExLN Int(6) VAT Exemption LineNum
  NatOfTrans Int(11) Nature of Transaction ->ODCI
  ISDtCryImp nVarChar(3) Destination Country/Region for Import ->OCRY
  ISDtRgnImp Int(11) Destination Region for Import ->ODCI
  ISOrCryExp nVarChar(3) Country/Region of Origin for Export ->OCRY
  ISOrRgnExp Int(11) Region of Origin for Export ->ODCI
  NVECode nVarChar(6) NVE Code
  PoNum nVarChar(20) Customer's Purchase Order Number
  PoItmNum Int(11) Customer's Purchase Order Item Number
  IndEscala VarChar(1) Indicator for Relevant Scale default=N [Y=Yes, N=No]
  CESTCode Int(11) CEST Code ->OCEST
  CtrSealQty Num(19,6) Control Seal Quantity
  CNJPMan nVarChar(14) CNPJ of Manufacturer
  UFFiscBene nVarChar(10) UF Fiscal Benefit Code
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]
  LegalTIMD nVarChar(250) Legal Text from Item Master Data
  LegalTTCA nVarChar(250) Legal Text from Tax Code Attributes
  LegalTW nVarChar(250) Legal Text from Warehouse
  LegalTCD nVarChar(250) Legal Text from Tax Code Determination
  RevCharge VarChar(1) Reverse Charge default=N [Y=Yes, N=No]
  ListNum Int(6) Price List No. ->OPLN

# RIN10 - A/R Credit Memo - Row Structure
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SECONDERY U: DocEntry, AftLineNum, OrderNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORIN
  LineSeq Int(11) Row Sequence
  AftLineNum Int(11) After Row Number
  OrderNum Int(11) Order Number
  LineType VarChar(1) Row Type [T=Text, S=Subtotal]
  LineText Text(16) Row Text
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=14 ->ADP1

# RIN11 - A/R Cr. Memo - Drawn Dpm Det.
Module: Marketing Documents | 70 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LineSeq
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORIN
  LineNum Int(11) Row Number
  LineSeq Int(11) Sequence Number
  BaseAbs Int(11) Base Document Internal ID default=-1 ->ODPI
  BaseType Int(11) Base Object Type default=203 [203=A/R Down Payment]
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  VatPrcnt Num(19,6) VAT Percent
  LineTotal Num(19,6) Net LC
  TotalFrgn Num(19,6) Net FC
  TotalSumSy Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFrgn Num(19,6) Tax FC
  VatSumSys Num(19,6) Tax SC
  ObjType nVarChar(20) Object Type default=14 ->ADP1
  LogInstanc Int(11) Log Instance
  IsAcq VarChar(1) Acquisition Tax-Liable default=N [N=No, Y=Yes]
  IsAllDrawn VarChar(1) Remaining Amount Drawn default=N [Y=Yes, N=No]
  IsGross VarChar(1) Is Gross Line default=N [N=Net Line, Y=Gross Line]
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  ApplNet Num(19,6) Applied Net LC
  ApplNetFc Num(19,6) Applied Net FC
  ApplNetSc Num(19,6) Applied Net SC
  ApplVat Num(19,6) Applied Tax LC
  ApplVatFc Num(19,6) Applied Tax FC
  ApplVatSc Num(19,6) Applied Tax SC
  BaseNet Num(19,6) Base Net LC
  BaseNetFc Num(19,6) Base Net FC
  BaseNetSc Num(19,6) Base Net SC
  BaseVat Num(19,6) Base Tax LC
  BaseVatFc Num(19,6) Base Tax FC
  BaseVatSc Num(19,6) Base Tax SC
  BaseGross Num(19,6) Base Gross LC
  BaseGrossF Num(19,6) Base Gross FC
  BaseGrossS Num(19,6) Base Gross SC
  LineType VarChar(1) Line Type default=D [D=Document Row, R=Currency Rounding, H=Down Payment Document Rounding]
  DctSum Num(19,6) Deductible Sum LC
  DctSumFc Num(19,6) Deductible Sum FC
  DctSumSc Num(19,6) Deductible Sum SC
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplDct Num(19,6) Applied Deductible Sum LC
  ApplDctFc Num(19,6) Applied Deductible Sum FC
  ApplDctSc Num(19,6) Applied Deductible Sum SC
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  BaseDct Num(19,6) Base Deductible Sum LC
  BaseDctFc Num(19,6) Base Deductible Sum FC
  BaseDctSc Num(19,6) Base Deductible Sum SC
  BaseEq Num(19,6) Base Equalization Sum LC
  BaseEqFc Num(19,6) Base Equalization Sum FC
  BaseEqSc Num(19,6) Base Equalization Sum SC
  TaxCode nVarChar(8) Tax Code ->OSTC
  ApplGross Num(19,6) Applied Gross LC
  ApplGrossF Num(19,6) Applied Gross FC
  ApplGrossS Num(19,6) Applied Gross SC
  TaxAdjust VarChar(1) Manual Tax Adjustment default=N [Y=Yes, N=No]
  RvsChrgSum Num(19,6) Reverse Charge Sum LC
  RvsChrgFc Num(19,6) Reverse Charge Sum FC
  RvsChrgSc Num(19,6) Reverse Charge Sum SC
  BasRvsChrg Num(19,6) Base Reverse Charge LC
  BasRvsFc Num(19,6) Base Reverse Charge FC
  BasRvsSc Num(19,6) Base Reverse Charge SC
  ApplRvs Num(19,6) Applied Reverse Charge LC
  ApplRvsFc Num(19,6) Applied Reverse Charge FC
  ApplRvsSc Num(19,6) Applied Reverse Charge SC
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# RIN12 - A/R Credit Memo - Tax Extension
Module: Marketing Documents | 117 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORIN
  TaxId0 nVarChar(100) Tax ID 0
  TaxId1 nVarChar(100) Tax ID 1
  TaxId2 nVarChar(100) Tax ID 2
  TaxId3 nVarChar(100) Tax ID 3
  TaxId4 nVarChar(100) Tax ID 4
  TaxId5 nVarChar(100) Tax ID 5
  TaxId6 nVarChar(100) Tax ID 6
  TaxId7 nVarChar(100) Tax ID 7
  TaxId8 nVarChar(100) Tax ID 8
  TaxId9 nVarChar(100) Tax ID 9
  State nVarChar(3) State Code
  County nVarChar(7) County Code
  Incoterms nVarChar(3) Incoterms
  Vehicle nVarChar(10) Vehicle ID
  VidState nVarChar(3) Vehicle ID (State)
  NfRef nVarChar(254) Nota Fiscal Reference
  Carrier nVarChar(15) Carrier Code
  QoP Int(11) Quantity of Packs
  PackDesc nVarChar(10) Pack Description
  Brand nVarChar(20) Brand
  NoSU Int(11) Number of Shipping Unit
  NetWeight Num(19,6) Net Weight
  GrsWeight Num(19,6) Gross Weight
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=14 ->ADP1
  TaxId10 nVarChar(100) Tax ID 10
  TransCat nVarChar(100) Transaction Category
  FormNo nVarChar(100) Form No.
  TaxId11 nVarChar(100) Tax ID 11
  StreetS nVarChar(100) Street
  BlockS nVarChar(100) Block
  BuildingS Text(16) Building/Floor/Room
  CityS nVarChar(100) City
  ZipCodeS nVarChar(20) Zip Code
  CountyS nVarChar(100) County
  StateS nVarChar(3) State ->OCST
  CountryS nVarChar(3) Country/Region ->OCRY
  AddrTypeS nVarChar(100) Address Type
  StreetNoS nVarChar(100) Street No.
  StreetB nVarChar(100) Street
  BlockB nVarChar(100) Block
  BuildingB Text(16) Building/Floor/Room
  CityB nVarChar(100) City
  ZipCodeB nVarChar(20) Zip Code
  CountyB nVarChar(100) County
  StateB nVarChar(3) State ->OCST
  CountryB nVarChar(3) Country/Region ->OCRY
  AddrTypeB nVarChar(100) Address Type
  StreetNoB nVarChar(100) Street No.
  ImpORExp VarChar(1) Import or Export [N=, Y=]
  Vat VarChar(1) VAT default=N [N=No VAT Support, Y=VAT Support]
  AltCrdNamB nVarChar(100) Alternative BP Name
  AltTaxIdB nVarChar(32) Alternative Tax ID
  Address2S nVarChar(50) Address Name 2
  Address3S nVarChar(50) Address Name 3
  Address2B nVarChar(50) Address Name 2
  Address3B nVarChar(50) Address Name 3
  MainUsage Int(11) Main Usage Code of Document ->OUSG
  GlbLocNumS nVarChar(50) Global Location Number
  GlbLocNumB nVarChar(50) Global Location Number
  CollectDT nVarChar(20) Date and Time of Collection
  TransprtDT Date(8) Transport Starting Date
  TransprtRS nVarChar(100) Transport Reason
  TaxId12 nVarChar(50) Tax ID 12
  TaxId13 nVarChar(100) Deductee Ref. No. in India
  ImpExpNo nVarChar(100) Import/Export Bill No.
  ImpExpDate Date(8) Import/Export Date
  BpGSTType Int(11) GST Regn Type of BP
  BpGSTN nVarChar(15) GST Regn No of BP
  BpStateCod nVarChar(3) State Code of Business Partner ->OCST
  BPStatGSTN nVarChar(2) GST State Code of BP
  LocGSTType Int(11) GST Regn Type of Location
  LocGSTN nVarChar(15) GST Regn No of Location
  LocStatCod nVarChar(3) State Code of Location ->OCST
  LocStaGSTN nVarChar(2) GST State Code of Location
  BpCountry nVarChar(3) Country/Region Code of BP ->OCRY
  OrigImpNo nVarChar(100) Original Bill of Entry No.
  OrigImpDat Date(8) Original Bill of Entry Date
  ExportType VarChar(1) Exporting Type default=E [E=Imports/Exports, S=SEZ Developer, U=SEZ Unit, D=Deemed Imports/Exports]
  PortCode nVarChar(100) Port Code
  BoEValue Num(19,6) Bill of Entry Value
  IsIGSTAct VarChar(1) Supply under IGST Account [Y=Yes, N=No]
  ClaimRefun VarChar(1) Claim Refund [Y=Yes, N=No]
  TaxRateDif Int(11) Differential % of Tax Rate [65=, 100=]
  BPGdsIssP nVarChar(15) Goods Issue Place BP
  CNPJGIP nVarChar(100) Goods Issue Place CNPJ
  CPFGIP nVarChar(100) Goods Issue Place CPF
  StreetGIP nVarChar(100) Goods Issue Place Street
  StrtNoGIP nVarChar(100) Goods Issue Place Street No.
  BldngGIP Text(16) Goods Issue Place Building
  ZipGIP nVarChar(20) Goods Issue Place Zip Code
  BlockGIP nVarChar(100) Goods Issue Place Block
  CityGIP nVarChar(100) Goods Issue Place City
  CountyGIP nVarChar(100) Goods Issue Place County
  StateGIP nVarChar(3) Goods Issue Place State ->OCST
  CountryGIP nVarChar(3) Goods Issue Place Country/Region ->OCRY
  PhoneGIP nVarChar(20) Goods Issue Place Phone
  EMailGIP nVarChar(100) Goods Issue Place E-Mail
  DptDateGIP Date(8) Goods Issue Place Departure Date
  BPDelivryP nVarChar(15) Delivery Place BP
  CNPJDlvryP nVarChar(100) Delivery Place CNPJ
  CPFDlvryP nVarChar(100) Delivery Place CPF
  StrtDlvryP nVarChar(100) Delivery Place Street
  StrNoDlvrP nVarChar(100) Delivery Place Street No.
  BldDlvryP Text(16) Delivery Place Building
  ZipDlvryP nVarChar(20) Delivery Place Zip Code
  BlckDlvryP nVarChar(100) Delivery Place Block
  CityDlvryP nVarChar(100) Delivery Place City
  CntyDlvryP nVarChar(100) Delivery Place County
  StatDlvryP nVarChar(3) Delivery Place State ->OCST
  CtryDlvryP nVarChar(3) Delivery Place Country/Region ->OCRY
  FoneDlvryP nVarChar(20) Delivery Place Phone
  MailDlvryP nVarChar(100) Delivery Place E-Mail
  DpDtDlvryP Date(8) Delivery Place Departure Date
  AuthedCNPJ nVarChar(250) Authorized CNPJ or CPF
  TaxId14 nVarChar(250) ITR Filing

# RIN13 - A/R Credit Memo Rows - Distributed Expenses
Module: Marketing Documents | 59 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORIN
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=14 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Aquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Normal Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) VAT Applied Frgn
  VatAppldSC Num(19,6) VAT Applied Sys
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock default=N [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Line No.
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Abs. Entry default=-1
  BaseGroup Int(11) Base Document Group default=-1
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1
  VisOrder Int(11) Visual Order
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DistribExp VarChar(1) Distribute Freights [Y=Yes, N=No]
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ

# RIN14 - A/R Credit Memo - Assembly - Rows
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORIN
  LineNum Int(11) Row Number default=-1
  ChildNum Int(11) Child Number default=-1
  ItemCode nVarChar(50) Item no. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  TotalQty Num(19,6) Total Quantity
  OpenQty Num(19,6) Remaining Open Quantity
  ObjectType nVarChar(20) object type default=14 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BaseChildN Int(11) Base Child Number default=-1
  EncryptIV nVarChar(100) Encrypt IV

# RIN15 - A/R Cr. Memo - Drawn Dpm Appld
Module: Marketing Documents | 84 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORIN
  LineNum Int(11) Row Number
  ObjType nVarChar(20) object type default=14 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  StaCode nVarChar(8) Tax Authority Code
  StaType Int(11) Tax Authority Type
  StaIndex Int(11) Tax Authority Seq Index
  BaseNet Num(19,6) Net LC
  BaseNetFc Num(19,6) Net FC
  BaseNetSc Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFc Num(19,6) Tax FC
  VatSumSc Num(19,6) Tax SC
  DctSum Num(19,6) Deductible Sum LC
  DctSumFc Num(19,6) Deductible Sum FC
  DctSumSc Num(19,6) Deductible Sum SC
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplNet Num(19,6) Applied Net LC
  ApplNetFc Num(19,6) Applied Net FC
  ApplNetSc Num(19,6) Applied Net SC
  ApplVat Num(19,6) Applied Tax LC
  ApplVatFc Num(19,6) Applied Tax FC
  ApplVatSc Num(19,6) Applied Tax SC
  ApplDct Num(19,6) Applied Deductible Sum LC
  ApplDctFc Num(19,6) Applied Deductible Sum FC
  ApplDctSc Num(19,6) Applied Deductible Sum SC
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  PaidNet Num(19,6) Paid Net LC
  PaidNetFc Num(19,6) Paid Net FC
  PaidNetSc Num(19,6) Paid Net SC
  PaidVat Num(19,6) Paid Tax LC
  PaidVatFc Num(19,6) Paid Tax FC
  PaidVatSc Num(19,6) Paid Tax SC
  PaidDct Num(19,6) Paid Deductible Sum LC
  PaidDctFc Num(19,6) Paid Deductible Sum FC
  PaidDctSc Num(19,6) Paid Deductible Sum SC
  PaidEq Num(19,6) Paid Equalization Sum LC
  PaidEqFc Num(19,6) Paid Equalization Sum FC
  PaidEqSc Num(19,6) Paid Equalization Sum SC
  DpApplNet Num(19,6) Dpm Appl Net LC
  DpApplNetF Num(19,6) Dpm Appl Net FC
  DpApplNetS Num(19,6) Dpm Appl Net SC
  DpApplVat Num(19,6) Dpm Appl Tax LC
  DpApplVatF Num(19,6) Dpm Appl Tax FC
  DpApplVatS Num(19,6) Dpm Appl Tax SC
  DpApplDct Num(19,6) Dpm Appl Deductible Sum LC
  DpApplDctF Num(19,6) Dpm Appl Deductible Sum FC
  DpApplDctS Num(19,6) Dpm Appl Deductible Sum SC
  DpApplEq Num(19,6) Dpm Appl Equalization Sum LC
  DpApplEqFc Num(19,6) Dpm Appl Equalization Sum FC
  DpApplEqSc Num(19,6) Dpm Appl Equalization Sum SC
  TaxCode nVarChar(8) Tax Code ->OSTC
  LineType VarChar(1) Row Type default=D [D=Document, R=Exchange Rate Rounding, H=Document Header Rounding]
  BaseGrs Num(19,6) Gross LC
  BaseGrsFc Num(19,6) Gross FC
  BaseGrsSc Num(19,6) Gross SC
  ApplGrs Num(19,6) Applied Gross LC
  ApplGrsFc Num(19,6) Applied Gross FC
  ApplGrsSc Num(19,6) Applied Gross SC
  PaidGrs Num(19,6) Paid Gross LC
  PaidGrsFc Num(19,6) Paid Gross FC
  PaidGrsSc Num(19,6) Paid Gross SC
  DpApplGrs Num(19,6) Dpm Appl Gross LC
  DpApplGrsF Num(19,6) Dpm Appl Gross FC
  DpApplGrsS Num(19,6) Dpm Appl Gross SC
  RvsChrgSum Num(19,6) Reverse Charge Sum
  RvsChrgSc Num(19,6) Reverse Charge Sum (SC)
  RvsChrgFc Num(19,6) Reverse Charge Sum (FC)
  ApplRvs Num(19,6) Applied Reverse Charge Sum LC
  ApplRvsSc Num(19,6) Applied Reverse Charge Sum SC
  ApplRvsFc Num(19,6) Applied Reverse Charge Sum FC
  PaidRvs Num(19,6) Paid Reverse Charge Sum LC
  PaidRvsSc Num(19,6) Paid Reverse Charge Sum SC
  PaidRvsFc Num(19,6) Paid Reverse Charge Sum FC
  DpApplRvs Num(19,6) Dpm Applied Reverse Charge LC
  DpApplRvsS Num(19,6) Dpm Applied Reverse Charge SC
  DpApplRvsF Num(19,6) Dpm Applied Reverse Charge FC
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# RIN16 - A/R Credit Memo - SnB properties
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, SnBIndex
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) abs entry ->ORIN
  LineNum Int(11) Line Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object id
  ObjAbs Int(11) Object Abs
  DrfWObjAbs Int(11) draft Wobj Abs default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type default=14
  LogInstanc Int(11) Log Instance

# RIN17 - A/R Credit Memo - Import Process
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORIN
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=14 ->ADP1
  ImpDocType VarChar(1) Type of Importation Document ->OBSI
  ImpDocNum nVarChar(10) Importation Document Number
  DateOfReg Date(8) Date of Registry DI/DSI/DA
  CustClrDat Date(8) Date of Customs Clearance
  ConcActNum nVarChar(30) Drawback Concession Acct No.
  AdditNum nVarChar(30) Additional Number
  AddItmDV Num(19,6) Additional Item Discount Value
  tpVTransp Int(6) Overland Transport Route [1=Maritime, 2=Waterway, 3=Lakeside, 4=Air, 5=Post, 6=Train, 7=Road, 8=Network Transmission, 9=Own Means, 10=Input/Output Fictitious, 11=Courier, 12=Hand Carry]
  DrawSReg nVarChar(11) Drawback - Suspension Regime
  AddFrNavyA Num(19,6) Additional Freight to Navy Authority
  TypeOfImp VarChar(1) Type of Import
  nSeqAdic Int(6) Additional Item Sequential Number

# RIN18 - A/R Credit Memo - Export Process
Module: Marketing Documents | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORIN
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=14 ->ADP1
  ExpDocType Int(11) Type of Exportation Document default=-1 ->OBNI
  ExpDeclNum Int(11) Exportation Declaration Number
  ExpDeclDat Date(8) Exportation Declaration Date
  ExpNature Int(11) Nature of Exportation default=-1 ->OBNI
  ExpRegNum Int(11) Number of Exportation Registry
  ExpRegDate Date(8) Date of Exportation Registry
  LadBillNum nVarChar(19) Bill of Lading Number
  LadBillDat Date(8) Date of Bill of Lading
  MerchLeftD Date(8) Date Merchandise Left Customs
  LadBillTyp Int(11) Type of Bill of Lading default=-1 ->OBNI
  DrawSReg nVarChar(11) Drawback - Suspension Regime
  NatureExp nVarChar(44) Nature of Export
  QultExpItm Num(19,6) Quantity of Exported Items
  nSeqAdic Int(6) Additional Item Sequential Number

# RIN19 - A/R Credit Memo - Bin Allocation Data
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, BinAllocSe
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->ORIN
  BinAllocSe Int(11) Bin Allocation Sequence
  LineNum Int(11) Line Number
  SubLineNum Int(11) Subline Number default=-1
  SnBType Int(11) SnB Type default=-1
  SnBMDAbs Int(11) SnB Master Data Internal No. default=-1
  BinAbs Int(11) Bin Internal Number ->OBIN
  Quantity Num(19,6) Quantity
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjType nVarChar(20) Object Type default=14 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  BinActTyp Int(6) Bin Action Type [1=Transaction In, 2=Transaction Out, 4=SnB Complete, 8=Bin First Then SnB]

# RIN2 - A/R Credit Memo - Freight - Rows
Module: Marketing Documents | 64 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORIN
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=14 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) Vat Applied
  VatAppldFC Num(19,6) Vat Applied Frgn
  VatAppldSC Num(19,6) Vat Applied Sys
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report [Y=Yes, N=No]
  BaseGroup Int(11) Base Document Group default=-1 [-1=, 0=, 1=, 2=]
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1 [-1=, 0=, 1=, 2=]
  VisOrder Int(11) Visual Order
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]

# RIN20 - Intrastat Expenses
Module: Marketing Documents | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORIN
  ExpnsCode Int(11) Freight Code ->OEXD
  TotalLC Num(19,6) Total
  TotalFC Num(19,6) Total (FC)
  TotalSC Num(19,6) Total (SC)
  DistribM VarChar(1) Distribution Method default=T [Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DrawnLC Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  LineNum Int(11) Line Number default=-1
  BaseAbsEnt Int(11) Base Abs. Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 16=Return, 13=A/R Invoice, 203=Down Payment Incoming, 204=Down Payment Outgoing, 22=Purchase Order, 20=Goods Receipt PO, 21=Goods Return, 18=A/P Invoice, 540000006=Purchase Quotation, 0=, -1=]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No. default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=14 ->ADP1
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  AppliedLC Num(19,6) Applied
  AppliedFC Num(19,6) Applied (FC)
  AppliedSC Num(19,6) Applied (SC)

# RIN21 - A/R Credit Memo - Document Reference Information
Module: Marketing Documents | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, RefType
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjectType nVarChar(20) Object Type default=14
  LogInstanc Int(11) Log Instance default=0
  RefType VarChar(1) Reference Types default=S [S=System Document, E=External Document]
  LineNum Int(11) Line Number
  RefDocEntr Int(11) Referenced Internal Number
  RefDocNum Int(11) Referenced Document Number
  ExtDocNum nVarChar(100) External Referenced Document Number
  RefObjType nVarChar(20) Referenced Object Type [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 234000031=Return Request, 16=Return, 203=A/R Down Payment, 13=A/R Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 280=A/R Tax Invoice, 1470000113=Purchase Request, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Return Request, 21=Goods Return, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 281=A/P Tax Invoice, 69=Landed Costs, 24=Incoming Payments, 46=Outgoing Payments, 57=Checks for Payment, 321=Internal Reconciliation, 34=Recurring Posting, 30=Journal Entry, 59=Goods Receipt, 60=Goods Issue, 162=Inventory Revaluation, 1470000065=Inventory Counting, 10000071=Inventory Posting, 1250000001=Inventory Transfer Request, 67=Inventory Transfer, 202=Production Order, 13001=Original Invoice, -1=External Document, 20301=Original Down Payment Invoice]
  AccessKey nVarChar(100) Access Key
  IssueDate Date(8) Date of Issue
  IssuerCNPJ nVarChar(100) Issuer CNPJ
  IssuerCode nVarChar(10) Fiscal Document Issuer UF Code
  Model nVarChar(6) Fiscal Document Model
  Series nVarChar(3) Fiscal Document Series
  Number Int(11) Fiscal Document Number
  RefAccKey nVarChar(100) Referenced CT-e Access Key
  RefAmount Num(19,6) Referenced Amount
  SubSeries nVarChar(3) Fiscal Document Subseries
  Remark nVarChar(254) Remarks
  LinkRefTyp nVarChar(20) Link Reference Type default=00 [00=, 01=Nota de cr�dito de los documentos relacionados, 02=Nota de d�bito de los documentos relacionados, 03=Devoluci�n de mercanc�a sobre facturas o traslados previos, 04=Sustituci�n de los CFDI previos, 05=Traslados de mercancias facturados previamente, 06=Factura generada por los traslados previos, 07=CFDI por aplicaci�n de anticipo, 08=Customs, MX_08=Factura generada por pagos en parcialidades, 09=Factura generada por pagos diferidos]

# RIN22 - A/R Credit Memo - Resource Costs
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, StdCostNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->RIN1
  LineNum Int(11) Row Number ->RIN1
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=14
  LogInstanc Int(11) Log Instance default=0

# RIN23 - A/P Invoice - Selected Asset Master Data
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, VisOrder
  ASSETS: DocEntry, LineNum, AssetCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORIN
  LineNum Int(11) Row Number
  AssetCode nVarChar(50) Selected Asset Code ->OITM
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Remarks nVarChar(100) Remarks
  Amount Num(19,6) Amount
  AmountSC Num(19,6) Amount (SC)
  SerialNo nVarChar(30) Serial Number
  VisOrder Int(11) Visual Order
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=14 ->ADP1

# RIN24 - A/R Credit Memo - Tracking Note Assignment
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  ItemCCDNum nVarChar(40) Item CCD Number
  CntrOrigin nVarChar(3) Country/Region of Origin
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=14 ->ADP1
  SubLineNum Int(11) BOM Line No.

# RIN25 - A/R Credit Memo - Amt Per VAT Grp
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, VatGroup, Type
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  VatGroup nVarChar(8) Tax Definition ->OVTG
  VatPrcnt Num(19,6) Tax Rate
  BaseAmnt Num(19,6) Base Amount
  BaseAmntFC Num(19,6) Base Amount (FC)
  BaseAmntSC Num(19,6) Base Amount (SC)
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  Type Int(11) Type default=1 [1=Discount by Tax]
  Currency nVarChar(3) Price Currency
  Rate Num(19,6) Currency Rate
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=14 ->ADP1

# RIN26 - A/R Credit Memo - E-Way Bill Information
Module: Marketing Documents | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORIN
  SuplyType nVarChar(20) EWB Transaction Type [O=Outward, I=Inward]
  SubSplyTyp Int(11) EWB Sub-Type ->OEST
  DocType nVarChar(3) EWB Doc. Type ->OEDT
  TransMode Int(11) EWB Transportation Mode ->OETM
  Distance Num(19,6) EWB Transport Distance
  TransDocNo nVarChar(16) EWB Transporter Doc. No.
  TransDate Date(8) EWB Transportation Date
  VehicleTyp nVarChar(2) EWB Vehicle Type ->OEVT
  VehicleNo nVarChar(15) EWB Vehicle Number
  EWayBillNo nVarChar(20) EWB No.
  EwbDate Date(8) E-Way Bill Date
  FrmTraName nVarChar(100) EWB Consignor Name
  FrmAddres1 nVarChar(120) EWB Consignor Address 1
  FrmAddres2 nVarChar(120) EWB Consignor Address 2
  FrmZipCode nVarChar(20) EWB Consignor Zip Code
  ActFrmStat nVarChar(2) Dispatch State of EWB Consignor
  ToTraName nVarChar(100) EWB Consignee Name
  ToAddres1 nVarChar(120) EWB Consignee Address 1
  ToAddres2 nVarChar(120) EWB Consignee Address 2
  ToZipCode nVarChar(20) EWB Consignee Zip Code
  ActToState nVarChar(2) Ship-To State of EWB Consignee
  FrmGSTN nVarChar(15) EWB Consignor GSTN
  FrmState nVarChar(2) Bill-To State of EWB Consignor
  ToGSTN nVarChar(15) EWB Consignee GSTN
  ToState nVarChar(2) Bill-To State of EWB Consignee
  MainHsnEnt Int(11) EWB Main HSN Entry ->OCHP
  FrmPlace nVarChar(50) EWB Consignor Place
  ToPlace nVarChar(50) EWB Consignee Place
  TransID nVarChar(15) EWB Transporter ID
  TransName nVarChar(25) EWB Transporter Name
  ExpireDate Date(8) EWB Expiration Date
  ObjectType nVarChar(20) Object Type default=14 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TspEntry Int(11) Transporter Abs. Entry ->OTSP
  TspLine Int(11) Transportation Line
  TransType Int(11) Transaction Type [1=Regular, 2=Bill To-Ship To, 3=Bill From-Dispatch From, 4=Combination of 2 and 3]

# RIN27 - A/R Credit Memo - E-Books(GR) Rows
Module: Marketing Documents | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  RELATE_ROW: DocEntry, RelateType, RelateLine, GroupNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORIN
  LineNum Int(11) Row Number
  RelateType Int(11) Relation Type default=-1 [1=Row, 2=Row Expenses, 3=Document Expenses, 13=Distributed Freights, -1=Manual]
  RelateLine Int(11) Relation Row Number default=-1
  GroupNum Int(11) Group Number default=-1
  LineTotal Num(19,6) Line Total
  LineTotalF Num(19,6) Line Total (FC)
  LineTotalS Num(19,6) Line Total (SC)
  InClassTyp Int(11) Income Classification Type ->OICP
  InClassCat Int(11) Income Classification Category ->OICC
  ExClassTyp Int(11) Expense Classification Type ->OECP
  ExClassCat Int(11) Expense Classification Cat. ->OECC
  VatCate Int(11) VAT Category
  NetValue Num(19,6) Net Value
  NetValueFC Num(19,6) Net Value (FC)
  NetValueSC Num(19,6) Net Value (SC)
  VatAmount Num(19,6) VAT Amount
  VatAmFC Num(19,6) VAT Amount (FC)
  VatAmSC Num(19,6) VAT Amount (SC)
  WtPercCat Int(11) Withheld Percentage Category
  WtAmount Num(19,6) Withheld Amount
  WtAmountFC Num(19,6) Withheld Amount (FC)
  WtAmountSC Num(19,6) Withheld Amount (SC)
  ObjectType nVarChar(20) Object Type default=14 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  WtCategory VarChar(1) Withheld Category [I=Invoice, P=Payment]
  VATClassTy Int(11) VAT Classification Type ->OECP
  VATClassCa Int(11) VAT Classification Category ->OECC
  EBVatExCau Int(11) VAT Exemption Cause ->OVEC

# RIN28 - A/R Credit Memo - Reported Tracking Note
Module: Marketing Documents | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
  TCN_KEY U: DocEntry, LineNum, TrackingNt, TrackiNtLn
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  UnusedQty Num(19,6) Unused Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=14 ->ADP1
  SubLineNum Int(11) BOM Line No.

# RIN3 - A/R Credit Memo - Freight
Module: Marketing Documents | 80 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  DOCUMENT: DocEntry, BaseAbsEnt
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORIN
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  Comments nVarChar(100) Remarks
  ObjType nVarChar(20) Object Type default=14 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  WTLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  VatApplied Num(19,6) Vat Applied
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatF Num(19,6) Net Tax Amount (FC)
  LineVatS Num(19,6) Net Tax Amount (SC)
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 16=A/R Returns, 13=A/R Invoice, 203=A/R Down Payment, 234000031=A/R Return Request]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No.
  LineNum Int(11) line num default=-1
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Doc. Internal No. default=-1
  StDstr Num(19,6) Stock Distributed Sum
  StDstrSC Num(19,6) Stock Distributed Sum (SC)
  StDstrFC Num(19,6) Stock Distributed Sum (FC)
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  TaxDistMtd VarChar(1) Tax Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  GrsAmount Num(19,6) Gross Amount
  GrsFC Num(19,6) Gross Amount (FC)
  GrsSC Num(19,6) Gross Amount (SC)
  BaseTotal VarChar(1) Base Total for Calculation default=N [N=Net Total, G=Gross Total]
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)
  RRVatLC Num(19,6) Return Request VAT Amount
  RRVatFC Num(19,6) Return Request VAT Amount (FC)
  RRVatSC Num(19,6) Return Request VAT Amount (SC)
  EncryptIV nVarChar(100) Encrypt IV
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]

# RIN4 - A/R Credit Memo - Tax Amount per Document
Module: Marketing Documents | 61 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SCONDARY: DocEntry, LineNum, GroupNum, ExpnsCode, StcCode, StaCode, staType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORIN
  LineNum Int(11) Row Number default=-1
  GroupNum Int(11) Group Number default=-1
  ExpnsCode Int(11) Expense Code default=-1 ->OEXD
  RelateType Int(11) Relation Type default=1 [1=Row, 2=Row Freight Charges, 3=Document Expenses, 13=Distributed Freights]
  StcCode nVarChar(8) Tax Code ->OSTC
  StaCode nVarChar(8) Authority Code ->OSTA
  staType Int(11) Authority Type ->OSTT
  TaxRate Num(19,6) Tax Rate
  TaxAcct nVarChar(15) Tax Account ->OACT
  TaxSum Num(19,6) Tax Amount
  TaxSumFrgn Num(19,6) Tax Amount (FC)
  TaxSumSys Num(19,6) Tax Amount (SC)
  BaseSum Num(19,6) Base Amount
  BaseSumFrg Num(19,6) Base Amount (FC)
  BaseSumSys Num(19,6) Base Amount (SC)
  ObjectType nVarChar(20) Object Type default=14 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Status default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  LineSeq Int(11) Line Sequence
  DeferrAcct nVarChar(15) Deferred Tax Account ->OACT
  BaseType Int(11) Base Document Type default=-1
  BaseAbs Int(11) Base Doc Abs Entry default=-1
  BaseSeq Int(11) Base Doc. Line Sequence
  DeductTax Num(19,6) Deductible Tax Amount
  DdctTaxFrg Num(19,6) Deductible Tax Amount (FC)
  DdctTaxSys Num(19,6) Deductible Tax Amount (SC)
  BaseAppld Num(19,6) Applied Base Amount
  BaseApldFC Num(19,6) Applied Base Amount (FC)
  BaseApldSC Num(19,6) Applied Base Amount (SC)
  NonDdctPrc Num(19,6) Non Deductible %
  NonDdctAct nVarChar(15) Non Deductible Account ->OACT
  TaxInPrice VarChar(1) Tax Included in Price? default=N [Y=Yes, N=No]
  Exempt VarChar(1) Exempt? default=N [Y=Yes, N=No]
  TaxExpAct nVarChar(15) Expense Account for Tax ->OACT
  OnHoldTax Num(19,6) On Hold Tax Amount
  OnHoldTaxF Num(19,6) On Hold Tax Amount (FC)
  OnHoldTaxS Num(19,6) On Hold Tax Amount (SC)
  InGrossRev VarChar(1) Included in Gross Revenue default=N [Y=Yes, N=No]
  TaxSumOrg Num(19,6) Tax Amount Original
  TaxSumOrgF Num(19,6) Tax Amount Original (FC)
  TaxSumOrgS Num(19,6) Tax Amount Original (SC)
  OpenTax Num(19,6) Open Service Tax
  OpenTaxFC Num(19,6) Open Service Tax (FC)
  OpenTaxSC Num(19,6) Open Service Tax (SC)
  Unencumbrd VarChar(1) Unencumbered default=N [Y=Yes, N=No]
  TaxOnRI VarChar(1) Tax On Reserve Invoice default=N [Y=Yes, N=No]
  RvsChrgPrc Num(19,6) Reverse Charge %
  RvsChrgTax Num(19,6) Reverse Charge Tax Amount
  RvsChrgSC Num(19,6) Reverse Charge Tax Amount (SC)
  RvsChrgFC Num(19,6) Reverse Charge Tax Amount (FC)
  InFirstIns VarChar(1) Included in First Installment default=N [Y=Yes, N=No]
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CESTrel VarChar(1) CEST Relevant default=N [Y=, N=]

# RIN5 - A/R Credit Memo - Withholding Tax
Module: Marketing Documents | 158 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  SECONDERY U: AbsEntry, WTCode, BaseAbsEnt, Doc1LineNo
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator ->ORIN
  WTCode nVarChar(4) WT Code ->OWHT
  Rate Num(19,6) Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntSC Num(19,6) Taxable Amount in SC
  TxblAmntFC Num(19,6) Taxable Amount in FC
  WTAmnt Num(19,6) WT Amount
  WTAmntSC Num(19,6) WT Amount (SC)
  WTAmntFC Num(19,6) WT Amount (FC)
  ApplAmnt Num(19,6) Applied WT Amount
  ApplAmntSC Num(19,6) Applied WTax Amount (SC)
  ApplAmntFC Num(19,6) Applied WTax Amount (FC)
  Category VarChar(1) Category [P=Payment, I=Invoice]
  Criteria VarChar(1) Criteria [Y=Accrual, N=Cash]
  Account nVarChar(15) G/L Account ->OACT
  Type VarChar(1) Withholding Type [V=VAT Withholding, I=Income Tax Withholding]
  RoundType VarChar(1) Rounding Type [T=Truncated, C=Commercial Values, N=No Rounding]
  BaseType VarChar(1) Base Type [G=Gross, N=Net, V=VAT, U=UoM]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseLine Int(11) Base Line
  BaseNum Int(11) Base Document Type default=-1 [-1=, 0=, 16=A/R Returns, 13=A/R Invoice, 203=A/R Down Payment]
  LineNum Int(11) Line Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Abs. Entry default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=14 ->ADP1
  Doc1LineNo Int(11) DOC1 Line Number default=-1
  WtLineType VarChar(1) WT Line Type default=D [D=Document Level WTax, L=Row Level WTax]
  TxblCurr nVarChar(3) Taxable Currency from Doc Line
  DtblCurr nVarChar(3) Deductible Currency
  DtblRate Num(19,6) Rate for Deductible Amount
  txblRate Num(19,6) Rate for Taxable Amount
  DtblAmount Num(19,6) Deductible Amount
  TdsAcc nVarChar(15) TDS Account ->OACT
  SurAcc nVarChar(15) Surcharge Account ->OACT
  CessAcc nVarChar(15) Cess Account ->OACT
  HscAcc nVarChar(15) HSC Account ->OACT
  TdsRate Num(19,6) TDS Rate
  SurRate Num(19,6) Surcharge Rate
  CessRate Num(19,6) Cess Rate
  HscRate Num(19,6) HSC Rate
  TdsBAmt Num(19,6) TDS Base Amount
  TdsBAmtSC Num(19,6) TDS Base Amount (SC)
  TdsBAmtFC Num(19,6) TDS Base Amount (FC)
  SurBAmt Num(19,6) Surcharge Base Amount
  SurBAmtSC Num(19,6) Surcharge Base Amount (SC)
  SurBAmtFC Num(19,6) Surcharge Base Amount (FC)
  CessBAmt Num(19,6) Cess Base Amount
  CessBAmtSC Num(19,6) Cess Base Amount (SC)
  CessBAmtFC Num(19,6) Cess Base Amount (FC)
  HscBAmt Num(19,6) HSC Base Amount
  HscBAmtSC Num(19,6) HSC Base Amount (SC)
  HscBAmtFC Num(19,6) HSC Base Amount (FC)
  TdsAmnt Num(19,6) TDS Tax Amount
  TdsAmntSC Num(19,6) TDS Tax Amount (SC)
  TdsAmntFC Num(19,6) TDS Tax Amount (FC)
  SurAmnt Num(19,6) Surcharge Tax Amount
  SurAmntSC Num(19,6) Surcharge Tax Amount (SC)
  SurAmntFC Num(19,6) Surcharge Tax Amount (FC)
  CessAmnt Num(19,6) Cess Tax Amount
  CessAmntSC Num(19,6) Cess Tax Amount (SC)
  CessAmntFC Num(19,6) Cess Tax Amount (FC)
  HscAmnt Num(19,6) HSC Tax Amount
  HscAmntSC Num(19,6) HSC Tax Amount (SC)
  HscAmntFC Num(19,6) HSC Tax Amount (FC)
  TdsAppl Num(19,6) Applied TDS Amount
  TdsApplSC Num(19,6) Applied TDS Amount (SC)
  TdsApplFC Num(19,6) Applied TDS Amount (FC)
  SurAppl Num(19,6) Applied Surcharge Amount
  SurApplSC Num(19,6) Applied Surcharge Amount (SC)
  SurApplFC Num(19,6) Applied Surcharge Amount (FC)
  CessAppl Num(19,6) Applied Cess Amount
  CessApplSC Num(19,6) Applied Cess Amount (SC)
  CessApplFC Num(19,6) Applied Cess Amount (FC)
  HscAppl Num(19,6) Applied HSC Amount
  HscApplSC Num(19,6) Applied HSC Amount (SC)
  HscApplFC Num(19,6) Applied HSC Amount (FC)
  BatchNum Int(11) Journal Voucher No.
  InCSTCode nVarChar(2) CST Code Incoming
  OutCSTCode nVarChar(2) CST Code Outgoing
  DpmWTApl Num(19,6) DPM WT Applied Amount
  DpmWTAplSC Num(19,6) DPM WT Applied Amount (SC)
  DpmWTAplFC Num(19,6) DPM WT Applied Amount (FC)
  WTTypeId Int(11) WT Type Id ->OWTT
  LnBsAmt Num(19,6) BR Line WT Base Amount
  LnBsAmtSC Num(19,6) BR Line WT Base Amount(SC)
  LnBsAmtFC Num(19,6) BR Line WT Base Amount(FC)
  LnCmTAmt Num(19,6) BR Line Cumulated Taxable Amount
  LnCmTAmtSC Num(19,6) BR Line Cumulated Taxable Amount(SC)
  LnCmTAmtFC Num(19,6) BR Line Cumulated Taxable Amount(FC)
  TDSType VarChar(1) TDS Type [E=eTDS, D=GST TDS, C=GST TCS, S=SALES TCS]
  IgstAcc nVarChar(15) IGST Account ->OACT
  CgstAcc nVarChar(15) CGST Account ->OACT
  SgstAcc nVarChar(15) SGST Account ->OACT
  IgstAmnt Num(19,6) IGST Tax Amount
  IgstAmntSC Num(19,6) IGST Tax Amount (SC)
  IgstAmntFC Num(19,6) IGST Tax Amount (FC)
  CgstAmnt Num(19,6) CGST Tax Amount
  CgstAmntSC Num(19,6) CGST Tax Amount (SC)
  CgstAmntFC Num(19,6) CGST Tax Amount (FC)
  SgstAmnt Num(19,6) SGST Tax Amount
  SgstAmntSC Num(19,6) SGST Tax Amount (SC)
  SgstAmntFC Num(19,6) SGST Tax Amount (FC)
  IgstRate Num(19,6) IGST Rate
  CgstRate Num(19,6) CGST Rate
  SgstRate Num(19,6) SGST Rate
  IgstBAmt Num(19,6) IGST Base Amount
  IgstBAmtSC Num(19,6) IGST Base Amount (SC)
  IgstBAmtFC Num(19,6) IGST Base Amount (FC)
  CgstBAmt Num(19,6) CGST Base Amount
  CgstBAmtSC Num(19,6) CGST Base Amount (SC)
  CgstBAmtFC Num(19,6) CGST Base Amount (FC)
  SgstBAmt Num(19,6) SGST Base Amount
  SgstBAmtSC Num(19,6) SGST Base Amount (SC)
  SgstBAmtFC Num(19,6) SGST Base Amount (FC)
  IgstAppl Num(19,6) Applied IGST Amount
  IgstApplSC Num(19,6) Applied IGST Amount (SC)
  IgstApplFC Num(19,6) Applied IGST Amount (FC)
  CgstAppl Num(19,6) Applied CGST Amount
  CgstApplSC Num(19,6) Applied CGST Amount (SC)
  CgstApplFC Num(19,6) Applied CGST Amount (FC)
  SgstAppl Num(19,6) Applied SGST Amount
  SgstApplSC Num(19,6) Applied SGST Amount (SC)
  SgstApplFC Num(19,6) Applied SGST Amount (FC)
  UtgstAcc nVarChar(15) UTGST Account ->OACT
  CsgstAcc nVarChar(15) Cess GST Account ->OACT
  UtgstAmt Num(19,6) UTGST Tax Amount
  UtgstAmtSC Num(19,6) UTGST Tax Amount (SC)
  UtgstAmtFC Num(19,6) UTGST Tax Amount (FC)
  CsgstAmt Num(19,6) Cess GST Tax Amount
  CsgstAmtSC Num(19,6) Cess GST Tax Amount (SC)
  CsgstAmtFC Num(19,6) Cess GST Tax Amount (FC)
  UtgstRate Num(19,6) UTGST Rate
  CsgstRate Num(19,6) Cess GST Rate
  UtgstBAmt Num(19,6) UTGST Base Amount
  UtgstBAmtS Num(19,6) UTGST Base Amount (SC)
  UtgstBAmtF Num(19,6) UTGST Base Amount (FC)
  CsgstBAmt Num(19,6) Cess GST Base Amount
  CsgstBAmtS Num(19,6) Cess GST Base Amount (SC)
  CsgstBAmtF Num(19,6) Cess GST Base Amount (FC)
  UtgstAppl Num(19,6) Applied UTGST Amount
  UtgstApplS Num(19,6) Applied UTGST Amount (SC)
  UtgstApplF Num(19,6) Applied UTGST Amount (FC)
  CsgstAppl Num(19,6) Applied Cess GST Amount
  CsgstApplS Num(19,6) Applied Cess GST Amount (SC)
  CsgstApplF Num(19,6) Applied Cess GST Amount (FC)
  EncryptIV nVarChar(100) Encrypt IV
  TcsIntAcct nVarChar(15) TCS Interim Account ->OACT
  SurIntAcct nVarChar(15) Surcharge Interim Account ->OACT
  CesIntAcct nVarChar(15) Cess Interim Account ->OACT
  HscIntAcct nVarChar(15) HSC interim Account ->OACT
  LnIntAcct nVarChar(15) Interim Account for Tax ->OACT
  FixedAmnt Num(19,6) Fixed Amount
  FixedAmtSC Num(19,6) Fixed Amount (SC)
  FixedAmtFC Num(19,6) Fixed Amount (FC)
  BaseQty Num(19,6) Base Quantity

# RIN6 - A/R Credit Memo - Installments
Module: Marketing Documents | 65 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, InstlmntID
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORIN
  InstlmntID Int(6) Installment ID default=1
  ObjType nVarChar(20) Object Type default=14 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DueDate Date(8) Due Date
  Status VarChar(1) Installment Status default=O [O=Open, C=Closed]
  DunnLevel Int(11) Dunning Level default=0
  InsTotal Num(19,6) Total Installment
  InsTotalFC Num(19,6) Total Installment (FC)
  InsTotalSy Num(19,6) Total Installment (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  VatSum Num(19,6) Total Tax
  VatSumFC Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  VatPaid Num(19,6) Tax Paid to Date
  VatPaidFC Num(19,6) Tax Paid (FC)
  VatPaidSys Num(19,6) Tax Paid (SC)
  TotalExpns Num(19,6) Total Freight Charges
  TotalExpFC Num(19,6) Total Freight Charges (FC)
  TotalExpSC Num(19,6) Total Freight Charges (SC)
  ExpAppl Num(19,6) Applied Freight Charges
  ExpApplFC Num(19,6) Applied Freight Charges (SC)
  ExpApplSC Num(19,6) Applied Freight Charges (SC)
  WTSum Num(19,6) WTax Amount
  WTSumFC Num(19,6) WTax Amount (FC)
  WTSumSC Num(19,6) WTax Amount (SC)
  WTApplied Num(19,6) Applied WTax
  WTAppliedF Num(19,6) Applied WTax (FC)
  WTAppliedS Num(19,6) Applied WTax (SC)
  TotalBlck Num(19,6) Total Reserved Amount
  TotalBlckF Num(19,6) Total Reserved Amount (FC)
  TotalBlckS Num(19,6) Total Reserved Amount (SC)
  VATBlck Num(19,6) Reserved Tax
  VATBlckFC Num(19,6) Reserved Tax (FC)
  VATBlckSC Num(19,6) Reserved Tax (SC)
  ExpnsBlck Num(19,6) Reserved Freight Charges
  ExpnsBlckF Num(19,6) Reserved Freight Charges (FC)
  ExpnsBlckS Num(19,6) Reserved Freight Charges (SC)
  WTBlocked Num(19,6) Reserved WTax Amount
  WTBlockedF Num(19,6) Reserved WTax Amount (FC)
  WTBlockedS Num(19,6) Reserved WTax Amount (SC)
  InstPrcnt Num(19,6) Installment %
  DunWizBlck VarChar(1) Wizard dunning block default=N [N=No, Y=Yes]
  DunDate Date(8) Last Dunning Date
  Paid Num(19,6) Paid
  PaidFrgn Num(19,6) Paid (FC)
  PaidSc Num(19,6) Paid (SC)
  reserved VarChar(1) Reserved default=N [N=No, Y=Yes]
  TaxOnExp Num(19,6) Tax on Expenses
  TaxOnExpFc Num(19,6) Tax on Expenses (FC)
  TaxOnExpSc Num(19,6) Tax on Expenses (SC)
  TaxOnExpAp Num(19,6) Applied Tax on Expenses
  TaxOnExApF Num(19,6) Applied Tax on Expenses (FC)
  TaxOnExApS Num(19,6) Applied Tax on Expenses (SC)
  TaxOnExBlo Num(19,6) Reserved Tax on Freight Amount
  TaxOnExBlF Num(19,6) Reserved Tax on Freight Amt FC
  TaxOnExBlS Num(19,6) Reserved Tax on Freight Amt SC
  LvlUpdDate Date(8) Dunning Level Update Date
  Ordered VarChar(1) Payment Ordered default=N [Y=Yes, N=No]
  PaidDpm Num(19,6) Paid by Down Payment
  PaidDpmFc Num(19,6) Paid by Down Payment (FC)
  PaidDpmSc Num(19,6) Paid by Down Payment (SC)
  EncryptIV nVarChar(100) Encrypt IV

# RIN7 - A/R Credit Memo - Delivery Packages
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORIN
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type default=14 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV

# RIN8 - Items in Package - A/R Credit Memo
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum, ItemCode, UomEntry, NumPerMsr
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORIN
  PackageNum Int(11) Package Number
  ItemCode nVarChar(50) Item Code ->OITM
  Quantity Num(19,6) Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=14 ->ADP1
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value default=0

# RIN9 - A/R Credit Memo - Drawn Dpm
Module: Marketing Documents | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORIN
  LineNum Int(11) Row Number
  BaseAbs Int(11) Base Document Internal ID ->ODPI
  BaseLine Int(11) Base Document Row
  TargetBase VarChar(1) Target or Base Document default=B [B=Base, T=Target]
  ObjType nVarChar(20) Base Object Type
  DrawnSum Num(19,6) Net LC
  DrawnSumFc Num(19,6) Net FC
  DrawnSumSc Num(19,6) Net SC
  LogInstanc Int(11) Log Instance default=0
  ObjCode nVarChar(20) Object Type default=14 ->ADP1
  ApplDrawn Num(19,6) Applied Net LC
  ApplDrawnF Num(19,6) Applied Net FC
  ApplDrawnS Num(19,6) Applied Net SC
  BaseDocNum Int(11) Base Document Number
  BsDocDate Date(8) Base Posting Date
  BsDueDate Date(8) Base Due Date
  BsCardName nVarChar(100) Base BP Name
  BsComments nVarChar(254) Base Remarks
  Posted VarChar(1) Base Document Posted default=Y [Y=Yes, N=No]
  Vat Num(19,6) Tax LC
  VatFc Num(19,6) Tax FC
  VatSc Num(19,6) Tax SC
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  IsGross VarChar(1) Is Gross Line default=N [N=Net Line, Y=Gross Line]

# RPC1 - A/P Credit Memo - Rows
Module: Marketing Documents | 317 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  STATUS: LineStatus
  CURRENCY: Currency
  ACCOUNT: AcctCode
  BASE_ENTRY: BaseEntry, BaseType, BaseLine
  VIS_ORDER: DocEntry, VisOrder
  OWNER_CODE: OwnerCode
  ITM_WHS_OQ: ItemCode, WhsCode, OpenQty
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPC
  LineNum Int(11) Row Number
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=]
  TrgetEntry Int(11) Target Document Internal ID
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 18=A/P Invoice, 21=Goods Return, 204=A/P Down Payment, 19=A/P Credit Memo, 234000032=A/P Return Request]
  BaseEntry Int(11) Base Document Internal ID
  BaseLine Int(11) Base Row
  LineStatus VarChar(1) Row Status default=O [O=Open, C=Closed]
  ItemCode nVarChar(50) Item No. ->OITM
  Dscription nVarChar(200) Item/Service Description
  Quantity Num(19,6) Quantity
  ShipDate Date(8) Row Delivery Date
  OpenQty Num(19,6) Remaining Open Quantity
  Price Num(19,6) Price
  Currency nVarChar(3) Price Currency ->OCRN
  Rate Num(19,6) Currency Rate
  DiscPrcnt Num(19,6) Discount % per Row
  LineTotal Num(19,6) Row Total
  TotalFrgn Num(19,6) Row Total (FC)
  OpenSum Num(19,6) Open Amount
  OpenSumFC Num(19,6) Open Amount (FC)
  VendorNum nVarChar(50) Vendor Catalog No.
  SerialNum nVarChar(17) Serial Number
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  SlpCode Int(11) Sales Employee Code default=-1 ->OSLP
  Commission Num(19,6) Commission Percentage
  TreeType VarChar(1) BOM Type default=N [N=Not a BOM, A=Assembly, S=Sales, I=Sales BOM Component, P=Production, T=Template]
  AcctCode nVarChar(15) Account Code ->OACT
  TaxStatus VarChar(1) Tax Definition [Y=Yes, N=No]
  GrossBuyPr Num(19,6) Gross Profit Base Price
  PriceBefDi Num(19,6) Unit Price
  DocDate Date(8) Posting Date
  Flags Int(11) Flags default=0
  OpenCreQty Num(19,6) Credit Memo Amount
  UseBaseUn VarChar(1) Inventory UoM default=N [Y=Yes, N=No]
  SubCatNum nVarChar(50) BP Catalog No. ->OSCN
  BaseCard nVarChar(15) Base BP Code ->OCRD
  TotalSumSy Num(19,6) Row Total (SC)
  OpenSumSys Num(19,6) Open Amount (SC)
  InvntSttus VarChar(1) Warehouse Status default=O [O=Open, C=Closed]
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  CodeBars nVarChar(254) Bar Code
  VatPrcnt Num(19,6) Tax Rate per Row
  VatGroup nVarChar(8) Tax Definition ->OVTG
  PriceAfVAT Num(19,6) Gross Price after Discount
  Height1 Num(19,6) Height 1
  Hght1Unit Int(6) Unit of Height 1
  Height2 Num(19,6) Height 2
  Hght2Unit Int(6) Unit of Height 2
  Width1 Num(19,6) Width 1
  Wdth1Unit Int(6) Unit of Width 1
  Width2 Num(19,6) Width 2
  Wdth2Unit Int(6) Unit of Width 2
  Length1 Num(19,6) Length 1
  Len1Unit Int(6) Unit of Length 1
  length2 Num(19,6) Length 2
  Len2Unit Int(6) Unit of Length 2
  Volume Num(19,6) Quantity
  VolUnit Int(6) Vol. Unit
  Weight1 Num(19,6) Weight 1
  Wght1Unit Int(6) Unit of Weight 1
  Weight2 Num(19,6) Weight 2
  Wght2Unit Int(6) Unit of Weight 2
  Factor1 Num(19,6) Factor 1
  Factor2 Num(19,6) Factor 2
  Factor3 Num(19,6) Factor 3
  Factor4 Num(19,6) Factor 4
  PackQty Num(19,6) Packing Quantity
  UpdInvntry VarChar(1) Warehouse Update default=Y [Y=Yes, N=No]
  BaseDocNum Int(11) Base Document No.
  BaseAtCard nVarChar(100) Customer/Vendor Base Document
  SWW nVarChar(16) Additional Identifier
  VatSum Num(19,6) Total Tax
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  FinncPriod Int(11) Posting Period ->OFPR
  ObjType nVarChar(20) Object Type default=19 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BlockNum nVarChar(100) Block Number
  ImportLog nVarChar(20) Import Log
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAqcuistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  DistribSum Num(19,6) Distributed Amount
  DstrbSumFC Num(19,6) Distributed Amount (FC)
  DstrbSumSC Num(19,6) Distributed Amount (SC)
  GrssProfit Num(19,6) Row Gross Profit
  GrssProfSC Num(19,6) Row Gross Profit (SC)
  GrssProfFC Num(19,6) Row Gross Profit (FC)
  VisOrder Int(11) Visual Order
  INMPrice Num(19,6) Item's Last Sales Price (OINM)
  PoTrgNum Int(11) PO Target No.
  PoTrgEntry nVarChar(11) PO Target Internal ID
  DropShip VarChar(1) Drop-Ship default=N [Y=Yes, N=No]
  PoLineNum Int(11) PO Target Row No.
  Address nVarChar(254) Address
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type [Y=Regular Tax, N=No Tax, U=Use Tax]
  OrigItem nVarChar(50) Original Item ->OITM
  BackOrdr VarChar(1) Allow Backorder [Y=Yes, N=No]
  FreeTxt nVarChar(100) Free Text
  PickStatus VarChar(1) Pick Status default=N [Y=Picked, N=Not Picked, R=Released for Picking, P=Partially Picked]
  PickOty Num(19,6) Pick Quantity
  PickIdNo Int(11) Pick ID
  TrnsCode Int(6) Shipping Method default=-1 ->OSHP
  VatAppld Num(19,6) Applied Tax
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  BaseQty Num(19,6) Base Quantity
  BaseOpnQty Num(19,6) Base Open Quantity
  VatDscntPr Num(19,6) Tax Discount %
  WtLiable VarChar(1) Withholding Tax Liable [Y=Yes, N=No]
  DeferrTax VarChar(1) Deferred Tax default=N [Y=Yes, N=No]
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatlF Num(19,6) Net Tax Amount
  LineVatS Num(19,6) Net Tax Amount
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value
  CEECFlag VarChar(1) Correction Invoice Was/Should Be default=S [W=Was, S=Should Be]
  ToStock Num(19,6) Corr. Invoice Amt to Inventory
  ToDiff Num(19,6) Corr. Invoice Amount to Diff.
  ExciseAmt Num(19,6) Excise Amount
  TaxPerUnit Num(19,6) Tax per Unit
  TotInclTax Num(19,6) Total Including Tax
  CountryOrg nVarChar(3) Country/Region of Origin
  StckDstSum Num(19,6) Stock Distribution Sum
  ReleasQtty Num(19,6) Released Quantity
  LineType VarChar(1) Row Type default=R [R=Regular]
  TranType VarChar(1) Transaction Type [C=Complete, R=Reject]
  Text Text(16) Text
  OwnerCode Int(11) Document Owner
  StockPrice Num(19,6) Inventory Price
  ConsumeFCT VarChar(1) Consumer Sales Forecast [Y=Yes, N=No]
  LstByDsSum Num(19,6) Last Buy Distribute Sum
  StckINMPr Num(19,6) Stock Inm Price
  LstBINMPr Num(19,6) Last Buy Inventory Journal Pr.
  StckDstFc Num(19,6) Stock Distribution Sum (FC)
  StckDstSc Num(19,6) Stock Distribution Sum (SC)
  LstByDsFc Num(19,6) Last Buy Distribute Sum (FC)
  LstByDsSc Num(19,6) Last Buy Distribute Sum (SC)
  StockSum Num(19,6) Stock Sum
  StockSumFc Num(19,6) Stock Sum FC
  StockSumSc Num(19,6) Stock Sum SC
  StckSumApp Num(19,6) Stock Sum Applied
  StckAppFc Num(19,6) Stock Sum Applied FC
  StckAppSc Num(19,6) Stock Sum Applied SC
  ShipToCode nVarChar(50) Ship-to Code
  ShipToDesc nVarChar(254) Ship-to Description
  StckAppD Num(19,6) Stock Distrib. - Applied Sum
  StckAppDFC Num(19,6) Stock Dist. - Applied Sum (FC)
  StckAppDSC Num(19,6) Stock Dist. - Applied Sum (SC)
  BasePrice VarChar(1) Price for Total Calculation default=E [E=Exclude Tax, I=Include Tax]
  GTotal Num(19,6) Gross Total
  GTotalFC Num(19,6) Gross Total (FC)
  GTotalSC Num(19,6) Gross Total (SC)
  DistribExp VarChar(1) Distribute Freight [Y=Yes, N=No]
  DescOW VarChar(1) Description Overwritten default=N [Y=Yes, N=No]
  DetailsOW VarChar(1) Details Overwritten default=N [Y=Yes, N=No]
  GrossBase Int(6) Base Method for Gross Profit
  VatWoDpm Num(19,6) Tax Before DPM Applied
  VatWoDpmFc Num(19,6) Tax Before DPM Applied (FC)
  VatWoDpmSc Num(19,6) Tax Before DPM Applied (SC)
  CFOPCode nVarChar(6) CFOP Code for Document ->OCFP
  CSTCode nVarChar(6) CST Code for ICMS
  Usage Int(11) Usage Code for Document ->OUSG
  TaxOnly VarChar(1) Tax Only [Y=Yes, N=No]
  WtCalced VarChar(1) Withholding Tax Calculated default=N [N=No, Y=Yes]
  QtyToShip Num(19,6) Quantity to Ship
  DelivrdQty Num(19,6) Delivered Quantity
  OrderedQty Num(19,6) Ordered Quantity
  CogsOcrCod nVarChar(8) COGS Distribution Rule Code ->OOCR
  CiOppLineN Int(11) Line Number of Opposite Line default=-1
  CogsAcct nVarChar(15) COGS Account Code ->OACT
  ChgAsmBoMW VarChar(1) Change Whs for Asm BoM Child [Y=Yes, N=No]
  ActDelDate Date(8) Actual Delivery Date
  OcrCode2 nVarChar(8) Costing Code 2 ->OOCR
  OcrCode3 nVarChar(8) Costing Code 3 ->OOCR
  OcrCode4 nVarChar(8) Costing Code 4 ->OOCR
  OcrCode5 nVarChar(8) Costing Code 5 ->OOCR
  TaxDistSum Num(19,6) Tax Distributed Amount
  TaxDistSFC Num(19,6) Tax Distributed Amount (FC)
  TaxDistSSC Num(19,6) Tax Distributed Amount (SC)
  PostTax VarChar(1) Post Tax in Price to Stock default=Y [Y=Yes, N=No]
  Excisable VarChar(1) Excisable [Yes/No] [Y=Yes, N=No]
  AssblValue Num(19,6) Assessable Value
  RG23APart1 Int(11) RG23A Part1 Number
  RG23APart2 Int(11) RG23A Part2 Number
  RG23CPart1 Int(11) RG23C Part1 Number
  RG23CPart2 Int(11) RG23C Part2 Number
  CogsOcrCo2 nVarChar(8) COGS Distribution Rule Code2 ->OOCR
  CogsOcrCo3 nVarChar(8) COGS Distribution Rule Code3 ->OOCR
  CogsOcrCo4 nVarChar(8) COGS Distribution Rule Code4 ->OOCR
  CogsOcrCo5 nVarChar(8) COGS Distribution Rule Code5 ->OOCR
  LnExcised VarChar(1) Line Excised [O=Open, C=Closed, P=Copied to OEI]
  LocCode Int(11) Location Code ->OLCT
  StockValue Num(19,6) Total COGS Value
  GPTtlBasPr Num(19,6) Total Base Price for Profit
  unitMsr2 nVarChar(100) Pur/Sal UoM if BaseUnit
  NumPerMsr2 Num(19,6) Pur/Sal UoM Value if Base Unit
  SpecPrice VarChar(1) Price Source Type default=N [Y=Special Prices for Business Partner, N=Manual, W=Active Price List, Discount Groups, R=Active Price List, U=Inactive Price List, A=Blanket Agreement, P=Period and Volume Discounts, Q=Period and Volume Discounts, Discount Groups, V=Inactive Price List, Discount Groups, 9=Special Prices for Business Partner, !=Blanket Agreement, 0=Period and Volume Discounts, 1=Period and Volume Discounts, Discount Groups, 2=Active Price List, 7=Active Price List, Discount Groups, 5=Inactive Price List, 6=Inactive Price List, Discount Groups]
  CSTfIPI nVarChar(2) CST for IPI Code
  CSTfPIS nVarChar(2) CST for PIS Code
  CSTfCOFINS nVarChar(2) CST for COFINS Code
  ExLineNo nVarChar(10) ExLineNo
  isSrvCall VarChar(1) Created from Service Call default=N [Y=Yes, N=No]
  PQTReqQty Num(19,6) Pur Quotation: Required Qty
  PQTReqDate Date(8) Pur Quotation: Required Date
  PcDocType Int(11) Purchase Confirmation Doc Type default=-1 [-1=No Type, 22=Purchase Order, 540000006=Purchase Quotation]
  PcQuantity Num(19,6) Purchase Confirmation Quantity
  LinManClsd VarChar(1) Line Was Closed Manually default=N [Y=Yes, N=No, U=Unknown]
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  NoInvtryMv VarChar(1) Without Inventory Movement default=N [Y=Yes, N=No]
  ActBaseEnt Int(11) Actual Base Document Entry
  ActBaseLn Int(11) Actual Base Line Number
  ActBaseNum Int(11) Actual Base Document No.
  OpenRtnQty Num(19,6) Quantity Open for Return
  AgrNo Int(11) Agreement No. ->OOAT
  AgrLnNum Int(11) Agreement Row Number
  CredOrigin VarChar(1) Credit Origin ->OBSI
  Surpluses Num(19,6) Surpluses
  DefBreak Num(19,6) Defect and Breakup
  Shortages Num(19,6) Shortages
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  UomEntry2 Int(11) UoM Entry if Base Unit default=0 ->OUOM
  UomCode nVarChar(20) UoM Code
  UomCode2 nVarChar(20) UoM Code if Base Unit
  FromWhsCod nVarChar(8) From Warehouse Code ->OWHS
  NeedQty VarChar(1) Consider Quantity of Items default=N [Y=Yes, N=No]
  PartRetire VarChar(1) Partial Retirement default=N [Y=Yes, N=No]
  RetireQty Num(19,6) Retirement Quantity
  RetireAPC Num(19,6) Retirement APC
  RetirAPCFC Num(19,6) Retirement APC FC
  RetirAPCSC Num(19,6) Retirement APC SC
  InvQty Num(19,6) Quantity - Inventory UoM
  OpenInvQty Num(19,6) Open Quantity (Inventory UoM)
  EnSetCost VarChar(1) Enable Set Item Cost in Return default=N [Y=Yes, N=No]
  RetCost Num(19,6) Return Cost in A/R Return
  Incoterms Int(11) Incoterms default=0 ->ODCI
  TransMod Int(11) Transport Mode default=0 ->ODCI
  LineVendor nVarChar(15) Line Vendor Code ->OCRD
  DistribIS VarChar(1) Distribute Intrastat Freight default=N [Y=Yes, N=No]
  ISDistrb Num(19,6) Intrastat Distrib. Amount
  ISDistrbFC Num(19,6) Intrastat Distrib. Amount (FC)
  ISDistrbSC Num(19,6) Intrastat Distrib. Amount (SC)
  IsByPrdct VarChar(1) Item Is By-Product default=N [N=No, Y=Yes]
  ItemType Int(11) Item Type default=4 [4=Item]
  PriceEdit VarChar(1) Price Was Edited by User default=N [N=No, Y=Yes]
  PrntLnNum Int(11) Parent Line Number
  LinePoPrss VarChar(1) Line PO Process default=N [Y=Yes, N=No]
  FreeChrgBP VarChar(1) Free of Charge (BP) default=N [Y=Yes, N=No]
  TaxRelev VarChar(1) Tax Relevant Row default=Y [Y=Yes, N=No]
  LegalText nVarChar(254) Legal Text
  ThirdParty VarChar(1) Third Party default=N [Y=Yes, N=No]
  LicTradNum nVarChar(32) Federal Tax ID
  InvQtyOnly VarChar(1) Change Qty (Inv. UoM) Only default=N [Y=Yes, N=No]
  UnencReasn Int(11) Reason for Unencumbered ICMS
  ShipFromCo nVarChar(50) Ship-From Code
  ShipFromDe nVarChar(254) Ship-From Description
  FisrtBin nVarChar(228) First Bin Location
  AllocBinC nVarChar(11) Allocated Bin Location Count
  ExpType nVarChar(4) Expense Type ->OEXD
  ExpUUID nVarChar(50) Expense UUID
  ExpOpType VarChar(1) Expense Operation Type [P=Professional Services, R=Renting Assets, O=Others]
  DIOTNat nVarChar(3) DIOT Nationality ->OCRY
  MYFtype nVarChar(2) MYF type [S1=MYF Wholesale Sales, S2=Retail Sales, P1=MYF Wholesale Purchases, P3=Other Expense Transactions]
  GPBefDisc Num(19,6) Gross Price
  ReturnRsn Int(6) Return Reason default=-1
  ReturnAct Int(6) Return Action default=-1
  StgSeqNum Int(11) Stage Sequence Number
  StgEntry Int(11) Stage Entry ->ORST
  StgDesc nVarChar(100) Stage Description
  ItmTaxType nVarChar(2) Item GST Tax Category [GR=GST Regular, GN=GST Nil Rated, GE=GST Exempt, NE=Excisable, NN=Non-GST Non-Excisable]
  SacEntry Int(11) SAC Entry ->OSAC
  NCMCode Int(11) NCM Code default=-1 ->ONCM
  HsnEntry Int(11) HSN Entry
  OriBAbsEnt Int(11) Original Base Document Internal ID
  OriBLinNum Int(11) Original Base Document Line Number
  OriBDocTyp Int(11) Original Base Document Type
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No, U=Use]
  EncryptIV nVarChar(100) Encrypt IV
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  StdItemId Int(11) Standard Item Identification ->OUNCL
  CommClass Int(11) Commodity Classification ->OUNCL
  VatExEntry Int(11) VAT Exemption AbsEntry ->OVEB
  VatExLN Int(6) VAT Exemption LineNum
  NatOfTrans Int(11) Nature of Transaction ->ODCI
  ISDtCryImp nVarChar(3) Destination Country/Region for Import ->OCRY
  ISDtRgnImp Int(11) Destination Region for Import ->ODCI
  ISOrCryExp nVarChar(3) Country/Region of Origin for Export ->OCRY
  ISOrRgnExp Int(11) Region of Origin for Export ->ODCI
  NVECode nVarChar(6) NVE Code
  PoNum nVarChar(20) Customer's Purchase Order Number
  PoItmNum Int(11) Customer's Purchase Order Item Number
  IndEscala VarChar(1) Indicator for Relevant Scale default=N [Y=Yes, N=No]
  CESTCode Int(11) CEST Code ->OCEST
  CtrSealQty Num(19,6) Control Seal Quantity
  CNJPMan nVarChar(14) CNPJ of Manufacturer
  UFFiscBene nVarChar(10) UF Fiscal Benefit Code
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]
  LegalTIMD nVarChar(250) Legal Text from Item Master Data
  LegalTTCA nVarChar(250) Legal Text from Tax Code Attributes
  LegalTW nVarChar(250) Legal Text from Warehouse
  LegalTCD nVarChar(250) Legal Text from Tax Code Determination
  RevCharge VarChar(1) Reverse Charge default=N [Y=Yes, N=No]
  ListNum Int(6) Price List No. ->OPLN

# RPC10 - A/P Credit Memo - Row Structure
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SECONDERY U: DocEntry, AftLineNum, OrderNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPC
  LineSeq Int(11) Row Sequence
  AftLineNum Int(11) After Row Number
  OrderNum Int(11) Order Number
  LineType VarChar(1) Row Type [T=Text, S=Subtotal]
  LineText Text(16) Row Text
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=19 ->ADP1

# RPC11 - A/P Cr. Memo - Drawn Dpm Det.
Module: Marketing Documents | 70 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LineSeq
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPC
  LineNum Int(11) Row Number
  LineSeq Int(11) Sequence Number
  BaseAbs Int(11) Base Document Internal ID default=-1 ->ODPO
  BaseType Int(11) Base Object Type default=204 [204=A/P Down Payment]
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  VatPrcnt Num(19,6) VAT Percent
  LineTotal Num(19,6) Net LC
  TotalFrgn Num(19,6) Net FC
  TotalSumSy Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFrgn Num(19,6) Tax FC
  VatSumSys Num(19,6) Tax SC
  ObjType nVarChar(20) Object Type default=19 ->ADP1
  LogInstanc Int(11) Log Instance
  IsAcq VarChar(1) Acquisition Tax-Liable default=N [N=No, Y=Yes]
  IsAllDrawn VarChar(1) Remaining Amount Drawn default=N [Y=Yes, N=No]
  IsGross VarChar(1) Is Gross Line default=N [N=Net Line, Y=Gross Line]
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  ApplNet Num(19,6) Applied Net LC
  ApplNetFc Num(19,6) Applied Net FC
  ApplNetSc Num(19,6) Applied Net SC
  ApplVat Num(19,6) Applied Tax LC
  ApplVatFc Num(19,6) Applied Tax FC
  ApplVatSc Num(19,6) Applied Tax SC
  BaseNet Num(19,6) Base Net LC
  BaseNetFc Num(19,6) Base Net FC
  BaseNetSc Num(19,6) Base Net SC
  BaseVat Num(19,6) Base Tax LC
  BaseVatFc Num(19,6) Base Tax FC
  BaseVatSc Num(19,6) Base Tax SC
  BaseGross Num(19,6) Base Gross LC
  BaseGrossF Num(19,6) Base Gross FC
  BaseGrossS Num(19,6) Base Gross SC
  LineType VarChar(1) Line Type default=D [D=Document Row, R=Currency Rounding, H=Down Payment Document Rounding]
  DctSum Num(19,6) Deductible Sum LC
  DctSumFc Num(19,6) Deductible Sum FC
  DctSumSc Num(19,6) Deductible Sum SC
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplDct Num(19,6) Applied Deductible Sum LC
  ApplDctFc Num(19,6) Applied Deductible Sum FC
  ApplDctSc Num(19,6) Applied Deductible Sum SC
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  BaseDct Num(19,6) Base Deductible Sum LC
  BaseDctFc Num(19,6) Base Deductible Sum FC
  BaseDctSc Num(19,6) Base Deductible Sum SC
  BaseEq Num(19,6) Base Equalization Sum LC
  BaseEqFc Num(19,6) Base Equalization Sum FC
  BaseEqSc Num(19,6) Base Equalization Sum SC
  TaxCode nVarChar(8) Tax Code ->OSTC
  ApplGross Num(19,6) Applied Gross LC
  ApplGrossF Num(19,6) Applied Gross FC
  ApplGrossS Num(19,6) Applied Gross SC
  TaxAdjust VarChar(1) Manual Tax Adjustment default=N [Y=Yes, N=No]
  RvsChrgSum Num(19,6) Reverse Charge Sum LC
  RvsChrgFc Num(19,6) Reverse Charge Sum FC
  RvsChrgSc Num(19,6) Reverse Charge Sum SC
  BasRvsChrg Num(19,6) Base Reverse Charge LC
  BasRvsFc Num(19,6) Base Reverse Charge FC
  BasRvsSc Num(19,6) Base Reverse Charge SC
  ApplRvs Num(19,6) Applied Reverse Charge LC
  ApplRvsFc Num(19,6) Applied Reverse Charge FC
  ApplRvsSc Num(19,6) Applied Reverse Charge SC
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# RPC12 - A/P Credit Memo - Tax Extension
Module: Marketing Documents | 117 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPC
  TaxId0 nVarChar(100) Tax ID 0
  TaxId1 nVarChar(100) Tax ID 1
  TaxId2 nVarChar(100) Tax ID 2
  TaxId3 nVarChar(100) Tax ID 3
  TaxId4 nVarChar(100) Tax ID 4
  TaxId5 nVarChar(100) Tax ID 5
  TaxId6 nVarChar(100) Tax ID 6
  TaxId7 nVarChar(100) Tax ID 7
  TaxId8 nVarChar(100) Tax ID 8
  TaxId9 nVarChar(100) Tax ID 9
  State nVarChar(3) State Code
  County nVarChar(7) County Code
  Incoterms nVarChar(3) Incoterms
  Vehicle nVarChar(10) Vehicle ID
  VidState nVarChar(3) Vehicle ID (State)
  NfRef nVarChar(254) Nota Fiscal Reference
  Carrier nVarChar(15) Carrier Code
  QoP Int(11) Quantity of Packs
  PackDesc nVarChar(10) Pack Description
  Brand nVarChar(20) Brand
  NoSU Int(11) Number of Shipping Unit
  NetWeight Num(19,6) Net Weight
  GrsWeight Num(19,6) Gross Weight
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=19 ->ADP1
  TaxId10 nVarChar(100) Tax ID 10
  TransCat nVarChar(100) Transaction Category
  FormNo nVarChar(100) Form No.
  TaxId11 nVarChar(100) Tax ID 11
  StreetS nVarChar(100) Street
  BlockS nVarChar(100) Block
  BuildingS Text(16) Building/Floor/Room
  CityS nVarChar(100) City
  ZipCodeS nVarChar(20) Zip Code
  CountyS nVarChar(100) County
  StateS nVarChar(3) State ->OCST
  CountryS nVarChar(3) Country/Region ->OCRY
  AddrTypeS nVarChar(100) Address Type
  StreetNoS nVarChar(100) Street No.
  StreetB nVarChar(100) Street
  BlockB nVarChar(100) Block
  BuildingB Text(16) Building/Floor/Room
  CityB nVarChar(100) City
  ZipCodeB nVarChar(20) Zip Code
  CountyB nVarChar(100) County
  StateB nVarChar(3) State ->OCST
  CountryB nVarChar(3) Country/Region ->OCRY
  AddrTypeB nVarChar(100) Address Type
  StreetNoB nVarChar(100) Street No.
  ImpORExp VarChar(1) Import or Export [N=, Y=]
  Vat VarChar(1) VAT default=N [N=No VAT Support, Y=VAT Support]
  AltCrdNamB nVarChar(100) Alternative BP Name
  AltTaxIdB nVarChar(32) Alternative Tax ID
  Address2S nVarChar(50) Address Name 2
  Address3S nVarChar(50) Address Name 3
  Address2B nVarChar(50) Address Name 2
  Address3B nVarChar(50) Address Name 3
  MainUsage Int(11) Main Usage Code of Document ->OUSG
  GlbLocNumS nVarChar(50) Global Location Number
  GlbLocNumB nVarChar(50) Global Location Number
  CollectDT nVarChar(20) Date and Time of Collection
  TransprtDT Date(8) Transport Starting Date
  TransprtRS nVarChar(100) Transport Reason
  TaxId12 nVarChar(50) Tax ID 12
  TaxId13 nVarChar(100) Deductee Ref. No. in India
  ImpExpNo nVarChar(100) Import/Export Bill No.
  ImpExpDate Date(8) Import/Export Date
  BpGSTType Int(11) GST Regn Type of BP
  BpGSTN nVarChar(15) GST Regn No of BP
  BpStateCod nVarChar(3) State Code of Business Partner ->OCST
  BPStatGSTN nVarChar(2) GST State Code of BP
  LocGSTType Int(11) GST Regn Type of Location
  LocGSTN nVarChar(15) GST Regn No of Location
  LocStatCod nVarChar(3) State Code of Location ->OCST
  LocStaGSTN nVarChar(2) GST State Code of Location
  BpCountry nVarChar(3) Country/Region Code of BP ->OCRY
  OrigImpNo nVarChar(100) Original Bill of Entry No.
  OrigImpDat Date(8) Original Bill of Entry Date
  ExportType VarChar(1) Exporting Type default=E [E=Imports/Exports, S=SEZ Developer, U=SEZ Unit, D=Deemed Imports/Exports]
  PortCode nVarChar(100) Port Code
  BoEValue Num(19,6) Bill of Entry Value
  IsIGSTAct VarChar(1) Supply under IGST Account [Y=Yes, N=No]
  ClaimRefun VarChar(1) Claim Refund [Y=Yes, N=No]
  TaxRateDif Int(11) Differential % of Tax Rate [65=, 100=]
  BPGdsIssP nVarChar(15) Goods Issue Place BP
  CNPJGIP nVarChar(100) Goods Issue Place CNPJ
  CPFGIP nVarChar(100) Goods Issue Place CPF
  StreetGIP nVarChar(100) Goods Issue Place Street
  StrtNoGIP nVarChar(100) Goods Issue Place Street No.
  BldngGIP Text(16) Goods Issue Place Building
  ZipGIP nVarChar(20) Goods Issue Place Zip Code
  BlockGIP nVarChar(100) Goods Issue Place Block
  CityGIP nVarChar(100) Goods Issue Place City
  CountyGIP nVarChar(100) Goods Issue Place County
  StateGIP nVarChar(3) Goods Issue Place State ->OCST
  CountryGIP nVarChar(3) Goods Issue Place Country/Region ->OCRY
  PhoneGIP nVarChar(20) Goods Issue Place Phone
  EMailGIP nVarChar(100) Goods Issue Place E-Mail
  DptDateGIP Date(8) Goods Issue Place Departure Date
  BPDelivryP nVarChar(15) Delivery Place BP
  CNPJDlvryP nVarChar(100) Delivery Place CNPJ
  CPFDlvryP nVarChar(100) Delivery Place CPF
  StrtDlvryP nVarChar(100) Delivery Place Street
  StrNoDlvrP nVarChar(100) Delivery Place Street No.
  BldDlvryP Text(16) Delivery Place Building
  ZipDlvryP nVarChar(20) Delivery Place Zip Code
  BlckDlvryP nVarChar(100) Delivery Place Block
  CityDlvryP nVarChar(100) Delivery Place City
  CntyDlvryP nVarChar(100) Delivery Place County
  StatDlvryP nVarChar(3) Delivery Place State ->OCST
  CtryDlvryP nVarChar(3) Delivery Place Country/Region ->OCRY
  FoneDlvryP nVarChar(20) Delivery Place Phone
  MailDlvryP nVarChar(100) Delivery Place E-Mail
  DpDtDlvryP Date(8) Delivery Place Departure Date
  AuthedCNPJ nVarChar(250) Authorized CNPJ or CPF
  TaxId14 nVarChar(250) ITR Filing

# RPC13 - A/P Credit Memo Rows - Distributed Expenses
Module: Marketing Documents | 59 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPC
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=19 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Aquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Normal Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) VAT Applied Frgn
  VatAppldSC Num(19,6) VAT Applied Sys
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock default=N [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Line No.
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Abs. Entry default=-1
  BaseGroup Int(11) Base Document Group default=-1
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1
  VisOrder Int(11) Visual Order
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DistribExp VarChar(1) Distribute Freights [Y=Yes, N=No]
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ

# RPC14 - A/P Credit Memo - Assembly - Rows
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPC
  LineNum Int(11) Row Number default=-1
  ChildNum Int(11) Child Number default=-1
  ItemCode nVarChar(50) Item no. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  TotalQty Num(19,6) Total Quantity
  OpenQty Num(19,6) Remaining Open Quantity
  ObjectType nVarChar(20) object type default=19 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BaseChildN Int(11) Base Child Number default=-1
  EncryptIV nVarChar(100) Encrypt IV

# RPC15 - A/P Cr. Memo - Drawn Dpm Appld
Module: Marketing Documents | 84 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPC
  LineNum Int(11) Row Number
  ObjType nVarChar(20) object type default=19 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  StaCode nVarChar(8) Tax Authority Code
  StaType Int(11) Tax Authority Type
  StaIndex Int(11) Tax Authority Seq Index
  BaseNet Num(19,6) Net LC
  BaseNetFc Num(19,6) Net FC
  BaseNetSc Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFc Num(19,6) Tax FC
  VatSumSc Num(19,6) Tax SC
  DctSum Num(19,6) Deductible Sum LC
  DctSumFc Num(19,6) Deductible Sum FC
  DctSumSc Num(19,6) Deductible Sum SC
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplNet Num(19,6) Applied Net LC
  ApplNetFc Num(19,6) Applied Net FC
  ApplNetSc Num(19,6) Applied Net SC
  ApplVat Num(19,6) Applied Tax LC
  ApplVatFc Num(19,6) Applied Tax FC
  ApplVatSc Num(19,6) Applied Tax SC
  ApplDct Num(19,6) Applied Deductible Sum LC
  ApplDctFc Num(19,6) Applied Deductible Sum FC
  ApplDctSc Num(19,6) Applied Deductible Sum SC
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  PaidNet Num(19,6) Paid Net LC
  PaidNetFc Num(19,6) Paid Net FC
  PaidNetSc Num(19,6) Paid Net SC
  PaidVat Num(19,6) Paid Tax LC
  PaidVatFc Num(19,6) Paid Tax FC
  PaidVatSc Num(19,6) Paid Tax SC
  PaidDct Num(19,6) Paid Deductible Sum LC
  PaidDctFc Num(19,6) Paid Deductible Sum FC
  PaidDctSc Num(19,6) Paid Deductible Sum SC
  PaidEq Num(19,6) Paid Equalization Sum LC
  PaidEqFc Num(19,6) Paid Equalization Sum FC
  PaidEqSc Num(19,6) Paid Equalization Sum SC
  DpApplNet Num(19,6) Dpm Appl Net LC
  DpApplNetF Num(19,6) Dpm Appl Net FC
  DpApplNetS Num(19,6) Dpm Appl Net SC
  DpApplVat Num(19,6) Dpm Appl Tax LC
  DpApplVatF Num(19,6) Dpm Appl Tax FC
  DpApplVatS Num(19,6) Dpm Appl Tax SC
  DpApplDct Num(19,6) Dpm Appl Deductible Sum LC
  DpApplDctF Num(19,6) Dpm Appl Deductible Sum FC
  DpApplDctS Num(19,6) Dpm Appl Deductible Sum SC
  DpApplEq Num(19,6) Dpm Appl Equalization Sum LC
  DpApplEqFc Num(19,6) Dpm Appl Equalization Sum FC
  DpApplEqSc Num(19,6) Dpm Appl Equalization Sum SC
  TaxCode nVarChar(8) Tax Code ->OSTC
  LineType VarChar(1) Row Type default=D [D=Document, R=Exchange Rate Rounding, H=Document Header Rounding]
  BaseGrs Num(19,6) Gross LC
  BaseGrsFc Num(19,6) Gross FC
  BaseGrsSc Num(19,6) Gross SC
  ApplGrs Num(19,6) Applied Gross LC
  ApplGrsFc Num(19,6) Applied Gross FC
  ApplGrsSc Num(19,6) Applied Gross SC
  PaidGrs Num(19,6) Paid Gross LC
  PaidGrsFc Num(19,6) Paid Gross FC
  PaidGrsSc Num(19,6) Paid Gross SC
  DpApplGrs Num(19,6) Dpm Appl Gross LC
  DpApplGrsF Num(19,6) Dpm Appl Gross FC
  DpApplGrsS Num(19,6) Dpm Appl Gross SC
  RvsChrgSum Num(19,6) Reverse Charge Sum
  RvsChrgSc Num(19,6) Reverse Charge Sum (SC)
  RvsChrgFc Num(19,6) Reverse Charge Sum (FC)
  ApplRvs Num(19,6) Applied Reverse Charge Sum LC
  ApplRvsSc Num(19,6) Applied Reverse Charge Sum SC
  ApplRvsFc Num(19,6) Applied Reverse Charge Sum FC
  PaidRvs Num(19,6) Paid Reverse Charge Sum LC
  PaidRvsSc Num(19,6) Paid Reverse Charge Sum SC
  PaidRvsFc Num(19,6) Paid Reverse Charge Sum FC
  DpApplRvs Num(19,6) Dpm Applied Reverse Charge LC
  DpApplRvsS Num(19,6) Dpm Applied Reverse Charge SC
  DpApplRvsF Num(19,6) Dpm Applied Reverse Charge FC
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# RPC16 - A/P Credit Memo - SnB properties
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, SnBIndex
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) abs entry ->ORPC
  LineNum Int(11) Line Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object id
  ObjAbs Int(11) Object Abs
  DrfWObjAbs Int(11) draft Wobj Abs default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type default=19
  LogInstanc Int(11) Log Instance

# RPC17 - A/P Credit Memo - Import Process
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPC
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=19 ->ADP1
  ImpDocType VarChar(1) Type of Importation Document ->OBSI
  ImpDocNum nVarChar(10) Importation Document Number
  DateOfReg Date(8) Date of Registry DI/DSI/DA
  CustClrDat Date(8) Date of Customs Clearance
  ConcActNum nVarChar(30) Drawback Concession Acct No.
  AdditNum nVarChar(30) Additional Number
  AddItmDV Num(19,6) Additional Item Discount Value
  tpVTransp Int(6) Overland Transport Route [1=Maritime, 2=Waterway, 3=Lakeside, 4=Air, 5=Post, 6=Train, 7=Road, 8=Network Transmission, 9=Own Means, 10=Input/Output Fictitious, 11=Courier, 12=Hand Carry]
  DrawSReg nVarChar(11) Drawback - Suspension Regime
  AddFrNavyA Num(19,6) Additional Freight to Navy Authority
  TypeOfImp VarChar(1) Type of Import
  nSeqAdic Int(6) Additional Item Sequential Number

# RPC18 - A/P Credit Memo - Export Process
Module: Marketing Documents | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPC
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=19 ->ADP1
  ExpDocType Int(11) Type of Exportation Document default=-1 ->OBNI
  ExpDeclNum Int(11) Exportation Declaration Number
  ExpDeclDat Date(8) Exportation Declaration Date
  ExpNature Int(11) Nature of Exportation default=-1 ->OBNI
  ExpRegNum Int(11) Number of Exportation Registry
  ExpRegDate Date(8) Date of Exportation Registry
  LadBillNum nVarChar(19) Bill of Lading Number
  LadBillDat Date(8) Date of Bill of Lading
  MerchLeftD Date(8) Date Merchandise Left Customs
  LadBillTyp Int(11) Type of Bill of Lading default=-1 ->OBNI
  DrawSReg nVarChar(11) Drawback - Suspension Regime
  NatureExp nVarChar(44) Nature of Export
  QultExpItm Num(19,6) Quantity of Exported Items
  nSeqAdic Int(6) Additional Item Sequential Number

# RPC19 - A/P Credit Memo - Bin Allocation Data
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, BinAllocSe
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->ORPC
  BinAllocSe Int(11) Bin Allocation Sequence
  LineNum Int(11) Line Number
  SubLineNum Int(11) Subline Number default=-1
  SnBType Int(11) SnB Type default=-1
  SnBMDAbs Int(11) SnB Master Data Internal No. default=-1
  BinAbs Int(11) Bin Internal Number ->OBIN
  Quantity Num(19,6) Quantity
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjType nVarChar(20) Object Type default=19 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  BinActTyp Int(6) Bin Action Type [1=Transaction In, 2=Transaction Out, 4=SnB Complete, 8=Bin First Then SnB]

# RPC2 - A/P Credit Memo Rows - Expenses
Module: Marketing Documents | 64 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPC
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=19 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) Vat Applied
  VatAppldFC Num(19,6) Vat Applied Frgn
  VatAppldSC Num(19,6) Vat Applied Sys
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report [Y=Yes, N=No]
  BaseGroup Int(11) Base Document Group default=-1 [-1=, 0=, 1=, 2=]
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1 [-1=, 0=, 1=, 2=]
  VisOrder Int(11) Visual Order
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]

# RPC20 - Intrastat Expenses
Module: Marketing Documents | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPC
  ExpnsCode Int(11) Freight Code ->OEXD
  TotalLC Num(19,6) Total
  TotalFC Num(19,6) Total (FC)
  TotalSC Num(19,6) Total (SC)
  DistribM VarChar(1) Distribution Method default=T [Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DrawnLC Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  LineNum Int(11) Line Number default=-1
  BaseAbsEnt Int(11) Base Abs. Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 16=Return, 13=A/R Invoice, 203=Down Payment Incoming, 204=Down Payment Outgoing, 22=Purchase Order, 20=Goods Receipt PO, 21=Goods Return, 18=A/P Invoice, 540000006=Purchase Quotation, 0=, -1=]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No. default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=19 ->ADP1
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  AppliedLC Num(19,6) Applied
  AppliedFC Num(19,6) Applied (FC)
  AppliedSC Num(19,6) Applied (SC)

# RPC21 - A/P Credit Memo - Document Reference Information
Module: Marketing Documents | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, RefType
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjectType nVarChar(20) Object Type default=19
  LogInstanc Int(11) Log Instance default=0
  RefType VarChar(1) Reference Types default=S [S=System Document, E=External Document]
  LineNum Int(11) Line Number
  RefDocEntr Int(11) Referenced Internal Number
  RefDocNum Int(11) Referenced Document Number
  ExtDocNum nVarChar(100) External Referenced Document Number
  RefObjType nVarChar(20) Referenced Object Type [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 234000031=Return Request, 16=Return, 203=A/R Down Payment, 13=A/R Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 280=A/R Tax Invoice, 1470000113=Purchase Request, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Return Request, 21=Goods Return, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 281=A/P Tax Invoice, 69=Landed Costs, 24=Incoming Payments, 46=Outgoing Payments, 57=Checks for Payment, 321=Internal Reconciliation, 34=Recurring Posting, 30=Journal Entry, 59=Goods Receipt, 60=Goods Issue, 162=Inventory Revaluation, 1470000065=Inventory Counting, 10000071=Inventory Posting, 1250000001=Inventory Transfer Request, 67=Inventory Transfer, 202=Production Order, 13001=Original Invoice, -1=External Document, 20301=Original Down Payment Invoice]
  AccessKey nVarChar(100) Access Key
  IssueDate Date(8) Date of Issue
  IssuerCNPJ nVarChar(100) Issuer CNPJ
  IssuerCode nVarChar(10) Fiscal Document Issuer UF Code
  Model nVarChar(6) Fiscal Document Model
  Series nVarChar(3) Fiscal Document Series
  Number Int(11) Fiscal Document Number
  RefAccKey nVarChar(100) Referenced CT-e Access Key
  RefAmount Num(19,6) Referenced Amount
  SubSeries nVarChar(3) Fiscal Document Subseries
  Remark nVarChar(254) Remarks
  LinkRefTyp nVarChar(20) Link Reference Type default=00 [00=, 01=Nota de cr�dito de los documentos relacionados, 02=Nota de d�bito de los documentos relacionados, 03=Devoluci�n de mercanc�a sobre facturas o traslados previos, 04=Sustituci�n de los CFDI previos, 05=Traslados de mercancias facturados previamente, 06=Factura generada por los traslados previos, 07=CFDI por aplicaci�n de anticipo, 08=Customs, MX_08=Factura generada por pagos en parcialidades, 09=Factura generada por pagos diferidos]

# RPC22 - A/P Credit Memo - Resource Costs
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, StdCostNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->RPC1
  LineNum Int(11) Row Number ->RPC1
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=19
  LogInstanc Int(11) Log Instance default=0

# RPC23 - A/P Invoice - Selected Asset Master Data
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, VisOrder
  ASSETS: DocEntry, LineNum, AssetCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPC
  LineNum Int(11) Row Number
  AssetCode nVarChar(50) Selected Asset Code ->OITM
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Remarks nVarChar(100) Remarks
  Amount Num(19,6) Amount
  AmountSC Num(19,6) Amount (SC)
  SerialNo nVarChar(30) Serial Number
  VisOrder Int(11) Visual Order
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=19 ->ADP1

# RPC24 - A/P Credit Memo - Tracking Note Assignment
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  ItemCCDNum nVarChar(40) Item CCD Number
  CntrOrigin nVarChar(3) Country/Region of Origin
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=19 ->ADP1
  SubLineNum Int(11) BOM Line No.

# RPC25 - A/P Credit Memo - Amt Per VAT Grp
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, VatGroup, Type
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  VatGroup nVarChar(8) Tax Definition ->OVTG
  VatPrcnt Num(19,6) Tax Rate
  BaseAmnt Num(19,6) Base Amount
  BaseAmntFC Num(19,6) Base Amount (FC)
  BaseAmntSC Num(19,6) Base Amount (SC)
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  Type Int(11) Type default=1 [1=Discount by Tax]
  Currency nVarChar(3) Price Currency
  Rate Num(19,6) Currency Rate
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=19 ->ADP1

# RPC26 - A/P Credit Memo - E-Way Bill Information
Module: Marketing Documents | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPC
  SuplyType nVarChar(20) EWB Transaction Type [O=Outward, I=Inward]
  SubSplyTyp Int(11) EWB Sub-Type ->OEST
  DocType nVarChar(3) EWB Doc. Type ->OEDT
  TransMode Int(11) EWB Transportation Mode ->OETM
  Distance Num(19,6) EWB Transport Distance
  TransDocNo nVarChar(16) EWB Transporter Doc. No.
  TransDate Date(8) EWB Transportation Date
  VehicleTyp nVarChar(2) EWB Vehicle Type ->OEVT
  VehicleNo nVarChar(15) EWB Vehicle Number
  EWayBillNo nVarChar(20) EWB No.
  EwbDate Date(8) E-Way Bill Date
  FrmTraName nVarChar(100) EWB Consignor Name
  FrmAddres1 nVarChar(120) EWB Consignor Address 1
  FrmAddres2 nVarChar(120) EWB Consignor Address 2
  FrmZipCode nVarChar(20) EWB Consignor Zip Code
  ActFrmStat nVarChar(2) Dispatch State of EWB Consignor
  ToTraName nVarChar(100) EWB Consignee Name
  ToAddres1 nVarChar(120) EWB Consignee Address 1
  ToAddres2 nVarChar(120) EWB Consignee Address 2
  ToZipCode nVarChar(20) EWB Consignee Zip Code
  ActToState nVarChar(2) Ship-To State of EWB Consignee
  FrmGSTN nVarChar(15) EWB Consignor GSTN
  FrmState nVarChar(2) Bill-To State of EWB Consignor
  ToGSTN nVarChar(15) EWB Consignee GSTN
  ToState nVarChar(2) Bill-To State of EWB Consignee
  MainHsnEnt Int(11) EWB Main HSN Entry ->OCHP
  FrmPlace nVarChar(50) EWB Consignor Place
  ToPlace nVarChar(50) EWB Consignee Place
  TransID nVarChar(15) EWB Transporter ID
  TransName nVarChar(25) EWB Transporter Name
  ExpireDate Date(8) EWB Expiration Date
  ObjectType nVarChar(20) Object Type default=19 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TspEntry Int(11) Transporter Abs. Entry ->OTSP
  TspLine Int(11) Transportation Line
  TransType Int(11) Transaction Type [1=Regular, 2=Bill To-Ship To, 3=Bill From-Dispatch From, 4=Combination of 2 and 3]

# RPC27 - A/P Credit Memo - E-Books(GR) Rows
Module: Marketing Documents | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  RELATE_ROW: DocEntry, RelateType, RelateLine, GroupNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPC
  LineNum Int(11) Row Number
  RelateType Int(11) Relation Type default=-1 [1=Row, 2=Row Expenses, 3=Document Expenses, 13=Distributed Freights, -1=Manual]
  RelateLine Int(11) Relation Row Number default=-1
  GroupNum Int(11) Group Number default=-1
  LineTotal Num(19,6) Line Total
  LineTotalF Num(19,6) Line Total (FC)
  LineTotalS Num(19,6) Line Total (SC)
  InClassTyp Int(11) Income Classification Type ->OICP
  InClassCat Int(11) Income Classification Category ->OICC
  ExClassTyp Int(11) Expense Classification Type ->OECP
  ExClassCat Int(11) Expense Classification Cat. ->OECC
  VatCate Int(11) VAT Category
  NetValue Num(19,6) Net Value
  NetValueFC Num(19,6) Net Value (FC)
  NetValueSC Num(19,6) Net Value (SC)
  VatAmount Num(19,6) VAT Amount
  VatAmFC Num(19,6) VAT Amount (FC)
  VatAmSC Num(19,6) VAT Amount (SC)
  WtPercCat Int(11) Withheld Percentage Category
  WtAmount Num(19,6) Withheld Amount
  WtAmountFC Num(19,6) Withheld Amount (FC)
  WtAmountSC Num(19,6) Withheld Amount (SC)
  ObjectType nVarChar(20) Object Type default=19 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  WtCategory VarChar(1) Withheld Category [I=Invoice, P=Payment]
  VATClassTy Int(11) VAT Classification Type ->OECP
  VATClassCa Int(11) VAT Classification Category ->OECC
  EBVatExCau Int(11) VAT Exemption Cause ->OVEC

# RPC28 - A/P Credit Memo - Reported Tracking Note
Module: Marketing Documents | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
  TCN_KEY U: DocEntry, LineNum, TrackingNt, TrackiNtLn
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  UnusedQty Num(19,6) Unused Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=19 ->ADP1
  SubLineNum Int(11) BOM Line No.

# RPC3 - A/P Credit Memo - Freight
Module: Marketing Documents | 80 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  DOCUMENT: DocEntry, BaseAbsEnt
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPC
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  Comments nVarChar(100) Remarks
  ObjType nVarChar(20) Object Type default=19 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  WTLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  VatApplied Num(19,6) Vat Applied
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatF Num(19,6) Net Tax Amount (FC)
  LineVatS Num(19,6) Net Tax Amount (SC)
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 21=Goods Return, 18=A/P Invoice, 204=A/P Down Payment, 20=Goods Receipt PO, 234000032=A/P Return Request]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No.
  LineNum Int(11) line num default=-1
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Doc. Internal No. default=-1
  StDstr Num(19,6) Stock Distributed Sum
  StDstrSC Num(19,6) Stock Distributed Sum (SC)
  StDstrFC Num(19,6) Stock Distributed Sum (FC)
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  TaxDistMtd VarChar(1) Tax Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  GrsAmount Num(19,6) Gross Amount
  GrsFC Num(19,6) Gross Amount (FC)
  GrsSC Num(19,6) Gross Amount (SC)
  BaseTotal VarChar(1) Base Total for Calculation default=N [N=Net Total, G=Gross Total]
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)
  RRVatLC Num(19,6) Return Request VAT Amount
  RRVatFC Num(19,6) Return Request VAT Amount (FC)
  RRVatSC Num(19,6) Return Request VAT Amount (SC)
  EncryptIV nVarChar(100) Encrypt IV
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]

# RPC4 - A/P Credit Memo - Tax Amount per Document
Module: Marketing Documents | 61 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SCONDARY: DocEntry, LineNum, GroupNum, ExpnsCode, StcCode, StaCode, staType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPC
  LineNum Int(11) Row Number default=-1
  GroupNum Int(11) Group Number default=-1
  ExpnsCode Int(11) Expense Code default=-1 ->OEXD
  RelateType Int(11) Relation Type default=1 [1=Row, 2=Row Freight Charges, 3=Document Expenses, 13=Distributed Freights]
  StcCode nVarChar(8) Tax Code ->OSTC
  StaCode nVarChar(8) Authority Code ->OSTA
  staType Int(11) Authority Type ->OSTT
  TaxRate Num(19,6) Tax Rate
  TaxAcct nVarChar(15) Tax Account ->OACT
  TaxSum Num(19,6) Tax Amount
  TaxSumFrgn Num(19,6) Tax Amount (FC)
  TaxSumSys Num(19,6) Tax Amount (SC)
  BaseSum Num(19,6) Base Amount
  BaseSumFrg Num(19,6) Base Amount (FC)
  BaseSumSys Num(19,6) Base Amount (SC)
  ObjectType nVarChar(20) Object Type default=19 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Status default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  LineSeq Int(11) Line Sequence
  DeferrAcct nVarChar(15) Deferred Tax Account ->OACT
  BaseType Int(11) Base Document Type default=-1
  BaseAbs Int(11) Base Doc Abs Entry default=-1
  BaseSeq Int(11) Base Doc. Line Sequence
  DeductTax Num(19,6) Deductible Tax Amount
  DdctTaxFrg Num(19,6) Deductible Tax Amount (FC)
  DdctTaxSys Num(19,6) Deductible Tax Amount (SC)
  BaseAppld Num(19,6) Applied Base Amount
  BaseApldFC Num(19,6) Applied Base Amount (FC)
  BaseApldSC Num(19,6) Applied Base Amount (SC)
  NonDdctPrc Num(19,6) Non Deductible %
  NonDdctAct nVarChar(15) Non Deductible Account ->OACT
  TaxInPrice VarChar(1) Tax Included in Price? default=N [Y=Yes, N=No]
  Exempt VarChar(1) Exempt? default=N [Y=Yes, N=No]
  TaxExpAct nVarChar(15) Expense Account for Tax ->OACT
  OnHoldTax Num(19,6) On Hold Tax Amount
  OnHoldTaxF Num(19,6) On Hold Tax Amount (FC)
  OnHoldTaxS Num(19,6) On Hold Tax Amount (SC)
  InGrossRev VarChar(1) Included in Gross Revenue default=N [Y=Yes, N=No]
  TaxSumOrg Num(19,6) Tax Amount Original
  TaxSumOrgF Num(19,6) Tax Amount Original (FC)
  TaxSumOrgS Num(19,6) Tax Amount Original (SC)
  OpenTax Num(19,6) Open Service Tax
  OpenTaxFC Num(19,6) Open Service Tax (FC)
  OpenTaxSC Num(19,6) Open Service Tax (SC)
  Unencumbrd VarChar(1) Unencumbered default=N [Y=Yes, N=No]
  TaxOnRI VarChar(1) Tax On Reserve Invoice default=N [Y=Yes, N=No]
  RvsChrgPrc Num(19,6) Reverse Charge %
  RvsChrgTax Num(19,6) Reverse Charge Tax Amount
  RvsChrgSC Num(19,6) Reverse Charge Tax Amount (SC)
  RvsChrgFC Num(19,6) Reverse Charge Tax Amount (FC)
  InFirstIns VarChar(1) Included in First Installment default=N [Y=Yes, N=No]
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CESTrel VarChar(1) CEST Relevant default=N [Y=, N=]

# RPC5 - A/P Credit Memo - Withholding Tax
Module: Marketing Documents | 158 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  SECONDERY U: AbsEntry, WTCode, BaseAbsEnt, Doc1LineNo
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator ->ORPC
  WTCode nVarChar(4) WT Code ->OWHT
  Rate Num(19,6) Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntSC Num(19,6) Taxable Amount in SC
  TxblAmntFC Num(19,6) Taxable Amount in FC
  WTAmnt Num(19,6) WT Amount
  WTAmntSC Num(19,6) WT Amount (SC)
  WTAmntFC Num(19,6) WT Amount (FC)
  ApplAmnt Num(19,6) Applied WT Amount
  ApplAmntSC Num(19,6) Applied WTax Amount (SC)
  ApplAmntFC Num(19,6) Applied WTax Amount (FC)
  Category VarChar(1) Category [P=Payment, I=Invoice]
  Criteria VarChar(1) Criteria [Y=Accrual, N=Cash]
  Account nVarChar(15) G/L Account ->OACT
  Type VarChar(1) Withholding Type [V=VAT Withholding, I=Income Tax Withholding]
  RoundType VarChar(1) Rounding Type [T=Truncated, C=Commercial Values, N=No Rounding]
  BaseType VarChar(1) Base Type [G=Gross, N=Net, V=VAT, U=UoM]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseLine Int(11) Base Line
  BaseNum Int(11) Base Document Type default=-1 [-1=, 0=, 21=Goods Return, 18=A/P Invoice, 204=A/P Down Payment]
  LineNum Int(11) Line Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Abs. Entry default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=19 ->ADP1
  Doc1LineNo Int(11) DOC1 Line Number default=-1
  WtLineType VarChar(1) WT Line Type default=D [D=Document Level WTax, L=Row Level WTax]
  TxblCurr nVarChar(3) Taxable Currency from Doc Line
  DtblCurr nVarChar(3) Deductible Currency
  DtblRate Num(19,6) Rate for Deductible Amount
  txblRate Num(19,6) Rate for Taxable Amount
  DtblAmount Num(19,6) Deductible Amount
  TdsAcc nVarChar(15) TDS Account ->OACT
  SurAcc nVarChar(15) Surcharge Account ->OACT
  CessAcc nVarChar(15) Cess Account ->OACT
  HscAcc nVarChar(15) HSC Account ->OACT
  TdsRate Num(19,6) TDS Rate
  SurRate Num(19,6) Surcharge Rate
  CessRate Num(19,6) Cess Rate
  HscRate Num(19,6) HSC Rate
  TdsBAmt Num(19,6) TDS Base Amount
  TdsBAmtSC Num(19,6) TDS Base Amount (SC)
  TdsBAmtFC Num(19,6) TDS Base Amount (FC)
  SurBAmt Num(19,6) Surcharge Base Amount
  SurBAmtSC Num(19,6) Surcharge Base Amount (SC)
  SurBAmtFC Num(19,6) Surcharge Base Amount (FC)
  CessBAmt Num(19,6) Cess Base Amount
  CessBAmtSC Num(19,6) Cess Base Amount (SC)
  CessBAmtFC Num(19,6) Cess Base Amount (FC)
  HscBAmt Num(19,6) HSC Base Amount
  HscBAmtSC Num(19,6) HSC Base Amount (SC)
  HscBAmtFC Num(19,6) HSC Base Amount (FC)
  TdsAmnt Num(19,6) TDS Tax Amount
  TdsAmntSC Num(19,6) TDS Tax Amount (SC)
  TdsAmntFC Num(19,6) TDS Tax Amount (FC)
  SurAmnt Num(19,6) Surcharge Tax Amount
  SurAmntSC Num(19,6) Surcharge Tax Amount (SC)
  SurAmntFC Num(19,6) Surcharge Tax Amount (FC)
  CessAmnt Num(19,6) Cess Tax Amount
  CessAmntSC Num(19,6) Cess Tax Amount (SC)
  CessAmntFC Num(19,6) Cess Tax Amount (FC)
  HscAmnt Num(19,6) HSC Tax Amount
  HscAmntSC Num(19,6) HSC Tax Amount (SC)
  HscAmntFC Num(19,6) HSC Tax Amount (FC)
  TdsAppl Num(19,6) Applied TDS Amount
  TdsApplSC Num(19,6) Applied TDS Amount (SC)
  TdsApplFC Num(19,6) Applied TDS Amount (FC)
  SurAppl Num(19,6) Applied Surcharge Amount
  SurApplSC Num(19,6) Applied Surcharge Amount (SC)
  SurApplFC Num(19,6) Applied Surcharge Amount (FC)
  CessAppl Num(19,6) Applied Cess Amount
  CessApplSC Num(19,6) Applied Cess Amount (SC)
  CessApplFC Num(19,6) Applied Cess Amount (FC)
  HscAppl Num(19,6) Applied HSC Amount
  HscApplSC Num(19,6) Applied HSC Amount (SC)
  HscApplFC Num(19,6) Applied HSC Amount (FC)
  BatchNum Int(11) Journal Voucher No.
  InCSTCode nVarChar(2) CST Code Incoming
  OutCSTCode nVarChar(2) CST Code Outgoing
  DpmWTApl Num(19,6) DPM WT Applied Amount
  DpmWTAplSC Num(19,6) DPM WT Applied Amount (SC)
  DpmWTAplFC Num(19,6) DPM WT Applied Amount (FC)
  WTTypeId Int(11) WT Type Id ->OWTT
  LnBsAmt Num(19,6) BR Line WT Base Amount
  LnBsAmtSC Num(19,6) BR Line WT Base Amount(SC)
  LnBsAmtFC Num(19,6) BR Line WT Base Amount(FC)
  LnCmTAmt Num(19,6) BR Line Cumulated Taxable Amount
  LnCmTAmtSC Num(19,6) BR Line Cumulated Taxable Amount(SC)
  LnCmTAmtFC Num(19,6) BR Line Cumulated Taxable Amount(FC)
  TDSType VarChar(1) TDS Type [E=eTDS, D=GST TDS, C=GST TCS, S=SALES TCS]
  IgstAcc nVarChar(15) IGST Account ->OACT
  CgstAcc nVarChar(15) CGST Account ->OACT
  SgstAcc nVarChar(15) SGST Account ->OACT
  IgstAmnt Num(19,6) IGST Tax Amount
  IgstAmntSC Num(19,6) IGST Tax Amount (SC)
  IgstAmntFC Num(19,6) IGST Tax Amount (FC)
  CgstAmnt Num(19,6) CGST Tax Amount
  CgstAmntSC Num(19,6) CGST Tax Amount (SC)
  CgstAmntFC Num(19,6) CGST Tax Amount (FC)
  SgstAmnt Num(19,6) SGST Tax Amount
  SgstAmntSC Num(19,6) SGST Tax Amount (SC)
  SgstAmntFC Num(19,6) SGST Tax Amount (FC)
  IgstRate Num(19,6) IGST Rate
  CgstRate Num(19,6) CGST Rate
  SgstRate Num(19,6) SGST Rate
  IgstBAmt Num(19,6) IGST Base Amount
  IgstBAmtSC Num(19,6) IGST Base Amount (SC)
  IgstBAmtFC Num(19,6) IGST Base Amount (FC)
  CgstBAmt Num(19,6) CGST Base Amount
  CgstBAmtSC Num(19,6) CGST Base Amount (SC)
  CgstBAmtFC Num(19,6) CGST Base Amount (FC)
  SgstBAmt Num(19,6) SGST Base Amount
  SgstBAmtSC Num(19,6) SGST Base Amount (SC)
  SgstBAmtFC Num(19,6) SGST Base Amount (FC)
  IgstAppl Num(19,6) Applied IGST Amount
  IgstApplSC Num(19,6) Applied IGST Amount (SC)
  IgstApplFC Num(19,6) Applied IGST Amount (FC)
  CgstAppl Num(19,6) Applied CGST Amount
  CgstApplSC Num(19,6) Applied CGST Amount (SC)
  CgstApplFC Num(19,6) Applied CGST Amount (FC)
  SgstAppl Num(19,6) Applied SGST Amount
  SgstApplSC Num(19,6) Applied SGST Amount (SC)
  SgstApplFC Num(19,6) Applied SGST Amount (FC)
  UtgstAcc nVarChar(15) UTGST Account ->OACT
  CsgstAcc nVarChar(15) Cess GST Account ->OACT
  UtgstAmt Num(19,6) UTGST Tax Amount
  UtgstAmtSC Num(19,6) UTGST Tax Amount (SC)
  UtgstAmtFC Num(19,6) UTGST Tax Amount (FC)
  CsgstAmt Num(19,6) Cess GST Tax Amount
  CsgstAmtSC Num(19,6) Cess GST Tax Amount (SC)
  CsgstAmtFC Num(19,6) Cess GST Tax Amount (FC)
  UtgstRate Num(19,6) UTGST Rate
  CsgstRate Num(19,6) Cess GST Rate
  UtgstBAmt Num(19,6) UTGST Base Amount
  UtgstBAmtS Num(19,6) UTGST Base Amount (SC)
  UtgstBAmtF Num(19,6) UTGST Base Amount (FC)
  CsgstBAmt Num(19,6) Cess GST Base Amount
  CsgstBAmtS Num(19,6) Cess GST Base Amount (SC)
  CsgstBAmtF Num(19,6) Cess GST Base Amount (FC)
  UtgstAppl Num(19,6) Applied UTGST Amount
  UtgstApplS Num(19,6) Applied UTGST Amount (SC)
  UtgstApplF Num(19,6) Applied UTGST Amount (FC)
  CsgstAppl Num(19,6) Applied Cess GST Amount
  CsgstApplS Num(19,6) Applied Cess GST Amount (SC)
  CsgstApplF Num(19,6) Applied Cess GST Amount (FC)
  EncryptIV nVarChar(100) Encrypt IV
  TcsIntAcct nVarChar(15) TCS Interim Account ->OACT
  SurIntAcct nVarChar(15) Surcharge Interim Account ->OACT
  CesIntAcct nVarChar(15) Cess Interim Account ->OACT
  HscIntAcct nVarChar(15) HSC interim Account ->OACT
  LnIntAcct nVarChar(15) Interim Account for Tax ->OACT
  FixedAmnt Num(19,6) Fixed Amount
  FixedAmtSC Num(19,6) Fixed Amount (SC)
  FixedAmtFC Num(19,6) Fixed Amount (FC)
  BaseQty Num(19,6) Base Quantity

# RPC6 - A/P Credit Memo - Installments
Module: Marketing Documents | 65 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, InstlmntID
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPC
  InstlmntID Int(6) Installment ID default=1
  ObjType nVarChar(20) Object Type default=19 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DueDate Date(8) Due Date
  Status VarChar(1) Installment Status default=O [O=Open, C=Closed]
  DunnLevel Int(11) Dunning Level default=0
  InsTotal Num(19,6) Total Installment
  InsTotalFC Num(19,6) Total Installment (FC)
  InsTotalSy Num(19,6) Total Installment (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  VatSum Num(19,6) Total Tax
  VatSumFC Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  VatPaid Num(19,6) Tax Paid to Date
  VatPaidFC Num(19,6) Tax Paid (FC)
  VatPaidSys Num(19,6) Tax Paid (SC)
  TotalExpns Num(19,6) Total Freight Charges
  TotalExpFC Num(19,6) Total Freight Charges (FC)
  TotalExpSC Num(19,6) Total Freight Charges (SC)
  ExpAppl Num(19,6) Applied Freight Charges
  ExpApplFC Num(19,6) Applied Freight Charges (FC)
  ExpApplSC Num(19,6) Applied Freight Charges (SC)
  WTSum Num(19,6) WTax Amount
  WTSumFC Num(19,6) WTax Amount (FC)
  WTSumSC Num(19,6) WTax Amount (SC)
  WTApplied Num(19,6) Applied WTax
  WTAppliedF Num(19,6) Applied WTax (FC)
  WTAppliedS Num(19,6) Applied WTax (SC)
  TotalBlck Num(19,6) Total Reserved Amount
  TotalBlckF Num(19,6) Total Reserved Amount (FC)
  TotalBlckS Num(19,6) Total Reserved Amount (SC)
  VATBlck Num(19,6) Reserved Tax
  VATBlckFC Num(19,6) Reserved Tax (FC)
  VATBlckSC Num(19,6) Reserved Tax (SC)
  ExpnsBlck Num(19,6) Reserved Freight Charges
  ExpnsBlckF Num(19,6) Reserved Freight Charges (FC)
  ExpnsBlckS Num(19,6) Reserved Freight Charges (SC)
  WTBlocked Num(19,6) Reserved WTax Amount
  WTBlockedF Num(19,6) Reserved WTax Amount (FC)
  WTBlockedS Num(19,6) Reserved WTax Amount (SC)
  InstPrcnt Num(19,6) Installment %
  DunWizBlck VarChar(1) Wizard dunning block default=N [N=No, Y=Yes]
  DunDate Date(8) Last Dunning Date
  Paid Num(19,6) Paid
  PaidFrgn Num(19,6) Paid (FC)
  PaidSc Num(19,6) Paid (SC)
  reserved VarChar(1) Reserved default=N [N=No, Y=Yes]
  TaxOnExp Num(19,6) Tax on Expenses
  TaxOnExpFc Num(19,6) Tax on Expenses (FC)
  TaxOnExpSc Num(19,6) Tax on Expenses (SC)
  TaxOnExpAp Num(19,6) Applied Tax on Expenses
  TaxOnExApF Num(19,6) Applied Tax on Expenses (FC)
  TaxOnExApS Num(19,6) Applied Tax on Expenses (SC)
  TaxOnExBlo Num(19,6) Reserved Tax on Freight Amount
  TaxOnExBlF Num(19,6) Reserved Tax on Freight Amt FC
  TaxOnExBlS Num(19,6) Reserved Tax on Freight Amt SC
  LvlUpdDate Date(8) Dunning Level Update Date
  Ordered VarChar(1) Payment Ordered default=N [Y=Yes, N=No]
  PaidDpm Num(19,6) Paid by Down Payment
  PaidDpmFc Num(19,6) Paid by Down Payment (FC)
  PaidDpmSc Num(19,6) Paid by Down Payment (SC)
  EncryptIV nVarChar(100) Encrypt IV

# RPC7 - Delivery Packages - A/P Credit Memo
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPC
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type default=19 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV

# RPC8 - Items in Package - A/P Credit Memo
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum, ItemCode, UomEntry, NumPerMsr
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPC
  PackageNum Int(11) Package Number
  ItemCode nVarChar(50) Item Code ->OITM
  Quantity Num(19,6) Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=19 ->ADP1
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value default=0

# RPC9 - A/P Credit Memo - Drawn Dpm
Module: Marketing Documents | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPC
  LineNum Int(11) Row Number
  BaseAbs Int(11) Base Document Internal ID ->ODPO
  BaseLine Int(11) Base Document Row
  TargetBase VarChar(1) Target or Base Document default=B [B=Base, T=Target]
  ObjType nVarChar(20) Base Object Type
  DrawnSum Num(19,6) Net LC
  DrawnSumFc Num(19,6) Net FC
  DrawnSumSc Num(19,6) Net SC
  LogInstanc Int(11) Log Instance default=0
  ObjCode nVarChar(20) Object Type default=19 ->ADP1
  ApplDrawn Num(19,6) Applied Net LC
  ApplDrawnF Num(19,6) Applied Net FC
  ApplDrawnS Num(19,6) Applied Net SC
  BaseDocNum Int(11) Base Document Number
  BsDocDate Date(8) Base Posting Date
  BsDueDate Date(8) Base Due Date
  BsCardName nVarChar(100) Base BP Name
  BsComments nVarChar(254) Base Remarks
  Posted VarChar(1) Base Document Posted default=Y [Y=Yes, N=No]
  Vat Num(19,6) Tax LC
  VatFc Num(19,6) Tax FC
  VatSc Num(19,6) Tax SC
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  IsGross VarChar(1) Is Gross Line default=N [N=Net Line, Y=Gross Line]

# RPD1 - Goods Return - Rows
Module: Marketing Documents | 317 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  STATUS: LineStatus
  CURRENCY: Currency
  ACCOUNT: AcctCode
  BASE_ENTRY: BaseEntry, BaseType, BaseLine
  VIS_ORDER: DocEntry, VisOrder
  OWNER_CODE: OwnerCode
  ITM_WHS_OQ: ItemCode, WhsCode, OpenQty
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPD
  LineNum Int(11) Row Number
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=, 19=A/P Credit Memo]
  TrgetEntry Int(11) Target Document Internal ID
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 20=Purchase Delivery Notes, 21=Goods Return, 234000032=A/P Return Request]
  BaseEntry Int(11) Base Document Internal ID
  BaseLine Int(11) Base Row
  LineStatus VarChar(1) Row Status default=O [O=Open, C=Closed]
  ItemCode nVarChar(50) Item No. ->OITM
  Dscription nVarChar(200) Item/Service Description
  Quantity Num(19,6) Quantity
  ShipDate Date(8) Row Delivery Date
  OpenQty Num(19,6) Remaining Open Quantity
  Price Num(19,6) Price
  Currency nVarChar(3) Price Currency ->OCRN
  Rate Num(19,6) Currency Rate
  DiscPrcnt Num(19,6) Discount % per Row
  LineTotal Num(19,6) Row Total
  TotalFrgn Num(19,6) Row Total (FC)
  OpenSum Num(19,6) Open Amount
  OpenSumFC Num(19,6) Open Amount (FC)
  VendorNum nVarChar(50) Vendor Catalog No.
  SerialNum nVarChar(17) Serial Number
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  SlpCode Int(11) Sales Employee Code default=-1 ->OSLP
  Commission Num(19,6) Commission Percentage
  TreeType VarChar(1) BOM Type default=N [N=Not a BOM, A=Assembly, S=Sales, I=Sales BOM Component, P=Production, T=Template]
  AcctCode nVarChar(15) Account Code ->OACT
  TaxStatus VarChar(1) Tax Definition [Y=Yes, N=No]
  GrossBuyPr Num(19,6) Gross Profit Base Price
  PriceBefDi Num(19,6) Unit Price
  DocDate Date(8) Posting Date
  Flags Int(11) Flags default=0
  OpenCreQty Num(19,6) Credit Memo Amount
  UseBaseUn VarChar(1) Inventory UoM default=N [Y=Yes, N=No]
  SubCatNum nVarChar(50) BP Catalog No. ->OSCN
  BaseCard nVarChar(15) Base BP Code ->OCRD
  TotalSumSy Num(19,6) Row Total (SC)
  OpenSumSys Num(19,6) Open Amount (SC)
  InvntSttus VarChar(1) Warehouse Status default=O [O=Open, C=Closed]
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  CodeBars nVarChar(254) Bar Code
  VatPrcnt Num(19,6) Tax Rate per Row
  VatGroup nVarChar(8) Tax Definition ->OVTG
  PriceAfVAT Num(19,6) Gross Price after Discount
  Height1 Num(19,6) Height 1
  Hght1Unit Int(6) Unit of Height 1
  Height2 Num(19,6) Height 2
  Hght2Unit Int(6) Unit of Height 2
  Width1 Num(19,6) Width 1
  Wdth1Unit Int(6) Unit of Width 1
  Width2 Num(19,6) Width 2
  Wdth2Unit Int(6) Unit of Width 2
  Length1 Num(19,6) Length 1
  Len1Unit Int(6) Unit of Length 1
  length2 Num(19,6) Length 2
  Len2Unit Int(6) Unit of Length 2
  Volume Num(19,6) Quantity
  VolUnit Int(6) Vol. Unit
  Weight1 Num(19,6) Weight 1
  Wght1Unit Int(6) Unit of Weight 1
  Weight2 Num(19,6) Weight 2
  Wght2Unit Int(6) Unit of Weight 2
  Factor1 Num(19,6) Factor 1
  Factor2 Num(19,6) Factor 2
  Factor3 Num(19,6) Factor 3
  Factor4 Num(19,6) Factor 4
  PackQty Num(19,6) Packing Quantity
  UpdInvntry VarChar(1) Warehouse Update default=Y [Y=Yes, N=No]
  BaseDocNum Int(11) Base Document No.
  BaseAtCard nVarChar(100) Customer/Vendor Base Document
  SWW nVarChar(16) Additional Identifier
  VatSum Num(19,6) Total Tax
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  FinncPriod Int(11) Posting Period ->OFPR
  ObjType nVarChar(20) Object Type default=21 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BlockNum nVarChar(100) Block Number
  ImportLog nVarChar(20) Import Log
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAqcuistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  DistribSum Num(19,6) Distributed Amount
  DstrbSumFC Num(19,6) Distributed Amount (FC)
  DstrbSumSC Num(19,6) Distributed Amount (SC)
  GrssProfit Num(19,6) Row Gross Profit
  GrssProfSC Num(19,6) Row Gross Profit (SC)
  GrssProfFC Num(19,6) Row Gross Profit (FC)
  VisOrder Int(11) Visual Order
  INMPrice Num(19,6) Item's Last Sales Price (OINM)
  PoTrgNum Int(11) PO Target No.
  PoTrgEntry nVarChar(11) PO Target Internal ID
  DropShip VarChar(1) Drop-Ship default=N [Y=Yes, N=No]
  PoLineNum Int(11) PO Target Row No.
  Address nVarChar(254) Address
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type [Y=Regular Tax, N=No Tax, U=Use Tax]
  OrigItem nVarChar(50) Original Item ->OITM
  BackOrdr VarChar(1) Allow Backorder [Y=Yes, N=No]
  FreeTxt nVarChar(100) Free Text
  PickStatus VarChar(1) Pick Status default=N [Y=Picked, N=Not Picked, R=Released for Picking, P=Partially Picked]
  PickOty Num(19,6) Pick Quantity
  PickIdNo Int(11) Pick ID
  TrnsCode Int(6) Shipping Method default=-1 ->OSHP
  VatAppld Num(19,6) Applied Tax
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  BaseQty Num(19,6) Base Quantity
  BaseOpnQty Num(19,6) Base Open Quantity
  VatDscntPr Num(19,6) Tax Discount %
  WtLiable VarChar(1) Withholding Tax Liable [Y=Yes, N=No]
  DeferrTax VarChar(1) Deferred Tax default=N [Y=Yes, N=No]
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatlF Num(19,6) Net Tax Amount
  LineVatS Num(19,6) Net Tax Amount
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value
  CEECFlag VarChar(1) Correction Invoice Was/Should Be default=S [W=Was, S=Should Be]
  ToStock Num(19,6) Corr. Invoice Amt to Inventory
  ToDiff Num(19,6) Corr. Invoice Amount to Diff.
  ExciseAmt Num(19,6) Excise Amount
  TaxPerUnit Num(19,6) Tax per Unit
  TotInclTax Num(19,6) Total Including Tax
  CountryOrg nVarChar(3) Country/Region of Origin
  StckDstSum Num(19,6) Stock Distribution Sum
  ReleasQtty Num(19,6) Released Quantity
  LineType VarChar(1) Row Type default=R [R=Regular]
  TranType VarChar(1) Transaction Type [C=Complete, R=Reject]
  Text Text(16) Text
  OwnerCode Int(11) Document Owner
  StockPrice Num(19,6) Inventory Price
  ConsumeFCT VarChar(1) Consumer Sales Forecast [Y=Yes, N=No]
  LstByDsSum Num(19,6) Last Buy Distribute Sum
  StckINMPr Num(19,6) Stock Inm Price
  LstBINMPr Num(19,6) Last Buy Inventory Journal Pr.
  StckDstFc Num(19,6) Stock Distribution Sum (FC)
  StckDstSc Num(19,6) Stock Distribution Sum (SC)
  LstByDsFc Num(19,6) Last Buy Distribute Sum (FC)
  LstByDsSc Num(19,6) Last Buy Distribute Sum (SC)
  StockSum Num(19,6) Stock Sum
  StockSumFc Num(19,6) Stock Sum FC
  StockSumSc Num(19,6) Stock Sum SC
  StckSumApp Num(19,6) Stock Sum Applied
  StckAppFc Num(19,6) Stock Sum Applied FC
  StckAppSc Num(19,6) Stock Sum Applied SC
  ShipToCode nVarChar(50) Ship-to Code
  ShipToDesc nVarChar(254) Ship-to Description
  StckAppD Num(19,6) Stock Distrib. - Applied Sum
  StckAppDFC Num(19,6) Stock Dist. - Applied Sum (FC)
  StckAppDSC Num(19,6) Stock Dist. - Applied Sum (SC)
  BasePrice VarChar(1) Price for Total Calculation default=E [E=Exclude Tax, I=Include Tax]
  GTotal Num(19,6) Gross Total
  GTotalFC Num(19,6) Gross Total (FC)
  GTotalSC Num(19,6) Gross Total (SC)
  DistribExp VarChar(1) Distribute Freight [Y=Yes, N=No]
  DescOW VarChar(1) Description Overwritten default=N [Y=Yes, N=No]
  DetailsOW VarChar(1) Details Overwritten default=N [Y=Yes, N=No]
  GrossBase Int(6) Base Method for Gross Profit
  VatWoDpm Num(19,6) Tax Before DPM Applied
  VatWoDpmFc Num(19,6) Tax Before DPM Applied (FC)
  VatWoDpmSc Num(19,6) Tax Before DPM Applied (SC)
  CFOPCode nVarChar(6) CFOP Code for Document ->OCFP
  CSTCode nVarChar(6) CST Code for ICMS
  Usage Int(11) Usage Code for Document ->OUSG
  TaxOnly VarChar(1) Tax Only [Y=Yes, N=No]
  WtCalced VarChar(1) Withholding Tax Calculated default=N [N=No, Y=Yes]
  QtyToShip Num(19,6) Quantity to Ship
  DelivrdQty Num(19,6) Delivered Quantity
  OrderedQty Num(19,6) Ordered Quantity
  CogsOcrCod nVarChar(8) COGS Distribution Rule Code ->OOCR
  CiOppLineN Int(11) Line Number of Opposite Line default=-1
  CogsAcct nVarChar(15) COGS Account Code ->OACT
  ChgAsmBoMW VarChar(1) Change Whs for Asm BoM Child [Y=Yes, N=No]
  ActDelDate Date(8) Actual Delivery Date
  OcrCode2 nVarChar(8) Costing Code 2 ->OOCR
  OcrCode3 nVarChar(8) Costing Code 3 ->OOCR
  OcrCode4 nVarChar(8) Costing Code 4 ->OOCR
  OcrCode5 nVarChar(8) Costing Code 5 ->OOCR
  TaxDistSum Num(19,6) Tax Distributed Amount
  TaxDistSFC Num(19,6) Tax Distributed Amount (FC)
  TaxDistSSC Num(19,6) Tax Distributed Amount (SC)
  PostTax VarChar(1) Post Tax in Price to Stock default=Y [Y=Yes, N=No]
  Excisable VarChar(1) Excisable [Yes/No] [Y=Yes, N=No]
  AssblValue Num(19,6) Assessable Value
  RG23APart1 Int(11) RG23A Part1 Number
  RG23APart2 Int(11) RG23A Part2 Number
  RG23CPart1 Int(11) RG23C Part1 Number
  RG23CPart2 Int(11) RG23C Part2 Number
  CogsOcrCo2 nVarChar(8) COGS Distribution Rule Code2 ->OOCR
  CogsOcrCo3 nVarChar(8) COGS Distribution Rule Code3 ->OOCR
  CogsOcrCo4 nVarChar(8) COGS Distribution Rule Code4 ->OOCR
  CogsOcrCo5 nVarChar(8) COGS Distribution Rule Code5 ->OOCR
  LnExcised VarChar(1) Line Excised [O=Open, C=Closed, P=Copied to OEI]
  LocCode Int(11) Location Code ->OLCT
  StockValue Num(19,6) Total COGS Value
  GPTtlBasPr Num(19,6) Total Base Price for Profit
  unitMsr2 nVarChar(100) Pur/Sal UoM if BaseUnit
  NumPerMsr2 Num(19,6) Pur/Sal UoM Value if Base Unit
  SpecPrice VarChar(1) Price Source Type default=N [Y=Special Prices for Business Partner, N=Manual, W=Active Price List, Discount Groups, R=Active Price List, U=Inactive Price List, A=Blanket Agreement, P=Period and Volume Discounts, Q=Period and Volume Discounts, Discount Groups, V=Inactive Price List, Discount Groups, 9=Special Prices for Business Partner, !=Blanket Agreement, 0=Period and Volume Discounts, 1=Period and Volume Discounts, Discount Groups, 2=Active Price List, 7=Active Price List, Discount Groups, 5=Inactive Price List, 6=Inactive Price List, Discount Groups]
  CSTfIPI nVarChar(2) CST for IPI Code
  CSTfPIS nVarChar(2) CST for PIS Code
  CSTfCOFINS nVarChar(2) CST for COFINS Code
  ExLineNo nVarChar(10) ExLineNo
  isSrvCall VarChar(1) Created from Service Call default=N [Y=Yes, N=No]
  PQTReqQty Num(19,6) Pur Quotation: Required Qty
  PQTReqDate Date(8) Pur Quotation: Required Date
  PcDocType Int(11) Purchase Confirmation Doc Type default=-1 [-1=No Type, 22=Purchase Order, 540000006=Purchase Quotation]
  PcQuantity Num(19,6) Purchase Confirmation Quantity
  LinManClsd VarChar(1) Line Was Closed Manually default=N [Y=Yes, N=No, U=Unknown]
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  NoInvtryMv VarChar(1) Without Inventory Movement default=N [Y=Yes, N=No]
  ActBaseEnt Int(11) Actual Base Document Entry
  ActBaseLn Int(11) Actual Base Line Number
  ActBaseNum Int(11) Actual Base Document No.
  OpenRtnQty Num(19,6) Quantity Open for Return
  AgrNo Int(11) Agreement No. ->OOAT
  AgrLnNum Int(11) Agreement Row Number
  CredOrigin VarChar(1) Credit Origin ->OBSI
  Surpluses Num(19,6) Surpluses
  DefBreak Num(19,6) Defect and Breakup
  Shortages Num(19,6) Shortages
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  UomEntry2 Int(11) UoM Entry if Base Unit default=0 ->OUOM
  UomCode nVarChar(20) UoM Code
  UomCode2 nVarChar(20) UoM Code if Base Unit
  FromWhsCod nVarChar(8) From Warehouse Code ->OWHS
  NeedQty VarChar(1) Consider Quantity of Items default=N [Y=Yes, N=No]
  PartRetire VarChar(1) Partial Retirement default=N [Y=Yes, N=No]
  RetireQty Num(19,6) Retirement Quantity
  RetireAPC Num(19,6) Retirement APC
  RetirAPCFC Num(19,6) Retirement APC FC
  RetirAPCSC Num(19,6) Retirement APC SC
  InvQty Num(19,6) Quantity - Inventory UoM
  OpenInvQty Num(19,6) Open Quantity (Inventory UoM)
  EnSetCost VarChar(1) Enable Set Item Cost in Return default=N [Y=Yes, N=No]
  RetCost Num(19,6) Return Cost in A/R Return
  Incoterms Int(11) Incoterms default=0 ->ODCI
  TransMod Int(11) Transport Mode default=0 ->ODCI
  LineVendor nVarChar(15) Line Vendor Code ->OCRD
  DistribIS VarChar(1) Distribute Intrastat Freight default=N [Y=Yes, N=No]
  ISDistrb Num(19,6) Intrastat Distrib. Amount
  ISDistrbFC Num(19,6) Intrastat Distrib. Amount (FC)
  ISDistrbSC Num(19,6) Intrastat Distrib. Amount (SC)
  IsByPrdct VarChar(1) Item Is By-Product default=N [N=No, Y=Yes]
  ItemType Int(11) Item Type default=4 [4=Item]
  PriceEdit VarChar(1) Price Was Edited by User default=N [N=No, Y=Yes]
  PrntLnNum Int(11) Parent Line Number
  LinePoPrss VarChar(1) Line PO Process default=N [Y=Yes, N=No]
  FreeChrgBP VarChar(1) Free of Charge (BP) default=N [Y=Yes, N=No]
  TaxRelev VarChar(1) Tax Relevant Row default=Y [Y=Yes, N=No]
  LegalText nVarChar(254) Legal Text
  ThirdParty VarChar(1) Third Party default=N [Y=Yes, N=No]
  LicTradNum nVarChar(32) Federal Tax ID
  InvQtyOnly VarChar(1) Change Qty (Inv. UoM) Only default=N [Y=Yes, N=No]
  UnencReasn Int(11) Reason for Unencumbered ICMS
  ShipFromCo nVarChar(50) Ship-From Code
  ShipFromDe nVarChar(254) Ship-From Description
  FisrtBin nVarChar(228) First Bin Location
  AllocBinC nVarChar(11) Allocated Bin Location Count
  ExpType nVarChar(4) Expense Type ->OEXD
  ExpUUID nVarChar(50) Expense UUID
  ExpOpType VarChar(1) Expense Operation Type [P=Professional Services, R=Renting Assets, O=Others]
  DIOTNat nVarChar(3) DIOT Nationality ->OCRY
  MYFtype nVarChar(2) MYF type [S1=MYF Wholesale Sales, S2=Retail Sales, P1=MYF Wholesale Purchases, P3=Other Expense Transactions]
  GPBefDisc Num(19,6) Gross Price
  ReturnRsn Int(6) Return Reason default=-1
  ReturnAct Int(6) Return Action default=-1
  StgSeqNum Int(11) Stage Sequence Number
  StgEntry Int(11) Stage Entry ->ORST
  StgDesc nVarChar(100) Stage Description
  ItmTaxType nVarChar(2) Item GST Tax Category [GR=GST Regular, GN=GST Nil Rated, GE=GST Exempt, NE=Excisable, NN=Non-GST Non-Excisable]
  SacEntry Int(11) SAC Entry ->OSAC
  NCMCode Int(11) NCM Code default=-1 ->ONCM
  HsnEntry Int(11) HSN Entry
  OriBAbsEnt Int(11) Original Base Document Internal ID
  OriBLinNum Int(11) Original Base Document Line Number
  OriBDocTyp Int(11) Original Base Document Type
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No, U=Use]
  EncryptIV nVarChar(100) Encrypt IV
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  StdItemId Int(11) Standard Item Identification ->OUNCL
  CommClass Int(11) Commodity Classification ->OUNCL
  VatExEntry Int(11) VAT Exemption AbsEntry ->OVEB
  VatExLN Int(6) VAT Exemption LineNum
  NatOfTrans Int(11) Nature of Transaction ->ODCI
  ISDtCryImp nVarChar(3) Destination Country/Region for Import ->OCRY
  ISDtRgnImp Int(11) Destination Region for Import ->ODCI
  ISOrCryExp nVarChar(3) Country/Region of Origin for Export ->OCRY
  ISOrRgnExp Int(11) Region of Origin for Export ->ODCI
  NVECode nVarChar(6) NVE Code
  PoNum nVarChar(20) Customer's Purchase Order Number
  PoItmNum Int(11) Customer's Purchase Order Item Number
  IndEscala VarChar(1) Indicator for Relevant Scale default=N [Y=Yes, N=No]
  CESTCode Int(11) CEST Code ->OCEST
  CtrSealQty Num(19,6) Control Seal Quantity
  CNJPMan nVarChar(14) CNPJ of Manufacturer
  UFFiscBene nVarChar(10) UF Fiscal Benefit Code
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]
  LegalTIMD nVarChar(250) Legal Text from Item Master Data
  LegalTTCA nVarChar(250) Legal Text from Tax Code Attributes
  LegalTW nVarChar(250) Legal Text from Warehouse
  LegalTCD nVarChar(250) Legal Text from Tax Code Determination
  RevCharge VarChar(1) Reverse Charge default=N [Y=Yes, N=No]
  ListNum Int(6) Price List No. ->OPLN

# RPD10 - Goods Return - Row Structure
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SECONDARY U: DocEntry, AftLineNum, OrderNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPD
  LineSeq Int(11) Row Sequence
  AftLineNum Int(11) After Row Number
  OrderNum Int(11) Order Number
  LineType VarChar(1) Row Type [T=Text, S=Subtotal]
  LineText Text(16) Row Text
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=21 ->ADP1

# RPD11 - Gds Return - Drawn Dpm Detail
Module: Marketing Documents | 70 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LineSeq
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPD
  LineNum Int(11) Row Number
  LineSeq Int(11) Sequence Number
  BaseAbs Int(11) Base Document Internal ID
  BaseType Int(11) Base Object Type default=-1 [-1=]
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  VatPrcnt Num(19,6) VAT Percent
  LineTotal Num(19,6) Net LC
  TotalFrgn Num(19,6) Net FC
  TotalSumSy Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFrgn Num(19,6) Tax FC
  VatSumSys Num(19,6) Tax SC
  ObjType nVarChar(20) Object Type default=21 ->ADP1
  LogInstanc Int(11) Log Instance
  IsAcq VarChar(1) Acquisition Tax-Liable default=N [N=No, Y=Yes]
  IsAllDrawn VarChar(1) Remaining Amount Drawn default=N [Y=Yes, N=No]
  IsGross VarChar(1) Is Gross Line default=N [N=Net Line, Y=Gross Line]
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  ApplNet Num(19,6) Applied Net LC
  ApplNetFc Num(19,6) Applied Net FC
  ApplNetSc Num(19,6) Applied Net SC
  ApplVat Num(19,6) Applied Tax LC
  ApplVatFc Num(19,6) Applied Tax FC
  ApplVatSc Num(19,6) Applied Tax SC
  BaseNet Num(19,6) Base Net LC
  BaseNetFc Num(19,6) Base Net FC
  BaseNetSc Num(19,6) Base Net SC
  BaseVat Num(19,6) Base Tax LC
  BaseVatFc Num(19,6) Base Tax FC
  BaseVatSc Num(19,6) Base Tax SC
  BaseGross Num(19,6) Base Gross LC
  BaseGrossF Num(19,6) Base Gross FC
  BaseGrossS Num(19,6) Base Gross SC
  LineType VarChar(1) Line Type default=D [D=Document Row, R=Currency Rounding, H=Down Payment Document Rounding]
  DctSum Num(19,6) Deductible Sum LC
  DctSumFc Num(19,6) Deductible Sum FC
  DctSumSc Num(19,6) Deductible Sum SC
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplDct Num(19,6) Applied Deductible Sum LC
  ApplDctFc Num(19,6) Applied Deductible Sum FC
  ApplDctSc Num(19,6) Applied Deductible Sum SC
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  BaseDct Num(19,6) Base Deductible Sum LC
  BaseDctFc Num(19,6) Base Deductible Sum FC
  BaseDctSc Num(19,6) Base Deductible Sum SC
  BaseEq Num(19,6) Base Equalization Sum LC
  BaseEqFc Num(19,6) Base Equalization Sum FC
  BaseEqSc Num(19,6) Base Equalization Sum SC
  TaxCode nVarChar(8) Tax Code ->OSTC
  ApplGross Num(19,6) Applied Gross LC
  ApplGrossF Num(19,6) Applied Gross FC
  ApplGrossS Num(19,6) Applied Gross SC
  TaxAdjust VarChar(1) Manual Tax Adjustment default=N [Y=Yes, N=No]
  RvsChrgSum Num(19,6) Reverse Charge Sum LC
  RvsChrgFc Num(19,6) Reverse Charge Sum FC
  RvsChrgSc Num(19,6) Reverse Charge Sum SC
  BasRvsChrg Num(19,6) Base Reverse Charge LC
  BasRvsFc Num(19,6) Base Reverse Charge FC
  BasRvsSc Num(19,6) Base Reverse Charge SC
  ApplRvs Num(19,6) Applied Reverse Charge LC
  ApplRvsFc Num(19,6) Applied Reverse Charge FC
  ApplRvsSc Num(19,6) Applied Reverse Charge SC
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# RPD12 - Goods Return - Tax Extension
Module: Marketing Documents | 117 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPD
  TaxId0 nVarChar(100) Tax ID 0
  TaxId1 nVarChar(100) Tax ID 1
  TaxId2 nVarChar(100) Tax ID 2
  TaxId3 nVarChar(100) Tax ID 3
  TaxId4 nVarChar(100) Tax ID 4
  TaxId5 nVarChar(100) Tax ID 5
  TaxId6 nVarChar(100) Tax ID 6
  TaxId7 nVarChar(100) Tax ID 7
  TaxId8 nVarChar(100) Tax ID 8
  TaxId9 nVarChar(100) Tax ID 9
  State nVarChar(3) State Code
  County nVarChar(7) County Code
  Incoterms nVarChar(3) Incoterms
  Vehicle nVarChar(10) Vehicle ID
  VidState nVarChar(3) Vehicle ID (State)
  NfRef nVarChar(254) Nota Fiscal Reference
  Carrier nVarChar(15) Carrier Code
  QoP Int(11) Quantity of Packs
  PackDesc nVarChar(10) Pack Description
  Brand nVarChar(20) Brand
  NoSU Int(11) Number of Shipping Unit
  NetWeight Num(19,6) Net Weight
  GrsWeight Num(19,6) Gross Weight
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=21 ->ADP1
  TaxId10 nVarChar(100) Tax ID 10
  TransCat nVarChar(100) Transaction Category
  FormNo nVarChar(100) Form No.
  TaxId11 nVarChar(100) Tax ID 11
  StreetS nVarChar(100) Street
  BlockS nVarChar(100) Block
  BuildingS Text(16) Building/Floor/Room
  CityS nVarChar(100) City
  ZipCodeS nVarChar(20) Zip Code
  CountyS nVarChar(100) County
  StateS nVarChar(3) State ->OCST
  CountryS nVarChar(3) Country/Region ->OCRY
  AddrTypeS nVarChar(100) Address Type
  StreetNoS nVarChar(100) Street No.
  StreetB nVarChar(100) Street
  BlockB nVarChar(100) Block
  BuildingB Text(16) Building/Floor/Room
  CityB nVarChar(100) City
  ZipCodeB nVarChar(20) Zip Code
  CountyB nVarChar(100) County
  StateB nVarChar(3) State ->OCST
  CountryB nVarChar(3) Country/Region ->OCRY
  AddrTypeB nVarChar(100) Address Type
  StreetNoB nVarChar(100) Street No.
  ImpORExp VarChar(1) Import or Export [N=, Y=]
  Vat VarChar(1) VAT default=N [N=No VAT Support, Y=VAT Support]
  AltCrdNamB nVarChar(100) Alternative BP Name
  AltTaxIdB nVarChar(32) Alternative Tax ID
  Address2S nVarChar(50) Address Name 2
  Address3S nVarChar(50) Address Name 3
  Address2B nVarChar(50) Address Name 2
  Address3B nVarChar(50) Address Name 3
  MainUsage Int(11) Main Usage Code of Document ->OUSG
  GlbLocNumS nVarChar(50) Global Location Number
  GlbLocNumB nVarChar(50) Global Location Number
  CollectDT nVarChar(20) Date and Time of Collection
  TransprtDT Date(8) Transport Starting Date
  TransprtRS nVarChar(100) Transport Reason
  TaxId12 nVarChar(50) Tax ID 12
  TaxId13 nVarChar(100) Deductee Ref. No. in India
  ImpExpNo nVarChar(100) Import/Export Bill No.
  ImpExpDate Date(8) Import/Export Date
  BpGSTType Int(11) GST Regn Type of BP
  BpGSTN nVarChar(15) GST Regn No of BP
  BpStateCod nVarChar(3) State Code of Business Partner ->OCST
  BPStatGSTN nVarChar(2) GST State Code of BP
  LocGSTType Int(11) GST Regn Type of Location
  LocGSTN nVarChar(15) GST Regn No of Location
  LocStatCod nVarChar(3) State Code of Location ->OCST
  LocStaGSTN nVarChar(2) GST State Code of Location
  BpCountry nVarChar(3) Country/Region Code of BP ->OCRY
  OrigImpNo nVarChar(100) Original Bill of Entry No.
  OrigImpDat Date(8) Original Bill of Entry Date
  ExportType VarChar(1) Exporting Type default=E [E=Imports/Exports, S=SEZ Developer, U=SEZ Unit, D=Deemed Imports/Exports]
  PortCode nVarChar(100) Port Code
  BoEValue Num(19,6) Bill of Entry Value
  IsIGSTAct VarChar(1) Supply under IGST Account [Y=Yes, N=No]
  ClaimRefun VarChar(1) Claim Refund [Y=Yes, N=No]
  TaxRateDif Int(11) Differential % of Tax Rate [65=, 100=]
  BPGdsIssP nVarChar(15) Goods Issue Place BP
  CNPJGIP nVarChar(100) Goods Issue Place CNPJ
  CPFGIP nVarChar(100) Goods Issue Place CPF
  StreetGIP nVarChar(100) Goods Issue Place Street
  StrtNoGIP nVarChar(100) Goods Issue Place Street No.
  BldngGIP Text(16) Goods Issue Place Building
  ZipGIP nVarChar(20) Goods Issue Place Zip Code
  BlockGIP nVarChar(100) Goods Issue Place Block
  CityGIP nVarChar(100) Goods Issue Place City
  CountyGIP nVarChar(100) Goods Issue Place County
  StateGIP nVarChar(3) Goods Issue Place State ->OCST
  CountryGIP nVarChar(3) Goods Issue Place Country/Region ->OCRY
  PhoneGIP nVarChar(20) Goods Issue Place Phone
  EMailGIP nVarChar(100) Goods Issue Place E-Mail
  DptDateGIP Date(8) Goods Issue Place Departure Date
  BPDelivryP nVarChar(15) Delivery Place BP
  CNPJDlvryP nVarChar(100) Delivery Place CNPJ
  CPFDlvryP nVarChar(100) Delivery Place CPF
  StrtDlvryP nVarChar(100) Delivery Place Street
  StrNoDlvrP nVarChar(100) Delivery Place Street No.
  BldDlvryP Text(16) Delivery Place Building
  ZipDlvryP nVarChar(20) Delivery Place Zip Code
  BlckDlvryP nVarChar(100) Delivery Place Block
  CityDlvryP nVarChar(100) Delivery Place City
  CntyDlvryP nVarChar(100) Delivery Place County
  StatDlvryP nVarChar(3) Delivery Place State ->OCST
  CtryDlvryP nVarChar(3) Delivery Place Country/Region ->OCRY
  FoneDlvryP nVarChar(20) Delivery Place Phone
  MailDlvryP nVarChar(100) Delivery Place E-Mail
  DpDtDlvryP Date(8) Delivery Place Departure Date
  AuthedCNPJ nVarChar(250) Authorized CNPJ or CPF
  TaxId14 nVarChar(250) ITR Filing

# RPD13 - Goods Returns Rows - Distributed Expenses
Module: Marketing Documents | 59 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPD
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=21 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Aquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Normal Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) VAT Applied Frgn
  VatAppldSC Num(19,6) VAT Applied Sys
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock default=N [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Line No.
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Abs. Entry default=-1
  BaseGroup Int(11) Base Document Group default=-1
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1
  VisOrder Int(11) Visual Order
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DistribExp VarChar(1) Distribute Freights [Y=Yes, N=No]
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ

# RPD14 - Goods Return - Assembly - Rows
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPD
  LineNum Int(11) Row Number default=-1
  ChildNum Int(11) Child Number default=-1
  ItemCode nVarChar(50) Item no. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  TotalQty Num(19,6) Total Quantity
  OpenQty Num(19,6) Remaining Open Quantity
  ObjectType nVarChar(20) object type default=21 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BaseChildN Int(11) Base Child Number default=-1
  EncryptIV nVarChar(100) Encrypt IV

# RPD15 - Gds Return - Drawn Dpm Applied
Module: Marketing Documents | 84 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPD
  LineNum Int(11) Row Number
  ObjType nVarChar(20) object type default=21 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  StaCode nVarChar(8) Tax Authority Code
  StaType Int(11) Tax Authority Type
  StaIndex Int(11) Tax Authority Seq Index
  BaseNet Num(19,6) Net LC
  BaseNetFc Num(19,6) Net FC
  BaseNetSc Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFc Num(19,6) Tax FC
  VatSumSc Num(19,6) Tax SC
  DctSum Num(19,6) Deductible Sum LC
  DctSumFc Num(19,6) Deductible Sum FC
  DctSumSc Num(19,6) Deductible Sum SC
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplNet Num(19,6) Applied Net LC
  ApplNetFc Num(19,6) Applied Net FC
  ApplNetSc Num(19,6) Applied Net SC
  ApplVat Num(19,6) Applied Tax LC
  ApplVatFc Num(19,6) Applied Tax FC
  ApplVatSc Num(19,6) Applied Tax SC
  ApplDct Num(19,6) Applied Deductible Sum LC
  ApplDctFc Num(19,6) Applied Deductible Sum FC
  ApplDctSc Num(19,6) Applied Deductible Sum SC
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  PaidNet Num(19,6) Paid Net LC
  PaidNetFc Num(19,6) Paid Net FC
  PaidNetSc Num(19,6) Paid Net SC
  PaidVat Num(19,6) Paid Tax LC
  PaidVatFc Num(19,6) Paid Tax FC
  PaidVatSc Num(19,6) Paid Tax SC
  PaidDct Num(19,6) Paid Deductible Sum LC
  PaidDctFc Num(19,6) Paid Deductible Sum FC
  PaidDctSc Num(19,6) Paid Deductible Sum SC
  PaidEq Num(19,6) Paid Equalization Sum LC
  PaidEqFc Num(19,6) Paid Equalization Sum FC
  PaidEqSc Num(19,6) Paid Equalization Sum SC
  DpApplNet Num(19,6) Dpm Appl Net LC
  DpApplNetF Num(19,6) Dpm Appl Net FC
  DpApplNetS Num(19,6) Dpm Appl Net SC
  DpApplVat Num(19,6) Dpm Appl Tax LC
  DpApplVatF Num(19,6) Dpm Appl Tax FC
  DpApplVatS Num(19,6) Dpm Appl Tax SC
  DpApplDct Num(19,6) Dpm Appl Deductible Sum LC
  DpApplDctF Num(19,6) Dpm Appl Deductible Sum FC
  DpApplDctS Num(19,6) Dpm Appl Deductible Sum SC
  DpApplEq Num(19,6) Dpm Appl Equalization Sum LC
  DpApplEqFc Num(19,6) Dpm Appl Equalization Sum FC
  DpApplEqSc Num(19,6) Dpm Appl Equalization Sum SC
  TaxCode nVarChar(8) Tax Code ->OSTC
  LineType VarChar(1) Row Type default=D [D=Document, R=Exchange Rate Rounding, H=Document Header Rounding]
  BaseGrs Num(19,6) Gross LC
  BaseGrsFc Num(19,6) Gross FC
  BaseGrsSc Num(19,6) Gross SC
  ApplGrs Num(19,6) Applied Gross LC
  ApplGrsFc Num(19,6) Applied Gross FC
  ApplGrsSc Num(19,6) Applied Gross SC
  PaidGrs Num(19,6) Paid Gross LC
  PaidGrsFc Num(19,6) Paid Gross FC
  PaidGrsSc Num(19,6) Paid Gross SC
  DpApplGrs Num(19,6) Dpm Appl Gross LC
  DpApplGrsF Num(19,6) Dpm Appl Gross FC
  DpApplGrsS Num(19,6) Dpm Appl Gross SC
  RvsChrgSum Num(19,6) Reverse Charge Sum
  RvsChrgSc Num(19,6) Reverse Charge Sum (SC)
  RvsChrgFc Num(19,6) Reverse Charge Sum (FC)
  ApplRvs Num(19,6) Applied Reverse Charge Sum LC
  ApplRvsSc Num(19,6) Applied Reverse Charge Sum SC
  ApplRvsFc Num(19,6) Applied Reverse Charge Sum FC
  PaidRvs Num(19,6) Paid Reverse Charge Sum LC
  PaidRvsSc Num(19,6) Paid Reverse Charge Sum SC
  PaidRvsFc Num(19,6) Paid Reverse Charge Sum FC
  DpApplRvs Num(19,6) Dpm Applied Reverse Charge LC
  DpApplRvsS Num(19,6) Dpm Applied Reverse Charge SC
  DpApplRvsF Num(19,6) Dpm Applied Reverse Charge FC
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# RPD16 - Goods Return - SnB properties
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, SnBIndex
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) abs entry ->ORPD
  LineNum Int(11) Line Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object id
  ObjAbs Int(11) Object Abs
  DrfWObjAbs Int(11) draft Wobj Abs default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type default=21
  LogInstanc Int(11) Log Instance

# RPD17 - Goods Return - Import Process
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPD
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=21 ->ADP1
  ImpDocType VarChar(1) Type of Importation Document ->OBSI
  ImpDocNum nVarChar(10) Importation Document Number
  DateOfReg Date(8) Date of Registry DI/DSI/DA
  CustClrDat Date(8) Date of Customs Clearance
  ConcActNum nVarChar(30) Drawback Concession Acct No.
  AdditNum nVarChar(30) Additional Number
  AddItmDV Num(19,6) Additional Item Discount Value
  tpVTransp Int(6) Overland Transport Route [1=Maritime, 2=Waterway, 3=Lakeside, 4=Air, 5=Post, 6=Train, 7=Road, 8=Network Transmission, 9=Own Means, 10=Input/Output Fictitious, 11=Courier, 12=Hand Carry]
  DrawSReg nVarChar(11) Drawback - Suspension Regime
  AddFrNavyA Num(19,6) Additional Freight to Navy Authority
  TypeOfImp VarChar(1) Type of Import
  nSeqAdic Int(6) Additional Item Sequential Number

# RPD18 - Goods Return - Export Process
Module: Marketing Documents | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPD
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=21 ->ADP1
  ExpDocType Int(11) Type of Exportation Document default=-1 ->OBNI
  ExpDeclNum Int(11) Exportation Declaration Number
  ExpDeclDat Date(8) Exportation Declaration Date
  ExpNature Int(11) Nature of Exportation default=-1 ->OBNI
  ExpRegNum Int(11) Number of Exportation Registry
  ExpRegDate Date(8) Date of Exportation Registry
  LadBillNum nVarChar(19) Bill of Lading Number
  LadBillDat Date(8) Date of Bill of Lading
  MerchLeftD Date(8) Date Merchandise Left Customs
  LadBillTyp Int(11) Type of Bill of Lading default=-1 ->OBNI
  DrawSReg nVarChar(11) Drawback - Suspension Regime
  NatureExp nVarChar(44) Nature of Export
  QultExpItm Num(19,6) Quantity of Exported Items
  nSeqAdic Int(6) Additional Item Sequential Number

# RPD19 - Goods Return - Bin Allocation Data
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, BinAllocSe
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->ORPD
  BinAllocSe Int(11) Bin Allocation Sequence
  LineNum Int(11) Line Number
  SubLineNum Int(11) Subline Number default=-1
  SnBType Int(11) SnB Type default=-1
  SnBMDAbs Int(11) SnB Master Data Internal No. default=-1
  BinAbs Int(11) Bin Internal Number ->OBIN
  Quantity Num(19,6) Quantity
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjType nVarChar(20) Object Type default=21 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  BinActTyp Int(6) Bin Action Type [1=Transaction In, 2=Transaction Out, 4=SnB Complete, 8=Bin First Then SnB]

# RPD2 - Goods Return - Freight - Rows
Module: Marketing Documents | 64 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPD
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=21 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) Vat Applied
  VatAppldFC Num(19,6) Vat Applied Frgn
  VatAppldSC Num(19,6) Vat Applied Sys
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report [Y=Yes, N=No]
  BaseGroup Int(11) Base Document Group default=-1 [-1=, 0=, 1=, 2=]
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1 [-1=, 0=, 1=, 2=]
  VisOrder Int(11) Visual Order
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]

# RPD20 - Intrastat Expenses
Module: Marketing Documents | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPD
  ExpnsCode Int(11) Freight Code ->OEXD
  TotalLC Num(19,6) Total
  TotalFC Num(19,6) Total (FC)
  TotalSC Num(19,6) Total (SC)
  DistribM VarChar(1) Distribution Method default=T [Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DrawnLC Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  LineNum Int(11) Line Number default=-1
  BaseAbsEnt Int(11) Base Abs. Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 16=Return, 13=A/R Invoice, 203=Down Payment Incoming, 204=Down Payment Outgoing, 22=Purchase Order, 20=Goods Receipt PO, 21=Goods Return, 18=A/P Invoice, 540000006=Purchase Quotation, 0=, -1=]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No. default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=21 ->ADP1
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  AppliedLC Num(19,6) Applied
  AppliedFC Num(19,6) Applied (FC)
  AppliedSC Num(19,6) Applied (SC)

# RPD21 - Goods Return - Document Reference Information
Module: Marketing Documents | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, RefType
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjectType nVarChar(20) Object Type default=21
  LogInstanc Int(11) Log Instance default=0
  RefType VarChar(1) Reference Types default=S [S=System Document, E=External Document]
  LineNum Int(11) Line Number
  RefDocEntr Int(11) Referenced Internal Number
  RefDocNum Int(11) Referenced Document Number
  ExtDocNum nVarChar(100) External Referenced Document Number
  RefObjType nVarChar(20) Referenced Object Type [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 234000031=Return Request, 16=Return, 203=A/R Down Payment, 13=A/R Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 280=A/R Tax Invoice, 1470000113=Purchase Request, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Return Request, 21=Goods Return, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 281=A/P Tax Invoice, 69=Landed Costs, 24=Incoming Payments, 46=Outgoing Payments, 57=Checks for Payment, 321=Internal Reconciliation, 34=Recurring Posting, 30=Journal Entry, 59=Goods Receipt, 60=Goods Issue, 162=Inventory Revaluation, 1470000065=Inventory Counting, 10000071=Inventory Posting, 1250000001=Inventory Transfer Request, 67=Inventory Transfer, 202=Production Order, 13001=Original Invoice, -1=External Document, 20301=Original Down Payment Invoice]
  AccessKey nVarChar(100) Access Key
  IssueDate Date(8) Date of Issue
  IssuerCNPJ nVarChar(100) Issuer CNPJ
  IssuerCode nVarChar(10) Fiscal Document Issuer UF Code
  Model nVarChar(6) Fiscal Document Model
  Series nVarChar(3) Fiscal Document Series
  Number Int(11) Fiscal Document Number
  RefAccKey nVarChar(100) Referenced CT-e Access Key
  RefAmount Num(19,6) Referenced Amount
  SubSeries nVarChar(3) Fiscal Document Subseries
  Remark nVarChar(254) Remarks
  LinkRefTyp nVarChar(20) Link Reference Type default=00 [00=, 01=Nota de cr�dito de los documentos relacionados, 02=Nota de d�bito de los documentos relacionados, 03=Devoluci�n de mercanc�a sobre facturas o traslados previos, 04=Sustituci�n de los CFDI previos, 05=Traslados de mercancias facturados previamente, 06=Factura generada por los traslados previos, 07=CFDI por aplicaci�n de anticipo, 08=Customs, MX_08=Factura generada por pagos en parcialidades, 09=Factura generada por pagos diferidos]

# RPD22 - Goods Return - Resource Costs
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, StdCostNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->RPD1
  LineNum Int(11) Row Number ->RPD1
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=21
  LogInstanc Int(11) Log Instance default=0

# RPD23 - A/P Invoice - Selected Asset Master Data
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, VisOrder
  ASSETS: DocEntry, LineNum, AssetCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPD
  LineNum Int(11) Row Number
  AssetCode nVarChar(50) Selected Asset Code ->OITM
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Remarks nVarChar(100) Remarks
  Amount Num(19,6) Amount
  AmountSC Num(19,6) Amount (SC)
  SerialNo nVarChar(30) Serial Number
  VisOrder Int(11) Visual Order
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=21 ->ADP1

# RPD24 - Goods Return - Tracking Note Assignment
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  ItemCCDNum nVarChar(40) Item CCD Number
  CntrOrigin nVarChar(3) Country/Region of Origin
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=21 ->ADP1
  SubLineNum Int(11) BOM Line No.

# RPD25 - Goods Return - Amt Per VAT Grp
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, VatGroup, Type
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  VatGroup nVarChar(8) Tax Definition ->OVTG
  VatPrcnt Num(19,6) Tax Rate
  BaseAmnt Num(19,6) Base Amount
  BaseAmntFC Num(19,6) Base Amount (FC)
  BaseAmntSC Num(19,6) Base Amount (SC)
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  Type Int(11) Type default=1 [1=Discount by Tax]
  Currency nVarChar(3) Price Currency
  Rate Num(19,6) Currency Rate
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=21 ->ADP1

# RPD26 - Goods Return - E-Way Bill Information
Module: Marketing Documents | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPD
  SuplyType nVarChar(20) EWB Transaction Type [O=Outward, I=Inward]
  SubSplyTyp Int(11) EWB Sub-Type ->OEST
  DocType nVarChar(3) EWB Doc. Type ->OEDT
  TransMode Int(11) EWB Transportation Mode ->OETM
  Distance Num(19,6) EWB Transport Distance
  TransDocNo nVarChar(16) EWB Transporter Doc. No.
  TransDate Date(8) EWB Transportation Date
  VehicleTyp nVarChar(2) EWB Vehicle Type ->OEVT
  VehicleNo nVarChar(15) EWB Vehicle Number
  EWayBillNo nVarChar(20) EWB No.
  EwbDate Date(8) E-Way Bill Date
  FrmTraName nVarChar(100) EWB Consignor Name
  FrmAddres1 nVarChar(120) EWB Consignor Address 1
  FrmAddres2 nVarChar(120) EWB Consignor Address 2
  FrmZipCode nVarChar(20) EWB Consignor Zip Code
  ActFrmStat nVarChar(2) Dispatch State of EWB Consignor
  ToTraName nVarChar(100) EWB Consignee Name
  ToAddres1 nVarChar(120) EWB Consignee Address 1
  ToAddres2 nVarChar(120) EWB Consignee Address 2
  ToZipCode nVarChar(20) EWB Consignee Zip Code
  ActToState nVarChar(2) Ship-To State of EWB Consignee
  FrmGSTN nVarChar(15) EWB Consignor GSTN
  FrmState nVarChar(2) Bill-To State of EWB Consignor
  ToGSTN nVarChar(15) EWB Consignee GSTN
  ToState nVarChar(2) Bill-To State of EWB Consignee
  MainHsnEnt Int(11) EWB Main HSN Entry ->OCHP
  FrmPlace nVarChar(50) EWB Consignor Place
  ToPlace nVarChar(50) EWB Consignee Place
  TransID nVarChar(15) EWB Transporter ID
  TransName nVarChar(25) EWB Transporter Name
  ExpireDate Date(8) EWB Expiration Date
  ObjectType nVarChar(20) Object Type default=21 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TspEntry Int(11) Transporter Abs. Entry ->OTSP
  TspLine Int(11) Transportation Line
  TransType Int(11) Transaction Type [1=Regular, 2=Bill To-Ship To, 3=Bill From-Dispatch From, 4=Combination of 2 and 3]

# RPD27 - Goods Return - E-Books(GR) Rows
Module: Marketing Documents | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  RELATE_ROW: DocEntry, RelateType, RelateLine, GroupNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPD
  LineNum Int(11) Row Number
  RelateType Int(11) Relation Type default=-1 [1=Row, 2=Row Expenses, 3=Document Expenses, 13=Distributed Freights, -1=Manual]
  RelateLine Int(11) Relation Row Number default=-1
  GroupNum Int(11) Group Number default=-1
  LineTotal Num(19,6) Line Total
  LineTotalF Num(19,6) Line Total (FC)
  LineTotalS Num(19,6) Line Total (SC)
  InClassTyp Int(11) Income Classification Type ->OICP
  InClassCat Int(11) Income Classification Category ->OICC
  ExClassTyp Int(11) Expense Classification Type ->OECP
  ExClassCat Int(11) Expense Classification Cat. ->OECC
  VatCate Int(11) VAT Category
  NetValue Num(19,6) Net Value
  NetValueFC Num(19,6) Net Value (FC)
  NetValueSC Num(19,6) Net Value (SC)
  VatAmount Num(19,6) VAT Amount
  VatAmFC Num(19,6) VAT Amount (FC)
  VatAmSC Num(19,6) VAT Amount (SC)
  WtPercCat Int(11) Withheld Percentage Category
  WtAmount Num(19,6) Withheld Amount
  WtAmountFC Num(19,6) Withheld Amount (FC)
  WtAmountSC Num(19,6) Withheld Amount (SC)
  ObjectType nVarChar(20) Object Type default=13 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  WtCategory VarChar(1) Withheld Category [I=Invoice, P=Payment]
  VATClassTy Int(11) VAT Classification Type ->OECP
  VATClassCa Int(11) VAT Classification Category ->OECC
  EBVatExCau Int(11) VAT Exemption Cause ->OVEC

# RPD28 - Goods Return - Reported Tracking Note
Module: Marketing Documents | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
  TCN_KEY U: DocEntry, LineNum, TrackingNt, TrackiNtLn
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  UnusedQty Num(19,6) Unused Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=21 ->ADP1
  SubLineNum Int(11) BOM Line No.

# RPD3 - Goods Return - Freight
Module: Marketing Documents | 80 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  DOCUMENT: DocEntry, BaseAbsEnt
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPD
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  Comments nVarChar(100) Remarks
  ObjType nVarChar(20) Object Type default=21 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  WTLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  VatApplied Num(19,6) Vat Applied
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatF Num(19,6) Net Tax Amount (FC)
  LineVatS Num(19,6) Net Tax Amount (SC)
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 20=Purchase Delivery Notes, 234000032=A/P Return Request]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No.
  LineNum Int(11) line num default=-1
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Doc. Internal No. default=-1
  StDstr Num(19,6) Stock Distributed Sum
  StDstrSC Num(19,6) Stock Distributed Sum (SC)
  StDstrFC Num(19,6) Stock Distributed Sum (FC)
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  TaxDistMtd VarChar(1) Tax Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  GrsAmount Num(19,6) Gross Amount
  GrsFC Num(19,6) Gross Amount (FC)
  GrsSC Num(19,6) Gross Amount (SC)
  BaseTotal VarChar(1) Base Total for Calculation default=N [N=Net Total, G=Gross Total]
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)
  RRVatLC Num(19,6) Return Request VAT Amount
  RRVatFC Num(19,6) Return Request VAT Amount (FC)
  RRVatSC Num(19,6) Return Request VAT Amount (SC)
  EncryptIV nVarChar(100) Encrypt IV
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]

# RPD4 - Goods Return - Tax Amount per Document
Module: Marketing Documents | 61 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SCONDARY: DocEntry, LineNum, GroupNum, ExpnsCode, StcCode, StaCode, staType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPD
  LineNum Int(11) Row Number default=-1
  GroupNum Int(11) Group Number default=-1
  ExpnsCode Int(11) Expense Code default=-1 ->OEXD
  RelateType Int(11) Relation Type default=1 [1=Row, 2=Row Freight Charges, 3=Document Expenses, 13=Distributed Freights]
  StcCode nVarChar(8) Tax Code ->OSTC
  StaCode nVarChar(8) Authority Code ->OSTA
  staType Int(11) Authority Type ->OSTT
  TaxRate Num(19,6) Tax Rate
  TaxAcct nVarChar(15) Tax Account ->OACT
  TaxSum Num(19,6) Tax Amount
  TaxSumFrgn Num(19,6) Tax Amount (FC)
  TaxSumSys Num(19,6) Tax Amount (SC)
  BaseSum Num(19,6) Base Amount
  BaseSumFrg Num(19,6) Base Amount (FC)
  BaseSumSys Num(19,6) Base Amount (SC)
  ObjectType nVarChar(20) Object Type default=21 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Status default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  LineSeq Int(11) Line Sequence
  DeferrAcct nVarChar(15) Deferred Tax Account ->OACT
  BaseType Int(11) Base Document Type default=-1
  BaseAbs Int(11) Base Doc Abs Entry default=-1
  BaseSeq Int(11) Base Doc. Line Sequence
  DeductTax Num(19,6) Deductible Tax Amount
  DdctTaxFrg Num(19,6) Deductible Tax Amount (FC)
  DdctTaxSys Num(19,6) Deductible Tax Amount (SC)
  BaseAppld Num(19,6) Applied Base Amount
  BaseApldFC Num(19,6) Applied Base Amount (FC)
  BaseApldSC Num(19,6) Applied Base Amount (SC)
  NonDdctPrc Num(19,6) Non Deductible %
  NonDdctAct nVarChar(15) Non Deductible Account ->OACT
  TaxInPrice VarChar(1) Tax Included in Price? default=N [Y=Yes, N=No]
  Exempt VarChar(1) Exempt? default=N [Y=Yes, N=No]
  TaxExpAct nVarChar(15) Expense Account for Tax ->OACT
  OnHoldTax Num(19,6) On Hold Tax Amount
  OnHoldTaxF Num(19,6) On Hold Tax Amount (FC)
  OnHoldTaxS Num(19,6) On Hold Tax Amount (SC)
  InGrossRev VarChar(1) Included in Gross Revenue default=N [Y=Yes, N=No]
  TaxSumOrg Num(19,6) Tax Amount Original
  TaxSumOrgF Num(19,6) Tax Amount Original (FC)
  TaxSumOrgS Num(19,6) Tax Amount Original (SC)
  OpenTax Num(19,6) Open Service Tax
  OpenTaxFC Num(19,6) Open Service Tax (FC)
  OpenTaxSC Num(19,6) Open Service Tax (SC)
  Unencumbrd VarChar(1) Unencumbered default=N [Y=Yes, N=No]
  TaxOnRI VarChar(1) Tax On Reserve Invoice default=N [Y=Yes, N=No]
  RvsChrgPrc Num(19,6) Reverse Charge %
  RvsChrgTax Num(19,6) Reverse Charge Tax Amount
  RvsChrgSC Num(19,6) Reverse Charge Tax Amount (SC)
  RvsChrgFC Num(19,6) Reverse Charge Tax Amount (FC)
  InFirstIns VarChar(1) Included in First Installment default=N [Y=Yes, N=No]
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CESTrel VarChar(1) CEST Relevant default=N [Y=, N=]

# RPD5 - Goods Return - Withholding Tax Data
Module: Marketing Documents | 158 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  SECONDERY U: AbsEntry, WTCode, BaseAbsEnt, Doc1LineNo
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator ->ORPD
  WTCode nVarChar(4) WT Code ->OWHT
  Rate Num(19,6) Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntSC Num(19,6) Taxable Amount in SC
  TxblAmntFC Num(19,6) Taxable Amount in FC
  WTAmnt Num(19,6) WT Amount
  WTAmntSC Num(19,6) WT Amount (SC)
  WTAmntFC Num(19,6) WT Amount (FC)
  ApplAmnt Num(19,6) Applied WT Amount
  ApplAmntSC Num(19,6) Applied WTax Amount (SC)
  ApplAmntFC Num(19,6) Applied WTax Amount (FC)
  Category VarChar(1) Category [P=Payment, I=Invoice]
  Criteria VarChar(1) Criteria [Y=Accrual, N=Cash]
  Account nVarChar(15) G/L Account ->OACT
  Type VarChar(1) Withholding Type [V=VAT Withholding, I=Income Tax Withholding]
  RoundType VarChar(1) Rounding Type [T=Truncated, C=Commercial Values, N=No Rounding]
  BaseType VarChar(1) Base Type [G=Gross, N=Net, V=VAT, U=UoM]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseLine Int(11) Base Line
  BaseNum Int(11) Base Document Type default=-1 [-1=, 0=, 20=Purchase Delivery Notes]
  LineNum Int(11) Line Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Abs. Entry default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=21 ->ADP1
  Doc1LineNo Int(11) DOC1 Line Number default=-1
  WtLineType VarChar(1) WT Line Type default=D [D=Document Level WTax, L=Row Level WTax]
  TxblCurr nVarChar(3) Taxable Currency from Doc Line
  DtblCurr nVarChar(3) Deductible Currency
  DtblRate Num(19,6) Rate for Deductible Amount
  txblRate Num(19,6) Rate for Taxable Amount
  DtblAmount Num(19,6) Deductible Amount
  TdsAcc nVarChar(15) TDS Account ->OACT
  SurAcc nVarChar(15) Surcharge Account ->OACT
  CessAcc nVarChar(15) Cess Account ->OACT
  HscAcc nVarChar(15) HSC Account ->OACT
  TdsRate Num(19,6) TDS Rate
  SurRate Num(19,6) Surcharge Rate
  CessRate Num(19,6) Cess Rate
  HscRate Num(19,6) HSC Rate
  TdsBAmt Num(19,6) TDS Base Amount
  TdsBAmtSC Num(19,6) TDS Base Amount (SC)
  TdsBAmtFC Num(19,6) TDS Base Amount (FC)
  SurBAmt Num(19,6) Surcharge Base Amount
  SurBAmtSC Num(19,6) Surcharge Base Amount (SC)
  SurBAmtFC Num(19,6) Surcharge Base Amount (FC)
  CessBAmt Num(19,6) Cess Base Amount
  CessBAmtSC Num(19,6) Cess Base Amount (SC)
  CessBAmtFC Num(19,6) Cess Base Amount (FC)
  HscBAmt Num(19,6) HSC Base Amount
  HscBAmtSC Num(19,6) HSC Base Amount (SC)
  HscBAmtFC Num(19,6) HSC Base Amount (FC)
  TdsAmnt Num(19,6) TDS Tax Amount
  TdsAmntSC Num(19,6) TDS Tax Amount (SC)
  TdsAmntFC Num(19,6) TDS Tax Amount (FC)
  SurAmnt Num(19,6) Surcharge Tax Amount
  SurAmntSC Num(19,6) Surcharge Tax Amount (SC)
  SurAmntFC Num(19,6) Surcharge Tax Amount (FC)
  CessAmnt Num(19,6) Cess Tax Amount
  CessAmntSC Num(19,6) Cess Tax Amount (SC)
  CessAmntFC Num(19,6) Cess Tax Amount (FC)
  HscAmnt Num(19,6) HSC Tax Amount
  HscAmntSC Num(19,6) HSC Tax Amount (SC)
  HscAmntFC Num(19,6) HSC Tax Amount (FC)
  TdsAppl Num(19,6) Applied TDS Amount
  TdsApplSC Num(19,6) Applied TDS Amount (SC)
  TdsApplFC Num(19,6) Applied TDS Amount (FC)
  SurAppl Num(19,6) Applied Surcharge Amount
  SurApplSC Num(19,6) Applied Surcharge Amount (SC)
  SurApplFC Num(19,6) Applied Surcharge Amount (FC)
  CessAppl Num(19,6) Applied Cess Amount
  CessApplSC Num(19,6) Applied Cess Amount (SC)
  CessApplFC Num(19,6) Applied Cess Amount (FC)
  HscAppl Num(19,6) Applied HSC Amount
  HscApplSC Num(19,6) Applied HSC Amount (SC)
  HscApplFC Num(19,6) Applied HSC Amount (FC)
  BatchNum Int(11) Journal Voucher No.
  InCSTCode nVarChar(2) CST Code Incoming
  OutCSTCode nVarChar(2) CST Code Outgoing
  DpmWTApl Num(19,6) DPM WT Applied Amount
  DpmWTAplSC Num(19,6) DPM WT Applied Amount (SC)
  DpmWTAplFC Num(19,6) DPM WT Applied Amount (FC)
  WTTypeId Int(11) WT Type Id ->OWTT
  LnBsAmt Num(19,6) BR Line WT Base Amount
  LnBsAmtSC Num(19,6) BR Line WT Base Amount(SC)
  LnBsAmtFC Num(19,6) BR Line WT Base Amount(FC)
  LnCmTAmt Num(19,6) BR Line Cumulated Taxable Amount
  LnCmTAmtSC Num(19,6) BR Line Cumulated Taxable Amount(SC)
  LnCmTAmtFC Num(19,6) BR Line Cumulated Taxable Amount(FC)
  TDSType VarChar(1) TDS Type [E=eTDS, D=GST TDS, C=GST TCS, S=SALES TCS]
  IgstAcc nVarChar(15) IGST Account ->OACT
  CgstAcc nVarChar(15) CGST Account ->OACT
  SgstAcc nVarChar(15) SGST Account ->OACT
  IgstAmnt Num(19,6) IGST Tax Amount
  IgstAmntSC Num(19,6) IGST Tax Amount (SC)
  IgstAmntFC Num(19,6) IGST Tax Amount (FC)
  CgstAmnt Num(19,6) CGST Tax Amount
  CgstAmntSC Num(19,6) CGST Tax Amount (SC)
  CgstAmntFC Num(19,6) CGST Tax Amount (FC)
  SgstAmnt Num(19,6) SGST Tax Amount
  SgstAmntSC Num(19,6) SGST Tax Amount (SC)
  SgstAmntFC Num(19,6) SGST Tax Amount (FC)
  IgstRate Num(19,6) IGST Rate
  CgstRate Num(19,6) CGST Rate
  SgstRate Num(19,6) SGST Rate
  IgstBAmt Num(19,6) IGST Base Amount
  IgstBAmtSC Num(19,6) IGST Base Amount (SC)
  IgstBAmtFC Num(19,6) IGST Base Amount (FC)
  CgstBAmt Num(19,6) CGST Base Amount
  CgstBAmtSC Num(19,6) CGST Base Amount (SC)
  CgstBAmtFC Num(19,6) CGST Base Amount (FC)
  SgstBAmt Num(19,6) SGST Base Amount
  SgstBAmtSC Num(19,6) SGST Base Amount (SC)
  SgstBAmtFC Num(19,6) SGST Base Amount (FC)
  IgstAppl Num(19,6) Applied IGST Amount
  IgstApplSC Num(19,6) Applied IGST Amount (SC)
  IgstApplFC Num(19,6) Applied IGST Amount (FC)
  CgstAppl Num(19,6) Applied CGST Amount
  CgstApplSC Num(19,6) Applied CGST Amount (SC)
  CgstApplFC Num(19,6) Applied CGST Amount (FC)
  SgstAppl Num(19,6) Applied SGST Amount
  SgstApplSC Num(19,6) Applied SGST Amount (SC)
  SgstApplFC Num(19,6) Applied SGST Amount (FC)
  UtgstAcc nVarChar(15) UTGST Account ->OACT
  CsgstAcc nVarChar(15) Cess GST Account ->OACT
  UtgstAmt Num(19,6) UTGST Tax Amount
  UtgstAmtSC Num(19,6) UTGST Tax Amount (SC)
  UtgstAmtFC Num(19,6) UTGST Tax Amount (FC)
  CsgstAmt Num(19,6) Cess GST Tax Amount
  CsgstAmtSC Num(19,6) Cess GST Tax Amount (SC)
  CsgstAmtFC Num(19,6) Cess GST Tax Amount (FC)
  UtgstRate Num(19,6) UTGST Rate
  CsgstRate Num(19,6) Cess GST Rate
  UtgstBAmt Num(19,6) UTGST Base Amount
  UtgstBAmtS Num(19,6) UTGST Base Amount (SC)
  UtgstBAmtF Num(19,6) UTGST Base Amount (FC)
  CsgstBAmt Num(19,6) Cess GST Base Amount
  CsgstBAmtS Num(19,6) Cess GST Base Amount (SC)
  CsgstBAmtF Num(19,6) Cess GST Base Amount (FC)
  UtgstAppl Num(19,6) Applied UTGST Amount
  UtgstApplS Num(19,6) Applied UTGST Amount (SC)
  UtgstApplF Num(19,6) Applied UTGST Amount (FC)
  CsgstAppl Num(19,6) Applied Cess GST Amount
  CsgstApplS Num(19,6) Applied Cess GST Amount (SC)
  CsgstApplF Num(19,6) Applied Cess GST Amount (FC)
  EncryptIV nVarChar(100) Encrypt IV
  TcsIntAcct nVarChar(15) TCS Interim Account ->OACT
  SurIntAcct nVarChar(15) Surcharge Interim Account ->OACT
  CesIntAcct nVarChar(15) Cess Interim Account ->OACT
  HscIntAcct nVarChar(15) HSC interim Account ->OACT
  LnIntAcct nVarChar(15) Interim Account for Tax ->OACT
  FixedAmnt Num(19,6) Fixed Amount
  FixedAmtSC Num(19,6) Fixed Amount (SC)
  FixedAmtFC Num(19,6) Fixed Amount (FC)
  BaseQty Num(19,6) Base Quantity

# RPD6 - Goods Return - Installments
Module: Marketing Documents | 65 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, InstlmntID
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPD
  InstlmntID Int(6) Installment ID default=1
  ObjType nVarChar(20) Object Type default=21 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DueDate Date(8) Due Date
  Status VarChar(1) Installment Status default=O [O=Open, C=Closed]
  DunnLevel Int(11) Dunning Level default=0
  InsTotal Num(19,6) Total Installment
  InsTotalFC Num(19,6) Total Installment (FC)
  InsTotalSy Num(19,6) Total Installment (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  VatSum Num(19,6) Total Tax
  VatSumFC Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  VatPaid Num(19,6) Tax Paid to Date
  VatPaidFC Num(19,6) Tax Paid (FC)
  VatPaidSys Num(19,6) Tax Paid (SC)
  TotalExpns Num(19,6) Total Freight Charges
  TotalExpFC Num(19,6) Total Freight Charges (FC)
  TotalExpSC Num(19,6) Total Freight Charges (SC)
  ExpAppl Num(19,6) Applied Freight Charges
  ExpApplFC Num(19,6) Applied Freight Charges (FC)
  ExpApplSC Num(19,6) Applied Freight Charges (SC)
  WTSum Num(19,6) WTax Amount
  WTSumFC Num(19,6) WTax Amount (FC)
  WTSumSC Num(19,6) WTax Amount (SC)
  WTApplied Num(19,6) Applied WTax
  WTAppliedF Num(19,6) Applied WTax (FC)
  WTAppliedS Num(19,6) Applied WTax (SC)
  TotalBlck Num(19,6) Total Reserved Amount
  TotalBlckF Num(19,6) Total Reserved Amount (FC)
  TotalBlckS Num(19,6) Total Reserved Amount (SC)
  VATBlck Num(19,6) Reserved Tax
  VATBlckFC Num(19,6) Reserved Tax (FC)
  VATBlckSC Num(19,6) Reserved Tax (SC)
  ExpnsBlck Num(19,6) Reserved Freight Charges
  ExpnsBlckF Num(19,6) Reserved Freight Charges (FC)
  ExpnsBlckS Num(19,6) Reserved Freight Charges (SC)
  WTBlocked Num(19,6) Reserved WTax Amount
  WTBlockedF Num(19,6) Reserved WTax Amount (FC)
  WTBlockedS Num(19,6) Reserved WTax Amount (SC)
  InstPrcnt Num(19,6) Installment %
  DunWizBlck VarChar(1) Wizard dunning block default=N [N=No, Y=Yes]
  DunDate Date(8) Last Dunning Date
  Paid Num(19,6) Paid
  PaidFrgn Num(19,6) Paid (FC)
  PaidSc Num(19,6) Paid (SC)
  reserved VarChar(1) Reserved default=N [N=No, Y=Yes]
  TaxOnExp Num(19,6) Tax on Expenses
  TaxOnExpFc Num(19,6) Tax on Expenses (FC)
  TaxOnExpSc Num(19,6) Tax on Expenses (SC)
  TaxOnExpAp Num(19,6) Applied Tax on Expenses
  TaxOnExApF Num(19,6) Applied Tax on Expenses (FC)
  TaxOnExApS Num(19,6) Applied Tax on Expenses (SC)
  TaxOnExBlo Num(19,6) Reserved Tax on Freight Amount
  TaxOnExBlF Num(19,6) Reserved Tax on Freight Amt FC
  TaxOnExBlS Num(19,6) Reserved Tax on Freight Amt SC
  LvlUpdDate Date(8) Dunning Level Update Date
  Ordered VarChar(1) Payment Ordered default=N [Y=Yes, N=No]
  PaidDpm Num(19,6) Paid by Down Payment
  PaidDpmFc Num(19,6) Paid by Down Payment (FC)
  PaidDpmSc Num(19,6) Paid by Down Payment (SC)
  EncryptIV nVarChar(100) Encrypt IV

# RPD7 - Goods Return - Delivery Packages
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPD
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type default=21 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV

# RPD8 - Goods Return - Items in Package
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum, ItemCode, UomEntry, NumPerMsr
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPD
  PackageNum Int(11) Package Number
  ItemCode nVarChar(50) Item Code ->OITM
  Quantity Num(19,6) Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=21 ->ADP1
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value default=0

# RPD9 - Goods Return - Drawn Dpm
Module: Marketing Documents | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPD
  LineNum Int(11) Row Number
  BaseAbs Int(11) Base Document Internal ID
  BaseLine Int(11) Base Document Row
  TargetBase VarChar(1) Target or Base Document default=B [B=Base, T=Target]
  ObjType nVarChar(20) Base Object Type
  DrawnSum Num(19,6) Net LC
  DrawnSumFc Num(19,6) Net FC
  DrawnSumSc Num(19,6) Net SC
  LogInstanc Int(11) Log Instance default=0
  ObjCode nVarChar(20) Object Type default=21 ->ADP1
  ApplDrawn Num(19,6) Applied Net LC
  ApplDrawnF Num(19,6) Applied Net FC
  ApplDrawnS Num(19,6) Applied Net SC
  BaseDocNum Int(11) Base Document Number
  BsDocDate Date(8) Base Posting Date
  BsDueDate Date(8) Base Due Date
  BsCardName nVarChar(100) Base BP Name
  BsComments nVarChar(254) Base Remarks
  Posted VarChar(1) Base Document Posted default=Y [Y=Yes, N=No]
  Vat Num(19,6) Tax LC
  VatFc Num(19,6) Tax FC
  VatSc Num(19,6) Tax SC
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  IsGross VarChar(1) Is Gross Line default=N [N=Net Line, Y=Gross Line]

# RRR1 - A/R Return Request - Rows
Module: Marketing Documents | 317 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  STATUS: LineStatus
  CURRENCY: Currency
  ACCOUNT: AcctCode
  BASE_ENTRY: BaseEntry, BaseType, BaseLine
  VIS_ORDER: DocEntry, VisOrder
  OWNER_CODE: OwnerCode
  ITM_WHS_OQ: ItemCode, WhsCode, OpenQty
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORRR
  LineNum Int(11) Row Number
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=, 14=A/R Credit Note, 16=A/R Returns]
  TrgetEntry Int(11) Target Document Internal ID
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 15=Delivery, 13=Invoice]
  BaseEntry Int(11) Base Document Internal ID
  BaseLine Int(11) Base Row
  LineStatus VarChar(1) Row Status default=O [O=Open, C=Closed]
  ItemCode nVarChar(50) Item No. ->OITM
  Dscription nVarChar(200) Item/Service Description
  Quantity Num(19,6) Quantity
  ShipDate Date(8) Row Delivery Date
  OpenQty Num(19,6) Remaining Open Quantity
  Price Num(19,6) Price after Discount
  Currency nVarChar(3) Price Currency ->OCRN
  Rate Num(19,6) Currency Rate
  DiscPrcnt Num(19,6) Discount % per Row
  LineTotal Num(19,6) Row Total
  TotalFrgn Num(19,6) Row Total (FC)
  OpenSum Num(19,6) Open Amount
  OpenSumFC Num(19,6) Open Amount (FC)
  VendorNum nVarChar(50) Vendor Catalog No.
  SerialNum nVarChar(17) Serial Number
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  SlpCode Int(11) Sales Employee Code default=-1 ->OSLP
  Commission Num(19,6) Commission Percentage
  TreeType VarChar(1) BOM Type default=N [N=Not a BOM, A=Assembly, S=Sales, I=Sales BOM Component, P=Production, T=Template]
  AcctCode nVarChar(15) Account Code ->OACT
  TaxStatus VarChar(1) Tax Definition [Y=Yes, N=No]
  GrossBuyPr Num(19,6) Gross Profit Base Price
  PriceBefDi Num(19,6) Unit Price
  DocDate Date(8) Posting Date
  Flags Int(11) Flags default=0
  OpenCreQty Num(19,6) Credit Memo Amount
  UseBaseUn VarChar(1) Inventory UoM default=N [Y=Yes, N=No]
  SubCatNum nVarChar(50) BP Catalog No. ->OSCN
  BaseCard nVarChar(15) Base BP Code ->OCRD
  TotalSumSy Num(19,6) Row Total (SC)
  OpenSumSys Num(19,6) Open Amount (SC)
  InvntSttus VarChar(1) Warehouse Status default=O [O=Open, C=Closed]
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  CodeBars nVarChar(254) Bar Code
  VatPrcnt Num(19,6) Tax Rate per Row
  VatGroup nVarChar(8) Tax Definition ->OVTG
  PriceAfVAT Num(19,6) Gross Price
  Height1 Num(19,6) Height 1
  Hght1Unit Int(6) Unit of Height 1
  Height2 Num(19,6) Height 2
  Hght2Unit Int(6) Unit of Height 2
  Width1 Num(19,6) Width 1
  Wdth1Unit Int(6) Unit of Width 1
  Width2 Num(19,6) Width 2
  Wdth2Unit Int(6) Unit of Width 2
  Length1 Num(19,6) Length 1
  Len1Unit Int(6) Unit of Length 1
  length2 Num(19,6) Length 2
  Len2Unit Int(6) Unit of Length 2
  Volume Num(19,6) Volume
  VolUnit Int(6) Vol. Unit
  Weight1 Num(19,6) Weight 1
  Wght1Unit Int(6) Unit of Weight 1
  Weight2 Num(19,6) Weight 2
  Wght2Unit Int(6) Unit of Weight 2
  Factor1 Num(19,6) Factor 1
  Factor2 Num(19,6) Factor 2
  Factor3 Num(19,6) Factor 3
  Factor4 Num(19,6) Factor 4
  PackQty Num(19,6) Packing Quantity
  UpdInvntry VarChar(1) Whse Update default=Y [Y=Yes, N=No]
  BaseDocNum Int(11) Base Document No.
  BaseAtCard nVarChar(100) Customer/Vendor Base Document
  SWW nVarChar(16) Additional Identifier
  VatSum Num(19,6) Total Tax
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  FinncPriod Int(11) Posting Period ->OFPR
  ObjType nVarChar(20) Object Type default=234000031 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BlockNum nVarChar(100) Block Number
  ImportLog nVarChar(20) Import Log
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAqcuistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  DistribSum Num(19,6) Distributed Amount
  DstrbSumFC Num(19,6) Distributed Amount (FC)
  DstrbSumSC Num(19,6) Distributed Amount (SC)
  GrssProfit Num(19,6) Row Gross Profit
  GrssProfSC Num(19,6) Row Gross Profit (SC)
  GrssProfFC Num(19,6) Row Gross Profit (FC)
  VisOrder Int(11) Visual Order
  INMPrice Num(19,6) Item's Last Sales Price (OINM)
  PoTrgNum Int(11) PO Target No.
  PoTrgEntry nVarChar(11) PO Target Internal ID
  DropShip VarChar(1) Drop-Ship default=N [Y=Yes, N=No]
  PoLineNum Int(11) PO Target Row No.
  Address nVarChar(254) Address
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type [Y=Regular Tax, N=No Tax, U=Use Tax]
  OrigItem nVarChar(50) Original Item ->OITM
  BackOrdr VarChar(1) Allow Backorder [Y=Yes, N=No]
  FreeTxt nVarChar(100) Free Text
  PickStatus VarChar(1) Pick Status default=N [Y=Picked, N=Not Picked, R=Released for Picking, P=Partially Picked]
  PickOty Num(19,6) Pick Quantity
  PickIdNo Int(11) Pick ID
  TrnsCode Int(6) Shipping Method default=-1 ->OSHP
  VatAppld Num(19,6) Applied Tax
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  BaseQty Num(19,6) Base Quantity
  BaseOpnQty Num(19,6) Base Open Quantity
  VatDscntPr Num(19,6) Tax Discount %
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  DeferrTax VarChar(1) Deferred Tax default=N [Y=Yes, N=No]
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatlF Num(19,6) Net Tax Amount (FC)
  LineVatS Num(19,6) Net Tax Amount (SC)
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value
  CEECFlag VarChar(1) Correction Invoice Was/Should Be default=S [W=Was, S=Should Be]
  ToStock Num(19,6) Corr. Invoice Amt to Inventory
  ToDiff Num(19,6) Corr. Invoice Amount to Diff.
  ExciseAmt Num(19,6) Excise Amount
  TaxPerUnit Num(19,6) Tax per Unit
  TotInclTax Num(19,6) Total Including Tax
  CountryOrg nVarChar(3) Country/Region of Origin
  StckDstSum Num(19,6) Stock Distribution Sum
  ReleasQtty Num(19,6) Released Quantity
  LineType VarChar(1) Row Type default=R [R=Regular]
  TranType VarChar(1) Transaction Type [C=Complete, R=Reject]
  Text Text(16) Text
  OwnerCode Int(11) Document Owner
  StockPrice Num(19,6) Item Cost
  ConsumeFCT VarChar(1) Consumer Sales Forecast [Y=Yes, N=No]
  LstByDsSum Num(19,6) Last Buy Distribute Sum
  StckINMPr Num(19,6) Stock Inm Price
  LstBINMPr Num(19,6) Last Buy Inventory Journal Pr.
  StckDstFc Num(19,6) Stock Distribution Sum (FC)
  StckDstSc Num(19,6) Stock Distribution Sum (SC)
  LstByDsFc Num(19,6) Last Buy Distribute Sum (FC)
  LstByDsSc Num(19,6) Last Buy Distribute Sum (SC)
  StockSum Num(19,6) Stock Sum
  StockSumFc Num(19,6) Stock Sum FC
  StockSumSc Num(19,6) Stock Sum SC
  StckSumApp Num(19,6) Stock Sum Applied
  StckAppFc Num(19,6) Stock Sum Applied FC
  StckAppSc Num(19,6) Stock Sum Applied SC
  ShipToCode nVarChar(50) Ship-to Code
  ShipToDesc nVarChar(254) Ship-to Description
  StckAppD Num(19,6) Stock Distrib. - Applied Sum
  StckAppDFC Num(19,6) Stock Dist. - Applied Sum (FC)
  StckAppDSC Num(19,6) Stock Dist. - Applied Sum (SC)
  BasePrice VarChar(1) Price for Total Calculation default=E [E=Exclude Tax, I=Include Tax]
  GTotal Num(19,6) Gross Total
  GTotalFC Num(19,6) Gross Total (FC)
  GTotalSC Num(19,6) Gross Total (SC)
  DistribExp VarChar(1) Distribute Freight Charges [Y=Yes, N=No]
  DescOW VarChar(1) Description overwritten default=N [Y=Yes, N=No]
  DetailsOW VarChar(1) Remarks overwritten default=N [Y=Yes, N=No]
  GrossBase Int(6) Base Method for Gross Profit
  VatWoDpm Num(19,6) Tax Before DPM Applied
  VatWoDpmFc Num(19,6) Tax Before DPM Applied (FC)
  VatWoDpmSc Num(19,6) Tax Before DPM Applied (SC)
  CFOPCode nVarChar(6) CFOP Code for Document ->OCFP
  CSTCode nVarChar(6) CST Code for ICMS
  Usage Int(11) Usage Code for Document ->OUSG
  TaxOnly VarChar(1) Tax Only [Y=Yes, N=No]
  WtCalced VarChar(1) Withholding Tax Calculated default=N [N=No, Y=Yes]
  QtyToShip Num(19,6) Quantity to Ship
  DelivrdQty Num(19,6) Delivered Quantity
  OrderedQty Num(19,6) Ordered Quantity
  CogsOcrCod nVarChar(8) COGS Distribution Rule Code ->OOCR
  CiOppLineN Int(11) Row Number of Associated Row default=-1
  CogsAcct nVarChar(15) COGS Account Code ->OACT
  ChgAsmBoMW VarChar(1) Change Whs for Asm BoM Child [Y=Yes, N=No]
  ActDelDate Date(8) Actual Delivery Date
  OcrCode2 nVarChar(8) Costing Code 2 ->OOCR
  OcrCode3 nVarChar(8) Costing Code 3 ->OOCR
  OcrCode4 nVarChar(8) Costing Code 4 ->OOCR
  OcrCode5 nVarChar(8) Costing Code 5 ->OOCR
  TaxDistSum Num(19,6) Tax Distributed Amount
  TaxDistSFC Num(19,6) Tax Distributed Amount (FC)
  TaxDistSSC Num(19,6) Tax Distributed Amount (SC)
  PostTax VarChar(1) Post Tax in Price to Stock default=Y [Y=Yes, N=No]
  Excisable VarChar(1) Excisable [Yes/No] [Y=Yes, N=No]
  AssblValue Num(19,6) Assessable Value
  RG23APart1 Int(11) RG23A Part1 Number
  RG23APart2 Int(11) RG23A Part2 Number
  RG23CPart1 Int(11) RG23C Part1 Number
  RG23CPart2 Int(11) RG23C Part2 Number
  CogsOcrCo2 nVarChar(8) COGS Distribution Rule Code2 ->OOCR
  CogsOcrCo3 nVarChar(8) COGS Distribution Rule Code3 ->OOCR
  CogsOcrCo4 nVarChar(8) COGS Distribution Rule Code4 ->OOCR
  CogsOcrCo5 nVarChar(8) COGS Distribution Rule Code5 ->OOCR
  LnExcised VarChar(1) Line Excised [O=Open, C=Closed, P=Copied to OEI]
  LocCode Int(11) Location Code ->OLCT
  StockValue Num(19,6) Total COGS Value
  GPTtlBasPr Num(19,6) Total Base Price for Profit
  unitMsr2 nVarChar(100) Pur/Sal UoM if BaseUnit
  NumPerMsr2 Num(19,6) Pur/Sal UoM Value if Base Unit
  SpecPrice VarChar(1) Price Source Type default=N [Y=Special Prices for Business Partner, N=Manual, W=Active Price List, Discount Groups, R=Active Price List, U=Inactive Price List, A=Blanket Agreement, P=Period and Volume Discounts, Q=Period and Volume Discounts, Discount Groups, V=Inactive Price List, Discount Groups, 9=Special Prices for Business Partner, !=Blanket Agreement, 0=Period and Volume Discounts, 1=Period and Volume Discounts, Discount Groups, 2=Active Price List, 7=Active Price List, Discount Groups, 5=Inactive Price List, 6=Inactive Price List, Discount Groups]
  CSTfIPI nVarChar(2) CST for IPI Code
  CSTfPIS nVarChar(2) CST for PIS Code
  CSTfCOFINS nVarChar(2) CST for COFINS Code
  ExLineNo nVarChar(10) ExLineNo
  isSrvCall VarChar(1) Created from Service Call default=N [Y=Yes, N=No]
  PQTReqQty Num(19,6) Pur Quotation: Required Qty
  PQTReqDate Date(8) Pur Quotation: Required Date
  PcDocType Int(11) Purchase Confirmation Doc Type default=-1 [-1=No Type, 22=Purchase Order, 540000006=Purchase Quotation]
  PcQuantity Num(19,6) Purchase Confirmation Quantity
  LinManClsd VarChar(1) Line Was Closed Manually default=N [Y=Yes, N=No, U=Unknown]
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  NoInvtryMv VarChar(1) Without Inventory Movement default=N [Y=Yes, N=No]
  ActBaseEnt Int(11) Actual Base Document Entry
  ActBaseLn Int(11) Actual Base Line Number
  ActBaseNum Int(11) Actual Base Document No.
  OpenRtnQty Num(19,6) Quantity Open for Return
  AgrNo Int(11) Agreement No. ->OOAT
  AgrLnNum Int(11) Agreement Row Number
  CredOrigin VarChar(1) Credit Origin ->OBSI
  Surpluses Num(19,6) Surpluses
  DefBreak Num(19,6) Defect and Breakup
  Shortages Num(19,6) Shortages
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  UomEntry2 Int(11) UoM Entry if Base Unit default=0 ->OUOM
  UomCode nVarChar(20) UoM Code
  UomCode2 nVarChar(20) UoM Code if Base Unit
  FromWhsCod nVarChar(8) From Warehouse Code ->OWHS
  NeedQty VarChar(1) Consider Quantity of Items default=N [Y=Yes, N=No]
  PartRetire VarChar(1) Partial Retirement default=N [Y=Yes, N=No]
  RetireQty Num(19,6) Retirement Quantity
  RetireAPC Num(19,6) Retirement APC
  RetirAPCFC Num(19,6) Retirement APC FC
  RetirAPCSC Num(19,6) Retirement APC SC
  InvQty Num(19,6) Quantity - Inventory UoM
  OpenInvQty Num(19,6) Open Quantity (Inventory UoM)
  EnSetCost VarChar(1) Enable Set Item Cost in Return default=N [Y=Yes, N=No]
  RetCost Num(19,6) Return Cost in A/R Return
  Incoterms Int(11) Incoterms default=0 ->ODCI
  TransMod Int(11) Transport Mode default=0 ->ODCI
  LineVendor nVarChar(15) Line Vendor Code ->OCRD
  DistribIS VarChar(1) Distribute Intrastat Freight default=N [Y=Yes, N=No]
  ISDistrb Num(19,6) Intrastat Distrib. Amount
  ISDistrbFC Num(19,6) Intrastat Distrib. Amount (FC)
  ISDistrbSC Num(19,6) Intrastat Distrib. Amount (SC)
  IsByPrdct VarChar(1) Item Is By-Product default=N [N=No, Y=Yes]
  ItemType Int(11) Item Type default=4 [4=Item]
  PriceEdit VarChar(1) Price Was Edited by User default=N [N=No, Y=Yes]
  PrntLnNum Int(11) Parent Line Number
  LinePoPrss VarChar(1) Line PO Process default=N [Y=Yes, N=No]
  FreeChrgBP VarChar(1) Free of Charge (BP) default=N [Y=Yes, N=No]
  TaxRelev VarChar(1) Tax Relevant Row default=Y [Y=Yes, N=No]
  LegalText nVarChar(254) Legal Text
  ThirdParty VarChar(1) Third Party default=N [Y=Yes, N=No]
  LicTradNum nVarChar(32) Federal Tax ID
  InvQtyOnly VarChar(1) Change Qty (Inv. UoM) Only default=N [Y=Yes, N=No]
  UnencReasn Int(11) Reason for Unencumbered ICMS
  ShipFromCo nVarChar(50) Ship-From Code
  ShipFromDe nVarChar(254) Ship-From Description
  FisrtBin nVarChar(228) First Bin Location
  AllocBinC nVarChar(11) Allocated Bin Location Count
  ExpType nVarChar(4) Expense Type ->OEXD
  ExpUUID nVarChar(50) Expense UUID
  ExpOpType VarChar(1) Expense Operation Type [P=Professional Services, R=Renting Assets, O=Others]
  DIOTNat nVarChar(3) DIOT Nationality
  MYFtype nVarChar(2) MYF type [S1=MYF Wholesale Sales, S2=Retail Sales, P1=MYF Wholesale Purchases, P3=Other Expense Transactions]
  GPBefDisc Num(19,6) Gross Price Before Discount
  ReturnRsn Int(6) Return Reason default=-1
  ReturnAct Int(6) Return Action default=-1
  StgSeqNum Int(11) Stage Sequence Number
  StgEntry Int(11) Stage Entry ->ORST
  StgDesc nVarChar(100) Stage Description
  ItmTaxType nVarChar(2) Item GST Tax Category [GR=GST Regular, GN=GST Nil Rated, GE=GST Exempt, NE=Excisable, NN=Non-GST Non-Excisable]
  SacEntry Int(11) SAC Entry ->OSAC
  NCMCode Int(11) NCM Code default=-1
  HsnEntry Int(11) HSN Entry
  OriBAbsEnt Int(11) Original Base Document Internal ID
  OriBLinNum Int(11) Original Base Document Line Number
  OriBDocTyp Int(11) Original Base Document Type
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No, U=Use]
  EncryptIV nVarChar(100) Encrypt IV
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  StdItemId Int(11) Standard Item Identification ->OUNCL
  CommClass Int(11) Commodity Classification ->OUNCL
  VatExEntry Int(11) VAT Exemption AbsEntry ->OVEB
  VatExLN Int(6) VAT Exemption LineNum
  NatOfTrans Int(11) Nature of Transaction ->ODCI
  ISDtCryImp nVarChar(3) Destination Country/Region for Import ->OCRY
  ISDtRgnImp Int(11) Destination Region for Import ->ODCI
  ISOrCryExp nVarChar(3) Country/Region of Origin for Export ->OCRY
  ISOrRgnExp Int(11) Region of Origin for Export ->ODCI
  NVECode nVarChar(6) NVE Code
  PoNum nVarChar(20) Customer's Purchase Order Number
  PoItmNum Int(11) Customer's Purchase Order Item Number
  IndEscala VarChar(1) Indicator for Relevant Scale default=N [Y=Yes, N=No]
  CESTCode Int(11) CEST Code ->OCEST
  CtrSealQty Num(19,6) Control Seal Quantity
  CNJPMan nVarChar(14) CNPJ of Manufacturer
  UFFiscBene nVarChar(10) UF Fiscal Benefit Code
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]
  LegalTIMD nVarChar(250) Legal Text from Item Master Data
  LegalTTCA nVarChar(250) Legal Text from Tax Code Attributes
  LegalTW nVarChar(250) Legal Text from Warehouse
  LegalTCD nVarChar(250) Legal Text from Tax Code Determination
  RevCharge VarChar(1) Reverse Charge default=N [Y=Yes, N=No]
  ListNum Int(6) Price List No. ->OPLN

# RRR10 - A/R Return Request - Row Structure
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SECONDERY U: DocEntry, AftLineNum, OrderNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORRR
  LineSeq Int(11) Row Sequence
  AftLineNum Int(11) After Row Number
  OrderNum Int(11) Order Number
  LineType VarChar(1) Row Type [T=Text, S=Subtotal]
  LineText Text(16) Row Text
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=234000031 ->ADP1

# RRR11 - A/R Return Request - Drawn Dpm Detail
Module: Marketing Documents | 70 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LineSeq
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORRR
  LineNum Int(11) Row Number
  LineSeq Int(11) Sequence Number
  BaseAbs Int(11) Base Document Internal ID default=-1 ->ODPI
  BaseType Int(11) Base Object Type default=203 [203=A/R Down Payment]
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  VatPrcnt Num(19,6) VAT Percent
  LineTotal Num(19,6) Net LC
  TotalFrgn Num(19,6) Net FC
  TotalSumSy Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFrgn Num(19,6) Tax FC
  VatSumSys Num(19,6) Tax SC
  ObjType nVarChar(20) Object Type default=234000031 ->ADP1
  LogInstanc Int(11) Log Instance
  IsAcq VarChar(1) Acquisition Tax Liable default=N [N=No, Y=Yes]
  IsAllDrawn VarChar(1) Remaining Amount Drawn default=N [Y=Yes, N=No]
  IsGross VarChar(1) Is Gross Line default=N [N=Net Line, Y=Gross Line]
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  ApplNet Num(19,6) Applied Net LC
  ApplNetFc Num(19,6) Applied Net FC
  ApplNetSc Num(19,6) Applied Net SC
  ApplVat Num(19,6) Applied Tax LC
  ApplVatFc Num(19,6) Applied Tax FC
  ApplVatSc Num(19,6) Applied Tax SC
  BaseNet Num(19,6) Base Net LC
  BaseNetFc Num(19,6) Base Net FC
  BaseNetSc Num(19,6) Base Net SC
  BaseVat Num(19,6) Base Tax LC
  BaseVatFc Num(19,6) Base Tax FC
  BaseVatSc Num(19,6) Base Tax SC
  BaseGross Num(19,6) Base Gross LC
  BaseGrossF Num(19,6) Base Gross FC
  BaseGrossS Num(19,6) Base Gross SC
  LineType VarChar(1) Line Type default=D [D=Document Row, R=Currency Rounding, H=Down Payment Document Rounding]
  DctSum Num(19,6) Deductible Sum LC
  DctSumFc Num(19,6) Deductible Sum FC
  DctSumSc Num(19,6) Deductible Sum SC
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplDct Num(19,6) Applied Deductible Sum LC
  ApplDctFc Num(19,6) Applied Deductible Sum FC
  ApplDctSc Num(19,6) Applied Deductible Sum SC
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  BaseDct Num(19,6) Base Deductible Sum LC
  BaseDctFc Num(19,6) Base Deductible Sum FC
  BaseDctSc Num(19,6) Base Deductible Sum SC
  BaseEq Num(19,6) Base Equalization Sum LC
  BaseEqFc Num(19,6) Base Equalization Sum FC
  BaseEqSc Num(19,6) Base Equalization Sum SC
  TaxCode nVarChar(8) Tax Code ->OSTC
  ApplGross Num(19,6) Applied Gross LC
  ApplGrossF Num(19,6) Applied Gross FC
  ApplGrossS Num(19,6) Applied Gross SC
  TaxAdjust VarChar(1) Manual Tax Adjustment default=N [Y=Yes, N=No]
  RvsChrgSum Num(19,6) Reverse Charge Sum LC
  RvsChrgFc Num(19,6) Reverse Charge Sum FC
  RvsChrgSc Num(19,6) Reverse Charge Sum SC
  BasRvsChrg Num(19,6) Base Reverse Charge LC
  BasRvsFc Num(19,6) Base Reverse Charge FC
  BasRvsSc Num(19,6) Base Reverse Charge SC
  ApplRvs Num(19,6) Applied Reverse Charge LC
  ApplRvsFc Num(19,6) Applied Reverse Charge FC
  ApplRvsSc Num(19,6) Applied Reverse Charge SC
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# RRR12 - A/R Return Request - Tax Extension
Module: Marketing Documents | 117 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORRR
  TaxId0 nVarChar(100) Tax ID 0
  TaxId1 nVarChar(100) Tax ID 1
  TaxId2 nVarChar(100) Tax ID 2
  TaxId3 nVarChar(100) Tax ID 3
  TaxId4 nVarChar(100) Tax ID 4
  TaxId5 nVarChar(100) Tax ID 5
  TaxId6 nVarChar(100) Tax ID 6
  TaxId7 nVarChar(100) Tax ID 7
  TaxId8 nVarChar(100) Tax ID 8
  TaxId9 nVarChar(100) Tax ID 9
  State nVarChar(3) State Code
  County nVarChar(7) County Code
  Incoterms nVarChar(3) Incoterms
  Vehicle nVarChar(10) Vehicle ID
  VidState nVarChar(3) Vehicle ID (State)
  NfRef nVarChar(254) NF Reference
  Carrier nVarChar(15) Carrier Code ->OCRD
  QoP Int(11) Quantity of Packs
  PackDesc nVarChar(10) Pack Description
  Brand nVarChar(20) Brand
  NoSU Int(11) Number of Shipping Unit
  NetWeight Num(19,6) Net Weight
  GrsWeight Num(19,6) Gross Weight
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=234000031 ->ADP1
  TaxId10 nVarChar(100) Tax ID 10
  TransCat nVarChar(100) Transaction Category
  FormNo nVarChar(100) Form No.
  TaxId11 nVarChar(100) Tax ID 11
  StreetS nVarChar(100) Street
  BlockS nVarChar(100) Block
  BuildingS Text(16) Building/Floor/Room
  CityS nVarChar(100) City
  ZipCodeS nVarChar(20) Zip Code
  CountyS nVarChar(100) County
  StateS nVarChar(3) State ->OCST
  CountryS nVarChar(3) Country/Region ->OCRY
  AddrTypeS nVarChar(100) Address Type
  StreetNoS nVarChar(100) Street No.
  StreetB nVarChar(100) Street
  BlockB nVarChar(100) Block
  BuildingB Text(16) Building/Floor/Room
  CityB nVarChar(100) City
  ZipCodeB nVarChar(20) Zip Code
  CountyB nVarChar(100) County
  StateB nVarChar(3) State ->OCST
  CountryB nVarChar(3) Country/Region ->OCRY
  AddrTypeB nVarChar(100) Address Type
  StreetNoB nVarChar(100) Street No.
  ImpORExp VarChar(1) Import or Export [N=, Y=]
  Vat VarChar(1) VAT default=N [N=No VAT Support, Y=VAT Support]
  AltCrdNamB nVarChar(100) Alternative BP Name
  AltTaxIdB nVarChar(32) Alternative Tax ID
  Address2S nVarChar(50) Address Name 2
  Address3S nVarChar(50) Address Name 3
  Address2B nVarChar(50) Address Name 2
  Address3B nVarChar(50) Address Name 3
  MainUsage Int(11) Main Usage Code of Document ->OUSG
  GlbLocNumS nVarChar(50) Global Location Number
  GlbLocNumB nVarChar(50) Global Location Number
  CollectDT nVarChar(20) Date and Time of Collection
  TransprtDT Date(8) Transport Starting Date
  TransprtRS nVarChar(100) Transport Reason
  TaxId12 nVarChar(50) Tax ID 12
  TaxId13 nVarChar(100) Deductee Ref. No. in India
  ImpExpNo nVarChar(100) Import/Export Bill No.
  ImpExpDate Date(8) Import/Export Date
  BpGSTType Int(11) GST Regn Type of BP
  BpGSTN nVarChar(15) GST Regn No of BP
  BpStateCod nVarChar(3) State Code of Business Partner ->OCST
  BPStatGSTN nVarChar(2) GST State Code of BP
  LocGSTType Int(11) GST Regn Type of Location
  LocGSTN nVarChar(15) GST Regn No of Location
  LocStatCod nVarChar(3) State Code of Location ->OCST
  LocStaGSTN nVarChar(2) GST State Code of Location
  BpCountry nVarChar(3) Country/Region Code of BP ->OCRY
  OrigImpNo nVarChar(100) Original Bill of Entry No.
  OrigImpDat Date(8) Original Bill of Entry Date
  ExportType VarChar(1) Exporting Type default=E [E=Imports/Exports, S=SEZ Developer, U=SEZ Unit, D=Deemed Imports/Exports]
  PortCode nVarChar(100) Port Code
  BoEValue Num(19,6) Bill of Entry Value
  IsIGSTAct VarChar(1) Supply under IGST Account [Y=Yes, N=No]
  ClaimRefun VarChar(1) Claim Refund [Y=Yes, N=No]
  TaxRateDif Int(11) Differential % of Tax Rate [65=, 100=]
  BPGdsIssP nVarChar(15) Goods Issue Place BP
  CNPJGIP nVarChar(100) Goods Issue Place CNPJ
  CPFGIP nVarChar(100) Goods Issue Place CPF
  StreetGIP nVarChar(100) Goods Issue Place Street
  StrtNoGIP nVarChar(100) Goods Issue Place Street No.
  BldngGIP Text(16) Goods Issue Place Building
  ZipGIP nVarChar(20) Goods Issue Place Zip Code
  BlockGIP nVarChar(100) Goods Issue Place Block
  CityGIP nVarChar(100) Goods Issue Place City
  CountyGIP nVarChar(100) Goods Issue Place County
  StateGIP nVarChar(3) Goods Issue Place State ->OCST
  CountryGIP nVarChar(3) Goods Issue Place Country/Region ->OCRY
  PhoneGIP nVarChar(20) Goods Issue Place Phone
  EMailGIP nVarChar(100) Goods Issue Place E-Mail
  DptDateGIP Date(8) Goods Issue Place Departure Date
  BPDelivryP nVarChar(15) Delivery Place BP
  CNPJDlvryP nVarChar(100) Delivery Place CNPJ
  CPFDlvryP nVarChar(100) Delivery Place CPF
  StrtDlvryP nVarChar(100) Delivery Place Street
  StrNoDlvrP nVarChar(100) Delivery Place Street No.
  BldDlvryP Text(16) Delivery Place Building
  ZipDlvryP nVarChar(20) Delivery Place Zip Code
  BlckDlvryP nVarChar(100) Delivery Place Block
  CityDlvryP nVarChar(100) Delivery Place City
  CntyDlvryP nVarChar(100) Delivery Place County
  StatDlvryP nVarChar(3) Delivery Place State ->OCST
  CtryDlvryP nVarChar(3) Delivery Place Country/Region ->OCRY
  FoneDlvryP nVarChar(20) Delivery Place Phone
  MailDlvryP nVarChar(100) Delivery Place E-Mail
  DpDtDlvryP Date(8) Delivery Place Departure Date
  AuthedCNPJ nVarChar(250) Authorized CNPJ or CPF
  TaxId14 nVarChar(250) ITR Filing

# RRR13 - A/R Return Request - Distributed Freights
Module: Marketing Documents | 59 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORRR
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=234000031 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Aquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Normal Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) VAT Applied Frgn
  VatAppldSC Num(19,6) VAT Applied Sys
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock default=N [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Line No.
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Abs. Entry default=-1
  BaseGroup Int(11) Base Document Group default=-1
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1
  VisOrder Int(11) Visual Order
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DistribExp VarChar(1) Distribute Freights [Y=Yes, N=No]
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ

# RRR14 - A/R Return Request - Assembly - Rows
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORRR
  LineNum Int(11) Row Number default=-1
  ChildNum Int(11) Child Number default=-1
  ItemCode nVarChar(50) Item no. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  TotalQty Num(19,6) Total Quantity
  OpenQty Num(19,6) Remaining Open Quantity
  ObjectType nVarChar(20) object type default=234000031 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BaseChildN Int(11) Base Child Number default=-1
  EncryptIV nVarChar(100) Encrypt IV

# RRR15 - A/R Return Request - Drawn Dpm Applied
Module: Marketing Documents | 84 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORRR
  LineNum Int(11) Row Number
  ObjType nVarChar(20) object type default=234000031 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  StaCode nVarChar(8) Tax Authority Code
  StaType Int(11) Tax Authority Type
  StaIndex Int(11) Tax Authority Seq Index
  BaseNet Num(19,6) Net LC
  BaseNetFc Num(19,6) Net FC
  BaseNetSc Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFc Num(19,6) Tax FC
  VatSumSc Num(19,6) Tax SC
  DctSum Num(19,6) Deductible Sum LC
  DctSumFc Num(19,6) Deductible Sum FC
  DctSumSc Num(19,6) Deductible Sum SC
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplNet Num(19,6) Applied Net LC
  ApplNetFc Num(19,6) Applied Net FC
  ApplNetSc Num(19,6) Applied Net SC
  ApplVat Num(19,6) Applied Tax LC
  ApplVatFc Num(19,6) Applied Tax FC
  ApplVatSc Num(19,6) Applied Tax SC
  ApplDct Num(19,6) Applied Deductible Sum LC
  ApplDctFc Num(19,6) Applied Deductible Sum FC
  ApplDctSc Num(19,6) Applied Deductible Sum SC
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  PaidNet Num(19,6) Paid Net LC
  PaidNetFc Num(19,6) Paid Net FC
  PaidNetSc Num(19,6) Paid Net SC
  PaidVat Num(19,6) Paid Tax LC
  PaidVatFc Num(19,6) Paid Tax FC
  PaidVatSc Num(19,6) Paid Tax SC
  PaidDct Num(19,6) Paid Deductible Sum LC
  PaidDctFc Num(19,6) Paid Deductible Sum FC
  PaidDctSc Num(19,6) Paid Deductible Sum SC
  PaidEq Num(19,6) Paid Equalization Sum LC
  PaidEqFc Num(19,6) Paid Equalization Sum FC
  PaidEqSc Num(19,6) Paid Equalization Sum SC
  DpApplNet Num(19,6) Dpm Appl Net LC
  DpApplNetF Num(19,6) Dpm Appl Net FC
  DpApplNetS Num(19,6) Dpm Appl Net SC
  DpApplVat Num(19,6) Dpm Appl Tax LC
  DpApplVatF Num(19,6) Dpm Appl Tax FC
  DpApplVatS Num(19,6) Dpm Appl Tax SC
  DpApplDct Num(19,6) Dpm Appl Deductible Sum LC
  DpApplDctF Num(19,6) Dpm Appl Deductible Sum FC
  DpApplDctS Num(19,6) Dpm Appl Deductible Sum SC
  DpApplEq Num(19,6) Dpm Appl Equalization Sum LC
  DpApplEqFc Num(19,6) Dpm Appl Equalization Sum FC
  DpApplEqSc Num(19,6) Dpm Appl Equalization Sum SC
  TaxCode nVarChar(8) Tax Code ->OSTC
  LineType VarChar(1) Row Type default=D [D=Document, R=Exchange Rate Rounding, H=Document Header Rounding]
  BaseGrs Num(19,6) Gross LC
  BaseGrsFc Num(19,6) Gross FC
  BaseGrsSc Num(19,6) Gross SC
  ApplGrs Num(19,6) Applied Gross LC
  ApplGrsFc Num(19,6) Applied Gross FC
  ApplGrsSc Num(19,6) Applied Gross SC
  PaidGrs Num(19,6) Paid Gross LC
  PaidGrsFc Num(19,6) Paid Gross FC
  PaidGrsSc Num(19,6) Paid Gross SC
  DpApplGrs Num(19,6) Dpm Appl Gross LC
  DpApplGrsF Num(19,6) Dpm Appl Gross FC
  DpApplGrsS Num(19,6) Dpm Appl Gross SC
  RvsChrgSum Num(19,6) Reverse Charge Sum
  RvsChrgSc Num(19,6) Reverse Charge Sum (SC)
  RvsChrgFc Num(19,6) Reverse Charge Sum (FC)
  ApplRvs Num(19,6) Applied Reverse Charge Sum LC
  ApplRvsSc Num(19,6) Applied Reverse Charge Sum SC
  ApplRvsFc Num(19,6) Applied Reverse Charge Sum FC
  PaidRvs Num(19,6) Paid Reverse Charge Sum LC
  PaidRvsSc Num(19,6) Paid Reverse Charge Sum SC
  PaidRvsFc Num(19,6) Paid Reverse Charge Sum FC
  DpApplRvs Num(19,6) Dpm Applied Reverse Charge LC
  DpApplRvsS Num(19,6) Dpm Applied Reverse Charge SC
  DpApplRvsF Num(19,6) Dpm Applied Reverse Charge FC
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# RRR16 - A/R Return Request - SnB properties
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, SnBIndex
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) abs entry ->ORRR
  LineNum Int(11) Line Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object id
  ObjAbs Int(11) Object Abs
  DrfWObjAbs Int(11) draft Wobj Abs default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type default=234000031
  LogInstanc Int(11) Log Instance

# RRR17 - A/R Return Request - Import Process
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORRR
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=234000031 ->ADP1
  ImpDocType VarChar(1) Type of Importation Document ->OBSI
  ImpDocNum nVarChar(10) Importation Document Number
  DateOfReg Date(8) Date of Registry DI/DSI/DA
  CustClrDat Date(8) Date of Customs Clearance
  ConcActNum nVarChar(30) Drawback Concession Acct No.
  AdditNum nVarChar(30) Additional Number
  AddItmDV Num(19,6) Additional Item Discount Value
  tpVTransp Int(6) Overland Transport Route [1=Maritime, 2=Waterway, 3=Lakeside, 4=Air, 5=Post, 6=Train, 7=Road, 8=Network Transmission, 9=Own Means, 10=Input/Output Fictitious, 11=Courier, 12=Hand Carry]
  DrawSReg nVarChar(11) Drawback - Suspension Regime
  AddFrNavyA Num(19,6) Additional Freight to Navy Authority
  TypeOfImp VarChar(1) Type of Import
  nSeqAdic Int(6) Additional Item Sequential Number

# RRR18 - A/R Return Request - Export Process
Module: Marketing Documents | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORRR
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=234000031 ->ADP1
  ExpDocType Int(11) Type of Exportation Document default=-1 ->OBNI
  ExpDeclNum Int(11) Exportation Declaration Number
  ExpDeclDat Date(8) Exportation Declaration Date
  ExpNature Int(11) Nature of Exportation default=-1 ->OBNI
  ExpRegNum Int(11) Number of Exportation Registry
  ExpRegDate Date(8) Date of Exportation Registry
  LadBillNum nVarChar(19) Bill of Lading Number
  LadBillDat Date(8) Date of Bill of Lading
  MerchLeftD Date(8) Date Merchandise Left Customs
  LadBillTyp Int(11) Type of Bill of Lading default=-1 ->OBNI
  DrawSReg nVarChar(11) Drawback - Suspension Regime
  NatureExp nVarChar(44) Nature of Export
  QultExpItm Num(19,6) Quantity of Exported Items
  nSeqAdic Int(6) Additional Item Sequential Number

# RRR19 - A/R Return Request - Bin Allocation Data
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, BinAllocSe
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->ORRR
  BinAllocSe Int(11) Bin Allocation Sequence
  LineNum Int(11) Line Number
  SubLineNum Int(11) Subline Number default=-1
  SnBType Int(11) SnB Type default=-1
  SnBMDAbs Int(11) SnB Master Data Internal No. default=-1
  BinAbs Int(11) Bin Internal Number ->OBIN
  Quantity Num(19,6) Quantity
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjType nVarChar(20) Object Type default=234000031 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  BinActTyp Int(6) Bin Action Type [1=Transaction In, 2=Transaction Out, 4=SnB Complete, 8=Bin First Then SnB]

# RRR2 - A/R Return Request - Freight - Rows
Module: Marketing Documents | 64 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORRR
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=A/R Return Request ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) Vat Applied
  VatAppldFC Num(19,6) Vat Applied Frgn
  VatAppldSC Num(19,6) Vat Applied Sys
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report [Y=Yes, N=No]
  BaseGroup Int(11) Base Document Group default=-1 [-1=, 0=, 1=, 2=]
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1 [-1=, 0=, 1=, 2=]
  VisOrder Int(11) Visual Order
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]

# RRR20 - Intrastat Expenses
Module: Marketing Documents | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORRR
  ExpnsCode Int(11) Freight Code ->OEXD
  TotalLC Num(19,6) Total
  TotalFC Num(19,6) Total (FC)
  TotalSC Num(19,6) Total (SC)
  DistribM VarChar(1) Distribution Method default=T [Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DrawnLC Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  LineNum Int(11) Line Number default=-1
  BaseAbsEnt Int(11) Base Abs. Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 16=Return, 13=A/R Invoice, 203=Down Payment Incoming, 204=Down Payment Outgoing, 22=Purchase Order, 20=Goods Receipt PO, 21=Goods Return, 18=A/P Invoice, 540000006=Purchase Quotation, 0=, -1=]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No. default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=234000031 ->ADP1
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  AppliedLC Num(19,6) Applied
  AppliedFC Num(19,6) Applied (FC)
  AppliedSC Num(19,6) Applied (SC)

# RRR21 - A/R Return Request - Document Reference Information
Module: Marketing Documents | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, RefType
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjectType nVarChar(20) Object Type default=234000031
  LogInstanc Int(11) Log Instance default=0
  RefType VarChar(1) Reference Types default=S [S=System Document, E=External Document]
  LineNum Int(11) Line Number
  RefDocEntr Int(11) Referenced Internal Number
  RefDocNum Int(11) Referenced Document Number
  ExtDocNum nVarChar(100) External Referenced Document Number
  RefObjType nVarChar(20) Referenced Object Type [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 234000031=Return Request, 16=Return, 203=A/R Down Payment, 13=A/R Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 280=A/R Tax Invoice, 1470000113=Purchase Request, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Return Request, 21=Goods Return, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 281=A/P Tax Invoice, 69=Landed Costs, 24=Incoming Payments, 46=Outgoing Payments, 57=Checks for Payment, 321=Internal Reconciliation, 34=Recurring Posting, 30=Journal Entry, 59=Goods Receipt, 60=Goods Issue, 162=Inventory Revaluation, 1470000065=Inventory Counting, 10000071=Inventory Posting, 1250000001=Inventory Transfer Request, 67=Inventory Transfer, 202=Production Order, 13001=Original Invoice, -1=External Document, 20301=Original Down Payment Invoice]
  AccessKey nVarChar(100) Access Key
  IssueDate Date(8) Date of Issue
  IssuerCNPJ nVarChar(100) Issuer CNPJ
  IssuerCode nVarChar(10) Fiscal Document Issuer UF Code
  Model nVarChar(6) Fiscal Document Model
  Series nVarChar(3) Fiscal Document Series
  Number Int(11) Fiscal Document Number
  RefAccKey nVarChar(100) Referenced CT-e Access Key
  RefAmount Num(19,6) Referenced Amount
  SubSeries nVarChar(3) Fiscal Document Subseries
  Remark nVarChar(254) Remarks
  LinkRefTyp nVarChar(20) Link Reference Type default=00 [00=, 01=Nota de cr�dito de los documentos relacionados, 02=Nota de d�bito de los documentos relacionados, 03=Devoluci�n de mercanc�a sobre facturas o traslados previos, 04=Sustituci�n de los CFDI previos, 05=Traslados de mercancias facturados previamente, 06=Factura generada por los traslados previos, 07=CFDI por aplicaci�n de anticipo, 08=Customs, MX_08=Factura generada por pagos en parcialidades, 09=Factura generada por pagos diferidos]

# RRR22 - A/R Return Request - Resource Costs
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, StdCostNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->RRR1
  LineNum Int(11) Row Number
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=234000031
  LogInstanc Int(11) Log Instance default=0

# RRR23 - A/R Return Request - Selected Asset Master Data
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, VisOrder
  ASSETS: DocEntry, LineNum, AssetCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORRR
  LineNum Int(11) Row Number
  AssetCode nVarChar(50) Selected Asset Code ->OITM
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Remarks nVarChar(100) Remarks
  Amount Num(19,6) Amount
  AmountSC Num(19,6) Amount (SC)
  SerialNo nVarChar(30) Serial Number
  VisOrder Int(11) Visual Order
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=234000031 ->ADP1

# RRR24 - Return Request - Tracking Note Assignment
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  ItemCCDNum nVarChar(40) Item CCD Number
  CntrOrigin nVarChar(3) Country/Region of Origin
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=234000031 ->ADP1
  SubLineNum Int(11) BOM Line No.

# RRR25 - Return Request - Amt Per VAT Grp
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, VatGroup, Type
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  VatGroup nVarChar(8) Tax Definition ->OVTG
  VatPrcnt Num(19,6) Tax Rate
  BaseAmnt Num(19,6) Base Amount
  BaseAmntFC Num(19,6) Base Amount (FC)
  BaseAmntSC Num(19,6) Base Amount (SC)
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  Type Int(11) Type default=1 [1=Discount by Tax]
  Currency nVarChar(3) Price Currency
  Rate Num(19,6) Currency Rate
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=234000031 ->ADP1

# RRR26 - A/R Return Request - E-Way Bill Information
Module: Marketing Documents | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORRR
  SuplyType nVarChar(20) EWB Transaction Type [O=Outward, I=Inward]
  SubSplyTyp Int(11) EWB Sub-Type ->OEST
  DocType nVarChar(3) EWB Doc. Type ->OEDT
  TransMode Int(11) EWB Transportation Mode ->OETM
  Distance Num(19,6) EWB Transport Distance
  TransDocNo nVarChar(16) EWB Transporter Doc. No.
  TransDate Date(8) EWB Transportation Date
  VehicleTyp nVarChar(2) EWB Vehicle Type ->OEVT
  VehicleNo nVarChar(15) EWB Vehicle Number
  EWayBillNo nVarChar(20) EWB No.
  EwbDate Date(8) E-Way Bill Date
  FrmTraName nVarChar(100) EWB Consignor Name
  FrmAddres1 nVarChar(120) EWB Consignor Address 1
  FrmAddres2 nVarChar(120) EWB Consignor Address 2
  FrmZipCode nVarChar(20) EWB Consignor Zip Code
  ActFrmStat nVarChar(2) Dispatch State of EWB Consignor
  ToTraName nVarChar(100) EWB Consignee Name
  ToAddres1 nVarChar(120) EWB Consignee Address 1
  ToAddres2 nVarChar(120) EWB Consignee Address 2
  ToZipCode nVarChar(20) EWB Consignee Zip Code
  ActToState nVarChar(2) Ship-To State of EWB Consignee
  FrmGSTN nVarChar(15) EWB Consignor GSTN
  FrmState nVarChar(2) Bill-To State of EWB Consignor
  ToGSTN nVarChar(15) EWB Consignee GSTN
  ToState nVarChar(2) Bill-To State of EWB Consignee
  MainHsnEnt Int(11) EWB Main HSN Entry ->OCHP
  FrmPlace nVarChar(50) EWB Consignor Place
  ToPlace nVarChar(50) EWB Consignee Place
  TransID nVarChar(15) EWB Transporter ID
  TransName nVarChar(25) EWB Transporter Name
  ExpireDate Date(8) EWB Expiration Date
  ObjectType nVarChar(20) Object Type default=234000031 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TspEntry Int(11) Transporter Abs. Entry ->OTSP
  TspLine Int(11) Transportation Line
  TransType Int(11) Transaction Type [1=Regular, 2=Bill To-Ship To, 3=Bill From-Dispatch From, 4=Combination of 2 and 3]

# RRR27 - A/R Return Request - E-Books(GR) Rows
Module: Marketing Documents | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  RELATE_ROW: DocEntry, RelateType, RelateLine, GroupNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORRR
  LineNum Int(11) Row Number
  RelateType Int(11) Relation Type default=-1 [1=Row, 2=Row Expenses, 3=Document Expenses, 13=Distributed Freights, -1=Manual]
  RelateLine Int(11) Relation Row Number default=-1
  GroupNum Int(11) Group Number default=-1
  LineTotal Num(19,6) Line Total
  LineTotalF Num(19,6) Line Total (FC)
  LineTotalS Num(19,6) Line Total (SC)
  InClassTyp Int(11) Income Classification Type ->OICP
  InClassCat Int(11) Income Classification Category ->OICC
  ExClassTyp Int(11) Expense Classification Type ->OECP
  ExClassCat Int(11) Expense Classification Cat. ->OECC
  VatCate Int(11) VAT Category
  NetValue Num(19,6) Net Value
  NetValueFC Num(19,6) Net Value (FC)
  NetValueSC Num(19,6) Net Value (SC)
  VatAmount Num(19,6) VAT Amount
  VatAmFC Num(19,6) VAT Amount (FC)
  VatAmSC Num(19,6) VAT Amount (SC)
  WtPercCat Int(11) Withheld Percentage Category
  WtAmount Num(19,6) Withheld Amount
  WtAmountFC Num(19,6) Withheld Amount (FC)
  WtAmountSC Num(19,6) Withheld Amount (SC)
  ObjectType nVarChar(20) Object Type default=13 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  WtCategory VarChar(1) Withheld Category [I=Invoice, P=Payment]
  VATClassTy Int(11) VAT Classification Type ->OECP
  VATClassCa Int(11) VAT Classification Category ->OECC
  EBVatExCau Int(11) VAT Exemption Cause ->OVEC

# RRR28 - Return Request - Reported Tracking Note
Module: Marketing Documents | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
  TCN_KEY U: DocEntry, LineNum, TrackingNt, TrackiNtLn
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  UnusedQty Num(19,6) Unused Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=234000031 ->ADP1
  SubLineNum Int(11) BOM Line No.

# RRR3 - A/R Return Request - Freight
Module: Marketing Documents | 80 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  DOCUMENT: DocEntry, BaseAbsEnt
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORRR
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  Comments nVarChar(100) Remarks
  ObjType nVarChar(20) Object Type default=234000031 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  WTLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  VatApplied Num(19,6) Vat Applied
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatF Num(19,6) Net Tax Amount (FC)
  LineVatS Num(19,6) Net Tax Amount (SC)
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 15=Delivery, 13=Invoice]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No.
  LineNum Int(11) line num default=-1
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Doc. Internal No. default=-1
  StDstr Num(19,6) Stock Distributed Sum
  StDstrSC Num(19,6) Stock Distributed Sum (SC)
  StDstrFC Num(19,6) Stock Distributed Sum (FC)
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  TaxDistMtd VarChar(1) Tax Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  GrsAmount Num(19,6) Gross Amount
  GrsFC Num(19,6) Gross Amount (FC)
  GrsSC Num(19,6) Gross Amount (SC)
  BaseTotal VarChar(1) Base Total for Calculation default=N [N=Net Total, G=Gross Total]
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)
  RRVatLC Num(19,6) Return Request VAT Amount
  RRVatFC Num(19,6) Return Request VAT Amount (FC)
  RRVatSC Num(19,6) Return Request VAT Amount (SC)
  EncryptIV nVarChar(100) Encrypt IV
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]

# RRR4 - A/R Return Request - Tax Amount per Document
Module: Marketing Documents | 61 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SCONDARY: DocEntry, LineNum, GroupNum, ExpnsCode, StcCode, StaCode, staType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORRR
  LineNum Int(11) Row Number default=-1
  GroupNum Int(11) Group Number default=-1
  ExpnsCode Int(11) Expense Code default=-1 ->OEXD
  RelateType Int(11) Relation Type default=1 [1=Row, 2=Row Expenses, 3=Document Expenses, 13=Distributed Freights]
  StcCode nVarChar(8) Tax Code ->OSTC
  StaCode nVarChar(8) Authority Code ->OSTA
  staType Int(11) Authority Type ->OSTT
  TaxRate Num(19,6) Tax Rate
  TaxAcct nVarChar(15) Tax Account ->OACT
  TaxSum Num(19,6) Tax Amount
  TaxSumFrgn Num(19,6) Tax Amount (FC)
  TaxSumSys Num(19,6) Tax Amount (SC)
  BaseSum Num(19,6) Base Amount
  BaseSumFrg Num(19,6) Base Amount (FC)
  BaseSumSys Num(19,6) Base Amount (SC)
  ObjectType nVarChar(20) Object Type default=234000031 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Status default=Y [Y=Normal Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) Applied Tax
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  LineSeq Int(11) Row Sequence
  DeferrAcct nVarChar(15) Deferred Tax Account ->OACT
  BaseType Int(11) Base Document Type default=-1
  BaseAbs Int(11) Base Document Internal No. default=-1
  BaseSeq Int(11) Base Doc. Row Sequence
  DeductTax Num(19,6) Deductible Tax Amount
  DdctTaxFrg Num(19,6) Deductible Tax Amount (FC)
  DdctTaxSys Num(19,6) Deductible Tax Amount (SC)
  BaseAppld Num(19,6) Applied Base Amount
  BaseApldFC Num(19,6) Applied Base Amount (FC)
  BaseApldSC Num(19,6) Applied Base Amount (SC)
  NonDdctPrc Num(19,6) Non Deductible %
  NonDdctAct nVarChar(15) Non Deductible Account ->OACT
  TaxInPrice VarChar(1) Tax Included in Price? default=N [Y=Yes, N=No]
  Exempt VarChar(1) Exempt? default=N [Y=Yes, N=No]
  TaxExpAct nVarChar(15) Expense Account for Tax ->OACT
  OnHoldTax Num(19,6) On Hold Tax Amount
  OnHoldTaxF Num(19,6) On Hold Tax Amount (FC)
  OnHoldTaxS Num(19,6) On Hold Tax Amount (SC)
  InGrossRev VarChar(1) Included in Gross Revenue default=N [Y=Yes, N=No]
  TaxSumOrg Num(19,6) Tax Amount Original
  TaxSumOrgF Num(19,6) Tax Amount Original (FC)
  TaxSumOrgS Num(19,6) Tax Amount Original (SC)
  OpenTax Num(19,6) Open Service Tax
  OpenTaxFC Num(19,6) Open Service Tax (FC)
  OpenTaxSC Num(19,6) Open Service Tax (SC)
  Unencumbrd VarChar(1) Unencumbered default=N [Y=Yes, N=No]
  TaxOnRI VarChar(1) Tax On Reserve Invoice default=N [Y=Yes, N=No]
  RvsChrgPrc Num(19,6) Reverse Charge %
  RvsChrgTax Num(19,6) Reverse Charge Tax Amount
  RvsChrgSC Num(19,6) Reverse Charge Tax Amount (SC)
  RvsChrgFC Num(19,6) Reverse Charge Tax Amount (FC)
  InFirstIns VarChar(1) Included in First Installment default=N [Y=Yes, N=No]
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CESTrel VarChar(1) CEST Relevant default=N [Y=, N=]

# RRR5 - A/R Return Request - Withholding Tax
Module: Marketing Documents | 158 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  SECONDERY U: AbsEntry, WTCode, BaseAbsEnt, Doc1LineNo
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->ORRR
  WTCode nVarChar(4) WTax Code ->OWHT
  Rate Num(19,6) Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntSC Num(19,6) Taxable Amount (SC)
  TxblAmntFC Num(19,6) Taxable Amount (FC)
  WTAmnt Num(19,6) WTax Amount
  WTAmntSC Num(19,6) WTax Amount (SC)
  WTAmntFC Num(19,6) WTax Amount (FC)
  ApplAmnt Num(19,6) Applied WTax Amount
  ApplAmntSC Num(19,6) Applied WTax Amount (SC)
  ApplAmntFC Num(19,6) Applied WTax Amount (FC)
  Category VarChar(1) Category [P=Payment, I=Invoice]
  Criteria VarChar(1) Criteria [Y=Accrual, N=Cash]
  Account nVarChar(15) G/L Account ->OACT
  Type VarChar(1) Withholding Tax Type [V=VAT Withholding, I=Income Tax Withholding]
  RoundType VarChar(1) Rounding Type [T=Truncated, C=Commercial Values, N=No Rounding]
  BaseType VarChar(1) Base Type [G=Gross, N=Net, V=VAT, U=UoM]
  BaseAbsEnt Int(11) Base Document Internal No. default=-1
  BaseLine Int(11) Base Row
  BaseNum Int(11) Base Document Type default=-1 [-1=, 0=, 23=Sales Quotation, 17=Sales Order, 15=Delivery]
  LineNum Int(11) Row Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Doc. Internal No. default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=234000031 ->ADP1
  Doc1LineNo Int(11) DOC1 Line Number default=-1
  WtLineType VarChar(1) WTax Row Type default=D [D=Document Level WTax, L=Row Level WTax]
  TxblCurr nVarChar(3) Taxable Currency from Doc Line
  DtblCurr nVarChar(3) Deductible Currency
  DtblRate Num(19,6) Rate for Deductible Amount
  txblRate Num(19,6) Rate for Taxable Amount
  DtblAmount Num(19,6) Deductible Amount
  TdsAcc nVarChar(15) TDS Account ->OACT
  SurAcc nVarChar(15) Surcharge Account ->OACT
  CessAcc nVarChar(15) Cess Account ->OACT
  HscAcc nVarChar(15) HSC Account ->OACT
  TdsRate Num(19,6) TDS Rate
  SurRate Num(19,6) Surcharge Rate
  CessRate Num(19,6) Cess Rate
  HscRate Num(19,6) HSC Rate
  TdsBAmt Num(19,6) TDS Base Amount
  TdsBAmtSC Num(19,6) TDS Base Amount (SC)
  TdsBAmtFC Num(19,6) TDS Base Amount (FC)
  SurBAmt Num(19,6) Surcharge Base Amount
  SurBAmtSC Num(19,6) Surcharge Base Amount (SC)
  SurBAmtFC Num(19,6) Surcharge Base Amount (FC)
  CessBAmt Num(19,6) Cess Base Amount
  CessBAmtSC Num(19,6) Cess Base Amount (SC)
  CessBAmtFC Num(19,6) Cess Base Amount (FC)
  HscBAmt Num(19,6) HSC Base Amount
  HscBAmtSC Num(19,6) HSC Base Amount (SC)
  HscBAmtFC Num(19,6) HSC Base Amount (FC)
  TdsAmnt Num(19,6) TDS Tax Amount
  TdsAmntSC Num(19,6) TDS Tax Amount (SC)
  TdsAmntFC Num(19,6) TDS Tax Amount (FC)
  SurAmnt Num(19,6) Surcharge Tax Amount
  SurAmntSC Num(19,6) Surcharge Tax Amount (SC)
  SurAmntFC Num(19,6) Surcharge Tax Amount (FC)
  CessAmnt Num(19,6) Cess Tax Amount
  CessAmntSC Num(19,6) Cess Tax Amount (SC)
  CessAmntFC Num(19,6) Cess Tax Amount (FC)
  HscAmnt Num(19,6) HSC Tax Amount
  HscAmntSC Num(19,6) HSC Tax Amount (SC)
  HscAmntFC Num(19,6) HSC Tax Amount (FC)
  TdsAppl Num(19,6) Applied TDS Amount
  TdsApplSC Num(19,6) Applied TDS Amount (SC)
  TdsApplFC Num(19,6) Applied TDS Amount (FC)
  SurAppl Num(19,6) Applied Surcharge Amount
  SurApplSC Num(19,6) Applied Surcharge Amount (SC)
  SurApplFC Num(19,6) Applied Surcharge Amount (FC)
  CessAppl Num(19,6) Applied Cess Amount
  CessApplSC Num(19,6) Applied Cess Amount (SC)
  CessApplFC Num(19,6) Applied Cess Amount (FC)
  HscAppl Num(19,6) Applied HSC Amount
  HscApplSC Num(19,6) Applied HSC Amount (SC)
  HscApplFC Num(19,6) Applied HSC Amount (FC)
  BatchNum Int(11) Journal Voucher No.
  InCSTCode nVarChar(2) CST Code Incoming
  OutCSTCode nVarChar(2) CST Code Outgoing
  DpmWTApl Num(19,6) DPM WT Applied Amount
  DpmWTAplSC Num(19,6) DPM WT Applied Amount (SC)
  DpmWTAplFC Num(19,6) DPM WT Applied Amount (FC)
  WTTypeId Int(11) WT Type Id ->OWTT
  LnBsAmt Num(19,6) BR Line WT Base Amount
  LnBsAmtSC Num(19,6) BR Line WT Base Amount(SC)
  LnBsAmtFC Num(19,6) BR Line WT Base Amount(FC)
  LnCmTAmt Num(19,6) BR Line Cumulated Taxable Amount
  LnCmTAmtSC Num(19,6) BR Line Cumulated Taxable Amount(SC)
  LnCmTAmtFC Num(19,6) BR Line Cumulated Taxable Amount(FC)
  TDSType VarChar(1) TDS Type [E=eTDS, D=GST TDS, C=GST TCS, S=SALES TCS]
  IgstAcc nVarChar(15) IGST Account ->OACT
  CgstAcc nVarChar(15) CGST Account ->OACT
  SgstAcc nVarChar(15) SGST Account ->OACT
  IgstAmnt Num(19,6) IGST Tax Amount
  IgstAmntSC Num(19,6) IGST Tax Amount (SC)
  IgstAmntFC Num(19,6) IGST Tax Amount (FC)
  CgstAmnt Num(19,6) CGST Tax Amount
  CgstAmntSC Num(19,6) CGST Tax Amount (SC)
  CgstAmntFC Num(19,6) CGST Tax Amount (FC)
  SgstAmnt Num(19,6) SGST Tax Amount
  SgstAmntSC Num(19,6) SGST Tax Amount (SC)
  SgstAmntFC Num(19,6) SGST Tax Amount (FC)
  IgstRate Num(19,6) IGST Rate
  CgstRate Num(19,6) CGST Rate
  SgstRate Num(19,6) SGST Rate
  IgstBAmt Num(19,6) IGST Base Amount
  IgstBAmtSC Num(19,6) IGST Base Amount (SC)
  IgstBAmtFC Num(19,6) IGST Base Amount (FC)
  CgstBAmt Num(19,6) CGST Base Amount
  CgstBAmtSC Num(19,6) CGST Base Amount (SC)
  CgstBAmtFC Num(19,6) CGST Base Amount (FC)
  SgstBAmt Num(19,6) SGST Base Amount
  SgstBAmtSC Num(19,6) SGST Base Amount (SC)
  SgstBAmtFC Num(19,6) SGST Base Amount (FC)
  IgstAppl Num(19,6) Applied IGST Amount
  IgstApplSC Num(19,6) Applied IGST Amount (SC)
  IgstApplFC Num(19,6) Applied IGST Amount (FC)
  CgstAppl Num(19,6) Applied CGST Amount
  CgstApplSC Num(19,6) Applied CGST Amount (SC)
  CgstApplFC Num(19,6) Applied CGST Amount (FC)
  SgstAppl Num(19,6) Applied SGST Amount
  SgstApplSC Num(19,6) Applied SGST Amount (SC)
  SgstApplFC Num(19,6) Applied SGST Amount (FC)
  UtgstAcc nVarChar(15) UTGST Account ->OACT
  CsgstAcc nVarChar(15) Cess GST Account ->OACT
  UtgstAmt Num(19,6) UTGST Tax Amount
  UtgstAmtSC Num(19,6) UTGST Tax Amount (SC)
  UtgstAmtFC Num(19,6) UTGST Tax Amount (FC)
  CsgstAmt Num(19,6) Cess GST Tax Amount
  CsgstAmtSC Num(19,6) Cess GST Tax Amount (SC)
  CsgstAmtFC Num(19,6) Cess GST Tax Amount (FC)
  UtgstRate Num(19,6) UTGST Rate
  CsgstRate Num(19,6) Cess GST Rate
  UtgstBAmt Num(19,6) UTGST Base Amount
  UtgstBAmtS Num(19,6) UTGST Base Amount (SC)
  UtgstBAmtF Num(19,6) UTGST Base Amount (FC)
  CsgstBAmt Num(19,6) Cess GST Base Amount
  CsgstBAmtS Num(19,6) Cess GST Base Amount (SC)
  CsgstBAmtF Num(19,6) Cess GST Base Amount (FC)
  UtgstAppl Num(19,6) Applied UTGST Amount
  UtgstApplS Num(19,6) Applied UTGST Amount (SC)
  UtgstApplF Num(19,6) Applied UTGST Amount (FC)
  CsgstAppl Num(19,6) Applied Cess GST Amount
  CsgstApplS Num(19,6) Applied Cess GST Amount (SC)
  CsgstApplF Num(19,6) Applied Cess GST Amount (FC)
  EncryptIV nVarChar(100) Encrypt IV
  TcsIntAcct nVarChar(15) TCS Interim Account ->OACT
  SurIntAcct nVarChar(15) Surcharge Interim Account ->OACT
  CesIntAcct nVarChar(15) Cess Interim Account ->OACT
  HscIntAcct nVarChar(15) HSC interim Account ->OACT
  LnIntAcct nVarChar(15) Interim Account for Tax ->OACT
  FixedAmnt Num(19,6) Fixed Amount
  FixedAmtSC Num(19,6) Fixed Amount (SC)
  FixedAmtFC Num(19,6) Fixed Amount (FC)
  BaseQty Num(19,6) Base Quantity

# RRR6 - A/R Return Request - Installments
Module: Marketing Documents | 65 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, InstlmntID
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORRR
  InstlmntID Int(6) Installment ID default=1
  ObjType nVarChar(20) Object Type default=234000031 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DueDate Date(8) Due Date
  Status VarChar(1) Installment Status default=O [O=Open, C=Closed]
  DunnLevel Int(11) Dunning Level default=0
  InsTotal Num(19,6) Total Installment
  InsTotalFC Num(19,6) Total Installment (FC)
  InsTotalSy Num(19,6) Total Installment (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  VatSum Num(19,6) Total Tax
  VatSumFC Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  VatPaid Num(19,6) Tax Paid to Date
  VatPaidFC Num(19,6) Tax Paid (FC)
  VatPaidSys Num(19,6) Tax Paid (SC)
  TotalExpns Num(19,6) Total Freight Charges
  TotalExpFC Num(19,6) Total Freight Charges (FC)
  TotalExpSC Num(19,6) Total Freight Charges (SC)
  ExpAppl Num(19,6) Applied Freight Charges
  ExpApplFC Num(19,6) Applied Freight Charges (FC)
  ExpApplSC Num(19,6) Applied Freight Charges (SC)
  WTSum Num(19,6) WTax Amount
  WTSumFC Num(19,6) WTax Amount (FC)
  WTSumSC Num(19,6) WTax Amount (SC)
  WTApplied Num(19,6) Applied WTax
  WTAppliedF Num(19,6) Applied WTax (FC)
  WTAppliedS Num(19,6) Applied WTax (SC)
  TotalBlck Num(19,6) Total Reserved Amount
  TotalBlckF Num(19,6) Total Reserved Amount (FC)
  TotalBlckS Num(19,6) Total Reserved Amount (SC)
  VATBlck Num(19,6) Reserved Tax Amount
  VATBlckFC Num(19,6) Reserved Tax Amount (FC)
  VATBlckSC Num(19,6) Reserved Tax Amount (SC)
  ExpnsBlck Num(19,6) Reserved Freight Charges
  ExpnsBlckF Num(19,6) Reserved Freight Charges (FC)
  ExpnsBlckS Num(19,6) Reserved Freight Charges (SC)
  WTBlocked Num(19,6) Reserved WTax Amount
  WTBlockedF Num(19,6) Reserved WTax Amount (FC)
  WTBlockedS Num(19,6) Reserved WTax Amount (SC)
  InstPrcnt Num(19,6) Installment %
  DunWizBlck VarChar(1) Wizard dunning block default=N [N=No, Y=Yes]
  DunDate Date(8) Last Dunning Date
  Paid Num(19,6) Paid
  PaidFrgn Num(19,6) Paid (FC)
  PaidSc Num(19,6) Paid (SC)
  reserved VarChar(1) Reserved default=N [N=No, Y=Yes]
  TaxOnExp Num(19,6) Tax on Freight
  TaxOnExpFc Num(19,6) Tax on Expenses (FC)
  TaxOnExpSc Num(19,6) Tax on Expenses (SC)
  TaxOnExpAp Num(19,6) Applied Tax on Expenses
  TaxOnExApF Num(19,6) Applied Tax on Expenses (FC)
  TaxOnExApS Num(19,6) Applied Tax on Expenses (SC)
  TaxOnExBlo Num(19,6) Reserved Tax on Freight Amount
  TaxOnExBlF Num(19,6) Reserved Tax on Freight Amt FC
  TaxOnExBlS Num(19,6) Reserved Tax on Freight Amt SC
  LvlUpdDate Date(8) Dunning Level Update Date
  Ordered VarChar(1) Payment Ordered default=N [Y=Yes, N=No]
  PaidDpm Num(19,6) Paid by Down Payment
  PaidDpmFc Num(19,6) Paid by Down Payment (FC)
  PaidDpmSc Num(19,6) Paid by Down Payment (SC)
  EncryptIV nVarChar(100) Encrypt IV

# RRR7 - A/R Return Request - Delivery Packages
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORRR
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type default=234000031 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV

# RRR8 - A/R Return Request - Items in Package
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum, ItemCode, UomEntry, NumPerMsr
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORRR
  PackageNum Int(11) Package Number
  ItemCode nVarChar(50) Item Code ->OITM
  Quantity Num(19,6) Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=234000031 ->ADP1
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value default=0

# RRR9 - A/R Return Request - Drawn Dpm
Module: Marketing Documents | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORRR
  LineNum Int(11) Row Number
  BaseAbs Int(11) Base Document Internal ID ->ODPI
  BaseLine Int(11) Base Document Row
  TargetBase VarChar(1) Target or Base Document default=T [B=Base, T=Target]
  ObjType nVarChar(20) Base Object Type default=203 [203=A/R Down Payment]
  DrawnSum Num(19,6) Net LC
  DrawnSumFc Num(19,6) Net FC
  DrawnSumSc Num(19,6) Net SC
  LogInstanc Int(11) Log Instance default=0
  ObjCode nVarChar(20) Object Type default=234000031 ->ADP1
  ApplDrawn Num(19,6) Applied Net LC
  ApplDrawnF Num(19,6) Applied Net FC
  ApplDrawnS Num(19,6) Applied Net SC
  BaseDocNum Int(11) Base Document Number
  BsDocDate Date(8) Base Posting Date
  BsDueDate Date(8) Base Due Date
  BsCardName nVarChar(100) Base BP Name
  BsComments nVarChar(254) Base Remarks
  Posted VarChar(1) Base Document Posted default=Y [Y=Yes, N=No]
  Vat Num(19,6) Tax LC
  VatFc Num(19,6) Tax FC
  VatSc Num(19,6) Tax SC
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  IsGross VarChar(1) Is Gross Line default=N [N=Net Line, Y=Gross Line]

# SAL1 - Salida - Rows
Module: Marketing Documents | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Entry ->OINV
  LineNum Int(11) Row Number
  BaseEntry Int(11) Base Document Internal ID
  PackQty Num(19,6) Packing Quantity
  PurPackMsr nVarChar(8) Packaging UoM Name default=Pack
  ArsnalName nVarChar(20) Storage Group Name
  ArsnalCode nVarChar(20) Storage Group Code
  UnitMsr nVarChar(5) Ref. UoM (Type) default=Unit
  Quantity Num(19,6) Quantity
  Fraction Num(19,6) Remainder
  Weight1 Num(19,6) Weight
  LineTotal Num(19,6) Row Total
  ItemCode nVarChar(50) Item No. ->OITM

# SFC1 - Self Credit Memo - Rows
Module: Marketing Documents | 317 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  STATUS: LineStatus
  CURRENCY: Currency
  ACCOUNT: AcctCode
  BASE_ENTRY: BaseEntry, BaseType, BaseLine
  VIS_ORDER: DocEntry, VisOrder
  OWNER_CODE: OwnerCode
  ITM_WHS_OQ: ItemCode, WhsCode, OpenQty
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFC
  LineNum Int(11) Row Number
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=, 254000066=Self Credit Memo]
  TrgetEntry Int(11) Target Document Internal ID
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 19=A/P Credit Memo, 254000066=Self Credit Memo]
  BaseEntry Int(11) Base Document Internal ID
  BaseLine Int(11) Base Row
  LineStatus VarChar(1) Row Status default=O [O=Open, C=Closed]
  ItemCode nVarChar(50) Item No. ->OITM
  Dscription nVarChar(200) Item/Service Description
  Quantity Num(19,6) Quantity
  ShipDate Date(8) Row Delivery Date
  OpenQty Num(19,6) Remaining Open Quantity
  Price Num(19,6) Price after Discount
  Currency nVarChar(3) Price Currency ->OCRN
  Rate Num(19,6) Currency Rate
  DiscPrcnt Num(19,6) Discount % per Row
  LineTotal Num(19,6) Row Total
  TotalFrgn Num(19,6) Row Total (FC)
  OpenSum Num(19,6) Open Amount
  OpenSumFC Num(19,6) Open Amount (FC)
  VendorNum nVarChar(50) Vendor Catalog No.
  SerialNum nVarChar(17) Serial Number
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  SlpCode Int(11) Sales Employee Code default=-1 ->OSLP
  Commission Num(19,6) Commission Percentage
  TreeType VarChar(1) BOM Type default=N [N=Not a BOM, A=Assembly, S=Sales, I=Sales BOM Component, P=Production, T=Template]
  AcctCode nVarChar(15) Account Code ->OACT
  TaxStatus VarChar(1) Tax Definition [Y=Yes, N=No]
  GrossBuyPr Num(19,6) Gross Profit Base Price
  PriceBefDi Num(19,6) Unit Price
  DocDate Date(8) Posting Date
  Flags Int(11) Flags default=0
  OpenCreQty Num(19,6) Credit Memo Amount
  UseBaseUn VarChar(1) Inventory UoM default=N [Y=Yes, N=No]
  SubCatNum nVarChar(50) BP Catalog No. ->OSCN
  BaseCard nVarChar(15) Base BP Code ->OCRD
  TotalSumSy Num(19,6) Row Total (SC)
  OpenSumSys Num(19,6) Open Amount (SC)
  InvntSttus VarChar(1) Warehouse Status default=O [O=Open, C=Closed]
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  CodeBars nVarChar(254) Bar Code
  VatPrcnt Num(19,6) Tax Rate per Row
  VatGroup nVarChar(8) Tax Definition ->OVTG
  PriceAfVAT Num(19,6) Gross Price after Discount
  Height1 Num(19,6) Height 1
  Hght1Unit Int(6) Unit of Height 1
  Height2 Num(19,6) Height 2
  Hght2Unit Int(6) Unit of Height 2
  Width1 Num(19,6) Width 1
  Wdth1Unit Int(6) Unit of Width 1
  Width2 Num(19,6) Width 2
  Wdth2Unit Int(6) Unit of Width 2
  Length1 Num(19,6) Length 1
  Len1Unit Int(6) Unit of Length 1
  length2 Num(19,6) Length 2
  Len2Unit Int(6) Unit of Length 2
  Volume Num(19,6) Volume
  VolUnit Int(6) Vol. Unit
  Weight1 Num(19,6) Weight 1
  Wght1Unit Int(6) Unit of Weight 1
  Weight2 Num(19,6) Weight 2
  Wght2Unit Int(6) Unit of Weight 2
  Factor1 Num(19,6) Factor 1
  Factor2 Num(19,6) Factor 2
  Factor3 Num(19,6) Factor 3
  Factor4 Num(19,6) Factor 4
  PackQty Num(19,6) Packing Quantity
  UpdInvntry VarChar(1) Whse Update default=Y [Y=Yes, N=No]
  BaseDocNum Int(11) Base Document No.
  BaseAtCard nVarChar(100) Customer/Vendor Base Document
  SWW nVarChar(16) Additional Identifier
  VatSum Num(19,6) Total Tax
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  FinncPriod Int(11) Posting Period ->OFPR
  ObjType nVarChar(20) Object Type default=254000066 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BlockNum nVarChar(100) Block Number
  ImportLog nVarChar(20) Import Log
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAqcuistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  DistribSum Num(19,6) Distributed Amount
  DstrbSumFC Num(19,6) Distributed Amount (FC)
  DstrbSumSC Num(19,6) Distributed Amount (SC)
  GrssProfit Num(19,6) Row Gross Profit
  GrssProfSC Num(19,6) Row Gross Profit (SC)
  GrssProfFC Num(19,6) Row Gross Profit (FC)
  VisOrder Int(11) Visual Order
  INMPrice Num(19,6) Item's Last Sales Price (OINM)
  PoTrgNum Int(11) PO Target No.
  PoTrgEntry nVarChar(11) PO Target Internal ID
  DropShip VarChar(1) Drop-Ship default=N [Y=Yes, N=No]
  PoLineNum Int(11) PO Target Row No.
  Address nVarChar(254) Address
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type [Y=Regular Tax, N=No Tax, U=Use Tax]
  OrigItem nVarChar(50) Original Item ->OITM
  BackOrdr VarChar(1) Allow Backorder [Y=Yes, N=No]
  FreeTxt nVarChar(100) Free Text
  PickStatus VarChar(1) Pick Status default=N [Y=Picked, N=Not Picked, R=Released for Picking, P=Partially Picked]
  PickOty Num(19,6) Pick Quantity
  PickIdNo Int(11) Pick ID
  TrnsCode Int(6) Shipping Method default=-1 ->OSHP
  VatAppld Num(19,6) Applied Tax
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  BaseQty Num(19,6) Base Quantity
  BaseOpnQty Num(19,6) Base Open Quantity
  VatDscntPr Num(19,6) Tax Discount %
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  DeferrTax VarChar(1) Deferred Tax default=N [Y=Yes, N=No]
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatlF Num(19,6) Net Tax Amount (FC)
  LineVatS Num(19,6) Net Tax Amount (SC)
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value
  CEECFlag VarChar(1) Correction Invoice Was/Should Be default=S [W=Was, S=Should Be]
  ToStock Num(19,6) Corr. Invoice Amt to Inventory
  ToDiff Num(19,6) Corr. Invoice Amount to Diff.
  ExciseAmt Num(19,6) Excise Amount
  TaxPerUnit Num(19,6) Tax per Unit
  TotInclTax Num(19,6) Total Including Tax
  CountryOrg nVarChar(3) Country/Region of Origin
  StckDstSum Num(19,6) Stock Distribution Sum
  ReleasQtty Num(19,6) Released Quantity
  LineType VarChar(1) Row Type default=R [R=Regular]
  TranType VarChar(1) Transaction Type [C=Complete, R=Reject]
  Text Text(16) Text
  OwnerCode Int(11) Document Owner
  StockPrice Num(19,6) Item Cost
  ConsumeFCT VarChar(1) Consumer Sales Forecast [Y=Yes, N=No]
  LstByDsSum Num(19,6) Last Buy Distribute Sum
  StckINMPr Num(19,6) Stock Inm Price
  LstBINMPr Num(19,6) Last Buy Inventory Journal Pr.
  StckDstFc Num(19,6) Stock Distribution Sum (FC)
  StckDstSc Num(19,6) Stock Distribution Sum (SC)
  LstByDsFc Num(19,6) Last Buy Distribute Sum (FC)
  LstByDsSc Num(19,6) Last Buy Distribute Sum (SC)
  StockSum Num(19,6) Stock Sum
  StockSumFc Num(19,6) Stock Sum FC
  StockSumSc Num(19,6) Stock Sum SC
  StckSumApp Num(19,6) Stock Sum Applied
  StckAppFc Num(19,6) Stock Sum Applied FC
  StckAppSc Num(19,6) Stock Sum Applied SC
  ShipToCode nVarChar(50) Ship-to Code
  ShipToDesc nVarChar(254) Ship-to Description
  StckAppD Num(19,6) Stock Distrib. - Applied Sum
  StckAppDFC Num(19,6) Stock Dist. - Applied Sum (FC)
  StckAppDSC Num(19,6) Stock Dist. - Applied Sum (SC)
  BasePrice VarChar(1) Price for Total Calculation default=E [E=Exclude Tax, I=Include Tax]
  GTotal Num(19,6) Gross Total
  GTotalFC Num(19,6) Gross Total (FC)
  GTotalSC Num(19,6) Gross Total (SC)
  DistribExp VarChar(1) Distribute Freight Charges [Y=Yes, N=No]
  DescOW VarChar(1) Description overwritten default=N [Y=Yes, N=No]
  DetailsOW VarChar(1) Remarks overwritten default=N [Y=Yes, N=No]
  GrossBase Int(6) Base Method for Gross Profit
  VatWoDpm Num(19,6) Tax Before DPM Applied
  VatWoDpmFc Num(19,6) Tax Before DPM Applied (FC)
  VatWoDpmSc Num(19,6) Tax Before DPM Applied (SC)
  CFOPCode nVarChar(6) CFOP Code for Document ->OCFP
  CSTCode nVarChar(6) CST Code for ICMS
  Usage Int(11) Usage Code for Document ->OUSG
  TaxOnly VarChar(1) Tax Only [Y=Yes, N=No]
  WtCalced VarChar(1) Withholding Tax Calculated default=N [N=No, Y=Yes]
  QtyToShip Num(19,6) Quantity to Ship
  DelivrdQty Num(19,6) Delivered Quantity
  OrderedQty Num(19,6) Ordered Quantity
  CogsOcrCod nVarChar(8) COGS Distribution Rule Code ->OOCR
  CiOppLineN Int(11) Row Number of Associated Row default=-1
  CogsAcct nVarChar(15) COGS Account Code ->OACT
  ChgAsmBoMW VarChar(1) Change Whs for Asm BoM Child [Y=Yes, N=No]
  ActDelDate Date(8) Actual Delivery Date
  OcrCode2 nVarChar(8) Costing Code 2 ->OOCR
  OcrCode3 nVarChar(8) Costing Code 3 ->OOCR
  OcrCode4 nVarChar(8) Costing Code 4 ->OOCR
  OcrCode5 nVarChar(8) Costing Code 5 ->OOCR
  TaxDistSum Num(19,6) Tax Distributed Amount
  TaxDistSFC Num(19,6) Tax Distributed Amount (FC)
  TaxDistSSC Num(19,6) Tax Distributed Amount (SC)
  PostTax VarChar(1) Post Tax in Price to Stock default=Y [Y=Yes, N=No]
  Excisable VarChar(1) Excisable [Yes/No] [Y=Yes, N=No]
  AssblValue Num(19,6) Assessable Value
  RG23APart1 Int(11) RG23A Part1 Number
  RG23APart2 Int(11) RG23A Part2 Number
  RG23CPart1 Int(11) RG23C Part1 Number
  RG23CPart2 Int(11) RG23C Part2 Number
  CogsOcrCo2 nVarChar(8) COGS Distribution Rule Code2 ->OOCR
  CogsOcrCo3 nVarChar(8) COGS Distribution Rule Code3 ->OOCR
  CogsOcrCo4 nVarChar(8) COGS Distribution Rule Code4 ->OOCR
  CogsOcrCo5 nVarChar(8) COGS Distribution Rule Code5 ->OOCR
  LnExcised VarChar(1) Line Excised [O=Open, C=Closed, P=Copied to OEI]
  LocCode Int(11) Location Code ->OLCT
  StockValue Num(19,6) Total COGS Value
  GPTtlBasPr Num(19,6) Total Base Price for Profit
  unitMsr2 nVarChar(100) Pur/Sal UoM if BaseUnit
  NumPerMsr2 Num(19,6) Pur/Sal UoM Value if Base Unit
  SpecPrice VarChar(1) Price Source Type default=N [Y=Special Prices for Business Partner, N=Manual, W=Active Price List, Discount Groups, R=Active Price List, U=Inactive Price List, A=Blanket Agreement, P=Period and Volume Discounts, Q=Period and Volume Discounts, Discount Groups, V=Inactive Price List, Discount Groups, 9=Special Prices for Business Partner, !=Blanket Agreement, 0=Period and Volume Discounts, 1=Period and Volume Discounts, Discount Groups, 2=Active Price List, 7=Active Price List, Discount Groups, 5=Inactive Price List, 6=Inactive Price List, Discount Groups]
  CSTfIPI nVarChar(2) CST for IPI Code
  CSTfPIS nVarChar(2) CST for PIS Code
  CSTfCOFINS nVarChar(2) CST for COFINS Code
  ExLineNo nVarChar(10) ExLineNo
  isSrvCall VarChar(1) Created from Service Call default=N [Y=Yes, N=No]
  PQTReqQty Num(19,6) Pur Quotation: Required Qty
  PQTReqDate Date(8) Pur Quotation: Required Date
  PcDocType Int(11) Purchase Confirmation Doc Type default=-1 [-1=No Type, 22=Purchase Order, 540000006=Purchase Quotation]
  PcQuantity Num(19,6) Purchase Confirmation Quantity
  LinManClsd VarChar(1) Line Was Closed Manually default=N [Y=Yes, N=No, U=Unknown]
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  NoInvtryMv VarChar(1) Without Inventory Movement default=N [Y=Yes, N=No]
  ActBaseEnt Int(11) Actual Base Document Entry
  ActBaseLn Int(11) Actual Base Line Number
  ActBaseNum Int(11) Actual Base Document No.
  OpenRtnQty Num(19,6) Quantity Open for Return
  AgrNo Int(11) Agreement No. ->OOAT
  AgrLnNum Int(11) Agreement Row Number
  CredOrigin VarChar(1) Credit Origin ->OBSI
  Surpluses Num(19,6) Surpluses
  DefBreak Num(19,6) Defect and Breakup
  Shortages Num(19,6) Shortages
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  UomEntry2 Int(11) UoM Entry if Base Unit default=0 ->OUOM
  UomCode nVarChar(20) UoM Code
  UomCode2 nVarChar(20) UoM Code if Base Unit
  FromWhsCod nVarChar(8) From Warehouse Code ->OWHS
  NeedQty VarChar(1) Consider Quantity of Items default=N [Y=Yes, N=No]
  PartRetire VarChar(1) Partial Retirement default=N [Y=Yes, N=No]
  RetireQty Num(19,6) Retirement Quantity
  RetireAPC Num(19,6) Retirement APC
  RetirAPCFC Num(19,6) Retirement APC FC
  RetirAPCSC Num(19,6) Retirement APC SC
  InvQty Num(19,6) Quantity - Inventory UoM
  OpenInvQty Num(19,6) Open Quantity (Inventory UoM)
  EnSetCost VarChar(1) Enable Set Item Cost in Return default=N [Y=Yes, N=No]
  RetCost Num(19,6) Return Cost in A/R Return
  Incoterms Int(11) Incoterms default=0 ->ODCI
  TransMod Int(11) Transport Mode default=0 ->ODCI
  LineVendor nVarChar(15) Line Vendor Code ->OCRD
  DistribIS VarChar(1) Distribute Intrastat Freight default=N [Y=Yes, N=No]
  ISDistrb Num(19,6) Intrastat Distrib. Amount
  ISDistrbFC Num(19,6) Intrastat Distrib. Amount (FC)
  ISDistrbSC Num(19,6) Intrastat Distrib. Amount (SC)
  IsByPrdct VarChar(1) Item Is By-Product default=N [N=No, Y=Yes]
  ItemType Int(11) Item Type default=4 [4=Item]
  PriceEdit VarChar(1) Price Was Edited by User default=N [N=No, Y=Yes]
  PrntLnNum Int(11) Parent Line Number
  LinePoPrss VarChar(1) Line PO Process default=N [Y=Yes, N=No]
  FreeChrgBP VarChar(1) Free of Charge (BP) default=N [Y=Yes, N=No]
  TaxRelev VarChar(1) Tax Relevant Row default=Y [Y=Yes, N=No]
  LegalText nVarChar(254) Legal Text
  ThirdParty VarChar(1) Third Party default=N [Y=Yes, N=No]
  LicTradNum nVarChar(32) Federal Tax ID
  InvQtyOnly VarChar(1) Change Qty (Inv. UoM) Only default=N [Y=Yes, N=No]
  UnencReasn Int(11) Reason for Unencumbered ICMS
  ShipFromCo nVarChar(50) Ship-from Code
  ShipFromDe nVarChar(254) Ship-from Description
  FisrtBin nVarChar(228) First Bin Location
  AllocBinC nVarChar(11) Allocated Bin Location Count
  ExpType nVarChar(4) Expense Type ->OEXD
  ExpUUID nVarChar(50) Expense UUID
  ExpOpType VarChar(1) Expense Operation Type [P=Professional Services, R=Renting Assets, O=Others]
  DIOTNat nVarChar(3) DIOT Nationality ->OCRY
  MYFtype nVarChar(2) MYF type [S1=MYF Wholesale Sales, S2=Retail Sales, P1=MYF Wholesale Purchases, P3=Other Expense Transactions]
  GPBefDisc Num(19,6) Gross Price
  ReturnRsn Int(6) Return Reason default=-1
  ReturnAct Int(6) Return Action default=-1
  StgSeqNum Int(11) Stage Sequence Number
  StgEntry Int(11) Stage Entry ->ORST
  StgDesc nVarChar(100) Stage Description
  ItmTaxType nVarChar(2) Item GST Tax Category [GR=GST Regular, GN=GST Nil Rated, GE=GST Exempt, NE=Excisable, NN=Non-GST Non-Excisable]
  SacEntry Int(11) SAC Entry ->OSAC
  NCMCode Int(11) NCM Code default=-1 ->ONCM
  HsnEntry Int(11) HSN Entry ->OCHP
  OriBAbsEnt Int(11) Original Base Document Internal ID
  OriBLinNum Int(11) Original Base Document Line Number
  OriBDocTyp Int(11) Original Base Document Type
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No, U=Use]
  EncryptIV nVarChar(100) Encrypt IV
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  StdItemId Int(11) Standard Item Identification ->OUNCL
  CommClass Int(11) Commodity Classification ->OUNCL
  VatExEntry Int(11) VAT Exemption AbsEntry ->OVEB
  VatExLN Int(6) VAT Exemption LineNum
  NatOfTrans Int(11) Nature of Transaction ->ODCI
  ISDtCryImp nVarChar(3) Destination Country/Region for Import ->OCRY
  ISDtRgnImp Int(11) Destination Region for Import ->ODCI
  ISOrCryExp nVarChar(3) Country/Region of Origin for Export ->OCRY
  ISOrRgnExp Int(11) Region of Origin for Export ->ODCI
  NVECode nVarChar(6) NVE Code
  PoNum nVarChar(20) Customer's Purchase Order Number
  PoItmNum Int(11) Customer's Purchase Order Item Number
  IndEscala VarChar(1) Indicator for Relevant Scale default=N [Y=Yes, N=No]
  CESTCode Int(11) CEST Code ->OCEST
  CtrSealQty Num(19,6) Control Seal Quantity
  CNJPMan nVarChar(14) CNPJ of Manufacturer
  UFFiscBene nVarChar(10) UF Fiscal Benefit Code
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]
  LegalTIMD nVarChar(250) Legal Text from Item Master Data
  LegalTTCA nVarChar(250) Legal Text from Tax Code Attributes
  LegalTW nVarChar(250) Legal Text from Warehouse
  LegalTCD nVarChar(250) Legal Text from Tax Code Determination
  RevCharge VarChar(1) Reverse Charge default=N [Y=Yes, N=No]
  ListNum Int(6) Price List No. ->OPLN

# SFC10 - Self Credit Memo - Row Structure
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SECONDERY U: DocEntry, AftLineNum, OrderNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFC
  LineSeq Int(11) Row Sequence
  AftLineNum Int(11) After Row Number
  OrderNum Int(11) Order Number
  LineType VarChar(1) Row Type [T=Text, S=Subtotal]
  LineText Text(16) Row Text
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=254000066 ->ADP1

# SFC11 - Self Credit Memo - Drawn Down Payment Detail
Module: Marketing Documents | 70 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LineSeq
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFC
  LineNum Int(11) Row Number
  LineSeq Int(11) Sequence Number
  BaseAbs Int(11) Base Document Internal ID
  BaseType Int(11) Base Object Type default=-1
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  VatPrcnt Num(19,6) VAT Percent
  LineTotal Num(19,6) Net LC
  TotalFrgn Num(19,6) Net FC
  TotalSumSy Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFrgn Num(19,6) Tax FC
  VatSumSys Num(19,6) Tax SC
  ObjType nVarChar(20) Object Type default=254000066 ->ADP1
  LogInstanc Int(11) Log Instance
  IsAcq VarChar(1) Acquisition Tax Liable default=N [N=No, Y=Yes]
  IsAllDrawn VarChar(1) Remaining Amount Drawn default=N [Y=Yes, N=No]
  IsGross VarChar(1) Is Gross Line default=N [N=Net Line, Y=Gross Line]
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  ApplNet Num(19,6) Applied Net LC
  ApplNetFc Num(19,6) Applied Net FC
  ApplNetSc Num(19,6) Applied Net SC
  ApplVat Num(19,6) Applied Tax (LC)
  ApplVatFc Num(19,6) Applied Tax (FC)
  ApplVatSc Num(19,6) Applied Tax (SC)
  BaseNet Num(19,6) Base Net LC
  BaseNetFc Num(19,6) Base Net FC
  BaseNetSc Num(19,6) Base Net SC
  BaseVat Num(19,6) Base Tax LC
  BaseVatFc Num(19,6) Base Tax FC
  BaseVatSc Num(19,6) Base Tax SC
  BaseGross Num(19,6) Base Gross LC
  BaseGrossF Num(19,6) Base Gross FC
  BaseGrossS Num(19,6) Base Gross SC
  LineType VarChar(1) Line Type default=D [D=Document Row, R=Currency Rounding, H=Down Payment Document Rounding]
  DctSum Num(19,6) Deductible Sum LC
  DctSumFc Num(19,6) Deductible Sum FC
  DctSumSc Num(19,6) Deductible Sum SC
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplDct Num(19,6) Applied Deductible Sum LC
  ApplDctFc Num(19,6) Applied Deductible Sum FC
  ApplDctSc Num(19,6) Applied Deductible Sum SC
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  BaseDct Num(19,6) Base Deductible Sum LC
  BaseDctFc Num(19,6) Base Deductible Sum FC
  BaseDctSc Num(19,6) Base Deductible Sum SC
  BaseEq Num(19,6) Base Equalization Sum LC
  BaseEqFc Num(19,6) Base Equalization Sum FC
  BaseEqSc Num(19,6) Base Equalization Sum SC
  TaxCode nVarChar(8) Tax Code ->OSTC
  ApplGross Num(19,6) Applied Gross LC
  ApplGrossF Num(19,6) Applied Gross FC
  ApplGrossS Num(19,6) Applied Gross SC
  TaxAdjust VarChar(1) Manual Tax Adjustment default=N [Y=Yes, N=No]
  RvsChrgSum Num(19,6) Reverse Charge Sum LC
  RvsChrgFc Num(19,6) Reverse Charge Sum FC
  RvsChrgSc Num(19,6) Reverse Charge Sum SC
  BasRvsChrg Num(19,6) Base Reverse Charge LC
  BasRvsFc Num(19,6) Base Reverse Charge FC
  BasRvsSc Num(19,6) Base Reverse Charge SC
  ApplRvs Num(19,6) Applied Reverse Charge LC
  ApplRvsFc Num(19,6) Applied Reverse Charge FC
  ApplRvsSc Num(19,6) Applied Reverse Charge SC
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# SFC12 - Self Credit Memo - Tax Extension
Module: Marketing Documents | 117 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFC
  TaxId0 nVarChar(100) Tax ID 0
  TaxId1 nVarChar(100) Tax ID 1
  TaxId2 nVarChar(100) Tax ID 2
  TaxId3 nVarChar(100) Tax ID 3
  TaxId4 nVarChar(100) Tax ID 4
  TaxId5 nVarChar(100) Tax ID 5
  TaxId6 nVarChar(100) Tax ID 6
  TaxId7 nVarChar(100) Tax ID 7
  TaxId8 nVarChar(100) Tax ID 8
  TaxId9 nVarChar(100) Tax ID 9
  State nVarChar(3) State Code
  County nVarChar(7) County Code
  Incoterms nVarChar(3) Incoterms
  Vehicle nVarChar(10) Vehicle ID
  VidState nVarChar(3) Vehicle State ID
  NfRef nVarChar(254) NF Reference
  Carrier nVarChar(15) Carrier Code ->OCRD
  QoP Int(11) Quantity of Packs
  PackDesc nVarChar(10) Pack Description
  Brand nVarChar(20) Brand
  NoSU Int(11) Number of Shipping Unit
  NetWeight Num(19,6) Net Weight
  GrsWeight Num(19,6) Gross Weight
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=254000066 ->ADP1
  TaxId10 nVarChar(100) Tax ID 10
  TransCat nVarChar(100) Transaction Category
  FormNo nVarChar(100) Form No.
  TaxId11 nVarChar(100) Tax ID 11
  StreetS nVarChar(100) Street
  BlockS nVarChar(100) Block
  BuildingS Text(16) Building/Floor/Room
  CityS nVarChar(100) City
  ZipCodeS nVarChar(20) Zip Code
  CountyS nVarChar(100) County
  StateS nVarChar(3) State ->OCST
  CountryS nVarChar(3) Country/Region ->OCRY
  AddrTypeS nVarChar(100) Address Type
  StreetNoS nVarChar(100) Street No.
  StreetB nVarChar(100) Street
  BlockB nVarChar(100) Block
  BuildingB Text(16) Building/Floor/Room
  CityB nVarChar(100) City
  ZipCodeB nVarChar(20) Zip Code
  CountyB nVarChar(100) County
  StateB nVarChar(3) State ->OCST
  CountryB nVarChar(3) Country/Region ->OCRY
  AddrTypeB nVarChar(100) Address Type
  StreetNoB nVarChar(100) Street No.
  ImpORExp VarChar(1) Import or Export [N=, Y=]
  Vat VarChar(1) VAT default=N [N=No VAT Support, Y=VAT Support]
  AltCrdNamB nVarChar(100) Alternative BP Name
  AltTaxIdB nVarChar(32) Alternative Tax ID
  Address2S nVarChar(50) Address Name 2
  Address3S nVarChar(50) Address Name 3
  Address2B nVarChar(50) Address Name 2
  Address3B nVarChar(50) Address Name 3
  MainUsage Int(11) Main Usage Code of Document ->OUSG
  GlbLocNumS nVarChar(50) Global Location Number
  GlbLocNumB nVarChar(50) Global Location Number
  CollectDT nVarChar(20) Date and Time of Collection
  TransprtDT Date(8) Transport Start Date
  TransprtRS nVarChar(100) Transport Reason
  TaxId12 nVarChar(50) Tax ID 12
  TaxId13 nVarChar(100) Deductee Ref. No. in India
  ImpExpNo nVarChar(100) Import/Export Bill No.
  ImpExpDate Date(8) Import/Export Date
  BpGSTType Int(11) GST Regn Type of BP
  BpGSTN nVarChar(15) GST Regn No of BP
  BpStateCod nVarChar(3) State Code of Business Partner ->OCST
  BPStatGSTN nVarChar(2) GST State Code of BP
  LocGSTType Int(11) GST Regn Type of Location
  LocGSTN nVarChar(15) GST Regn No of Location
  LocStatCod nVarChar(3) State Code of Location ->OCST
  LocStaGSTN nVarChar(2) GST State Code of Location
  BpCountry nVarChar(3) Country/Region Code of BP ->OCRY
  OrigImpNo nVarChar(100) Original Bill of Entry No.
  OrigImpDat Date(8) Original Bill of Entry Date
  ExportType VarChar(1) Exporting Type default=E [E=Imports/Exports, S=SEZ Developer, U=SEZ Unit, D=Deemed Imports/Exports]
  PortCode nVarChar(100) Port Code
  BoEValue Num(19,6) Bill of Entry Value
  IsIGSTAct VarChar(1) Supply under IGST Account [Y=Yes, N=No]
  ClaimRefun VarChar(1) Claim Refund [Y=Yes, N=No]
  TaxRateDif Int(11) Differential % of Tax Rate [65=, 100=]
  BPGdsIssP nVarChar(15) Goods Issue Place BP
  CNPJGIP nVarChar(100) Goods Issue Place CNPJ
  CPFGIP nVarChar(100) Goods Issue Place CPF
  StreetGIP nVarChar(100) Goods Issue Place Street
  StrtNoGIP nVarChar(100) Goods Issue Place Street No.
  BldngGIP Text(16) Goods Issue Place Building
  ZipGIP nVarChar(20) Goods Issue Place Zip Code
  BlockGIP nVarChar(100) Goods Issue Place Block
  CityGIP nVarChar(100) Goods Issue Place City
  CountyGIP nVarChar(100) Goods Issue Place County
  StateGIP nVarChar(3) Goods Issue Place State ->OCST
  CountryGIP nVarChar(3) Goods Issue Place Country/Region ->OCRY
  PhoneGIP nVarChar(20) Goods Issue Place Phone
  EMailGIP nVarChar(100) Goods Issue Place E-Mail
  DptDateGIP Date(8) Goods Issue Place Departure Date
  BPDelivryP nVarChar(15) Delivery Place BP
  CNPJDlvryP nVarChar(100) Delivery Place CNPJ
  CPFDlvryP nVarChar(100) Delivery Place CPF
  StrtDlvryP nVarChar(100) Delivery Place Street
  StrNoDlvrP nVarChar(100) Delivery Place Street No.
  BldDlvryP Text(16) Delivery Place Building
  ZipDlvryP nVarChar(20) Delivery Place Zip Code
  BlckDlvryP nVarChar(100) Delivery Place Block
  CityDlvryP nVarChar(100) Delivery Place City
  CntyDlvryP nVarChar(100) Delivery Place County
  StatDlvryP nVarChar(3) Delivery Place State ->OCST
  CtryDlvryP nVarChar(3) Delivery Place Country/Region ->OCRY
  FoneDlvryP nVarChar(20) Delivery Place Phone
  MailDlvryP nVarChar(100) Delivery Place E-Mail
  DpDtDlvryP Date(8) Delivery Place Departure Date
  AuthedCNPJ nVarChar(250) Authorized CNPJ or CPF
  TaxId14 nVarChar(250) ITR Filing

# SFC13 - Self Credit Memo Rows - Distributed Freights
Module: Marketing Documents | 59 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFC
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=254000066 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Aquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Normal Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) VAT Applied (FC)
  VatAppldSC Num(19,6) VAT Applied (SC)
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock default=N [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Line No.
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Abs. Entry default=-1
  BaseGroup Int(11) Base Document Group default=-1
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1
  VisOrder Int(11) Visual Order
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DistribExp VarChar(1) Distribute Freights [Y=Yes, N=No]
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ

# SFC14 - Self Credit Memo - Assembly - Rows
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFC
  LineNum Int(11) Row Number default=-1
  ChildNum Int(11) Child Number default=-1
  ItemCode nVarChar(50) Item no. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  TotalQty Num(19,6) Total Quantity
  OpenQty Num(19,6) Remaining Open Quantity
  ObjectType nVarChar(20) object type default=254000066 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BaseChildN Int(11) Base Child Number default=-1
  EncryptIV nVarChar(100) Encrypt IV

# SFC15 - Self Credit Memo - Drawn Down Payment Applied
Module: Marketing Documents | 84 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFC
  LineNum Int(11) Row Number
  ObjType nVarChar(20) object type default=254000066 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  StaCode nVarChar(8) Tax Authority Code
  StaType Int(11) Tax Authority Type
  StaIndex Int(11) Tax Authority Seq Index
  BaseNet Num(19,6) Net LC
  BaseNetFc Num(19,6) Net FC
  BaseNetSc Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFc Num(19,6) Tax FC
  VatSumSc Num(19,6) Tax SC
  DctSum Num(19,6) Deductible Sum LC
  DctSumFc Num(19,6) Deductible Sum FC
  DctSumSc Num(19,6) Deductible Sum SC
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplNet Num(19,6) Applied Net LC
  ApplNetFc Num(19,6) Applied Net FC
  ApplNetSc Num(19,6) Applied Net SC
  ApplVat Num(19,6) Applied Tax (LC)
  ApplVatFc Num(19,6) Applied Tax (FC)
  ApplVatSc Num(19,6) Applied Tax (SC)
  ApplDct Num(19,6) Applied Deductible Sum LC
  ApplDctFc Num(19,6) Applied Deductible Sum FC
  ApplDctSc Num(19,6) Applied Deductible Sum SC
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  PaidNet Num(19,6) Paid Net LC
  PaidNetFc Num(19,6) Paid Net FC
  PaidNetSc Num(19,6) Paid Net SC
  PaidVat Num(19,6) Paid Tax LC
  PaidVatFc Num(19,6) Paid Tax FC
  PaidVatSc Num(19,6) Paid Tax SC
  PaidDct Num(19,6) Paid Deductible Sum LC
  PaidDctFc Num(19,6) Paid Deductible Sum FC
  PaidDctSc Num(19,6) Paid Deductible Sum SC
  PaidEq Num(19,6) Paid Equalization Sum LC
  PaidEqFc Num(19,6) Paid Equalization Sum FC
  PaidEqSc Num(19,6) Paid Equalization Sum SC
  DpApplNet Num(19,6) Dpm Appl Net LC
  DpApplNetF Num(19,6) Dpm Appl Net FC
  DpApplNetS Num(19,6) Dpm Appl Net SC
  DpApplVat Num(19,6) Dpm Appl Tax LC
  DpApplVatF Num(19,6) Dpm Appl Tax FC
  DpApplVatS Num(19,6) Dpm Appl Tax SC
  DpApplDct Num(19,6) Dpm Appl Deductible Sum LC
  DpApplDctF Num(19,6) Dpm Appl Deductible Sum FC
  DpApplDctS Num(19,6) Dpm Appl Deductible Sum SC
  DpApplEq Num(19,6) Dpm Appl Equalization Sum LC
  DpApplEqFc Num(19,6) Dpm Appl Equalization Sum FC
  DpApplEqSc Num(19,6) Dpm Appl Equalization Sum SC
  TaxCode nVarChar(8) Tax Code ->OSTC
  LineType VarChar(1) Row Type default=D [D=Document, R=Exchange Rate Rounding, H=Document Header Rounding]
  BaseGrs Num(19,6) Gross LC
  BaseGrsFc Num(19,6) Gross FC
  BaseGrsSc Num(19,6) Gross SC
  ApplGrs Num(19,6) Applied Gross LC
  ApplGrsFc Num(19,6) Applied Gross FC
  ApplGrsSc Num(19,6) Applied Gross SC
  PaidGrs Num(19,6) Paid Gross LC
  PaidGrsFc Num(19,6) Paid Gross FC
  PaidGrsSc Num(19,6) Paid Gross SC
  DpApplGrs Num(19,6) Dpm Appl Gross LC
  DpApplGrsF Num(19,6) Dpm Appl Gross FC
  DpApplGrsS Num(19,6) Dpm Appl Gross SC
  RvsChrgSum Num(19,6) Reverse Charge Sum
  RvsChrgSc Num(19,6) Reverse Charge Sum (SC)
  RvsChrgFc Num(19,6) Reverse Charge Sum (FC)
  ApplRvs Num(19,6) Applied Reverse Charge Sum LC
  ApplRvsSc Num(19,6) Applied Reverse Charge Sum SC
  ApplRvsFc Num(19,6) Applied Reverse Charge Sum FC
  PaidRvs Num(19,6) Paid Reverse Charge Sum LC
  PaidRvsSc Num(19,6) Paid Reverse Charge Sum SC
  PaidRvsFc Num(19,6) Paid Reverse Charge Sum FC
  DpApplRvs Num(19,6) Dpm Applied Reverse Charge LC
  DpApplRvsS Num(19,6) Dpm Applied Reverse Charge SC
  DpApplRvsF Num(19,6) Dpm Applied Reverse Charge FC
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# SFC16 - Self Credit Memo - SnB properties
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, SnBIndex
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) abs entry ->OSFC
  LineNum Int(11) Line Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object id
  ObjAbs Int(11) Object Abs
  DrfWObjAbs Int(11) draft Wobj Abs default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type default=254000066
  LogInstanc Int(11) Log Instance

# SFC17 - Self Credit Memo - Import Process
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFC
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=254000066 ->ADP1
  ImpDocType VarChar(1) Type of Import Document ->OBSI
  ImpDocNum nVarChar(10) Importation Document Number
  DateOfReg Date(8) Date of Registry DI/DSI/DA
  CustClrDat Date(8) Date of Customs Clearance
  ConcActNum nVarChar(30) Drawback Concession Acct No.
  AdditNum nVarChar(30) Additional Number
  AddItmDV Num(19,6) Additional Item Discount Value
  tpVTransp Int(6) Overland Transport Route [1=Maritime, 2=Waterway, 3=Lakeside, 4=Air, 5=Post, 6=Train, 7=Road, 8=Network Transmission, 9=Own Means, 10=Input/Output Fictitious, 11=Courier, 12=Hand Carry]
  DrawSReg nVarChar(11) Drawback - Suspension Regime
  AddFrNavyA Num(19,6) Additional Freight to Navy Authority
  TypeOfImp VarChar(1) Type of Import
  nSeqAdic Int(6) Additional Item Sequential Number

# SFC18 - Self Credit Memo - Export Process
Module: Marketing Documents | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFC
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=254000066 ->ADP1
  ExpDocType Int(11) Type of Exportation Document default=-1 ->OBNI
  ExpDeclNum Int(11) Exportation Declaration Number
  ExpDeclDat Date(8) Exportation Declaration Date
  ExpNature Int(11) Nature of Exportation default=-1 ->OBNI
  ExpRegNum Int(11) Number of Exportation Registry
  ExpRegDate Date(8) Date of Exportation Registry
  LadBillNum nVarChar(19) Bill of Lading Number
  LadBillDat Date(8) Date of Bill of Lading
  MerchLeftD Date(8) Date Merchandise Left Customs
  LadBillTyp Int(11) Type of Bill of Lading default=-1 ->OBNI
  DrawSReg nVarChar(11) Drawback - Suspension Regime
  NatureExp nVarChar(44) Nature of Export
  QultExpItm Num(19,6) Quantity of Exported Items
  nSeqAdic Int(6) Additional Item Sequential Number

# SFC19 - Self Credit Memo - Bin Allocation Data
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, BinAllocSe
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OSFC
  BinAllocSe Int(11) Bin Allocation Sequence
  LineNum Int(11) Line Number
  SubLineNum Int(11) Subline Number default=-1
  SnBType Int(11) SnB Type default=-1
  SnBMDAbs Int(11) SnB Master Data Internal No. default=-1
  BinAbs Int(11) Bin Internal Number ->OBIN
  Quantity Num(19,6) Quantity
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjType nVarChar(20) Object Type default=254000066 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  BinActTyp Int(6) Bin Action Type [1=Transaction In, 2=Transaction Out, 4=SnB Complete, 8=Bin First Then SnB]

# SFC2 - Self Credit Memo - Freight - Rows
Module: Marketing Documents | 64 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFC
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=254000066 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) Vat Applied
  VatAppldFC Num(19,6) Vat Applied Frgn
  VatAppldSC Num(19,6) Vat Applied Sys
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report [Y=Yes, N=No]
  BaseGroup Int(11) Base Document Group default=-1 [-1=, 0=, 1=, 2=]
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1 [-1=, 0=, 1=, 2=]
  VisOrder Int(11) Visual Order
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]

# SFC20 - Intrastat Expenses
Module: Marketing Documents | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFC
  ExpnsCode Int(11) Freight Code ->OEXD
  TotalLC Num(19,6) Total
  TotalFC Num(19,6) Total (FC)
  TotalSC Num(19,6) Total (SC)
  DistribM VarChar(1) Distribution Method default=T [Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DrawnLC Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  LineNum Int(11) Line Number default=-1
  BaseAbsEnt Int(11) Base Abs. Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 16=Return, 13=Self Credit Memo, 203=Down Payment Incoming, 204=Down Payment Outgoing, 22=Purchase Order, 20=Goods Receipt PO, 21=Goods Return, 18=A/P Invoice, 540000006=Purchase Quotation, 0=, -1=]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No. default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=254000066 ->ADP1
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  AppliedLC Num(19,6) Applied
  AppliedFC Num(19,6) Applied (FC)
  AppliedSC Num(19,6) Applied (SC)

# SFC21 - Self Credit Memo - Document Reference Information
Module: Marketing Documents | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, RefType
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjectType nVarChar(20) Object Type default=254000066
  LogInstanc Int(11) Log Instance default=0
  RefType VarChar(1) Reference Types default=S [S=System Document, E=External Document]
  LineNum Int(11) Line Number
  RefDocEntr Int(11) Referenced Internal Number
  RefDocNum Int(11) Referenced Document Number
  ExtDocNum nVarChar(100) External Referenced Document Number
  RefObjType nVarChar(20) Referenced Object Type [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 234000031=Return Request, 16=Return, 203=A/R Down Payment, 13=A/R Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 280=A/R Tax Invoice, 1470000113=Purchase Request, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Return Request, 21=Goods Return, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 281=A/P Tax Invoice, 69=Landed Costs, 24=Incoming Payments, 46=Outgoing Payments, 57=Checks for Payment, 321=Internal Reconciliation, 34=Recurring Posting, 30=Journal Entry, 59=Goods Receipt, 60=Goods Issue, 162=Inventory Revaluation, 1470000065=Inventory Counting, 10000071=Inventory Posting, 1250000001=Inventory Transfer Request, 67=Inventory Transfer, 202=Production Order, 13001=Original Invoice, -1=External Document, 20301=Original Down Payment Invoice]
  AccessKey nVarChar(100) Access Key
  IssueDate Date(8) Date of Issue
  IssuerCNPJ nVarChar(100) Issuer CNPJ
  IssuerCode nVarChar(10) Fiscal Document Issuer UF Code
  Model nVarChar(6) Fiscal Document Model
  Series nVarChar(3) Fiscal Document Series
  Number Int(11) Fiscal Document Number
  RefAccKey nVarChar(100) Referenced CT-e Access Key
  RefAmount Num(19,6) Referenced Amount
  SubSeries nVarChar(3) Fiscal Document Subseries
  Remark nVarChar(254) Remarks
  LinkRefTyp nVarChar(20) Link Reference Type default=00 [00=, 01=Nota de cr�dito de los documentos relacionados, 02=Nota de d�bito de los documentos relacionados, 03=Devoluci�n de mercanc�a sobre facturas o traslados previos, 04=Sustituci�n de los CFDI previos, 05=Traslados de mercancias facturados previamente, 06=Factura generada por los traslados previos, 07=CFDI por aplicaci�n de anticipo, 08=Customs, MX_08=Factura generada por pagos en parcialidades, 09=Factura generada por pagos diferidos]

# SFC22 - Self Credit Memo - Resource Costs
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, StdCostNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->SFC1
  LineNum Int(11) Row Number
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=254000066
  LogInstanc Int(11) Log Instance default=0

# SFC23 - A/P Invoice - Selected Asset Master Data
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, VisOrder
  ASSETS: DocEntry, LineNum, AssetCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFC
  LineNum Int(11) Row Number
  AssetCode nVarChar(50) Selected Asset Code ->OITM
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Remarks nVarChar(100) Remarks
  Amount Num(19,6) Amount
  AmountSC Num(19,6) Amount (SC)
  SerialNo nVarChar(30) Serial Number
  VisOrder Int(11) Visual Order
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=254000066 ->ADP1

# SFC24 - Self Credit Memo - Tracking Note Assignment
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  ItemCCDNum nVarChar(40) Item CCD Number
  CntrOrigin nVarChar(3) Country/Region of Origin
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=254000066 ->ADP1
  SubLineNum Int(11) BOM Line No.

# SFC25 - Self Credit Memo - Amt Per VAT Grp
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, VatGroup, Type
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  VatGroup nVarChar(8) Tax Definition ->OVTG
  VatPrcnt Num(19,6) Tax Rate
  BaseAmnt Num(19,6) Base Amount
  BaseAmntFC Num(19,6) Base Amount (FC)
  BaseAmntSC Num(19,6) Base Amount (SC)
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  Type Int(11) Type default=1 [1=Discount by Tax]
  Currency nVarChar(3) Price Currency
  Rate Num(19,6) Currency Rate
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=254000066 ->ADP1

# SFC26 - Self Credit Memo - E-Way Bill Information
Module: Marketing Documents | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFC
  SuplyType nVarChar(20) EWB Transaction Type [O=Outward, I=Inward]
  SubSplyTyp Int(11) EWB Sub-Type ->OEST
  DocType nVarChar(3) EWB Doc. Type ->OEDT
  TransMode Int(11) EWB Transportation Mode ->OETM
  Distance Num(19,6) EWB Transport Distance
  TransDocNo nVarChar(16) EWB Transporter Doc. No.
  TransDate Date(8) EWB Transportation Date
  VehicleTyp nVarChar(2) EWB Vehicle Type ->OEVT
  VehicleNo nVarChar(15) EWB Vehicle Number
  EWayBillNo nVarChar(20) EWB No.
  EwbDate Date(8) E-Way Bill Date
  FrmTraName nVarChar(100) EWB Consignor Name
  FrmAddres1 nVarChar(120) EWB Consignor Address 1
  FrmAddres2 nVarChar(120) EWB Consignor Address 2
  FrmZipCode nVarChar(20) EWB Consignor Zip Code
  ActFrmStat nVarChar(2) Dispatch State of EWB Consignor
  ToTraName nVarChar(100) EWB Consignee Name
  ToAddres1 nVarChar(120) EWB Consignee Address 1
  ToAddres2 nVarChar(120) EWB Consignee Address 2
  ToZipCode nVarChar(20) EWB Consignee Zip Code
  ActToState nVarChar(2) Ship-To State of EWB Consignee
  FrmGSTN nVarChar(15) EWB Consignor GSTN
  FrmState nVarChar(2) Bill-To State of EWB Consignor
  ToGSTN nVarChar(15) EWB Consignee GSTN
  ToState nVarChar(2) Bill-To State of EWB Consignee
  MainHsnEnt Int(11) EWB Main HSN Entry ->OCHP
  FrmPlace nVarChar(50) EWB Consignor Place
  ToPlace nVarChar(50) EWB Consignee Place
  TransID nVarChar(15) EWB Transporter ID
  TransName nVarChar(25) EWB Transporter Name
  ExpireDate Date(8) EWB Expiration Date
  ObjectType nVarChar(20) Object Type default=254000066 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TspEntry Int(11) Transporter Abs. Entry ->OTSP
  TspLine Int(11) Transportation Line
  TransType Int(11) Transaction Type [1=Regular, 2=Bill To-Ship To, 3=Bill From-Dispatch From, 4=Combination of 2 and 3]

# SFC27 - Self Credit Memo - E-Books(GR) Rows
Module: Marketing Documents | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  RELATE_ROW: DocEntry, RelateType, RelateLine, GroupNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFC
  LineNum Int(11) Row Number
  RelateType Int(11) Relation Type default=-1 [1=Row, 2=Row Expenses, 3=Document Expenses, 13=Distributed Freights, -1=Manual]
  RelateLine Int(11) Relation Row Number default=-1
  GroupNum Int(11) Group Number default=-1
  LineTotal Num(19,6) Line Total
  LineTotalF Num(19,6) Line Total (FC)
  LineTotalS Num(19,6) Line Total (SC)
  InClassTyp Int(11) Income Classification Type ->OICP
  InClassCat Int(11) Income Classification Category ->OICC
  ExClassTyp Int(11) Expense Classification Type ->OECP
  ExClassCat Int(11) Expense Classification Cat. ->OECC
  VatCate Int(11) VAT Category
  NetValue Num(19,6) Net Value
  NetValueFC Num(19,6) Net Value (FC)
  NetValueSC Num(19,6) Net Value (SC)
  VatAmount Num(19,6) VAT Amount
  VatAmFC Num(19,6) VAT Amount (FC)
  VatAmSC Num(19,6) VAT Amount (SC)
  WtPercCat Int(11) Withheld Percentage Category
  WtAmount Num(19,6) Withheld Amount
  WtAmountFC Num(19,6) Withheld Amount (FC)
  WtAmountSC Num(19,6) Withheld Amount (SC)
  ObjectType nVarChar(20) Object Type default=13 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  WtCategory VarChar(1) Withheld Category [I=Invoice, P=Payment]
  VATClassTy Int(11) VAT Classification Type ->OECP
  VATClassCa Int(11) VAT Classification Category ->OECC
  EBVatExCau Int(11) VAT Exemption Cause ->OVEC

# SFC28 - Self Credit Memo - Reported Tracking Note
Module: Marketing Documents | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
  TCN_KEY U: DocEntry, LineNum, TrackingNt, TrackiNtLn
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  UnusedQty Num(19,6) Unused Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=254000066 ->ADP1
  SubLineNum Int(11) BOM Line No.

# SFC3 - Self Credit Memo - Freight
Module: Marketing Documents | 80 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  DOCUMENT: DocEntry, BaseAbsEnt
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFC
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  Comments nVarChar(100) Remarks
  ObjType nVarChar(20) Object Type default=254000066 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  WTLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  VatApplied Num(19,6) Vat Applied
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatF Num(19,6) Net Tax Amount (FC)
  LineVatS Num(19,6) Net Tax Amount (SC)
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 23=Sales Quotation, 17=Sales Order, 15=Delivery]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No.
  LineNum Int(11) line num default=-1
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Doc. Internal No. default=-1
  StDstr Num(19,6) Stock Distributed Sum
  StDstrSC Num(19,6) Stock Distributed Sum (SC)
  StDstrFC Num(19,6) Stock Distributed Sum (FC)
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  TaxDistMtd VarChar(1) Tax Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  GrsAmount Num(19,6) Gross Amount
  GrsFC Num(19,6) Gross Amount (FC)
  GrsSC Num(19,6) Gross Amount (SC)
  BaseTotal VarChar(1) Base Total for Calculation default=N [N=Net Total, G=Gross Total]
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)
  RRVatLC Num(19,6) Return Request VAT Amount
  RRVatFC Num(19,6) Return Request VAT Amount (FC)
  RRVatSC Num(19,6) Return Request VAT Amount (SC)
  EncryptIV nVarChar(100) Encrypt IV
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]

# SFC4 - Self Credit Memo - Tax Amount per Document
Module: Marketing Documents | 61 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SCONDARY: DocEntry, LineNum, GroupNum, ExpnsCode, StcCode, StaCode, staType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFC
  LineNum Int(11) Row Number default=-1
  GroupNum Int(11) Group Number default=-1
  ExpnsCode Int(11) Expense Code default=-1 ->OEXD
  RelateType Int(11) Relation Type default=1 [1=Row, 2=Row Expenses, 3=Document Expenses, 13=Distributed Freights]
  StcCode nVarChar(8) Tax Code ->OSTC
  StaCode nVarChar(8) Authority Code ->OSTA
  staType Int(11) Authority Type ->OSTT
  TaxRate Num(19,6) Tax Rate
  TaxAcct nVarChar(15) Tax Account ->OACT
  TaxSum Num(19,6) Tax Amount
  TaxSumFrgn Num(19,6) Tax Amount (FC)
  TaxSumSys Num(19,6) Tax Amount (SC)
  BaseSum Num(19,6) Base Amount
  BaseSumFrg Num(19,6) Base Amount (FC)
  BaseSumSys Num(19,6) Base Amount (SC)
  ObjectType nVarChar(20) Object Type default=254000066 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Status default=Y [Y=Normal Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) Applied Tax
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  LineSeq Int(11) Row Sequence
  DeferrAcct nVarChar(15) Deferred Tax Account ->OACT
  BaseType Int(11) Base Document Type default=-1
  BaseAbs Int(11) Base Document Internal No. default=-1
  BaseSeq Int(11) Base Doc. Row Sequence
  DeductTax Num(19,6) Deductible Tax Amount
  DdctTaxFrg Num(19,6) Deductible Tax Amount (FC)
  DdctTaxSys Num(19,6) Deductible Tax Amount (SC)
  BaseAppld Num(19,6) Applied Base Amount
  BaseApldFC Num(19,6) Applied Base Amount (FC)
  BaseApldSC Num(19,6) Applied Base Amount (SC)
  NonDdctPrc Num(19,6) Non Deductible %
  NonDdctAct nVarChar(15) Non Deductible Account ->OACT
  TaxInPrice VarChar(1) Tax Included in Price? default=N [Y=Yes, N=No]
  Exempt VarChar(1) Exempt? default=N [Y=Yes, N=No]
  TaxExpAct nVarChar(15) Expense Account for Tax ->OACT
  OnHoldTax Num(19,6) On Hold Tax Amount
  OnHoldTaxF Num(19,6) On Hold Tax Amount (FC)
  OnHoldTaxS Num(19,6) On Hold Tax Amount (SC)
  InGrossRev VarChar(1) Included in Gross Revenue default=N [Y=Yes, N=No]
  TaxSumOrg Num(19,6) Tax Amount Original
  TaxSumOrgF Num(19,6) Tax Amount Original (FC)
  TaxSumOrgS Num(19,6) Tax Amount Original (SC)
  OpenTax Num(19,6) Open Service Tax
  OpenTaxFC Num(19,6) Open Service Tax (FC)
  OpenTaxSC Num(19,6) Open Service Tax (SC)
  Unencumbrd VarChar(1) Unencumbered default=N [Y=Yes, N=No]
  TaxOnRI VarChar(1) Tax On Reserve Invoice default=N [Y=Yes, N=No]
  RvsChrgPrc Num(19,6) Reverse Charge %
  RvsChrgTax Num(19,6) Reverse Charge Tax Amount
  RvsChrgSC Num(19,6) Reverse Charge Tax Amount (SC)
  RvsChrgFC Num(19,6) Reverse Charge Tax Amount (FC)
  InFirstIns VarChar(1) Included in First Installment default=N [Y=Yes, N=No]
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CESTrel VarChar(1) CEST Relevant default=N [Y=, N=]

# SFC5 - Self Credit Memo - Withholding Tax
Module: Marketing Documents | 158 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  SECONDERY U: AbsEntry, WTCode, BaseAbsEnt, Doc1LineNo
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OSFC
  WTCode nVarChar(4) WTax Code ->OWHT
  Rate Num(19,6) Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntSC Num(19,6) Taxable Amount (SC)
  TxblAmntFC Num(19,6) Taxable Amount (FC)
  WTAmnt Num(19,6) WTax Amount
  WTAmntSC Num(19,6) WTax Amount (SC)
  WTAmntFC Num(19,6) WTax Amount (FC)
  ApplAmnt Num(19,6) Applied WTax Amount
  ApplAmntSC Num(19,6) Applied WTax Amount (SC)
  ApplAmntFC Num(19,6) Applied WTax Amount (FC)
  Category VarChar(1) Category [P=Payment, I=Invoice]
  Criteria VarChar(1) Criteria [Y=Accrual, N=Cash]
  Account nVarChar(15) G/L Account ->OACT
  Type VarChar(1) Withholding Tax Type [V=VAT Withholding, I=Income Tax Withholding]
  RoundType VarChar(1) Rounding Type [T=Truncated, C=Commercial Values, N=No Rounding]
  BaseType VarChar(1) Base Type [G=Gross, N=Net, V=VAT, U=UoM]
  BaseAbsEnt Int(11) Base Document Internal No. default=-1
  BaseLine Int(11) Base Row
  BaseNum Int(11) Base Document Type default=-1 [-1=, 0=, 23=Sales Quotation, 17=Sales Order, 15=Delivery]
  LineNum Int(11) Row Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Doc. Internal No. default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=254000066 ->ADP1
  Doc1LineNo Int(11) DOC1 Line Number default=-1
  WtLineType VarChar(1) WTax Row Type default=D [D=Document Level WTax, L=Row Level WTax]
  TxblCurr nVarChar(3) Taxable Currency from Document Line
  DtblCurr nVarChar(3) Deductible Currency
  DtblRate Num(19,6) Rate for Deductible Amount
  txblRate Num(19,6) Rate for Taxable Amount
  DtblAmount Num(19,6) Deductible Amount
  TdsAcc nVarChar(15) TDS Account ->OACT
  SurAcc nVarChar(15) Surcharge Account ->OACT
  CessAcc nVarChar(15) Cess Account ->OACT
  HscAcc nVarChar(15) HSC Account ->OACT
  TdsRate Num(19,6) TDS Rate
  SurRate Num(19,6) Surcharge Rate
  CessRate Num(19,6) Cess Rate
  HscRate Num(19,6) HSC Rate
  TdsBAmt Num(19,6) TDS Base Amount
  TdsBAmtSC Num(19,6) TDS Base Amount (SC)
  TdsBAmtFC Num(19,6) TDS Base Amount (FC)
  SurBAmt Num(19,6) Surcharge Base Amount
  SurBAmtSC Num(19,6) Surcharge Base Amount (SC)
  SurBAmtFC Num(19,6) Surcharge Base Amount (FC)
  CessBAmt Num(19,6) Cess Base Amount
  CessBAmtSC Num(19,6) Cess Base Amount (SC)
  CessBAmtFC Num(19,6) Cess Base Amount (FC)
  HscBAmt Num(19,6) HSC Base Amount
  HscBAmtSC Num(19,6) HSC Base Amount (SC)
  HscBAmtFC Num(19,6) HSC Base Amount (FC)
  TdsAmnt Num(19,6) TDS Tax Amount
  TdsAmntSC Num(19,6) TDS Tax Amount (SC)
  TdsAmntFC Num(19,6) TDS Tax Amount (FC)
  SurAmnt Num(19,6) Surcharge Tax Amount
  SurAmntSC Num(19,6) Surcharge Tax Amount (SC)
  SurAmntFC Num(19,6) Surcharge Tax Amount (FC)
  CessAmnt Num(19,6) Cess Tax Amount
  CessAmntSC Num(19,6) Cess Tax Amount (SC)
  CessAmntFC Num(19,6) Cess Tax Amount (FC)
  HscAmnt Num(19,6) HSC Tax Amount
  HscAmntSC Num(19,6) HSC Tax Amount (SC)
  HscAmntFC Num(19,6) HSC Tax Amount (FC)
  TdsAppl Num(19,6) Applied TDS Amount
  TdsApplSC Num(19,6) Applied TDS Amount (SC)
  TdsApplFC Num(19,6) Applied TDS Amount (FC)
  SurAppl Num(19,6) Applied Surcharge Amount
  SurApplSC Num(19,6) Applied Surcharge Amount (SC)
  SurApplFC Num(19,6) Applied Surcharge Amount (FC)
  CessAppl Num(19,6) Applied Cess Amount
  CessApplSC Num(19,6) Applied Cess Amount (SC)
  CessApplFC Num(19,6) Applied Cess Amount (FC)
  HscAppl Num(19,6) Applied HSC Amount
  HscApplSC Num(19,6) Applied HSC Amount (SC)
  HscApplFC Num(19,6) Applied HSC Amount (FC)
  BatchNum Int(11) Journal Voucher No.
  InCSTCode nVarChar(2) CST Code Incoming
  OutCSTCode nVarChar(2) CST Code Outgoing
  DpmWTApl Num(19,6) DPM WT Applied Amount
  DpmWTAplSC Num(19,6) DPM WT Applied Amount (SC)
  DpmWTAplFC Num(19,6) DPM WT Applied Amount (FC)
  WTTypeId Int(11) WT Type Id ->OWTT
  LnBsAmt Num(19,6) BR Line WT Base Amount
  LnBsAmtSC Num(19,6) BR Line WT Base Amount(SC)
  LnBsAmtFC Num(19,6) BR Line WT Base Amount(FC)
  LnCmTAmt Num(19,6) BR Line Cumulated Taxable Amount
  LnCmTAmtSC Num(19,6) BR Line Cumulated Taxable Amount(SC)
  LnCmTAmtFC Num(19,6) BR Line Cumulated Taxable Amount(FC)
  TDSType VarChar(1) TDS Type [E=eTDS, D=GST TDS, C=GST TCS, S=SALES TCS]
  IgstAcc nVarChar(15) IGST Account ->OACT
  CgstAcc nVarChar(15) CGST Account ->OACT
  SgstAcc nVarChar(15) SGST Account ->OACT
  IgstAmnt Num(19,6) IGST Tax Amount
  IgstAmntSC Num(19,6) IGST Tax Amount (SC)
  IgstAmntFC Num(19,6) IGST Tax Amount (FC)
  CgstAmnt Num(19,6) CGST Tax Amount
  CgstAmntSC Num(19,6) CGST Tax Amount (SC)
  CgstAmntFC Num(19,6) CGST Tax Amount (FC)
  SgstAmnt Num(19,6) SGST Tax Amount
  SgstAmntSC Num(19,6) SGST Tax Amount (SC)
  SgstAmntFC Num(19,6) SGST Tax Amount (FC)
  IgstRate Num(19,6) IGST Rate
  CgstRate Num(19,6) CGST Rate
  SgstRate Num(19,6) SGST Rate
  IgstBAmt Num(19,6) IGST Base Amount
  IgstBAmtSC Num(19,6) IGST Base Amount (SC)
  IgstBAmtFC Num(19,6) IGST Base Amount (FC)
  CgstBAmt Num(19,6) CGST Base Amount
  CgstBAmtSC Num(19,6) CGST Base Amount (SC)
  CgstBAmtFC Num(19,6) CGST Base Amount (FC)
  SgstBAmt Num(19,6) SGST Base Amount
  SgstBAmtSC Num(19,6) SGST Base Amount (SC)
  SgstBAmtFC Num(19,6) SGST Base Amount (FC)
  IgstAppl Num(19,6) Applied IGST Amount
  IgstApplSC Num(19,6) Applied IGST Amount (SC)
  IgstApplFC Num(19,6) Applied IGST Amount (FC)
  CgstAppl Num(19,6) Applied CGST Amount
  CgstApplSC Num(19,6) Applied CGST Amount (SC)
  CgstApplFC Num(19,6) Applied CGST Amount (FC)
  SgstAppl Num(19,6) Applied SGST Amount
  SgstApplSC Num(19,6) Applied SGST Amount (SC)
  SgstApplFC Num(19,6) Applied SGST Amount (FC)
  UtgstAcc nVarChar(15) UTGST Account ->OACT
  CsgstAcc nVarChar(15) Cess GST Account ->OACT
  UtgstAmt Num(19,6) UTGST Tax Amount
  UtgstAmtSC Num(19,6) UTGST Tax Amount (SC)
  UtgstAmtFC Num(19,6) UTGST Tax Amount (FC)
  CsgstAmt Num(19,6) Cess GST Tax Amount
  CsgstAmtSC Num(19,6) Cess GST Tax Amount (SC)
  CsgstAmtFC Num(19,6) Cess GST Tax Amount (FC)
  UtgstRate Num(19,6) UTGST Rate
  CsgstRate Num(19,6) Cess GST Rate
  UtgstBAmt Num(19,6) UTGST Base Amount
  UtgstBAmtS Num(19,6) UTGST Base Amount (SC)
  UtgstBAmtF Num(19,6) UTGST Base Amount (FC)
  CsgstBAmt Num(19,6) Cess GST Base Amount
  CsgstBAmtS Num(19,6) Cess GST Base Amount (SC)
  CsgstBAmtF Num(19,6) Cess GST Base Amount (FC)
  UtgstAppl Num(19,6) Applied UTGST Amount
  UtgstApplS Num(19,6) Applied UTGST Amount (SC)
  UtgstApplF Num(19,6) Applied UTGST Amount (FC)
  CsgstAppl Num(19,6) Applied Cess GST Amount
  CsgstApplS Num(19,6) Applied Cess GST Amount (SC)
  CsgstApplF Num(19,6) Applied Cess GST Amount (FC)
  EncryptIV nVarChar(100) Encrypt IV
  TcsIntAcct nVarChar(15) TCS Interim Account ->OACT
  SurIntAcct nVarChar(15) Surcharge Interim Account ->OACT
  CesIntAcct nVarChar(15) Cess Interim Account ->OACT
  HscIntAcct nVarChar(15) HSC interim Account ->OACT
  LnIntAcct nVarChar(15) Interim Account for Tax ->OACT
  FixedAmnt Num(19,6) Fixed Amount
  FixedAmtSC Num(19,6) Fixed Amount (SC)
  FixedAmtFC Num(19,6) Fixed Amount (FC)
  BaseQty Num(19,6) Base Quantity

# SFC6 - Self Credit Memo - Installments
Module: Marketing Documents | 65 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, InstlmntID
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFC
  InstlmntID Int(6) Installment ID default=1
  ObjType nVarChar(20) Object Type default=254000066 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DueDate Date(8) Due Date
  Status VarChar(1) Installment Status default=O [O=Open, C=Closed]
  DunnLevel Int(11) Dunning Level default=0
  InsTotal Num(19,6) Total Installment
  InsTotalFC Num(19,6) Total Installment (FC)
  InsTotalSy Num(19,6) Total Installment (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  VatSum Num(19,6) Total Tax
  VatSumFC Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  VatPaid Num(19,6) Tax Paid to Date
  VatPaidFC Num(19,6) Tax Paid (FC)
  VatPaidSys Num(19,6) Tax Paid (SC)
  TotalExpns Num(19,6) Total Freight Charges
  TotalExpFC Num(19,6) Total Freight Charges (FC)
  TotalExpSC Num(19,6) Total Freight Charges (SC)
  ExpAppl Num(19,6) Applied Freight Charges
  ExpApplFC Num(19,6) Applied Freight Charges (FC)
  ExpApplSC Num(19,6) Applied Freight Charges (SC)
  WTSum Num(19,6) WTax Amount
  WTSumFC Num(19,6) WTax Amount (FC)
  WTSumSC Num(19,6) WTax Amount (SC)
  WTApplied Num(19,6) Applied WTax
  WTAppliedF Num(19,6) Applied WTax (FC)
  WTAppliedS Num(19,6) Applied WTax (SC)
  TotalBlck Num(19,6) Total Reserved Amount
  TotalBlckF Num(19,6) Total Reserved Amount (FC)
  TotalBlckS Num(19,6) Total Reserved Amount (SC)
  VATBlck Num(19,6) Reserved Tax Amount
  VATBlckFC Num(19,6) Reserved Tax Amount (FC)
  VATBlckSC Num(19,6) Reserved Tax Amount (SC)
  ExpnsBlck Num(19,6) Reserved Freight Charges
  ExpnsBlckF Num(19,6) Reserved Freight Charges (FC)
  ExpnsBlckS Num(19,6) Reserved Freight Charges (SC)
  WTBlocked Num(19,6) Reserved WTax Amount
  WTBlockedF Num(19,6) Reserved WTax Amount (FC)
  WTBlockedS Num(19,6) Reserved WTax Amount (SC)
  InstPrcnt Num(19,6) Installment %
  DunWizBlck VarChar(1) Wizard dunning block default=N [N=No, Y=Yes]
  DunDate Date(8) Last Dunning Date
  Paid Num(19,6) Paid
  PaidFrgn Num(19,6) Paid (FC)
  PaidSc Num(19,6) Paid (SC)
  reserved VarChar(1) Reserved default=N [N=No, Y=Yes]
  TaxOnExp Num(19,6) Tax on Freight
  TaxOnExpFc Num(19,6) Tax on Expenses (FC)
  TaxOnExpSc Num(19,6) Tax on Expenses (SC)
  TaxOnExpAp Num(19,6) Applied Tax on Expenses
  TaxOnExApF Num(19,6) Applied Tax on Expenses (FC)
  TaxOnExApS Num(19,6) Applied Tax on Expenses (SC)
  TaxOnExBlo Num(19,6) Reserved Tax on Freight Amount
  TaxOnExBlF Num(19,6) Reserved Tax on Freight Amt FC
  TaxOnExBlS Num(19,6) Reserved Tax on Freight Amt SC
  LvlUpdDate Date(8) Dunning Level Update Date
  Ordered VarChar(1) Payment Ordered default=N [Y=Yes, N=No]
  PaidDpm Num(19,6) Paid by Down Payment
  PaidDpmFc Num(19,6) Paid by Down Payment (FC)
  PaidDpmSc Num(19,6) Paid by Down Payment (SC)
  EncryptIV nVarChar(100) Encrypt IV

# SFC7 - Self Credit Memo - Delivery Packages
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFC
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type default=254000066 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV

# SFC8 - Self Credit Memo - Items in Package
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum, ItemCode, UomEntry, NumPerMsr
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFC
  PackageNum Int(11) Package Number
  ItemCode nVarChar(50) Item Code ->OITM
  Quantity Num(19,6) Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=254000066 ->ADP1
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value default=0

# SFC9 - Self Credit Memo - Drawn Down Payment
Module: Marketing Documents | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFC
  LineNum Int(11) Row Number
  BaseAbs Int(11) Base Document Internal ID ->ODPI
  BaseLine Int(11) Base Document Row
  TargetBase VarChar(1) Target or Base Document default=T [B=Base, T=Target]
  ObjType nVarChar(20) Base Object Type default=203 [203=A/R Down Payment]
  DrawnSum Num(19,6) Net LC
  DrawnSumFc Num(19,6) Net FC
  DrawnSumSc Num(19,6) Net SC
  LogInstanc Int(11) Log Instance default=0
  ObjCode nVarChar(20) Object Type default=254000066 ->ADP1
  ApplDrawn Num(19,6) Applied Net LC
  ApplDrawnF Num(19,6) Applied Net FC
  ApplDrawnS Num(19,6) Applied Net SC
  BaseDocNum Int(11) Base Document Number
  BsDocDate Date(8) Base Posting Date
  BsDueDate Date(8) Base Due Date
  BsCardName nVarChar(100) Base BP Name
  BsComments nVarChar(254) Base Remarks
  Posted VarChar(1) Base Document Posted default=Y [Y=Yes, N=No]
  Vat Num(19,6) Tax LC
  VatFc Num(19,6) Tax FC
  VatSc Num(19,6) Tax SC
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  IsGross VarChar(1) Is Gross Line default=N [N=Net Line, Y=Gross Line]

# SFI1 - Self Invoice - Rows
Module: Marketing Documents | 317 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  STATUS: LineStatus
  CURRENCY: Currency
  ACCOUNT: AcctCode
  BASE_ENTRY: BaseEntry, BaseType, BaseLine
  VIS_ORDER: DocEntry, VisOrder
  OWNER_CODE: OwnerCode
  ITM_WHS_OQ: ItemCode, WhsCode, OpenQty
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFI
  LineNum Int(11) Row Number
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=, 14=A/R Credit Note, 15=Delivery, 165=A/R Correction Invoice]
  TrgetEntry Int(11) Target Document Internal ID
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 18=A/P Invoice, 19=A/P Credit Memo, 254000065=Self Invoice]
  BaseEntry Int(11) Base Document Internal ID
  BaseLine Int(11) Base Row
  LineStatus VarChar(1) Row Status default=O [O=Open, C=Closed]
  ItemCode nVarChar(50) Item No. ->OITM
  Dscription nVarChar(200) Item/Service Description
  Quantity Num(19,6) Quantity
  ShipDate Date(8) Row Delivery Date
  OpenQty Num(19,6) Remaining Open Quantity
  Price Num(19,6) Price after Discount
  Currency nVarChar(3) Price Currency ->OCRN
  Rate Num(19,6) Currency Rate
  DiscPrcnt Num(19,6) Discount % per Row
  LineTotal Num(19,6) Row Total
  TotalFrgn Num(19,6) Row Total (FC)
  OpenSum Num(19,6) Open Amount
  OpenSumFC Num(19,6) Open Amount (FC)
  VendorNum nVarChar(50) Vendor Catalog No.
  SerialNum nVarChar(17) Serial Number
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  SlpCode Int(11) Sales Employee Code default=-1 ->OSLP
  Commission Num(19,6) Commission Percentage
  TreeType VarChar(1) BOM Type default=N [N=Not a BOM, A=Assembly, S=Sales, I=Sales BOM Component, P=Production, T=Template]
  AcctCode nVarChar(15) Account Code ->OACT
  TaxStatus VarChar(1) Tax Definition [Y=Yes, N=No]
  GrossBuyPr Num(19,6) Gross Profit Base Price
  PriceBefDi Num(19,6) Unit Price
  DocDate Date(8) Posting Date
  Flags Int(11) Flags default=0
  OpenCreQty Num(19,6) Credit Memo Amount
  UseBaseUn VarChar(1) Inventory UoM default=N [Y=Yes, N=No]
  SubCatNum nVarChar(50) BP Catalog No. ->OSCN
  BaseCard nVarChar(15) Base BP Code ->OCRD
  TotalSumSy Num(19,6) Row Total (SC)
  OpenSumSys Num(19,6) Open Amount (SC)
  InvntSttus VarChar(1) Warehouse Status default=O [O=Open, C=Closed]
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  CodeBars nVarChar(254) Bar Code
  VatPrcnt Num(19,6) Tax Rate per Row
  VatGroup nVarChar(8) Tax Definition ->OVTG
  PriceAfVAT Num(19,6) Gross Price after Discount
  Height1 Num(19,6) Height 1
  Hght1Unit Int(6) Unit of Height 1
  Height2 Num(19,6) Height 2
  Hght2Unit Int(6) Unit of Height 2
  Width1 Num(19,6) Width 1
  Wdth1Unit Int(6) Unit of Width 1
  Width2 Num(19,6) Width 2
  Wdth2Unit Int(6) Unit of Width 2
  Length1 Num(19,6) Length 1
  Len1Unit Int(6) Unit of Length 1
  length2 Num(19,6) Length 2
  Len2Unit Int(6) Unit of Length 2
  Volume Num(19,6) Volume
  VolUnit Int(6) Vol. Unit
  Weight1 Num(19,6) Weight 1
  Wght1Unit Int(6) Unit of Weight 1
  Weight2 Num(19,6) Weight 2
  Wght2Unit Int(6) Unit of Weight 2
  Factor1 Num(19,6) Factor 1
  Factor2 Num(19,6) Factor 2
  Factor3 Num(19,6) Factor 3
  Factor4 Num(19,6) Factor 4
  PackQty Num(19,6) Packing Quantity
  UpdInvntry VarChar(1) Whse Update default=Y [Y=Yes, N=No]
  BaseDocNum Int(11) Base Document No.
  BaseAtCard nVarChar(100) Customer/Vendor Base Document
  SWW nVarChar(16) Additional Identifier
  VatSum Num(19,6) Total Tax
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  FinncPriod Int(11) Posting Period ->OFPR
  ObjType nVarChar(20) Object Type default=254000065 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BlockNum nVarChar(100) Block Number
  ImportLog nVarChar(20) Import Log
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAqcuistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  DistribSum Num(19,6) Distributed Amount
  DstrbSumFC Num(19,6) Distributed Amount (FC)
  DstrbSumSC Num(19,6) Distributed Amount (SC)
  GrssProfit Num(19,6) Row Gross Profit
  GrssProfSC Num(19,6) Row Gross Profit (SC)
  GrssProfFC Num(19,6) Row Gross Profit (FC)
  VisOrder Int(11) Visual Order
  INMPrice Num(19,6) Item's Last Sales Price (OINM)
  PoTrgNum Int(11) PO Target No.
  PoTrgEntry nVarChar(11) PO Target Internal ID
  DropShip VarChar(1) Drop-Ship default=N [Y=Yes, N=No]
  PoLineNum Int(11) PO Target Row No.
  Address nVarChar(254) Address
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type [Y=Regular Tax, N=No Tax, U=Use Tax]
  OrigItem nVarChar(50) Original Item ->OITM
  BackOrdr VarChar(1) Allow Backorder [Y=Yes, N=No]
  FreeTxt nVarChar(100) Free Text
  PickStatus VarChar(1) Pick Status default=N [Y=Picked, N=Not Picked, R=Released for Picking, P=Partially Picked]
  PickOty Num(19,6) Pick Quantity
  PickIdNo Int(11) Pick ID
  TrnsCode Int(6) Shipping Method default=-1 ->OSHP
  VatAppld Num(19,6) Applied Tax
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  BaseQty Num(19,6) Base Quantity
  BaseOpnQty Num(19,6) Base Open Quantity
  VatDscntPr Num(19,6) Tax Discount %
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  DeferrTax VarChar(1) Deferred Tax default=N [Y=Yes, N=No]
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatlF Num(19,6) Net Tax Amount (FC)
  LineVatS Num(19,6) Net Tax Amount (SC)
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value
  CEECFlag VarChar(1) Correction Invoice Was/Should Be default=S [W=Was, S=Should Be]
  ToStock Num(19,6) Corr. Invoice Amt to Inventory
  ToDiff Num(19,6) Corr. Invoice Amount to Diff.
  ExciseAmt Num(19,6) Excise Amount
  TaxPerUnit Num(19,6) Tax per Unit
  TotInclTax Num(19,6) Total Including Tax
  CountryOrg nVarChar(3) Country/Region of Origin
  StckDstSum Num(19,6) Stock Distribution Sum
  ReleasQtty Num(19,6) Released Quantity
  LineType VarChar(1) Row Type default=R [R=Regular]
  TranType VarChar(1) Transaction Type [C=Complete, R=Reject]
  Text Text(16) Text
  OwnerCode Int(11) Document Owner
  StockPrice Num(19,6) Item Cost
  ConsumeFCT VarChar(1) Consumer Sales Forecast [Y=Yes, N=No]
  LstByDsSum Num(19,6) Last Buy Distribute Sum
  StckINMPr Num(19,6) Stock Inm Price
  LstBINMPr Num(19,6) Last Buy Inventory Journal Pr.
  StckDstFc Num(19,6) Stock Distribution Sum (FC)
  StckDstSc Num(19,6) Stock Distribution Sum (SC)
  LstByDsFc Num(19,6) Last Buy Distribute Sum (FC)
  LstByDsSc Num(19,6) Last Buy Distribute Sum (SC)
  StockSum Num(19,6) Stock Sum
  StockSumFc Num(19,6) Stock Sum FC
  StockSumSc Num(19,6) Stock Sum SC
  StckSumApp Num(19,6) Stock Sum Applied
  StckAppFc Num(19,6) Stock Sum Applied FC
  StckAppSc Num(19,6) Stock Sum Applied SC
  ShipToCode nVarChar(50) Ship-to Code
  ShipToDesc nVarChar(254) Ship-to Description
  StckAppD Num(19,6) Stock Distrib. - Applied Sum
  StckAppDFC Num(19,6) Stock Dist. - Applied Sum (FC)
  StckAppDSC Num(19,6) Stock Dist. - Applied Sum (SC)
  BasePrice VarChar(1) Price for Total Calculation default=E [E=Exclude Tax, I=Include Tax]
  GTotal Num(19,6) Gross Total
  GTotalFC Num(19,6) Gross Total (FC)
  GTotalSC Num(19,6) Gross Total (SC)
  DistribExp VarChar(1) Distribute Freight Charges [Y=Yes, N=No]
  DescOW VarChar(1) Description overwritten default=N [Y=Yes, N=No]
  DetailsOW VarChar(1) Remarks overwritten default=N [Y=Yes, N=No]
  GrossBase Int(6) Base Method for Gross Profit
  VatWoDpm Num(19,6) Tax Before DPM Applied
  VatWoDpmFc Num(19,6) Tax Before DPM Applied (FC)
  VatWoDpmSc Num(19,6) Tax Before DPM Applied (SC)
  CFOPCode nVarChar(6) CFOP Code for Document ->OCFP
  CSTCode nVarChar(6) CST Code for ICMS
  Usage Int(11) Usage Code for Document ->OUSG
  TaxOnly VarChar(1) Tax Only [Y=Yes, N=No]
  WtCalced VarChar(1) Withholding Tax Calculated default=N [N=No, Y=Yes]
  QtyToShip Num(19,6) Quantity to Ship
  DelivrdQty Num(19,6) Delivered Quantity
  OrderedQty Num(19,6) Ordered Quantity
  CogsOcrCod nVarChar(8) COGS Distribution Rule Code ->OOCR
  CiOppLineN Int(11) Row Number of Associated Row default=-1
  CogsAcct nVarChar(15) COGS Account Code ->OACT
  ChgAsmBoMW VarChar(1) Change Whs for Asm BoM Child [Y=Yes, N=No]
  ActDelDate Date(8) Actual Delivery Date
  OcrCode2 nVarChar(8) Costing Code 2 ->OOCR
  OcrCode3 nVarChar(8) Costing Code 3 ->OOCR
  OcrCode4 nVarChar(8) Costing Code 4 ->OOCR
  OcrCode5 nVarChar(8) Costing Code 5 ->OOCR
  TaxDistSum Num(19,6) Tax Distributed Amount
  TaxDistSFC Num(19,6) Tax Distributed Amount (FC)
  TaxDistSSC Num(19,6) Tax Distributed Amount (SC)
  PostTax VarChar(1) Post Tax in Price to Stock default=Y [Y=Yes, N=No]
  Excisable VarChar(1) Excisable [Yes/No] [Y=Yes, N=No]
  AssblValue Num(19,6) Assessable Value
  RG23APart1 Int(11) RG23A Part1 Number
  RG23APart2 Int(11) RG23A Part2 Number
  RG23CPart1 Int(11) RG23C Part1 Number
  RG23CPart2 Int(11) RG23C Part2 Number
  CogsOcrCo2 nVarChar(8) COGS Distribution Rule Code2 ->OOCR
  CogsOcrCo3 nVarChar(8) COGS Distribution Rule Code3 ->OOCR
  CogsOcrCo4 nVarChar(8) COGS Distribution Rule Code4 ->OOCR
  CogsOcrCo5 nVarChar(8) COGS Distribution Rule Code5 ->OOCR
  LnExcised VarChar(1) Line Excised [O=Open, C=Closed, P=Copied to OEI]
  LocCode Int(11) Location Code ->OLCT
  StockValue Num(19,6) Total COGS Value
  GPTtlBasPr Num(19,6) Total Base Price for Profit
  unitMsr2 nVarChar(100) Pur/Sal UoM if BaseUnit
  NumPerMsr2 Num(19,6) Pur/Sal UoM Value if Base Unit
  SpecPrice VarChar(1) Price Source Type default=N [Y=Special Prices for Business Partner, N=Manual, W=Active Price List, Discount Groups, R=Active Price List, U=Inactive Price List, A=Blanket Agreement, P=Period and Volume Discounts, Q=Period and Volume Discounts, Discount Groups, V=Inactive Price List, Discount Groups, 9=Special Prices for Business Partner, !=Blanket Agreement, 0=Period and Volume Discounts, 1=Period and Volume Discounts, Discount Groups, 2=Active Price List, 7=Active Price List, Discount Groups, 5=Inactive Price List, 6=Inactive Price List, Discount Groups]
  CSTfIPI nVarChar(2) CST for IPI Code
  CSTfPIS nVarChar(2) CST for PIS Code
  CSTfCOFINS nVarChar(2) CST for COFINS Code
  ExLineNo nVarChar(10) ExLineNo
  isSrvCall VarChar(1) Created from Service Call default=N [Y=Yes, N=No]
  PQTReqQty Num(19,6) Pur Quotation: Required Qty
  PQTReqDate Date(8) Pur Quotation: Required Date
  PcDocType Int(11) Purchase Confirmation Doc Type default=-1 [-1=No Type, 22=Purchase Order, 540000006=Purchase Quotation]
  PcQuantity Num(19,6) Purchase Confirmation Quantity
  LinManClsd VarChar(1) Line Was Closed Manually default=N [Y=Yes, N=No, U=Unknown]
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  NoInvtryMv VarChar(1) Without Inventory Movement default=N [Y=Yes, N=No]
  ActBaseEnt Int(11) Actual Base Document Entry
  ActBaseLn Int(11) Actual Base Line Number
  ActBaseNum Int(11) Actual Base Document No.
  OpenRtnQty Num(19,6) Quantity Open for Return
  AgrNo Int(11) Agreement No. ->OOAT
  AgrLnNum Int(11) Agreement Row Number
  CredOrigin VarChar(1) Credit Origin ->OBSI
  Surpluses Num(19,6) Surpluses
  DefBreak Num(19,6) Defect and Breakup
  Shortages Num(19,6) Shortages
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  UomEntry2 Int(11) UoM Entry if Base Unit default=0 ->OUOM
  UomCode nVarChar(20) UoM Code
  UomCode2 nVarChar(20) UoM Code if Base Unit
  FromWhsCod nVarChar(8) From Warehouse Code ->OWHS
  NeedQty VarChar(1) Consider Quantity of Items default=N [Y=Yes, N=No]
  PartRetire VarChar(1) Partial Retirement default=N [Y=Yes, N=No]
  RetireQty Num(19,6) Retirement Quantity
  RetireAPC Num(19,6) Retirement APC
  RetirAPCFC Num(19,6) Retirement APC FC
  RetirAPCSC Num(19,6) Retirement APC SC
  InvQty Num(19,6) Quantity - Inventory UoM
  OpenInvQty Num(19,6) Open Quantity (Inventory UoM)
  EnSetCost VarChar(1) Enable Set Item Cost in Return default=N [Y=Yes, N=No]
  RetCost Num(19,6) Return Cost in A/R Return
  Incoterms Int(11) Incoterms default=0 ->ODCI
  TransMod Int(11) Transport Mode default=0 ->ODCI
  LineVendor nVarChar(15) Line Vendor Code ->OCRD
  DistribIS VarChar(1) Distribute Intrastat Freight default=N [Y=Yes, N=No]
  ISDistrb Num(19,6) Intrastat Distrib. Amount
  ISDistrbFC Num(19,6) Intrastat Distrib. Amount (FC)
  ISDistrbSC Num(19,6) Intrastat Distrib. Amount (SC)
  IsByPrdct VarChar(1) Item Is By-Product default=N [N=No, Y=Yes]
  ItemType Int(11) Item Type default=4 [4=Item]
  PriceEdit VarChar(1) Price Was Edited by User default=N [N=No, Y=Yes]
  PrntLnNum Int(11) Parent Line Number
  LinePoPrss VarChar(1) Line PO Process default=N [Y=Yes, N=No]
  FreeChrgBP VarChar(1) Free of Charge (BP) default=N [Y=Yes, N=No]
  TaxRelev VarChar(1) Tax Relevant Row default=Y [Y=Yes, N=No]
  LegalText nVarChar(254) Legal Text
  ThirdParty VarChar(1) Third Party default=N [Y=Yes, N=No]
  LicTradNum nVarChar(32) Federal Tax ID
  InvQtyOnly VarChar(1) Change Qty (Inv. UoM) Only default=N [Y=Yes, N=No]
  UnencReasn Int(11) Reason for Unencumbered ICMS
  ShipFromCo nVarChar(50) Ship-from Code
  ShipFromDe nVarChar(254) Ship-from Description
  FisrtBin nVarChar(228) First Bin Location
  AllocBinC nVarChar(11) Allocated Bin Location Count
  ExpType nVarChar(4) Expense Type ->OEXD
  ExpUUID nVarChar(50) Expense UUID
  ExpOpType VarChar(1) Expense Operation Type [P=Professional Services, R=Renting Assets, O=Others]
  DIOTNat nVarChar(3) DIOT Nationality ->OCRY
  MYFtype nVarChar(2) MYF type [S1=MYF Wholesale Sales, S2=Retail Sales, P1=MYF Wholesale Purchases, P3=Other Expense Transactions]
  GPBefDisc Num(19,6) Gross Price
  ReturnRsn Int(6) Return Reason default=-1
  ReturnAct Int(6) Return Action default=-1
  StgSeqNum Int(11) Stage Sequence Number
  StgEntry Int(11) Stage Entry ->ORST
  StgDesc nVarChar(100) Stage Description
  ItmTaxType nVarChar(2) Item GST Tax Category [GR=GST Regular, GN=GST Nil Rated, GE=GST Exempt, NE=Excisable, NN=Non-GST Non-Excisable]
  SacEntry Int(11) SAC Entry ->OSAC
  NCMCode Int(11) NCM Code default=-1 ->ONCM
  HsnEntry Int(11) HSN Entry ->OCHP
  OriBAbsEnt Int(11) Original Base Document Internal ID
  OriBLinNum Int(11) Original Base Document Line Number
  OriBDocTyp Int(11) Original Base Document Type
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No, U=Use]
  EncryptIV nVarChar(100) Encrypt IV
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  StdItemId Int(11) Standard Item Identification ->OUNCL
  CommClass Int(11) Commodity Classification ->OUNCL
  VatExEntry Int(11) VAT Exemption AbsEntry ->OVEB
  VatExLN Int(6) VAT Exemption LineNum
  NatOfTrans Int(11) Nature of Transaction ->ODCI
  ISDtCryImp nVarChar(3) Destination Country/Region for Import ->OCRY
  ISDtRgnImp Int(11) Destination Region for Import ->ODCI
  ISOrCryExp nVarChar(3) Country/Region of Origin for Export ->OCRY
  ISOrRgnExp Int(11) Region of Origin for Export ->ODCI
  NVECode nVarChar(6) NVE Code
  PoNum nVarChar(20) Customer's Purchase Order Number
  PoItmNum Int(11) Customer's Purchase Order Item Number
  IndEscala VarChar(1) Indicator for Relevant Scale default=N [Y=Yes, N=No]
  CESTCode Int(11) CEST Code ->OCEST
  CtrSealQty Num(19,6) Control Seal Quantity
  CNJPMan nVarChar(14) CNPJ of Manufacturer
  UFFiscBene nVarChar(10) UF Fiscal Benefit Code
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]
  LegalTIMD nVarChar(250) Legal Text from Item Master Data
  LegalTTCA nVarChar(250) Legal Text from Tax Code Attributes
  LegalTW nVarChar(250) Legal Text from Warehouse
  LegalTCD nVarChar(250) Legal Text from Tax Code Determination
  RevCharge VarChar(1) Reverse Charge default=N [Y=Yes, N=No]
  ListNum Int(6) Price List No. ->OPLN

# SFI10 - Self Invoice - Row Structure
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SECONDERY U: DocEntry, AftLineNum, OrderNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFI
  LineSeq Int(11) Row Sequence
  AftLineNum Int(11) After Row Number
  OrderNum Int(11) Order Number
  LineType VarChar(1) Row Type [T=Text, S=Subtotal]
  LineText Text(16) Row Text
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=254000065 ->ADP1

# SFI11 - Self Invoice - Drawn Down Payment Detail
Module: Marketing Documents | 70 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LineSeq
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFI
  LineNum Int(11) Row Number
  LineSeq Int(11) Sequence Number
  BaseAbs Int(11) Base Document Internal ID
  BaseType Int(11) Base Object Type default=-1
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  VatPrcnt Num(19,6) VAT Percent
  LineTotal Num(19,6) Net LC
  TotalFrgn Num(19,6) Net FC
  TotalSumSy Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFrgn Num(19,6) Tax FC
  VatSumSys Num(19,6) Tax SC
  ObjType nVarChar(20) Object Type default=254000065 ->ADP1
  LogInstanc Int(11) Log Instance
  IsAcq VarChar(1) Acquisition Tax Liable default=N [N=No, Y=Yes]
  IsAllDrawn VarChar(1) Remaining Amount Drawn default=N [Y=Yes, N=No]
  IsGross VarChar(1) Is Gross Line default=N [N=Net Line, Y=Gross Line]
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  ApplNet Num(19,6) Applied Net LC
  ApplNetFc Num(19,6) Applied Net FC
  ApplNetSc Num(19,6) Applied Net SC
  ApplVat Num(19,6) Applied Tax (LC)
  ApplVatFc Num(19,6) Applied Tax (FC)
  ApplVatSc Num(19,6) Applied Tax (SC)
  BaseNet Num(19,6) Base Net LC
  BaseNetFc Num(19,6) Base Net FC
  BaseNetSc Num(19,6) Base Net SC
  BaseVat Num(19,6) Base Tax LC
  BaseVatFc Num(19,6) Base Tax FC
  BaseVatSc Num(19,6) Base Tax SC
  BaseGross Num(19,6) Base Gross LC
  BaseGrossF Num(19,6) Base Gross FC
  BaseGrossS Num(19,6) Base Gross SC
  LineType VarChar(1) Line Type default=D [D=Document Row, R=Currency Rounding, H=Down Payment Document Rounding]
  DctSum Num(19,6) Deductible Sum LC
  DctSumFc Num(19,6) Deductible Sum FC
  DctSumSc Num(19,6) Deductible Sum SC
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplDct Num(19,6) Applied Deductible Sum LC
  ApplDctFc Num(19,6) Applied Deductible Sum FC
  ApplDctSc Num(19,6) Applied Deductible Sum SC
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  BaseDct Num(19,6) Base Deductible Sum LC
  BaseDctFc Num(19,6) Base Deductible Sum FC
  BaseDctSc Num(19,6) Base Deductible Sum SC
  BaseEq Num(19,6) Base Equalization Sum LC
  BaseEqFc Num(19,6) Base Equalization Sum FC
  BaseEqSc Num(19,6) Base Equalization Sum SC
  TaxCode nVarChar(8) Tax Code ->OSTC
  ApplGross Num(19,6) Applied Gross LC
  ApplGrossF Num(19,6) Applied Gross FC
  ApplGrossS Num(19,6) Applied Gross SC
  TaxAdjust VarChar(1) Manual Tax Adjustment default=N [Y=Yes, N=No]
  RvsChrgSum Num(19,6) Reverse Charge Sum LC
  RvsChrgFc Num(19,6) Reverse Charge Sum FC
  RvsChrgSc Num(19,6) Reverse Charge Sum SC
  BasRvsChrg Num(19,6) Base Reverse Charge LC
  BasRvsFc Num(19,6) Base Reverse Charge FC
  BasRvsSc Num(19,6) Base Reverse Charge SC
  ApplRvs Num(19,6) Applied Reverse Charge LC
  ApplRvsFc Num(19,6) Applied Reverse Charge FC
  ApplRvsSc Num(19,6) Applied Reverse Charge SC
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# SFI12 - Self Invoice - Tax Extension
Module: Marketing Documents | 117 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFI
  TaxId0 nVarChar(100) Tax ID 0
  TaxId1 nVarChar(100) Tax ID 1
  TaxId2 nVarChar(100) Tax ID 2
  TaxId3 nVarChar(100) Tax ID 3
  TaxId4 nVarChar(100) Tax ID 4
  TaxId5 nVarChar(100) Tax ID 5
  TaxId6 nVarChar(100) Tax ID 6
  TaxId7 nVarChar(100) Tax ID 7
  TaxId8 nVarChar(100) Tax ID 8
  TaxId9 nVarChar(100) Tax ID 9
  State nVarChar(3) State Code
  County nVarChar(7) County Code
  Incoterms nVarChar(3) Incoterms
  Vehicle nVarChar(10) Vehicle ID
  VidState nVarChar(3) Vehicle State ID
  NfRef nVarChar(254) NF Reference
  Carrier nVarChar(15) Carrier Code ->OCRD
  QoP Int(11) Quantity of Packs
  PackDesc nVarChar(10) Pack Description
  Brand nVarChar(20) Brand
  NoSU Int(11) Number of Shipping Unit
  NetWeight Num(19,6) Net Weight
  GrsWeight Num(19,6) Gross Weight
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=254000065 ->ADP1
  TaxId10 nVarChar(100) Tax ID 10
  TransCat nVarChar(100) Transaction Category
  FormNo nVarChar(100) Form No.
  TaxId11 nVarChar(100) Tax ID 11
  StreetS nVarChar(100) Street
  BlockS nVarChar(100) Block
  BuildingS Text(16) Building/Floor/Room
  CityS nVarChar(100) City
  ZipCodeS nVarChar(20) Zip Code
  CountyS nVarChar(100) County
  StateS nVarChar(3) State ->OCST
  CountryS nVarChar(3) Country/Region ->OCRY
  AddrTypeS nVarChar(100) Address Type
  StreetNoS nVarChar(100) Street No.
  StreetB nVarChar(100) Street
  BlockB nVarChar(100) Block
  BuildingB Text(16) Building/Floor/Room
  CityB nVarChar(100) City
  ZipCodeB nVarChar(20) Zip Code
  CountyB nVarChar(100) County
  StateB nVarChar(3) State ->OCST
  CountryB nVarChar(3) Country/Region ->OCRY
  AddrTypeB nVarChar(100) Address Type
  StreetNoB nVarChar(100) Street No.
  ImpORExp VarChar(1) Import or Export [N=, Y=]
  Vat VarChar(1) VAT default=N [N=No VAT Support, Y=VAT Support]
  AltCrdNamB nVarChar(100) Alternative BP Name
  AltTaxIdB nVarChar(32) Alternative Tax ID
  Address2S nVarChar(50) Address Name 2
  Address3S nVarChar(50) Address Name 3
  Address2B nVarChar(50) Address Name 2
  Address3B nVarChar(50) Address Name 3
  MainUsage Int(11) Main Usage Code of Document ->OUSG
  GlbLocNumS nVarChar(50) Global Location Number
  GlbLocNumB nVarChar(50) Global Location Number
  CollectDT nVarChar(20) Date and Time of Collection
  TransprtDT Date(8) Transport Start Date
  TransprtRS nVarChar(100) Transport Reason
  TaxId12 nVarChar(50) Tax ID 12
  TaxId13 nVarChar(100) Deductee Ref. No. in India
  ImpExpNo nVarChar(100) Import/Export Bill No.
  ImpExpDate Date(8) Import/Export Date
  BpGSTType Int(11) GST Regn Type of BP
  BpGSTN nVarChar(15) GST Regn No of BP
  BpStateCod nVarChar(3) State Code of Business Partner ->OCST
  BPStatGSTN nVarChar(2) GST State Code of BP
  LocGSTType Int(11) GST Regn Type of Location
  LocGSTN nVarChar(15) GST Regn No of Location
  LocStatCod nVarChar(3) State Code of Location ->OCST
  LocStaGSTN nVarChar(2) GST State Code of Location
  BpCountry nVarChar(3) Country/Region Code of BP ->OCRY
  OrigImpNo nVarChar(100) Original Bill of Entry No.
  OrigImpDat Date(8) Original Bill of Entry Date
  ExportType VarChar(1) Exporting Type default=E [E=Imports/Exports, S=SEZ Developer, U=SEZ Unit, D=Deemed Imports/Exports]
  PortCode nVarChar(100) Port Code
  BoEValue Num(19,6) Bill of Entry Value
  IsIGSTAct VarChar(1) Supply under IGST Account [Y=Yes, N=No]
  ClaimRefun VarChar(1) Claim Refund [Y=Yes, N=No]
  TaxRateDif Int(11) Differential % of Tax Rate [65=, 100=]
  BPGdsIssP nVarChar(15) Goods Issue Place BP
  CNPJGIP nVarChar(100) Goods Issue Place CNPJ
  CPFGIP nVarChar(100) Goods Issue Place CPF
  StreetGIP nVarChar(100) Goods Issue Place Street
  StrtNoGIP nVarChar(100) Goods Issue Place Street No.
  BldngGIP Text(16) Goods Issue Place Building
  ZipGIP nVarChar(20) Goods Issue Place Zip Code
  BlockGIP nVarChar(100) Goods Issue Place Block
  CityGIP nVarChar(100) Goods Issue Place City
  CountyGIP nVarChar(100) Goods Issue Place County
  StateGIP nVarChar(3) Goods Issue Place State ->OCST
  CountryGIP nVarChar(3) Goods Issue Place Country/Region ->OCRY
  PhoneGIP nVarChar(20) Goods Issue Place Phone
  EMailGIP nVarChar(100) Goods Issue Place E-Mail
  DptDateGIP Date(8) Goods Issue Place Departure Date
  BPDelivryP nVarChar(15) Delivery Place BP
  CNPJDlvryP nVarChar(100) Delivery Place CNPJ
  CPFDlvryP nVarChar(100) Delivery Place CPF
  StrtDlvryP nVarChar(100) Delivery Place Street
  StrNoDlvrP nVarChar(100) Delivery Place Street No.
  BldDlvryP Text(16) Delivery Place Building
  ZipDlvryP nVarChar(20) Delivery Place Zip Code
  BlckDlvryP nVarChar(100) Delivery Place Block
  CityDlvryP nVarChar(100) Delivery Place City
  CntyDlvryP nVarChar(100) Delivery Place County
  StatDlvryP nVarChar(3) Delivery Place State ->OCST
  CtryDlvryP nVarChar(3) Delivery Place Country/Region ->OCRY
  FoneDlvryP nVarChar(20) Delivery Place Phone
  MailDlvryP nVarChar(100) Delivery Place E-Mail
  DpDtDlvryP Date(8) Delivery Place Departure Date
  AuthedCNPJ nVarChar(250) Authorized CNPJ or CPF
  TaxId14 nVarChar(250) ITR Filing

# SFI13 - Self Invoice Rows - Distributed Freights
Module: Marketing Documents | 59 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFI
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=254000065 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Aquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Normal Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) VAT Applied (FC)
  VatAppldSC Num(19,6) VAT Applied (SC)
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock default=N [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Line No.
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Abs. Entry default=-1
  BaseGroup Int(11) Base Document Group default=-1
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1
  VisOrder Int(11) Visual Order
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DistribExp VarChar(1) Distribute Freights [Y=Yes, N=No]
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ

# SFI14 - Self Invoice - Assembly - Rows
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFI
  LineNum Int(11) Row Number default=-1
  ChildNum Int(11) Child Number default=-1
  ItemCode nVarChar(50) Item no. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  TotalQty Num(19,6) Total Quantity
  OpenQty Num(19,6) Remaining Open Quantity
  ObjectType nVarChar(20) object type default=254000065 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BaseChildN Int(11) Base Child Number default=-1
  EncryptIV nVarChar(100) Encrypt IV

# SFI15 - Self Invoice - Drawn Down Payment Applied
Module: Marketing Documents | 84 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFI
  LineNum Int(11) Row Number
  ObjType nVarChar(20) object type default=254000065 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  StaCode nVarChar(8) Tax Authority Code
  StaType Int(11) Tax Authority Type
  StaIndex Int(11) Tax Authority Seq Index
  BaseNet Num(19,6) Net LC
  BaseNetFc Num(19,6) Net FC
  BaseNetSc Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFc Num(19,6) Tax FC
  VatSumSc Num(19,6) Tax SC
  DctSum Num(19,6) Deductible Sum LC
  DctSumFc Num(19,6) Deductible Sum FC
  DctSumSc Num(19,6) Deductible Sum SC
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplNet Num(19,6) Applied Net LC
  ApplNetFc Num(19,6) Applied Net FC
  ApplNetSc Num(19,6) Applied Net SC
  ApplVat Num(19,6) Applied Tax (LC)
  ApplVatFc Num(19,6) Applied Tax (FC)
  ApplVatSc Num(19,6) Applied Tax (SC)
  ApplDct Num(19,6) Applied Deductible Sum LC
  ApplDctFc Num(19,6) Applied Deductible Sum FC
  ApplDctSc Num(19,6) Applied Deductible Sum SC
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  PaidNet Num(19,6) Paid Net LC
  PaidNetFc Num(19,6) Paid Net FC
  PaidNetSc Num(19,6) Paid Net SC
  PaidVat Num(19,6) Paid Tax LC
  PaidVatFc Num(19,6) Paid Tax FC
  PaidVatSc Num(19,6) Paid Tax SC
  PaidDct Num(19,6) Paid Deductible Sum LC
  PaidDctFc Num(19,6) Paid Deductible Sum FC
  PaidDctSc Num(19,6) Paid Deductible Sum SC
  PaidEq Num(19,6) Paid Equalization Sum LC
  PaidEqFc Num(19,6) Paid Equalization Sum FC
  PaidEqSc Num(19,6) Paid Equalization Sum SC
  DpApplNet Num(19,6) Dpm Appl Net LC
  DpApplNetF Num(19,6) Dpm Appl Net FC
  DpApplNetS Num(19,6) Dpm Appl Net SC
  DpApplVat Num(19,6) Dpm Appl Tax LC
  DpApplVatF Num(19,6) Dpm Appl Tax FC
  DpApplVatS Num(19,6) Dpm Appl Tax SC
  DpApplDct Num(19,6) Dpm Appl Deductible Sum LC
  DpApplDctF Num(19,6) Dpm Appl Deductible Sum FC
  DpApplDctS Num(19,6) Dpm Appl Deductible Sum SC
  DpApplEq Num(19,6) Dpm Appl Equalization Sum LC
  DpApplEqFc Num(19,6) Dpm Appl Equalization Sum FC
  DpApplEqSc Num(19,6) Dpm Appl Equalization Sum SC
  TaxCode nVarChar(8) Tax Code ->OSTC
  LineType VarChar(1) Row Type default=D [D=Document, R=Exchange Rate Rounding, H=Document Header Rounding]
  BaseGrs Num(19,6) Gross LC
  BaseGrsFc Num(19,6) Gross FC
  BaseGrsSc Num(19,6) Gross SC
  ApplGrs Num(19,6) Applied Gross LC
  ApplGrsFc Num(19,6) Applied Gross FC
  ApplGrsSc Num(19,6) Applied Gross SC
  PaidGrs Num(19,6) Paid Gross LC
  PaidGrsFc Num(19,6) Paid Gross FC
  PaidGrsSc Num(19,6) Paid Gross SC
  DpApplGrs Num(19,6) Dpm Appl Gross LC
  DpApplGrsF Num(19,6) Dpm Appl Gross FC
  DpApplGrsS Num(19,6) Dpm Appl Gross SC
  RvsChrgSum Num(19,6) Reverse Charge Sum
  RvsChrgSc Num(19,6) Reverse Charge Sum (SC)
  RvsChrgFc Num(19,6) Reverse Charge Sum (FC)
  ApplRvs Num(19,6) Applied Reverse Charge Sum LC
  ApplRvsSc Num(19,6) Applied Reverse Charge Sum SC
  ApplRvsFc Num(19,6) Applied Reverse Charge Sum FC
  PaidRvs Num(19,6) Paid Reverse Charge Sum LC
  PaidRvsSc Num(19,6) Paid Reverse Charge Sum SC
  PaidRvsFc Num(19,6) Paid Reverse Charge Sum FC
  DpApplRvs Num(19,6) Dpm Applied Reverse Charge LC
  DpApplRvsS Num(19,6) Dpm Applied Reverse Charge SC
  DpApplRvsF Num(19,6) Dpm Applied Reverse Charge FC
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# SFI16 - Self Invoice - SnB properties
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, SnBIndex
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) abs entry ->OSFI
  LineNum Int(11) Line Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object id
  ObjAbs Int(11) Object Abs
  DrfWObjAbs Int(11) draft Wobj Abs default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type default=254000065
  LogInstanc Int(11) Log Instance

# SFI17 - Self Invoice - Import Process
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFI
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=254000065 ->ADP1
  ImpDocType VarChar(1) Type of Import Document ->OBSI
  ImpDocNum nVarChar(10) Importation Document Number
  DateOfReg Date(8) Date of Registry DI/DSI/DA
  CustClrDat Date(8) Date of Customs Clearance
  ConcActNum nVarChar(30) Drawback Concession Acct No.
  AdditNum nVarChar(30) Additional Number
  AddItmDV Num(19,6) Additional Item Discount Value
  tpVTransp Int(6) Overland Transport Route [1=Maritime, 2=Waterway, 3=Lakeside, 4=Air, 5=Post, 6=Train, 7=Road, 8=Network Transmission, 9=Own Means, 10=Input/Output Fictitious, 11=Courier, 12=Hand Carry]
  DrawSReg nVarChar(11) Drawback - Suspension Regime
  AddFrNavyA Num(19,6) Additional Freight to Navy Authority
  TypeOfImp VarChar(1) Type of Import
  nSeqAdic Int(6) Additional Item Sequential Number

# SFI18 - Self Invoice - Export Process
Module: Marketing Documents | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFI
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=254000065 ->ADP1
  ExpDocType Int(11) Type of Export Document default=-1 ->OBNI
  ExpDeclNum Int(11) Exportation Declaration Number
  ExpDeclDat Date(8) Exportation Declaration Date
  ExpNature Int(11) Nature of Exportation default=-1 ->OBNI
  ExpRegNum Int(11) Number of Exportation Registry
  ExpRegDate Date(8) Date of Exportation Registry
  LadBillNum nVarChar(19) Bill of Lading Number
  LadBillDat Date(8) Date of Bill of Lading
  MerchLeftD Date(8) Date Merchandise Left Customs
  LadBillTyp Int(11) Type of Bill of Lading default=-1 ->OBNI
  DrawSReg nVarChar(11) Drawback - Suspension Regime
  NatureExp nVarChar(44) Nature of Export
  QultExpItm Num(19,6) Quantity of Exported Items
  nSeqAdic Int(6) Additional Item Sequential Number

# SFI19 - Self Invoice - Bin Allocation Data
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, BinAllocSe
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OSFI
  BinAllocSe Int(11) Bin Allocation Sequence
  LineNum Int(11) Line Number
  SubLineNum Int(11) Subline Number default=-1
  SnBType Int(11) SnB Type default=-1
  SnBMDAbs Int(11) SnB Master Data Internal No. default=-1
  BinAbs Int(11) Bin Internal Number ->OBIN
  Quantity Num(19,6) Quantity
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjType nVarChar(20) Object Type default=254000065 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  BinActTyp Int(6) Bin Action Type [1=Transaction In, 2=Transaction Out, 4=SnB Complete, 8=Bin First Then SnB]

# SFI2 - Self Invoice - Freight - Rows
Module: Marketing Documents | 64 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFI
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=254000065 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) Vat Applied
  VatAppldFC Num(19,6) Vat Applied Frgn
  VatAppldSC Num(19,6) Vat Applied Sys
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report [Y=Yes, N=No]
  BaseGroup Int(11) Base Document Group default=-1 [-1=, 0=, 1=, 2=]
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1 [-1=, 0=, 1=, 2=]
  VisOrder Int(11) Visual Order
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]

# SFI20 - Intrastat Expenses
Module: Marketing Documents | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFI
  ExpnsCode Int(11) Freight Code ->OEXD
  TotalLC Num(19,6) Total
  TotalFC Num(19,6) Total (FC)
  TotalSC Num(19,6) Total (SC)
  DistribM VarChar(1) Distribution Method default=T [Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DrawnLC Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  LineNum Int(11) Line Number default=-1
  BaseAbsEnt Int(11) Base Abs. Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 16=Return, 13=A/R Invoice, 203=Down Payment Incoming, 204=Down Payment Outgoing, 22=Purchase Order, 20=Goods Receipt PO, 21=Goods Return, 18=A/P Invoice, 540000006=Purchase Quotation, 0=, -1=]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No. default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=254000065 ->ADP1
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  AppliedLC Num(19,6) Applied
  AppliedFC Num(19,6) Applied (FC)
  AppliedSC Num(19,6) Applied (SC)

# SFI21 - Self Invoice - Document Reference Information
Module: Marketing Documents | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, RefType
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjectType nVarChar(20) Object Type default=254000065
  LogInstanc Int(11) Log Instance default=0
  RefType VarChar(1) Reference Types default=S [S=System Document, E=External Document]
  LineNum Int(11) Line Number
  RefDocEntr Int(11) Referenced Internal Number
  RefDocNum Int(11) Referenced Document Number
  ExtDocNum nVarChar(100) External Referenced Document Number
  RefObjType nVarChar(20) Referenced Object Type [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 234000031=Return Request, 16=Return, 203=A/R Down Payment, 13=A/R Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 280=A/R Tax Invoice, 1470000113=Purchase Request, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Return Request, 21=Goods Return, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 281=A/P Tax Invoice, 69=Landed Costs, 24=Incoming Payments, 46=Outgoing Payments, 57=Checks for Payment, 321=Internal Reconciliation, 34=Recurring Posting, 30=Journal Entry, 59=Goods Receipt, 60=Goods Issue, 162=Inventory Revaluation, 1470000065=Inventory Counting, 10000071=Inventory Posting, 1250000001=Inventory Transfer Request, 67=Inventory Transfer, 202=Production Order, 13001=Original Invoice, -1=External Document, 20301=Original Down Payment Invoice]
  AccessKey nVarChar(100) Access Key
  IssueDate Date(8) Date of Issue
  IssuerCNPJ nVarChar(100) Issuer CNPJ
  IssuerCode nVarChar(10) Fiscal Document Issuer UF Code
  Model nVarChar(6) Fiscal Document Model
  Series nVarChar(3) Fiscal Document Series
  Number Int(11) Fiscal Document Number
  RefAccKey nVarChar(100) Referenced CT-e Access Key
  RefAmount Num(19,6) Referenced Amount
  SubSeries nVarChar(3) Fiscal Document Subseries
  Remark nVarChar(254) Remarks
  LinkRefTyp nVarChar(20) Link Reference Type default=00 [00=, 01=Nota de cr�dito de los documentos relacionados, 02=Nota de d�bito de los documentos relacionados, 03=Devoluci�n de mercanc�a sobre facturas o traslados previos, 04=Sustituci�n de los CFDI previos, 05=Traslados de mercancias facturados previamente, 06=Factura generada por los traslados previos, 07=CFDI por aplicaci�n de anticipo, 08=Customs, MX_08=Factura generada por pagos en parcialidades, 09=Factura generada por pagos diferidos]

# SFI22 - Self Invoice - Resource Costs
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, StdCostNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->SFI1
  LineNum Int(11) Row Number
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=254000065
  LogInstanc Int(11) Log Instance default=0

# SFI23 - Self Invoice - Selected Asset Master Data
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, VisOrder
  ASSETS: DocEntry, LineNum, AssetCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFI
  LineNum Int(11) Row Number
  AssetCode nVarChar(50) Selected Asset Code ->OITM
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Remarks nVarChar(100) Remarks
  Amount Num(19,6) Amount
  AmountSC Num(19,6) Amount (SC)
  SerialNo nVarChar(30) Serial Number
  VisOrder Int(11) Visual Order
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=254000065 ->ADP1

# SFI24 - Self Invoice - Tracking Note Assignment
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  ItemCCDNum nVarChar(40) Item CCD Number
  CntrOrigin nVarChar(3) Country/Region of Origin
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=254000065 ->ADP1
  SubLineNum Int(11) BOM Line No.

# SFI25 - Self Invoice - Amt Per VAT Grp
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, VatGroup, Type
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  VatGroup nVarChar(8) Tax Definition ->OVTG
  VatPrcnt Num(19,6) Tax Rate
  BaseAmnt Num(19,6) Base Amount
  BaseAmntFC Num(19,6) Base Amount (FC)
  BaseAmntSC Num(19,6) Base Amount (SC)
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  Type Int(11) Type default=1 [1=Discount by Tax]
  Currency nVarChar(3) Price Currency
  Rate Num(19,6) Currency Rate
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=254000065 ->ADP1

# SFI26 - Self Invoice - E-Way Bill Information
Module: Marketing Documents | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFI
  SuplyType nVarChar(20) EWB Transaction Type [O=Outward, I=Inward]
  SubSplyTyp Int(11) EWB Sub-Type ->OEST
  DocType nVarChar(3) EWB Doc. Type ->OEDT
  TransMode Int(11) EWB Transportation Mode ->OETM
  Distance Num(19,6) EWB Transport Distance
  TransDocNo nVarChar(16) EWB Transporter Doc. No.
  TransDate Date(8) EWB Transportation Date
  VehicleTyp nVarChar(2) EWB Vehicle Type ->OEVT
  VehicleNo nVarChar(15) EWB Vehicle Number
  EWayBillNo nVarChar(20) EWB No.
  EwbDate Date(8) E-Way Bill Date
  FrmTraName nVarChar(100) EWB Consignor Name
  FrmAddres1 nVarChar(120) EWB Consignor Address 1
  FrmAddres2 nVarChar(120) EWB Consignor Address 2
  FrmZipCode nVarChar(20) EWB Consignor Zip Code
  ActFrmStat nVarChar(2) Dispatch State of EWB Consignor
  ToTraName nVarChar(100) EWB Consignee Name
  ToAddres1 nVarChar(120) EWB Consignee Address 1
  ToAddres2 nVarChar(120) EWB Consignee Address 2
  ToZipCode nVarChar(20) EWB Consignee Zip Code
  ActToState nVarChar(2) Ship-To State of EWB Consignee
  FrmGSTN nVarChar(15) EWB Consignor GSTN
  FrmState nVarChar(2) Bill-To State of EWB Consignor
  ToGSTN nVarChar(15) EWB Consignee GSTN
  ToState nVarChar(2) Bill-To State of EWB Consignee
  MainHsnEnt Int(11) EWB Main HSN Entry ->OCHP
  FrmPlace nVarChar(50) EWB Consignor Place
  ToPlace nVarChar(50) EWB Consignee Place
  TransID nVarChar(15) EWB Transporter ID
  TransName nVarChar(25) EWB Transporter Name
  ExpireDate Date(8) EWB Expiration Date
  ObjectType nVarChar(20) Object Type default=254000065 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TspEntry Int(11) Transporter Abs. Entry ->OTSP
  TspLine Int(11) Transportation Line
  TransType Int(11) Transaction Type [1=Regular, 2=Bill To-Ship To, 3=Bill From-Dispatch From, 4=Combination of 2 and 3]

# SFI27 - Self Invoice - E-Books(GR) Rows
Module: Marketing Documents | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  RELATE_ROW: DocEntry, RelateType, RelateLine, GroupNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFI
  LineNum Int(11) Row Number
  RelateType Int(11) Relation Type default=-1 [1=Row, 2=Row Expenses, 3=Document Expenses, 13=Distributed Freights, -1=Manual]
  RelateLine Int(11) Relation Row Number default=-1
  GroupNum Int(11) Group Number default=-1
  LineTotal Num(19,6) Line Total
  LineTotalF Num(19,6) Line Total (FC)
  LineTotalS Num(19,6) Line Total (SC)
  InClassTyp Int(11) Income Classification Type ->OICP
  InClassCat Int(11) Income Classification Category ->OICC
  ExClassTyp Int(11) Expense Classification Type ->OECP
  ExClassCat Int(11) Expense Classification Cat. ->OECC
  VatCate Int(11) VAT Category
  NetValue Num(19,6) Net Value
  NetValueFC Num(19,6) Net Value (FC)
  NetValueSC Num(19,6) Net Value (SC)
  VatAmount Num(19,6) VAT Amount
  VatAmFC Num(19,6) VAT Amount (FC)
  VatAmSC Num(19,6) VAT Amount (SC)
  WtPercCat Int(11) Withheld Percentage Category
  WtAmount Num(19,6) Withheld Amount
  WtAmountFC Num(19,6) Withheld Amount (FC)
  WtAmountSC Num(19,6) Withheld Amount (SC)
  ObjectType nVarChar(20) Object Type default=13 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  WtCategory VarChar(1) Withheld Category [I=Invoice, P=Payment]
  VATClassTy Int(11) VAT Classification Type ->OECP
  VATClassCa Int(11) VAT Classification Category ->OECC
  EBVatExCau Int(11) VAT Exemption Cause ->OVEC

# SFI28 - Self Invoice - Reported Tracking Note
Module: Marketing Documents | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
  TCN_KEY U: DocEntry, LineNum, TrackingNt, TrackiNtLn
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  UnusedQty Num(19,6) Unused Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=254000065 ->ADP1
  SubLineNum Int(11) BOM Line No.

# SFI3 - Self Invoice - Freight
Module: Marketing Documents | 80 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  DOCUMENT: DocEntry, BaseAbsEnt
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFI
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  Comments nVarChar(100) Remarks
  ObjType nVarChar(20) Object Type default=254000065 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  WTLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  VatApplied Num(19,6) Vat Applied
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatF Num(19,6) Net Tax Amount (FC)
  LineVatS Num(19,6) Net Tax Amount (SC)
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 23=Sales Quotation, 17=Sales Order, 15=Delivery]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No.
  LineNum Int(11) line num default=-1
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Doc. Internal No. default=-1
  StDstr Num(19,6) Stock Distributed Sum
  StDstrSC Num(19,6) Stock Distributed Sum (SC)
  StDstrFC Num(19,6) Stock Distributed Sum (FC)
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  TaxDistMtd VarChar(1) Tax Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  GrsAmount Num(19,6) Gross Amount
  GrsFC Num(19,6) Gross Amount (FC)
  GrsSC Num(19,6) Gross Amount (SC)
  BaseTotal VarChar(1) Base Total for Calculation default=N [N=Net Total, G=Gross Total]
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)
  RRVatLC Num(19,6) Return Request VAT Amount
  RRVatFC Num(19,6) Return Request VAT Amount (FC)
  RRVatSC Num(19,6) Return Request VAT Amount (SC)
  EncryptIV nVarChar(100) Encrypt IV
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]

# SFI4 - Self Invoice - Tax Amount per Document
Module: Marketing Documents | 61 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SCONDARY: DocEntry, LineNum, GroupNum, ExpnsCode, StcCode, StaCode, staType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFI
  LineNum Int(11) Row Number default=-1
  GroupNum Int(11) Group Number default=-1
  ExpnsCode Int(11) Expense Code default=-1 ->OEXD
  RelateType Int(11) Relation Type default=1 [1=Row, 2=Row Expenses, 3=Document Expenses, 13=Distributed Freights]
  StcCode nVarChar(8) Tax Code ->OSTC
  StaCode nVarChar(8) Authority Code ->OSTA
  staType Int(11) Authority Type ->OSTT
  TaxRate Num(19,6) Tax Rate
  TaxAcct nVarChar(15) Tax Account ->OACT
  TaxSum Num(19,6) Tax Amount
  TaxSumFrgn Num(19,6) Tax Amount (FC)
  TaxSumSys Num(19,6) Tax Amount (SC)
  BaseSum Num(19,6) Base Amount
  BaseSumFrg Num(19,6) Base Amount (FC)
  BaseSumSys Num(19,6) Base Amount (SC)
  ObjectType nVarChar(20) Object Type default=254000065 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Status default=Y [Y=Normal Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) Applied Tax
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  LineSeq Int(11) Row Sequence
  DeferrAcct nVarChar(15) Deferred Tax Account ->OACT
  BaseType Int(11) Base Document Type default=-1
  BaseAbs Int(11) Base Document Internal No. default=-1
  BaseSeq Int(11) Base Doc. Row Sequence
  DeductTax Num(19,6) Deductible Tax Amount
  DdctTaxFrg Num(19,6) Deductible Tax Amount (FC)
  DdctTaxSys Num(19,6) Deductible Tax Amount (SC)
  BaseAppld Num(19,6) Applied Base Amount
  BaseApldFC Num(19,6) Applied Base Amount (FC)
  BaseApldSC Num(19,6) Applied Base Amount (SC)
  NonDdctPrc Num(19,6) Non Deductible %
  NonDdctAct nVarChar(15) Non Deductible Account ->OACT
  TaxInPrice VarChar(1) Tax Included in Price? default=N [Y=Yes, N=No]
  Exempt VarChar(1) Exempt? default=N [Y=Yes, N=No]
  TaxExpAct nVarChar(15) Expense Account for Tax ->OACT
  OnHoldTax Num(19,6) On Hold Tax Amount
  OnHoldTaxF Num(19,6) On Hold Tax Amount (FC)
  OnHoldTaxS Num(19,6) On Hold Tax Amount (SC)
  InGrossRev VarChar(1) Included in Gross Revenue default=N [Y=Yes, N=No]
  TaxSumOrg Num(19,6) Tax Amount Original
  TaxSumOrgF Num(19,6) Tax Amount Original (FC)
  TaxSumOrgS Num(19,6) Tax Amount Original (SC)
  OpenTax Num(19,6) Open Service Tax
  OpenTaxFC Num(19,6) Open Service Tax (FC)
  OpenTaxSC Num(19,6) Open Service Tax (SC)
  Unencumbrd VarChar(1) Unencumbered default=N [Y=Yes, N=No]
  TaxOnRI VarChar(1) Tax On Reserve Invoice default=N [Y=Yes, N=No]
  RvsChrgPrc Num(19,6) Reverse Charge %
  RvsChrgTax Num(19,6) Reverse Charge Tax Amount
  RvsChrgSC Num(19,6) Reverse Charge Tax Amount (SC)
  RvsChrgFC Num(19,6) Reverse Charge Tax Amount (FC)
  InFirstIns VarChar(1) Included in First Installment default=N [Y=Yes, N=No]
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CESTrel VarChar(1) CEST Relevant default=N [Y=, N=]

# SFI5 - Self Invoice - Withholding Tax
Module: Marketing Documents | 158 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  SECONDERY U: AbsEntry, WTCode, BaseAbsEnt, Doc1LineNo
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OSFI
  WTCode nVarChar(4) WTax Code ->OWHT
  Rate Num(19,6) Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntSC Num(19,6) Taxable Amount (SC)
  TxblAmntFC Num(19,6) Taxable Amount (FC)
  WTAmnt Num(19,6) WTax Amount
  WTAmntSC Num(19,6) WTax Amount (SC)
  WTAmntFC Num(19,6) WTax Amount (FC)
  ApplAmnt Num(19,6) Applied WTax Amount
  ApplAmntSC Num(19,6) Applied WTax Amount (SC)
  ApplAmntFC Num(19,6) Applied WTax Amount (FC)
  Category VarChar(1) Category [P=Payment, I=Invoice]
  Criteria VarChar(1) Criteria [Y=Accrual, N=Cash]
  Account nVarChar(15) G/L Account ->OACT
  Type VarChar(1) Withholding Tax Type [V=VAT Withholding, I=Income Tax Withholding]
  RoundType VarChar(1) Rounding Type [T=Truncated, C=Commercial Values, N=No Rounding]
  BaseType VarChar(1) Base Type [G=Gross, N=Net, V=VAT, U=UoM]
  BaseAbsEnt Int(11) Base Document Internal No. default=-1
  BaseLine Int(11) Base Row
  BaseNum Int(11) Base Document Type default=-1 [-1=, 0=, 23=Sales Quotation, 17=Sales Order, 15=Delivery]
  LineNum Int(11) Row Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Doc. Internal No. default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=254000065 ->ADP1
  Doc1LineNo Int(11) DOC1 Line Number default=-1
  WtLineType VarChar(1) WTax Row Type default=D [D=Document Level WTax, L=Row Level WTax]
  TxblCurr nVarChar(3) Taxable Currency from Document Line
  DtblCurr nVarChar(3) Deductible Currency
  DtblRate Num(19,6) Rate for Deductible Amount
  txblRate Num(19,6) Rate for Taxable Amount
  DtblAmount Num(19,6) Deductible Amount
  TdsAcc nVarChar(15) TDS Account ->OACT
  SurAcc nVarChar(15) Surcharge Account ->OACT
  CessAcc nVarChar(15) Cess Account ->OACT
  HscAcc nVarChar(15) HSC Account ->OACT
  TdsRate Num(19,6) TDS Rate
  SurRate Num(19,6) Surcharge Rate
  CessRate Num(19,6) Cess Rate
  HscRate Num(19,6) HSC Rate
  TdsBAmt Num(19,6) TDS Base Amount
  TdsBAmtSC Num(19,6) TDS Base Amount (SC)
  TdsBAmtFC Num(19,6) TDS Base Amount (FC)
  SurBAmt Num(19,6) Surcharge Base Amount
  SurBAmtSC Num(19,6) Surcharge Base Amount (SC)
  SurBAmtFC Num(19,6) Surcharge Base Amount (FC)
  CessBAmt Num(19,6) Cess Base Amount
  CessBAmtSC Num(19,6) Cess Base Amount (SC)
  CessBAmtFC Num(19,6) Cess Base Amount (FC)
  HscBAmt Num(19,6) HSC Base Amount
  HscBAmtSC Num(19,6) HSC Base Amount (SC)
  HscBAmtFC Num(19,6) HSC Base Amount (FC)
  TdsAmnt Num(19,6) TDS Tax Amount
  TdsAmntSC Num(19,6) TDS Tax Amount (SC)
  TdsAmntFC Num(19,6) TDS Tax Amount (FC)
  SurAmnt Num(19,6) Surcharge Tax Amount
  SurAmntSC Num(19,6) Surcharge Tax Amount (SC)
  SurAmntFC Num(19,6) Surcharge Tax Amount (FC)
  CessAmnt Num(19,6) Cess Tax Amount
  CessAmntSC Num(19,6) Cess Tax Amount (SC)
  CessAmntFC Num(19,6) Cess Tax Amount (FC)
  HscAmnt Num(19,6) HSC Tax Amount
  HscAmntSC Num(19,6) HSC Tax Amount (SC)
  HscAmntFC Num(19,6) HSC Tax Amount (FC)
  TdsAppl Num(19,6) Applied TDS Amount
  TdsApplSC Num(19,6) Applied TDS Amount (SC)
  TdsApplFC Num(19,6) Applied TDS Amount (FC)
  SurAppl Num(19,6) Applied Surcharge Amount
  SurApplSC Num(19,6) Applied Surcharge Amount (SC)
  SurApplFC Num(19,6) Applied Surcharge Amount (FC)
  CessAppl Num(19,6) Applied Cess Amount
  CessApplSC Num(19,6) Applied Cess Amount (SC)
  CessApplFC Num(19,6) Applied Cess Amount (FC)
  HscAppl Num(19,6) Applied HSC Amount
  HscApplSC Num(19,6) Applied HSC Amount (SC)
  HscApplFC Num(19,6) Applied HSC Amount (FC)
  BatchNum Int(11) Journal Voucher No.
  InCSTCode nVarChar(2) CST Code Incoming
  OutCSTCode nVarChar(2) CST Code Outgoing
  DpmWTApl Num(19,6) DPM WT Applied Amount
  DpmWTAplSC Num(19,6) DPM WT Applied Amount (SC)
  DpmWTAplFC Num(19,6) DPM WT Applied Amount (FC)
  WTTypeId Int(11) WT Type Id ->OWTT
  LnBsAmt Num(19,6) BR Line WT Base Amount
  LnBsAmtSC Num(19,6) BR Line WT Base Amount(SC)
  LnBsAmtFC Num(19,6) BR Line WT Base Amount(FC)
  LnCmTAmt Num(19,6) BR Line Cumulated Taxable Amount
  LnCmTAmtSC Num(19,6) BR Line Cumulated Taxable Amount(SC)
  LnCmTAmtFC Num(19,6) BR Line Cumulated Taxable Amount(FC)
  TDSType VarChar(1) TDS Type [E=eTDS, D=GST TDS, C=GST TCS, S=SALES TCS]
  IgstAcc nVarChar(15) IGST Account ->OACT
  CgstAcc nVarChar(15) CGST Account ->OACT
  SgstAcc nVarChar(15) SGST Account ->OACT
  IgstAmnt Num(19,6) IGST Tax Amount
  IgstAmntSC Num(19,6) IGST Tax Amount (SC)
  IgstAmntFC Num(19,6) IGST Tax Amount (FC)
  CgstAmnt Num(19,6) CGST Tax Amount
  CgstAmntSC Num(19,6) CGST Tax Amount (SC)
  CgstAmntFC Num(19,6) CGST Tax Amount (FC)
  SgstAmnt Num(19,6) SGST Tax Amount
  SgstAmntSC Num(19,6) SGST Tax Amount (SC)
  SgstAmntFC Num(19,6) SGST Tax Amount (FC)
  IgstRate Num(19,6) IGST Rate
  CgstRate Num(19,6) CGST Rate
  SgstRate Num(19,6) SGST Rate
  IgstBAmt Num(19,6) IGST Base Amount
  IgstBAmtSC Num(19,6) IGST Base Amount (SC)
  IgstBAmtFC Num(19,6) IGST Base Amount (FC)
  CgstBAmt Num(19,6) CGST Base Amount
  CgstBAmtSC Num(19,6) CGST Base Amount (SC)
  CgstBAmtFC Num(19,6) CGST Base Amount (FC)
  SgstBAmt Num(19,6) SGST Base Amount
  SgstBAmtSC Num(19,6) SGST Base Amount (SC)
  SgstBAmtFC Num(19,6) SGST Base Amount (FC)
  IgstAppl Num(19,6) Applied IGST Amount
  IgstApplSC Num(19,6) Applied IGST Amount (SC)
  IgstApplFC Num(19,6) Applied IGST Amount (FC)
  CgstAppl Num(19,6) Applied CGST Amount
  CgstApplSC Num(19,6) Applied CGST Amount (SC)
  CgstApplFC Num(19,6) Applied CGST Amount (FC)
  SgstAppl Num(19,6) Applied SGST Amount
  SgstApplSC Num(19,6) Applied SGST Amount (SC)
  SgstApplFC Num(19,6) Applied SGST Amount (FC)
  UtgstAcc nVarChar(15) UTGST Account ->OACT
  CsgstAcc nVarChar(15) Cess GST Account ->OACT
  UtgstAmt Num(19,6) UTGST Tax Amount
  UtgstAmtSC Num(19,6) UTGST Tax Amount (SC)
  UtgstAmtFC Num(19,6) UTGST Tax Amount (FC)
  CsgstAmt Num(19,6) Cess GST Tax Amount
  CsgstAmtSC Num(19,6) Cess GST Tax Amount (SC)
  CsgstAmtFC Num(19,6) Cess GST Tax Amount (FC)
  UtgstRate Num(19,6) UTGST Rate
  CsgstRate Num(19,6) Cess GST Rate
  UtgstBAmt Num(19,6) UTGST Base Amount
  UtgstBAmtS Num(19,6) UTGST Base Amount (SC)
  UtgstBAmtF Num(19,6) UTGST Base Amount (FC)
  CsgstBAmt Num(19,6) Cess GST Base Amount
  CsgstBAmtS Num(19,6) Cess GST Base Amount (SC)
  CsgstBAmtF Num(19,6) Cess GST Base Amount (FC)
  UtgstAppl Num(19,6) Applied UTGST Amount
  UtgstApplS Num(19,6) Applied UTGST Amount (SC)
  UtgstApplF Num(19,6) Applied UTGST Amount (FC)
  CsgstAppl Num(19,6) Applied Cess GST Amount
  CsgstApplS Num(19,6) Applied Cess GST Amount (SC)
  CsgstApplF Num(19,6) Applied Cess GST Amount (FC)
  EncryptIV nVarChar(100) Encrypt IV
  TcsIntAcct nVarChar(15) TCS Interim Account ->OACT
  SurIntAcct nVarChar(15) Surcharge Interim Account ->OACT
  CesIntAcct nVarChar(15) Cess Interim Account ->OACT
  HscIntAcct nVarChar(15) HSC interim Account ->OACT
  LnIntAcct nVarChar(15) Interim Account for Tax ->OACT
  FixedAmnt Num(19,6) Fixed Amount
  FixedAmtSC Num(19,6) Fixed Amount (SC)
  FixedAmtFC Num(19,6) Fixed Amount (FC)
  BaseQty Num(19,6) Base Quantity

# SFI6 - Self Invoice - Installments
Module: Marketing Documents | 65 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, InstlmntID
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFI
  InstlmntID Int(6) Installment ID default=1
  ObjType nVarChar(20) Object Type default=254000065 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DueDate Date(8) Due Date
  Status VarChar(1) Installment Status default=O [O=Open, C=Closed]
  DunnLevel Int(11) Dunning Level default=0
  InsTotal Num(19,6) Total Installment
  InsTotalFC Num(19,6) Total Installment (FC)
  InsTotalSy Num(19,6) Total Installment (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  VatSum Num(19,6) Total Tax
  VatSumFC Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  VatPaid Num(19,6) Tax Paid to Date
  VatPaidFC Num(19,6) Tax Paid (FC)
  VatPaidSys Num(19,6) Tax Paid (SC)
  TotalExpns Num(19,6) Total Freight Charges
  TotalExpFC Num(19,6) Total Freight Charges (FC)
  TotalExpSC Num(19,6) Total Freight Charges (SC)
  ExpAppl Num(19,6) Applied Freight Charges
  ExpApplFC Num(19,6) Applied Freight Charges (FC)
  ExpApplSC Num(19,6) Applied Freight Charges (SC)
  WTSum Num(19,6) WTax Amount
  WTSumFC Num(19,6) WTax Amount (FC)
  WTSumSC Num(19,6) WTax Amount (SC)
  WTApplied Num(19,6) Applied WTax
  WTAppliedF Num(19,6) Applied WTax (FC)
  WTAppliedS Num(19,6) Applied WTax (SC)
  TotalBlck Num(19,6) Total Reserved Amount
  TotalBlckF Num(19,6) Total Reserved Amount (FC)
  TotalBlckS Num(19,6) Total Reserved Amount (SC)
  VATBlck Num(19,6) Reserved Tax Amount
  VATBlckFC Num(19,6) Reserved Tax Amount (FC)
  VATBlckSC Num(19,6) Reserved Tax Amount (SC)
  ExpnsBlck Num(19,6) Reserved Freight Charges
  ExpnsBlckF Num(19,6) Reserved Freight Charges (FC)
  ExpnsBlckS Num(19,6) Reserved Freight Charges (SC)
  WTBlocked Num(19,6) Reserved WTax Amount
  WTBlockedF Num(19,6) Reserved WTax Amount (FC)
  WTBlockedS Num(19,6) Reserved WTax Amount (SC)
  InstPrcnt Num(19,6) Installment %
  DunWizBlck VarChar(1) Wizard dunning block default=N [N=No, Y=Yes]
  DunDate Date(8) Last Dunning Date
  Paid Num(19,6) Paid
  PaidFrgn Num(19,6) Paid (FC)
  PaidSc Num(19,6) Paid (SC)
  reserved VarChar(1) Reserved default=N [N=No, Y=Yes]
  TaxOnExp Num(19,6) Tax on Freight
  TaxOnExpFc Num(19,6) Tax on Expenses (FC)
  TaxOnExpSc Num(19,6) Tax on Expenses (SC)
  TaxOnExpAp Num(19,6) Applied Tax on Expenses
  TaxOnExApF Num(19,6) Applied Tax on Expenses (FC)
  TaxOnExApS Num(19,6) Applied Tax on Expenses (SC)
  TaxOnExBlo Num(19,6) Reserved Tax on Freight Amount
  TaxOnExBlF Num(19,6) Reserved Tax on Freight Amt FC
  TaxOnExBlS Num(19,6) Reserved Tax on Freight Amt SC
  LvlUpdDate Date(8) Dunning Level Update Date
  Ordered VarChar(1) Payment Ordered default=N [Y=Yes, N=No]
  PaidDpm Num(19,6) Paid by Down Payment
  PaidDpmFc Num(19,6) Paid by Down Payment (FC)
  PaidDpmSc Num(19,6) Paid by Down Payment (SC)
  EncryptIV nVarChar(100) Encrypt IV

# SFI7 - Self Invoice - Delivery Packages
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFI
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type default=254000065 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV

# SFI8 - Self Invoice - Items in Package
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum, ItemCode, UomEntry, NumPerMsr
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFI
  PackageNum Int(11) Package Number
  ItemCode nVarChar(50) Item Code ->OITM
  Quantity Num(19,6) Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=254000065 ->ADP1
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value default=0

# SFI9 - Self Invoice - Drawn Down Payment
Module: Marketing Documents | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSFI
  LineNum Int(11) Row Number
  BaseAbs Int(11) Base Document Internal ID ->ODPI
  BaseLine Int(11) Base Document Row
  TargetBase VarChar(1) Target or Base Document default=T [B=Base, T=Target]
  ObjType nVarChar(20) Base Object Type default=203 [203=A/R Down Payment]
  DrawnSum Num(19,6) Net LC
  DrawnSumFc Num(19,6) Net FC
  DrawnSumSc Num(19,6) Net SC
  LogInstanc Int(11) Log Instance default=0
  ObjCode nVarChar(20) Object Type default=254000065 ->ADP1
  ApplDrawn Num(19,6) Applied Net LC
  ApplDrawnF Num(19,6) Applied Net FC
  ApplDrawnS Num(19,6) Applied Net SC
  BaseDocNum Int(11) Base Document Number
  BsDocDate Date(8) Base Posting Date
  BsDueDate Date(8) Base Due Date
  BsCardName nVarChar(100) Base BP Name
  BsComments nVarChar(254) Base Remarks
  Posted VarChar(1) Base Document Posted default=Y [Y=Yes, N=No]
  Vat Num(19,6) Tax LC
  VatFc Num(19,6) Tax FC
  VatSc Num(19,6) Tax SC
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  IsGross VarChar(1) Is Gross Line default=N [N=Net Line, Y=Gross Line]

# TGPA - Gross Profit Adjustment - Log
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Identity(11) Internal Key
  ItemCode nVarChar(50) Item No. ->OITM
  ItemName nVarChar(200) Item Description
  LineID Int(11) Line ID
  Selected VarChar(1) Selected default=N
  DocType nVarChar(20) Document Type
  DocNum Int(11) Document Number
  DocAbs Int(11) Document Abs. Entry
  DocLineNum Int(11) Document Line Number
  ManagedBy Int(11) Managed By default=-1 [10000044=Batch Numbers, 10000045=Serial Numbers]
  SysNumber Int(11) System Number

# TPI1 - Purchase Tax Invoice - Rows
Module: Marketing Documents | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BaseEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  BaseEntry Int(11) Base Document Internal ID ->OTPI
  LineNum Int(11) Row Number
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  DocType VarChar(1) Document Type default=I [I=Invoice, P=Payment, J=Journal Entry, C=Correction Invoice, D=Down Payment, L=Landed Cost]
  RefEntry1 Int(11) Ref.1 Document Key
  RefEntry2 Int(11) Ref.1 Document Key
  ObjType Int(6) Object Type ->ADP1
  LogInstanc Int(11) Log Instance default=0
  RefType Int(11) Ref. Object Type default=-1 [-1=, 13=A/R Invoice, 18=A/P Invoice, 30=Journal Entry, 24=Incoming Payment, 204=A/P Down Payment, 165=A/R Correction Invoice, 163=A/P Correction Invoice, 69=Landed Cost]
  EncryptIV nVarChar(100) Encrypt IV

# TPI2 - Tax Invoice Operation Codes
Module: Marketing Documents | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BaseEntry, LineNum, OpCode
Fields (name type(len) description [values] ->parent table):
  BaseEntry Int(11) Abs. Entry ->OTSI
  LineNum Int(11) Base Doc. Abs. Entry ->TSI1
  OpCode Int(11) Operation Code ->OBSI
  ObjType Int(11) Object Type ->ADP1
  LogInstanc Int(11) Log Instance default=0

# TPI3 - Purchase Tax Invoice - Document Reference Information
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjType Int(11) Object Type
  LogInstanc Int(11) Log Instance default=0
  LineNum Int(11) Line Number
  RefDocEntr Int(11) Referenced Internal Number
  RefDocNum Int(11) Referenced Document Number
  ExtDocNum nVarChar(100) External Referenced Document Number
  RefObjType nVarChar(20) Referenced Object Type [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 234000031=Return Request, 16=Return, 203=A/R Down Payment, 13=A/R Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 280=A/R Tax Invoice, 1470000113=Purchase Request, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Return Request, 21=Goods Return, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 281=A/P Tax Invoice, 69=Landed Costs, 24=Incoming Payments, 46=Outgoing Payments, 57=Checks for Payment, 321=Internal Reconciliation, 34=Recurring Posting, 30=Journal Entry, 59=Goods Receipt, 60=Goods Issue, 162=Inventory Revaluation, 1470000065=Inventory Counting, 10000071=Inventory Posting, 1250000001=Inventory Transfer Request, 67=Inventory Transfer, 202=Production Order, 13001=Original Invoice, -1=External Document]
  IssueDate Date(8) Date of Issue
  Remark nVarChar(254) Remarks
  CardCode nVarChar(15) Business Partner

# TPI4 - Purchase Tax Invoice - Linked Down Payments
Module: Marketing Documents | 23 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjType Int(11) Object Type
  LogInstanc Int(11) Log Instance default=0
  LineNum Int(11) Line Number
  DpmObjType Int(11) Down Payment Type
  DpmDocEntr Int(11) Down Payment Entry
  DpmDocNum Int(11) Down Payment No.
  PmnObjType Int(11) Payment Type
  PmnDocEntr Int(11) Payment Entry
  PmnDocNum Int(11) Payment Number
  PmnTaxDate Date(8) Payment Date
  TrsfrDate Date(8) Transfer Date
  TrsfrRef nVarChar(27) Intended Purpose
  DrawnSum Num(19,6) Drawn Amount
  DrawnSumFc Num(19,6) Drawn Amount (FC)
  DrawnSumSc Num(19,6) Drawn Amount (SC)
  DocCur nVarChar(3) Document Currency
  Vat Num(19,6) Tax Amount
  VatFc Num(19,6) Tax Amount (FC)
  VatSc Num(19,6) Tax Amount (SC)
  Gross Num(19,6) Gross Amount
  GrossFc Num(19,6) Gross Amount (FC)
  GrossSc Num(19,6) Gross Amount (SC)

# TRA1 - Transition - Rows
Module: Marketing Documents | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Entry ->OINV
  LineNum Int(11) Row Number
  BaseEntry Int(11) Base Document Internal ID
  PackQty Num(19,6) Packing Quantity
  PurPackMsr nVarChar(8) Packaging UoM Name default=Pack
  ArsnalName nVarChar(20) Storage Group Name
  ArsnalCode nVarChar(20) Storage Group Code
  UnitMsr nVarChar(5) Ref. UoM (Type) default=Unit
  Quantity Num(19,6) Quantity
  Fraction Num(19,6) Remainder
  Weight1 Num(19,6) Weight
  LineTotal Num(19,6) Row Total
  ItemCode nVarChar(50) Item No. ->OITM

# TRO1 - Lines of Transportation Document
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  DOC_LINK_U U: AbsEntry, DocObjType, DocEntry, DocLineNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OTRO
  LineNum Int(11) Line Number
  DocObjType Int(11) Document Object Type [13=A/R Invoice, 15=Delivery, 21=Goods Return, 67=Inventory Transfer]
  DocEntry Int(11) Internal Number
  DocLineNum Int(11) Document Line Number
  ItemCode nVarChar(50) Item No.
  TranspQty Num(19,6) Transported Quantity
  LogInstanc Int(11) Log Instance default=0
  DocOrdNum Int(11) Document Order Number

# TSI1 - Sales Tax Invoice - Rows1
Module: Marketing Documents | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BaseEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  BaseEntry Int(11) Base Document Internal ID ->OTSI
  LineNum Int(11) Row Number
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  DocType VarChar(1) Document Type default=I [I=Invoice, P=Payment, J=Journal Entry, C=Correction Invoice, L=Landed Cost]
  RefEntry1 Int(11) Ref.1 Document Key
  RefEntry2 Int(11) Ref.1 Document Key
  ObjType Int(6) Object Type ->ADP1
  LogInstanc Int(11) Log Instance default=0
  RefType Int(11) Ref. Object Type default=-1 [-1=, 13=A/R Invoice, 18=A/P Invoice, 30=Journal Entry, 24=Incoming Payment, 204=A/P Down Payment, 165=A/R Correction Invoice, 163=A/P Correction Invoice, 69=Landed Cost]
  EncryptIV nVarChar(100) Encrypt IV

# TSI2 - Tax Invoice Operation Codes
Module: Marketing Documents | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BaseEntry, LineNum, OpCode
Fields (name type(len) description [values] ->parent table):
  BaseEntry Int(11) Abs. Entry ->OTSI
  LineNum Int(11) Base Doc. Abs. Entry ->TSI1
  OpCode Int(11) Operation Code ->OBSI
  ObjType Int(11) Object Type ->ADP1
  LogInstanc Int(11) Log Instance default=0

# TSI3 - Sales Tax Invoice - Document Reference Information
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjType Int(11) Object Type
  LogInstanc Int(11) Log Instance default=0
  LineNum Int(11) Line Number
  RefDocEntr Int(11) Referenced Internal Number
  RefDocNum Int(11) Referenced Document Number
  ExtDocNum nVarChar(100) External Referenced Document Number
  RefObjType nVarChar(20) Referenced Object Type [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 234000031=Return Request, 16=Return, 203=A/R Down Payment, 13=A/R Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 280=A/R Tax Invoice, 1470000113=Purchase Request, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Return Request, 21=Goods Return, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 281=A/P Tax Invoice, 69=Landed Costs, 24=Incoming Payments, 46=Outgoing Payments, 57=Checks for Payment, 321=Internal Reconciliation, 34=Recurring Posting, 30=Journal Entry, 59=Goods Receipt, 60=Goods Issue, 162=Inventory Revaluation, 1470000065=Inventory Counting, 10000071=Inventory Posting, 1250000001=Inventory Transfer Request, 67=Inventory Transfer, 202=Production Order, 13001=Original Invoice, -1=External Document]
  IssueDate Date(8) Date of Issue
  Remark nVarChar(254) Remarks
  CardCode nVarChar(15) Business Partner

# TSI4 - Sales Tax Invoice - Linked Down Payments
Module: Marketing Documents | 23 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjType Int(11) Object Type
  LogInstanc Int(11) Log Instance default=0
  LineNum Int(11) Line Number
  DpmObjType Int(11) Down Payment Type
  DpmDocEntr Int(11) Down Payment Entry
  DpmDocNum Int(11) Down Payment No.
  PmnObjType Int(11) Payment Type
  PmnDocEntr Int(11) Payment Entry
  PmnDocNum Int(11) Payment Number
  PmnTaxDate Date(8) Payment Date
  TrsfrDate Date(8) Transfer Date
  TrsfrRef nVarChar(27) Intended Purpose
  DrawnSum Num(19,6) Drawn Amount
  DrawnSumFc Num(19,6) Drawn Amount (FC)
  DrawnSumSc Num(19,6) Drawn Amount (SC)
  DocCur nVarChar(3) Document Currency
  Vat Num(19,6) Tax Amount
  VatFc Num(19,6) Tax Amount (FC)
  VatSc Num(19,6) Tax Amount (SC)
  Gross Num(19,6) Gross Amount
  GrossFc Num(19,6) Gross Amount (FC)
  GrossSc Num(19,6) Gross Amount (SC)

# TXD1 - Tax Invoice Drafts - Rows
Module: Marketing Documents | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BaseEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  BaseEntry Int(11) Base Document Internal ID
  LineNum Int(11) Row Number
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  DocType VarChar(1) Document Type default=I [I=Invoice, P=Payment, J=Journal Entry, C=Correction Invoice, R=Payment Request, L=Landed Cost]
  RefEntry1 Int(11) Ref.1 Document Key
  RefEntry2 Int(11) Ref. 2 Document Key
  ObjType Int(6) Object Type ->ADP1
  LogInstanc Int(11) Log Instance default=0
  RefType Int(11) Ref. Object Type default=-1 [-1=, 13=A/R Invoice, 18=A/P Invoice, 30=Journal Entry, 24=Incoming Payment, 204=A/P Down Payment, 165=A/R Correction Invoice, 163=A/P Correction Invoice, 69=Landed Cost]
  EncryptIV nVarChar(100) Encrypt IV

# TXD2 - Tax Invoice Draft Operation Codes
Module: Marketing Documents | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BaseEntry, LineNum, OpCode
Fields (name type(len) description [values] ->parent table):
  BaseEntry Int(11) Abs. Entry ->OTSI
  LineNum Int(11) Base Doc. Abs. Entry ->TSI1
  OpCode Int(11) Operation Code ->OBSI
  ObjType Int(11) Object Type ->ADP1
  LogInstanc Int(11) Log Instance default=0

# TXD3 - Tax Invoice Draft - Document Reference Information
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ObjType
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjType Int(11) Object Type
  LogInstanc Int(11) Log Instance default=0
  LineNum Int(11) Line Number
  RefDocEntr Int(11) Referenced Internal Number
  RefDocNum Int(11) Referenced Document Number
  ExtDocNum nVarChar(100) External Referenced Document Number
  RefObjType nVarChar(20) Referenced Object Type [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 234000031=Return Request, 16=Return, 203=A/R Down Payment, 13=A/R Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 280=A/R Tax Invoice, 1470000113=Purchase Request, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Return Request, 21=Goods Return, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 281=A/P Tax Invoice, 69=Landed Costs, 24=Incoming Payments, 46=Outgoing Payments, 57=Checks for Payment, 321=Internal Reconciliation, 34=Recurring Posting, 30=Journal Entry, 59=Goods Receipt, 60=Goods Issue, 162=Inventory Revaluation, 1470000065=Inventory Counting, 10000071=Inventory Posting, 1250000001=Inventory Transfer Request, 67=Inventory Transfer, 202=Production Order, 13001=Original Invoice, -1=External Document]
  IssueDate Date(8) Date of Issue
  Remark nVarChar(254) Remarks
  CardCode nVarChar(15) Business Partner

# TXD4 - Tax Invoice Draft - Linked Down Payments
Module: Marketing Documents | 23 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ObjType
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjType Int(11) Object Type
  LogInstanc Int(11) Log Instance default=0
  LineNum Int(11) Line Number
  DpmObjType Int(11) Down Payment Type
  DpmDocEntr Int(11) Down Payment Entry
  DpmDocNum Int(11) Down Payment No.
  PmnObjType Int(11) Payment Type
  PmnDocEntr Int(11) Payment Entry
  PmnDocNum Int(11) Payment Number
  PmnTaxDate Date(8) Payment Date
  TrsfrDate Date(8) Transfer Date
  TrsfrRef nVarChar(27) Intended Purpose
  DrawnSum Num(19,6) Drawn Amount
  DrawnSumFc Num(19,6) Drawn Amount (FC)
  DrawnSumSc Num(19,6) Drawn Amount (SC)
  DocCur nVarChar(3) Document Currency
  Vat Num(19,6) Tax Amount
  VatFc Num(19,6) Tax Amount (FC)
  VatSc Num(19,6) Tax Amount (SC)
  Gross Num(19,6) Gross Amount
  GrossFc Num(19,6) Gross Amount (FC)
  GrossSc Num(19,6) Gross Amount (SC)

# TXI1 - Tax Invoice - Rows
Module: Marketing Documents | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BaseEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  BaseEntry Int(11) Base Document Internal ID ->OTSI
  LineNum Int(11) Row Number
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  DocType VarChar(1) Document Type default=I [I=Invoice, P=Payment, J=Journal Entry, C=Correction Invoice, L=Landed Cost]
  RefEntry1 Int(11) Ref.1 Document Key
  RefEntry2 Int(11) Ref.1 Document Key
  ObjType Int(6) Object Type ->ADP1
  LogInstanc Int(11) Log Instance default=0
  RefType Int(11) Ref. Object Type default=-1 [-1=, 13=A/R Invoice, 18=A/P Invoice, 30=Journal Entry, 24=Incoming Payment, 204=A/P Down Payment, 165=A/R Correction Invoice, 163=A/P Correction Invoice, 69=Landed Cost]
  EncryptIV nVarChar(100) Encrypt IV

# TXI2 - Tax Invoice - Operation Codes
Module: Marketing Documents | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BaseEntry, LineNum, OpCode
Fields (name type(len) description [values] ->parent table):
  BaseEntry Int(11) Abs. Entry ->OTSI
  LineNum Int(11) Base Doc. Abs. Entry ->TSI1
  OpCode Int(11) Operation Code ->OBSI
  ObjType Int(11) Object Type ->ADP1
  LogInstanc Int(11) Log Instance default=0

# TXI3 - Tax Invoice - Document Reference Information
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjType Int(11) Object Type
  LogInstanc Int(11) Log Instance default=0
  LineNum Int(11) Line Number
  RefDocEntr Int(11) Referenced Internal Number
  RefDocNum Int(11) Referenced Document Number
  ExtDocNum nVarChar(100) External Referenced Document Number
  RefObjType nVarChar(20) Referenced Object Type [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 234000031=Return Request, 16=Return, 203=A/R Down Payment, 13=A/R Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 280=A/R Tax Invoice, 1470000113=Purchase Request, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Return Request, 21=Goods Return, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 281=A/P Tax Invoice, 69=Landed Costs, 24=Incoming Payments, 46=Outgoing Payments, 57=Checks for Payment, 321=Internal Reconciliation, 34=Recurring Posting, 30=Journal Entry, 59=Goods Receipt, 60=Goods Issue, 162=Inventory Revaluation, 1470000065=Inventory Counting, 10000071=Inventory Posting, 1250000001=Inventory Transfer Request, 67=Inventory Transfer, 202=Production Order, 13001=Original Invoice, -1=External Document]
  IssueDate Date(8) Date of Issue
  Remark nVarChar(254) Remarks
  CardCode nVarChar(15) Business Partner

# VRT1 - Tax Invoice Report - Rows
Module: Marketing Documents | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TxInvRptNo, SeqNo
Fields (name type(len) description [values] ->parent table):
  TxInvRptNo nVarChar(10) Tax Invoice Report No. ->OVRT
  SeqNo Int(11) Sequence No.
  MD Date(8) Original Date of Line Item
  ItemDesc nVarChar(200) Description of Line Item
  Unit nVarChar(100) Unit of Line Item
  Quantity Num(19,6) Quantity
  UnitPrice Num(19,6) Unit Price
  BaseAmt Num(19,6) Base Amount
  TaxAmt Num(19,6) Tax Amount
  Remark nVarChar(100) Remarks

# VRT2 - Tax Invoice Report Grid Info
Module: Marketing Documents | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TxInvRptNo, GridRow
Fields (name type(len) description [values] ->parent table):
  TxInvRptNo nVarChar(10) Tax Invoice Report No. ->OVRT
  GridRow Int(11) Grid Row Number
  BPLId Int(11) Business Place ID
  BPCode nVarChar(15) BP Code
  BPName nVarChar(100) BP Name
  DocDate Date(8) Doc. Date
  ItemNo nVarChar(50) Item Number
  ItemDes nVarChar(200) Item Description
  TaxCode nVarChar(8) Tax Code
  ItemQty Num(19,6) Item Quantity
  ItemPrice Num(19,6) Item Price
  BaseAmt Num(19,6) Base Amount
  TaxAmt Num(19,6) Tax Amount
  LineType Int(11) Row Type
  DocEntry Int(11) Unique Document ID
  DocType Int(11) Document Type [0=, 13=A/R Invoice, 14=A/R Credit Memo, 203=A/R Down Payment]
  LineNum Int(11) Item Row Number
  Currency nVarChar(3) Currency
  Remark nVarChar(100) Remarks
  LegacyData VarChar(1) Legacy Data default=N [Y=Yes, N=No]
  Quantity Num(19,6) Quantity

# VRW4 - VAT Reposting Wizard Array 4-Selected Branches
Module: Marketing Documents | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, BPLId
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  BPLId Int(11) Assigned Branch ->OBPL

# WDD1 - Documents for Approval - Authorizers
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WddCode, StepCode, UserID
Fields (name type(len) description [values] ->parent table):
  WddCode Int(11) Internal ID
  StepCode Int(11) Stage Key ->OWST
  UserID Int(11) Authorizer Code ->OUSR
  Status VarChar(1) Status default=W [W=Pending, Y=Approved, N=Rejected]
  Remarks nVarChar(254) Remarks
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Request Date
  CreateTime Int(6) Request Time
  UpdateDate Date(8) Date of Update
  UpdateTime Int(6) Update Time
  SortId Int(6) Sort Code
  AuthUpdDat Date(8) Authorizer last update date
  AuthUpdTim Int(11) Authorizer last update time
  Substt Int(11) Substitute Authorizer User ID ->OUSR

# WDD2 - Documents for Approval - Terms
Module: Marketing Documents | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WddCode, CondId
Fields (name type(len) description [values] ->parent table):
  WddCode Int(11) Internal ID
  CondId Int(11) Condition No. [1=Deviation from Credit Limit, 2=Deviation from Commitment, 3=Gross Profit %, 4=Discount %, 5=Deviation from Budget, 6=Total Document]
  opCode Int(6) Ratio [1=Greater than, 2=Greater or Equal, 3=Less than, 4=Less or Equal, 5=Equal, 6=Does not Equal]
  opValue nVarChar(40) Value

# WTQ17 - Inventory Transfer Request - Import Process
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OWTQ
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=1250000001 ->ADP1
  ImpDocType VarChar(1) Type of Importation Document ->OBSI
  ImpDocNum nVarChar(10) Importation Document Number
  DateOfReg Date(8) Date of Registry DI/DSI/DA
  CustClrDat Date(8) Date of Customs Clearance
  ConcActNum nVarChar(30) Drawback Concession Acct No.
  AdditNum nVarChar(30) Additional Number
  AddItmDV Num(19,6) Additional Item Discount Value
  tpVTransp Int(6) Overland Transport Route [1=Maritime, 2=Waterway, 3=Lakeside, 4=Air, 5=Post, 6=Train, 7=Road, 8=Network Transmission, 9=Own Means, 10=Input/Output Fictitious, 11=Courier, 12=Hand Carry]
  DrawSReg nVarChar(11) Drawback - Suspension Regime
  AddFrNavyA Num(19,6) Additional Freight to Navy Authority
  TypeOfImp VarChar(1) Type of Import
  nSeqAdic Int(6) Additional Item Sequential Number

# WTQ18 - Inventory Transfer Request - Export Process
Module: Marketing Documents | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OWTQ
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=1250000001 ->ADP1
  ExpDocType Int(11) Type of Exportation Document default=-1 ->OBNI
  ExpDeclNum Int(11) Exportation Declaration Number
  ExpDeclDat Date(8) Exportation Declaration Date
  ExpNature Int(11) Nature of Exportation default=-1 ->OBNI
  ExpRegNum Int(11) Number of Exportation Registry
  ExpRegDate Date(8) Date of Exportation Registry
  LadBillNum nVarChar(19) Bill of Lading Number
  LadBillDat Date(8) Date of Bill of Lading
  MerchLeftD Date(8) Date Merchandise Left Customs
  LadBillTyp Int(11) Type of Bill of Lading default=-1 ->OBNI
  DrawSReg nVarChar(11) Drawback - Suspension Regime
  NatureExp nVarChar(44) Nature of Export
  QultExpItm Num(19,6) Quantity of Exported Items
  nSeqAdic Int(6) Additional Item Sequential Number

# WTQ20 - Intrastat Expenses
Module: Marketing Documents | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OWTQ
  ExpnsCode Int(11) Freight Code ->OEXD
  TotalLC Num(19,6) Total
  TotalFC Num(19,6) Total (FC)
  TotalSC Num(19,6) Total (SC)
  DistribM VarChar(1) Distribution Method default=T [Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DrawnLC Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  LineNum Int(11) Line Number default=-1
  BaseAbsEnt Int(11) Base Abs. Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 16=Return, 13=A/R Invoice, 203=Down Payment Incoming, 204=Down Payment Outgoing, 22=Purchase Order, 20=Goods Receipt PO, 21=Goods Return, 18=A/P Invoice, 540000006=Purchase Quotation, 0=, -1=]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No. default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=1250000001 ->ADP1
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  AppliedLC Num(19,6) Applied
  AppliedFC Num(19,6) Applied (FC)
  AppliedSC Num(19,6) Applied (SC)

# WTQ22 - Inventory Transfer Request - Resource Costs
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, StdCostNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->WTQ1
  LineNum Int(11) Row Number ->WTQ1
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=1250000001
  LogInstanc Int(11) Log Instance default=0

# WTQ23 - A/P Invoice - Selected Asset Master Data
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, VisOrder
  ASSETS: DocEntry, LineNum, AssetCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OWTQ
  LineNum Int(11) Row Number
  AssetCode nVarChar(50) Selected Asset Code ->OITM
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Remarks nVarChar(100) Remarks
  Amount Num(19,6) Amount
  AmountSC Num(19,6) Amount (SC)
  SerialNo nVarChar(30) Serial Number
  VisOrder Int(11) Visual Order
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=1250000001 ->ADP1

# WTQ24 - Inventory Transfer Request - Tracking Note Assignment
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  ItemCCDNum nVarChar(40) Item CCD Number
  CntrOrigin nVarChar(3) Country/Region of Origin
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=1250000001 ->ADP1
  SubLineNum Int(11) BOM Line No.

# WTQ25 - Inventory Transfer Request - Amt Per VAT Grp
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, VatGroup, Type
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  VatGroup nVarChar(8) Tax Definition ->OVTG
  VatPrcnt Num(19,6) Tax Rate
  BaseAmnt Num(19,6) Base Amount
  BaseAmntFC Num(19,6) Base Amount (FC)
  BaseAmntSC Num(19,6) Base Amount (SC)
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  Type Int(11) Type default=1 [1=Discount by Tax]
  Currency nVarChar(3) Price Currency
  Rate Num(19,6) Currency Rate
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=1250000001 ->ADP1

# WTQ28 - Inventory Transfer Request - Reported Tracking Note
Module: Marketing Documents | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
  TCN_KEY U: DocEntry, LineNum, TrackingNt, TrackiNtLn
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  UnusedQty Num(19,6) Unused Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=1250000001 ->ADP1
  SubLineNum Int(11) BOM Line No.

# WTR17 - Inventory Transfer - Import Process
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OWTR
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=67 ->ADP1
  ImpDocType VarChar(1) Type of Importation Document ->OBSI
  ImpDocNum nVarChar(10) Importation Document Number
  DateOfReg Date(8) Date of Registry DI/DSI/DA
  CustClrDat Date(8) Date of Customs Clearance
  ConcActNum nVarChar(30) Drawback Concession Acct No.
  AdditNum nVarChar(30) Additional Number
  AddItmDV Num(19,6) Additional Item Discount Value
  tpVTransp Int(6) Overland Transport Route [1=Maritime, 2=Waterway, 3=Lakeside, 4=Air, 5=Post, 6=Train, 7=Road, 8=Network Transmission, 9=Own Means, 10=Input/Output Fictitious, 11=Courier, 12=Hand Carry]
  DrawSReg nVarChar(11) Drawback - Suspension Regime
  AddFrNavyA Num(19,6) Additional Freight to Navy Authority
  TypeOfImp VarChar(1) Type of Import
  nSeqAdic Int(6) Additional Item Sequential Number

# WTR18 - Inventory Transfer - Export Process
Module: Marketing Documents | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OWTR
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=67 ->ADP1
  ExpDocType Int(11) Type of Exportation Document default=-1 ->OBNI
  ExpDeclNum Int(11) Exportation Declaration Number
  ExpDeclDat Date(8) Exportation Declaration Date
  ExpNature Int(11) Nature of Exportation default=-1 ->OBNI
  ExpRegNum Int(11) Number of Exportation Registry
  ExpRegDate Date(8) Date of Exportation Registry
  LadBillNum nVarChar(19) Bill of Lading Number
  LadBillDat Date(8) Date of Bill of Lading
  MerchLeftD Date(8) Date Merchandise Left Customs
  LadBillTyp Int(11) Type of Bill of Lading default=-1 ->OBNI
  DrawSReg nVarChar(11) Drawback - Suspension Regime
  NatureExp nVarChar(44) Nature of Export
  QultExpItm Num(19,6) Quantity of Exported Items
  nSeqAdic Int(6) Additional Item Sequential Number

# WTR20 - Intrastat Expenses
Module: Marketing Documents | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OWTR
  ExpnsCode Int(11) Freight Code ->OEXD
  TotalLC Num(19,6) Total
  TotalFC Num(19,6) Total (FC)
  TotalSC Num(19,6) Total (SC)
  DistribM VarChar(1) Distribution Method default=T [Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DrawnLC Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  LineNum Int(11) Line Number default=-1
  BaseAbsEnt Int(11) Base Abs. Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 16=Return, 13=A/R Invoice, 203=Down Payment Incoming, 204=Down Payment Outgoing, 22=Purchase Order, 20=Goods Receipt PO, 21=Goods Return, 18=A/P Invoice, 540000006=Purchase Quotation, 0=, -1=]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No. default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=67 ->ADP1
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  AppliedLC Num(19,6) Applied
  AppliedFC Num(19,6) Applied (FC)
  AppliedSC Num(19,6) Applied (SC)

# WTR22 - Inventory Transfer - Resource Costs
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, StdCostNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->WTR1
  LineNum Int(11) Row Number ->WTR1
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=67
  LogInstanc Int(11) Log Instance default=0

# WTR23 - A/P Invoice - Selected Asset Master Data
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, VisOrder
  ASSETS: DocEntry, LineNum, AssetCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OWTR
  LineNum Int(11) Row Number
  AssetCode nVarChar(50) Selected Asset Code ->OITM
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Remarks nVarChar(100) Remarks
  Amount Num(19,6) Amount
  AmountSC Num(19,6) Amount (SC)
  SerialNo nVarChar(30) Serial Number
  VisOrder Int(11) Visual Order
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=67 ->ADP1

# WTR24 - Inventory Transfer - Tracking Note Assignment
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  ItemCCDNum nVarChar(40) Item CCD Number
  CntrOrigin nVarChar(3) Country/Region of Origin
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=67 ->ADP1
  SubLineNum Int(11) BOM Line No.

# WTR25 - Inventory Transfer - Amt Per VAT Grp
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, VatGroup, Type
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  VatGroup nVarChar(8) Tax Definition ->OVTG
  VatPrcnt Num(19,6) Tax Rate
  BaseAmnt Num(19,6) Base Amount
  BaseAmntFC Num(19,6) Base Amount (FC)
  BaseAmntSC Num(19,6) Base Amount (SC)
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  Type Int(11) Type default=1 [1=Discount by Tax]
  Currency nVarChar(3) Price Currency
  Rate Num(19,6) Currency Rate
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=67 ->ADP1

# WTR26 - Inventory Transfer - E-Way Bill Information
Module: Marketing Documents | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OWTR
  SuplyType nVarChar(20) EWB Transaction Type [O=Outward, I=Inward]
  SubSplyTyp Int(11) EWB Sub-Type ->OEST
  DocType nVarChar(3) EWB Doc. Type ->OEDT
  TransMode Int(11) EWB Transportation Mode ->OETM
  Distance Num(19,6) EWB Transport Distance
  TransDocNo nVarChar(16) EWB Transporter Doc. No.
  TransDate Date(8) EWB Transportation Date
  VehicleTyp nVarChar(2) EWB Vehicle Type ->OEVT
  VehicleNo nVarChar(15) EWB Vehicle Number
  EWayBillNo nVarChar(20) EWB No.
  EwbDate Date(8) E-Way Bill Date
  FrmTraName nVarChar(100) EWB Consignor Name
  FrmAddres1 nVarChar(120) EWB Consignor Address 1
  FrmAddres2 nVarChar(120) EWB Consignor Address 2
  FrmZipCode nVarChar(20) EWB Consignor Zip Code
  ActFrmStat nVarChar(2) Dispatch State of EWB Consignor
  ToTraName nVarChar(100) EWB Consignee Name
  ToAddres1 nVarChar(120) EWB Consignee Address 1
  ToAddres2 nVarChar(120) EWB Consignee Address 2
  ToZipCode nVarChar(20) EWB Consignee Zip Code
  ActToState nVarChar(2) Ship-To State of EWB Consignee
  FrmGSTN nVarChar(15) EWB Consignor GSTN
  FrmState nVarChar(2) Bill-To State of EWB Consignor
  ToGSTN nVarChar(15) EWB Consignee GSTN
  ToState nVarChar(2) Bill-To State of EWB Consignee
  MainHsnEnt Int(11) EWB Main HSN Entry ->OCHP
  FrmPlace nVarChar(50) EWB Consignor Place
  ToPlace nVarChar(50) EWB Consignee Place
  TransID nVarChar(15) EWB Transporter ID
  TransName nVarChar(25) EWB Transporter Name
  ExpireDate Date(8) EWB Expiration Date
  ObjectType nVarChar(20) Object Type default=67 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TspEntry Int(11) Transporter Abs. Entry ->OTSP
  TspLine Int(11) Transportation Line
  TransType Int(11) Transaction Type [1=Regular, 2=Bill To-Ship To, 3=Bill From-Dispatch From, 4=Combination of 2 and 3]

# WTR27 - Inventory Transfer - E-Books(GR) Rows
Module: Marketing Documents | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  RELATE_ROW: DocEntry, RelateType, RelateLine, GroupNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OWTR
  LineNum Int(11) Row Number
  RelateType Int(11) Relation Type default=-1 [1=Row, 2=Row Expenses, 3=Document Expenses, 13=Distributed Freights, -1=Manual]
  RelateLine Int(11) Relation Row Number default=-1
  GroupNum Int(11) Group Number default=-1
  LineTotal Num(19,6) Line Total
  LineTotalF Num(19,6) Line Total (FC)
  LineTotalS Num(19,6) Line Total (SC)
  InClassTyp Int(11) Income Classification Type ->OICP
  InClassCat Int(11) Income Classification Category ->OICC
  ExClassTyp Int(11) Expense Classification Type ->OECP
  ExClassCat Int(11) Expense Classification Cat. ->OECC
  VatCate Int(11) VAT Category
  NetValue Num(19,6) Net Value
  NetValueFC Num(19,6) Net Value (FC)
  NetValueSC Num(19,6) Net Value (SC)
  VatAmount Num(19,6) VAT Amount
  VatAmFC Num(19,6) VAT Amount (FC)
  VatAmSC Num(19,6) VAT Amount (SC)
  WtPercCat Int(11) Withheld Percentage Category
  WtAmount Num(19,6) Withheld Amount
  WtAmountFC Num(19,6) Withheld Amount (FC)
  WtAmountSC Num(19,6) Withheld Amount (SC)
  ObjectType nVarChar(20) Object Type default=13 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  WtCategory VarChar(1) Withheld Category [I=Invoice, P=Payment]
  VATClassTy Int(11) VAT Classification Type ->OECP
  VATClassCa Int(11) VAT Classification Category ->OECC
  EBVatExCau Int(11) VAT Exemption Cause ->OVEC

# WTR28 - Inventory Transfer - Reported Tracking Note
Module: Marketing Documents | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
  TCN_KEY U: DocEntry, LineNum, TrackingNt, TrackiNtLn
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  UnusedQty Num(19,6) Unused Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=67 ->ADP1
  SubLineNum Int(11) BOM Line No.
