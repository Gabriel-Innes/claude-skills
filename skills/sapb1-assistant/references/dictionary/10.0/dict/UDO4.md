<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# UDO4 - User-Defined Objects - Child Table Columns
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, SonNum, ColumnNum
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(20) Code
  ColumnNum Int(11) Form Column Number
  SonNum Int(11) Child No.
  ColAlias nVarChar(52) Form Column Alias
  ColDesc nVarChar(80) Form Column Description
  ColIsUsed VarChar(1) Form Column Used or Not default=N
  ColEdit VarChar(1) Form Column Actived or Not default=N
