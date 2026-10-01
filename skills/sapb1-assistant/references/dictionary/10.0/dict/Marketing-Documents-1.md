<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->

# ACM1 - Input Service Distribution - Credit Memo Lines
Module: Marketing Documents | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OISI
  LineNum Int(11) Row Number
  SourceType Int(11) Source Document Type [18=GST Tax Invoice, 19=GST Credit Memo, -18=GST Debit Memo]
  SourceNo Int(11) Source Document No.
  SrcEntry Int(11) Source Document Entry
  SrcStaType Int(11) Source GST Tax Type [-100=CGST, -110=SGST, -120=IGST, -130=Cess GST, -150=UTGST]
  SrcTaxAcct nVarChar(15) Source Tax Account
  SACEntry Int(11) SAC Entry
  TarStaType Int(11) Target GST Tax Type [-100=CGST, -110=SGST, -120=IGST, -130=Cess GST, -150=UTGST]
  TarTaxAcct nVarChar(15) Target Tax Account
  DistAmnt Num(19,6) Credit Amount to Distribute
  SrcSubType nVarChar(2) Source Document Subtype
  ITCType VarChar(1) ITC Type default=E [E=Eligible, I=Ineligible]

# ADO1 - Marketing Document (Rows) - History
Module: Marketing Documents | 317 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LogInstanc, ObjType
  ITEM_WHS: ItemCode, WhsCode
  ITEM: ItemCode
  STATUS: LineStatus
  CURRENCY: Currency
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ADOC
  LineNum Int(11) Row Number
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=, 19=Purchase credit note, 59=Goods Receipt]
  TrgetEntry Int(11) Target Document Internal ID
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 23=Sales Quotation, 17=Sales Order, 16=A/R Returns, 13=Invoices, 15=Delivery notes, 18=Purchases, 20=Purchase Delivery Notes, 21=Revert Purchase Delivery Notes, 22=Purchase orders, 60=Goods Issue, 202=Production Order]
  BaseEntry Int(11) Base Document Internal ID
  BaseLine Int(11) Base Row
  LineStatus VarChar(1) Row Status default=O [O=Open, C=Closed]
  ItemCode nVarChar(50) Item No. ->OITM
  Dscription nVarChar(200) Item/Service Description
  Quantity Num(19,6) Quantity
  ShipDate Date(8) Row Shipping Date
  OpenQty Num(19,6) Remaining Open Quantity
  Price Num(19,6) Price
  Currency nVarChar(3) Price Currency ->OCRN
  Rate Num(19,6) Currency Rate
  DiscPrcnt Num(19,6) Discount % per Row
  LineTotal Num(19,6) Total Row
  TotalFrgn Num(19,6) Total Row (FC)
  OpenSum Num(19,6) Open Amount
  OpenSumFC Num(19,6) Open Amount (FC)
  VendorNum nVarChar(50) Vendor Catalog No.
  SerialNum nVarChar(17) Serial Number
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  SlpCode Int(11) Sales Employee Code default=-1 ->OSLP
  Commission Num(19,6) Commission %
  TreeType VarChar(1) Bill of Materials Type default=N [N=Not a BOM, A=Assembly, S=Sales, I=Sales BOM Component, P=Production, T=Template]
  AcctCode nVarChar(15) Account Code ->OACT
  TaxStatus VarChar(1) Tax Definition [Y=Yes, N=No]
  GrossBuyPr Num(19,6) Gross Profit Base Price
  PriceBefDi Num(19,6) Price Before Discount
  DocDate Date(8) Posting Date
  Flags Int(11) Flags default=0
  OpenCreQty Num(19,6) Credited Quantity
  UseBaseUn VarChar(1) Inventory UoM default=N [Y=Yes, N=No]
  SubCatNum nVarChar(50) BP Catalog No. ->OSCN
  BaseCard nVarChar(15) Base BP Code ->OCRD
  TotalSumSy Num(19,6) Total Row (FC)
  OpenSumSys Num(19,6) Open Amount (SC)
  InvntSttus VarChar(1) Whse Status default=O [O=Open, C=Closed]
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  CodeBars nVarChar(254) EAN Code
  VatPrcnt Num(19,6) Tax % per Row
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
  UpdInvntry VarChar(1) Stock Update default=Y [Y=Yes, N=No]
  BaseDocNum Int(11) Base Document No.
  BaseAtCard nVarChar(100) Base Document BP
  SWW nVarChar(16) Additional Identifier
  VatSum Num(19,6) Total Tax
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  FinncPriod Int(11) Posting Period ->OFPR
  ObjType nVarChar(20) Object Type ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BlockNum nVarChar(100) Block No.
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
  PoTrgNum Int(11) PO Target Doc. No.
  PoTrgEntry nVarChar(11) PO Target Doc. Key
  DropShip VarChar(1) Drop Ship - History default=N [Y=Yes, N=No]
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
  WtLiable VarChar(1) WT Liable [Y=Yes, N=No]
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
  ToStock Num(19,6) Corr. Invoice Amount to Stock
  ToDiff Num(19,6) Corr. Invoice Amount to Diff.
  ExciseAmt Num(19,6) Excise Amount
  TaxPerUnit Num(19,6) Tax per Unit
  TotInclTax Num(19,6) Total (incl. Tax)
  CountryOrg nVarChar(3) Country/Region of Origin
  StckDstSum Num(19,6) Stock Distribute Sum
  ReleasQtty Num(19,6) Released Quantity
  LineType VarChar(1) Line Type default=R [R=Regular, M=Resource]
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
  GTotalFC Num(19,6) Gross Total (FC)
  GTotalSC Num(19,6) Gross Total (SC)
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
  ChgAsmBoMW VarChar(1) Change Whse for Asm BoM Child [Y=Yes, N=No]
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
  ItemType Int(11) Item Type default=4 [4=Item, 290=Resource]
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

# ADO10 - Marketing Document - Row Structure - History
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq, ObjType, LogInstanc
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ADOC
  LineSeq Int(11) Row Sequence
  AftLineNum Int(11) After Row Number
  OrderNum Int(11) Order Number
  LineType VarChar(1) Row Type [T=Text, S=Subtotal]
  LineText Text(16) Row Text
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=23 ->ADP1

# ADO11 - Marketing Document (Drawn Dpm Det) - Hist
Module: Marketing Documents | 70 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LineSeq, ObjType, LogInstanc
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ADOC
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
  ObjType nVarChar(20) Object Type default=13 ->ADP1
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

# ADO12 - Marketing Document - Tax Extension - History
Module: Marketing Documents | 117 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LogInstanc, ObjectType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ADOC
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
  Carrier nVarChar(15) Carrier Code
  QoP Int(11) Quantity of Packs
  PackDesc nVarChar(10) Pack Description
  Brand nVarChar(20) Brand
  NoSU Int(11) Number of Shipping Unit
  NetWeight Num(19,6) Net Weight
  GrsWeight Num(19,6) Gross Weight
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type ->ADP1
  TaxId10 nVarChar(100) Assessee Type
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
  Vat VarChar(1) VAT default=N [N=, Y=]
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

# ADO13 - Marketing Document Rows - Distributed Expenses
Module: Marketing Documents | 59 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum, LogInstanc, ObjType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ADOC
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type ->ADP1
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

# ADO14 - Marketing Document - Assembly - Rows - History
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum, LogInstanc, ObjectType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ADOC
  LineNum Int(11) Row Number default=-1
  ChildNum Int(11) Child Number default=-1
  ItemCode nVarChar(50) Item no. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  TotalQty Num(19,6) Total Quantity
  OpenQty Num(19,6) Remaining Open Quantity
  ObjectType nVarChar(20) object type ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BaseChildN Int(11) Base Child Number default=-1
  EncryptIV nVarChar(100) Encrypt IV

# ADO15 - Marketing Document (Drawn Dpm Applied) - Hist
Module: Marketing Documents | 84 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ObjType, LogInstanc
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Number ->ADOC
  LineNum Int(11) Row Number
  ObjType nVarChar(20) object type default=13 ->ADP1
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

# ADO16 - Draft - SnB properties
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, SnBIndex, LogInstanc, ObjType
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Document Number ->ADOC
  LineNum Int(11) Row Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjId Int(11) Object ID
  ObjAbs Int(11) SnB Object No.
  DrfWObjAbs Int(11) SnBW Draft Object No. default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance

# ADO17 - Marketing Document - Import Process - History
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LogInstanc, ObjectType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ADOC
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type ->ADP1
  ImpDocType VarChar(1) Importation Document Type ->OBSI
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

# ADO18 - Marketing Document - Export Process - History
Module: Marketing Documents | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LogInstanc, ObjectType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ADOC
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=166 ->ADP1
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

# ADO19 - Bin Allocation Data - History
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, BinAllocSe, LogInstanc, ObjType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->ADOC
  BinAllocSe Int(11) Bin Allocation Sequence
  LineNum Int(11) Line Number
  SubLineNum Int(11) Subline Number default=-1
  SnBType Int(11) SnB Type default=-1
  SnBMDAbs Int(11) SnB Master Data Internal No. default=-1
  BinAbs Int(11) Bin Internal Number ->OBIN
  Quantity Num(19,6) Quantity
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjType nVarChar(20) Object Type ->ADP1
  LogInstanc Int(11) Log Instance default=0
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  BinActTyp Int(6) Bin Action Type [1=Transaction In, 2=Transaction Out, 4=SnB Complete, 8=Bin First Then SnB]

# ADO2 - Marketing Document - Freight - Rows
Module: Marketing Documents | 64 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum, LogInstanc, ObjType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ADOC
  LineNum Int(11) Row Number
  GroupNum Int(11) Group No.
  ExpnsCode Int(11) Expense Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type ->ADP1
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
  WtLiable VarChar(1) WT Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
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

# ADO20 - Intrastat Expenses
Module: Marketing Documents | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LogInstanc, ObjectType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ADOC
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
  ObjectType nVarChar(20) Object Type default=166 ->ADP1
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  AppliedLC Num(19,6) Applied
  AppliedFC Num(19,6) Applied (FC)
  AppliedSC Num(19,6) Applied (SC)

# ADO21 - Marketing Document - Document Reference Information - History
Module: Marketing Documents | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LogInstanc, ObjectType, RefType
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjectType nVarChar(20) Object Type default=0
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

# ADO22 - Marketing Document (Resource Costs) - History
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, StdCostNum, LogInstanc, ObjectType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ADO1
  LineNum Int(11) Row Number ->ADO1
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=13
  LogInstanc Int(11) Log Instance default=0

# ADO23 - Marketing Document - Selected Asset Master Data
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, VisOrder, LogInstanc, ObjectType
  ASSETS: DocEntry, LineNum, AssetCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ADO1
  LineNum Int(11) Row Number
  AssetCode nVarChar(50) Selected Asset Code ->OITM
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Remarks nVarChar(100) Remarks
  Amount Num(19,6) Amount
  AmountSC Num(19,6) Amount (SC)
  SerialNo nVarChar(30) Serial Number
  VisOrder Int(11) Visual Order
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=20 ->ADP1

# ADO24 - Marketing Document - Tracking Note Assignment - History
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum, LogInstanc, ObjType
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
  ObjType nVarChar(20) Object Type default=0 ->ADP1
  SubLineNum Int(11) BOM Line No.

# ADO25 - Marketing Document - Amt Per VAT Grp - History
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, VatGroup, Type, LogInstanc, ObjType
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
  ObjType nVarChar(20) Object Type default=0 ->ADP1

# ADO26 - Marketing Document - E-Way Bill Information - History
Module: Marketing Documents | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LogInstanc, ObjectType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ADOC
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
  ObjectType nVarChar(20) Object Type ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TspEntry Int(11) Transporter Abs. Entry ->OTSP
  TspLine Int(11) Transportation Line
  TransType Int(11) Transaction Type [1=Regular, 2=Bill To-Ship To, 3=Bill From-Dispatch From, 4=Combination of 2 and 3]

# ADO27 - Marketing Document - E-Books(GR) Rows - History
Module: Marketing Documents | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LogInstanc, ObjectType
  RELATE_ROW: DocEntry, RelateType, RelateLine, GroupNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ADOC
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

# ADO28 - Marketing Document - Reported Tracking Note - History
Module: Marketing Documents | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum, LogInstanc, ObjType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  UnusedQty Num(19,6) Unused Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=0 ->ADP1
  SubLineNum Int(11) BOM Line No.

# ADO3 - Marketing Document - Freight - History
Module: Marketing Documents | 80 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LogInstanc, ObjType
  DOCUMENT: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ADOC
  ExpnsCode Int(11) Expense Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  Comments nVarChar(100) Remarks
  ObjType nVarChar(20) Object Type ->ADP1
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
  IsAcquistn VarChar(1) Aquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  WTLiable VarChar(1) WT Liable [Y=Yes, N=No]
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
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 13=Invoices, 15=Delivery notes, 16=Revert Delivery Notes, 17=Orders, 18=Purchases, 20=Purchase Delivery Notes, 21=Revert Purchase Delivery Notes, 22=Purchase orders, 23=Quotations]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Line No.
  LineNum Int(11) line num default=-1
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Abs. Entry default=-1
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

# ADO4 - Documents - Tax - History
Module: Marketing Documents | 61 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq, ObjectType, LogInstanc
  SCONDARY: DocEntry, LineNum, GroupNum, ExpnsCode, StcCode, StaCode, staType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ADOC
  LineNum Int(11) Row Number default=-1
  GroupNum Int(11) Group No. default=-1
  ExpnsCode Int(11) Expense Code default=-1 ->OEXD
  RelateType Int(11) Relation Type default=1 [1=Row, 2=Row Freight Charges, 3=Document Expenses, 13=Distributed Freights]
  StcCode nVarChar(8) Tax Code ->OSTC
  StaCode nVarChar(8) Tax Code ->OSTA
  staType Int(11) Authority Type ->OSTT
  TaxRate Num(19,6) Authority Type ->OSTT
  TaxAcct nVarChar(15) Authority Code
  TaxSum Num(19,6) Tax % ->OACT
  TaxSumFrgn Num(19,6) Tax Account
  TaxSumSys Num(19,6) Tax Amount
  BaseSum Num(19,6) Tax Amount (FC)
  BaseSumFrg Num(19,6) Base Amount
  BaseSumSys Num(19,6) Base Amount (FC)
  ObjectType nVarChar(20) Base Amount (SC)
  LogInstanc Int(11) Tax Amount (SC) default=0 ->ADP1
  TaxStatus VarChar(1) Base Amount default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
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

# ADO5 - Withholding Tax - History
Module: Marketing Documents | 158 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, LogInstanc, ObjType
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator ->ADOC
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
  Criteria VarChar(1) WTax Criteria [Y=Accrual, N=Cash]
  Account nVarChar(15) G/L Account ->OACT
  Type VarChar(1) Withholding Type [V=VAT Withholding, I=Income Tax Withholding]
  RoundType VarChar(1) Rounding Type [T=Truncated, C=Commercial Values, N=No Rounding]
  BaseType VarChar(1) Base Type [G=Gross, N=Net, V=VAT, U=UoM]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseLine Int(11) Base Line
  BaseNum Int(11) Base Document Type default=-1 [-1=, 0=, 13=Invoices, 15=Delivery notes, 16=Revert Delivery Notes, 17=Orders, 18=Purchases, 20=Purchase Delivery Notes, 21=Revert Purchase Delivery Notes, 22=Purchase orders, 23=Quotations]
  LineNum Int(11) Line Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Abs. Entry default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type ->ADP1
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

# ADO6 - Documents History - Installments
Module: Marketing Documents | 65 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, InstlmntID, LogInstanc, ObjType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ADOC
  InstlmntID Int(6) Installment ID default=1
  ObjType nVarChar(20) Object Type ->ADP1
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
  ExpnsBlck Num(19,6) Reserved Freight Amount
  ExpnsBlckF Num(19,6) Reserved Freight Amount (FC)
  ExpnsBlckS Num(19,6) Reserved Freight Amount (SC)
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

# ADO7 - Delivery Packages - History
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum, ObjType, LogInstanc
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ADOC
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type ->ADP1
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV

# ADO8 - Items in Package - History
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum, ItemCode, UomEntry, NumPerMsr, ObjType, LogInstanc
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ADOC
  PackageNum Int(11) Package Number
  ItemCode nVarChar(50) Item Code ->OITM
  Quantity Num(19,6) Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type ->ADP1
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value default=0

# ADO9 - Marketing Document (Rows) - History
Module: Marketing Documents | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ObjCode, LogInstanc
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ADOC
  LineNum Int(11) Row Number
  BaseAbs Int(11) Base Document Internal ID
  BaseLine Int(11) Base Document Row
  TargetBase VarChar(1) Target or Base Document default=B [B=Base, T=Target]
  ObjType nVarChar(20) Base Object Type
  DrawnSum Num(19,6) Net LC
  DrawnSumFc Num(19,6) Net FC
  DrawnSumSc Num(19,6) Net SC
  LogInstanc Int(11) Log Instance default=0
  ObjCode nVarChar(20) Object Type ->ADP1
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

