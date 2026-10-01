<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# UDO4 - User-Defined Objects - Child Table Columns
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ColumnNum, SonNum, Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(20) Code
  ColumnNum Int(11) Form Column Number
  SonNum Int(11) Child No.
  ColAlias nVarChar(52) Form Column Alias
  ColDesc nVarChar(80) Form Column Description
  ColIsUsed VarChar(1) Form Column Used or Not default=N
  ColEdit VarChar(1) Form Column Actived or Not default=N
