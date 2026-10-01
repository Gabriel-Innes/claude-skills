<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OSRW - Serial No. Attribs in Location
Module: Inventory and Production | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SYSTEM_KEY U: ItemCode, SysNumber, WhsCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item Code ->OITM
  SysNumber Int(11) System Number ->OSRN
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Location nVarChar(100) Location
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Transfered VarChar(1) Transferred default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  AbsEntry Int(11) abs entry
  MdAbsEntry Int(11) MD Abs Entry ->OSRN
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
