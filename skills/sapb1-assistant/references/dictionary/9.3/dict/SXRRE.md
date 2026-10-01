<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SXRRE - XLR Relations
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: relid
  second U: seqno, propdefid, objidfrom
Fields (name type(len) description [values] ->parent table):
  relid Identity(11) relid
  objidfrom Int(11) objidfrom default=0
  propdefid Int(11) propdefid default=0
  seqno Int(11) seqno default=0
  objidto Int(11) objidto default=0
