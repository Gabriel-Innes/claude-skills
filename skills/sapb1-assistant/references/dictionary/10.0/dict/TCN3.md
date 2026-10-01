<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# TCN3 - Tracking Note - Warehouse Qty
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, WhsCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Abs. Entry ->OTCN
  LineNum Int(11) Row Number
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  QtyOnHand Num(19,6) On Hand Quantity
