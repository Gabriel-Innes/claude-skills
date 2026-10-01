<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# MDKY - MetaData Tables DKeys
Module: General | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: RevCode, ResCode, DKeyIndex, HKeyIndex, TableName
Fields (name type(len) description [values] ->parent table):
  TableName nVarChar(5) Table Name
  HKeyIndex Int(6) HKey Index
  DKeyIndex Int(6) DKey Index
  FieldName nVarChar(20) Field in Key
  Upper VarChar(1) Upper default=Y [Y=Yes, N=No]
  UpdateDate Date(8) Update Date
  UpdateTime Int(11) Update Time default=0
  UsrSgnAttr Int(11) User Sign For Attribs Change default=-1
  ResCode Int(11) Resource Code from RSBD default=-1
  RevCode Int(11) Revision Code default=-1
