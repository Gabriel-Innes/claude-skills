<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# MVAL - MetaData Tables Fields Vals
Module: General | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: RevCode, ResCode, ValIndex, FieldIndex, TableName
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
