<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SIVQ - FIFO Queue Working Table
Module: Inventory and Production | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  TRANS_SEQ U: LayerID, TransSeq
  TreeOpenQt: OpenQty, TreeID
Fields (name type(len) description [values] ->parent table):
  TreeID Int(11) Tree ID default=0
  ParentID Int(11) Parent ID default=-1
  LocType Int(6) Location Type
  LocCode nVarChar(8) Location Code
  TransSeq Int(11) Transaction Sequence No. ->SIVL
  LayerID Int(11) Layer ID
  OpenQty Num(19,6) Open Quantity
  OpenValue Num(19,6) Open Value
  ItemCode nVarChar(50) Item Code ->SITM
  AbsEntry Int(11) Internal ID
  StockActio Int(11) Stock Action Type default=-1 [15=Delivery, 16=Returns, 13=A/R Invoice, 14=A/R Credit Memo, 132=Correction Invoice, 20=Goods Receipt, 21=Goods Return, 18=A/P Invoice, 19=A/P Credit Memo, -2=Opening Balance, 58=Inventory Update, 59=Goods Receipt, 60=Goods Issue, 67=Inventory Transfer, 68=Work Instructions, -1=All Transactions, 162=Inventory Revaluation, 69=Landed Costs]
  RemMethod VarChar(1) Quantity Removal Method default=U [U=Unspecified, I=Issue, R=Revaluation]
