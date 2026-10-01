<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ACR5 - BP Payment Dates - History
Module: Business Partners | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CardCode, PmntDate, LogInstanc
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code ->OCRD
  PmntDate nVarChar(2) Payment Date
  LogInstanc Int(11) Log Instance default=0
