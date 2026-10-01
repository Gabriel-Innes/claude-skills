<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ECDW1 - ECD Wizard - Rows 1
Module: Reports | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ExNumData2, ExNumData1, DocType, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  DocType VarChar(1) Template Type [B=Balance Sheet, P=Profit and Loss]
  ExNumData1 Int(11) Extra Numeric Data 1
  ExNumData2 Int(11) Extra Numeric Data 2
  ExNumData3 Int(11) Extra Numeric Data 3
  ExStrData1 nVarChar(254) Extra String Data 1
  ExStrData2 nVarChar(254) Extra String Data 2
  ExStrData3 nVarChar(254) Extra String Data 3
