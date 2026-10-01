<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OTRX - Transformation Documents
Module: Reports | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CODE U: Code
Fields (name type(len) description [values] ->parent table):
  AbsEntry Identity(11) Internal Number
  Code nVarChar(20) Code
  Descr nVarChar(250) Description
  Type nVarChar(8) Type default=XSLT [XSLT=XSLT Document]
  Data Text(16) Data
