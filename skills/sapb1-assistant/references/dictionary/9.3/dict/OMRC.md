<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OMRC - Manufacturers
Module: Inventory and Production | 4 columns | ObjType: 43
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: FirmCode
  GROUP_NAME U: FirmName
Fields (name type(len) description [values] ->parent table):
  FirmCode Int(6) Code
  FirmName nVarChar(30) Manufacturer Name
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
