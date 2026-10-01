<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# NNM1 - Documents Numbering - Series
Module: Administration | 28 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Series
  SER_NAME U: SeriesType, SeriesName, DocSubType, ObjectCode
Fields (name type(len) description [values] ->parent table):
  ObjectCode nVarChar(20) Document ->ONNM
  Series Int(11) Series default=0
  SeriesName nVarChar(8) Series Name
  InitialNum Int(11) Initial Number default=0
  NextNumber Int(11) Next Number for Use default=0
  LastNum Int(11) Last Number Allowed
  BeginStr nVarChar(20) Prefix String
  EndStr nVarChar(20) Suffix String
  Remark nVarChar(50) Remarks
  GroupCode Int(6) Group default=1 [1=Series Group 1, 2=Series Group 2, 3=Series Group 3, 4=Series Group 4, 5=Series Group 5, 6=Series Group 6, 7=Series Group 7, 8=Series Group 8, 9=Series Group 9, 10=Series Group 10]
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  YearTransf VarChar(1) Year-End Closing default=N [Y=Yes, N=No]
  Indicator nVarChar(10) Period Indicator ->OPID
  Template nVarChar(20) Template
  NumSize Int(11) Numeric Size
  FolioPref nVarChar(4) Folio Prefix String
  NextFolio Int(11) Next Folio Number
  DocSubType nVarChar(2) Document Sub-Type default=--
  DefESeries Int(6) Default Electronic Series default=0
  IsDigSerie VarChar(1) Is Digital Series default=N [Y=Yes, N=No]
  SeriesType VarChar(1) Series Type default=D [D=Document, B=Business Partner, I=Item, R=Resource, W=Witholding Certificates]
  IsManual VarChar(1) Is Manual Series default=N [Y=Yes, N=No]
  BPLId Int(11) Assigned Branch ->OBPL
  IsForCncl VarChar(1) Is Series for Cancelation default=N [Y=Yes, N=No]
  AtDocType nVarChar(2) AT Document Type [GT=GT, GA=GA, GD=GD, GR=GR, GC=GC, FT=FT, FS=FS, NC=NC, ND=ND, FR=FR]
  IsElAuth VarChar(1) Elec. Authorization Code default=N [Y=Yes, N=No]
  CoAccount VarChar(1) Cost Account Only default=N [Y=Yes, N=No]
  GenPassprt VarChar(1) Do Generate SAP Passport default=N [Y=Yes, N=No]
