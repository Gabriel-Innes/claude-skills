<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OSWA - Specific Withholding Amounts
Module: General | 72 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PymntRsnCd, CardCode, CUSplit
Fields (name type(len) description [values] ->parent table):
  PymntRsnCd nVarChar(3) Payment Reason Code ->OPTR
  CardCode nVarChar(15) BP Code ->OCRD
  FllTxInAdv Num(19,6) Full WTax Taxation in Advance
  AmntsOnhld Num(19,6) WTax Amount on Hold
  RTAsWth Num(19,6) Regional IRPEF Held as WTax
  RTAsAdv Num(19,6) Regional IRPEF - In Advance
  SspndRegTx Num(19,6) Regional Suspended Tax - IRPEF
  MTAsWth Num(19,6) Municipal Tax as WTax - IRPEF
  MTAsAdv Num(19,6) Municipal Tax Held as Advance
  SspndMTTx Num(19,6) Suspended Municipal Tax
  TxblPrYr Num(19,6) Taxable Amt - Previous Year
  WTHPrYr Num(19,6) WTax Amount - Previous Year
  ScrtyCntrP Num(19,6) Social Security Tax Payer
  ScrtyCntrS Num(19,6) Social Security Supplier
  ExpsRmbrsd Num(19,6) Expenses Reimbursed
  WTHRmbrsd Num(19,6) WTax Reimbursed
  DlvryIdNo nVarChar(100) Delivery Identification No.
  SnglCrtfNo nVarChar(17) Single Certification No.
  ErnYr Int(6) Earning Year
  Advanced VarChar(1) Advanced default=N [Y=Yes, N=No]
  WTHTypCd nVarChar(2) WTax Type Code ->OWXT
  GrssAmount Num(19,6) Gross Amount Due to Supplier
  NtSbjctFrg Num(19,6) Amount Not Subject to WT
  TxblAmnt Num(19,6) Taxable Amount
  WTHAmnt Num(19,6) Withholding Tax Amount
  SSFiscalCd nVarChar(16) Social Security Fiscal C..(29)
  SSIName nVarChar(100) Social Security Institut..(30)
  SSICode VarChar(1) Social Security Institut..(31) [2=ENPAM, 4=ENPAPI]
  CompanyCd nVarChar(16) Company Code(32)
  Category VarChar(1) Category(33) [O=Medico di assistenze primaria, P=Pediatra di libera scelta, Q=Medico specialista esterno, R=Medico della Medicina dei Servize a tempo determinato, S=Medico dell'Emergenza territoriale a tempo determinato, T=Medico della Continuit� assistenziale a tempo determinato, U=Infermieri prestatori d'opera occasionali]
  EmpeSSCntr Num(19,6) Employee social security..(34)
  EmprSSCntr Num(19,6) Employer social security..(35)
  OthCntrbts VarChar(1) Other Contributions(36) default=N [Y=Yes, N=No]
  VOthCntrbt Num(19,6) Value of Other Contribut..(37)
  OthAmntDue Num(19,6) Other amounts due(38)
  OthAmntPd Num(19,6) Other amounts paid(39)
  AmntPdBfBr Num(19,6) Amount Paid before Bankr..(41)
  AmntPdByTr Num(19,6) Amount Paid by Trustee(42)
  FiscalCode nVarChar(16) Fiscal Code(52)
  TxblAmntE Num(19,6) Taxable Amount(53)
  TaxAmount Num(19,6) Tax Amount(54)
  TxAmntInAd Num(19,6) Tax Amount in Advance(55)
  SspndWTHTx Num(19,6) Suspended WTH Tax(56)
  AdRgTxIRPH Num(19,6) Additional Regional tax..(57)
  AdRgTxIRPA Num(19,6) Additional Regional tax..(58)
  SspdRgnlTx Num(19,6) Suspended Regional Tax(59)
  AdCtTxIRWT Num(19,6) Additional City tax to I..(60)
  AdCtTxIWTA Num(19,6) Additional City Tax to I..(61)
  SspndCtTx Num(19,6) Suspended City Tax(62)
  FsCdTrdPty nVarChar(16) Fiscal Code Third Party(71)
  FCdTrdPtyS nVarChar(16) Fiscal Code Third Party..(72)
  FscCdExpr nVarChar(16) Fiscal Code Expropriation(73)
  FsCdMnDbS nVarChar(16) Fiscal Code of Main Deb..(101)
  AmntPdS Num(19,6) Amount Paid(102)
  WHTApdS Num(19,6) WHT Applied(103)
  WHTNApdS VarChar(1) WHT not Applied(104) default=N [Y=Yes, N=No]
  FsCdMnDbR nVarChar(16) Fiscal Code of Main Deb..(105)
  AmntPdR Num(19,6) Amount Paid(106)
  WHTApdR Num(19,6) WHT Applied(107)
  WHTNApdR VarChar(1) WHT not Applied(108) default=N [Y=Yes, N=No]
  AmntPdA Num(19,6) Amount Paid(131)
  TxAppldA Num(19,6) Tax Applied(132)
  AmntPdB Num(19,6) Amount Paid(133)
  TxAppldB Num(19,6) Tax Applied(134)
  AmntPdC Num(19,6) Amount Paid(135)
  TxAppldC Num(19,6) Tax Applied(136)
  AmntPdD Num(19,6) Amount Paid(137)
  TxAppldD Num(19,6) Tax Applied(138)
  AmtPvdNTxS Num(19,6) Amounts provided and no..(104)
  AmtPvdNTxR Num(19,6) Amounts provided and no..(108)
  CUSplit VarChar(1) CU Split default=N [N=No, Y=Yes]
  SmRnNtWTx Num(19,6) Returned Amount After Deduction of WTax
