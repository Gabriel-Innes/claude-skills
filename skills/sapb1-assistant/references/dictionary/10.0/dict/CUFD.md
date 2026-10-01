<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CUFD - User Fields - Description
Module: Administration | 21 columns | ObjType: 152
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TableID, FieldID
  ALIAS U: TableID, AliasID
Fields (name type(len) description [values] ->parent table):
  TableID nVarChar(21) Table
  FieldID Int(6) Field
  AliasID nVarChar(50) Title
  Descr nVarChar(80) Description
  TypeID VarChar(1) Type
  EditType VarChar(1) Edit Type
  SizeID Int(6) Size
  EditSize Int(6) Edit Size
  Dflt nVarChar(254) Default
  NotNull VarChar(1) Required Entry Field default=N [Y=Yes, N=No]
  IndexID VarChar(1) Create Index default=N [Y=Yes, N=No]
  RTable nVarChar(21) Linked Table ->OUTB
  RField Int(6) Linked Field
  Action VarChar(1) Action
  Sys VarChar(1) System Defined? default=N [Y=Yes, N=No]
  DfltDate Date(8) Default Date
  RelUDO nVarChar(20) Related UDO
  ValidRule nVarChar(254) Validation Rule
  RelSO nVarChar(20) Related System Object
  RThrdPTab nVarChar(100) Related to Third Party Table
  RThrdPFld nVarChar(100) Related to Third Party Field