# ADOC - Invoice - History
Module: Marketing Documents | 448 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, ObjType, LogInstanc
  AT_CARD: NumAtCard, CardCode
  CUSTOMER: CardCode
  NUM: DocNum, Instance, LogInstanc, ObjType, Segment
  DOC_STATUS: DocStatus, CANCELED
  FTHR_CARD: FatherCard, FatherType
  SERIES: Series
  DOC_ABSREF: DocEntry, ObjType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Numerator
  DocNum Int(11) Document Number
  DocType VarChar(1) Document Type default=I [I=Item, S=Service]
  CANCELED VarChar(1) Canceled default=N [Y=Yes, N=No, C=Cancellation]
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  Printed VarChar(1) Printed default=N [Y=Copy, N=Original, A=Amended]
  DocStatus VarChar(1) Document Status default=O [O=Open, C=Closed]
  InvntSttus VarChar(1) Inventory Status default=O [O=Open, C=Closed]
  Transfered VarChar(1) Year Transferred default=N [Y=Yes, N=No]
  ObjType nVarChar(20) Object Type ->ADP1
  DocDate Date(8) Posting Date
  DocDueDate Date(8) Value Date
  CardCode nVarChar(15) BP Code ->OCRD
  CardName nVarChar(100) BP Name
  Address nVarChar(254) Bill To
  NumAtCard nVarChar(100) Customer/Vendor Ref. No.
  VatPercent Num(19,6) Tax %
  VatSum Num(19,6) Total Tax
  VatSumFC Num(19,6) Tax Amount (FC)
  DiscPrcnt Num(19,6) Discount % for Document
  DiscSum Num(19,6) Total Discount
  DiscSumFC Num(19,6) Total Discount (FC)
  DocCur nVarChar(3) Document Currency ->OCRN
  DocRate Num(19,6) Document Rate
  DocTotal Num(19,6) Total Document
  DocTotalFC Num(19,6) Total Document (FC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  GrosProfit Num(19,6) Gross Profit
  GrosProfFC Num(19,6) Gross Profit (FC)
  Ref1 nVarChar(11) Ref. 1
  Ref2 nVarChar(11) Ref. 3
  Comments nVarChar(254) Remarks
  JrnlMemo nVarChar(254) Journal Remark
  TransId Int(11) Transaction Number ->OJDT
  ReceiptNum Int(11) Incoming Payment No.
  GroupNum Int(6) Payment Terms Code ->OCTG
  DocTime Int(6) Creation Time
  SlpCode Int(11) Sales Employee default=-1 ->OSLP
  TrnspCode Int(6) Shipping Type default=-1 ->OSHP
  PartSupply VarChar(1) Partial Delivery default=Y [Y=Yes, N=No]
  Confirmed VarChar(1) Confirmed default=Y [Y=Yes, N=No]
  GrossBase Int(6) Price List for Gross Profit default=0
  ImportEnt Int(11) Order No. ->OIPF
  CreateTran VarChar(1) Create Journal Entry default=N [Y=Yes, N=No]
  SummryType VarChar(1) Consolidation Method default=N [N=No Summary, I=By Items, D=By Documents]
  UpdInvnt VarChar(1) Stock Update default=N [N=No, O=Orders from Vendors, C=Customer Orders, G=Consignment, I=Stock]
  UpdCardBal VarChar(1) Update Balances default=N [N=No, O=Orders, D=Delivery Notes, B=Bookkeeping]
  Instance Int(6) Instance default=0
  Flags Int(11) Flags default=0
  InvntDirec VarChar(1) Stock Direction default=X [X=Release, E=Receipt]
  CntctCode Int(11) Contact Person ->OCPR
  ShowSCN VarChar(1) Display BP Catalog Number default=N [Y=Yes, N=No]
  FatherCard nVarChar(15) BP Consolidation ->OCRD
  SysRate Num(19,6) Price (SC)
  CurSource VarChar(1) Base Currency default=C [L=Local Currency, S=System Currency, C=BP Currency]
  VatSumSy Num(19,6) Tax Amount (SC)
  DiscSumSy Num(19,6) Total Discount (SC)
  DocTotalSy Num(19,6) Total Document (SC)
  PaidSys Num(19,6) Paid (SC)
  FatherType VarChar(1) Parent Consolidation Type default=P [P=Payment Consolidation, D=Delivery Consolidation]
  GrosProfSy Num(19,6) Gross Profit (SC)
  UpdateDate Date(8) Update Date
  IsICT VarChar(1) A/R Invoice + Payment default=N [Y=Yes, N=No]
  CreateDate Date(8) Creation Date
  Volume Num(19,6) Volume
  VolUnit Int(6) Volume UoM
  Weight Num(19,6) Weight
  WeightUnit Int(6) Weight Unit
  Series Int(11) Series ->NNM1
  TaxDate Date(8) Document Date
  Filler nVarChar(8) Filter ->OWHS
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Auto Summary, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  StampNum nVarChar(16) Stamp No.
  isCrin VarChar(1) Correction Invoice default=N [Y=Yes, N=No]
  FinncPriod Int(11) Posting Period ->OFPR
  UserSign Int(6) User Signature ->OUSR
  selfInv VarChar(1) Auto. Invoice default=N [N=No, Y=Yes]
  VatPaid Num(19,6) Tax Paid to Date
  VatPaidFC Num(19,6) Tax Paid (FC)
  VatPaidSys Num(19,6) Tax Paid (SC)
  UserSign2 Int(6) Updating User ->OUSR
  WddStatus VarChar(1) Authorization Status default=- [-=Without, W=Pending, Y=Approved, N=Rejected, P=Generated, A=Generated by Authorizer, C=Canceled]
  draftKey Int(11) Document Draft Internal ID default=-1 ->ODRF
  TotalExpns Num(19,6) Total Expenses
  TotalExpFC Num(19,6) Total Expenses (FC)
  TotalExpSC Num(19,6) Total Expenses (SC)
  DunnLevel Int(11) Dunning Level ->ODUN
  Address2 nVarChar(254) Ship To
  LogInstanc Int(11) Log Instance default=0
  Exported VarChar(1) Exported default=N [Y=Yes, N=No]
  StationID Int(11) Workstation ID ->CSTN
  Indicator nVarChar(2) Indicator ->OIDC
  NetProc VarChar(1) Net Procedure default=N [Y=Yes, N=No]
  AqcsTax Num(19,6) Acquisition Tax
  AqcsTaxFC Num(19,6) Acquisition Tax (FC)
  AqcsTaxSC Num(19,6) Acquisition Tax (SC)
  CashDiscPr Num(19,6) Cash Discount %
  CashDiscnt Num(19,6) Cash Discount
  CashDiscFC Num(19,6) Cash Discount (FC)
  CashDiscSC Num(19,6) Cash Discount (SC)
  ShipToCode nVarChar(50) Ship-to Code
  LicTradNum nVarChar(32) L.T. No.
  PaymentRef nVarChar(27) Payment Reference No.
  WTSum Num(19,6) Withholding Tax Amount
  WTSumFC Num(19,6) WTax Amount (FC)
  WTSumSC Num(19,6) WTax Amount (SC)
  RoundDif Num(19,6) Rounding Diff. Amount
  RoundDifFC Num(19,6) Rounding Diff. Amount (FC)
  RoundDifSy Num(19,6) Rounding Diff. Amount (SC)
  CheckDigit VarChar(1) Control Digit
  Form1099 Int(11) 1099 Form ->OTNN
  Box1099 nVarChar(20) 1099 Box
  submitted VarChar(1) Submitted default=N [Y=Yes, N=No]
  PoPrss VarChar(1) PO Process default=N [Y=Yes, N=No]
  Rounding VarChar(1) Rounding default=N [Y=Yes, N=No]
  RevisionPo VarChar(1) Split PO default=N [Y=Yes, N=No]
  Segment Int(6) Segment default=0
  ReqDate Date(8) Required Date
  CancelDate Date(8) Cancelation Date
  PickStatus VarChar(1) Pick Status default=N [Y=Yes, N=No]
  Pick VarChar(1) Pick default=N [Y=Yes, N=No]
  BlockDunn VarChar(1) Block Dunning default=N [Y=Yes, N=No]
  PeyMethod nVarChar(15) Payment Method ->OPYM
  PayBlock VarChar(1) Payment Block default=N [Y=Yes, N=No]
  PayBlckRef Int(11) Payment Block Abs Entry ->OPYB
  MaxDscn VarChar(1) Max. Discount default=N [Y=Yes, N=No]
  Reserve VarChar(1) Reserved default=N [Y=Yes, N=No]
  Max1099 Num(19,6) Max. 1099 Amount
  CntrlBnk nVarChar(15) Central Bank Indicator ->OCBI
  PickRmrk nVarChar(254) Pick Remarks
  ISRCodLine nVarChar(53) ISR Coding Line
  ExpAppl Num(19,6) Exp applied
  ExpApplFC Num(19,6) Exp applied FC
  ExpApplSC Num(19,6) Exp applied DC
  Project nVarChar(20) Project Code ->OPRJ
  DeferrTax VarChar(1) Deferred Tax [Y=Yes, N=No]
  LetterNum nVarChar(50) Tax Exemption Letter No.
  FromDate Date(8) Exemption Validity Date From
  ToDate Date(8) To
  WTApplied Num(19,6) Applied Withholding Tax
  WTAppliedF Num(19,6) Applied WTax (FC)
  BoeReserev VarChar(1) Bill of Exchange Reserved default=N [Y=Yes, N=No]
  AgentCode nVarChar(32) Agent Code ->OAGP
  WTAppliedS Num(19,6) Applied WTax (SC)
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  Installmnt Int(6) No. of Installments default=1
  VATFirst VarChar(1) Apply Tax on 1st Installment [Y=Yes, N=No]
  NnSbAmnt Num(19,6) WT Non-Subject Amount
  NnSbAmntSC Num(19,6) WT Non Subject Amount (SC)
  NbSbAmntFC Num(19,6) WT Non Subject Amount (FC)
  ExepAmnt Num(19,6) WT Exempted Amount
  ExepAmntSC Num(19,6) WTax Exempt Amount (FC)
  ExepAmntFC Num(19,6) WTax Exempt Amount (FC)
  VatDate Date(8) VAT Date
  CorrExt nVarChar(25) External Corrected Document No.
  CorrInv Int(11) Internal Corrected Document No.
  NCorrInv Int(11) Next Correcting Document
  CEECFlag VarChar(1) Block Creation of Target Corr. Inv. default=N [N=No, Y=Yes]
  BaseAmnt Num(19,6) Base Amount
  BaseAmntSC Num(19,6) Base Amount (SC)
  BaseAmntFC Num(19,6) Base Amount (FC)
  CtlAccount nVarChar(15) Control Account ->OACT
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  VATRegNum nVarChar(32) VAT Reg Number
  TxInvRptNo nVarChar(10) Tax Invoice Rpt Number
  TxInvRptDt Date(8) Tax Invoice Rpt Date
  KVVATCode Text(16) VAT Code for Tax Invoice Rpt
  WTDetails nVarChar(100) WT Details
  SumAbsId Int(11) Summary VAT Abstract ID default=-1
  SumRptDate Date(8) Summary VAT Report Date
  PIndicator nVarChar(10) Period Indicator default=' ' ->OPID
  ManualNum nVarChar(20) Manual Number
  UseShpdGd VarChar(1) Use Shipped Goods Account default=N [N=No, Y=Yes]
  BaseVtAt Num(19,6) BPL ID Assigned to Invoice
  BaseVtAtSC Num(19,6) BPL Name
  BaseVtAtFC Num(19,6) Tax Reg. Number
  NnSbVAt Num(19,6) Tax Invoice Rpt Number
  NnSbVAtSC Num(19,6) Tax Invoice Rpt Date
  NbSbVAtFC Num(19,6) WT Non Subject Vat Amount (FC)
  ExptVAt Num(19,6) WTax Exempted VAT Amount
  ExptVAtSC Num(19,6) WTax Exempted VAT Amount (SC)
  ExptVAtFC Num(19,6) Withholding Tax Details
  LYPmtAt Num(19,6) Last Year's Payments
  LYPmtAtSC Num(19,6) Last Years Payments (SC)
  LYPmtAtFC Num(19,6) Summary Tax Report Date
  ExpAnSum Num(19,6) Period Indicator
  ExpAnSys Num(19,6) Manual Number
  ExpAnFrgn Num(19,6) Use Shipped Goods Account
  DocSubType nVarChar(2) VAT Code for Tax Invoice Rpt default=-- [--=]
  DpmStatus VarChar(1) Summary VAT Abstract ID default=O [O=Open, C=Closed]
  DpmAmnt Num(19,6) Down Payment Amount LC
  DpmAmntSC Num(19,6) Down Payment Amount SC
  DpmAmntFC Num(19,6) Down Payment Amount FC
  DpmDrawn VarChar(1) Drawn to Down Payment default=N [N=No, Y=Yes]
  DpmPrcnt Num(19,6) Down Payment Percent
  PaidSum Num(19,6) Total Paid Sum
  PaidSumFc Num(19,6) Total Paid Sum (FC)
  PaidSumSc Num(19,6) Total Paid Sum (SC)
  FolioPref nVarChar(4) Folio Prefix String
  FolioNum Int(11) Folio Number
  DpmAppl Num(19,6) Down Payment Applied LC
  DpmApplFc Num(19,6) Down Payment Applied FC
  DpmApplSc Num(19,6) Down Payment Applied SC
  LPgFolioN Int(11) Folio No. for Last Page in Doc.
  Header Text(16) Header
  Footer Text(16) Footer
  Posted VarChar(1) Dpm Was Posted default=Y [Y=Yes, N=No]
  OwnerCode Int(11) Document Owner ->OHEM
  BPChCode nVarChar(15) BP Channel Code ->OCRD
  BPChCntc Int(11) BP Channel Contact Person ->OCPR
  PayToCode nVarChar(50) Pay To
  IsPaytoBnk VarChar(1) Is Pay to Bank [N=No, Y=Yes]
  BnkCntry nVarChar(3) Pay to Bank Country/Region ->OCRY
  BankCode nVarChar(30) Pay to Bank Code
  BnkAccount nVarChar(50) Pay to Bank Account No.
  BnkBranch nVarChar(50) Pay to Bank Branch
  isIns VarChar(1) Reserve Invoice default=N [Y=Yes, N=No]
  TrackNo nVarChar(30) Tracking Number
  VersionNum nVarChar(13) Version Number
  LangCode Int(11) Language Code ->OLNG
  BPNameOW VarChar(1) BP_NAME_OVERWRITTEN default=N [Y=Yes, N=No]
  BillToOW VarChar(1) BILL_TO_OVERWRITTEN default=N [Y=Yes, N=No]
  ShipToOW VarChar(1) SHIP_TO_OVERWRITTEN default=N [Y=Yes, N=No]
  RetInvoice VarChar(1) Returning Invoice default=N [Y=Yes, N=No]
  ClsDate Date(8) Document Closing Date
  MInvNum Int(11) Monthly Invoice No.
  MInvDate Date(8) Monthly Invoice Date
  SeqCode Int(6) Sequence Code
  Serial Int(11) Serial Number
  SeriesStr nVarChar(3) Series String
  SubStr nVarChar(3) Subseries String
  Model nVarChar(6) Nota Fiscal Model default=0 ->ONFM
  TaxOnExp Num(19,6) Tax On Expenses Sum
  TaxOnExpFc Num(19,6) Tax On Expenses Sum (FC)
  TaxOnExpSc Num(19,6) Tax On Expenses Sum (SC)
  TaxOnExAp Num(19,6) Tax On Expenses Applied
  TaxOnExApF Num(19,6) Tax On Expenses Applied(FC)
  TaxOnExApS Num(19,6) Tax On Expenses Applied(SC)
  LastPmnTyp VarChar(1) Last Payment Type [R=Receipt, V=Vendor Payment]
  LndCstNum Int(11) Landed Cost Number
  UseCorrVat VarChar(1) Use Correction VAT Group default=N [N=No, Y=Yes]
  BlkCredMmo VarChar(1) Block Creating Credit Memo Tgt default=N [N=No, Y=Yes]
  OpenForLaC VarChar(1) Open For Landed Costs default=Y [Y=Open for Landed Costs, N=Closed for Landed Costs]
  Excised VarChar(1) Excised default=O [O=Open, C=Close]
  ExcRefDate Date(8) Excise Ref. Date
  ExcRmvTime nVarChar(8) Excise Removal Time
  SrvGpPrcnt Num(19,6) Gross Profit Prcnt of Service
  DepositNum Int(11) Deposit Number
  CertNum nVarChar(31) Certificate Number
  DutyStatus VarChar(1) Duty Status default=Y [Y=With Payment of Duty, N=Without Payment of Duty]
  AutoCrtFlw VarChar(1) Auto Create Follow-up Document default=N [N=No, Y=Yes]
  FlwRefDate Date(8) Follow-up Document Ref. Date
  FlwRefNum nVarChar(100) Follow-up Document Ref. Number
  VatJENum Int(11) VAT Journal Entry Number default=-1
  DpmVat Num(19,6) Down Payment Tax LC
  DpmVatFc Num(19,6) Down Payment Tax FC
  DpmVatSc Num(19,6) Down Payment Tax SC
  DpmAppVat Num(19,6) Down Payment Applied Tax LC
  DpmAppVatF Num(19,6) Down Payment Applied Tax FC
  DpmAppVatS Num(19,6) Down Payment Applied Tax SC
  InsurOp347 VarChar(1) 347 Insurance Operation default=N [N=No, Y=Yes]
  IgnRelDoc VarChar(1) Ignore Relevant Doc on Archive default=N [N=No, Y=Yes]
  BuildDesc nVarChar(50) Build Descriptor
  ResidenNum VarChar(1) Residence Number default=1 [1=Spanish Fiscal ID, 2=VAT Registration Number, 3=Passport, 4=Fiscal ID Issued by the Country/Region of Residence, 5=Certificate of Fiscal Residence, 6=Other Document, 7=Not Registered]
  Checker Int(11) Checker ->OHEM
  Payee Int(11) Payee ->OHEM
  CopyNumber Int(11) Copy Number default=0
  SSIExmpt VarChar(1) SSI Exemption [Y=Yes, N=No]
  PQTGrpSer Int(11) Pur Quotation Group Series
  PQTGrpNum Int(11) Pur Quotation Group Number
  PQTGrpHW VarChar(1) Pur Quotation Group Manual default=N [Y=Yes, N=No]
  ReopOriDoc VarChar(1) Reopen Origin. Order by Return [Y=Yes, N=No]
  ReopManCls VarChar(1) Reop. Man. Closed/Canc. Orders [Y=Yes, N=No]
  DocManClsd VarChar(1) Document Was Closed Manually default=N [Y=Yes, N=No, U=Unknown]
  ClosingOpt Int(6) Closing Option default=1
  SpecDate Date(8) Posting Date Specified by User
  Ordered VarChar(1) Payment Ordered default=N [Y=Yes, N=No]
  NTSApprov VarChar(1) NTS Approved default=N [N=No, Y=Yes]
  NTSWebSite Int(6) E-Tax Web Site ->OTWS
  NTSeTaxNo nVarChar(50) E-Tax Number
  NTSApprNo nVarChar(50) NTS Approval Number
  PayDuMonth VarChar(1) Start From [E=Month End, H=Half Month, Y=Month Start, N=]
  ExtraMonth Int(6) Number of Additional Months
  ExtraDays Int(6) Number of Additional Days
  CdcOffset Int(6) Cash Discount Offset default=0
  SignMsg Text(16) Signature Input Message
  SignDigest Text(16) Signature Digest
  CertifNum nVarChar(50) Certification Number
  KeyVersion Int(11) Private Key Version
  EDocGenTyp VarChar(1) Electr. Doc. Generation Type default=N [N=Not Relevant, G=Generate, L=Generate - Later, S=Send, R=Send - Later]
  ESeries Int(6) Electronic Series ->NNM4
  EDocNum nVarChar(50) Electronic Document Number
  EDocExpFrm Int(11) Electronic Doc. Export Format
  OnlineQuo VarChar(1) Create Online Quotation default=N [Y=Yes, N=No]
  POSEqNum nVarChar(20) POS Equipment Number
  POSManufSN nVarChar(20) POS Manufacturer Serial Number
  POSCashN Int(11) POS Cashier Number
  EDocStatus VarChar(1) Electronic Document Status default=C [N=New, P=Pending, S=Sent, E=Error, C=OK]
  EDocCntnt Text(16) Electronic Document Content
  EDocProces VarChar(1) Electronic Document Process default=C [C=CFD, I=CFDI]
  EDocErrCod nVarChar(50) Electronic Document Error Code
  EDocErrMsg Text(16) Electronic Document Error Msg
  EDocCancel VarChar(1) Electronic Document - Canceled default=N [N=No, Y=Yes]
  EDocTest VarChar(1) Electronic Document - Testing default=N [N=No, Y=Yes]
  EDocPrefix nVarChar(10) Electronic Document - Prefix
  CUP Int(11) Unique Code of Project ->OCUP
  CIG Int(11) Contract Code Identification ->OCIG
  DpmAsDscnt VarChar(1) Discount Document with Dpm default=N [N=No, Y=Yes]
  Attachment Text(16) Attachment
  AtcEntry Int(11) Attachment Entry
  SupplCode nVarChar(254) Supplementary Code
  GTSRlvnt VarChar(1) Relevant To GTS default=N [N=No, Y=Yes]
  BaseDisc Num(19,6) Base Discount LC
  BaseDiscSc Num(19,6) Base Discount SC
  BaseDiscFc Num(19,6) Base Discount FC
  BaseDiscPr Num(19,6) Base Discount Percentage
  CreateTS Int(11) Creatn Time - Incl. Secs
  UpdateTS Int(11) Update Full Time
  SrvTaxRule VarChar(1) Apply Service Tax Rule default=N [Y=Yes, N=No]
  AnnInvDecR Int(11) Annual Inv. Declaration Ref.
  Supplier nVarChar(15) Supplier ->OCRD
  Releaser Int(11) Goods Distribution Approver ->OHEM
  Receiver Int(11) Goods Release Approver ->OHEM
  ToWhsCode nVarChar(8) To Warehouse Code ->OWHS
  AssetDate Date(8) Fixed Asset Value Date
  Requester nVarChar(25) User Requesting Goods
  ReqName nVarChar(155) User Name
  Branch Int(6) Branch ->OUBR
  Department Int(6) Department ->OUDP
  Email nVarChar(100) E-Mail
  Notify VarChar(1) Send Notification Needed [Y=Yes, N=No]
  ReqType Int(11) Requester Type User/Employee default=12 [12=User, 171=Employee]
  OriginType VarChar(1) Document Origin default=M [M=Manual, R=MRP, S=Sales Order, D=Document Generation Wizard]
  IsReuseNum VarChar(1) Is Reusing Document Number default=N [Y=Yes, N=No]
  IsReuseNFN VarChar(1) Is Reusing Nota Fiscal Number default=N [Y=Yes, N=No]
  DocDlvry VarChar(1) Document Delivery [0=None, 1=Create Online Document, 2=Post to Ariba Network]
  PaidDpm Num(19,6) Paid by Down Payment
  PaidDpmF Num(19,6) Paid by Down Payment (FC)
  PaidDpmS Num(19,6) Paid by Down Payment (SC)
  EnvTypeNFe Int(11) Environment Type NF-e default=-1 ->OBNI
  AgrNo Int(11) Agreement No.
  IsAlt VarChar(1) Is Alteration default=N [Y=Yes, N=No]
  AltBaseTyp Int(11) Alteration Base Type default=-1 [-1=, 13=, 18=, 163=, 165=]
  AltBaseEnt Int(11) Alteration Base Entry
  AuthCode nVarChar(250) Authorization Code
  StDlvDate Date(8) Start Delivery Date
  StDlvTime Int(11) Start Delivery Time
  EndDlvDate Date(8) End Delivery Date
  EndDlvTime Int(11) End Delivery Time
  VclPlate nVarChar(20) Vehicle Plate
  ElCoStatus nVarChar(10) Elec. Comm. Status [0=Approved, 1=Pending Approval, 2=Rejected]
  AtDocType nVarChar(2) AT Document Type [GT=GT, GA=GA, GD=GD, GR=GR, GC=GC, FT=FT, FS=FS, NC=NC, ND=ND, FR=FR]
  ElCoMsg nVarChar(254) Elec. Comm. Message
  PrintSEPA VarChar(1) Print SEPA Direct Debit Prenotification default=N [Y=Yes, N=No]
  FreeChrg Num(19,6) Free of Charge BP
  FreeChrgFC Num(19,6) Free of Charge BP FC
  FreeChrgSC Num(19,6) Free of Charge BP SC
  NfeValue Num(19,6) NF-e Value
  FiscDocNum nVarChar(100) Fiscal Document Number
  RelatedTyp Int(11) Related Type default=-1 [-1=]
  RelatedEnt Int(11) Related Entry
  CCDEntry Int(11) CCD Abs. Entry
  NfePrntFo Int(11) NF-e Printing Format default=0 [0=No DANFE, 1=Portrait, 2=Landscape, 3=Simplified, 4=DANFE NFC-e, 5=Mail]
  ZrdAbs Int(11) POS Daily Summary Number ->OZRD
  POSRcptNo Int(11) POS Receipt Number
  FoCTax Num(19,6) Free of Charge BP Tax
  FoCTaxFC Num(19,6) Free of Charge BP Tax FC
  FoCTaxSC Num(19,6) Free of Charge BP Tax SC
  TpCusPres Int(11) Type of End-User Presence ->OBNI
  ExcDocDate Date(8) Excise Doc. Date
  FoCFrght Num(19,6) Free of Charge Freight
  FoCFrghtFC Num(19,6) Free of Charge Freight FC
  FoCFrghtSC Num(19,6) Free of Charge Freight SC
  InterimTyp Int(6) Interim Type default=0 [0=None]
  PTICode nVarChar(5) POI Code ->OPTI
  Letter VarChar(1) Letter
  FolNumFrom Int(11) Folio Number From
  FolNumTo Int(11) Folio Number To
  FolSeries Int(11) Folio Series ->OFNS
  SplitTax Num(19,6) Split Payment Tax
  SplitTaxFC Num(19,6) Split Payment Tax FC
  SplitTaxSC Num(19,6) Split Payment Tax SC
  ToBinCode nVarChar(228) To Bin Location
  PriceMode VarChar(1) Price Mode [N=Net, G=Gross, M=Net and Gross]
  PoDropPrss VarChar(1) PO Drop-Ship Process default=N [Y=Yes, N=No]
  PermitNo nVarChar(20) Permit Number
  MYFtype nVarChar(2) MYF type [S1=MYF Wholesale Sales, S2=Retail Sales, P1=MYF Wholesale Purchases, P3=Other Expense Transactions]
  DocTaxID nVarChar(32) Document Tax ID
  DateReport Date(8) Date of Reporting
  RepSection nVarChar(3) Reporting Section
  ExclTaxRep VarChar(1) Exclude from Control Statement default=N [Y=Yes, N=No]
  PosCashReg Int(11) POS/Cash Register
  DmpTransID nVarChar(20) Trans ID for Down Payment
  ECommerBP nVarChar(15) E-Commerce Operator ->OCRD
  EComerGSTN nVarChar(15) GST Regn No of E-Commerce
  Revision VarChar(1) Revision default=N [Y=Yes, N=No]
  RevRefNo nVarChar(100) Original Ref. No.
  RevRefDate Date(8) Original Ref. Date
  RevCreRefN nVarChar(100) Original Credit/Debit Ref. No.
  RevCreRefD Date(8) Orign Credit/Debit Ref. Date
  TaxInvNo nVarChar(100) Tax Invoice No.
  FrmBpDate Date(8) From Vendor Date
  GSTTranTyp nVarChar(2) GST Transaction Type [--=Bill of Supply, GA=GST Tax Invoice, GD=GST Debit Memo]
  BaseType Int(11) Base Document Type default=-1 [-1=, 67=Inventory Transfer]
  BaseEntry Int(11) Base Document Internal Key
  ComTrade VarChar(1) Commission Trade default=E [E=, S=Sales Agent, P=Purchase Agent, C=Consignor]
  UseBilAddr VarChar(1) Determine GST by Using Bill to [Y=Yes, N=No]
  IssReason Int(6) Reason for issuing note default=1 [1=Sales Return, 2=Post sale discount, 3=Deficiency in service, 4=Correction in invoice, 5=Change in POS, 6=Finalization of Provisional Assessment, 7=Others]
  ComTradeRt VarChar(1) Commission Trade Return default=N [Y=Yes, N=No]
  SplitPmnt VarChar(1) A/P Split Payment default=N [Y=Yes, N=No]
  SOIWizId Int(11) SOI Wizard ID ->OSOI
  SelfPosted VarChar(1) Self Invoice Created [Yes/No] default=N [Y=Yes, N=No]
  EnBnkAcct Text(16) Encryption of Pay to Bank Acct
  EncryptIV nVarChar(100) Encrypt IV
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
  SAPPassprt Text(16) Extended SAP Passport
  EWBGenType VarChar(1) E-Way Bill Generation Type [N=Not Relevant, G=Generate, L=Generate - Later]
  CtActTax Num(19,6) Customer Accounting Tax
  CtActTaxFC Num(19,6) Customer Accounting Tax (FC)
  CtActTaxSC Num(19,6) Customer Accounting Tax (SC)
  EDocType VarChar(1) eDoc Type default=F [F=FE, C=FCE]
  QRCodeSrc Text(16) QR Code Source
  AggregDoc VarChar(1) Aggregate Document default=N [Y=Yes, N=No]
  DataVers Int(11) Data Version default=1
  ShipState nVarChar(3) Shipment State Code ->OCST
  ShipPlace nVarChar(60) Shipment Place Name
  CustOffice nVarChar(60) Customs Office Name
  FCI nVarChar(36) FCI Number
  NnSbCuAmnt Num(19,6) WTax Non-Subject CU Amount
  NnSbCuSC Num(19,6) WTax Non-Subject CU Amount SC
  NnSbCuFC Num(19,6) WTax Non-Subject CU Amount FC
  ExepCuAmnt Num(19,6) WTax Exempt CU Amount
  ExepCuSC Num(19,6) WTax Exempt CU Amount SC
  ExepCuFC Num(19,6) WTax Exempt CU Amount FC
  AddLegIn nVarChar(100) Additional Legal Information
  LegTextF Int(11) Legal Text Format ->OLTF
  IndFinal VarChar(1) Indicator for Final Consumer default=N [Y=Yes, N=No]
  DANFELgTxt Text(16) DANFE Legal Text
  PostPmntWT VarChar(1) Post Payment Withholding Tax default=N [N=No, Y=Yes]
  QRCodeSPGn Text(16) QR Code Source Generated from Stored Procedure
  FCEPmnMean VarChar(1) Use FCEs as Payment Means default=N [Y=Yes, N=No]
  ReqCode nVarChar(50) Requester Code
  NotRel4MI VarChar(1) Not Relevant for Monthly Invoice default=N [Y=Yes, N=No]
  Rel4PPTax VarChar(1) Relevant for Plastic Packaging Tax default=N [Y=Yes, N=No]

# AIR1 - Input Service Distribution - Recipient Invoice Lines
Module: Marketing Documents | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIRI
  LineNum Int(11) Row Number
  StaType Int(11) GST Tax Type [-100=CGST, -110=SGST, -120=IGST, -130=Cess GST, -150=UTGST]
  TaxAcct nVarChar(15) Tax Account
  RecAmnt Num(19,6) Received Amount
  ElgAmnt Num(19,6) Eligible Amount

# AIS1 - Input Service Distribution - Rows
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OISD
  LineNum Int(11) Row Number
  SourceType Int(11) Source Document Type [18=GST Tax Invoice, 19=GST Credit Memo, -18=GST Debit Memo]
  SourceNo Int(11) Source Document No.
  SrcEntry Int(11) Source Document Entry
  SrcLocCode Int(11) Source Location Code ->OLCT
  SrcLocName nVarChar(100) Source Location Name
  SrcStaType Int(11) Source GST Tax Type [-100=CGST, -110=SGST, -120=IGST, -130=Cess GST, -150=UTGST]
  SrcTaxAcct nVarChar(15) Source Tax Account
  SACEntry Int(11) SAC Entry
  CrdtAmnt Num(19,6) Total Credit Amount
  DistAmnt Num(19,6) Credit Amount to Distribute
  SrcSubType nVarChar(2) Source Document Subtype
  ITCType VarChar(1) ITC Type default=E [E=Eligible, I=Ineligible]

# AIS2 - Input Service Distribution - Row Detail
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, TargetLoc, TarTaxAcct, TarStaType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OISD
  LineNum Int(11) Row Number
  TargetLoc Int(11) Target Location Code
  TarLocName nVarChar(100) Target Location Name
  TarStaType Int(11) Target GST Tax Type [-100=CGST, -110=SGST, -120=IGST, -130=Cess GST, -150=UTGST]
  TarTaxAcct nVarChar(15) Target Tax Account Code ->OACT
  AllocAmnt Num(19,6) Allocated Amount
  ITCType VarChar(1) ITC Type default=E [E=Eligible, I=Ineligible]

# ARR1 - Input Service Distribution - Recipient Credit Memo
Module: Marketing Documents | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIRI
  LineNum Int(11) Row Number
  StaType Int(11) GST Tax Type [-100=CGST, -110=SGST, -120=IGST, -130=Cess GST, -150=UTGST]
  TaxAcct nVarChar(15) Tax Account
  RecAmnt Num(19,6) Received Amount
  ElgAmnt Num(19,6) Eligible Amount

# ASI1 - Input Service Distribution - Invoice Lines
Module: Marketing Documents | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OISI
  LineNum Int(11) Row Number
  SourceType Int(11) Source Document Type [18=GST Tax Invoice, 19=GST Credit Memo, -18=GST Debit Memo]
  SourceNo Int(11) Source Document No.
  SrcEntry Int(11) Source Document Entry
  SrcStaType Int(11) Source GST Tax Type [-100=CGST, -110=SGST, -120=IGST, -130=Cess GST, -150=UTGST]
  SrcTaxAcct nVarChar(15) Source Tax Account
  SACEntry Int(11) SAC Entry
  TarStaType Int(11) Target GST Tax Type [-100=CGST, -110=SGST, -120=IGST, -130=Cess GST, -150=UTGST]
  TarTaxAcct nVarChar(15) Target Tax Account
  DistAmnt Num(19,6) Credit Amount to Distribute
  SrcSubType nVarChar(2) Source Document Subtype
  ITCType VarChar(1) ITC Type default=E [E=Eligible, I=Ineligible]

# ATR1 - Transportation Document Lines - History
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->ATRO
  LineNum Int(11) Line Number
  DocObjType Int(11) Document Object Type [13=A/R Invoice, 15=Delivery, 21=Goods Return, 67=Inventory Transfer]
  DocEntry Int(11) Internal Number
  DocLineNum Int(11) Document Line Number
  ItemCode nVarChar(50) Item No.
  TranspQty Num(19,6) Transported Quantity
  LogInstanc Int(11) Log Instance default=0
  DocOrdNum Int(11) Document Order Number

# ATRO - Transportation Document - History
Module: Marketing Documents | 24 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LogInstanc
  NEXT_NUM_U U: NextNum, WhsCode, IssueGate, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  NextNum Int(11) Consecutive Number
  PostDate Date(8) Posting Date
  EDocGenTyp VarChar(1) El. Doc. Gen. Type default=N [N=Not Relevant, G=Generate, L=Generate Later]
  EDocExpFrm Int(11) Electronic Doc. Export Format
  TranspNum nVarChar(100) Transportation Number
  Expiration Date(8) Expiration Date
  Vehicle nVarChar(10) Vehicle ID
  TrailerID nVarChar(10) Trailer ID
  Carrier nVarChar(15) Carrier Code
  IssueGate Int(11) Issue Gate default=0
  AtcEntry Int(11) Attachment Entry
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature
  UserSign2 Int(6) Updating User
  CreateDate Date(8) Production Date
  UpdateTS Int(11) Update Full Time
  CANCELED VarChar(1) Canceled default=N [Y=Yes, N=No]
  Weight Num(19,6) Weight
  WghtUnit Int(6) Unit of Weight
  TotalLC Num(19,6) Row Total
  WhsCode nVarChar(8) Warehouse Code
  COTcode nVarChar(3) COT Code

# ATX1 - Tax Invoice - History - Rows
Module: Marketing Documents | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BaseEntry, LineNum, LogInstanc, ObjType
Fields (name type(len) description [values] ->parent table):
  BaseEntry Int(11) Base Document Internal ID
  LineNum Int(11) Row Number
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  DocType VarChar(1) Document Type default=I [I=Invoice, P=Payment, J=Journal Entry, C=Correction Invoice, L=Landed Cost]
  RefEntry1 Int(11) Ref.1 Document Key
  RefEntry2 Int(11) Ref.1 Document Key
  ObjType Int(6) Object Type ->ADP1
  LogInstanc Int(11) Log Instance default=0
  RefType Int(11) Ref. Object Type default=-1 [-1=, 13=A/R Invoice, 18=A/P Invoice, 30=Journal Entry, 24=Incoming Payment, 204=A/P Down Payment, 165=A/R Correction Invoice, 163=A/P Correction Invoice, 69=Landed Cost]
  EncryptIV nVarChar(100) Encrypt IV

# ATX2 - Tax Invoice Operation Codes
Module: Marketing Documents | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BaseEntry, LineNum, OpCode, LogInstanc, ObjType
Fields (name type(len) description [values] ->parent table):
  BaseEntry Int(11) Abs. Entry ->OTSI
  LineNum Int(11) Base Doc. Abs. Entry ->TSI1
  OpCode Int(11) Operation Code ->OBSI
  ObjType Int(11) Object Type ->ADP1
  LogInstanc Int(11) Log Instance default=0

# ATX3 - Tax Invoice Archive - Document Reference Information
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ObjType, LogInstanc
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

# ATX4 - Tax Invoice Archive - Linked Down Payments
Module: Marketing Documents | 23 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ObjType, LogInstanc
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

# ATXI - Tax Invoice - History
Module: Marketing Documents | 47 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LogInstanc, ObjType
  NUM U: DocNum, AltRev, LogInstanc, ObjType, PIndicator, Series
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  DocType VarChar(1) Document Type default=I [I=Invoice, P=Payment, J=Journal Entry, C=Correction Invoice, D=Down Payment, A=Alteration Invoice, B=Alteration Correction Invoice]
  CANCELED VarChar(1) Canceled default=N [Y=Yes, N=No]
  HandWriten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  Printed VarChar(1) Printed default=N [Y=Yes, N=No]
  Transfered VarChar(1) Year Transfer default=N [Y=Yes, N=No]
  ObjType nVarChar(20) Object Type default=194 ->ADP1
  DocDate Date(8) Posting Date
  CardCode nVarChar(15) Customer Code ->OCRD
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Date of Update
  DocDueDate Date(8) Due Date
  Series Int(11) Series default=0
  Segment Int(6) Segment default=0
  CntctCode Int(11) Contact Person ->OCPR
  VatDate Date(8) Document Date
  Comments nVarChar(254) Remarks
  TrnspCode Int(6) Shipping Type default=-1 ->OSHP
  ShipToCode nVarChar(50) Ship-to Code
  Address nVarChar(254) Bill To
  Address2 nVarChar(254) Ship To
  LogInstanc Int(11) Log Instance default=0
  CurSource VarChar(1) Base Currency default=C [L=Local Currency, S=System Currency, C=BP Currency]
  DocCur nVarChar(3) Document Currency
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  NumAtCard nVarChar(100) BP Reference No.
  CardName nVarChar(100) Customer/Vendor Name
  CancelDate Date(8) Cancel Date
  DocTotal Num(19,6) Document Total
  VatSum Num(19,6) Total Tax
  PayRefNo nVarChar(16) Payment Ref. No.
  PayRefDate Date(8) Payment Ref. Date
  TaxMethod VarChar(1) Taxation Method default=S [S=On Shipment, P=On Payment]
  AtcEntry Int(11) Attachment Entry
  IsDpm VarChar(1) IS Down Payment default=N [Y=Yes, N=No]
  AltRev Int(11) Alteration Revision default=0
  PIndicator nVarChar(10) Period Indicator ->OPID
  TransId Int(11) Transaction Number ->OJDT
  JrnlMemo nVarChar(254) Journal Remark
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  VATRegNum nVarChar(32) Branch Reg. No.
  GovContrID nVarChar(254) Gov. Contract ID
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
  EncryptIV nVarChar(100) Encrypt IV

# BAL1 - Opening Balance Instances
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, Instance
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Instance Int(11) Instance
  OBDate Date(8) Date of Opening Balance (first day of next fiscal period)
  InAmount Num(19,6) Total Received Value
  InQty Num(19,6) Total Received Quantity
  OutQty Num(19,6) Total Issued Quantity
  InAmntLWA Num(19,6) Last Non-zero Total Received Value
  InQtyLWA Num(19,6) Last Non-zero Total Received Quantity
  LastTrnsID Int(11) Last Transaction ID
  WasPrevOB VarChar(1) OB from Start of Fiscal Year default=N [Y=Yes, N=No]
  CreateDate Date(8) Create Date
  UpdateDate Date(8) Update Date
  CrossPRev Num(19,6) Cross Period Revaluation from Next Period
  WasUpdPrCB VarChar(1) Update previous Closing Balance with cross period revaluations default=N [Y=Yes, N=No]

# BAL2 - Period indicators for opening Balance
Module: Marketing Documents | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PeriodID
  SECONDARY U: DateFrom, DateTo
Fields (name type(len) description [values] ->parent table):
  PeriodID Int(11) Period Indicator
  DateFrom Date(8) Date From
  DateTo Date(8) Date To
  FiscalYear Int(11) Fiscal Year
  CreateDate Date(8) Create Date

# CIN1 - Correction Invoice - Rows
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
  DocEntry Int(11) Document Internal ID ->OCIN
  LineNum Int(11) Row Number
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=, 14=A/R Credit Memo]
  TrgetEntry Int(11) Target Document Internal ID
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 23=Sales Quotation, 17=Sales Order, 16=A/R Returns]
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
  OpenSumFC Num(19,6) Open Amount in FC
  VendorNum nVarChar(50) Vendor Catalog No.
  SerialNum nVarChar(17) Serial Number
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  SlpCode Int(11) Sales Employee Code default=-1 ->OSLP
  Commission Num(19,6) Commission %
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
  TotalSumSy Num(19,6) Row Total (FC)
  OpenSumSys Num(19,6) Open Amount (SC)
  InvntSttus VarChar(1) Whse Status default=O [O=Open, C=Closed]
  OcrCode nVarChar(8) Costing Code ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  CodeBars nVarChar(254) EAN Code
  VatPrcnt Num(19,6) Tax % per Row
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
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  FinncPriod Int(11) Posting Period ->OFPR
  ObjType nVarChar(20) Object Type default=132 ->ADP1
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
  WtLiable VarChar(1) WT Liable [Y=Yes, N=No]
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
  GTotalFC Num(19,6) Gross Total (FC)
  GTotalSC Num(19,6) Gross Total (SC)
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

