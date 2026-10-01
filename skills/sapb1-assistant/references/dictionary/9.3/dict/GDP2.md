<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# GDP2 - General Data Protection Wizard - Natural Persons
Module: Reports | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, AbsEntry
  NATOBJ_KEY U: NatObjKey2, NatObjKey1, NatObjArr, NatObjType, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OGDP
  LineNum Int(6) Line
  NatObjType nVarChar(20) Natural Person Object Type
  NatObjArr Int(11) Natural Person Object Array
  NatObjKey1 nVarChar(20) Natural Person Object Key
  NatObjKey2 nVarChar(20) Natural Person Object Subkey
  Result Int(11) Result
  ErrorStr nVarChar(254) Error String
