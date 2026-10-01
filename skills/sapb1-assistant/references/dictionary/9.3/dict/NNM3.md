<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# NNM3 - Documents Numbering -Belgium Series
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Series, DocSubType, ObjectCode
  SERIES: Series
Fields (name type(len) description [values] ->parent table):
  ObjectCode nVarChar(20) Document ->ONNM
  Series Int(11) Series default=0
  DocSubType nVarChar(2) VAT Code for Tax Invoice Rpt default=--
