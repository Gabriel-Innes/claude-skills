<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# NFN1 - Not a Fiscal Sequence
Module: Administration | 23 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SeqCode, DocSubType, ObjectCode
  S_NAME U: SeqName, BPLId, DocSubType, ObjectCode
Fields (name type(len) description [values] ->parent table):
  ObjectCode nVarChar(20) Document ->ONFN
  SeqCode Int(6) Seq. Code default=0
  SeqName nVarChar(8) Seq. Name
  InitialNum Int(11) Initial Number default=0
  NextNum Int(11) Next Number for Use default=0
  LastNum Int(11) Last Number Allowed
  SeriesStr nVarChar(3) Series String
  SubStr nVarChar(3) Subseries String
  Remark nVarChar(50) Remarks
  GroupCode Int(6) Group default=1 [1=, 2=, 3=, 4=, 5=, 6=, 7=, 8=, 9=, 10=]
  Locked VarChar(1) Locked default=N [Y=, N=]
  YearTransf VarChar(1) Year-End Closing default=N [Y=, N=]
  Indicator nVarChar(10) Period Indicator [=] ->OPID
  Template nVarChar(20) Template
  NumSize Int(11) Numeric Size
  Prefix nVarChar(8) Prefix
  Suffix nVarChar(8) Suffix
  DocSubType nVarChar(2) Document Sub-Type default=--
  Model nVarChar(6) Nota Fiscal Model default=0 ->ONFM
  Location Int(11) Location Code ->OLCT
  BPLId Int(11) Assigned Branch default=0 ->OBPL
  IsDigital VarChar(1) Digital Series default=N [Y=Yes, N=No]
  EnvTypeNFe Int(11) Environment Type NF-e default=-1 ->OBNI
