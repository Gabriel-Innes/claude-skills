<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OLNG - User Language Table
Module: Administration | 7 columns | ObjType: 223
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
  SHORT_NAME U: ShortName
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Code
  ShortName nVarChar(3) Language Short Name
  Name nVarChar(30) Language
  SysLang Int(11) Related System Language
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
