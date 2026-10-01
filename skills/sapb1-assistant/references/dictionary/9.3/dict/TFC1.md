<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# TFC1 - Tax Type Combination - Rows
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DispOrder, TfcId
  TAXTYPE: TypeId
Fields (name type(len) description [values] ->parent table):
  TfcId Int(11) TFC ID ->OTFC
  DispOrder Int(11) Display Order
  TypeId Int(11) Tax Type ID ->OSTT
  FmlId Int(11) Formula ID ->OFML
