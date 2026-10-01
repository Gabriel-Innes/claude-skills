<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OBDC - B1i DI Configuration
Module: Administration | 16 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Code
  Server nVarChar(254) Server
  License nVarChar(254) License Server
  Company nVarChar(128) Company
  DBType Int(11) DB Type
  DBUser nVarChar(254) DB User
  DBPassword nVarChar(254) DB Password
  Username nVarChar(254) User Name
  UPassword nVarChar(254) User Password
  DBTrusted VarChar(1) DB Trusted
  JCOPath nVarChar(254) Java Connector Path
  Language Int(11) Language
  AddOnIF nVarChar(254) Add-On Identifier
  StateFder nVarChar(254) Bank Statement Folder
  FormatFder nVarChar(254) Bank Format Folder
  FileFolder nVarChar(254) Bank File Folder
