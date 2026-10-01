<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OPKL - Pick List
Module: Inventory and Production | 17 columns | ObjType: 156
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Absolute entry
  Name nVarChar(155) Name
  OwnerCode Int(6) Owner Code ->OUSR
  OwnerName nVarChar(155) Owner Name
  PickDate Date(8) Pick Date
  Remarks Text(16) Remarks
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  ShipType Int(6) Shipping Type
  Status VarChar(1) Status default=R [R=Released, Y=Picked, P=Partially Picked, D=Partially Delivered, C=Closed]
  Printed VarChar(1) Printed default=N [Y=Copy, N=Original, =]
  LogInstac Int(11) Log Instance - History
  ObjType nVarChar(20) Object Type default=156 ->ADP1
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  UseBaseUn VarChar(1) Inventory UoM default=N [Y=Yes, N=No]
