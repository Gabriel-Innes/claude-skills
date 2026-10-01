<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OIWB - Items - Warehouse Counting Data Backup
Module: Inventory and Production | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SYSTEM_KEY U: WhsCode, ItemCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Abs. Entry
  ItemCode nVarChar(50) Item No. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Counted Num(19,6) Counted Quantity
  WasCounted VarChar(1) Counted Yes/No default=N [Y=Yes, N=No]
