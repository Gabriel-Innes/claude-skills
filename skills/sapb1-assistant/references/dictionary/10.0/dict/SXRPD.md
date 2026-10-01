<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SXRPD - XLR Property Definitions
Module: General | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: propdefid
Fields (name type(len) description [values] ->parent table):
  propdefid Int(11) propdefid
  classid Int(11) classid
  seqno Int(11) seqno default=0
  name nVarChar(50) name
  category nVarChar(50) category default='General'
  descriptio nVarChar(254) description
  type Int(11) type default=0
  minoccurs Int(11) minoccurs default=0
  maxoccurs Int(11) maxoccurs default=999999
  classrefid Int(11) classrefid default=0
  enumid Int(11) enumid default=0 [0=]
