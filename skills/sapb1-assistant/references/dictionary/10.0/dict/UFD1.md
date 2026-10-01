<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# UFD1 - User Fields - Values Definitions
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TableID, FieldID, IndexID
Fields (name type(len) description [values] ->parent table):
  TableID nVarChar(21) Table
  FieldID Int(6) Field
  IndexID Int(6) Index
  FldValue nVarChar(254) Value
  Descr nVarChar(254) Description
  FldDate Date(8) Date Value
