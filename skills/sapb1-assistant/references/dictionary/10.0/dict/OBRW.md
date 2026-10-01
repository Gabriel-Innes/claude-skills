<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OBRW - Browser Widget
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Name nVarChar(100) Browser Widget Name
  Type Int(6) Type default=0 [0=Web Site, 1=App]
  Url nVarChar(254) Web Site or Extreme Application URL
  App nVarChar(100) Extreme Application Name
  Title nVarChar(254) Title
  ShowWebTil VarChar(1) Display Web Page Title default=N [Y=Yes, N=No]
  Size nVarChar(15) Widget Size
