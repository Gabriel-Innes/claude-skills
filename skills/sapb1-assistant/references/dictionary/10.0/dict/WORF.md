<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# WORF - Object Wizard Related Files
Module: General | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjName, SonNum
  UNIQUE_ID U: UniqueId
  TABLE U: ObjName, ObjTable
Fields (name type(len) description [values] ->parent table):
  ObjName Int(11) Parent Object Code
  SonNum Int(11) Son Number
  ObjTable nVarChar(20) Son Table
  RelObj nVarChar(20) Object
  RelType VarChar(1) Relationship Type default=L [L=Line, O=Odd, A=Another object contained]
  LogSon nVarChar(20) Son's Log table
  FthrLineId Int(11) Father's Line Id default=0
  UniqueId Int(11) Son Unique Id
  LnObjCode nVarChar(20) Line object code
  SonDesc nVarChar(30) Son Description
  CreateDate Date(8) Creation date
  CreateTime Int(6) Creation Time
  UpdateDate Date(8) Update Date
  UpdateTime Int(6) Update Time
  UserSign Int(11) User Sign
  FieldIndex Int(6) Field Index
