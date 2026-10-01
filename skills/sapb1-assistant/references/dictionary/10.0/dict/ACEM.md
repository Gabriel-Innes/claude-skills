<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ACEM - Cost Element
Module: Sales Opportunities | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CemCode, LogInstanc
Fields (name type(len) description [values] ->parent table):
  CemCode nVarChar(20) Cost Element Code
  CemDescr nVarChar(50) Cost Element Description
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
  ObjType nVarChar(20) Object Type default=256000005 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Date of Update
  CreateTS Int(11) Creatn Time - Incl. Secs
  UpdateTS Int(11) Update Full Time
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
