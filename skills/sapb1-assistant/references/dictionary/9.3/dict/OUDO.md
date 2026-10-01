<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OUDO - User-Defined Object
Module: Administration | 29 columns | ObjType: 206
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
  TABLE U: TableName
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(20) Code
  Name nVarChar(100) Name
  TableName nVarChar(19) Table Name ->OUTB
  LogTable nVarChar(20) Log Table Name
  TYPE VarChar(1) Object Type default=1 [1=Master Data, 3=Document]
  MngSeries VarChar(1) Manage Series default=N [Y=Yes, N=No]
  CanDelete VarChar(1) Delete default=Y [Y=Yes, N=No]
  CanClose VarChar(1) Close default=N [Y=Yes, N=No]
  CanCancel VarChar(1) Cancel default=N [Y=Yes, N=No]
  ExtName nVarChar(254) Extension Name
  CanFind VarChar(1) Find default=N [Y=Yes, N=No]
  CanYrTrnsf VarChar(1) Year Transfer default=N [Y=Yes, N=No]
  CanDefForm VarChar(1) Create Default Form default=N [Y=Yes, N=No]
  CanLog VarChar(1) Log default=N [Y=Yes, N=No]
  OvrWrtDll VarChar(1) Overwrite DLL File default=Y [Y=Yes, N=No]
  UIDFormat VarChar(1) Unique Form ID Format default=Y [Y=Yes, N=No]
  CanArchive VarChar(1) Archive default=N
  MenuItem VarChar(1) Specify Menu Item default=N [Y=Yes, N=No]
  MenuCapt nVarChar(254) Menu Caption
  FatherMenu Int(11) Parent Menu ID
  Position Int(6) Menu Position
  CanNewForm VarChar(1) Create Enhanced Form default=Y
  IsRebuild VarChar(1) If Needed, Rebuild New Form default=Y
  NewFormSrf Text(16) Enhanced Form: SRF File
  MenuUid nVarChar(32) Menu UID
  LstUpdDate Date(8) Last Update Date
  LstUpdTime Int(11) Last Update Time
  CanApprove VarChar(1) Approve default=N [Y=Yes, N=No]
  TemplateID Int(11) Workflow Template ID ->OWMG
