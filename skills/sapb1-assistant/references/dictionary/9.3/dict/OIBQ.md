<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OIBQ - Item - Bin Accumulator
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  BUSINESS_K U: BinAbs, ItemCode
  BIN_ABS: BinAbs
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ItemCode nVarChar(50) Item Code ->OITM
  BinAbs Int(11) Bin Internal Number ->OBIN
  OnHandQty Num(19,6) On-Hand Quantity
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Freezed VarChar(1) Item Frozen in Bin Location default=N [Y=Yes, N=No]
  FreezeDoc Int(11) Inventory Count Doc. Frozen By ->OINC
