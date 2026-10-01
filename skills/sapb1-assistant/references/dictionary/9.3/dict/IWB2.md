<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# IWB2 - Serial No. Quantities Backup
Module: Inventory and Production | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineNumber, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Abs. Entry ->OIWB
  LineNumber Int(11) Line Number
  SrqAbs Int(11) SRQ Abs. Entry ->OSRQ
  MdAbsEntry Int(11) MD Abs. Entry ->OSRN
  CountedQty Num(19,6) Counted Quantity
