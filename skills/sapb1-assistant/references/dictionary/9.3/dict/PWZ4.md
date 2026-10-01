<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# PWZ4 - Payment Wizard - Rows 4
Module: Banking | 36 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ObjType, RctId, IdEntry
Fields (name type(len) description [values] ->parent table):
  IdEntry Int(11) ID Entry ->OPWZ
  PymNum Int(11) Payment Number
  CardCode nVarChar(15) Vendor's Card code ->OCRD
  CardName nVarChar(100) Vendor's Card Name
  PymMeth nVarChar(15) Payment Method ->OPYM
  GLAccCode nVarChar(15) G/L Account Code ->OACT
  PymAmount Num(19,6) Sum of payment amount
  PymAmntFC Num(19,6) Total Payment Amount (FC)
  ObjType nVarChar(20) Object Type [24=Incoming Payment, 46=Outgoing Payment]
  RctId Int(11) Document ID
  DocCurr nVarChar(3) Document Currency
  BankAccou nVarChar(50) Acct No. ->OACT
  BnkDflt nVarChar(30) Default Bank
  BankCountr nVarChar(3) Bank Country ->OCRY
  BankActKey Int(11) Bank Account Internal ID ->DSC1
  LineType VarChar(1) Line Type default=G
  ManualNum Int(11) Manual Entry No. default=0
  TBankCode nVarChar(30) Target Default Bank default=-1
  TDflAccoun nVarChar(50) Target Default Account
  TBankCount nVarChar(3) Target Bank Country ->OCRY
  TargetBran nVarChar(50) Target Bank Branch
  BcgPmnt Num(19,6) Payment Amount (BCG)
  BcgPmntFc Num(19,6) Payment Amount FC (BCG)
  RecipStatu nVarChar(2) Recipient Status
  BudgetId nVarChar(100) VAT Budget Classification Code
  OKATO nVarChar(11) OKATO
  PymReason nVarChar(2) Payment Reason
  PostPeriod nVarChar(10) Posting Period Code
  BaseDocTyp nVarChar(2) Base Document Type
  BaseDocDat Date(8) Base Docoument Date
  TaxPymType nVarChar(2) Tax Payment Type
  OKTMO nVarChar(12) OKTMO
  IBAN nVarChar(50) IBAN
  SwiftNum nVarChar(50) BIC/SWIFT Code
  UIPCode nVarChar(25) UIP Code
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
