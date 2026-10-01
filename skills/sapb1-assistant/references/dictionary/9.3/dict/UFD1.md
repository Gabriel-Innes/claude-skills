<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# UFD1 - User Fields - Values Definitions
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: IndexID, FieldID, TableID
Fields (name type(len) description [values] ->parent table):
  TableID nVarChar(21) Table
  FieldID Int(6) Field
  IndexID Int(6) Index
  FldValue nVarChar(254) Value
  Descr nVarChar(254) Description
  FldDate Date(8) Date Value
