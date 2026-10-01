<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# IWB1 - Batch No. Quantities Backup
Module: Inventory and Production | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNumber, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Abs. Entry ->OIWB
  LineNumber Int(11) Line Number
  BtqAbs Int(11) Btq Abs. Entry ->OBTQ
  MdAbsEntry Int(11) MD Abs. Entry ->OBTN
  CountedQty Num(19,6) Counted Quantity