# CIN10 - Correction Invoice - Row Structure
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SECONDERY U: DocEntry, AftLineNum, OrderNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCIN
  LineSeq Int(11) Row Sequence
  AftLineNum Int(11) After Row Number
  OrderNum Int(11) Order Number
  LineType VarChar(1) Row Type [T=Text, S=Subtotal]
  LineText Text(16) Row Text
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=132 ->ADP1

# CIN12 - Correction Invoice - Tax Extension
Module: Marketing Documents | 117 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCIN
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
  Carrier nVarChar(15) Carrier Code
  QoP Int(11) Quantity of Packs
  PackDesc nVarChar(10) Pack Description
  Brand nVarChar(20) Brand
  NoSU Int(11) Number of Shipping Unit
  NetWeight Num(19,6) Net Weight
  GrsWeight Num(19,6) Gross Weight
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=132 ->ADP1
  TaxId10 nVarChar(100) Assessee Type
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

# CIN13 - Correction Invoice Rows - Distributed Expenses
Module: Marketing Documents | 59 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCIN
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=132 ->ADP1
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

# CIN14 - Correction Invoice - Assembly - Rows
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCIN
  LineNum Int(11) Row Number default=-1
  ChildNum Int(11) Child Number default=-1
  ItemCode nVarChar(50) Item no. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  TotalQty Num(19,6) Total Quantity
  OpenQty Num(19,6) Remaining Open Quantity
  ObjectType nVarChar(20) object type default=132 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BaseChildN Int(11) Base Child Number default=-1
  EncryptIV nVarChar(100) Encrypt IV

# CIN15 - Correction Invoice - Applied Drawn Down Payment
Module: Marketing Documents | 84 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCIN
  LineNum Int(11) Row Number
  ObjType nVarChar(20) object type default=132 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  StaCode nVarChar(8) Tax Authority Code
  StaType Int(11) Tax Authority Type
  StaIndex Int(11) Tax Authority Seq. Index
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
  DpApplNet Num(19,6) Down Payment Applied Net LC
  DpApplNetF Num(19,6) Down Payment Applied Net FC
  DpApplNetS Num(19,6) Down Payment Applied Net SC
  DpApplVat Num(19,6) Down Payment Applied Tax LC
  DpApplVatF Num(19,6) Down Payment Applied Tax FC
  DpApplVatS Num(19,6) Down Payment Applied Tax SC
  DpApplDct Num(19,6) Down Payment Applied Deductible Sum LC
  DpApplDctF Num(19,6) Down Payment Applied Deductible Sum FC
  DpApplDctS Num(19,6) Down Payment Applied Deductible Sum SC
  DpApplEq Num(19,6) Down Payment Applied Equalization Sum LC
  DpApplEqFc Num(19,6) Down Payment Applied Equalization Sum FC
  DpApplEqSc Num(19,6) Down Payment Applied Equalization Sum SC
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
  DpApplGrs Num(19,6) Down Payment Applied Gross LC
  DpApplGrsF Num(19,6) Down Payment Applied Gross FC
  DpApplGrsS Num(19,6) Down Payment Applied Gross SC
  RvsChrgSum Num(19,6) Reverse Charge Sum
  RvsChrgSc Num(19,6) Reverse Charge Sum (SC)
  RvsChrgFc Num(19,6) Reverse Charge Sum (FC)
  ApplRvs Num(19,6) Applied Reverse Charge Sum LC
  ApplRvsSc Num(19,6) Applied Reverse Charge Sum SC
  ApplRvsFc Num(19,6) Applied Reverse Charge Sum FC
  PaidRvs Num(19,6) Paid Reverse Charge Sum LC
  PaidRvsSc Num(19,6) Paid Reverse Charge Sum SC
  PaidRvsFc Num(19,6) Paid Reverse Charge Sum FC
  DpApplRvs Num(19,6) Down Payment Applied Reverse Charge LC
  DpApplRvsS Num(19,6) Down Payment Applied Reverse Charge SC
  DpApplRvsF Num(19,6) Down Payment Applied Reverse Charge FC
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# CIN16 - Correction Invoice - SnB properties
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, SnBIndex
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) abs entry ->OCIN
  LineNum Int(11) Line Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object id
  ObjAbs Int(11) Object Abs
  DrfWObjAbs Int(11) draft Wobj Abs default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type default=163
  LogInstanc Int(11) Log Instance

# CIN17 - Correction Invoice - Bin Allocation Data
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OCIN
  LineNum Int(11) Bin Allocation Sequence
  LogInstanc Int(11) Line Number default=0
  ObjectType nVarChar(20) Subline Number default=132 ->ADP1
  ImpDocType VarChar(1) SnB Type ->OBSI
  ImpDocNum nVarChar(10) SnB Master Data Internal Number
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

# CIN18 - Correction Invoice - Export Process
Module: Marketing Documents | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCIN
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=132 ->ADP1
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

# CIN19 - Correction Invoice - Bin Allocation Data
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, BinAllocSe
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OCIN
  BinAllocSe Int(11) Bin Allocation Sequence
  LineNum Int(11) Line Number
  SubLineNum Int(11) Subline Number default=-1
  SnBType Int(11) SnB Type default=-1
  SnBMDAbs Int(11) SnB Master Data Internal No. default=-1
  BinAbs Int(11) Bin Internal Number ->OBIN
  Quantity Num(19,6) Quantity
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjType nVarChar(20) Object Type default=132 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  BinActTyp Int(6) Bin Action Type [1=Transaction In, 2=Transaction Out, 4=SnB Complete, 8=Bin First Then SnB]

# CIN2 - A/R Correction Invoice - Freight - Rows
Module: Marketing Documents | 64 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCIN
  LineNum Int(11) Row Number
  GroupNum Int(11) Expense Group
  ExpnsCode Int(11) Expense Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid in FC
  PaidSys Num(19,6) Paid in SC
  ObjType nVarChar(20) Object Type default=132 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) VAT Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) VAT Group ->OVTG
  VatPrcnt Num(19,6) Row VAT %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Aquisition Tax default=N [Y=Yes, N=No]
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
  WtLiable VarChar(1) WT Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
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

# CIN20 - Intrastat Expenses
Module: Marketing Documents | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCIN
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
  ObjectType nVarChar(20) Object Type default=132 ->ADP1
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  AppliedLC Num(19,6) Applied
  AppliedFC Num(19,6) Applied (FC)
  AppliedSC Num(19,6) Applied (SC)

# CIN21 - Correction Invoice - Document Reference Information
Module: Marketing Documents | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, RefType
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjectType nVarChar(20) Object Type default=132
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

# CIN22 - Correction Invoice - Resource Costs
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, StdCostNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->CIN1
  LineNum Int(11) Row Number ->CIN1
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=132
  LogInstanc Int(11) Log Instance default=0

# CIN23 - A/P Invoice - Selected Asset Master Data
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, VisOrder
  ASSETS: DocEntry, LineNum, AssetCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCIN
  LineNum Int(11) Row Number
  AssetCode nVarChar(50) Selected Asset Code ->OITM
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Remarks nVarChar(100) Remarks
  Amount Num(19,6) Amount
  AmountSC Num(19,6) Amount (SC)
  SerialNo nVarChar(30) Serial Number
  VisOrder Int(11) Visual Order
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=132 ->ADP1

# CIN24 - Correction Invoice - Tracking Note Assignment
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
  ObjType nVarChar(20) Object Type default=132 ->ADP1
  SubLineNum Int(11) BOM Line No.

# CIN25 - Correction Invoice - Amt Per VAT Grp
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
  ObjType nVarChar(20) Object Type default=132 ->ADP1

# CIN26 - Correction Invoice - E-Way Bill Information
Module: Marketing Documents | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCIN
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
  ObjectType nVarChar(20) Object Type default=132 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TspEntry Int(11) Transporter Abs. Entry ->OTSP
  TspLine Int(11) Transportation Line
  TransType Int(11) Transaction Type [1=Regular, 2=Bill To-Ship To, 3=Bill From-Dispatch From, 4=Combination of 2 and 3]

# CIN27 - Correction Invoice - E-Books(GR) Rows
Module: Marketing Documents | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  RELATE_ROW: DocEntry, RelateType, RelateLine, GroupNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCIN
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

# CIN28 - Correction Invoice - Reported Tracking Note
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
  ObjType nVarChar(20) Object Type default=132 ->ADP1
  SubLineNum Int(11) BOM Line No.

# CIN3 - A/R Correction Invoice - Freight
Module: Marketing Documents | 80 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  DOCUMENT: DocEntry, BaseAbsEnt
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCIN
  ExpnsCode Int(11) Expense Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid in FC
  PaidSys Num(19,6) Paid in SC
  Comments nVarChar(100) Remarks
  ObjType nVarChar(20) Object Type default=132 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  TaxStatus VarChar(1) VAT Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) VAT Group ->OVTG
  VatPrcnt Num(19,6) Row VAT Percentage
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Aquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  WTLiable VarChar(1) WT Liable [Y=Yes, N=No]
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
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 23=Sales Quotation, 17=Sales Order, 16=A/R Returns]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Line No.
  LineNum Int(11) line num default=-1
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Abs. Entry default=-1
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

# CIN4 - Correction Invoice - Tax Amount per Document
Module: Marketing Documents | 61 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SCONDARY: DocEntry, LineNum, GroupNum, ExpnsCode, StcCode, StaCode, staType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCIN
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
  ObjectType nVarChar(20) Object Type default=132 ->ADP1
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

# CIN5 - A\R Correction Invoice - Withholding Tax
Module: Marketing Documents | 158 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  SECONDERY U: AbsEntry, WTCode, BaseAbsEnt, Doc1LineNo
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator ->OCIN
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
  BaseNum Int(11) Base Document Type default=-1 [-1=, 0=, 23=Sales Quotation, 17=Sales Order, 16=A/R Returns]
  LineNum Int(11) Line Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Abs. Entry default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=132 ->ADP1
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

# CIN6 - Correction Invoice - Installments
Module: Marketing Documents | 65 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, InstlmntID
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCIN
  InstlmntID Int(6) Installment ID default=1
  ObjType nVarChar(20) Object Type default=132 ->ADP1
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

# CIN7 - Delivery Packages - Correction Invoice
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCIN
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type default=132 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV

# CIN8 - Items in Package - Correction Invoice
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum, ItemCode, UomEntry, NumPerMsr
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCIN
  PackageNum Int(11) Package Number
  ItemCode nVarChar(50) Item Code ->OITM
  Quantity Num(19,6) Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=132 ->ADP1
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value default=0

# CIN9 - Correction Invoice - Drawn Dpm
Module: Marketing Documents | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCIN
  LineNum Int(11) Row Number
  BaseAbs Int(11) Base Document Internal ID
  BaseLine Int(11) Base Document Row
  TargetBase VarChar(1) Target or Base Document default=B [B=Base, T=Target]
  ObjType nVarChar(20) Base Object Type
  DrawnSum Num(19,6) Net LC
  DrawnSumFc Num(19,6) Net FC
  DrawnSumSc Num(19,6) Net SC
  LogInstanc Int(11) Log Instance default=0
  ObjCode nVarChar(20) Object Type default=132 ->ADP1
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

# CPI1 - A/P Correction Invoice - Rows
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
  DocEntry Int(11) Document Internal ID ->OCPI
  LineNum Int(11) Row Number
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=, 20=Goods Receipt PO, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal]
  TrgetEntry Int(11) Target Document Internal ID
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 18=A/P Invoice, 163=A/P Correction Invoice]
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
  InvntSttus VarChar(1) Inventory Direction default=O [O=Open, C=Closed]
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
  UpdInvntry VarChar(1) Inventory Update default=Y [Y=Yes, N=No]
  BaseDocNum Int(11) Base Document No.
  BaseAtCard nVarChar(100) Customer/Vendor Base Document
  SWW nVarChar(16) Additional Identifier
  VatSum Num(19,6) Total Tax
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  FinncPriod Int(11) Posting Period ->OFPR
  ObjType nVarChar(20) Object Type default=163 ->ADP1
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
  CEECFlag VarChar(1) Correction Invoice Was/Should Be default=S [W=Was, S=Should be]
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
  StckDstFc Num(19,6) Stock Distributed Sum (FC)
  StckDstSc Num(19,6) Stock Distributed Sum (SC)
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
  PQTReqQty Num(19,6) Pur. Quotation: Required Qty
  PQTReqDate Date(8) Pur. Quotation: Required Date
  PcDocType Int(11) Pur. Confirmation Doc. Type default=-1 [-1=No Type, 22=Purchase Order, 540000006=Purchase Quotation]
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

# CPI10 - A/P Correction Invoice - Row Structure
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SECONDERY U: DocEntry, AftLineNum, OrderNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPI
  LineSeq Int(11) Row Sequence
  AftLineNum Int(11) After Row Number
  OrderNum Int(11) Order Number
  LineType VarChar(1) Row Type [T=Text, S=Subtotal]
  LineText Text(16) Row Text
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=163 ->ADP1

# CPI11 - A/P Corr. Inv - Drawn Dpm Det.
Module: Marketing Documents | 70 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LineSeq
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPI
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
  ObjType nVarChar(20) Object Type default=163 ->ADP1
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

# CPI12 - A/P Correction Invoice - Tax Extension
Module: Marketing Documents | 117 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPI
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
  Carrier nVarChar(15) Carrier Code
  QoP Int(11) Quantity of Packs
  PackDesc nVarChar(10) Pack Description
  Brand nVarChar(20) Brand
  NoSU Int(11) Number of Shipping Unit
  NetWeight Num(19,6) Net Weight
  GrsWeight Num(19,6) Gross Weight
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=163 ->ADP1
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

# CPI13 - A/P Correction Invoice Rows - Distributed Expenses
Module: Marketing Documents | 59 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPI
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=163 ->ADP1
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

# CPI14 - A/P Correction Invoice - Assembly - Rows
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPI
  LineNum Int(11) Row Number default=-1
  ChildNum Int(11) Child Number default=-1
  ItemCode nVarChar(50) Item no. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  TotalQty Num(19,6) Total Quantity
  OpenQty Num(19,6) Remaining Open Quantity
  ObjectType nVarChar(20) object type default=163 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BaseChildN Int(11) Base Child Number default=-1
  EncryptIV nVarChar(100) Encrypt IV

# CPI15 - A/P Corr Inv - Drawn Dpm Appld
Module: Marketing Documents | 84 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPI
  LineNum Int(11) Row Number
  ObjType nVarChar(20) object type default=163 ->ADP1
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

# CPI16 - A/P Corr. Inv - SnB properties
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, SnBIndex
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) abs entry ->OCPI
  LineNum Int(11) Line Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object id
  ObjAbs Int(11) Object Abs
  DrfWObjAbs Int(11) draft Wobj Abs default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type default=163
  LogInstanc Int(11) Log Instance

# CPI17 - A/P Correction Invoice - Import Process
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPI
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=163 ->ADP1
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

# CPI18 - A/P Correction Invoice - Export Process
Module: Marketing Documents | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPI
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=163 ->ADP1
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

# CPI19 - A/P Correction Invoice - Bin Allocation Data
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, BinAllocSe
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OCPI
  BinAllocSe Int(11) Bin Allocation Sequence
  LineNum Int(11) Line Number
  SubLineNum Int(11) Subline Number default=-1
  SnBType Int(11) SnB Type default=-1
  SnBMDAbs Int(11) SnB Master Data Internal No. default=-1
  BinAbs Int(11) Bin Internal Number ->OBIN
  Quantity Num(19,6) Quantity
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjType nVarChar(20) Object Type default=163 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  BinActTyp Int(6) Bin Action Type [1=Transaction In, 2=Transaction Out, 4=SnB Complete, 8=Bin First Then SnB]

# CPI2 - A/P Correction Invoice - Freight - Rows
Module: Marketing Documents | 64 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPI
  LineNum Int(11) Row Number
  GroupNum Int(11) Expense Group
  ExpnsCode Int(11) Expense Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid in FC
  PaidSys Num(19,6) Paid in SC
  ObjType nVarChar(20) Object Type default=163 ->ADP1
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
  WtLiable VarChar(1) WT Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
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

# CPI20 - Intrastat Expenses
Module: Marketing Documents | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPI
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
  ObjectType nVarChar(20) Object Type default=163 ->ADP1
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  AppliedLC Num(19,6) Applied
  AppliedFC Num(19,6) Applied (FC)
  AppliedSC Num(19,6) Applied (SC)

# CPI21 - A/P Correction Invoice - Document Reference Information
Module: Marketing Documents | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, RefType
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjectType nVarChar(20) Object Type default=163
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

# CPI22 - A/P Correction Invoice - Resource Costs
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, StdCostNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->CPI1
  LineNum Int(11) Row Number ->CPI1
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=163
  LogInstanc Int(11) Log Instance default=0

# CPI23 - A/P Invoice - Selected Asset Master Data
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, VisOrder
  ASSETS: DocEntry, LineNum, AssetCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPI
  LineNum Int(11) Row Number
  AssetCode nVarChar(50) Selected Asset Code ->OITM
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Remarks nVarChar(100) Remarks
  Amount Num(19,6) Amount
  AmountSC Num(19,6) Amount (SC)
  SerialNo nVarChar(30) Serial Number
  VisOrder Int(11) Visual Order
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=163 ->ADP1

# CPI24 - A/P Correction Invoice - Tracking Note Assignment
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
  ObjType nVarChar(20) Object Type default=163 ->ADP1
  SubLineNum Int(11) BOM Line No.

# CPI25 - A/P Correction Invoice - Amt Per VAT Grp
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
  ObjType nVarChar(20) Object Type default=163 ->ADP1

# CPI26 - A/P Correction Invoice - E-Way Bill Information
Module: Marketing Documents | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPI
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
  ObjectType nVarChar(20) Object Type default=163 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TspEntry Int(11) Transporter Abs. Entry ->OTSP
  TspLine Int(11) Transportation Line
  TransType Int(11) Transaction Type [1=Regular, 2=Bill To-Ship To, 3=Bill From-Dispatch From, 4=Combination of 2 and 3]

# CPI27 - A/P Correction Invoice - E-Books(GR) Rows
Module: Marketing Documents | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  RELATE_ROW: DocEntry, RelateType, RelateLine, GroupNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPI
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

# CPI28 - A/P Correction Invoice - Reported Tracking Note
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
  ObjType nVarChar(20) Object Type default=163 ->ADP1
  SubLineNum Int(11) BOM Line No.

