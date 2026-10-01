<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# DWZ1 - Dunning Wizard Array1 - BP Filter
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WizardId, CardCode
Fields (name type(len) description [values] ->parent table):
  WizardId Int(11) Wizard ID ->ODWZ
  CardCode nVarChar(15) BP Card Code ->OCRD
  DunAddr nVarChar(254) Dunning Address
  CheckedBP VarChar(1) Checked BP default=Y [Y=Yes, N=No]
  FaxNum nVarChar(50) Fax Number
  Email nVarChar(100) E-Mail Address
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
