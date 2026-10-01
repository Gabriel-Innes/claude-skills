<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# UDO3 - User-Defined Objects - Found Columns
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ColumnNum, SonNum, Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(20) Code
  ColumnNum Int(11) Form Column Number
  SonNum Int(11) Child No. default=0
  ColAlias nVarChar(52) Form Column Alias
  ColDesc nVarChar(80) Form Column Description
  ColEdit VarChar(1) Form Column Actived or Not default=N
