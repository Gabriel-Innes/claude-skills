<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# DWZ3 - Dunning Wizard Array 3 - Recommended Service Invoice
Module: Marketing Documents | 22 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LetterNum, CardCode, WizardId
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
