<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OAT4 - Blanket Agreement - Recurring Transactions
Module: Business Partners | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AgrNo, RcpEntry
Fields (name type(len) description [values] ->parent table):
  AgrNo Int(11) Agreement No. ->OOAT
  RcpEntry Int(11) Recurring Template Entry ->ORCP
  LogInstanc Int(11) Log Instance default=0
