<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ORCN - Retail Chains
Module: Inventory and Production | 11 columns | ObjType: 79
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ChainCode
  NAME U: ChainName
Fields (name type(len) description [values] ->parent table):
  ChainCode Int(11) Internal Number
  ChainName nVarChar(20) Chain Name
  SuppNum nVarChar(20) Vendor Code
  SuppName nVarChar(20) Vendor Name
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  SavePath Text(16) File Path
  UsePartSup VarChar(1) Use Goods Del. default=N [Y=Yes, N=No]
  BaseCode Int(11) Basic Grid Template default=-1
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  ExportNum Int(11) Export Counter default=0
  UserSign Int(6) User Signature ->OUSR
