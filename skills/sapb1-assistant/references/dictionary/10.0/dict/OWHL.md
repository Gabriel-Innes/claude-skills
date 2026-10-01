<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OWHL - Register of VAT Payers
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ImportDate
Fields (name type(len) description [values] ->parent table):
  ImportDate Date(8) Import Date
  HashCount Int(11) Hash Count
  Comment nVarChar(254) Comments
  NextDate Date(8) Next Date
