<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# RPRS - Print Sequence Definition
Module: Reports | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SeqID
  OBJECT_ID: ObjectID
Fields (name type(len) description [values] ->parent table):
  SeqID Int(11) Sequence ID
  SeqName nVarChar(254) Sequence Name
  LineNum Int(6) Visual Order
  ObjectID Int(11) Document Object ID
  SubDocType Int(6) Document Subtype
