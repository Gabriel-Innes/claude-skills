<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ACR13 - Business Partners Currency - History
Module: Business Partners | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CardCode, CurrCode, LogInstanc
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code ->OCRD
  CurrCode nVarChar(3) Currency Code ->OCRN
  INCLUDE VarChar(1) Include default=Y [Y=Yes, N=No]
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  LogInstanc Int(11) Log Instance default=0
