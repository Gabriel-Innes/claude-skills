<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# MVAL - MetaData Tables Fields Vals
Module: General | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TableName, FieldIndex, ValIndex, ResCode, RevCode
Fields (name type(len) description [values] ->parent table):
  TableName nVarChar(5) Table Name
  FieldIndex Int(6) Field Index
  ValIndex Int(6) Val Index
  Value nVarChar(254) Value
  Descr nVarChar(254) Description
  UpdateDate Date(8) Update Date
  UpdateTime Int(11) Update Time default=0
  UsrSgnAttr Int(11) User Sign For Attribs Change default=-1
  DiEnumCode Int(11) DI Enum Code
  DiEnItCode Int(11) DI Enum Item Code
  ResCode Int(11) Resource Code from RSBD default=-1
  RevCode Int(11) Revision Code default=-1
