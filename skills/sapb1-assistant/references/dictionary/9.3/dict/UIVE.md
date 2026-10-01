<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# UIVE - FIFO Based Sales Return
Module: Inventory and Production | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  TRANS_SEQ: LayerID, TransSeq
  TreeID: TreeID
Fields (name type(len) description [values] ->parent table):
  TreeID Int(11) Tree ID default=0
  ParentID Int(11) Parent ID default=-1
  AbsEntry Int(11) Internal Number
  LocType Int(6) Location Type
  LocCode nVarChar(8) Location Code
  TransSeq Int(11) Transaction Sequence No. ->UIVL
  LayerID Int(11) Layer ID
  LayerInQty Num(19,6) Layer In Quantity
  LayerOutQ Num(19,6) Layer Out Quantity
  LayerVal Num(19,6) Layer Value
  ItemCode nVarChar(50) Item Code ->UITM
  EntryTreeI Int(11) Entry Tree ID
  LayerCogs Num(19,6) Layer - Cost of Goods Sold
