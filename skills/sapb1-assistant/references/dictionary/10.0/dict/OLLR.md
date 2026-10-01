<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OLLR - Electronic Report Generation Result
Module: Reports | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  REPORT: EReportId
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  CreateTime Int(6) Creation Time
  EReportId Int(11) Electronic Report ID ->OLLF
  Status VarChar(1) Status default=C [C=Canceled, E=Executed, F=Failed]
  Log Text(16) Run Log
  ReportInst Int(11) Electronic Report Instance
  VersionNum nVarChar(13) Version Number
