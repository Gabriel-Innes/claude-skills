<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# UDO2 - User-Defined Objects - Find Columns
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ColumnNum, Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(20) Code
  ColumnNum Int(11) Column Number
  ColAlias nVarChar(52) Column Alias
  ColumnDesc nVarChar(80) Column Description
