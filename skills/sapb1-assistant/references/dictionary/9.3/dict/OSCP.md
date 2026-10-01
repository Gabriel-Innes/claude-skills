<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OSCP - Service Call Problem Types
Module: Service | 3 columns | ObjType: 169
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: prblmTypID
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  prblmTypID Int(6) Problem Type ID
  Name nVarChar(20) Name
  Descriptio Text(16) Description
