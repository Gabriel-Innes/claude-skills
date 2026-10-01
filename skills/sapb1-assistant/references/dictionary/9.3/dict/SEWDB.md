<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SEWDB - SEWDB
Module: General | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry nVarChar(8) Absolute Entry
  SmpTableId nVarChar(3) Smp Table ID
  CollectDat nVarChar(10) DB Size Collect Date
  CompDbName nVarChar(100) Company DB Name
  DbPath nVarChar(254) Db Path
  PrevDbSize nVarChar(32) Prev Db Size
  DbSize nVarChar(32) Db Size
  TranLogSiz nVarChar(32) Transaction Log Size
  TranLogPat nVarChar(254) Transaction Log Path
  TotalDbSiz nVarChar(16) Total Db Size
  FreDskSpac nVarChar(16) Free Disk Space
  MaxDbSize nVarChar(16) Max Db Size
  MaxLogSize nVarChar(16) Max Log Size
