<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# TFC1 - Tax Type Combination - Rows
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TfcId, DispOrder
  TAXTYPE: TypeId
Fields (name type(len) description [values] ->parent table):
  TfcId Int(11) TFC ID ->OTFC
  DispOrder Int(11) Display Order
  TypeId Int(11) Tax Type ID ->OSTT
  FmlId Int(11) Formula ID ->OFML
