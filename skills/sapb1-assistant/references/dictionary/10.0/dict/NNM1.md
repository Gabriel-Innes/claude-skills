<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# NNM1 - Documents Numbering - Series
Module: Administration | 39 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Series
  SER_NAME U: ObjectCode, DocSubType, SeriesName, SeriesType
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
  GroupCode Int(6) Group default=1 [1=Series Group 1, 2=Series Group 2, 3=Series Group 3, 4=Series Group 4, 5=Series Group 5, 6=Series Group 6, 7=Series Group 7, 8=Series Group 8, 9=Series Group 9, 10=Series Group 10, 11=Series Group 11, 12=Series Group 12, 13=Series Group 13, 14=Series Group 14, 15=Series Group 15, 16=Series Group 16, 17=Series Group 17, 18=Series Group 18, 19=Series Group 19, 20=Series Group 20, 21=Series Group 21, 22=Series Group 22, 23=Series Group 23, 24=Series Group 24, 25=Series Group 25, 26=Series Group 26, 27=Series Group 27, 28=Series Group 28, 29=Series Group 29, 30=Series Group 30]
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  YearTransf VarChar(1) Year-End Closing default=N [Y=Yes, N=No]
  Indicator nVarChar(10) Period Indicator default=' ' ->OPID
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
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Date of Update
  logInstanc Int(11) Log Instance - History
  PInvType Int(11) Abs Type of Positive Value Invoice ->OEIT
  NInvType Int(11) Abs Type of Negative Value Invoice ->OEIT
  AssignedID nVarChar(70) Assigned ID
  Action VarChar(1) Action [R=Report, C=Cancel, F=Finalize]
  Status VarChar(1) Status [R=Reported, C=Canceled, F=Finalized]
  Phase VarChar(1) Phase [T=To Be Processed, I=In Process, O=OK, E=Error]
