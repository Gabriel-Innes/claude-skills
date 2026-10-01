<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OORL - Relationships
Module: Sales Opportunities | 2 columns | ObjType: 212
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: OrlCode
  NAME U: OrlDesc
Fields (name type(len) description [values] ->parent table):
  OrlCode Int(11) Relationship Code
  OrlDesc nVarChar(100) Relationship Description
