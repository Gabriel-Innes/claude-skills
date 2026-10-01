<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ORCI - Recipient List
Module: Service | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
  NAME: Name
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Code
  Name nVarChar(30) Name
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
  IsMultiple VarChar(1) Is Mulitple default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  UserSign2 nVarChar(6) Updating User ->OUSR
