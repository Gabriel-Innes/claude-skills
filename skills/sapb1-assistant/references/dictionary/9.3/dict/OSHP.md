<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OSHP - Delivery Types
Module: Administration | 5 columns | ObjType: 49
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TrnspCode
  NAME U: TrnspName
Fields (name type(len) description [values] ->parent table):
  TrnspCode Int(6) Code
  TrnspName nVarChar(40) Name
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  WebSite nVarChar(50) Web Site
