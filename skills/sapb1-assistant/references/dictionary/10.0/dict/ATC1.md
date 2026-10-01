<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ATC1 - Attachments - Rows
Module: Administration | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, Line
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
  CopyToTrgt VarChar(1) Copy to Target Document default=N [Y=Yes, N=No]
  CopyToProd VarChar(1) Copy to Production Order default=N [Y=Yes, N=No]
