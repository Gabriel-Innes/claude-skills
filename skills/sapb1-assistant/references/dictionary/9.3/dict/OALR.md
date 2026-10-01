<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OALR - Alerts
Module: Administration | 14 columns | ObjType: 81
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
  USER: UserSign
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Internal Number
  Type VarChar(1) Type default=A [A=Alert, M=Message]
  Priority VarChar(1) Priority default=1 [0=-, 1=, 2=mHighPriority]
  TCode Int(11) Template Code ->OALT
  Subject nVarChar(254) Subject
  UserText Text(16) MEMO
  DataCols Int(11) No. of Columns
  DataParams Text(16) Data
  MsgData Text(16) Data
  UserSign Int(6) User Signature ->OUSR
  Attachment Text(16) Attached File
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  AtcEntry Int(11) Attachment Entry
  AltType VarChar(1) Alert Type default=N [N=Unknown, C=Inventory Cycle]
