<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# NNM5 - Document Numbering - Removed Serial Numbers
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Series, ObjectCode, DocSubType, Number
  SERIES: Series, Number
Fields (name type(len) description [values] ->parent table):
  ObjectCode nVarChar(20) Document
  Series Int(11) Series
  DocSubType nVarChar(2) Document Subtype default=--
  Number Int(11) Number
