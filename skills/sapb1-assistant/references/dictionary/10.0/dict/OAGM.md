<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OAGM - Arguments for Integration Framework
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, ObjType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number of Document
  ObjType nVarChar(20) Object Type
  XmlGen Text(16) XML File Generated
  XmlRet Text(16) XML File Returned
  Message nVarChar(254) Message
