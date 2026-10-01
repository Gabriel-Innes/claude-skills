<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ITW1 - Item Count Alert
Module: Inventory and Production | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ItemCode, WhsCode, BinAbs
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  UserSign Int(6) User Signature ->OUSR
  CycleCode Int(6) Cycle Code ->OCYC
  Alert VarChar(1) Alert default=N [N=No, Y=Yes]
  NextDate Date(8) Next Counting Date
  Time Int(6) Alert Time
  DestUser Int(6) Destination User ->OUSR
  Alerted VarChar(1) Alerted default=N [Y=Yes, N=No]
  BinAbs Int(11) Bin Internal Number default=-1 ->OBIN
