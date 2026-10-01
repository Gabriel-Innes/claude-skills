<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SXROB - XLR Objects
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: objid
Fields (name type(len) description [values] ->parent table):
  objid Int(11) objid
  classid Int(11) classid default=0
  name nVarChar(50) name
  descriptio nVarChar(254) description
  created Date(8) created
  lastmodifi Date(8) lastmodified
  access nVarChar(50) access
  searchstri nVarChar(200) searchstring
