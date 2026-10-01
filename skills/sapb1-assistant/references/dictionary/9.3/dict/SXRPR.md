<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SXRPR - XLR Properties
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: propid
Fields (name type(len) description [values] ->parent table):
  propid Identity(11) propid
  objid Int(11) objid
  propdefid Int(11) propdefid
  ivalue Int(11) ivalue
  fvalue Num(19,6) fvalue
  cvalue Text(16) cvalue
