<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# RSAT - RecordSet Audit Table
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: QueryID
Fields (name type(len) description [values] ->parent table):
  QueryID Identity(11) Query ID
  QueryDate Int(11) Date of Query
  QueryTime Int(11) Timestamp of Query
  QueryDetls Text(16) Query Details
