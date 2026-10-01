<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OSLP - Sales Employee
Module: Business Partners | 16 columns | ObjType: 53
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SlpCode
  SLP_NAME U: SlpName
  COM_GROUP: GroupCode
Fields (name type(len) description [values] ->parent table):
  SlpCode Int(11) Sales Employee Code
  SlpName nVarChar(155) Sales Employee Name
  Memo nVarChar(50) Remarks
  Commission Num(19,6) % Commission for Sales Employee
  GroupCode Int(6) Commission Group default=0 ->OCOG
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  EmpID Int(11) Employee ID ->OHEM
  Active VarChar(1) Active default=Y [Y=Active, N=Inactive]
  Telephone nVarChar(50) Telephone
  Mobil nVarChar(50) Mobile
  Fax nVarChar(50) Fax
  Email nVarChar(100) E-Mail
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased, B=Blocked, U=Unblocked]
  EncryptIV nVarChar(100) Encrypt IV
