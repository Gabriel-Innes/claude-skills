<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# UPT1 - User Authorization Tree - Extended Permission
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: FormId, PermId
  FORM_ID: FormId
Fields (name type(len) description [values] ->parent table):
  PermId nVarChar(20) Authorization ID ->OUPT
  FormId nVarChar(20) Form ID
  VisOrder Int(6) Display Order
