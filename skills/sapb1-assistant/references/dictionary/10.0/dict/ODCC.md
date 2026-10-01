<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ODCC - Dashboard Cache Configuration
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Abs Entry
  Enable VarChar(1) Enable default=N [Y=, N=]
  Start Int(11) Start
  CronString nVarChar(254) Cron String
  UserSign Int(6) User Signature ->OUSR
