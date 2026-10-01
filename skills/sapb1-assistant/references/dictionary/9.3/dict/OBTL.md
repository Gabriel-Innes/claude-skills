<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OBTL - Bin Transaction Log
Module: Inventory and Production | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  MESSAGE_ID: MessageID
  BIN_ABS: BinAbs
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  MessageID Int(11) ILM Message ID ->OILM
  BinAbs Int(11) Bin Internal Number ->OBIN
  SnBMDAbs Int(11) SnB Master Data Internal Number default=-1
  Quantity Num(19,6) Quantity
  ITLEntry Int(11) ITL Log Internal ID default=-1 ->OITL
