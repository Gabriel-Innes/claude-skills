<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OEGP - E-Mail Group
Module: Business Partners | 6 columns | ObjType: 234000004
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: EmlGrpCode
Fields (name type(len) description [values] ->parent table):
  EmlGrpCode nVarChar(20) E-Mail Group Code
  EmlGrpName nVarChar(100) E-Mail Group Name
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(11) User Signature ->OUSR
  LogInstanc Int(11) Log Instance
