<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# RSC3 - Resouces - Fixed Assets
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ResCode, ItemCode
  ITEM_CODE U: ItemCode
Fields (name type(len) description [values] ->parent table):
  ResCode nVarChar(50) Internal Resource ID ->ORSC
  ItemCode nVarChar(50) Item Code ->OITM
  LogInstanc Int(11) Log Instance default=0
