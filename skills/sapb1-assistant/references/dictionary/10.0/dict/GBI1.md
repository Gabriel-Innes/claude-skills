<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# GBI1 - GBI Row 1 - Electronic Account Book
Module: Finance | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: HistoryId, RowId
Fields (name type(len) description [values] ->parent table):
  HistoryId Int(11) History Key ->OGBI
  RowId Int(11) Row Number
  AcctBkNo nVarChar(5) Electronic Account Book No.
  AcctBkName nVarChar(30) Electronic Account Book Name
  OrgCode nVarChar(20) Organizational Code
  CompType nVarChar(8) Company Type
  Industry nVarChar(20) Industry
  SoftVender nVarChar(60) Accounting Software Provider
  Version nVarChar(20) Accounting Software Version
  FisYear nVarChar(4) Fiscal Year
  LocCurr nVarChar(3) Local Currency
  AcctStruct nVarChar(30) Account Structure
