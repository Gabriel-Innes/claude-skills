<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# PJT2 - Project Plan Steps Time Record
Module: Administration | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, StepCode, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  StepCode Int(11) Step Code
  LineNum Int(11) Line Number
  Date Date(8) Date
  StartTime Int(11) Start Time
  EndTime Int(11) End Time
  Remarks nVarChar(254) Remarks
  LogInstanc Int(11) Log Instance
  Owner nVarChar(254) Owner ->OHEM
  Duration Num(19,6) Duration
