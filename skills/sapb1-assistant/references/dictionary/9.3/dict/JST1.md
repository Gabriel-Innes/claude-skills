<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# JST1 - TDS Adjustment - Rows
Module: Finance | 52 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineNum, AbsId
  BASE_ENTRY: BaseLine, BaseAbsId, BaseNum, AbsId
  WT_CODE: WTCode, AbsId
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number ->OJST
  LineNum Int(11) Row Number default=0
  WTCode nVarChar(4) WTax Code ->OWHT
  BaseNum Int(11) Base Document Type default=-1 [-1=, 18=A/P Invoice, 204=A/P Down Payment]
  BaseAbsId Int(11) Base Document Internal ID
  BaseLine Int(11) Base Row
  LogInstanc Int(11) Log Instance default=0
  Rate Num(19,6) Rate
  TdsRate Num(19,6) TDS Rate
  SurRate Num(19,6) Surcharge Rate
  CessRate Num(19,6) Cess Rate
  HscRate Num(19,6) HSC Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntSC Num(19,6) Taxable Amount (SC)
  TxblAmntFC Num(19,6) Taxable Amount (FC)
  Category VarChar(1) Category [P=Payment, I=Invoice]
  Criteria VarChar(1) Criteria [Y=Accrual, N=Cash]
  Type VarChar(1) Withholding Tax Type [V=VAT Withholding, I=Incoming Tax Withholding]
  RoundType VarChar(1) Rounding Type [T=Truncated, C=Commercial Values]
  BaseType VarChar(1) Base Type [G=Gross, N=Net, V=VAT]
  Account nVarChar(15) G/L Account ->OACT
  TdsAcc nVarChar(15) TDS Account ->OACT
  SurAcc nVarChar(15) Surcharge Account ->OACT
  CessAcc nVarChar(15) Cess Account ->OACT
  HscAcc nVarChar(15) HSC Account ->OACT
  WTAmnt Num(19,6) WTax Amount
  WTAmntSC Num(19,6) WTax Amount (SC)
  WTAmntFC Num(19,6) WTax Amount (FC)
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
