<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ILM3 - Non-Inventory and Resource Components Log Msg
Module: Inventory and Production | 15 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineID, MessageID
Fields (name type(len) description [values] ->parent table):
  MessageID Int(11) Message ID ->OILM
  LineID Int(11) Line ID
  POLine Int(11) Line in Production Order
  ItemType Int(11) Item Type
  ItemCode nVarChar(50) Item No. ->OITM
  LocType Int(6) Location Type
  LocCode nVarChar(8) Location Code
  Quantity Num(19,6) Quantity
  TotalLC Num(19,6) Inventory Total LC
  BaseAbsEnt Int(11) Abs. Entry of Base Doc. default=-1
  BaseType Int(11) Base Transaction Type default=-1 [-1=, 0=, 60=Goods Issue]
  BaseLine Int(11) Base Line Number default=-1
  StgSeqNum Int(11) Stage Sequence Number
  StgEntry Int(11) Stage Entry
  StgDesc nVarChar(100) Stage Description
