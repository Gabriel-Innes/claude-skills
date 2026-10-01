<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# NNM3 - Documents Numbering -Belgium Series
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjectCode, DocSubType, Series
  SERIES: Series
Fields (name type(len) description [values] ->parent table):
  ObjectCode nVarChar(20) Document ->ONNM
  Series Int(11) Series default=0
  DocSubType nVarChar(2) VAT Code for Tax Invoice Rpt default=--
  logInstanc Int(11) Log Instance - History
