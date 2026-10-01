<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# WTR1 - Inventory Transfer - Rows
Module: Inventory and Production | 317 columns
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
  DocEntry Int(11) Document Internal ID ->OWTR
  LineNum Int(11) Row Number
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=, 20=Goods Receipt, 18=A/P Invoice, 204=A/P Down Payment]
  TrgetEntry Int(11) Target Document Internal ID
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 20=Purchase Delivery Notes, 59=Inventory General Entry, 67=Warehouses Transfers, 1250000001=Inventory Transfer Request]
  BaseEntry Int(11) Base Document Internal ID
  BaseLine Int(11) Base Row
  LineStatus VarChar(1) Row Status default=O [O=Open, C=Closed]
  ItemCode nVarChar(50) Item Code ->OITM
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
  TreeType VarChar(1) Tree Type default=N [N=Not a BOM, A=Assembly, S=Sales, I=Sales BOM Component, P=Production, T=Template]
  AcctCode nVarChar(15) Account Code ->OACT
  TaxStatus VarChar(1) Tax Definition [Y=Yes, N=No]
  GrossBuyPr Num(19,6) Gross Profit Base Price
  PriceBefDi Num(19,6) Price Before Discount
  DocDate Date(8) Posting Date
  Flags Int(11) Flags default=0
  OpenCreQty Num(19,6) Credit Memo Amount
  UseBaseUn VarChar(1) Inventory UoM default=Y [Y=Yes, N=No]
  SubCatNum nVarChar(50) BP Catalog No. ->OSCN
  BaseCard nVarChar(15) Base Card Code ->OCRD
  TotalSumSy Num(19,6) Row Total in FC
  OpenSumSys Num(19,6) Open Amount in System Currency
  InvntSttus VarChar(1) Whse Status default=O [O=Open, C=Closed]
  OcrCode nVarChar(8) Costing Code ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  CodeBars nVarChar(254) Bar Code
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
  VolUnit Int(6) Unit of Measure
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
  SWW nVarChar(16) SWW
  VatSum Num(19,6) Tax Total
  VatSumFrgn Num(19,6) Tax Sum (FC)
  VatSumSy Num(19,6) Tax Sum (SC)
  FinncPriod Int(11) Posting Period ->OFPR
  ObjType nVarChar(20) Object Type default=67 ->ADP1
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
  PoTrgEntry nVarChar(11) PO Target Entry
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
  VatAppld Num(19,6) VAT Applied
  VatAppldFC Num(19,6) VAT Applied FC
  VatAppldSC Num(19,6) VAT Applied SC
  BaseQty Num(19,6) Base Quantity
  BaseOpnQty Num(19,6) Base Open Quantity
  VatDscntPr Num(19,6) VAT Discount Percent
  WtLiable VarChar(1) WT Liable [Y=Yes, N=No]
  DeferrTax VarChar(1) DeferredTax default=N [Y=Yes, N=No]
  EquVatPer Num(19,6) Equalization Tax Percentage
  EquVatSum Num(19,6) Equalization Tax Total
  EquVatSumF Num(19,6) Equalization Tax Total FC
  EquVatSumS Num(19,6) Equalization Tax Total SC
  LineVat Num(19,6) Net Tax Sum
  LineVatlF Num(19,6) Net Tax Sum
  LineVatS Num(19,6) Net Tax Sum
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value
  CEECFlag VarChar(1) Correction Invoice Item W/S default=S [W=Was, S=Should be]
  ToStock Num(19,6) Corr Inv. Amount to Stock
  ToDiff Num(19,6) Corr Inv. Amount to Diff. Acct
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
  StockPrice Num(19,6) Stock Price
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
  AgrNo Int(11) Agreement No.
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
