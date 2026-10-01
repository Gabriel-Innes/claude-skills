<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OTRS - Tax Report Saving Object
Module: Reports | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ObjType nVarChar(20) Object Type
  ReportType Int(11) Report Type [1=VAT Report (UK)]
  PeriodType VarChar(1) Report Period Type [Y=Year, Q=Quarter, B=Bi-Monthly, M=Month, P=Period, F=Fiscal Year, G=Fiscal Quarter]
  PeriodNum Int(11) Report Period Number
  Year Int(6) Report Year
  AdjustNum Int(6) Report Adjustment Number
  ApUserSign Int(6) Approved By (User Signature)
  ApDate Date(8) Approval Date
  ApTime Int(6) Approval Time
  DeclType VarChar(1) Declaration Type default=O [O=Original, S=Substitute, C=Complementary]
  SCDateFrom Date(8) Selection Criteria - Date From
  SCDateTo Date(8) Selection Criteria - Date To
  BosCode Int(11) Box Set Code ->OBOS
  BatchNum Int(11) Journal Voucher No. ->OBTD
