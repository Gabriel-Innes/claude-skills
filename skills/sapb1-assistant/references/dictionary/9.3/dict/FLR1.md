<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# FLR1 - Filter Lines
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ColName, AbsId
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Foreign Key
  LineNum Int(11) Line Number
  ColName nVarChar(10) Column Name
  CompValue nVarChar(254) Compare Value
  CompOper nVarChar(2) Compare Operator default== [===, >=>, =, >==>=, !==!=]
