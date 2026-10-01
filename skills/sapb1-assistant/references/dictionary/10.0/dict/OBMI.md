<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OBMI - Brazilian Multi-Indexer
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
  IND_CODE_K U: IndexType, Code
Fields (name type(len) description [values] ->parent table):
  ID Int(11) Unique ID
  IndexType Int(11) Indexer Type default=-1
  Code nVarChar(10) Code
  Descr nVarChar(254) Description
  RefIndCod1 nVarChar(10) First Referenced Indexer Code
  RefIndCod2 nVarChar(10) Second Referenced Indexer Code
  RefIndCod3 nVarChar(10) Third Referenced Indexer Code
  UserSign Int(6) User Signature ->OUSR
