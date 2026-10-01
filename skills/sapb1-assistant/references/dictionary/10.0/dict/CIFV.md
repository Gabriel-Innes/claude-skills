<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CIFV - Inventory-FIFO Revaluation
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ItemCode, LayerNum
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item Code ->OITM
  LayerNum Int(11) Layer Number
  OinmNum Int(11) OINM Transaction Number ->OINM
  Instance Int(11) Instance in OINM
  Quantity Num(19,6) Quantity in Layer
  Price Num(19,6) Price in Layer
  OutQty Num(19,6) Out Quantity
