<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# EML1 - E-mail Log - Rows
Module: Reports | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Line, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Absolute entry
  Line Int(11) Row Number
  ObjectID Int(11) Document Object ID
  DocDate Date(8) Posting Date
  DocEntry Int(11) Doc Internal Number
