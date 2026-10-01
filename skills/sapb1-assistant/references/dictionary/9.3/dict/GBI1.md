<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# GBI1 - GBI Row 1 - Electronic Account Book
Module: Finance | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: RowId, HistoryId
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
