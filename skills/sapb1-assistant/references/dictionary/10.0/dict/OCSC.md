<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OCSC - Crystal Server Configuration
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) CSC Abs. Entry
  Name nVarChar(100) Server Name
  User nVarChar(30) Logon User Code
  Password nVarChar(254) Logon User Password
  URL nVarChar(200) URL
  IsDefault VarChar(1) Is Default default=N [Y=Yes, N=No]
  Port nVarChar(20) Port default=8080
