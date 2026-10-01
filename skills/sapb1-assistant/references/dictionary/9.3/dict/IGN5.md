<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# IGN5 - Goods Receipt - Withholding Tax
Module: Inventory and Production | 148 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, AbsEntry
  SECONDERY U: Doc1LineNo, BaseAbsEnt, WTCode, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator ->OIGN
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
  BaseType VarChar(1) Base Type [G=Gross, N=Net, V=VAT]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseLine Int(11) Base Line
  BaseNum Int(11) Base Document Type default=-1 [-1=, 0=, 202=Production Order]
  LineNum Int(11) Line Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Abs. Entry default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=59 ->ADP1
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
  TDSType VarChar(1) TDS Type [E=eTDS, D=GST TDS, C=GST TCS]
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
