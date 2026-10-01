<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ATSC - CST Code for Nota Fiscal
Module: Administration | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, ID
  CST_CODE U: LogInstanc, Category, CODE
Fields (name type(len) description [values] ->parent table):
  ID Int(11) CST Internal Key
  CODE nVarChar(20) CST Code Incoming
  Situation Text(16) Description Incoming
  Locked VarChar(1) Locked default=N [Y=, N=]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=OB Server, A=Auto Incr., D=Data Doc., P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Category Int(6) Tax Category default=-6 ->ONFT
  CodeOut nVarChar(20) CST Code Outgoing
  OutDesc Text(16) Description Outgoing
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
