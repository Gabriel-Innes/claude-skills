<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# DGP2 - Expanded Selection Criteria
Module: Administration | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CondNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->ODGP
  CondNum Int(11) Condition Number
  SelFldID nVarChar(100) Selection Field ID
  FromString nVarChar(200) String Value From
  FromNumber Int(11) Number Value From
  FromMoney Num(19,6) Amount Value From
  FromDate Date(8) Date Value From
  ToString nVarChar(200) String Value To
  ToNumber Int(11) Number Value To
  ToMoney Num(19,6) Amount Value To
  ToDate Date(8) Date Value To
