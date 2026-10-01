<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OALT - Alerts Template
Module: Administration | 24 columns | ObjType: 80
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
  ACTIVE: Active
  NAME: Name
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Internal Number
  Name nVarChar(254) Name
  Type VarChar(1) Type default=U [S=System Alert, U=User Alert]
  Priority VarChar(1) Priority default=1 [0=Low, 1=Normal, 2=High]
  Active VarChar(1) Active Alert default=N [Y=Yes, N=No]
  NumOfParam Int(11) No. of Parameters
  ParamData Text(16) Parameters
  Params Text(16) Parameters
  NumOfDocs Int(11) Documents Numbers
  DocsData Text(16) Documents
  Docs Text(16) Documents
  UserText Text(16) MEMO
  QueryId Int(11) Query
  FrqncyType VarChar(1) Frequency Type default=H [S=Minutes, H=Hours, D=Days, W=Weeks, M=Months]
  FrqncyIntr Int(11) Frequency default=1
  ExecDaY Int(6) Day of Execution default=1
  ExecTime Int(11) Execution Hour default=800
  LastDate Date(8) Execution Date
  LastTIME Int(6) Execution Time
  NextDate Date(8) Next Date
  NextTime Int(6) Next Hour
  UserSign Int(6) User Signature ->OUSR
  History VarChar(1) Save History default=N [Y=Yes, N=No]
  QCategory Int(11) Query Category ->OUQR
