<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ITW1 - Item Count Alert
Module: Inventory and Production | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: BinAbs, WhsCode, ItemCode
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
