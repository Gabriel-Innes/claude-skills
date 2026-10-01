<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CUMF - Folder
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: FolderId, UserSign
Fields (name type(len) description [values] ->parent table):
  FolderId Int(11) Folder Key default=0
  FolderName nVarChar(50) Folder Name
  SortNum Int(11) Sort Number
  UserSign Int(6) User Signature ->OUSR
  FatherId Int(11) Parent Key default=-1
