<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ODBW - Batch Draft Attribs in Locat.
Module: Inventory and Production | 14 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item Code ->OITM
  SysNumber Int(11) System No. ->OBTN
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Location nVarChar(100) Loc.
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Transfered VarChar(1) Transferred default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  AbsEntry Int(11) abs entry
  MdAbsEntry Int(11) MD Abs Entry
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
