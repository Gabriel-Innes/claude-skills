<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OHST - Employee Status
Module: Human Resources | 3 columns | ObjType: 173
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: statusID
  NAME_KEY U: name
Fields (name type(len) description [values] ->parent table):
  statusID Int(11) Status ID
  name nVarChar(20) Name
  descriptio Text(16) Description
