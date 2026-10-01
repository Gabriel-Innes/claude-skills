<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ODAB - Dashboard
Module: General | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CODE U: DashbdCode, PackEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  PackEntry Int(11) Package Entry ->OWPK
  DashbdCode nVarChar(32) Dashboard Code
  DashbdName nVarChar(100) Dashboard Name
  DashbdPath nVarChar(254) Dashboard Path
  Note Text(16) Dashboard Description
  Status VarChar(1) Dashboard Status default=A [I=Inactive, A=Active]
  JobFlag VarChar(1) Use Schedule Job Flag default=N [Y=Yes, N=No]
  JobType VarChar(1) Schedule Job Type default=R [R=Real Time, P=Periodic]
  JobSetting nVarChar(100) Schedule Job Time Setting
  RenewDate Date(8) Latest Renew Date
  RenewTime Int(6) Latest Renew Time
  ProcName nVarChar(100) Procedure Name
  JobName nVarChar(100) Schedule Job Name
