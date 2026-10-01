<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# NNM2 - Series Default
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjectCode, DocSubType, UserSign
  USER: UserSign
Fields (name type(len) description [values] ->parent table):
  ObjectCode nVarChar(20) Document
  UserSign Int(6) User Signature ->OUSR
  Series Int(11) Series
  DocSubType nVarChar(2) Document Sub-Type default=--
