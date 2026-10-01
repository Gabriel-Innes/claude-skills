<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OPVL - Lender - Pelecard
Module: Administration | 5 columns | ObjType: 115
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
  CONSOL_NUM U: ConsolNum
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Internal Number
  Name nVarChar(50) Name
  ConsolNum nVarChar(2) Vendor Code
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
