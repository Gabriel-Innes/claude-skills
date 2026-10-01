<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CUMF - Folder
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: UserSign, FolderId
Fields (name type(len) description [values] ->parent table):
  FolderId Int(11) Folder Key default=0
  FolderName nVarChar(50) Folder Name
  SortNum Int(11) Sort Number
  UserSign Int(6) User Signature ->OUSR
  FatherId Int(11) Parent Key default=-1
