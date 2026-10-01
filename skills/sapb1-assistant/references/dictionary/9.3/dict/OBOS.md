<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OBOS - Box Set Definition
Module: Finance | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  EFFEC_DATE: EffecDate
  BZKEY U: ReportType, EffecDate
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  IsUsed VarChar(1) Is Set Used default=N [Y=Yes, N=No]
  EffecDate Date(8) Effective From
  FileFmtCo Int(11) File Format Code ->OLLF
  IsDeleted VarChar(1) Is Set Deleted default=N [Y=Yes, N=No]
  ReportType VarChar(1) Report Type default=S [B=Box Declaration, S=BAS Report]
