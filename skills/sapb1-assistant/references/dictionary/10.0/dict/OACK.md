<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OACK - Acknowledge Number
Module: Finance | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  LOC_QUART U: FinYear, Quarter, Location
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  FinYear Int(11) Financial Year ->OFYM
  Quarter VarChar(1) Quarter [1=Quarter 1, 2=Quarter 2, 3=Quarter 3, 4=Quarter 4]
  AckNum nVarChar(100) Acknowledgment No.
  Location Int(11) Location ->OLCT
