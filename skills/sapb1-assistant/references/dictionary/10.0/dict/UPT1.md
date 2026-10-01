<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# UPT1 - User Authorization Tree - Extended Permission
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PermId, FormId
  FORM_ID: FormId
Fields (name type(len) description [values] ->parent table):
  PermId nVarChar(20) Authorization ID ->OUPT
  FormId nVarChar(20) Form ID
  VisOrder Int(6) Display Order
