<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ORTL - Resource Transaction Log
Module: Inventory and Production | 24 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogEntry
Fields (name type(len) description [values] ->parent table):
  LogEntry Int(11) Log Entry ID
  ResCode nVarChar(50) Resource Code ->ORSC
  DocType Int(11) Transact. Type
  DocEntry Int(11) Document Internal ID
  DocLine Int(11) Doc. Row Number
  BaseType Int(11) Base Document Type
  BaseEntry Int(11) Base Document Internal ID
  BaseLine Int(11) Base Document Row Number
  ActionType Int(11) Action Type default=0 [0=RESOURCE_TRANSACTION_UNKNOWN, 1=RESOURCE_TRANSACTION_IN, 2=RESOURCE_TRANSACTION_OUT]
  LocType Int(6) Location Type
  LocCode nVarChar(8) Location Code
  VersionNum nVarChar(11) Version Number
  PostDate Date(8) Posting Date
  CreateDate Date(8) Creation Date
  CreateTime Int(6) Creation Time
  DocQty Num(19,6) Doc. Quantity
  Price Num(19,6) Price
  LineTotal Num(19,6) Row Total
  OpenQty Num(19,6) Open Quantity
  DocNum nVarChar(11) Document Number
  BaseDocNum nVarChar(11) Base Document Number
  StgSeqNum Int(11) Stage Sequence Number
  StgEntry Int(11) Stage Entry
  StgDesc nVarChar(100) Stage Description
