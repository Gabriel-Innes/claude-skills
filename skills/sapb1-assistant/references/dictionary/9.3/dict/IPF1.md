<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# IPF1 - Landed Costs - Rows
Module: Inventory and Production | 113 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
  BASE: OrigLine, BaseEntry
  ITEM: ItemCode, BaseEntry
  CURRENCY: Currency
  BASE_LINE: OrigLine, BaseEntry, BaseType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Landed Costs Internal ID ->OIPF
  LineNum Int(11) Row Number
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 20=Goods Receipt PO, 69=Landed Costs, 18=A/P Invoice]
  BaseEntry Int(11) Base Document Internal ID
  ItemCode nVarChar(50) Item No. ->OITM
  Dscription nVarChar(100) Item Description
  Quantity Num(19,6) Quantity
  PriceFOB Num(19,6) Base Doc. Price
  Currency nVarChar(3) Price Currency
  Rate Num(19,6) Currency Price
  Custom Num(19,6) Projected Customs
  CustomFC Num(19,6) Projected Customs (FC)
  Cost Num(19,6) Expenditure
  CostFC Num(19,6) Freight (FC)
  PriceAtWH Num(19,6) Whse Price
  PricAtWHFC Num(19,6) Whse Price (FC)
  LineTotal Num(19,6) Row Total
  TotalFrgn Num(19,6) Row Total (FC)
  Volume Num(19,6) Volume
  UnitCode Int(6) Volume UoM ->OLGT
  Weight1 Num(19,6) Weight 1
  UnitCode1 Int(6) Unit of Weight 1 ->OWGT
  Weight2 Num(19,6) Weight 2
  UnitCode2 Int(6) Unit of Weight 2 ->OWGT
  CardCode nVarChar(15) Vendor Code ->OCRD
  Reference nVarChar(16) Reference
  OrigLine Int(11) Base Line Number
  FactNoCust Num(19,6) Factor Without Customs
  FacWthCust Num(19,6) Factor with Customs
  PriceList Int(6) Price List No. ->OPLN
  CostOH VarChar(1) Cost Surcharge default=Y [Y=Yes, N=No]
  StockEval VarChar(1) Use for Inventory Valuation default=Y [Y=Yes, N=No]
  UseBaseUn VarChar(1) Inventory UoM [Y=Yes, N=No]
  BlockNum nVarChar(100) Block No.
  ImportLog nVarChar(20) Import Log
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  OrigRow Int(11) Original Row
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  OrigWhs nVarChar(8) Original Warehouse ->OWHS
  ReleaseNum Int(11) Release Number
  VarCosts Num(19,6) Variant Costs
  ConstCosts Num(19,6) Fixed Costs
  VarCostsFR Num(19,6) Variant Costs (FC)
  CnstCostFR Num(19,6) Fixed Costs (FC)
  UserCustom Num(19,6) User Expected Custom
  UsrCusomFC Num(19,6) User Expected Foreign Custom
  FobValue Num(19,6) Base Doc. Value Row Total (LC)
  FobValueFC Num(19,6) Base Doc. Value Row Total (FC)
  TtlExpndLC Num(19,6) Allocated Unit Costs Row Total
  TtlExpndFC Num(19,6) Allocated Unit Costs Row Total
  TtlCustLC Num(19,6) Allocated Unit Costs Row Total
  TtlCustFC Num(19,6) Allocated Unit Costs Row Total
  TtlCostLC Num(19,6) Row Ttl Cust + Alloc Costs LC
  TtlCostFC Num(19,6) Row Ttl Cust + Alloc Costs FC
  TtlVolume Num(19,6) Volume Row Total
  TtlWeight Num(19,6) Weight Row Total
  BaseRowNum Int(11) use IPF1_BASE_LINE_NUM instead
  TtlCustSC Num(19,6) Ttl Row Projected Customs (SC)
  TtlExpndSC Num(19,6) Allocated Costs Row Total (SC)
  OriBAbsEnt Int(11) Original Base Doc. Internal ID default=-1
  OriBLinNum Int(11) Original Base Doc. Row No. default=-1
  TargetDoc Int(11) Target Document Internal No.
  FobValCurr nVarChar(3) Base Doc. Value Currency
  FobnLaC Num(19,6) FOB and Included Costs (LC)
  FobnLaCFC Num(19,6) FOB and Included Costs (FC)
  NumPerMsr Num(19,6) UoM Value
  Project nVarChar(20) Project Code ->OPRJ
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  OriBDocTyp nVarChar(11) Original Base Document Type default=-1 [-1=, 18=A/P Invoice, 20=Goods Receipt PO]
  CustRate Num(19,6) Custom Group Rate
  LFixCost Num(19,6) Locked Fixed Cost
  LFixCostFC Num(19,6) Locked Fixed Cost (FC)
  LVarCost Num(19,6) Locked Variable Cost
  LVarCostFC Num(19,6) Locked Variable Cost (FC)
  CstmsRate Num(19,6) Customs Rate
  VatGroup nVarChar(8) VAT Code
  VatPrcnt Num(19,6) VAT Rate per Row
  VatSum Num(19,6) Total of VAT
  SnbType nVarChar(20) Batch or Serial Type default=-1 [-1=, 10000045=Serial, 10000044=Batch]
  SnbAbsEnt Int(11) SnB Abs. Entry default=-1
  SysNumber Int(11) System Number
  DistNumber nVarChar(36) Distinct Number
  ExciseSum Num(19,6) Sum of Excise
  ExcisSumFC Num(19,6) Sum of Excise - FC
  ExcInStk VarChar(1) Is Excise in Stock default=N [Y=Yes, N=No]
  CustomSum Num(19,6) Sum of Customs Cost
  CustSumFC Num(19,6) Sum of Customs Cost in FC
  CstmInStk VarChar(1) Is Customs in Stock default=Y [Y=Yes, N=No]
  CstmVatSum Num(19,6) Sum of Customs Cost VAT
  CstmVatFC Num(19,6) Sum of Customs Cost VAT in FC
  CstmVatStk VarChar(1) Is Customs VAT in Stock default=Y [Y=Yes, N=No]
  CCDEntry Int(11) CCD Abs. Entry
  CCDNumber nVarChar(20) Number of CCD
  ExcisSumSC Num(19,6) Sum of Excise - SC
  CustSumSC Num(19,6) Sum of Customs Cost in SC
  CstmVatSC Num(19,6) Sum of Customs Cost VAT in SC
  InvQty Num(19,6) Inventory Quantity
  CCDLineNum Int(11) CCD Row Number
  TtlVolCCM Num(19,6) Volume Row Total per CCM
  ExcImpQty Num(19,6) Excise Imported Quantity
  ExcFixAmnt Num(19,6) Excise Fixed Amount
  ExcRate Num(19,6) Excise Rate
  ExcAmntUoM Num(19,6) Excise Amount UoM
  ExcAmntAdV Num(19,6) Excise Amount Ad Valorem
  ExcImpQUoM Int(11) Excise Imported Quantity UoM [112=Liters, m3, 168=Tonne, metric ton (1000 kg), 251=Horsepower (1 hp = 0.75 kW), 831=Liters of anhydrous (pure) alcohol]
  ExcBasAmnt Num(19,6) Excise Base Amount
  LineNumV3 Int(11) Target VAT Row Number in IPF3 ->IPF3
  FobVal2 Num(19,6) Corrected Base Doc. Value Row Total (LC) default=0
  FobVal2FC Num(19,6) Corrected Base Doc. Value Row Total (FC) default=0
