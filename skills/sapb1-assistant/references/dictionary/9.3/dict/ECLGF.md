<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ECLGF - ECLGF
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: FileName, Id
Fields (name type(len) description [values] ->parent table):
  Id nVarChar(100) Transaction Id
  FileName nVarChar(254) The configuration file name
  FileHash nVarChar(100) The file hash code
  XmlFile Text(16) The file saved as Xml