# CPI3 - A/P Correction Invoice - Freight
Module: Marketing Documents | 80 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  DOCUMENT: DocEntry, BaseAbsEnt
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPI
  ExpnsCode Int(11) Expense Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid in FC
  PaidSys Num(19,6) Paid in SC
  Comments nVarChar(100) Remarks
  ObjType nVarChar(20) Object Type default=163 ->ADP1
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
  IsAcquistn VarChar(1) Aquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  WTLiable VarChar(1) WT Liable [Y=Yes, N=No]
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
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type [-1=, 0=, 18=A/P Invoice, 163=A/P Correction Invoice]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Line No.
  LineNum Int(11) line num default=-1
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Abs. Entry default=-1
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

# CPI4 - A/P Correction Invoice - Tax Amount per Document
Module: Marketing Documents | 61 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SCONDARY: DocEntry, LineNum, GroupNum, ExpnsCode, StcCode, StaCode, staType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPI
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
  ObjectType nVarChar(20) Object Type default=163 ->ADP1
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

# CPI5 - Withholding Tax Data
Module: Marketing Documents | 158 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  SECONDERY U: AbsEntry, WTCode, BaseAbsEnt, Doc1LineNo
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator ->OCPI
  WTCode nVarChar(4) WT Code ->OWHT
  Rate Num(19,6) Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntSC Num(19,6) Taxable Amount (SC)
  TxblAmntFC Num(19,6) Taxable Amount (FC)
  WTAmnt Num(19,6) WT Amount
  WTAmntSC Num(19,6) WT Amount (SC)
  WTAmntFC Num(19,6) WT Amount (FC)
  ApplAmnt Num(19,6) Applied WT Amount
  ApplAmntSC Num(19,6) Applied WTax Amount (SC)
  ApplAmntFC Num(19,6) Applied WTax Amount (FC)
  Category VarChar(1) Category [P=Payment, I=Invoice]
  Criteria VarChar(1) WT Criteria [Y=Accrual, N=Cash]
  Account nVarChar(15) G/L Account ->OACT
  Type VarChar(1) Withholding Type [V=VAT Withholding, I=Income Tax Withholding]
  RoundType VarChar(1) Rounding Type [T=Truncated, C=Commercial Values, N=No Rounding]
  BaseType VarChar(1) Base Type [G=Gross, N=Net, V=VAT, U=UoM]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseLine Int(11) Base Line
  BaseNum Int(11) Base Document Type default=-1 [-1=, 0=, 18=A/P Invoice, 163=A/P Correction Invoice]
  LineNum Int(11) Line Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Abs. Entry default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=163 ->ADP1
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

# CPI6 - Documents History - Installments
Module: Marketing Documents | 65 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, InstlmntID
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPI
  InstlmntID Int(6) Installment ID default=1
  ObjType nVarChar(20) Object Type default=163 ->ADP1
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
  ExpnsBlck Num(19,6) Reserved Freight Amount
  ExpnsBlckF Num(19,6) Reserved Freight Amount (FC)
  ExpnsBlckS Num(19,6) Reserved Freight Amount (SC)
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

# CPI7 - A/P Correction Invoice - Delivery Packages
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPI
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type default=163 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV

# CPI8 - A/P Correction Invoice - Items in Package
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum, ItemCode, UomEntry, NumPerMsr
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPI
  PackageNum Int(11) Package Number
  ItemCode nVarChar(50) Item Code ->OITM
  Quantity Num(19,6) Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=163 ->ADP1
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value default=0

# CPI9 - A/P Corr. Invoice - Drawn Dpm
Module: Marketing Documents | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPI
  LineNum Int(11) Row Number
  BaseAbs Int(11) Base Document Internal ID
  BaseLine Int(11) Base Document Row
  TargetBase VarChar(1) Target or Base Document default=T [B=Base, T=Target]
  ObjType nVarChar(20) Base Object Type
  DrawnSum Num(19,6) Net LC
  DrawnSumFc Num(19,6) Net FC
  DrawnSumSc Num(19,6) Net SC
  LogInstanc Int(11) Log Instance default=0
  ObjCode nVarChar(20) Object Type default=163 ->ADP1
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

# CPV1 - A/P Correction Invoice Reversal - Rows
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
  DocEntry Int(11) Document Internal ID ->OCPV
  LineNum Int(11) Row Number
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=]
  TrgetEntry Int(11) Target Document Internal ID
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 163=A/P Correction Invoice]
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
  InvntSttus VarChar(1) Inventory Direction default=O [O=Open, C=Closed]
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
  UpdInvntry VarChar(1) Inventory Update default=Y [Y=Yes, N=No]
  BaseDocNum Int(11) Base Document No.
  BaseAtCard nVarChar(100) Customer/Vendor Base Document
  SWW nVarChar(16) Additional Identifier
  VatSum Num(19,6) Total Tax
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  FinncPriod Int(11) Posting Period ->OFPR
  ObjType nVarChar(20) Object Type default=164 ->ADP1
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
  LineVatlF Num(19,6) Net Tax Amount
  LineVatS Num(19,6) Net Tax Amount
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value
  CEECFlag VarChar(1) Correction Invoice Was/Should Be default=S [W=Was, S=Should be]
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

# CPV10 - A/P CrIn Rev - Row Structure
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SECONDERY U: DocEntry, AftLineNum, OrderNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPV
  LineSeq Int(11) Row Sequence
  AftLineNum Int(11) After Row Number
  OrderNum Int(11) Order Number
  LineType VarChar(1) Row Type [T=Text, S=Subtotal]
  LineText Text(16) Row Text
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=164 ->ADP1

# CPV11 - A/P CrIn Rev - Drawn Dpm Det.
Module: Marketing Documents | 70 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LineSeq
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPV
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
  ObjType nVarChar(20) Object Type default=164 ->ADP1
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

# CPV12 - A/P Correction Invoice Reversal - Tax Extension
Module: Marketing Documents | 117 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPV
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
  Carrier nVarChar(15) Carrier Code
  QoP Int(11) Quantity of Packs
  PackDesc nVarChar(10) Pack Description
  Brand nVarChar(20) Brand
  NoSU Int(11) Number of Shipping Unit
  NetWeight Num(19,6) Net Weight
  GrsWeight Num(19,6) Gross Weight
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=164 ->ADP1
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
  Vat VarChar(1) VAT default=N [N=, Y=]
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

# CPV13 - A/P Correction Invoice Reversal Rows - Distributed Expenses
Module: Marketing Documents | 59 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPV
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=164 ->ADP1
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

# CPV14 - A/P Correction Invoice Reversal - Assembly - Rows
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPV
  LineNum Int(11) Row Number default=-1
  ChildNum Int(11) Child Number default=-1
  ItemCode nVarChar(50) Item no. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  TotalQty Num(19,6) Total Quantity
  OpenQty Num(19,6) Remaining Open Quantity
  ObjectType nVarChar(20) object type default=164 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BaseChildN Int(11) Base Child Number default=-1
  EncryptIV nVarChar(100) Encrypt IV

# CPV15 - A/P CrIn Rev - Drawn Dpm Appld
Module: Marketing Documents | 84 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPV
  LineNum Int(11) Row Number
  ObjType nVarChar(20) object type default=164 ->ADP1
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

# CPV16 - A/P Correction Invoice Reversal - SnB properties
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, SnBIndex
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) abs entry ->OCPV
  LineNum Int(11) Line Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object id
  ObjAbs Int(11) Object Abs
  DrfWObjAbs Int(11) draft Wobj Abs default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type default=164
  LogInstanc Int(11) Log Instance

# CPV17 - A/P Correction Invoice Reversal - Import Process
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPV
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=164 ->ADP1
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

# CPV18 - A/P Correction Invoice Reversal - Export Process
Module: Marketing Documents | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPV
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=164 ->ADP1
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

# CPV19 - A/P Correction Invoice Reversal - Bin Allocation Data
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, BinAllocSe
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OCPV
  BinAllocSe Int(11) Bin Allocation Sequence
  LineNum Int(11) Line Number
  SubLineNum Int(11) Subline Number default=-1
  SnBType Int(11) SnB Type default=-1
  SnBMDAbs Int(11) SnB Master Data Internal No. default=-1
  BinAbs Int(11) Bin Internal Number ->OBIN
  Quantity Num(19,6) Quantity
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjType nVarChar(20) Object Type default=164 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  BinActTyp Int(6) Bin Action Type [1=Transaction In, 2=Transaction Out, 4=SnB Complete, 8=Bin First Then SnB]

# CPV2 - A/P Correction Invoice Reversal - Freight - Rows
Module: Marketing Documents | 64 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPV
  LineNum Int(11) Row Number
  GroupNum Int(11) Expense Group
  ExpnsCode Int(11) Expense Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid in FC
  PaidSys Num(19,6) Paid in SC
  ObjType nVarChar(20) Object Type default=164 ->ADP1
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
  WtLiable VarChar(1) WT Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
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

# CPV20 - Intrastat Expenses
Module: Marketing Documents | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPV
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
  ObjectType nVarChar(20) Object Type default=164 ->ADP1
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  AppliedLC Num(19,6) Applied
  AppliedFC Num(19,6) Applied (FC)
  AppliedSC Num(19,6) Applied (SC)

# CPV21 - A/P Correction Invoice Reversal - Document Reference Information
Module: Marketing Documents | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, RefType
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjectType nVarChar(20) Object Type default=164
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

# CPV22 - A/P Correction Invoice Reversal - Resource Costs
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, StdCostNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->CPV1
  LineNum Int(11) Row Number ->CPV1
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=164
  LogInstanc Int(11) Log Instance default=0

# CPV23 - A/P Invoice - Selected Asset Master Data
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, VisOrder
  ASSETS: DocEntry, LineNum, AssetCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPV
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

# CPV24 - A/P Correction Invoice Reversal - Tracking Note Assignment
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
  ObjType nVarChar(20) Object Type default=164 ->ADP1
  SubLineNum Int(11) BOM Line No.

# CPV25 - A/P Correction Invoice Reversal - Amt Per VAT Grp
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
  ObjType nVarChar(20) Object Type default=164 ->ADP1

# CPV26 - A/P Correction Invoice Reversal - E-Way Bill Information
Module: Marketing Documents | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPV
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
  ObjectType nVarChar(20) Object Type default=164 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TspEntry Int(11) Transporter Abs. Entry ->OTSP
  TspLine Int(11) Transportation Line
  TransType Int(11) Transaction Type [1=Regular, 2=Bill To-Ship To, 3=Bill From-Dispatch From, 4=Combination of 2 and 3]

# CPV27 - A/P Correction Invoice Reversal - E-Books(GR) Rows
Module: Marketing Documents | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  RELATE_ROW: DocEntry, RelateType, RelateLine, GroupNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPV
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

# CPV28 - A/P Correction Invoice Reversal - Reported Tracking Note
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
  ObjType nVarChar(20) Object Type default=164 ->ADP1
  SubLineNum Int(11) BOM Line No.

# CPV3 - A/P Correction Invoice Reversal - Freight
Module: Marketing Documents | 80 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  DOCUMENT: DocEntry, BaseAbsEnt
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPV
  ExpnsCode Int(11) Expense Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid in FC
  PaidSys Num(19,6) Paid in SC
  Comments nVarChar(100) Remarks
  ObjType nVarChar(20) Object Type default=164 ->ADP1
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
  IsAcquistn VarChar(1) Aquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  WTLiable VarChar(1) WT Liable [Y=Yes, N=No]
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
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type [-1=, 0=, 163=A/P Correction Invoice]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Line No.
  LineNum Int(11) line num default=-1
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Abs. Entry default=-1
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

# CPV4 - A/P Correction Invoice Reversal - Tax Amt per Doc.
Module: Marketing Documents | 61 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SCONDARY: DocEntry, LineNum, GroupNum, ExpnsCode, StcCode, StaCode, staType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPV
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
  ObjectType nVarChar(20) Object Type default=164 ->ADP1
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

# CPV5 - A/P Correction Invoice Reversal - WTax
Module: Marketing Documents | 158 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  SECONDERY U: AbsEntry, WTCode, BaseAbsEnt, Doc1LineNo
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator ->OCPV
  WTCode nVarChar(4) WT Code ->OWHT
  Rate Num(19,6) Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntSC Num(19,6) Taxable Amount (SC)
  TxblAmntFC Num(19,6) Taxable Amount (FC)
  WTAmnt Num(19,6) WT Amount
  WTAmntSC Num(19,6) WT Amount (SC)
  WTAmntFC Num(19,6) WT Amount (FC)
  ApplAmnt Num(19,6) Applied WT Amount
  ApplAmntSC Num(19,6) Applied WTax Amount (SC)
  ApplAmntFC Num(19,6) Applied WTax Amount (FC)
  Category VarChar(1) Category [P=Payment, I=Invoice]
  Criteria VarChar(1) WT Criteria [Y=Accrual, N=Cash]
  Account nVarChar(15) G/L Account ->OACT
  Type VarChar(1) Withholding Type [V=VAT Withholding, I=Income Tax Withholding]
  RoundType VarChar(1) Rounding Type [T=Truncated, C=Commercial Values, N=No Rounding]
  BaseType VarChar(1) Base Type [G=Gross, N=Net, V=VAT, U=UoM]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseLine Int(11) Base Line
  BaseNum Int(11) Base Document Type default=-1 [-1=, 0=, 163=A/P Correction Invoice]
  LineNum Int(11) Line Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Abs. Entry default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=164 ->ADP1
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

# CPV6 - A/P Correction Invoice Reversal - Installments
Module: Marketing Documents | 65 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, InstlmntID
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPV
  InstlmntID Int(6) Installment ID default=1
  ObjType nVarChar(20) Object Type default=164 ->ADP1
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
  ExpnsBlck Num(19,6) Reserved Freight Amount
  ExpnsBlckF Num(19,6) Reserved Freight Amount (FC)
  ExpnsBlckS Num(19,6) Reserved Freight Amount (SC)
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

# CPV7 - A/P Corr Inv Rvsl - Deliv Pkgs
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPV
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type default=13 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV

# CPV8 - A/P Correction Invoice Reversal - Items in Package
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum, ItemCode, UomEntry, NumPerMsr
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPV
  PackageNum Int(11) Package Number
  ItemCode nVarChar(50) Item Number ->OITM
  Quantity Num(19,6) Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=164 ->ADP1
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value default=0

# CPV9 - A/P Corr Inv Rvrsl - Drawn Dpm
Module: Marketing Documents | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPV
  LineNum Int(11) Row Number
  BaseAbs Int(11) Base Document Internal ID
  BaseLine Int(11) Base Document Row
  TargetBase VarChar(1) Target or Base Document default=B [B=Base, T=Target]
  ObjType nVarChar(20) Base Object Type
  DrawnSum Num(19,6) Net LC
  DrawnSumFc Num(19,6) Net FC
  DrawnSumSc Num(19,6) Net SC
  LogInstanc Int(11) Log Instance default=0
  ObjCode nVarChar(20) Object Type default=164 ->ADP1
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

# CSI1 - A/R Correction Invoice - Rows
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
  DocEntry Int(11) Document Internal ID ->OCSI
  LineNum Int(11) Row Number
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=, 165=A/R Correction Invoice, 166=A/R Correction Invoice Reversal]
  TrgetEntry Int(11) Target Document Internal ID
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 13=A/R Invoice, 165=A/R Correction Invoice]
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
  InvntSttus VarChar(1) Inventory Direction default=O [O=Open, C=Closed]
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
  UpdInvntry VarChar(1) Inventory Update default=Y [Y=Yes, N=No]
  BaseDocNum Int(11) Base Document No.
  BaseAtCard nVarChar(100) Customer/Vendor Base Document
  SWW nVarChar(16) Additional Identifier
  VatSum Num(19,6) Total Tax
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  FinncPriod Int(11) Posting Period ->OFPR
  ObjType nVarChar(20) Object Type default=165 ->ADP1
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
  LineVatlF Num(19,6) Net Tax Amount
  LineVatS Num(19,6) Net Tax Amount
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value
  CEECFlag VarChar(1) Correction Invoice Was/Should Be default=S [W=Was, S=Should be]
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

# CSI10 - A/R Correction Invoice - Row Structure
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SECONDERY U: DocEntry, AftLineNum, OrderNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSI
  LineSeq Int(11) Row Sequence
  AftLineNum Int(11) After Row Number
  OrderNum Int(11) Order Number
  LineType VarChar(1) Row Type [T=Text, S=Subtotal]
  LineText Text(16) Row Text
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=165 ->ADP1

# CSI11 - A/R Corr. Inv. - Drawn Dpm Det
Module: Marketing Documents | 70 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LineSeq
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSI
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
  ObjType nVarChar(20) Object Type default=165 ->ADP1
  LogInstanc Int(11) Log Instance
  IsAcq VarChar(1) Liable for Acquisition Tax default=N [N=No, Y=Yes]
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

# CSI12 - A/R Correction Invoice - Tax Extension
Module: Marketing Documents | 117 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSI
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
  Carrier nVarChar(15) Carrier Code
  QoP Int(11) Quantity of Packs
  PackDesc nVarChar(10) Pack Description
  Brand nVarChar(20) Brand
  NoSU Int(11) Number of Shipping Unit
  NetWeight Num(19,6) Net Weight
  GrsWeight Num(19,6) Gross Weight
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=165 ->ADP1
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

# CSI13 - A/R Correction Invoice Rows - Distributed Expenses
Module: Marketing Documents | 59 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSI
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=165 ->ADP1
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

# CSI14 - A/R Correction Invoice - Assembly - Rows
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSI
  LineNum Int(11) Row Number default=-1
  ChildNum Int(11) Child Number default=-1
  ItemCode nVarChar(50) Item no. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  TotalQty Num(19,6) Total Quantity
  OpenQty Num(19,6) Remaining Open Quantity
  ObjectType nVarChar(20) object type default=165 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BaseChildN Int(11) Base Child Number default=-1
  EncryptIV nVarChar(100) Encrypt IV

# CSI15 - A/R Corr Inv - Drawn Dpm Appld
Module: Marketing Documents | 84 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSI
  LineNum Int(11) Row Number
  ObjType nVarChar(20) object type default=165 ->ADP1
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

# CSI16 - A/R Corr. Inv. - SnB properties
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, SnBIndex
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) abs entry ->OCSI
  LineNum Int(11) Line Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object id
  ObjAbs Int(11) Object Abs
  DrfWObjAbs Int(11) draft Wobj Abs default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type default=165
  LogInstanc Int(11) Log Instance

# CSI17 - A/R Correction Invoice - Import Process
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSI
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=165 ->ADP1
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

# CSI18 - A/R Correction Invoice - Export Process
Module: Marketing Documents | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSI
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=165 ->ADP1
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

# CSI19 - A/R Correction Invoice - Bin Allocation Data
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, BinAllocSe
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OCSI
  BinAllocSe Int(11) Bin Allocation Sequence
  LineNum Int(11) Line Number
  SubLineNum Int(11) Subline Number default=-1
  SnBType Int(11) SnB Type default=-1
  SnBMDAbs Int(11) SnB Master Data Internal No. default=-1
  BinAbs Int(11) Bin Internal Number ->OBIN
  Quantity Num(19,6) Quantity
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjType nVarChar(20) Object Type default=165 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  BinActTyp Int(6) Bin Action Type [1=Transaction In, 2=Transaction Out, 4=SnB Complete, 8=Bin First Then SnB]

# CSI2 - A/R Corr Inv - Freight - Rows
Module: Marketing Documents | 64 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSI
  LineNum Int(11) Row Number
  GroupNum Int(11) Expense Group
  ExpnsCode Int(11) Expense Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid in FC
  PaidSys Num(19,6) Paid in SC
  ObjType nVarChar(20) Object Type default=165 ->ADP1
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
  WtLiable VarChar(1) WT Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
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

# CSI20 - Intrastat Expenses
Module: Marketing Documents | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSI
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
  ObjectType nVarChar(20) Object Type default=165 ->ADP1
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  AppliedLC Num(19,6) Applied
  AppliedFC Num(19,6) Applied (FC)
  AppliedSC Num(19,6) Applied (SC)

# CSI21 - A/R Correction Invoice - Document Reference Information
Module: Marketing Documents | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, RefType
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjectType nVarChar(20) Object Type default=165
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

# CSI22 - A/R Correction Invoice - Resource Costs
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, StdCostNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->CSI1
  LineNum Int(11) Row Number ->CSI1
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=165
  LogInstanc Int(11) Log Instance default=0

# CSI23 - A/P Invoice - Selected Asset Master Data
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, VisOrder
  ASSETS: DocEntry, LineNum, AssetCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPCH
  LineNum Int(11) Row Number
  AssetCode nVarChar(50) Selected Asset Code ->OCSI
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Remarks nVarChar(100) Remarks
  Amount Num(19,6) Amount
  AmountSC Num(19,6) Amount (SC)
  SerialNo nVarChar(30) Serial Number
  VisOrder Int(11) Visual Order
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=165 ->ADP1

# CSI24 - A/R Correction Invoice - Tracking Note Assignment
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
  ObjType nVarChar(20) Object Type default=165 ->ADP1
  SubLineNum Int(11) BOM Line No.

# CSI25 - A/R Correction Invoice - Amt Per VAT Grp
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
  ObjType nVarChar(20) Object Type default=165 ->ADP1

# CSI26 - A/R Correction Invoice - E-Way Bill Information
Module: Marketing Documents | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSI
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
  ObjectType nVarChar(20) Object Type default=165 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TspEntry Int(11) Transporter Abs. Entry ->OTSP
  TspLine Int(11) Transportation Line
  TransType Int(11) Transaction Type [1=Regular, 2=Bill To-Ship To, 3=Bill From-Dispatch From, 4=Combination of 2 and 3]

# CSI27 - A/R Correction Invoice - E-Books(GR) Rows
Module: Marketing Documents | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  RELATE_ROW: DocEntry, RelateType, RelateLine, GroupNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSI
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

# CSI28 - A/R Correction Invoice - Reported Tracking Note
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
  ObjType nVarChar(20) Object Type default=165 ->ADP1
  SubLineNum Int(11) BOM Line No.

# CSI3 - A/R Correction Invoice - Freight
Module: Marketing Documents | 80 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  DOCUMENT: DocEntry, BaseAbsEnt
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSI
  ExpnsCode Int(11) Expense Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid in FC
  PaidSys Num(19,6) Paid in SC
  Comments nVarChar(100) Remarks
  ObjType nVarChar(20) Object Type default=165 ->ADP1
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
  IsAcquistn VarChar(1) Aquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  WTLiable VarChar(1) WT Liable [Y=Yes, N=No]
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
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type [-1=, 0=, 13=A/R Invoice, 165=A/R Correction Invoice]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Line No.
  LineNum Int(11) line num default=-1
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Abs. Entry default=-1
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

# CSI4 - A/R Correction Invoice - Tax Amount Per Document
Module: Marketing Documents | 61 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SCONDARY: DocEntry, LineNum, GroupNum, ExpnsCode, StcCode, StaCode, staType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSI
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
  ObjectType nVarChar(20) Object Type default=165 ->ADP1
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

# CSI5 - A/R Correction Invoice - Withholding Tax
Module: Marketing Documents | 158 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  SECONDERY U: AbsEntry, WTCode, BaseAbsEnt, Doc1LineNo
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator ->OCSI
  WTCode nVarChar(4) WT Code ->OWHT
  Rate Num(19,6) Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntSC Num(19,6) Taxable Amount (SC)
  TxblAmntFC Num(19,6) Taxable Amount (FC)
  WTAmnt Num(19,6) WT Amount
  WTAmntSC Num(19,6) WT Amount (SC)
  WTAmntFC Num(19,6) WT Amount (FC)
  ApplAmnt Num(19,6) Applied WT Amount
  ApplAmntSC Num(19,6) Applied WTax Amount (SC)
  ApplAmntFC Num(19,6) Applied WTax Amount (FC)
  Category VarChar(1) Category [P=Payment, I=Invoice]
  Criteria VarChar(1) WT Criteria [Y=Accrual, N=Cash]
  Account nVarChar(15) G/L Account ->OACT
  Type VarChar(1) Withholding Type [V=VAT Withholding, I=Income Tax Withholding]
  RoundType VarChar(1) Rounding Type [T=Truncated, C=Commercial Values, N=No Rounding]
  BaseType VarChar(1) Base Type [G=Gross, N=Net, V=VAT, U=UoM]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseLine Int(11) Base Line
  BaseNum Int(11) Base Document Type default=-1 [-1=, 0=, 13=A/R Invoice, 165=A/R Correction Invoice]
  LineNum Int(11) Line Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Abs. Entry default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=165 ->ADP1
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

# CSI6 - A/R Corr. Inv. - Installments
Module: Marketing Documents | 65 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, InstlmntID
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSI
  InstlmntID Int(6) Installment ID default=1
  ObjType nVarChar(20) Object Type default=165 ->ADP1
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
  ExpnsBlck Num(19,6) Reserved Freight Amount
  ExpnsBlckF Num(19,6) Reserved Freight Amount (FC)
  ExpnsBlckS Num(19,6) Reserved Freight Amount (SC)
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

# CSI7 - A/R Corr. Inv. Deliv. Pkgs
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSI
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type default=165 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV

# CSI8 - A/R Corr. Inv. - Items in Pkg
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum, ItemCode, UomEntry, NumPerMsr
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSI
  PackageNum Int(11) Package Number
  ItemCode nVarChar(50) Item Code ->OITM
  Quantity Num(19,6) Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=165 ->ADP1
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value default=0

# CSI9 - A/R Corr. Inv. - Drawn Dpm
Module: Marketing Documents | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSI
  LineNum Int(11) Row Number
  BaseAbs Int(11) Base Document Internal ID
  BaseLine Int(11) Base Document Row
  TargetBase VarChar(1) Target or Base Document default=T [B=Base, T=Target]
  ObjType nVarChar(20) Base Object Type default=203
  DrawnSum Num(19,6) Net LC
  DrawnSumFc Num(19,6) Net FC
  DrawnSumSc Num(19,6) Net SC
  LogInstanc Int(11) Log Instance default=0
  ObjCode nVarChar(20) Object Type default=165 ->ADP1
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

