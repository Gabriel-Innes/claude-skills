<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ITL1 - Srl & Batch Details in Transac
Module: Inventory and Production | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SysNumber, ItemCode, LogEntry
  SNB_SYSID: SysNumber, ItemCode
Fields (name type(len) description [values] ->parent table):
  LogEntry Int(11) Log Internal ID ->OITL
  ItemCode nVarChar(50) Item Code ->OITM
  SysNumber Int(11) System Number
  Quantity Num(19,6) Quantity
  AllocQty Num(19,6) Allocated Quantity
  MdAbsEntry Int(11) MD Abs Entry
  ReleaseQty Num(19,6) Release Quantity
  PickedQty Num(19,6) Picked Quantity
  OrderedQty Num(19,6) Ordered Quantity
