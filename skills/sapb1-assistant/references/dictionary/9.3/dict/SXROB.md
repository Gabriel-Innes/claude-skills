<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SXROB - XLR Objects
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
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
