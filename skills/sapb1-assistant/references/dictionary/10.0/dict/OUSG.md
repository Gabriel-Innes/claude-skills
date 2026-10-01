<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OUSG - Usage of Nota Fiscal
Module: Administration | 17 columns | ObjType: 260
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
Fields (name type(len) description [values] ->parent table):
  ID Int(11) Usage ID
  Usage nVarChar(20) Usage
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Auto Incr., D=Data Doc., P=Partner Implementation, T=Year Transfer]
  UserSign nVarChar(6) User Signature ->OUSR
  PostTax Int(6) Post Tax in Price to Stock default=1 [1=Yes, 0=No]
  TaxOnly VarChar(1) Tax Only default=N [Y=Yes, N=No]
  CFOPIIS nVarChar(6) CFOP Incoming In-State ->OCFP
  CFOPIOS nVarChar(6) CFOP Incoming Out-State ->OCFP
  CFOPII nVarChar(6) CFOP Incoming Import ->OCFP
  CFOPOIS nVarChar(6) CFOP Outgoing In-State ->OCFP
  CFOPOOS nVarChar(6) CFOP Outgoing Out-State ->OCFP
  CFOPOE nVarChar(6) CFOP Outgoing Export ->OCFP
  Descr nVarChar(100) Usage Description
  FreeChrgBP VarChar(1) Free of Charge (BP) default=N [Y=Yes, N=No]
  ThirdParty VarChar(1) Third Party default=N [Y=Yes, N=No]
  Adjustment VarChar(1) Adjustment default=N [Y=Yes, N=No]
