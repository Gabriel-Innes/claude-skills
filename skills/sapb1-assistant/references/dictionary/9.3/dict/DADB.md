<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# DADB - Data Archive DSA Balance
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Document Internal ID
  ItemCode nVarChar(50) Item Number ->OITM
  LocCode Int(11) Location Code ->OLCT
  OpenBal Num(19,6) Opening Balance
