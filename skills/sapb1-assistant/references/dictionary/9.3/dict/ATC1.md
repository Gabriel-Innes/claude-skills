<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ATC1 - Attachments - Rows
Module: Administration | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Line, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Absolute entry
  Line Int(11) Row Number
  srcPath Text(16) Source Path
  trgtPath Text(16) Target Path
  FileName nVarChar(254) File Name
  FileExt nVarChar(8) File Extension
  Date Date(8) Attachment Date
  UsrID Int(11) User ID
  Copied VarChar(1) Copied default=N [Y=Yes, N=No]
  Override VarChar(1) Override file default=N [Y=Yes, N=No]
  subPath nVarChar(254) Subpath
  FreeText nVarChar(100) Free Text
