<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SEWBU - SEWBU
Module: General | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) AbsEntry
  CompanyNam nVarChar(100) CompanyName
  SmpTableId nVarChar(3) Smp Table ID
  EwaSentDat nVarChar(10) EWA Sent Date
  CustNumber VarChar(1) Customer Number
  CompDbName nVarChar(100) Company DB Name
  DateFrom nVarChar(10) Bck Date From
  StartDate nVarChar(10) Bck start date
  FinishDate nVarChar(10) Bck finish date
  Size Int(11) Bck size
  LogSize Int(11) Bck Log Size
  DbVersion nVarChar(32) Db Version
  CodePage Int(11) Code Page
