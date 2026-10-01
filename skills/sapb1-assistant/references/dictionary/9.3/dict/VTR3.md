<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# VTR3 - Series Filter
Module: Finance | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjectCode, SeriesCode, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ObjectCode nVarChar(15) Object Code
  SeriesCode Int(11) Series Code
