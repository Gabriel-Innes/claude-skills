<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ATSC - CST Code for Nota Fiscal
Module: Administration | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID, LogInstanc
  CST_CODE U: CODE, Category, LogInstanc
Fields (name type(len) description [values] ->parent table):
  ID Int(11) CST Internal Key
  CODE nVarChar(20) CST Code Incoming
  Situation Text(16) Description Incoming
  Locked VarChar(1) Locked default=N [Y=, N=]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Auto Incr., D=Data Doc., P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Category Int(6) Tax Category default=-6 ->ONFT
  CodeOut nVarChar(20) CST Code Outgoing
  OutDesc Text(16) Description Outgoing
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
