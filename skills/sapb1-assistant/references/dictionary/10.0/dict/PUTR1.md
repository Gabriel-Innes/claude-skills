<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# PUTR1 - Pre-Upgrade Test Result Line
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SerialNum, TestID
Fields (name type(len) description [values] ->parent table):
  SerialNum Int(11) Serial Number
  TestID Int(11) Test ID
  TestDesc nVarChar(254) Test Description
  Result VarChar(1) Result [S=Success, E=Error, W=Warning, K=Skipped]
  BeginTime nVarChar(20) Start Time
  EndTime nVarChar(20) End Time
  SAPNote nVarChar(100) SAP Note Link
