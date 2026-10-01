<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AWD4 - WTax Codes Details for Item
Module: Business Partners | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineId, LogInstanc
  ITEM U: WTCode, ItemCode, DateFrom, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OWTD
  LineId Int(11) Row Number
  WTCode nVarChar(4) WTax Code
  ItemCode nVarChar(50) Item No. ->OITM
  DateFrom Date(8) Effective Date From
  DateTo Date(8) Effective Date To
  DataSource VarChar(1) Data Source default=N [N=Unknown, M=Import, O=DI API, S=Service Layer, W=Web Client, P=Partner Implementation]
  UpdateDate Date(8) Date of Update
  LogInstanc Int(11) Log Instance default=0
