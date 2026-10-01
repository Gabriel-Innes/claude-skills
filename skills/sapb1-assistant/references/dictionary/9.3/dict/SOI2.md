<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SOI2 - Statement of Import - Branches
Module: Reports | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BPLId, WizardId
Fields (name type(len) description [values] ->parent table):
  WizardId Int(11) Wizard ID ->OSOI
  BPLId Int(11) Assigned Branch ->OBPL
