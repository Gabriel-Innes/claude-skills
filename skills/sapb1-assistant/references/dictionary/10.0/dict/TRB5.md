<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# TRB5 - Tax Report Wizard Reported Tax Sums
Module: Reports | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, State
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OTRB
  State nVarChar(3) State Code ->OCST
  CardCode nVarChar(15) Vendor Code ->OCRD
  TransCrdt Num(19,6) Transferred Credit
  TotalDbt Num(19,6) Total Reported Debit
  TtlDbtSc Num(19,6) Total Reported Debit SC
  TotalCrdt Num(19,6) Total Reported Credit
  TtlCrdtSc Num(19,6) Total Reported Credit SC
  TotalDed Num(19,6) Total Reported Tax Deductions
  TtlDedSc Num(19,6) Total Reported Tax Deductions SC
  BlncDue Num(19,6) Balance Due
  TransId Int(11) Transaction Number ->OJDT
