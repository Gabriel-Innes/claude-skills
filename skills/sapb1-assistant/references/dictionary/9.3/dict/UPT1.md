<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# UPT1 - User Authorization Tree - Extended Permission
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: FormId, PermId
  FORM_ID: FormId
Fields (name type(len) description [values] ->parent table):
  PermId nVarChar(20) Authorization ID ->OUPT
  FormId nVarChar(20) Form ID
  VisOrder Int(6) Display Order
