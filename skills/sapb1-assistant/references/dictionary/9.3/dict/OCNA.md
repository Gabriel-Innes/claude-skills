<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCNA - CNAE Code
Module: Administration | 3 columns | ObjType: 278
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsId
  CODE U: CNAECode
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  CNAECode nVarChar(9) Code
  Descrip Text(16) Description
