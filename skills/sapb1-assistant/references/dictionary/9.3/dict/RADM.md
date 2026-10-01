<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RADM - Resource Administration
Module: General | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ResVersion
Fields (name type(len) description [values] ->parent table):
  DevGroup nVarChar(3) Development Group
  ResVersion nVarChar(5) Resource Version
  ReleaseDte Date(8) Rsleade Date
  RelFrzDate Date(8) GUI Freeze Date for Release
  Sp1Date Date(8) SP1 Date
  Sp1FrzDate Date(8) GUI Freeze Date for SP1
  Sp2Date Date(8) SP2 Date
  Sp2FrzDate Date(8) GUI Freeze Date for SP2
  DbLocked Int(11) Is DB Locked for Edit [0=Not Locked, 1=GUI Freeze (Translations), 2=Read Only, 3=Full Lock]
  DbVersion nVarChar(10) Resource DB Version
  CreateDate Date(8) Creation Date of DB
  CreateTime Int(11) Creation Time of DB default=0
  CanLogin VarChar(1) Can Users Login
  ValidPath nVarChar(100) Valid Path For Running
  P4Path nVarChar(100) P4 Version Path
  MDVersion Int(11) Metadata Version default=-1
  VerScpDate Date(8) Version Scope Date
  VerScpTime Int(11) Version Scope Time default=0
  TransVer nVarChar(10) Translation Version
  Flags nVarChar(100) Resource flags
  WpFileName nVarChar(100) Wallpaper File Name default=NotSet
