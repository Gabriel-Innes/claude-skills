<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OECC - Expense Classification Category
Module: Finance | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CODE U: Code
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Unique Entry
  Code nVarChar(50) Code
  Descriptio nVarChar(254) Description
