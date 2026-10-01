<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ACR4 - Allowed WTax Codes for BP - History
Module: Business Partners | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CardCode, WTCode, LogInstanc
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code
  WTCode nVarChar(4) WTax Code
  LogInstanc Int(11) Log Instance default=0
