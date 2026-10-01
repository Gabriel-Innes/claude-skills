<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# WOR2V - Production Order - Base
Module: Inventory and Production | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BaseEntry, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal Number ->OWOR
  BaseEntry Int(11) Production Order Base Entry ->ORDR
  BaseNum Int(11) Production Order Base Number
  CardCode nVarChar(15) Customer Code
  PostDate nVarChar(8) Posting Date
  DueDate nVarChar(8) Due Date
  DocTotal Num(19,6) Document Total
  Remark nVarChar(254) Document Remarks
  DocCur nVarChar(3) Document Currency
