<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SXRRE - XLR Relations
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: relid
  second U: objidfrom, propdefid, seqno
Fields (name type(len) description [values] ->parent table):
  relid Identity(11) relid
  objidfrom Int(11) objidfrom default=0
  propdefid Int(11) propdefid default=0
  seqno Int(11) seqno default=0
  objidto Int(11) objidto default=0
