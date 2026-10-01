<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OIBQ - Item - Bin Accumulator
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  BUSINESS_K U: ItemCode, BinAbs
  BIN_ABS: BinAbs
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ItemCode nVarChar(50) Item Code ->OITM
  BinAbs Int(11) Bin Internal Number ->OBIN
  OnHandQty Num(19,6) On-Hand Quantity
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Freezed VarChar(1) Item Frozen in Bin Location default=N [Y=Yes, N=No]
  FreezeDoc Int(11) Inventory Count Doc. Frozen By ->OINC
