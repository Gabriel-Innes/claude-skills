<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CIN23 - A/P Invoice - Selected Asset Master Data
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, VisOrder
  ASSETS: DocEntry, LineNum, AssetCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCIN
  LineNum Int(11) Row Number
  AssetCode nVarChar(50) Selected Asset Code ->OITM
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Remarks nVarChar(100) Remarks
  Amount Num(19,6) Amount
  AmountSC Num(19,6) Amount (SC)
  SerialNo nVarChar(30) Serial Number
  VisOrder Int(11) Visual Order
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=132 ->ADP1
