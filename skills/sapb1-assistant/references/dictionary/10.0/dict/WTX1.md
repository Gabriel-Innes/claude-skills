<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# WTX1 - WTax Transactions - Rows
Module: Finance | 54 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineSeq
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal ID ->OWTX
  LineSeq Int(11) Row Sequence
  SrcArrType Int(11) Source Array Type default=-1 [-1=Default, 1=Main, 12=Array 1, 13=Array 2, 14=Array 3]
  SrcLineNum Int(11) Source Row Number default=-1
  SrcGrpNum Int(11) Source Group Number default=-1 [-1=Default, 0=Group 1, 1=Group 2, 2=Group 3]
  BaseObjTyp nVarChar(20) Base Object Type default=-1
  BaseAbs Int(11) Base Document Internal No. default=-1
  BaseArrTyp Int(11) Base Array Type default=-1 [-1=Default, 1=Main, 12=Array 1, 13=Array 2, 14=Array 3, 15=Array 4, 16=Array 5, 17=Array 6, 18=Array 7, 24=Array 13]
  BaseLinNum Int(11) Base Row Number default=-1
  BaseGrpNum Int(11) Base Group No. default=-1 [-1=Default, 0=Group 1, 1=Group 2, 2=Group 3]
  WTaxAbsId nVarChar(8) Tax Code ID
  Account nVarChar(15) Account ->OACT
  Rate Num(19,6) Rate
  Exemption Num(19,6) Exemption Rate
  BaseType VarChar(1) Base Type default=N [N=Net, V=VAT, G=Gross, H=Gross - VAT]
  BaseNetSum Num(19,6) Base Net Sum
  BaseNetSC Num(19,6) Base Net Sum (SC)
  BaseNetFC Num(19,6) Base Net Sum (FC)
  BaseVatSum Num(19,6) Base VAT Sum
  BaseVatSC Num(19,6) Base VAT Sum (SC)
  BaseVatFC Num(19,6) Base VAT Sum (FC)
  AccBaseSum Num(19,6) Accumulated Sum
  AccBaseSC Num(19,6) Accumulated Sum (SC)
  AccBaseFC Num(19,6) Accumulated Sum (FC)
  AccWTaxSum Num(19,6) Accumulated WTax Sum
  AccWTaxSC Num(19,6) Accumulated WTax Sum (SC)
  AccWTaxFC Num(19,6) Accumulated WTax Sum (FC)
  TxblSum Num(19,6) Taxable Sum
  TxblSumSc Num(19,6) Taxable Sum (SC)
  TxblSumFc Num(19,6) Taxable Sum (FC)
  WTaxSum Num(19,6) WTax Sum
  WTaxSumSc Num(19,6) WTax Sum (SC)
  WTaxSumFc Num(19,6) WTax Sum (FC)
  ApplSum Num(19,6) Applied Sum
  ApplSumSc Num(19,6) Applied Sum (SC)
  ApplSumFc Num(19,6) Applied Sum (FC)
  CrditDebit VarChar(1) Credit or Debit Transaction [C=Credit, D=Debit]
  PostingTyp VarChar(1) Sales or Purchase default=N [N=None, R=Sales, P=Purchase]
  Category VarChar(1) Category default=P [I=Invoice, P=Payment]
  WTTypeId Int(11) Type
  WhtType VarChar(1) Withholding Type default=V [V=VAT Withholding, G=Gross Income Withholding, N=Income Tax Withholding, S=Social Security Withholding, I=Industry Specific Withholding, D=District Specific Withholding]
  FmlId Int(11) Formula ID
  BaseMin Num(19,6) Min. Amount
  BaseMinSc Num(19,6) Min. Amount (SC)
  BaseMinFc Num(19,6) Min. Amount (FC)
  ResMin Num(19,6) Min.Ret./Perc. Amount
  ResMinSc Num(19,6) Min.Ret./Perc. Amount (SC)
  ResMinFc Num(19,6) Min.Ret./Perc. Amount (FC)
  AddBas Num(19,6) Add to Base Amount
  AddBasSc Num(19,6) Add to Base Amount (SC)
  AddBasFc Num(19,6) Add to Base Amount (FC)
  ABWVAT Num(19,6) Add to Base without VAT Amount
  ABWVATSc Num(19,6) Add to Base without VAT Amount (SC)
  ABWVATFc Num(19,6) Add to Base without VAT Amount (FC)
