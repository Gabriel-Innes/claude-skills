<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SXRPD - XLR Property Definitions
Module: General | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: propdefid
Fields (name type(len) description [values] ->parent table):
  propdefid Int(11) propdefid
  classid Int(11) classid
  seqno Int(11) seqno default=0
  name nVarChar(50) name
  descriptio nVarChar(254) description
  type Int(11) type default=0
  minoccurs Int(11) minoccurs default=0
  maxoccurs Int(11) maxoccurs default=999999
  classrefid Int(11) classrefid default=0
  enumid Int(11) enumid default=0 [0=]
