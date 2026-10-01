<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OIWB - Items - Warehouse Counting Data Backup
Module: Inventory and Production | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SYSTEM_KEY U: ItemCode, WhsCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Abs. Entry
  ItemCode nVarChar(50) Item No. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Counted Num(19,6) Counted Quantity
  WasCounted VarChar(1) Counted Yes/No default=N [Y=Yes, N=No]
