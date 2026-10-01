<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# DWZ5 - Dunning Wizard Array 5-Selected Branches
Module: Marketing Documents | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BPLId, WizardId
Fields (name type(len) description [values] ->parent table):
  WizardId Int(11) Wizard ID ->ODWZ
  BPLId Int(11) Assigned Branch ->OBPL
