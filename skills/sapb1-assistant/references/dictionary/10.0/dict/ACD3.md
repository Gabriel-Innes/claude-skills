<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ACD3 - Credit Memo - Item Areas
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, ItemLine, DprArea
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OACQ
  ItemLine Int(11) Item Row Number
  ItemCode nVarChar(50) Item Code ->OITM
  DprArea nVarChar(15) Depreciation Area ->ODPA
  Total Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSys Num(19,6) Total (SC)
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance default=0
