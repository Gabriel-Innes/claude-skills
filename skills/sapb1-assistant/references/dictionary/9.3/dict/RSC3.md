<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RSC3 - Resouces - Fixed Assets
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ItemCode, ResCode
  ITEM_CODE U: ItemCode
Fields (name type(len) description [values] ->parent table):
  ResCode nVarChar(50) Internal Resource ID ->ORSC
  ItemCode nVarChar(50) Item Code ->OITM
  LogInstanc Int(11) Log Instance default=0
