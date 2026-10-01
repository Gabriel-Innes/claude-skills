<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AEB1 - VAT Exemptions for Business Partners Row - History
Module: Finance | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  LineNum Int(11) Row Number
  ExmpDoc nVarChar(40) Exemption Doc. No.
  IssueDate Date(8) Date of Issue
  IssueTime Int(11) Time of Issue
  ExmpType Int(6) Exemption Type ->OVET
  AllItems VarChar(1) Apply to All Items default=N [N=No, Y=Yes]
  ItemCode nVarChar(50) Item No. ->OITM
  ItemDesc nVarChar(200) Item Description
  Rate Num(19,6) Rate %
  TaxCode nVarChar(8) Exemption Tax Code ->OSTC
  AuthName nVarChar(160) Name of Authorities
  ValidFrom Date(8) Valid From
  ValidTo Date(8) Valid To
  LogInstanc Int(11) Log Instance default=0
  VisOrder Int(11) Visual Order
