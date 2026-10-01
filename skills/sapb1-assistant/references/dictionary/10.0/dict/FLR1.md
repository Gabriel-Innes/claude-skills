<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# FLR1 - Filter Lines
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId, ColName
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Foreign Key
  LineNum Int(11) Line Number
  ColName nVarChar(10) Column Name
  CompValue nVarChar(254) Compare Value
  CompOper nVarChar(2) Compare Operator default== [===, >=>, <</td>=<</td>, >==>=, <==<=, !==!=]