# CSV1 - A/R Correction Invoice Reversal - Rows
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
  DocEntry Int(11) Document Internal ID ->OCSV
  LineNum Int(11) Row Number
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=]
  TrgetEntry Int(11) Target Document Internal ID
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 165=A/R Correction Invoice]
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
  InvntSttus VarChar(1) Inventory Direction default=O [O=Open, C=Closed]
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
  UpdInvntry VarChar(1) Inventory Update default=Y [Y=Yes, N=No]
  BaseDocNum Int(11) Base Document No.
  BaseAtCard nVarChar(100) Customer/Vendor Base Document
  SWW nVarChar(16) Additional Identifier
  VatSum Num(19,6) Total Tax
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  FinncPriod Int(11) Posting Period ->OFPR
  ObjType nVarChar(20) Object Type default=166 ->ADP1
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
  LineVatlF Num(19,6) Net Tax Amount
  LineVatS Num(19,6) Net Tax Amount
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value
  CEECFlag VarChar(1) Correction Invoice Was/Should Be default=S [W=Was, S=Should be]
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

# CSV10 - A/R Correction Invoice Reversal - Row Structure
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SECONDERY U: DocEntry, AftLineNum, OrderNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSV
  LineSeq Int(11) Row Sequence
  AftLineNum Int(11) After Row Number
  OrderNum Int(11) Order Number
  LineType VarChar(1) Row Type [T=Text, S=Subtotal]
  LineText Text(16) Row Text
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=166 ->ADP1

# CSV11 - A/R CrIn Rev - Drawn Dpm Det.
Module: Marketing Documents | 70 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LineSeq
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSV
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
  ObjType nVarChar(20) Object Type default=166 ->ADP1
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

# CSV12 - A/R Correction Invoice Reversal - Tax Extension
Module: Marketing Documents | 117 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSV
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
  Carrier nVarChar(15) Carrier Code
  QoP Int(11) Quantity of Packs
  PackDesc nVarChar(10) Pack Description
  Brand nVarChar(20) Brand
  NoSU Int(11) Number of Shipping Unit
  NetWeight Num(19,6) Net Weight
  GrsWeight Num(19,6) Gross Weight
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=166 ->ADP1
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

# CSV13 - A/R Correction Invoice Reversal Rows - Distributed Expenses
Module: Marketing Documents | 59 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSV
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=166 ->ADP1
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

# CSV14 - A/R Correction Invoice Reversal - Assembly - Rows
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSV
  LineNum Int(11) Row Number default=-1
  ChildNum Int(11) Child Number default=-1
  ItemCode nVarChar(50) Item no. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  TotalQty Num(19,6) Total Quantity
  OpenQty Num(19,6) Remaining Open Quantity
  ObjectType nVarChar(20) object type default=166 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BaseChildN Int(11) Base Child Number default=-1
  EncryptIV nVarChar(100) Encrypt IV

# CSV15 - A/R CrIn Rev - Drawn Dpm Appld
Module: Marketing Documents | 84 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSV
  LineNum Int(11) Row Number
  ObjType nVarChar(20) object type default=166 ->ADP1
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

# CSV16 - A/R Correction Invoice Reversal - SnB properties
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, SnBIndex
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) abs entry ->OCSV
  LineNum Int(11) Line Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object id
  ObjAbs Int(11) Object Abs
  DrfWObjAbs Int(11) draft Wobj Abs default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type default=166
  LogInstanc Int(11) Log Instance

# CSV17 - A/R Correction Invoice Reversal - Bin Allocation Data
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OCSV
  LineNum Int(11) Bin Allocation Sequence
  LogInstanc Int(11) Line Number default=0
  ObjectType nVarChar(20) Subline Number default=166 ->ADP1
  ImpDocType VarChar(1) SnB Type ->OBSI
  ImpDocNum nVarChar(10) SnB Master Data Internal Number
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

# CSV18 - A/R Correction Invoice Reversal - Export Process
Module: Marketing Documents | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSV
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=166 ->ADP1
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

# CSV19 - A/R Correction Invoice Reversal - Bin Allocation Data
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, BinAllocSe
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OCSV
  BinAllocSe Int(11) Bin Allocation Sequence
  LineNum Int(11) Line Number
  SubLineNum Int(11) Subline Number default=-1
  SnBType Int(11) SnB Type default=-1
  SnBMDAbs Int(11) SnB Master Data Internal No. default=-1
  BinAbs Int(11) Bin Internal Number ->OBIN
  Quantity Num(19,6) Quantity
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjType nVarChar(20) Object Type default=166 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  BinActTyp Int(6) Bin Action Type [1=Transaction In, 2=Transaction Out, 4=SnB Complete, 8=Bin First Then SnB]

# CSV2 - A/R Correction Invoice Reversal - Freight - Rows
Module: Marketing Documents | 64 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSV
  LineNum Int(11) Row Number
  GroupNum Int(11) Expense Group
  ExpnsCode Int(11) Expense Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid in FC
  PaidSys Num(19,6) Paid in SC
  ObjType nVarChar(20) Object Type default=166 ->ADP1
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
  WtLiable VarChar(1) WT Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
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

# CSV20 - Intrastat Expenses
Module: Marketing Documents | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSV
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
  ObjectType nVarChar(20) Object Type default=166 ->ADP1
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  AppliedLC Num(19,6) Applied
  AppliedFC Num(19,6) Applied (FC)
  AppliedSC Num(19,6) Applied (SC)

# CSV21 - A/R Correction Invoice Reversal - Document Reference Information
Module: Marketing Documents | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, RefType
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjectType nVarChar(20) Object Type default=166
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

# CSV22 - A/R Correction Invoice Reversal - Resource Costs
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, StdCostNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->CSV1
  LineNum Int(11) Row Number ->CSV1
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=166
  LogInstanc Int(11) Log Instance default=0

# CSV23 - A/P Invoice - Selected Asset Master Data
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, VisOrder
  ASSETS: DocEntry, LineNum, AssetCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSV
  LineNum Int(11) Row Number
  AssetCode nVarChar(50) Selected Asset Code ->OITM
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Remarks nVarChar(100) Remarks
  Amount Num(19,6) Amount
  AmountSC Num(19,6) Amount (SC)
  SerialNo nVarChar(30) Serial Number
  VisOrder Int(11) Visual Order
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=166 ->ADP1

# CSV24 - A/R Correction Invoice Reversal - Tracking Note Assignment
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
  ObjType nVarChar(20) Object Type default=166 ->ADP1
  SubLineNum Int(11) BOM Line No.

# CSV25 - A/R Correction Invoice Reversal - Amt Per VAT Grp
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
  ObjType nVarChar(20) Object Type default=166 ->ADP1

# CSV26 - A/R Correction Invoice Reversal - E-Way Bill Information
Module: Marketing Documents | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSV
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
  ObjectType nVarChar(20) Object Type default=166 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TspEntry Int(11) Transporter Abs. Entry ->OTSP
  TspLine Int(11) Transportation Line
  TransType Int(11) Transaction Type [1=Regular, 2=Bill To-Ship To, 3=Bill From-Dispatch From, 4=Combination of 2 and 3]

# CSV27 - A/R Correction Invoice Reversal - E-Books(GR) Rows
Module: Marketing Documents | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  RELATE_ROW: DocEntry, RelateType, RelateLine, GroupNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSV
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

# CSV28 - A/R Correction Invoice Reversal - Reported Tracking Note
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
  ObjType nVarChar(20) Object Type default=166 ->ADP1
  SubLineNum Int(11) BOM Line No.

# CSV3 - A/R Correction Invoice Reversal - Freight
Module: Marketing Documents | 80 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  DOCUMENT: DocEntry, BaseAbsEnt
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSV
  ExpnsCode Int(11) Expense Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid in FC
  PaidSys Num(19,6) Paid in SC
  Comments nVarChar(100) Remarks
  ObjType nVarChar(20) Object Type default=166 ->ADP1
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
  IsAcquistn VarChar(1) Aquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  WTLiable VarChar(1) WT Liable [Y=Yes, N=No]
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
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type [-1=, 0=, 165=A/R Correction Invoice]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Line No.
  LineNum Int(11) line num default=-1
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Abs. Entry default=-1
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

# CSV4 - A/R Correction Invoice Reversal - Tax Amount Per Document
Module: Marketing Documents | 61 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SCONDARY: DocEntry, LineNum, GroupNum, ExpnsCode, StcCode, StaCode, staType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSV
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
  ObjectType nVarChar(20) Object Type default=166 ->ADP1
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

# CSV5 - A/R Correction Invoice Reversal - WTax
Module: Marketing Documents | 158 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  SECONDERY U: AbsEntry, WTCode, BaseAbsEnt, Doc1LineNo
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator ->OCSV
  WTCode nVarChar(4) WT Code ->OWHT
  Rate Num(19,6) Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntSC Num(19,6) Taxable Amount (SC)
  TxblAmntFC Num(19,6) Taxable Amount (FC)
  WTAmnt Num(19,6) WT Amount
  WTAmntSC Num(19,6) WT Amount (SC)
  WTAmntFC Num(19,6) WT Amount (FC)
  ApplAmnt Num(19,6) Applied WT Amount
  ApplAmntSC Num(19,6) Applied WTax Amount (SC)
  ApplAmntFC Num(19,6) Applied WTax Amount (FC)
  Category VarChar(1) Category [P=Payment, I=Invoice]
  Criteria VarChar(1) WT Criteria [Y=Accrual, N=Cash]
  Account nVarChar(15) G/L Account ->OACT
  Type VarChar(1) Withholding Type [V=VAT Withholding, I=Income Tax Withholding]
  RoundType VarChar(1) Rounding Type [T=Truncated, C=Commercial Values, N=No Rounding]
  BaseType VarChar(1) Base Type [G=Gross, N=Net, V=VAT, U=UoM]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseLine Int(11) Base Line
  BaseNum Int(11) Base Document Type default=-1 [-1=, 0=, 165=A/R Correction Invoice]
  LineNum Int(11) Line Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Abs. Entry default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=166 ->ADP1
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

# CSV6 - A/R Correction Invoice Reversal - Installments
Module: Marketing Documents | 65 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, InstlmntID
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSV
  InstlmntID Int(6) Installment ID default=1
  ObjType nVarChar(20) Object Type default=166 ->ADP1
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
  ExpnsBlck Num(19,6) Reserved Freight Amount
  ExpnsBlckF Num(19,6) Reserved Freight Amount (FC)
  ExpnsBlckS Num(19,6) Reserved Freight Amount (SC)
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

# CSV7 - A/R Correction Invoice Reversal - Delivery Packages
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSV
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type default=166 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV

# CSV8 - A/R Correction Invoice Reversal - Items in Package
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum, ItemCode, UomEntry, NumPerMsr
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSV
  PackageNum Int(11) Package Number
  ItemCode nVarChar(50) Item Number ->OITM
  Quantity Num(19,6) Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=166 ->ADP1
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value default=0

# CSV9 - A/R CrIn Rev - Drawn Dpm
Module: Marketing Documents | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSV
  LineNum Int(11) Row Number
  BaseAbs Int(11) Base Document Internal ID
  BaseLine Int(11) Base Document Row
  TargetBase VarChar(1) Target or Base Document default=B [B=Base, T=Target]
  ObjType nVarChar(20) Base Object Type
  DrawnSum Num(19,6) Net LC
  DrawnSumFc Num(19,6) Net FC
  DrawnSumSc Num(19,6) Net SC
  LogInstanc Int(11) Log Instance default=0
  ObjCode nVarChar(20) Object Type default=166 ->ADP1
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

# DLN1 - Delivery - Rows
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
  DocEntry Int(11) Document Internal ID ->ODLN
  LineNum Int(11) Row Number
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=, 13=A/R Invoice, 16=A/R Returns, 203=A/R Down Payment, 234000031=A/R Return Request]
  TrgetEntry Int(11) Target Document Internal ID
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 23=Sales Quotation, 17=Sales Order, 16=A/R Returns, 13=A/R Invoice, 165=A/R Correction Invoice, 15=Delivery]
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
  ObjType nVarChar(20) Object Type default=15 ->ADP1
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
  PoTrgNum Int(11) Target PO No.
  PoTrgEntry nVarChar(11) Target PO Entry
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
  LineVatlF Num(19,6) Net Tax Amount (SC)
  LineVatS Num(19,6) Net Tax Amount (FC)
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

# DLN10 - Delivery - Row Structure
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SECONDARY U: DocEntry, AftLineNum, OrderNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODLN
  LineSeq Int(11) Row Sequence
  AftLineNum Int(11) After Row Number
  OrderNum Int(11) Order Number
  LineType VarChar(1) Row Type [T=Text, S=Subtotal]
  LineText Text(16) Row Text
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=15 ->ADP1

# DLN11 - Delivery - Drawn Dpm Detail
Module: Marketing Documents | 70 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LineSeq
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODLN
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
  ObjType nVarChar(20) Object Type default=15 ->ADP1
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

# DLN12 - Delivery - Tax Extension
Module: Marketing Documents | 117 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODLN
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
  ObjectType nVarChar(20) Object Type default=15 ->ADP1
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

# DLN13 - Delivery Rows - Distributed Expenses
Module: Marketing Documents | 59 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODLN
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=15 ->ADP1
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

# DLN14 - Delivery Notes - Assembly - Rows
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODLN
  LineNum Int(11) Row Number default=-1
  ChildNum Int(11) Child Number default=-1
  ItemCode nVarChar(50) Item no. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  TotalQty Num(19,6) Total Quantity
  OpenQty Num(19,6) Remaining Open Quantity
  ObjectType nVarChar(20) object type default=15 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BaseChildN Int(11) Base Child Number default=-1
  EncryptIV nVarChar(100) Encrypt IV

# DLN15 - Delivery - Drawn Dpm Applied
Module: Marketing Documents | 84 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODLN
  LineNum Int(11) Row Number
  ObjType nVarChar(20) object type default=15 ->ADP1
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

# DLN16 - Delivery - SnB properties
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, SnBIndex
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) abs entry ->ODLN
  LineNum Int(11) Line Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object id
  ObjAbs Int(11) Object Abs
  DrfWObjAbs Int(11) draft Wobj Abs default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type default=15
  LogInstanc Int(11) Log Instance

# DLN17 - Delivery - Import Process
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODLN
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=15 ->ADP1
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

# DLN18 - Delivery - Export Process
Module: Marketing Documents | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODLN
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=15 ->ADP1
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

# DLN19 - Delivery - Bin Allocation Data
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, BinAllocSe
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->ODLN
  BinAllocSe Int(11) Bin Allocation Sequence
  LineNum Int(11) Line Number
  SubLineNum Int(11) Subline Number default=-1
  SnBType Int(11) SnB Type default=-1
  SnBMDAbs Int(11) SnB Master Data Internal No. default=-1
  BinAbs Int(11) Bin Internal Number ->OBIN
  Quantity Num(19,6) Quantity
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjType nVarChar(20) Object Type default=15 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  BinActTyp Int(6) Bin Action Type [1=Transaction In, 2=Transaction Out, 4=SnB Complete, 8=Bin First Then SnB]

# DLN2 - Delivery Notes - Freight - Rows
Module: Marketing Documents | 64 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODLN
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Expense Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid in FC
  PaidSys Num(19,6) Paid in SC
  ObjType nVarChar(20) Object Type default=15 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) VAT Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) VAT Group ->OVTG
  VatPrcnt Num(19,6) Row VAT %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Aquisition Tax default=N [Y=Yes, N=No]
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
  WtLiable VarChar(1) WT Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
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

# DLN20 - Intrastat Expenses
Module: Marketing Documents | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODLN
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
  ObjectType nVarChar(20) Object Type default=15 ->ADP1
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  AppliedLC Num(19,6) Applied
  AppliedFC Num(19,6) Applied (FC)
  AppliedSC Num(19,6) Applied (SC)

# DLN21 - Delivery - Document Reference Information
Module: Marketing Documents | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, RefType
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjectType nVarChar(20) Object Type default=15
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

# DLN22 - Delivery - Resource Costs
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, StdCostNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->DLN1
  LineNum Int(11) Row Number ->DLN1
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=15
  LogInstanc Int(11) Log Instance default=0

# DLN23 - A/P Invoice - Selected Asset Master Data
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, VisOrder
  ASSETS: DocEntry, LineNum, AssetCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODLN
  LineNum Int(11) Row Number
  AssetCode nVarChar(50) Selected Asset Code ->OITM
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Remarks nVarChar(100) Remarks
  Amount Num(19,6) Amount
  AmountSC Num(19,6) Amount (SC)
  SerialNo nVarChar(30) Serial Number
  VisOrder Int(11) Visual Order
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=15 ->ADP1

# DLN24 - Delivery - Tracking Note Assignment
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
  ObjType nVarChar(20) Object Type default=15 ->ADP1
  SubLineNum Int(11) BOM Line No.

# DLN25 - Delivery - Amt Per VAT Grp
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
  ObjType nVarChar(20) Object Type default=15 ->ADP1

# DLN26 - Delivery - E-Way Bill Information
Module: Marketing Documents | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODLN
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
  ObjectType nVarChar(20) Object Type default=15 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TspEntry Int(11) Transporter Abs. Entry ->OTSP
  TspLine Int(11) Transportation Line
  TransType Int(11) Transaction Type [1=Regular, 2=Bill To-Ship To, 3=Bill From-Dispatch From, 4=Combination of 2 and 3]

# DLN27 - Delivery - E-Books(GR) Rows
Module: Marketing Documents | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  RELATE_ROW: DocEntry, RelateType, RelateLine, GroupNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODLN
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

# DLN28 - Delivery - Reported Tracking Note
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
  ObjType nVarChar(20) Object Type default=15 ->ADP1
  SubLineNum Int(11) BOM Line No.

# DLN3 - Delivery Notes - Freight
Module: Marketing Documents | 80 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  DOCUMENT: DocEntry, BaseAbsEnt
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODLN
  ExpnsCode Int(11) Expense Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid in FC
  PaidSys Num(19,6) Paid in SC
  Comments nVarChar(100) Remarks
  ObjType nVarChar(20) Object Type default=15 ->ADP1
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
  WTLiable VarChar(1) WT Liable [Y=Yes, N=No]
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
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 23=Sales Quotation, 17=Sales Order, 16=A/R Returns, 13=A/R Invoice]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Line No.
  LineNum Int(11) line num default=-1
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Abs. Entry default=-1
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

# DLN4 - Delivery - Tax Amount per Document
Module: Marketing Documents | 61 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SCONDARY: DocEntry, LineNum, GroupNum, ExpnsCode, StcCode, StaCode, staType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODLN
  LineNum Int(11) Row Number default=-1
  GroupNum Int(11) Group Number default=-1
  ExpnsCode Int(11) Freight Code default=-1 ->OEXD
  RelateType Int(11) Relation Type default=1 [1=Row, 2=Row Freight Charges, 3=Document Expenses]
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
  ObjectType nVarChar(20) Object Type default=15 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Status default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
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
  NonDdctPrc Num(19,6) Non-Deductible %
  NonDdctAct nVarChar(15) Nondeductible Account ->OACT
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

# DLN5 - Delivery - Withholding Tax
Module: Marketing Documents | 158 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  SECONDERY U: AbsEntry, WTCode, BaseAbsEnt
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->ODLN
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
  BaseNum Int(11) Base Document Type default=-1 [-1=, 0=, 23=Sales Quotation, 17=Sales Order, 16=A/R Returns, 13=A/R Invoice]
  LineNum Int(11) Row Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Doc. Internal No. default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=15 ->ADP1
  Doc1LineNo Int(11) DOC1 Row Number default=-1
  WtLineType VarChar(1) WTax Row Type default=D [D=Document Level WTax, L=Row Level WTax]
  TxblCurr nVarChar(3) Taxable Currency from Doc Row
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

# DLN6 - Delivery - Installments
Module: Marketing Documents | 65 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, InstlmntID
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODLN
  InstlmntID Int(6) Installment ID default=1
  ObjType nVarChar(20) Object Type default=15 ->ADP1
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

# DLN7 - Delivery Packages
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODLN
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type default=15 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV

# DLN8 - Items in Package - Delivery
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum, ItemCode, UomEntry, NumPerMsr
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODLN
  PackageNum Int(11) Package Number
  ItemCode nVarChar(50) Item Number ->OITM
  Quantity Num(19,6) Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=15 ->ADP1
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value default=0

# DLN9 - Delivery - Drawn Dpm
Module: Marketing Documents | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODLN
  LineNum Int(11) Row Number
  BaseAbs Int(11) Base Document Internal ID
  BaseLine Int(11) Base Document Row
  TargetBase VarChar(1) Target or Base Document default=B [B=Base, T=Target]
  ObjType nVarChar(20) Base Object Type
  DrawnSum Num(19,6) Net LC
  DrawnSumFc Num(19,6) Net FC
  DrawnSumSc Num(19,6) Net SC
  LogInstanc Int(11) Log Instance default=0
  ObjCode nVarChar(20) Object Type default=15 ->ADP1
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

# DOC1 - Mktg Docs - Row
Module: Marketing Documents | 316 columns
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
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=, 14=A/R Credit Note, 15=Delivery]
  TrgetEntry Int(11) Target Document Internal ID
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 23=Sales Quotation, 17=Sales Order, 15=Delivery]
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
  DocDate Date(8) Post. Date
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
  ObjType nVarChar(20) Object Type default=13 ->ADP1
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
  CEECFlag VarChar(1) Correction Invoice Was/Should Be default=S [W=Was, S=Should be]
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
  StckINMPr Num(19,6) Inventory Journal Price
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
  StckAppDFC Num(19,6) Stock Distrib - Applied Sum FC
  StckAppDSC Num(19,6) Stock Distrib - Applied Sum SC
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
  ChgAsmBoMW VarChar(1) Change Whse for Asm BoM Child [Y=Yes, N=No]
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

# DOC10 - Mktg Docs - Row Structure
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SECONDERY U: DocEntry, AftLineNum, OrderNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineSeq Int(11) Row Sequence
  AftLineNum Int(11) After Row Number
  OrderNum Int(11) Order Number
  LineType VarChar(1) Row Type [T=Text, S=Subtotal]
  LineText Text(16) Row Text
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=13 ->ADP1

# DOC11 - Mktg Docs - Drawn Dpm Detail
Module: Marketing Documents | 70 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LineSeq
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  LineSeq Int(11) Sequence Number
  BaseAbs Int(11) Base Document Internal ID default=-1
  BaseType Int(11) Base Object Type default=-1 [-1=]
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  VatPrcnt Num(19,6) VAT Percent
  LineTotal Num(19,6) Net LC
  TotalFrgn Num(19,6) Net FC
  TotalSumSy Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFrgn Num(19,6) Tax FC
  VatSumSys Num(19,6) Tax SC
  ObjType nVarChar(20) Object Type default=13 ->ADP1
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

# DOC12 - Mktg Docs - Tax Extension
Module: Marketing Documents | 116 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
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
  ObjectType nVarChar(20) Object Type default=13 ->ADP1
  TaxId10 nVarChar(100) Tax ID 10
  TransCat nVarChar(100) Trans. Category
  FormNo nVarChar(100) Form #
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
  Vat VarChar(1) VAT default=N [N=, Y=]
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

# DOC13 - Mktg Docs - Freight Hist Rows
Module: Marketing Documents | 59 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=13 ->ADP1
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
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=, N=]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=, N=, U=]
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
  WtLiable VarChar(1) WTax Liable [Y=, N=]
  BaseMethod VarChar(1) Base Method [N=, Q=, V=, W=, T=, A=]
  Stock VarChar(1) Stock default=N [Y=, N=]
  LstPchPrce VarChar(1) Last Purchase Price [Y=, N=]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=, N=]
  BaseAbsEnt Int(11) Base Doc Internal ID default=-1
  BaseType Int(11) Base Document Type
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Line No.
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Document Internal ID default=-1
  BaseGroup Int(11) Base Document Group default=-1
  Status VarChar(1) Status default=O [O=, C=]
  TrgGroup Int(11) Target Group default=-1
  VisOrder Int(11) Visual Order
  DistrbMthd VarChar(1) Distribution Method [N=, Q=, V=, W=, E=, T=]
  DistribExp VarChar(1) Distribute Freights [Y=, N=]
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ

# DOC14 - Mktg Docs - Assembly Row
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number default=-1
  ChildNum Int(11) Child Number default=-1
  ItemCode nVarChar(50) Item no. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  TotalQty Num(19,6) Total Quantity
  OpenQty Num(19,6) Remaining Open Quantity
  ObjectType nVarChar(20) object type ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BaseChildN Int(11) Base Child Number default=-1
  EncryptIV nVarChar(100) Encrypt IV

# DOC15 - Mktg Docs - Drawn Dpm Applied
Module: Marketing Documents | 84 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  ObjType nVarChar(20) object type default=13 ->ADP1
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

# DOC16 - Mktg Docs - SnB property
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, SnBIndex
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) abs entry ->OCSV
  LineNum Int(11) Line Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object id
  ObjAbs Int(11) Object Abs
  DrfWObjAbs Int(11) draft Wobj Abs default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance

# DOC17 - Mkt Docs - Import Process
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=13 ->ADP1
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

# DOC18 - Mkt Docs - Export Process
Module: Marketing Documents | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=13 ->ADP1
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

# DOC19 - Mktg Docs - Bin Allocation Data
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, BinAllocSe
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->ODOC
  BinAllocSe Int(11) Bin Allocation Sequence
  LineNum Int(11) Line Number
  SubLineNum Int(11) Subline Number default=-1
  SnBType Int(11) SnB Type default=-1
  SnBMDAbs Int(11) SnB Master Data Internal No. default=-1
  BinAbs Int(11) Bin Internal Number ->OBIN
  Quantity Num(19,6) Quantity
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjType nVarChar(20) Object Type default=13 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  BinActTyp Int(6) Bin Action Type [1=Transaction In, 2=Transaction Out, 4=SnB Complete, 8=Bin First Then SnB]

# DOC2 - Mktg Docs - Rows Distr Freight
Module: Marketing Documents | 64 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=13 ->ADP1
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

# DOC20 - Intrastat Expenses
Module: Marketing Documents | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
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
  ObjectType nVarChar(20) Object Type default=13 ->ADP1
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  AppliedLC Num(19,6) Applied
  AppliedFC Num(19,6) Applied (FC)
  AppliedSC Num(19,6) Applied (SC)

# DOC21 - Mktg Docs - Document Reference Information
Module: Marketing Documents | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, RefType
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjectType nVarChar(20) Object Type default=0
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

# DOC22 - Mktg Docs - Resource Costs
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, StdCostNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->DOC1
  LineNum Int(11) Row Number ->DOC1
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=13
  LogInstanc Int(11) Log Instance default=0

