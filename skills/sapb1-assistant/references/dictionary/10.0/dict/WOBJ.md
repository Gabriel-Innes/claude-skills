<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# WOBJ - Object Wizard
Module: General | 44 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjCode
  NAME U: ObjName
Fields (name type(len) description [values] ->parent table):
  ObjCode Int(11) Object Code
  ObjName nVarChar(20) Object Name
  Category VarChar(1) Category default=2 [2=Noun, 3=Operation, 4=History, 1=Abstract, 0=Not Exists]
  TableName nVarChar(20) TableName
  NOE VarChar(1) NOE or form default=N [Y=Yes, F=Form, N=None]
  ObjDesc nVarChar(254) Object Description
  FileName nVarChar(254) File Name
  Status VarChar(1) Execution Status default=D [R=Ready, P=Postponed, D=Done]
  ClassName nVarChar(100) Class Name
  AutoComp VarChar(1) OnAutoComplete default=Y [Y=Yes, N=No]
  Cancel VarChar(1) OnCancel default=N [Y=Yes, N=No]
  CanUpdate VarChar(1) OnCanUpdate default=N [Y=Yes, N=No]
  ChckDelet VarChar(1) OnCheckDelete default=N [Y=Yes, N=No]
  Close1 VarChar(1) OnClose default=N [Y=Yes, N=No]
  Create1 VarChar(1) OnCreate default=Y [Y=Yes, N=No]
  CreateDef VarChar(1) OnCreateDefaults default=N [Y=Yes, N=No]
  Delete1 VarChar(1) OnDelete default=Y [Y=Yes, N=No]
  GetByKey VarChar(1) OnGetByKey default=N [Y=Yes, N=No]
  GetNextSer VarChar(1) OnGetNextSerial default=N [Y=Yes, N=No]
  InitData VarChar(1) OnInitData default=N [Y=Yes, N=No]
  InitFlow VarChar(1) OnInitFlow default=N [Y=Yes, N=No]
  EndSucFlow VarChar(1) OnEndSuccessfulFlow default=N [Y=Yes, N=No]
  IsValid VarChar(1) OnIsValid default=Y [Y=Yes, N=No]
  PutSignate VarChar(1) OnPutSignature default=N [Y=Yes, N=No]
  UndoCancel VarChar(1) OnUndoCancel default=N [Y=Yes, N=No]
  Update1 VarChar(1) OnUpdate default=Y [Y=Yes, N=No]
  Upgrade VarChar(1) OnUpgrade default=N [Y=Yes, N=No]
  YearTransf VarChar(1) OnYearTransfer default=N [Y=Yes, N=No]
  AddLogEnt VarChar(1) OnAddLogEntry default=N [Y=Yes, N=No]
  LogTable nVarChar(20) Log Table
  CanDisplay VarChar(1) Can Display default=Y [Y=Yes, N=No]
  UserSign Int(11) User Signature default=-1
  IsSeries VarChar(1) Is Series default=N [Y=Yes, N=No]
  AddInVer Int(11) Added in version
  AbbrevIdx Int(11) Index in abbreviation strl
  DfaultForm Int(11) Default form for DI permission
  IsService VarChar(1) Is Service default=N [Y=Yes, N=No]
  ExtraPerm Int(11) Extra Permission for DI
  StrlIndex nVarChar(254) String list index
  CanArchive VarChar(1) Can Archive default=N [Y=Yes, N=No]
  CreateDate Date(8) Creation date
  CreateTime Int(6) Creation Time
  UpdateDate Date(8) Update Date
  UpdateTime Int(6) Update Time
