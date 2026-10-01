<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# MFLD - MetaData Tables Fields
Module: General | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TableName, FieldIndex, ResCode, RevCode
Fields (name type(len) description [values] ->parent table):
  TableName nVarChar(5) Table Name
  FieldIndex Int(6) Field Index
  Name nVarChar(20) Field Name
  Alias nVarChar(10) Alias
  Descr nVarChar(250) Description
  Type VarChar(1) Type default=A [A=DB Alpha, M=DB Memo, N=DB Numeric, D=DB Date, B=DB Binary, I=DB Auto Key]
  Size Int(6) Size
  FieldType Int(6) Field Type Num
  Visible VarChar(1) Visible default=Y [Y=Yes, N=No]
  EditType VarChar(1) Edit Type
  EditSize Int(6) Edit Size
  RFile nVarChar(4) Related Table
  ColHeading nVarChar(30) Column Heading
  FrmHeading nVarChar(30) Form Heading
  GroupNum Int(6) Group Number default=0 [0=User, -1=System]
  DefaultVal nVarChar(254) Default Value
  DIStatus VarChar(1) DI Status default=E [N=Not added to DI, Y=Added as Read/Write, R=Added as Read Only, E=NOT DEFINED]
  Dirty VarChar(1) Dirty default=Y [Y=Yes, N=No]
  Flag1 VarChar(1) Flag1 default=N [Y=Yes, N=No]
  UpdateDate Date(8) Update Date
  UpdateTime Int(11) Update Time default=0
  UsrSgnAttr Int(11) User Sign For Attribs Change default=-1
  ResCode Int(11) Resource Code from RSBD default=-1
  RevCode Int(11) Revision Code default=-1
  AssGrp nVarChar(16) Association Group
  AssType nVarChar(2) Association Type default=-1 [-1=, OT=Object Type, O1=Object Key Seg. 1, O2=Object Key Seg. 2, O3=Object Key Seg. 3, O4=Object Key Seg. 4, O5=Object Key Seg. 5, O6=Object Key Seg. 6, AO=Array Offset, A1=Array Key 1, A2=Array Key 2, A3=Array Key 3]
  IsPersist VarChar(1) Is Field Persistant default=Y [Y=Yes, N=No]
