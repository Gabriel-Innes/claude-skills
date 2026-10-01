<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# PKL2 - Pick List for SnB and Bin Details
Module: Inventory and Production | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Pkl2LinNum, PickEntry, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OPKL
  PickEntry Int(11) Row Number
  Pkl2LinNum Int(11) PKl2 Line Number
  ItemCode nVarChar(50) Item No. ->OITM
  ManagedBy Int(11) Management Method default=-1 [10000044=BTN, 10000045=SRN, -1=NOB]
  SnBEntry Int(11) SnB Abs. Entry
  BinAbs Int(11) Bin Internal Number ->OBIN
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  RelQtty Num(19,6) Released Quantity
  PickQtty Num(19,6) Picked Quantity
  ObjType nVarChar(20) Object Type default=156 ->ADP1
  LogInstanc Int(11) Log Instance default=0
