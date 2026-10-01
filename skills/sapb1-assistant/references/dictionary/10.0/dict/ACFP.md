<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ACFP - CFOP for Nota Fiscal
Module: Administration | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID, LogInstanc
  CFOP_CODE U: Code, LogInstanc
Fields (name type(len) description [values] ->parent table):
  ID Int(11) CFOP ID
  Code nVarChar(6) CFOP Code
  Descrip Text(16) Description
  App Text(16) Application
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Auto Incr., D=Data Doc., P=Partner Implementation]
  UserSign nVarChar(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