# DOC23 - A/P Invoice - Selected Asset Master Data
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, VisOrder
  ASSETS: DocEntry, LineNum, AssetCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  AssetCode nVarChar(50) Selected Asset Code ->OITM
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Remarks nVarChar(100) Remarks
  Amount Num(19,6) Amount
  AmountSC Num(19,6) Amount (SC)
  SerialNo nVarChar(30) Serial Number
  VisOrder Int(11) Visual Order
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=13 ->ADP1

# DOC24 - Mktg Docs - Tracking Note Assignment
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
  ObjType nVarChar(20) Object Type default=0 ->ADP1
  SubLineNum Int(11) BOM Line No.

# DOC25 - Mktg Docs - Amt Per VAT Grp
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
  ObjType nVarChar(20) Object Type default=0 ->ADP1

# DOC26 - Mktg. Docs. - E-Way Bill Information
Module: Marketing Documents | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
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
  ObjectType nVarChar(20) Object Type default=13 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TspEntry Int(11) Transporter Abs. Entry ->OTSP
  TspLine Int(11) Transportation Line
  TransType Int(11) Transaction Type default=1 [1=Regular, 2=Bill To-Ship To, 3=Bill From-Dispatch From, 4=Combination of 2 and 3]

# DOC27 - Mktg. Docs. - E-Books(GR) Rows
Module: Marketing Documents | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  RELATE_ROW: DocEntry, RelateType, RelateLine, GroupNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
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

# DOC28 - Marketing Docs. - Reported Tracking Note
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
  ObjType nVarChar(20) Object Type default=0 ->ADP1
  SubLineNum Int(11) BOM Line No.

# DOC3 - Mktg Docs - Freight
Module: Marketing Documents | 80 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  DOCUMENT: DocEntry, BaseAbsEnt
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  Comments nVarChar(100) Remarks
  ObjType nVarChar(20) Object Type default=13 ->ADP1
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
  TrgAbsEnt Int(11) Target Document Internal ID default=-1
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

# DOC4 - Mktg Docs - Tax Amt Per Doc
Module: Marketing Documents | 61 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SCONDARY: DocEntry, LineNum, GroupNum, ExpnsCode, StcCode, StaCode, staType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
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
  ObjectType nVarChar(20) Object Type default=13 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Status default=Y [Y=Normal Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) Applied Tax
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  LineSeq Int(11) Row Sequence
  DeferrAcct nVarChar(15) Deferred Tax Account ->OACT
  BaseType Int(11) Base Document Type default=-1
  BaseAbs Int(11) Base Document Internal ID default=-1
  BaseSeq Int(11) Base Doc. Row Sequence
  DeductTax Num(19,6) Deductible Tax Amount
  DdctTaxFrg Num(19,6) Deductible Tax Amount (FC)
  DdctTaxSys Num(19,6) Deductible Tax Amount (SC)
  BaseAppld Num(19,6) Applied Base Amount
  BaseApldFC Num(19,6) Applied Base Amount (FC)
  BaseApldSC Num(19,6) Applied Base Amount (SC)
  NonDdctPrc Num(19,6) Non-Deductible %
  NonDdctAct nVarChar(15) Nondeductible Account ->OACT
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

# DOC5 - Mktg Docs - WithholdingTax
Module: Marketing Documents | 158 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  SECONDERY U: AbsEntry, WTCode, BaseAbsEnt, Doc1LineNo
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->ODOC
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
  BaseAbsEnt Int(11) Base Document Internal ID default=-1
  BaseLine Int(11) Base Row
  BaseNum Int(11) Base Document Type default=-1 [-1=, 0=, 23=Sales Quotation, 17=Sales Order, 15=Delivery]
  LineNum Int(11) Row Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Document Internal ID default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=13 ->ADP1
  Doc1LineNo Int(11) DOC1 Line Number default=-1
  WtLineType VarChar(1) WTax Row Type default=D [D=Document Level WTax, L=Row Level WTax]
  TxblCurr nVarChar(3) Taxable Currency from Doc Row
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

# DOC6 - Mktg Docs - Installment
Module: Marketing Documents | 65 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, InstlmntID
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  InstlmntID Int(6) Installment ID default=1
  ObjType nVarChar(20) Object Type default=13 ->ADP1
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

# DOC7 - Mktg Docs - Delivery Package
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type default=13 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV

# DOC8 - Mktg Docs - Items in Package
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum, ItemCode, UomEntry, NumPerMsr
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  PackageNum Int(11) Package Number
  ItemCode nVarChar(50) Item Code ->OITM
  Quantity Num(19,6) Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=13 ->ADP1
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value default=0

# DOC9 - Mktg Docs - Drawn Dpm
Module: Marketing Documents | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  LineNum Int(11) Row Number
  BaseAbs Int(11) Base Document Internal ID
  BaseLine Int(11) Base Document Row
  TargetBase VarChar(1) Target or Base Document default=T [B=Base, T=Target]
  ObjType nVarChar(20) Base Object Type default=203
  DrawnSum Num(19,6) Net LC
  DrawnSumFc Num(19,6) Net FC
  DrawnSumSc Num(19,6) Net SC
  LogInstanc Int(11) Log Instance default=0
  ObjCode nVarChar(20) Object Type default=13 ->ADP1
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

# DPI1 - A/R Down Payment - Rows
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
  DocEntry Int(11) Document Internal ID ->ODPI
  LineNum Int(11) Row Number
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=, 20=Goods Receipt, 18=A/P Invoice, 203=A/R Down Payment]
  TrgetEntry Int(11) Target Document Internal ID
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 23=Quotation, 17=Sales Order, 15=Delivery, 203=A/R Down Payment]
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
  Volume Num(19,6) Volume
  VolUnit Int(6) Unit of Measure for Volume
  Weight1 Num(19,6) Weight 1
  Wght1Unit Int(6) Unit of Weight 1
  Weight2 Num(19,6) Weight 2
  Wght2Unit Int(6) Unit of Weight 2
  Factor1 Num(19,6) Factor 1
  Factor2 Num(19,6) Factor 2
  Factor3 Num(19,6) Factor 3
  Factor4 Num(19,6) Factor 4
  PackQty Num(19,6) Packing Quantity
  UpdInvntry VarChar(1) Warehouse Update default=N [Y=Yes, N=No]
  BaseDocNum Int(11) Base Document No.
  BaseAtCard nVarChar(100) Customer/Vendor Base Document
  SWW nVarChar(16) SWW
  VatSum Num(19,6) Total Tax
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  FinncPriod Int(11) Posting Period ->OFPR
  ObjType nVarChar(20) Object Type default=203 ->ADP1
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
  CEECFlag VarChar(1) Correction Invoice Was/Should Be default=S [W=Was, S=Should be]
  ToStock Num(19,6) Corr. Invoice Amount to Stock
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
  StckDstFc Num(19,6) Stock Distributed Sum (FC)
  StckDstSc Num(19,6) Stock Distributed Sum (SC)
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

# DPI10 - A/R Down Payment - Row Structure
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SECONDARY U: DocEntry, AftLineNum, OrderNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPI
  LineSeq Int(11) Row Sequence
  AftLineNum Int(11) After Row Number
  OrderNum Int(11) Order Number
  LineType VarChar(1) Row Type [T=Text, S=Subtotal]
  LineText Text(16) Row Text
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=203 ->ADP1

# DPI11 - A/R DP - Drawn Dpm Detail
Module: Marketing Documents | 70 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LineSeq
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPI
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
  ObjType nVarChar(20) Object Type default=203 ->ADP1
  LogInstanc Int(11) Log Instance
  IsAcq VarChar(1) Liable for Acquisition Tax default=N [N=No, Y=Yes]
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

# DPI12 - Down Payment In - Tax Extension
Module: Marketing Documents | 117 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPI
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
  Carrier nVarChar(15) Carrier Code
  QoP Int(11) Quantity of Packs
  PackDesc nVarChar(10) Pack Description
  Brand nVarChar(20) Brand
  NoSU Int(11) Number of Shipping Unit
  NetWeight Num(19,6) Net Weight
  GrsWeight Num(19,6) Gross Weight
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=203 ->ADP1
  TaxId10 nVarChar(100) Assessee Type
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
  CountryGIP nVarChar(3) Goods Issue Place Country ->OCRY
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
  CtryDlvryP nVarChar(3) Delivery Place Country ->OCRY
  FoneDlvryP nVarChar(20) Delivery Place Phone
  MailDlvryP nVarChar(100) Delivery Place E-Mail
  DpDtDlvryP Date(8) Delivery Place Departure Date
  AuthedCNPJ nVarChar(250) Authorized CNPJ or CPF
  TaxId14 nVarChar(250) ITR Filing

# DPI13 - A/R Down Payment Rows - Distributed Expenses
Module: Marketing Documents | 59 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPI
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=202 ->ADP1
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

# DPI14 - A/R Down Payment - Assembly - Rows
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPI
  LineNum Int(11) Row Number default=-1
  ChildNum Int(11) Child Number default=-1
  ItemCode nVarChar(50) Item no. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  TotalQty Num(19,6) Total Quantity
  OpenQty Num(19,6) Remaining Open Quantity
  ObjectType nVarChar(20) object type default=203 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BaseChildN Int(11) Base Child Number default=-1
  EncryptIV nVarChar(100) Encrypt IV

# DPI15 - A/R DP - Drawn Dpm Applied
Module: Marketing Documents | 84 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPI
  LineNum Int(11) Row Number
  ObjType nVarChar(20) object type default=203 ->ADP1
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

# DPI16 - A/R Down Payment - SnB properties
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, SnBIndex
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) abs entry ->ODPI
  LineNum Int(11) Line Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object id
  ObjAbs Int(11) Object Abs
  DrfWObjAbs Int(11) draft Wobj Abs default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type default=203
  LogInstanc Int(11) Log Instance

# DPI17 - A/R Down Payment - Import Process
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPI
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=203 ->ADP1
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

# DPI18 - A/R Down Payment - Export Process
Module: Marketing Documents | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPI
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=203 ->ADP1
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

# DPI19 - A/R Down Payment - Bin Allocation Data
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, BinAllocSe
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->ODPI
  BinAllocSe Int(11) Bin Allocation Sequence
  LineNum Int(11) Line Number
  SubLineNum Int(11) Subline Number default=-1
  SnBType Int(11) SnB Type default=-1
  SnBMDAbs Int(11) SnB Master Data Internal No. default=-1
  BinAbs Int(11) Bin Internal Number ->OBIN
  Quantity Num(19,6) Quantity
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjType nVarChar(20) Object Type default=203 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  BinActTyp Int(6) Bin Action Type [1=Transaction In, 2=Transaction Out, 4=SnB Complete, 8=Bin First Then SnB]

# DPI2 - A/R Down Payment - Freight - Rows
Module: Marketing Documents | 64 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPI
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=203 ->ADP1
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

# DPI20 - Intrastat Expenses
Module: Marketing Documents | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPI
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
  ObjectType nVarChar(20) Object Type default=203 ->ADP1
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  AppliedLC Num(19,6) Applied
  AppliedFC Num(19,6) Applied (FC)
  AppliedSC Num(19,6) Applied (SC)

# DPI21 - A/R Down Payment - Document Reference Information
Module: Marketing Documents | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, RefType
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjectType nVarChar(20) Object Type default=203
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

# DPI22 - A/R Down Payment - Resource Costs
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, StdCostNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->DPI1
  LineNum Int(11) Row Number ->DPI1
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=203
  LogInstanc Int(11) Log Instance default=0

# DPI23 - A/P Invoice - Selected Asset Master Data
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, VisOrder
  ASSETS: DocEntry, LineNum, AssetCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPI
  LineNum Int(11) Row Number
  AssetCode nVarChar(50) Selected Asset Code ->OITM
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Remarks nVarChar(100) Remarks
  Amount Num(19,6) Amount
  AmountSC Num(19,6) Amount (SC)
  SerialNo nVarChar(30) Serial Number
  VisOrder Int(11) Visual Order
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=20 ->ADP1

# DPI24 - A/R Down Payment - Tracking Note Assignment
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
  ObjType nVarChar(20) Object Type default=203 ->ADP1
  SubLineNum Int(11) BOM Line No.

# DPI25 - A/R Down Payment - Amt Per VAT Grp
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
  ObjType nVarChar(20) Object Type default=203 ->ADP1

# DPI26 - Down Payment Inv. - E-Way Bill Information
Module: Marketing Documents | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPI
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
  ObjectType nVarChar(20) Object Type default=203 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TspEntry Int(11) Transporter Abs. Entry ->OTSP
  TspLine Int(11) Transportation Line
  TransType Int(11) Transaction Type [1=Regular, 2=Bill To-Ship To, 3=Bill From-Dispatch From, 4=Combination of 2 and 3]

# DPI27 - Down Payment Inv. - E-Books(GR) Rows
Module: Marketing Documents | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  RELATE_ROW: DocEntry, RelateType, RelateLine, GroupNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPI
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

# DPI28 - A/R Down Payment - Reported Tracking Note
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
  ObjType nVarChar(20) Object Type default=203 ->ADP1
  SubLineNum Int(11) BOM Line No.

# DPI3 - A/R Down Payment - Freight
Module: Marketing Documents | 80 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  DOCUMENT: DocEntry, BaseAbsEnt
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPI
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  Comments nVarChar(100) Remarks
  ObjType nVarChar(20) Object Type default=202 ->ADP1
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

# DPI4 - A/R Down Payment - Tax Amount per Document
Module: Marketing Documents | 61 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SCONDARY: DocEntry, LineNum, GroupNum, ExpnsCode, StcCode, StaCode, staType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPI
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
  ObjectType nVarChar(20) Object Type default=203 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Status default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) Applied Tax
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

# DPI5 - A/R Down Payment - Withholding Tax
Module: Marketing Documents | 158 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  SECONDERY U: AbsEntry, WTCode, BaseAbsEnt, Doc1LineNo
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator ->ODPI
  WTCode nVarChar(4) WT Code ->OWHT
  Rate Num(19,6) Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntSC Num(19,6) Taxable Amount in SC
  TxblAmntFC Num(19,6) Taxable Amount (FC)
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
  BaseNum Int(11) Base Document Type default=-1 [-1=, 0=, 23=Sales Quotation, 17=Sales Order, 15=Delivery]
  LineNum Int(11) Line Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Abs. Entry default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=203 ->ADP1
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

# DPI6 - A/R Down Payment - Installments
Module: Marketing Documents | 65 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, InstlmntID
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPI
  InstlmntID Int(6) Installment ID default=1
  ObjType nVarChar(20) Object Type default=203 ->ADP1
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

# DPI7 - Delivery Packages - A/R Down Pymt
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPI
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type default=203 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV

# DPI8 - Items in Package - A/R Down Pmt.
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum, ItemCode, UomEntry, NumPerMsr
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPI
  PackageNum Int(11) Package Number
  ItemCode nVarChar(50) Item Code ->OITM
  Quantity Num(19,6) Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=203 ->ADP1
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value default=0

# DPI9 - Down Payment Incoming - Drawn Dpm
Module: Marketing Documents | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPI
  LineNum Int(11) Row Number
  BaseAbs Int(11) Base Document Internal ID
  BaseLine Int(11) Base Document Row
  TargetBase VarChar(1) Target or Base Document default=B [B=Base, T=Target]
  ObjType nVarChar(20) Base Object Type
  DrawnSum Num(19,6) Net LC
  DrawnSumFc Num(19,6) Net FC
  DrawnSumSc Num(19,6) Net SC
  LogInstanc Int(11) Log Instance default=0
  ObjCode nVarChar(20) Object Type default=203 ->ADP1
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

# DPO1 - A/P Down Payment - Rows
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
  DocEntry Int(11) Document Internal ID ->ODPO
  LineNum Int(11) Row Number
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=, 19=Purchase credit note, 204=A/P Down Payment]
  TrgetEntry Int(11) Target Document Internal ID
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 22=Purchase Order, 20=Goods Receipt PO, 204=A/P Down Payment, 540000006=Purchase Quotation]
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
  Volume Num(19,6) Volume
  VolUnit Int(6) Unit of Measure for Volume
  Weight1 Num(19,6) Weight 1
  Wght1Unit Int(6) Unit of Weight 1
  Weight2 Num(19,6) Weight 2
  Wght2Unit Int(6) Unit of Weight 2
  Factor1 Num(19,6) Factor 1
  Factor2 Num(19,6) Factor 2
  Factor3 Num(19,6) Factor 3
  Factor4 Num(19,6) Factor 4
  PackQty Num(19,6) Packing Quantity
  UpdInvntry VarChar(1) Warehouse Update default=N [Y=Yes, N=No]
  BaseDocNum Int(11) Base Document No.
  BaseAtCard nVarChar(100) Customer/Vendor Base Document
  SWW nVarChar(16) SWW
  VatSum Num(19,6) Total Tax
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  FinncPriod Int(11) Posting Period ->OFPR
  ObjType nVarChar(20) Object Type default=204 ->ADP1
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
  CEECFlag VarChar(1) Correction Invoice Was/Should Be default=S [W=Was, S=Should be]
  ToStock Num(19,6) Corr. Invoice Amount to Stock
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
  StckDstFc Num(19,6) Stock Distributed Sum (FC)
  StckDstSc Num(19,6) Stock Distributed Sum (SC)
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

# DPO10 - A/P Down Payment - Row Structure
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SECONDARY U: DocEntry, AftLineNum, OrderNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPO
  LineSeq Int(11) Row Sequence
  AftLineNum Int(11) After Row Number
  OrderNum Int(11) Order Number
  LineType VarChar(1) Row Type [T=Text, S=Subtotal]
  LineText Text(16) Row Text
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=204 ->ADP1

# DPO11 - A/P DP - Drawn Dpm Detail
Module: Marketing Documents | 70 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LineSeq
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPO
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
  ObjType nVarChar(20) Object Type default=204 ->ADP1
  LogInstanc Int(11) Log Instance
  IsAcq VarChar(1) Liable for Acquisition Tax default=N [N=No, Y=Yes]
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

# DPO12 - Down Payment - Tax Extension
Module: Marketing Documents | 117 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPO
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
  Carrier nVarChar(15) Carrier Code
  QoP Int(11) Quantity of Packs
  PackDesc nVarChar(10) Pack Description
  Brand nVarChar(20) Brand
  NoSU Int(11) Number of Shipping Unit
  NetWeight Num(19,6) Net Weight
  GrsWeight Num(19,6) Gross Weight
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=204 ->ADP1
  TaxId10 nVarChar(100) Assessee Type
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

# DPO13 - A/P Down Payment Rows - Distributed Expenses
Module: Marketing Documents | 59 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPO
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=204 ->ADP1
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

# DPO14 - A/P Down Payment - Assembly - Rows
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPO
  LineNum Int(11) Row Number default=-1
  ChildNum Int(11) Child Number default=-1
  ItemCode nVarChar(50) Item no. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  TotalQty Num(19,6) Total Quantity
  OpenQty Num(19,6) Remaining Open Quantity
  ObjectType nVarChar(20) object type default=204 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BaseChildN Int(11) Base Child Number default=-1
  EncryptIV nVarChar(100) Encrypt IV

# DPO15 - A/P DP - Drawn Dpm Applied
Module: Marketing Documents | 84 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPO
  LineNum Int(11) Row Number
  ObjType nVarChar(20) object type default=204 ->ADP1
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

# DPO16 - A/P Down Payment - SnB properties
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, SnBIndex
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) abs entry ->ODPO
  LineNum Int(11) Line Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object id
  ObjAbs Int(11) Object Abs
  DrfWObjAbs Int(11) draft Wobj Abs default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type default=204
  LogInstanc Int(11) Log Instance

# DPO17 - A/P Down Payment - Import Process
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPO
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=204 ->ADP1
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

# DPO18 - A/P Down Payment - Export Process
Module: Marketing Documents | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPO
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=204 ->ADP1
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

# DPO19 - A/P Down Payment - Bin Allocation Data
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, BinAllocSe
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->ODPO
  BinAllocSe Int(11) Bin Allocation Sequence
  LineNum Int(11) Line Number
  SubLineNum Int(11) Subline Number default=-1
  SnBType Int(11) SnB Type default=-1
  SnBMDAbs Int(11) SnB Master Data Internal No. default=-1
  BinAbs Int(11) Bin Internal Number ->OBIN
  Quantity Num(19,6) Quantity
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjType nVarChar(20) Object Type default=204 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  BinActTyp Int(6) Bin Action Type [1=Transaction In, 2=Transaction Out, 4=SnB Complete, 8=Bin First Then SnB]

# DPO2 - A/P Down Payment - Freight - Rows
Module: Marketing Documents | 64 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPO
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=204 ->ADP1
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

# DPO20 - Intrastat Expenses
Module: Marketing Documents | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPO
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
  ObjectType nVarChar(20) Object Type default=204 ->ADP1
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  AppliedLC Num(19,6) Applied
  AppliedFC Num(19,6) Applied (FC)
  AppliedSC Num(19,6) Applied (SC)

# DPO21 - A/P Down Payment - Document Reference Information
Module: Marketing Documents | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, RefType
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjectType nVarChar(20) Object Type default=204
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

# DPO22 - A/P Down Payment - Resource Costs
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, StdCostNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->DPO1
  LineNum Int(11) Row Number ->DPO1
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=204
  LogInstanc Int(11) Log Instance default=0

# DPO23 - A/P Invoice - Selected Asset Master Data
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, VisOrder
  ASSETS: DocEntry, LineNum, AssetCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPO
  LineNum Int(11) Row Number
  AssetCode nVarChar(50) Selected Asset Code ->OITM
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Remarks nVarChar(100) Remarks
  Amount Num(19,6) Amount
  AmountSC Num(19,6) Amount (SC)
  SerialNo nVarChar(30) Serial Number
  VisOrder Int(11) Visual Order
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=204 ->ADP1

# DPO24 - A/P Down Payment - Tracking Note Assignment
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
  ObjType nVarChar(20) Object Type default=204 ->ADP1
  SubLineNum Int(11) BOM Line No.

# DPO25 - A/P Down Payment - Amt Per VAT Grp
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
  ObjType nVarChar(20) Object Type default=204 ->ADP1

# DPO26 - Down Payment - E-Way Bill Information
Module: Marketing Documents | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPO
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
  ObjectType nVarChar(20) Object Type default=204 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TspEntry Int(11) Transporter Abs. Entry ->OTSP
  TspLine Int(11) Transportation Line
  TransType Int(11) Transaction Type [1=Regular, 2=Bill To-Ship To, 3=Bill From-Dispatch From, 4=Combination of 2 and 3]

# DPO27 - Down Payment - E-Books(GR) Rows
Module: Marketing Documents | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  RELATE_ROW: DocEntry, RelateType, RelateLine, GroupNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPO
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

# DPO28 - A/P Down Payment - Reported Tracking Note
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
  ObjType nVarChar(20) Object Type default=204 ->ADP1
  SubLineNum Int(11) BOM Line No.

# DPO3 - A/P Down Payment - Freight
Module: Marketing Documents | 80 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  DOCUMENT: DocEntry, BaseAbsEnt
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPO
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  Comments nVarChar(100) Remarks
  ObjType nVarChar(20) Object Type default=204 ->ADP1
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
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 22=Purchase orders, 20=Goods Receipt PO]
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

# DPO4 - A/P Down Payment - Tax Amount per Document
Module: Marketing Documents | 61 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SCONDARY: DocEntry, LineNum, GroupNum, ExpnsCode, StcCode, StaCode, staType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPO
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
  ObjectType nVarChar(20) Object Type default=204 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Status default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) Applied Tax
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

# DPO5 - A/P Down Payment - Withholding Tax
Module: Marketing Documents | 158 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  SECONDERY U: AbsEntry, WTCode, BaseAbsEnt, Doc1LineNo
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator ->ODPO
  WTCode nVarChar(4) WT Code ->OWHT
  Rate Num(19,6) Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntSC Num(19,6) Taxable Amount in SC
  TxblAmntFC Num(19,6) Taxable Amount (FC)
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
  BaseNum Int(11) Base Document Type default=-1 [-1=, 0=, 22=Purchase orders, 20=Goods Receipt PO]
  LineNum Int(11) Line Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Abs. Entry default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=204 ->ADP1
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

# DPO6 - Down Payment Out - Installments
Module: Marketing Documents | 65 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, InstlmntID
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPO
  InstlmntID Int(6) Installment ID default=1
  ObjType nVarChar(20) Object Type default=204 ->ADP1
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

# DPO7 - Delivery Packages - A/P Down Pymt
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPO
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type default=204 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV

# DPO8 - Items in Package - A/P Down Pmt.
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum, ItemCode, UomEntry, NumPerMsr
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPO
  PackageNum Int(11) Package Number
  ItemCode nVarChar(50) Item Code ->OITM
  Quantity Num(19,6) Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=204 ->ADP1
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value default=0

# DPO9 - Down Payment Outgoing - Drawn Dpm
Module: Marketing Documents | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPO
  LineNum Int(11) Row Number
  BaseAbs Int(11) Base Document Internal ID
  BaseLine Int(11) Base Document Row
  TargetBase VarChar(1) Target or Base Document default=B [B=Base, T=Target]
  ObjType nVarChar(20) Base Object Type
  DrawnSum Num(19,6) Net LC
  DrawnSumFc Num(19,6) Net FC
  DrawnSumSc Num(19,6) Net SC
  LogInstanc Int(11) Log Instance default=0
  ObjCode nVarChar(20) Object Type default=204 ->ADP1
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

