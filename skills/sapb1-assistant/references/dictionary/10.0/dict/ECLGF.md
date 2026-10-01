<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ECLGF - 
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id, FileName
Fields (name type(len) description [values] ->parent table):
  Id nVarChar(100) Transaction Id
  FileName nVarChar(254) The configuration file name
  FileHash nVarChar(100) The file hash code
  XmlFile Text(16) The file saved as Xml
