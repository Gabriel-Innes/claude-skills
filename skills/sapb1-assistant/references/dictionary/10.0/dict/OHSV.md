<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OHSV - Hasavsevet Journal Entry
Module: Finance | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RecordKey
Fields (name type(len) description [values] ->parent table):
  RecordKey nVarChar(7) Record Number
  Ref1 nVarChar(5) Reference 1
  Ref2 nVarChar(5) Reference 2
  RefDate nVarChar(6) Posting Date
  DueDate nVarChar(6) Due Date
  CurrCode nVarChar(3) Currency Code
  Memo nVarChar(22) Details
  DebAcct1 nVarChar(8) Debit Account 1
  CredAcct1 nVarChar(8) Credit Account 1
  DebAmnt1 nVarChar(12) Debit
  credAmnt1 nVarChar(12) Credit
  FDebAmnt1 nVarChar(12) Debit Amount 1 in FC
  FCredAmnt1 nVarChar(12) Credit in FC
  Filler nVarChar(60) Filler
  EndField nVarChar(2) Ending Field
