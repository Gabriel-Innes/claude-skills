<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# GDP2 - General Data Protection Wizard - Natural Persons
Module: Reports | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  NATOBJ_KEY U: AbsEntry, NatObjType, NatObjArr, NatObjKey1, NatObjKey2
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OGDP
  LineNum Int(6) Line
  NatObjType nVarChar(20) Natural Person Object Type
  NatObjArr Int(11) Natural Person Object Array
  NatObjKey1 nVarChar(20) Natural Person Object Key
  NatObjKey2 nVarChar(20) Natural Person Object Subkey
  Result Int(11) Result
  ErrorStr nVarChar(254) Error String
