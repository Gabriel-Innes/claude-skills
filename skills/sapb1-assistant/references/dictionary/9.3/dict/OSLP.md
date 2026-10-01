<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OSLP - Sales Employee
Module: Business Partners | 15 columns | ObjType: 53
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
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
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  EmpID Int(11) Employee ID ->OHEM
  Active VarChar(1) Active default=Y [Y=Active, N=Inactive]
  Telephone nVarChar(20) Telephone
  Mobil nVarChar(50) Mobile
  Fax nVarChar(20) Fax
  Email nVarChar(100) E-Mail
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased, B=Blocked, U=Unblocked]
