<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CRD8 - BP Branch Assignment
Module: Business Partners | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BPLId, CardCode
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code ->OCRD
  BPLId Int(11) Assigned Branch ->OBPL
  DisabledBP VarChar(1) Disabled for BP default=N [Y=Yes, N=No]
