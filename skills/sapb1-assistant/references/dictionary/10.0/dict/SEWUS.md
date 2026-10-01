<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SEWUS - 
Module: General | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Absolute Entry
  CompanyNam nVarChar(100) CompanyName
  SmpTableId nVarChar(3) Smp Table ID
  EwaSentDat nVarChar(10) EWA Sent Date
  CustNumber VarChar(1) Customer Number
  CompDbName nVarChar(100) Company DB Name
  EwaUserCod nVarChar(16) Ewa User Code
  EwaUserNam nVarChar(16) Ewa User Name
  EwaUserSup VarChar(1) Ewa Is super user default=0 [1=Yes, 0=No]
