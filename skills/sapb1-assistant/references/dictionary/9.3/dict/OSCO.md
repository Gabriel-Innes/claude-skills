<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OSCO - Service Call Origins
Module: Service | 4 columns | ObjType: 192
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: originID
Fields (name type(len) description [values] ->parent table):
  originID Int(6) Origin ID
  Name nVarChar(20) Name
  Descriptio Text(16) Description
  Locked VarChar(1) Locked
