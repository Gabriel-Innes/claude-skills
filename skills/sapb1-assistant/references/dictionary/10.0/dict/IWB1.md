<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# IWB1 - Batch No. Quantities Backup
Module: Inventory and Production | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNumber
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Abs. Entry ->OIWB
  LineNumber Int(11) Line Number
  BtqAbs Int(11) Btq Abs. Entry ->OBTQ
  MdAbsEntry Int(11) MD Abs. Entry ->OBTN
  CountedQty Num(19,6) Counted Quantity
