<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# APRC - Cost Center
Module: Sales Opportunities | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PrcCode, LogInstanc
Fields (name type(len) description [values] ->parent table):
  PrcCode nVarChar(8) Center Code
  PrcName nVarChar(30) Center Name
  GrpCode nVarChar(4) Group Code
  Balance Num(19,6) Balance
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  DimCode Int(6) In Which Dimension default=1 ->ODIM
  CCTypeCode nVarChar(8) Cost Center Type Code ->OCCT
  ValidFrom Date(8) Valid From
  ValidTo Date(8) Valid To
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  CCOwner Int(11) Cost Center Owner ->OHEM
