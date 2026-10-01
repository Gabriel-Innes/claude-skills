<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OFYM - Financial Year Master
Module: Finance | 7 columns | ObjType: 10000073
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  CODE U: Code
  ASSESSYEAR U: AssessYear
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Code nVarChar(6) Code
  Descr nVarChar(30) Description
  StartDate Date(8) Start Date
  EndDate Date(8) End Date
  AssessYear nVarChar(6) Assessment Year
  TcsAcmBase VarChar(1) TCS Accumulation Base default=I [I=Accumulation Based on Invoice, P=Accumulation Based on Payment]