# DRF1 - Draft - Rows
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
  DocEntry Int(11) Document Internal ID ->ODRF
  LineNum Int(11) Row Number
  TargetType Int(11) Target Document Type default=-1
  TrgetEntry Int(11) Target Document Internal ID
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=-1 [-1=, 15=Delivery, 16=Returns, 203=A/R Down Payment, 13=A/R Invoice, 14=A/R Credit Memo, 132=Correction Invoice, 20=Goods Receipt PO, 21=Goods Return, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 17=Sales Order, 22=Purchase Order, 23=Sales Quotation, 67=Inventory Transfers, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 165=A/R Correction Invoice, 166=A/R Correction Invoice Reversal, 540000006=Purchase Quotation, 59=Goods Receipt, 1250000001=Inventory Transfers Request, 1470000113=Purchase Request, 0=, 60=Goods Issue, 234000031=A/R Return Request, 234000032=A/P Return Request, 202=Production Order]
  BaseEntry Int(11) Base Document Internal ID
  BaseLine Int(11) Base Row
  LineStatus VarChar(1) Row Status [O=Open, C=Closed]
  ItemCode nVarChar(50) Item No. ->OITM
  Dscription nVarChar(200) Item/Service Description
  Quantity Num(19,6) Quantity
  ShipDate Date(8) Delivery Date per Row
  OpenQty Num(19,6) Remaining Open Quantity
  Price Num(19,6) Price
  Currency nVarChar(3) Price Currency ->OCRN
  Rate Num(19,6) Currency Rate
  DiscPrcnt Num(19,6) Discount % per Row
  LineTotal Num(19,6) Row Total
  TotalFrgn Num(19,6) Row Total (FC)
  OpenSum Num(19,6) Open Amount
  OpenSumFC Num(19,6) Open Amount (FC)
  VendorNum nVarChar(50) Vendor Catalog Number
  SerialNum nVarChar(17) Serial Number
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  SlpCode Int(11) Sales Employee Code ->OSLP
  Commission Num(19,6) Commission Percentage
  TreeType VarChar(1) BOM Type default=N [N=Not a BOM, A=Assembly, S=Sales, I=Sales BOM Component, P=Production, T=Template]
  AcctCode nVarChar(15) Account Code ->OACT
  TaxStatus VarChar(1) Tax Definition [Y=Yes, N=No]
  GrossBuyPr Num(19,6) Gross Profit Base Price
  PriceBefDi Num(19,6) Unit Price
  DocDate Date(8) Posting Date
  Flags Int(11) Flags
  OpenCreQty Num(19,6) Credit Memo Amount
  UseBaseUn VarChar(1) Inventory UoM default=N [Y=Yes, N=No]
  SubCatNum nVarChar(50) BP Catalog No. ->OSCN
  BaseCard nVarChar(15) Base BP Code ->OCRD
  TotalSumSy Num(19,6) Row Total (FC)
  OpenSumSys Num(19,6) Open Amount (SC)
  InvntSttus VarChar(1) Warehouse Status [O=Open, C=Closed]
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  CodeBars nVarChar(254) Bar Code
  VatPrcnt Num(19,6) Tax Rate per Row
  VatGroup nVarChar(8) Tax Definition ->OVTG
  PriceAfVAT Num(19,6) Gross Price after Discount
  Height1 Num(19,6) Height 1
  Hght1Unit Int(6) Height 1 UoM
  Height2 Num(19,6) Height 2
  Hght2Unit Int(6) Height 2 UoM
  Width1 Num(19,6) Width 1
  Wdth1Unit Int(6) UoM for Width 1
  Width2 Num(19,6) Width 2
  Wdth2Unit Int(6) UoM for Width 2
  Length1 Num(19,6) Length 1
  Len1Unit Int(6) Length 1 UoM
  length2 Num(19,6) Length 2
  Len2Unit Int(6) Length 2 UoM
  Volume Num(19,6) Quantity
  VolUnit Int(6) Vol. Unit
  Weight1 Num(19,6) Weight 1
  Wght1Unit Int(6) UoM for Weight 1
  Weight2 Num(19,6) Weight 2
  Wght2Unit Int(6) UoM for Weight 2
  Factor1 Num(19,6) Factor 1
  Factor2 Num(19,6) Factor 2
  Factor3 Num(19,6) Factor 3
  Factor4 Num(19,6) Factor 4
  PackQty Num(19,6) No. of Packages
  UpdInvntry VarChar(1) Warehouse Update [Y=Yes, N=No]
  BaseDocNum Int(11) Base Document No.
  BaseAtCard nVarChar(100) BP Reference No. From
  SWW nVarChar(16) Additional Identifier
  VatSum Num(19,6) Total Tax
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  FinncPriod Int(11) Posting Period ->OFPR
  ObjType nVarChar(20) Object Type default=112 ->ADP1
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
  PoTrgNum Int(11) Target PO No.
  PoTrgEntry nVarChar(11) Target PO Entry
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
  LineType VarChar(1) Row Type default=R [R=Regular, A=Alternative, M=Resource]
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
  ItemType Int(11) Item Type default=4 [4=Item, 290=Resource]
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

# DRF10 - Draft - Row Structure
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SECONDARY U: DocEntry, AftLineNum, OrderNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODRF
  LineSeq Int(11) Row Sequence
  AftLineNum Int(11) After Row Number
  OrderNum Int(11) Order Number
  LineType VarChar(1) Row Type [T=Text, S=Subtotal]
  LineText Text(16) Row Text
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=112 ->ADP1

# DRF11 - Draft - Drawn Dpm Detail
Module: Marketing Documents | 70 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LineSeq
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODRF
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
  ObjType nVarChar(20) Object Type default=112 ->ADP1
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

# DRF12 - Draft - Tax Extension
Module: Marketing Documents | 117 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODRF
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
  ObjectType nVarChar(20) Object Type default=112 ->ADP1
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

# DRF13 - Draft Rows - Distributed Expenses
Module: Marketing Documents | 59 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODRF
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=112 ->ADP1
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

# DRF14 - Draft - Assembly - Rows
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODRF
  LineNum Int(11) Row Number default=-1
  ChildNum Int(11) Child Number default=-1
  ItemCode nVarChar(50) Item no. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  TotalQty Num(19,6) Total Quantity
  OpenQty Num(19,6) Remaining Open Quantity
  ObjectType nVarChar(20) object type ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BaseChildN Int(11) Base Child Number default=-1
  EncryptIV nVarChar(100) Encrypt IV

# DRF15 - Draft - Drawn Dpm Applied
Module: Marketing Documents | 84 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODRF
  LineNum Int(11) Row Number
  ObjType nVarChar(20) Object Type default=112 ->ADP1
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

# DRF16 - Draft - SnB - Rows
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, SnBIndex
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) abs entry ->ODRF
  LineNum Int(11) Line Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object id
  ObjAbs Int(11) Object Abs
  DrfWObjAbs Int(11) draft Wobj Abs default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance

# DRF17 - Draft - Import Process
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODRF
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=112 ->ADP1
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

# DRF18 - Draft - Export Process
Module: Marketing Documents | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODRF
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=112 ->ADP1
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

# DRF19 - Draft - Bin Allocation Data
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, BinAllocSe
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->ODRF
  BinAllocSe Int(11) Bin Allocation Sequence
  LineNum Int(11) Line Number
  SubLineNum Int(11) Subline Number default=-1
  SnBType Int(11) SnB Type default=-1
  SnBMDAbs Int(11) SnB Master Data Internal No. default=-1
  BinAbs Int(11) Bin Internal Number ->OBIN
  Quantity Num(19,6) Quantity
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjType nVarChar(20) Object Type default=112 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  BinActTyp Int(6) Bin Action Type [1=Transaction In, 2=Transaction Out, 4=SnB Complete, 8=Bin First Then SnB]

# DRF2 - Draft - Freight - Rows
Module: Marketing Documents | 64 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODRF
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=112 ->ADP1
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

# DRF20 - Intrastat Expenses
Module: Marketing Documents | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODRF
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
  BaseType Int(11) Base Document Type default=-1 [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 16=Return, 13=A/R Invoice, 203=Down Payment Incoming, 204=Down Payment Outgoing, 22=Purchase Order, 20=Goods Receipt PO, 21=Goods Return, 18=A/P Invoice, 540000006=Purchase Quotation, 1470000113=Purchase Request, 0=, -1=]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No. default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=112 ->ADP1
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  AppliedLC Num(19,6) Applied
  AppliedFC Num(19,6) Applied (FC)
  AppliedSC Num(19,6) Applied (SC)

# DRF21 - Draft - Document Reference Information
Module: Marketing Documents | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, RefType
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjectType nVarChar(20) Object Type default=112
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

# DRF22 - Draft - Resource Costs
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, StdCostNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->DRF1
  LineNum Int(11) Row Number ->DRF1
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=112
  LogInstanc Int(11) Log Instance default=0

# DRF23 - A/P Invoice - Selected Asset Master Data
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, VisOrder
  ASSETS: DocEntry, LineNum, AssetCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODRF
  LineNum Int(11) Row Number
  AssetCode nVarChar(50) Selected Asset Code ->OITM
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Remarks nVarChar(100) Remarks
  Amount Num(19,6) Amount
  AmountSC Num(19,6) Amount (SC)
  SerialNo nVarChar(30) Serial Number
  VisOrder Int(11) Visual Order
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=112 ->ADP1

# DRF24 - Draft - Tracking Note Assignment
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
  ObjType nVarChar(20) Object Type default=112 ->ADP1
  SubLineNum Int(11) BOM Line No.

# DRF25 - Draft - Amt Per VAT Grp
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
  ObjType nVarChar(20) Object Type default=112 ->ADP1

# DRF26 - Draft - E-Way Bill Information
Module: Marketing Documents | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODRF
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
  ObjectType nVarChar(20) Object Type default=112 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TspEntry Int(11) Transporter Abs. Entry ->OTSP
  TspLine Int(11) Transportation Line
  TransType Int(11) Transaction Type [1=Regular, 2=Bill To-Ship To, 3=Bill From-Dispatch From, 4=Combination of 2 and 3]

# DRF27 - Draft - E-Books(GR) Rows
Module: Marketing Documents | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  RELATE_ROW: DocEntry, RelateType, RelateLine, GroupNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODRF
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

# DRF28 - Draft - Reported Tracking Note
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
  ObjType nVarChar(20) Object Type default=112 ->ADP1
  SubLineNum Int(11) BOM Line No.

# DRF3 - Draft - Freight
Module: Marketing Documents | 80 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  DOCUMENT: DocEntry, BaseAbsEnt
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODRF
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  Comments nVarChar(100) Remarks
  ObjType nVarChar(20) Object Type default=112 ->ADP1
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
  BaseType Int(11) Base Document Type [23=Sales Quotation, 17=Sales Order, 15=Delivery notes, 16=Return, 13=A/R Invoice, 203=Down Payment Incoming, 204=Down Payment Outgoing, 22=Purchase order, 20=Good Receipt PO, 21=Goods Return, 18=A/P Invoice, 540000006=Purchase Quotation, 1470000113=Purchase Request, 0=, -1=]
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

# DRF4 - Draft Documents - Tax
Module: Marketing Documents | 61 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SCONDARY: DocEntry, LineNum, GroupNum, ExpnsCode, StcCode, StaCode, staType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODRF
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
  ObjectType nVarChar(20) Object Type default=13 ->ADP1
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

# DRF5 - Draft Documents - Withholding Tax
Module: Marketing Documents | 158 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  SECONDERY U: AbsEntry, WTCode, BaseAbsEnt, Doc1LineNo
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator ->ODRF
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
  BaseNum Int(11) Base Document Type [23=Sales Quotation, 17=Sales Order, 15=Delivery notes, 16=Return, 13=A/R Invoice, 14=A/R Credit Memo, 203=Down Payment Incoming, 204=Down Payment Outgoing, 22=Purchase order, 20=Good Receipt PO, 21=Goods Return, 18=A/P Invoice, 19=A/P Credit Memo, 59=Goods Receipt (inv), 60=Goods Issue (inv), 67=Warehouse Transfer, 540000006=Purchase Quotation, 0=, -1=]
  LineNum Int(11) Line Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Abs. Entry default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=112 ->ADP1
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

# DRF6 - Document Drafts - Installments
Module: Marketing Documents | 65 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, InstlmntID
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODRF
  InstlmntID Int(6) Installment ID default=1
  ObjType nVarChar(20) Object Type default=112 ->ADP1
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

# DRF7 - Delivery Packages - Drafts
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODRF
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type default=112 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV

# DRF8 - Items in Package - Draft
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum, ItemCode, UomEntry, NumPerMsr
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODRF
  PackageNum Int(11) Package Number
  ItemCode nVarChar(50) Item Code ->OITM
  Quantity Num(19,6) Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=112 ->ADP1
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value default=0

# DRF9 - Document Draft - Drawn Dpm
Module: Marketing Documents | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODRF
  LineNum Int(11) Row Number
  BaseAbs Int(11) Base Document Internal ID
  BaseLine Int(11) Base Document Row
  TargetBase VarChar(1) Target or Base Document default=B [B=Base, T=Target]
  ObjType nVarChar(20) Base Object Type
  DrawnSum Num(19,6) Net LC
  DrawnSumFc Num(19,6) Net FC
  DrawnSumSc Num(19,6) Net SC
  LogInstanc Int(11) Log Instance default=0
  ObjCode nVarChar(20) Object Type default=112 ->ADP1
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

# DUT1 - Dunning Term Array1
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TermCode, LevelNum
Fields (name type(len) description [values] ->parent table):
  TermCode nVarChar(25) Dunning Term Code ->ODUT
  LevelNum Int(11) Level No.
  LetterFrmt nVarChar(8) Letter Format
  EffctAftr nVarChar(3) Effective after
  LetterFee Num(19,6) Fee per Letter
  FeeCurr nVarChar(3) Fee Currency
  MinBalance Num(19,6) Mininum Balance
  MinBlnCurr nVarChar(3) Min Balance Currency
  CalcIntrst VarChar(1) Calc. Interest default=Y [Y=Yes, N=No]

# DWZ1 - Dunning Wizard Array1 - BP Filter
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WizardId, CardCode
Fields (name type(len) description [values] ->parent table):
  WizardId Int(11) Wizard ID ->ODWZ
  CardCode nVarChar(15) BP Card Code ->OCRD
  DunAddr nVarChar(254) Dunning Address
  CheckedBP VarChar(1) Checked BP default=Y [Y=Yes, N=No]
  FaxNum nVarChar(50) Fax Number
  Email nVarChar(100) E-Mail Address
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]

# DWZ2 - Dunning Wizard Array 2-Invoice Filter
Module: Marketing Documents | 43 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WizardId, LetterNum, DocAbs, InstlmntID, DocType
Fields (name type(len) description [values] ->parent table):
  WizardId Int(11) Wizard ID ->ODWZ
  CardCode nVarChar(15) BP Card Code ->OCRD
  LetterNum Int(11) Letter Number
  TotalFee Num(19,6) Total Fee
  FeeCurr nVarChar(3) Total Fee Currency ->OCRN
  TtlopnIntr Num(19,6) Sum of Open Sum+Interest
  EDunLevel nVarChar(3) Edited Dunning Level
  OpnIntrCrr nVarChar(3) Total Open + Interest Currency
  DocAbs Int(11) Document Internal Number
  DocNum Int(11) Doc. No.
  InstlmntID Int(6) Installment ID
  IntrstPC Num(19,6) Interest Percent
  IntrstAmnt Num(19,6) Interest Amount
  IntrstCurr nVarChar(3) Interest Currency ->OCRN
  ChckLine VarChar(1) Checked Row default=N [Y=Yes, N=No]
  IntrstDays Int(11) Interest Days
  DocType Int(11) Source Table [13=A/R Invoice, 203=Down Payment Incoming, 165=Correction A/R Invoice, 14=A/R Credit Memo, 24=Incoming Payment, 30=Journal Transactions, -2=Open Balance, -3=Close Balance, 46=Outgoing Payments]
  DueDate Date(8) Due Date
  LetterLvl nVarChar(3) Letter Level default=0
  OpenSum Num(19,6) Open Sum
  OpenCurr nVarChar(3) Open Sum Currency
  sumIntrClc Num(19,6) Sum for Interest Calculation
  folioNum nVarChar(14) Folio Number
  LvlUpdated VarChar(1) Level Updated Flag default=N [Y=Yes, N=No]
  TotalFeeFC Num(19,6) Total Fee in Document Currency
  TotalFeeLC Num(19,6) Total Fee in Local Currency
  TotalFeeSC Num(19,6) Total Fee in System Currency
  TtlopnInFC Num(19,6) Sum of Open Sum+Interest FC
  TtlopnInSC Num(19,6) Sum of Open Sum+Interest SC
  IntrAmtFC Num(19,6) Interest Amount (FC)
  IntrAmtSC Num(19,6) Interest Amount (SC)
  OpenSumFC Num(19,6) Open Sum (FC)
  OpenSumSC Num(19,6) Open Sum (SC)
  ExeChkLine VarChar(1) Executed Checked Row default=N [Y=Yes, N=No]
  AutoPost VarChar(1) Automatic Posting default=N [N=No, B=Interest and Fee, I=Interest Only, F=Fee Only]
  DocRate Num(19,6) Document Rate
  UnpaidBoEV Num(19,6) Unpaid BoE Value
  BoENumber Int(11) BoE Number
  BoEStatus VarChar(1) BoE Status
  BoEDate Date(8) BoE Date
  BoEKey Int(11) BoE Key
  BPType VarChar(1) Business Partner Type default=C [C=Customer, S=Vendor]
  BPLId Int(11) Assigned Branch ->OBPL

# DWZ3 - Dunning Wizard Array 3 - Recommended Service Invoice
Module: Marketing Documents | 22 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WizardId, CardCode, LetterNum
Fields (name type(len) description [values] ->parent table):
  WizardId Int(11) Wizard ID
  CardCode nVarChar(15) BP Card Code
  LetterNum Int(11) Letter Number
  AddChecked VarChar(1) Add Checked default=Y
  DocAbs Int(11) Internal Document Number
  IntrAmt Num(19,6) Interest Amount (LC)
  IntrAmtFC Num(19,6) Interest Amount (FC)
  IntrAmtSC Num(19,6) Interest Amount (SC)
  FeeAmt Num(19,6) Fee Amount (LC)
  FeeAmtFC Num(19,6) Fee Amount (FC)
  FeeAmtSC Num(19,6) Fee Amount (SC)
  InVatGroup nVarChar(8) Interest VAT Group
  InTaxCode nVarChar(8) Interest Tax Code
  FeVatGroup nVarChar(8) Fee VAT Group
  FeTaxCode nVarChar(8) Fee Tax Code
  VatPrcnt Num(19,6) VAT Percent
  Executed VarChar(1) Executed default=N [Y=Yes, N=No]
  Message nVarChar(254) Message
  DocCur nVarChar(3) Document Currency ->OCRN
  DocNum Int(11) Document Number
  BPLId Int(11) BPL ID Assigned to Invoice
  LocCode Int(11) Location Code

# DWZ4 - Dunning Wizard Array 4-Paging Grid
Module: Marketing Documents | 51 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WizardId, RowId
Fields (name type(len) description [values] ->parent table):
  WizardId Int(11) Wizard ID ->ODWZ
  CheckLine VarChar(1) Checked Row default=Y
  ExeChkLine VarChar(1) Executed Checked Row default=Y
  RowId Int(11) Row Num
  CardCode nVarChar(15) BP Card Code ->OCRD
  LetterNum Int(11) Letter Number
  DunnLevel Int(11) Dunning Level
  CardName nVarChar(100) BP Name
  DocCur nVarChar(3) Doc. Currency
  DocType Int(11) Source Table [13=A/R Invoice, 203=Down Payment Incoming, 165=Correction A/R Invoice, 14=A/R Credit Memo, 24=Incoming Payment, 30=Journal Transactions, -2=Open Balance, -3=Close Balance]
  DocNum Int(11) Doc. No.
  InstlmntID Int(6) Installment ID
  DueDate Date(8) Due Date
  LastLvlDte Date(8) Last Update Date
  LastDunDte Date(8) Last Dunning Date
  NewLvlDate Date(8) New Level Update Date
  DocAmntLC nVarChar(100) DOC. AMOUNT (LC)
  DocAmntFC nVarChar(100) DOC. AMOUNT (FC)
  OpenAmtLC nVarChar(100) Open Amount (LC)
  OpenAmtFC nVarChar(100) Open Amount (FC)
  IntrstDays Int(11) Interest Days
  IntrstPC Num(19,6) Interest Percent
  IntAmntLC nVarChar(100) Interest Amount (LC)
  IntAmntFC nVarChar(100) Interest Amount (FC)
  InclAmntLC nVarChar(100) Total Incl. Amount (LC)
  InclAmntFC nVarChar(100) Total Incl. Amount (FC)
  FeeLC nVarChar(100) Fee (LC)
  FeeFC nVarChar(100) Fee (FC)
  AllTotalLC nVarChar(100) Overall Total (LC)
  AllTotalFC nVarChar(100) Overall Total (FC)
  AutoPost VarChar(1) Automatic Posting default=N [N=No, B=Interest and Fee, I=Interest Only, F=Fee Only]
  LineProp Int(11) Line Property
  YearDays Int(11) Year Days
  YearlyRate Num(19,6) Yearly Rate
  LetterFrmt nVarChar(8) Letter Formant
  MinBlan Num(19,6) Min. Balance
  GrpMethod VarChar(1) Group Method
  DocEntry Int(11) DocEntry
  DocRate nVarChar(100) Exchange Rate on Document
  FeeCurr nVarChar(3) Fee Currency
  OrigFee Num(19,6) Original Fee on Dunning Term
  MinBalCurr nVarChar(3) Minimum Balance Currency
  LvlUpdated nVarChar(3) Level Updated
  DunAddr nVarChar(254) Dunning Address
  DocText nVarChar(254) Doc. Text
  ParentId Int(11) Parent Id
  BpCode2 nVarChar(15) BP Code 2
  BpType VarChar(1) BP Type
  CardName2 nVarChar(100) Card Name 2
  Comment nVarChar(254) Comment
  BPLId Int(11) Branch ID

# DWZ5 - Dunning Wizard Array 5-Selected Branches
Module: Marketing Documents | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WizardId, BPLId
Fields (name type(len) description [values] ->parent table):
  WizardId Int(11) Wizard ID ->ODWZ
  BPLId Int(11) Assigned Branch ->OBPL

# GPA1 - Gross Profit Adjustment - Documents
Module: Marketing Documents | 54 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineId
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OGPA
  LineId Int(11) Row No.
  ItemCode nVarChar(50) Item No. ->OITM
  ItemName nVarChar(200) Item Description
  DocType nVarChar(20) Document Type
  DocNum Int(11) Document Number
  DocAbs Int(11) Document Abs. Entry
  DocLineNum Int(11) Document Line Number
  ManagedBy Int(11) Managed By default=-1 [10000044=Batch Numbers, 10000045=Serial Numbers, -1=]
  Selected VarChar(1) Choose default=Y [Y=Yes, N=No]
  DistNumber nVarChar(36) Batch Number
  PostDate Date(8) Posting Date
  WhsCode nVarChar(8) Warehouse Code
  Quantity Num(19,6) Quantity
  CogsAcct nVarChar(15) COGS Account Code
  CogsAmnt Num(19,6) COGS Amount
  SalesAmnt Num(19,6) Sales Amount
  GrssProfit Num(19,6) Row Gross Profit
  COGSByCC Num(19,6) COGS By Current Cost
  GPByCC Num(19,6) Gross Profit By Current Cost
  DeltaGP Num(19,6) Delta Gross Profit
  SalesPrice Num(19,6) Sales Price
  BatchQt Num(19,6) Batch Quantity
  SnBAbs Int(11) SnB Abs. Entry
  AccTotal Num(19,6) Acct Total
  AccQty Num(19,6) Acct Qty
  ActionType Int(11) Action Type default=5 [0=TRANSACTION_UNKNOWN, 1=TRANSACTION_IN, 2=TRANSACTION_OUT, 3=TRANSACTION_SET, 4=TRANSACTION_COMPLETE, 5=EMPTY_TRANSACTION, 6=TRANSACTION_REVALUATION, 7=TRANSACTION_REVALUATION_INCREASE, 8=TRANSACTION_REVALUATION_DECREASE, 9=TRANSACTION_CLOSE_IN, 10=TRANSACTION_CLOSE_OUT, 11=TRANSACTION_NEGATIVE_REVALUATION, 12=TRANSACTION_NULLIFY, 13=TRANSACTION_RESERVE_CI_IN, 14=TRANSACTION_RESERVE_CI_OUT, 15=TRANSACTION_RESERVE_CI_REVAL_INC, 16=TRANSACTION_RESERVE_CI_REVAL_DEC, 17=TRANSACTION_REVAL_PRICE_CHANGE_INCREASE, 18=TRANSACTION_REVAL_PRICE_CHANGE_DECREASE]
  SBAccTotal Num(19,6) SnB Acct Total
  SBAccQty Num(19,6) SnB Acct Qty
  BaseType nVarChar(20) Base Type
  Execute VarChar(1) Execute default=Y [Y=Yes, N=No]
  SBCogsAmnt Num(19,6) SnB COGS Amount
  SBSaleAmnt Num(19,6) SnB Sales Amount
  SBGrssProf Num(19,6) SnB Gross Profit
  SBGrPrPerc Num(19,6) SnB Gross Profit Percentage
  GrPrPerc Num(19,6) Gross Profit Percentage
  GPPercByCC Num(19,6) Gross Profit Percentage By Current Cost
  DeltaGPLn Num(19,6) Delta gross profit calculated for the document line
  Applied Num(19,6) Applied Adjustment
  SBAccTtAdj Num(19,6) SnB Acct Total Adjustment
  IsMixed VarChar(1) Is Mixed Based Document default=N [Y=Yes, N=No]
  CogsAmByCC Num(19,6) Total COGS Amount By Current Cost
  GrssPrByCC Num(19,6) Total Gross Profit By Current Cost
  LineType VarChar(1) Wizard Line Type default=N [N=Normal, C=Chained, I=Non Based Correction Invoice]
  ChDocType nVarChar(20) Chained Document Type
  ChDocAbs Int(11) Chained Document Abs. Entry
  WasQty Num(19,6) Was Line Quantity
  WasCogs Num(19,6) Was Line COGS Amount
  WasSales Num(19,6) Was Line Sales Amount
  WasPrice Num(19,6) Was Line Sales Price
  WasGrProf Num(19,6) Was Line Gross Profit
  BaseAbs Int(11) Base Document Abs Entry
  WasNewCogs Num(19,6) Was Line New Cogs
  ChDocLine Int(11) Chained Document Line

