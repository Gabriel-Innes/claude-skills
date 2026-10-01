<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# DWZ1 - Dunning Wizard Array1 - BP Filter
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CardCode, WizardId
Fields (name type(len) description [values] ->parent table):
  WizardId Int(11) Wizard ID ->ODWZ
  CardCode nVarChar(15) BP Card Code ->OCRD
  DunAddr nVarChar(254) Dunning Address
  CheckedBP VarChar(1) Checked BP default=Y [Y=Yes, N=No]
  FaxNum nVarChar(20) Fax Number
  Email nVarChar(100) E-Mail Address
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
