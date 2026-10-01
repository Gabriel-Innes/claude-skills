<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# DAR3 - Data Archive - Handwritten Documents
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ArcEntry, Line_ID
  DOC_NUM: DocType, DocSubType, DocNum, PIndicator
Fields (name type(len) description [values] ->parent table):
  ArcEntry Int(11) Data Archive Entry
  Line_ID Int(11) Row Number
  DocType nVarChar(20) Document Type
  DocAbs Int(11) Doc. No.
  DocNum Int(11) Document Number
  DocSubType nVarChar(2) Document Sub-Type default=--
  PIndicator nVarChar(10) Period Indicator default=' '
