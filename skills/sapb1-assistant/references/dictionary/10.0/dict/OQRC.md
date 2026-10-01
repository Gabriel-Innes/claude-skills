<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OQRC - QR Code
Module: Administration | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SECONDARY U: SrcObjType, SrcObjAbs, FieldName
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  FileContnt Text(16) QR Code Image Content
  SrcObjType Int(11) Source Object Type
  SrcObjAbs nVarChar(20) Source Object Internal ID
  FieldName nVarChar(50) Field Name
  ExpAfter Int(6) Expire after defined days
  CreateDate Date(8) Creation Date
  CreateTS Int(11) Creation Time - Incl. Secs
  UpdateDate Date(8) Update Date
  UpdateTS Int(11) Update Time - Incl. Secs
