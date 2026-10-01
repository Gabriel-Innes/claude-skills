<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AWHT - Withholding Tax
Module: Finance | 63 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WTCode, LogInstanc
Fields (name type(len) description [values] ->parent table):
  WTCode nVarChar(4) WTax Code
  WTName nVarChar(50) WTax Name
  Rate Num(19,6) Rate
  EffecDate Date(8) Effective From
  Category VarChar(1) Category default=P [I=Invoice, P=Payment]
  BaseType VarChar(1) Base Type default=N [G=Gross, N=Net, V=VAT, U=UoM]
  PrctBsAmnt Num(19,6) % Base Amount
  OffclCode nVarChar(15) Official Code
  Account nVarChar(15) Account ->OACT
  MinTaxAmt Num(19,6) Minimum Taxable Amount
  IsPrgrss VarChar(1) Progressive Tax default=N [Y=Progressive Tax, N=Not Progressive Tax]
  Type VarChar(1) Withholding Type default=V [V=VAT Withholding, I=Income Tax Withholding]
  RoundType VarChar(1) Rounding Type default=C [T=Truncated AU, C=Commercial Values]
  WTTypeId Int(11) Type ->OWTT
  WTCurrency nVarChar(3) Currency ->OCRN
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature ->OUSR
  Section Int(11) Section ->OSEC
  Threshold Num(19,6) Cumulative Threshold
  Surcharge Num(19,6) Surcharge
  Concess VarChar(1) Concessional default=N [Y=Yes, N=No]
  Assessee Int(11) Assessee ->ONOA
  ApTdsAcc nVarChar(15) A/P TDS Account ->OACT
  ApSurAcc nVarChar(15) A/P Surcharge Account ->OACT
  ApCessAcc nVarChar(15) A/P Cess Account ->OACT
  ApHscAcc nVarChar(15) A/P HSC Account ->OACT
  ArTdsAcc nVarChar(15) A/R TDS Account ->OACT
  ArSurAcc nVarChar(15) A/R Surcharge Account ->OACT
  ArCessAcc nVarChar(15) A/R Cess Account ->OACT
  ArHscAcc nVarChar(15) A/R HSC Account ->OACT
  Location Int(11) Location ->OLCT
  ReturnType VarChar(1) Return Type [A=26, B=27]
  UserSign2 Int(6) Updating User ->OUSR
  Inactive VarChar(1) Inactive default=N [Y=Yes, N=No]
  InCSTCode Int(11) CST Code Incoming default=-1 ->OTSC
  OutCSTCode Int(11) CST Code Outgoing default=-1 ->OTSC
  CalBaseN nVarChar(2) Nature of Calculation Base ->OBSI
  PymntRsnCd nVarChar(3) Payment Reason Code ->OSWA
  DIOTRpt VarChar(1) DIOT Report default=N [Y=Yes, N=No]
  TDSType VarChar(1) TDS Type [E=eTDS, D=GST TDS, C=GST TCS]
  ApIgstAcc nVarChar(15) A/P IGST Account ->OACT
  ApCgstAcc nVarChar(15) A/P CGST Account ->OACT
  ApSgstAcc nVarChar(15) A/P SGST Account ->OACT
  ArIgstAcc nVarChar(15) A/R IGST Account ->OACT
  ArCgstAcc nVarChar(15) A/R CGST Account ->OACT
  ArSgstAcc nVarChar(15) A/R SGST Account ->OACT
  ApUtgstAcc nVarChar(15) A/P UTGST Account ->OACT
  ApCsgstAcc nVarChar(15) A/P Cess GST Account ->OACT
  ArUtgstAcc nVarChar(15) A/R UTGST Account ->OACT
  ArCsgstAcc nVarChar(15) A/R Cess GST Account ->OACT
  TransThres Num(19,6) Transaction Threshold default=0
  EBWTaxCate Int(11) Withholding Tax Category ->OWHC
  ArTcsInAcc nVarChar(15) A/R TCS Interim Account ->OACT
  ArSurInAcc nVarChar(15) A/R Surcharge Interim Account ->OACT
  ArCesInAcc nVarChar(15) A/R Cess Interim Account ->OACT
  ArHscInAcc nVarChar(15) A/R HSC Interim Account ->OACT
  ApTcsInAcc nVarChar(15) A/P TCS Interim Account ->OACT
  ApSurInAcc nVarChar(15) A/P Surcharge Interim Account ->OACT
  ApCesInAcc nVarChar(15) A/P Cess Interim Account ->OACT
  ApHscInAcc nVarChar(15) A/P HSC Interim Account ->OACT
  LnWTInAcc nVarChar(15) Interim Account for Tax ->OACT
  NoDedThrsh VarChar(1) Apply Tax Exemption After Threshold default=N [Y=Yes, N=No]
