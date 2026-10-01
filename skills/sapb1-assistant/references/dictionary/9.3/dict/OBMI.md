<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OBMI - Brazilian Multi-Indexer
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ID
  IND_CODE_K U: Code, IndexType
Fields (name type(len) description [values] ->parent table):
  ID Int(11) Unique ID
  IndexType Int(11) Indexer Type default=-1
  Code nVarChar(10) Code
  Descr nVarChar(254) Description
  RefIndCod1 nVarChar(10) First Referenced Indexer Code
  RefIndCod2 nVarChar(10) Second Referenced Indexer Code
  RefIndCod3 nVarChar(10) Third Referenced Indexer Code
  UserSign Int(6) User Signature ->OUSR
