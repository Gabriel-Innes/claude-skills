<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CCS1 - Cycle Count Determination- Subtable
Module: Inventory and Production | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Entry, WhsCode
Fields (name type(len) description [values] ->parent table):
  WhsCode nVarChar(8) Warehouse Code
  Entry Int(11) Entry
  CycleCode Int(6) Cycle Code
  Alert VarChar(1) Alert default=N [Y=Yes, N=No]
  DestUser Int(6) Destination User
  NextDate Date(8) Next Counting Date
  Time Int(6) Time
  ExcldZrQty VarChar(1) Exclude Zero Quantity default=Y [Y=Yes, N=No]
  Alerted VarChar(1) Alerted default=N [N=No, Y=Yes]
  ChangExist VarChar(1) Change Existing Items in DI default=N [N=No, Y=Yes]
