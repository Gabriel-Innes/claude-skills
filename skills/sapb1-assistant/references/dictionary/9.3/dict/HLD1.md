<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# HLD1 - Holiday Dates
Module: Human Resources | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: EndDate, StrDate, HldCode
Fields (name type(len) description [values] ->parent table):
  HldCode nVarChar(20) Holiday Code ->OHLD
  StrDate Date(8) Start Date
  EndDate Date(8) End Date
  Rmrks nVarChar(50) Remarks
