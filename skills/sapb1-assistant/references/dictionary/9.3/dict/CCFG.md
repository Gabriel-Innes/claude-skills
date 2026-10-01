<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CCFG - Company Configuration
Module: General | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ConfigEntr
Fields (name type(len) description [values] ->parent table):
  ConfigEntr Int(11) Internal Configuration ID
  ConfigName nVarChar(250) Configuration File Name
  ConfigDate Date(8) Configuration File Create Date
  ConfigTime Int(6) Configuration File Create Time
  UserCode Int(11) Configuration Created By
  CreateBy Int(11) Created from Menu: [0=Express Configuration Wizard, 1=Configuration Management]
  ServerName nVarChar(250) Configuration Saved on Server:
  CompanyDB nVarChar(250) Company Database
  Internal VarChar(1) Internal default=N [N=No, Y=Yes]
