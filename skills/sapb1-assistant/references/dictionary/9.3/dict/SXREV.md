<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SXREV - XLR Enum Values
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: name, enumid
Fields (name type(len) description [values] ->parent table):
  enumid Int(11) enumid
  name nVarChar(50) name
  ivalue Int(11) ivalue
  cvalue nVarChar(50) cvalue
