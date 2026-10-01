<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# FCT1 - Sales Forecast - Rows
Module: MRP | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsID, ItemCode, Date, WhsCode
Fields (name type(len) description [values] ->parent table):
  AbsID Int(11) Internal Number ->OFCT
  LineID Int(11) Row Number
  ItemCode nVarChar(50) Item No. ->OITM
  Date Date(8) Day Forecasted
  Quantity Num(19,6) Quantity
  WhsCode nVarChar(8) Warehouse default=-1 ->OWHS
