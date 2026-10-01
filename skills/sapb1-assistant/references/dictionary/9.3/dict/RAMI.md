<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RAMI - RAMI
Module: General | 24 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ErrUID
  GUID: GuidStr
  CodeDefine U: MsgDef
  String U: StrIdx, StrlNum
  ObjectId: Alias, SonTable, ObjName
Fields (name type(len) description [values] ->parent table):
  ErrUID nVarChar(11) Error Message Unique ID
  StrlNum Int(11) String List Number
  StrIdx Int(11) String Index
  GuidStr nVarChar(32) GUID String default=3A51AF1A405C41479530D05FF95A3FBA
  MsgDef nVarChar(100) Message Define
  MsgType VarChar(1) Message Type default=E [E=Error, W=Warning, N=Info, S=Success, O=None]
  MsgArea nVarChar(20) Message Area default=-1 [-1=, AP_AR=Sales and Purchurse orders, RPT=Reports, PROD=Production, LGST=ItemMasterData, INVT=Inventory, FIN=Financial, BANK=Banking, CARD=BP Master Data, AUTH=Authorization, ADMIN=Administration, SDK=SDK UI, LCNS=License, ADDON=Add-On manager, FORM=Form Infrastructure, DB=DB Infrastructure, CORE=Core Layer, INST=Installation and Upgrade]
  ScnExp Text(16) Scenarion Explanation
  ObjName nVarChar(20) Object Name
  SonTable nVarChar(20) Son Table
  Alias nVarChar(10) Alias
  FormID Int(11) Form ID
  PaneID Int(6) Pane Id default=0
  ItemID Int(11) Item ID default=-1
  CreateDate Date(8) Creation date
  CreateTime Int(6) Creation Time
  UpdateDate Date(8) Update Date
  UpdateTime Int(6) Update Time
  UserSign Int(11) User Sign
  SolExp Text(16) Solution Explanation
  CsnId nVarChar(30) CSN Note Id
  DispType nVarChar(30) Display Type default=SBAR [SBAR=Sbar, NOTE=Note, DIALOG_OKCancelType=Dialog OK Cancel, DIALOG_YesNoCancelType=Dialog Yes No Cancel, DIALOG_YesNoType=Dialog Yes No, DIALOG_YesAllNoAllCancelType=Dialog Yes All No All Cancel, DIALOG_ErrorOkType=Dialog Error Ok, DIALOG_ContinueSaveType=Dialog Continue Save, DIALOG_RemoveCancelType=Dialog Remove Cancel, DIALOG_ContinueCancelType=Dialog Continue Cancel, DIALOG_ContinueCancelNoType=Dialog Continue Cancel No, DIALOG_AddCancelType=Dialog Add Cancel, DIALOG_ContinueStopType=Dialog Continue Stop, DIALOG_YesCancelType=Dialog Yes Cancel, DIALOG_ContinueOpenType=Dialog Continue Open, DIALOG_OpenContinueCancelType=Dialog Open Continue Cancel, DIALOG_YesYesAllNoType=Dialog Yes Yes All No, DIALOG_YesYesAllNoAllType=Dialog Yes Yes All No All]
  ColmID Int(11) Column ID default=-1
  IsDeleted VarChar(1) Is Deleted default=N [N=No, Y=Yes]
