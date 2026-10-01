<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# GDP3 - General Data Protection Wizard - Processed Documents
Module: Reports | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  NATOBJ_KEY U: AbsEntry, RefObjType, RefObjKey1, RefObjKey2
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OGDP
  LineNum Int(6) Line
  RefObjType nVarChar(20) Referenced Object Type
  RefObjKey1 nVarChar(20) Referenced Object Key
  RefObjKey2 nVarChar(20) Referenced Object Subkey
