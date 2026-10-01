<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CUVV - User Validations
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineNum, IndexID
Fields (name type(len) description [values] ->parent table):
  IndexID Int(11) Index ->CSHS
  Value nVarChar(254) Field Value
  LineNum Int(11) Row Number
