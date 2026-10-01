<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# GDP3 - General Data Protection Wizard - Processed Documents
Module: Reports | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineNum, AbsEntry
  NATOBJ_KEY U: RefObjKey2, RefObjKey1, RefObjType, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OGDP
  LineNum Int(6) Line
  RefObjType nVarChar(20) Referenced Object Type
  RefObjKey1 nVarChar(20) Referenced Object Key
  RefObjKey2 nVarChar(20) Referenced Object Subkey
