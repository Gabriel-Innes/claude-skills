<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RPRS - Print Sequence Definition
Module: Reports | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SeqID
  OBJECT_ID: ObjectID
Fields (name type(len) description [values] ->parent table):
  SeqID Int(11) Sequence ID
  SeqName nVarChar(254) Sequence Name
  LineNum Int(6) Visual Order
  ObjectID Int(11) Document Object ID
  SubDocType Int(6) Document Subtype
