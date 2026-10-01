<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# VRW2 - VAT Reposting Wizard - Rows 2
Module: Finance | 35 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ARINVAbs, VatGroup, TaxInvID, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  TaxInvID Int(11) A/P Tax Invoice ID ->OTPI
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  Selected VarChar(1) Selected Line default=N [Y=Yes, N=No]
  LineStatus VarChar(1) Line Status default=R [C=Canceled, R=Regular]
  DebitAcc nVarChar(15) Debit Account ->OACT
  DocDate Date(8) Document Date
  VatAmount Num(19,6) VAT Amount
  NetAmount Num(19,6) Net Amount
  JETransID Int(11) Journal Entry Number ->OJDT
  Ref1 nVarChar(100) Reference 1
  Ref2 nVarChar(100) Reference 2
  Ref3 nVarChar(27) Reference 3
  Remarks nVarChar(50) Journal Entry Remarks
  TrnsCode nVarChar(4) Code
  BPLId Int(11) Branch ->OBPL
  ARINVAbs Int(11) First A/R Invoice Abs Entry default=0
  ARDocNumAb nVarChar(20) A/R Document No.
  ARAbsEntry Int(11) A/R Document Abs Entry default=0
  ARObjType nVarChar(20) A/R Document Object Type
  ARDocDate Date(8) A/R Document Date
  CstmrCode nVarChar(15) Customer Code
  CstmrName nVarChar(100) Customer Name
  TpiDocNum Int(11) A/P Tax Invoice No.
  TpiDocDate Date(8) A/P Tax Invoice Posting Date
  VendorCode nVarChar(15) Vendor Code
  VendorName nVarChar(100) Vendor Name
  ARDocMemo nVarChar(254) A/R Document Remarks
  TpiMemo nVarChar(254) A/P Tax Invoice Remarks
  GrsAmt Num(19,6) Gross Amount
  VatAcc nVarChar(15) VAT Account
  OpenVatAmt Num(19,6) Open VAT Amount
  OpenNetAmt Num(19,6) Open Net Amount
  OpenGrsAmt Num(19,6) Open Gross Amount
  RepstedVat Num(19,6) Reposted VAT
