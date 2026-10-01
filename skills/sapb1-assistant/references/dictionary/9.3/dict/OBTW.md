<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OBTW - Batch Attributes in Location
Module: Inventory and Production | 14 columns | ObjType: 310000008
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  SYSTEM_KEY U: WhsCode, SysNumber, ItemCode
  ABS_WHS U: WhsCode, MdAbsEntry
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item Code ->OITM
  SysNumber Int(11) System Number ->OBTN
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Location nVarChar(100) Location
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Transfered VarChar(1) Transferred default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  AbsEntry Int(11) abs entry
  MdAbsEntry Int(11) MD Abs Entry ->OBTN
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