# GPA2 - Gross Profit Adjustments - Parameters
Module: Marketing Documents | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  Name nVarChar(100) Wizard Parameters Name
  Descript nVarChar(100) Wizard Parameters Description
  PostDateFr Date(8) Sales Doc. Posting Date From
  PostDateTo Date(8) Sales Doc. Posting Date To
  ItemCodeFr nVarChar(50) Item No. From
  ItemCodeTo nVarChar(50) Item No. To
  ItmsGrpCod Int(6) Item Group default=100 ->OITB
  AdditFilt VarChar(1) Additional Filters
  SearchCond VarChar(1) Find Items Search Condition
  PropList nVarChar(100) Item Properties List
  DisplInact VarChar(1) Display Inactive Items
  UseGroups VarChar(1) Find items with only the selected properties

# GPA3 - Gross Profit Adjustment - JE Details
Module: Marketing Documents | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OGPA
  PostDate Date(8) Posting Date
  DocDate Date(8) Document Date
  DueDate Date(8) Due Date
  Series Int(11) Series default=0
  JERemarks nVarChar(254) Journal Remarks
  TransCode nVarChar(4) Transaction Code
  Ref1 nVarChar(100) Reference 1
  Ref2 nVarChar(100) Reference 2
  JERef nVarChar(11) Journal Entry Reference

# GPA4 - Gross Profit Adjustment - JE Details Accounts
Module: Marketing Documents | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineId
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OGPA
  LineId Int(11) Row No.
  LineType VarChar(1) Line Type default=T [T=Total, A=Account]
  CurrCogs Num(19,6) Current COGS
  CalcCogs Num(19,6) Calculated COGS
  CogsDebit Num(19,6) COGS Debit
  CogsCredit Num(19,6) COGS Credit
  CogsAcct nVarChar(15) COGS Account
  PrDiffAcct nVarChar(15) Price Difference Account
  AutoPost VarChar(1) Automatic Posting default=Y [Y=Yes, N=No]

# GPA5 - Product Cost Adjustment - Recalculation of Product Cost
Module: Marketing Documents | 31 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineId
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OGPA
  LineId Int(11) Row No.
  Selected VarChar(1) Choose default=Y [Y=Yes, N=No]
  LnType VarChar(1) Choose default=O [P=Product Serial/Batch Line, O=Production Order Line]
  ProdCode nVarChar(50) Product Code
  ProdDescr nVarChar(200) Product Description
  PODocAbs Int(11) PO Document Abs. Entry
  PODocNum Int(11) PO Document Number
  DocType VarChar(1) Choose default=I [I=Issue for Production, R=Receipt from Production]
  DocAbs Int(11) Document Abs. Entry
  DocNum Int(11) Document Number
  DocLineNum Int(11) Document Line Number
  PostDate Date(8) Posting Date
  ItemCode nVarChar(50) Item No.
  ItemDescr nVarChar(200) Item Description
  DistNumber nVarChar(36) Batch Number
  SnBAbs Int(11) SnB Abs. Entry
  ManagedBy Int(11) Managed By default=-1 [10000044=Batch Numbers, 10000045=Serial Numbers, -1=]
  LnQty Num(19,6) Line Quantity
  SnBQty Num(19,6) Serial/Batch Quantity
  LnCost Num(19,6) Line Cost
  DebCred VarChar(1) Debited or Credited default=D [D=Debited, C=Credited]
  LnTotal Num(19,6) Line Total
  SnBTotal Num(19,6) SnB Total
  SBAccTotal Num(19,6) Serial/Batch Accumulated Total
  SBAccQty Num(19,6) Serial/Batch Accumulated Quantity
  ACAccTotal Num(19,6) Actual Cost Accumulated Total
  ACAccQty Num(19,6) Actual Cost Accumulated Quantity
  Applied Num(19,6) Applied Adjustment
  Variance Num(19,6) Variance to Apply
  MRVAdjust Num(19,6) MRV Adjustment

# GPA6 - Product Cost Adjustment - Applied Material Revaluations
Module: Marketing Documents | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineId
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OGPA
  LineId Int(11) Row No.
  PODocAbs Int(11) PO Document Abs. Entry
  Applied Num(19,6) Applied Adjustment

# GPA7 - Product Cost Adjustment - Journal Entry Details
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OGPA
  PostDate Date(8) Posting Date
  DocDate Date(8) Document Date
  Series Int(11) Series default=0
  Ref2 nVarChar(100) Reference 2
  JERemarks nVarChar(254) Journal Remarks
  MRVRef nVarChar(11) MRV Entry Reference

# GPA8 - Product Cost Adjustment - MRV Document Lines
Module: Marketing Documents | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineId
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OGPA
  LineId Int(11) Row No.
  ProdCode nVarChar(20) Product Code
  ProdDescr nVarChar(200) Product Description
  DistNumber nVarChar(36) Batch Number
  SnBAbs Int(11) SnB Abs. Entry
  ManagedBy Int(11) Managed By default=-1 [10000044=Batch Numbers, 10000045=Serial Numbers, -1=]
  IncrAcct nVarChar(15) G/L Increase Account
  DecrAcct nVarChar(15) G/L Decrease Account
  DebCredAmt Num(19,6) Debit/Credit Amount

# GPA9 - Applied Gross Profit Adjustments
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineId
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OGPA
  LineId Int(11) Row No.
  DocAbs Int(11) Document Abs. Entry
  DocType nVarChar(20) Document Type
  DocLineNum Int(11) Document Line Number
  SnBAbs Int(11) SnB Abs. Entry
  ManagedBy Int(11) Managed By default=-1 [10000044=Batch Numbers, 10000045=Serial Numbers, -1=]
  Applied Num(19,6) Applied Adjustment

# GTI1 - GTS Invoice Details
Module: Marketing Documents | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OGTI
  LineNum Int(11) Line Number
  DisctLine VarChar(1) Discount Flag default=0 [0=Normal, 1=Discount Line]
  ItemName nVarChar(60) Item Name
  ItemSpec nVarChar(30) Item Specification
  Uom nVarChar(16) Unit of Measurement
  Quantity Num(19,6) Quantity
  NetAmount Num(19,6) Net Amount
  VatPercent Num(19,6) VAT Percent
  VatAmount Num(19,6) VAT Amount
  UnitPrice Num(19,6) Unit Price
  UnitPricTp VarChar(1) Unit Price Type default=0 [0=Net, 1=Gross]
  ItemTaxCat nVarChar(4) Item Tax Category

# GTM1 - GTS Mapping Object Details
Module: Marketing Documents | 17 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OGTM
  LineNum Int(11) Line Number
  ItemCode nVarChar(50) Item Code ->OITM
  ItemName nVarChar(200) Item Name
  ItemUoM nVarChar(100) Item UoM
  ItemSpec nVarChar(30) Item Spec.
  ItemTaxCat nVarChar(4) Item Tax Category
  Quantity Num(19,6) Quantity
  Amount Num(19,6) Amount
  VatPercent Num(19,6) VAT Percent
  DiscRate Num(19,6) Discount Rate
  DiscAmount Num(19,6) Discount Amount
  VatAmount Num(19,6) VAT Amount
  DiscVatAmt Num(19,6) Discount VAT Amount
  UnitPrice Num(19,6) Unit Price
  UPirceType VarChar(1) Unit Price Type default=0 [0=Net, 1=Gross]
  TaxCatCode nVarChar(50) Item Tax Category Code

# IEI1 - Incoming Excise Invoice - Rows
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
  DocEntry Int(11) Document Internal ID ->OIEI
  LineNum Int(11) Row Number
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=, 14=A/R Credit Note, 15=Delivery]
  TrgetEntry Int(11) Target Document Internal ID
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 16=A/R Returns, 140000009=Outgoing Excise Invoice, 20=Goods Receipt PO, 14=A/R Credit Memo, 15=Delivery, 21=Goods Return, 19=A/P Credit Memo]
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
  ObjType nVarChar(20) Object Type default=140000010 ->ADP1
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
  INMPrice Num(19,6) Item Cost
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
  TaxOnly VarChar(1) Tax Only default=N [Y=Yes, N=No]
  WtCalced VarChar(1) Withholding Tax Calculated default=N [N=No, Y=Yes]
  QtyToShip Num(19,6) Quantity to Ship
  DelivrdQty Num(19,6) Delivered Quantity
  OrderedQty Num(19,6) Ordered Quantity
  CogsOcrCod nVarChar(8) COGS Distribution Rule Code ->OOCR
  CiOppLineN Int(11) Line Number of Opposite Line default=-1
  CogsAcct nVarChar(15) COGS Account Code ->OACT
  ChgAsmBoMW VarChar(1) Change Whse for Asm BoM Child [Y=Yes, N=No]
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

# IEI10 - Incoming Excise Invoice - Row Structure
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SECONDERY U: DocEntry, AftLineNum, OrderNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIEI
  LineSeq Int(11) Row Sequence
  AftLineNum Int(11) After Row Number
  OrderNum Int(11) Order Number
  LineType VarChar(1) Row Type [T=Text, S=Subtotal]
  LineText Text(16) Row Text
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=140000010 ->ADP1

# IEI11 - IEI - Drawn Dpm Detail
Module: Marketing Documents | 70 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LineSeq
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIEI
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
  ObjType nVarChar(20) Object Type default=140000010 ->ADP1
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

# IEI12 - Incoming Excise Invoice - Tax Extension
Module: Marketing Documents | 117 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIEI
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
  Carrier nVarChar(15) Carrier Code
  QoP Int(11) Quantity of Packs
  PackDesc nVarChar(10) Pack Description
  Brand nVarChar(20) Brand
  NoSU Int(11) Number of Shipping Unit
  NetWeight Num(19,6) Net Weight
  GrsWeight Num(19,6) Gross Weight
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=140000010 ->ADP1
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

# IEI13 - Incoming Excise Invoice Rows - Distributed Expenses
Module: Marketing Documents | 59 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIEI
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=140000010 ->ADP1
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

# IEI14 - Incoming Excise Invoice - Assembly - Rows
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIEI
  LineNum Int(11) Row Number default=-1
  ChildNum Int(11) Child Number default=-1
  ItemCode nVarChar(50) Item no. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  TotalQty Num(19,6) Total Quantity
  OpenQty Num(19,6) Remaining Open Quantity
  ObjectType nVarChar(20) object type default=140000010 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BaseChildN Int(11) Base Child Number default=-1
  EncryptIV nVarChar(100) Encrypt IV

# IEI15 - IEI - Drawn Dpm Applied
Module: Marketing Documents | 84 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIEI
  LineNum Int(11) Row Number
  ObjType nVarChar(20) object type default=140000010 ->ADP1
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

# IEI16 - Incoming Excise Invoice - SnB properties
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, SnBIndex
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) abs entry ->OIEI
  LineNum Int(11) Line Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object id
  ObjAbs Int(11) Object Abs
  DrfWObjAbs Int(11) draft Wobj Abs default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type default=140000010
  LogInstanc Int(11) Log Instance

# IEI17 - Incoming Excise Invoice - Import Process
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIEI
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=140000010 ->ADP1
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

# IEI18 - Incoming Excise Invoice - Export Process
Module: Marketing Documents | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIEI
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=140000010 ->ADP1
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

# IEI19 - Incoming Excise Invoice - Bin Allocation Data
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, BinAllocSe
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OIEI
  BinAllocSe Int(11) Bin Allocation Sequence
  LineNum Int(11) Line Number
  SubLineNum Int(11) Subline Number default=-1
  SnBType Int(11) SnB Type default=-1
  SnBMDAbs Int(11) SnB Master Data Internal No. default=-1
  BinAbs Int(11) Bin Internal Number ->OBIN
  Quantity Num(19,6) Quantity
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjType nVarChar(20) Object Type default=140000010 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  BinActTyp Int(6) Bin Action Type [1=Transaction In, 2=Transaction Out, 4=SnB Complete, 8=Bin First Then SnB]

# IEI2 - Incoming Excise Invoice - Freight - History - Rows
Module: Marketing Documents | 64 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIEI
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=140000010 ->ADP1
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

# IEI20 - Intrastat Expenses
Module: Marketing Documents | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIEI
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
  ObjectType nVarChar(20) Object Type default=140000010 ->ADP1
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  AppliedLC Num(19,6) Applied
  AppliedFC Num(19,6) Applied (FC)
  AppliedSC Num(19,6) Applied (SC)

# IEI21 - Incoming Excise Invoice - Document Reference Information
Module: Marketing Documents | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, RefType
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjectType nVarChar(20) Object Type default=140000010
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

# IEI22 - Incoming Excise Invoice - Resource Costs
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, StdCostNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->IEI1
  LineNum Int(11) Row Number ->IEI1
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=140000010
  LogInstanc Int(11) Log Instance default=0

# IEI23 - A/P Invoice - Selected Asset Master Data
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, VisOrder
  ASSETS: DocEntry, LineNum, AssetCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIEI
  LineNum Int(11) Row Number
  AssetCode nVarChar(50) Selected Asset Code ->OITM
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Remarks nVarChar(100) Remarks
  Amount Num(19,6) Amount
  AmountSC Num(19,6) Amount (SC)
  SerialNo nVarChar(30) Serial Number
  VisOrder Int(11) Visual Order
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=140000010 ->ADP1

# IEI24 - Incoming Excise Invoice - Tracking Note Assignment
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
  ObjType nVarChar(20) Object Type default=140000010 ->ADP1
  SubLineNum Int(11) BOM Line No.

# IEI25 - Incoming Excise Invoice - Amt Per VAT Grp
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
  ObjType nVarChar(20) Object Type default=140000010 ->ADP1

# IEI26 - Incoming Excise Invoice - E-Way Bill Information
Module: Marketing Documents | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIEI
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
  ObjectType nVarChar(20) Object Type default=140000010 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TspEntry Int(11) Transporter Abs. Entry ->OTSP
  TspLine Int(11) Transportation Line
  TransType Int(11) Transaction Type [1=Regular, 2=Bill To-Ship To, 3=Bill From-Dispatch From, 4=Combination of 2 and 3]

# IEI27 - Incoming Excise Invoice - E-Books(GR) Rows
Module: Marketing Documents | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  RELATE_ROW: DocEntry, RelateType, RelateLine, GroupNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIEI
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

# IEI28 - Incoming Excise Invoice - Reported Tracking Note
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
  ObjType nVarChar(20) Object Type default=140000010 ->ADP1
  SubLineNum Int(11) BOM Line No.

# IEI3 - IEI - Freight
Module: Marketing Documents | 80 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  DOCUMENT: DocEntry, BaseAbsEnt
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIEI
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  Comments nVarChar(100) Remarks
  ObjType nVarChar(20) Object Type default=140000010 ->ADP1
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

# IEI4 - Incoming Excise Invoice - Tax Amount per Document
Module: Marketing Documents | 61 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SCONDARY: DocEntry, LineNum, GroupNum, ExpnsCode, StcCode, StaCode, staType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIEI
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
  ObjectType nVarChar(20) Object Type default=140000010 ->ADP1
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

# IEI5 - Incoming Excise Invoice - Withholding Tax
Module: Marketing Documents | 158 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  SECONDERY U: AbsEntry, WTCode, BaseAbsEnt, Doc1LineNo
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OIEI
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
  BaseNum Int(11) Base Document Type default=-1 [-1=, 0=]
  LineNum Int(11) Row Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Doc. Internal No. default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=140000010 ->ADP1
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

# IEI6 - IEI - Installments
Module: Marketing Documents | 65 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, InstlmntID
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIEI
  InstlmntID Int(6) Installment ID default=1
  ObjType nVarChar(20) Object Type default=140000010 ->ADP1
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

# IEI7 - Delivery Packages - Incoming Excise Invoice
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIEI
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type default=140000010 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV

# IEI8 - Incoming Excise Invoice - Items in Package
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum, ItemCode, UomEntry, NumPerMsr
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIEI
  PackageNum Int(11) Package Number
  ItemCode nVarChar(50) Item Code ->OITM
  Quantity Num(19,6) Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=140000010 ->ADP1
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value default=0

# IEI9 - IEI - Drawn Dpm
Module: Marketing Documents | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIEI
  LineNum Int(11) Row Number
  BaseAbs Int(11) Base Document Internal ID
  BaseLine Int(11) Base Document Row
  TargetBase VarChar(1) Target or Base Document default=T [B=Base, T=Target]
  ObjType nVarChar(20) Base Object Type default=203
  DrawnSum Num(19,6) Net LC
  DrawnSumFc Num(19,6) Net FC
  DrawnSumSc Num(19,6) Net SC
  LogInstanc Int(11) Log Instance default=0
  ObjCode nVarChar(20) Object Type default=140000010 ->ADP1
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

# IGE17 - Goods Issue - Import Process
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGE
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=60 ->ADP1
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

# IGE18 - Goods Issue - Export Process
Module: Marketing Documents | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGE
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=60 ->ADP1
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

# IGE20 - Intrastat Expenses
Module: Marketing Documents | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGE
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
  ObjectType nVarChar(20) Object Type default=60 ->ADP1
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  AppliedLC Num(19,6) Applied
  AppliedFC Num(19,6) Applied (FC)
  AppliedSC Num(19,6) Applied (SC)

# IGE22 - Goods Issue - Resource Costs
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, StdCostNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->IGE1
  LineNum Int(11) Row Number ->IGE1
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=60
  LogInstanc Int(11) Log Instance default=0

# IGE23 - A/P Invoice - Selected Asset Master Data
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, VisOrder
  ASSETS: DocEntry, LineNum, AssetCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGE
  LineNum Int(11) Row Number
  AssetCode nVarChar(50) Selected Asset Code ->OITM
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Remarks nVarChar(100) Remarks
  Amount Num(19,6) Amount
  AmountSC Num(19,6) Amount (SC)
  SerialNo nVarChar(30) Serial Number
  VisOrder Int(11) Visual Order
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=60 ->ADP1

# IGE24 - Goods Issue - Tracking Note Assignment
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
  ObjType nVarChar(20) Object Type default=60 ->ADP1
  SubLineNum Int(11) BOM Line No.

# IGE25 - Goods Issue - Amt Per VAT Grp
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
  ObjType nVarChar(20) Object Type default=60 ->ADP1

# IGE28 - Goods Issue - Reported Tracking Note
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
  ObjType nVarChar(20) Object Type default=60 ->ADP1
  SubLineNum Int(11) BOM Line No.

# IGN17 - Goods Receipt - Import Process
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGN
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=59 ->ADP1
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

# IGN18 - Goods Receipt - Export Process
Module: Marketing Documents | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGN
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=59 ->ADP1
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

# IGN20 - Intrastat Expenses
Module: Marketing Documents | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGN
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
  ObjectType nVarChar(20) Object Type default=59 ->ADP1
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  AppliedLC Num(19,6) Applied
  AppliedFC Num(19,6) Applied (FC)
  AppliedSC Num(19,6) Applied (SC)

# IGN22 - Goods Receipt - Resource Costs
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, StdCostNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->IGN1
  LineNum Int(11) Row Number ->IGN1
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=59
  LogInstanc Int(11) Log Instance default=0

# IGN23 - A/P Invoice - Selected Asset Master Data
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, VisOrder
  ASSETS: DocEntry, LineNum, AssetCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGN
  LineNum Int(11) Row Number
  AssetCode nVarChar(50) Selected Asset Code ->OITM
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Remarks nVarChar(100) Remarks
  Amount Num(19,6) Amount
  AmountSC Num(19,6) Amount (SC)
  SerialNo nVarChar(30) Serial Number
  VisOrder Int(11) Visual Order
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=59 ->ADP1

# IGN24 - Goods Receipt - Tracking Note Assignment
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
  ObjType nVarChar(20) Object Type default=59 ->ADP1
  SubLineNum Int(11) BOM Line No.

# IGN25 - Goods Receipt - Amt Per VAT Grp
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
  ObjType nVarChar(20) Object Type default=59 ->ADP1

# IGN28 - Goods Receipt - Reported Tracking Note
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
  ObjType nVarChar(20) Object Type default=59 ->ADP1
  SubLineNum Int(11) BOM Line No.

# INV1 - A/R Invoice - Rows
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
  DocEntry Int(11) Document Internal ID ->OINV
  LineNum Int(11) Row Number
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=, 14=A/R Credit Note, 15=Delivery, 165=A/R Correction Invoice, 234000031=A/R Return Request]
  TrgetEntry Int(11) Target Document Internal ID
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 23=Sales Quotation, 17=Sales Order, 15=Delivery, 13=Invoice, 67=Inventory Transfer]
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
  ObjType nVarChar(20) Object Type default=13 ->ADP1
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

# INV10 - A/R Invoice - Row Structure
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SECONDERY U: DocEntry, AftLineNum, OrderNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OINV
  LineSeq Int(11) Row Sequence
  AftLineNum Int(11) After Row Number
  OrderNum Int(11) Order Number
  LineType VarChar(1) Row Type [T=Text, S=Subtotal]
  LineText Text(16) Row Text
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=13 ->ADP1

# INV11 - A/R Invoice - Drawn Dpm Detail
Module: Marketing Documents | 70 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LineSeq
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OINV
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
  ObjType nVarChar(20) Object Type default=13 ->ADP1
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

# INV12 - A/R Invoice - Tax Extension
Module: Marketing Documents | 117 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OINV
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
  ObjectType nVarChar(20) Object Type default=13 ->ADP1
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

# INV13 - A/R Invoice Rows - Distributed Freights
Module: Marketing Documents | 59 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OINV
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=13 ->ADP1
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

# INV14 - A/R Invoice - Assembly - Rows
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OINV
  LineNum Int(11) Row Number default=-1
  ChildNum Int(11) Child Number default=-1
  ItemCode nVarChar(50) Item no. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  TotalQty Num(19,6) Total Quantity
  OpenQty Num(19,6) Remaining Open Quantity
  ObjectType nVarChar(20) object type default=13 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BaseChildN Int(11) Base Child Number default=-1
  EncryptIV nVarChar(100) Encrypt IV

# INV15 - A/R Inv. - Drawn Dpm Applied
Module: Marketing Documents | 84 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OINV
  LineNum Int(11) Row Number
  ObjType nVarChar(20) object type default=13 ->ADP1
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

# INV16 - A/R Invoice - SnB properties
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, SnBIndex
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) abs entry ->OINV
  LineNum Int(11) Line Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object id
  ObjAbs Int(11) Object Abs
  DrfWObjAbs Int(11) draft Wobj Abs default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type default=13
  LogInstanc Int(11) Log Instance

# INV17 - A/R Invoice - Import Process
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OINV
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=13 ->ADP1
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

# INV18 - A/R Invoice - Export Process
Module: Marketing Documents | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OINV
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=13 ->ADP1
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

# INV19 - A/R Invoice - Bin Allocation Data
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, BinAllocSe
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINV
  BinAllocSe Int(11) Bin Allocation Sequence
  LineNum Int(11) Line Number
  SubLineNum Int(11) Subline Number default=-1
  SnBType Int(11) SnB Type default=-1
  SnBMDAbs Int(11) SnB Master Data Internal No. default=-1
  BinAbs Int(11) Bin Internal Number ->OBIN
  Quantity Num(19,6) Quantity
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjType nVarChar(20) Object Type default=13 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  BinActTyp Int(6) Bin Action Type [1=Transaction In, 2=Transaction Out, 4=SnB Complete, 8=Bin First Then SnB]

# INV2 - A/R Invoice - Freight - Rows
Module: Marketing Documents | 64 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OINV
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=13 ->ADP1
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

# INV20 - Intrastat Expenses
Module: Marketing Documents | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OINV
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
  ObjectType nVarChar(20) Object Type default=13 ->ADP1
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  AppliedLC Num(19,6) Applied
  AppliedFC Num(19,6) Applied (FC)
  AppliedSC Num(19,6) Applied (SC)

# INV21 - A/R Invoice - Document Reference Information
Module: Marketing Documents | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, RefType
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjectType nVarChar(20) Object Type default=13
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

# INV22 - A/R Invoice - Resource Costs
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, StdCostNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->INV1
  LineNum Int(11) Row Number ->INV1
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=13
  LogInstanc Int(11) Log Instance default=0

# INV23 - A/P Invoice - Selected Asset Master Data
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, VisOrder
  ASSETS: DocEntry, LineNum, AssetCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OINV
  LineNum Int(11) Row Number
  AssetCode nVarChar(50) Selected Asset Code ->OITM
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Remarks nVarChar(100) Remarks
  Amount Num(19,6) Amount
  AmountSC Num(19,6) Amount (SC)
  SerialNo nVarChar(30) Serial Number
  VisOrder Int(11) Visual Order
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=13 ->ADP1

# INV24 - A/R Invoice - Tracking Note Assignment
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
  ObjType nVarChar(20) Object Type default=13 ->ADP1
  SubLineNum Int(11) BOM Line No.

# INV25 - A/R Invoice - Amt Per VAT Grp
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
  ObjType nVarChar(20) Object Type default=13 ->ADP1

# INV26 - A/R Invoice - E-Way Bill Information
Module: Marketing Documents | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OINV
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
  ObjectType nVarChar(20) Object Type default=13 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TspEntry Int(11) Transporter Abs. Entry ->OTSP
  TspLine Int(11) Transportation Line
  TransType Int(11) Transaction Type [1=Regular, 2=Bill To-Ship To, 3=Bill From-Dispatch From, 4=Combination of 2 and 3]

# INV27 - A/R Invoice - E-Books(GR) Rows
Module: Marketing Documents | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  RELATE_ROW: DocEntry, RelateType, RelateLine, GroupNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OINV
  LineNum Int(11) Row Number
  RelateType Int(11) Relation Type default=-1 [1=Row, 2=Row Expenses, 3=Document Expenses, -1=Manual]
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

# INV28 - A/R Invoice - Reported Tracking Note
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
  ObjType nVarChar(20) Object Type default=13 ->ADP1
  SubLineNum Int(11) BOM Line No.

# INV3 - A/R Invoice - Freight
Module: Marketing Documents | 80 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  DOCUMENT: DocEntry, BaseAbsEnt
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OINV
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  Comments nVarChar(100) Remarks
  ObjType nVarChar(20) Object Type default=13 ->ADP1
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

# INV4 - A/R Invoice - Tax Amount per Document
Module: Marketing Documents | 61 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SCONDARY: DocEntry, LineNum, GroupNum, ExpnsCode, StcCode, StaCode, staType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OINV
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
  ObjectType nVarChar(20) Object Type default=13 ->ADP1
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

# INV5 - A/R Invoice - Withholding Tax
Module: Marketing Documents | 158 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  SECONDERY U: AbsEntry, WTCode, BaseAbsEnt, Doc1LineNo
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OINV
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
