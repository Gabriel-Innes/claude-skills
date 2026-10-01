<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# TCN3 - Tracking Note - Warehouse Qty
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WhsCode, LineNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Abs. Entry ->OTCN
  LineNum Int(11) Row Number
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  QtyOnHand Num(19,6) On Hand Quantity
