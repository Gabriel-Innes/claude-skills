<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OSUL - Support User Login Record
Module: Administration | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
Fields (name type(len) description [values] ->parent table):
  ID Int(11) Main ID
  RealName nVarChar(100) Real Name
  LogReason nVarChar(100) Login Reason [A=Transaction Issue Analysis, B=Setup Issue Analysis, C=Data Issue Analysis, D=Add-on Issue Analysis, E=Customer Usage Assistance, F=System Maintenance, G=Consulting, H=Other, I=Add-on Access, J=Root Cause Analysis, K=Consulting / Support]
  LogDetail Text(16) Login Detail Information
  Mac nVarChar(100) MAC Address
  Machine nVarChar(100) Machine Name
  StartDate Date(8) Start Date
  StartTime Int(11) Start Time
  EndDate Date(8) End Date
  EndTime Int(11) End Time
  ChkHash Text(16) Checked Hash Value
