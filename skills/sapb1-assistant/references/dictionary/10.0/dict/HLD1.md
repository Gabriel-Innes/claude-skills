<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# HLD1 - Holiday Dates
Module: Human Resources | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: HldCode, StrDate, EndDate
Fields (name type(len) description [values] ->parent table):
  HldCode nVarChar(20) Holiday Code ->OHLD
  StrDate Date(8) Start Date
  EndDate Date(8) End Date
  Rmrks nVarChar(50) Remarks
