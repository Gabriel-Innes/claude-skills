<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OEBL - E-Balance
Module: Reports | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  WizardName nVarChar(100) Wizard Name
  Status VarChar(1) Status [G=Generated, S=Saved]
  CreateDate Date(8) Create Date
  UserSign Int(6) User Signature ->OUSR
