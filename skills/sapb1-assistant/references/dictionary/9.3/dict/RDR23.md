<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RDR23 - A/P Invoice - Selected Asset Master Data
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: VisOrder, LineNum, DocEntry
  ASSETS: AssetCode, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDR
  LineNum Int(11) Row Number
  AssetCode nVarChar(50) Selected Asset Code ->OITM
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Remarks nVarChar(100) Remarks
  Amount Num(19,6) Amount
  AmountSC Num(19,6) Amount (SC)
  SerialNo nVarChar(30) Serial Number
  VisOrder Int(11) Visual Order
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=17 ->ADP1
