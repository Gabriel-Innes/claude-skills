<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# NFN2 - NFSeq User Default
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SeqCode, UserSign, DocSubType, ObjectCode
  USER: UserSign
Fields (name type(len) description [values] ->parent table):
  ObjectCode nVarChar(20) Document ->ONFN
  UserSign Int(6) User Signature ->OUSR
  SeqCode Int(6) Sequence Code
  DocSubType nVarChar(2) Document Sub-Type default=--
