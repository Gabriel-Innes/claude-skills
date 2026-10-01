<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OPRT - Partners
Module: Business Partners | 8 columns | ObjType: 108
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PrtId
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  PrtId Int(11) Sequence No.
  Name nVarChar(15) Name
  RelatnType nVarChar(20) Relationship Type
  RelatCard nVarChar(15) Related BP ->OCRD
  Memo nVarChar(50) Details
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  DefaultORL Int(11) Default Relationship ->OORL
