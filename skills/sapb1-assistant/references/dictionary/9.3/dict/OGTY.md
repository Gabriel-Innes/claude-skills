<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OGTY - GST Regn Type
Module: Inventory and Production | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator
  GSTType nVarChar(50) GST Regn. type
  descrip nVarChar(100) Description
