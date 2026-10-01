<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# PKL1 - Pick List - Rows
Module: Inventory and Production | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, PickEntry
  ORDER: OrderEntry, OrderLine
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OPKL
  PickEntry Int(11) Row Number
  OrderEntry Int(11) Order Entry
  OrderLine Int(11) Order Row ID
  PickQtty Num(19,6) Picked Quantity
  PickStatus VarChar(1) Pick Status default=R [R=Released for Picking, Y=Picked, P=Partially Picked, D=Partially Delivered, C=Closed]
  RelQtty Num(19,6) Released Quantity
  LogInsac Int(11) Log Instance - History
  PrevReleas Num(19,6) Previously Released Quantity
  BaseObject Int(11) Base Object Type [17=Order, 13=Reserve Invoice, 202=Production Order, 1250000001=Inventory Transfer Request, 0=]
