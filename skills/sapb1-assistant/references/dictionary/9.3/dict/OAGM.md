<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OAGM - Arguments for Integration Framework
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ObjType, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number of Document
  ObjType nVarChar(20) Object Type
  XmlGen Text(16) XML File Generated
  XmlRet Text(16) XML File Returned
