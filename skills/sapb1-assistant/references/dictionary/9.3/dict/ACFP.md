<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ACFP - CFOP for Nota Fiscal
Module: Administration | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, ID
  CFOP_CODE U: LogInstanc, Code
Fields (name type(len) description [values] ->parent table):
  ID Int(11) CFOP ID
  Code nVarChar(6) CFOP Code
  Descrip Text(16) Description
  App Text(16) Application
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=OB Server, A=Auto Incr., D=Data Doc., P=Partner Implementation]
  UserSign nVarChar(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
