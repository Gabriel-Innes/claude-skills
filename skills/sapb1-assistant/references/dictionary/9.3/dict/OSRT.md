<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OSRT - Korean Summary Report
Module: Reports | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  SUM_RPT_ID U: SumRptId
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Abstract ID
  SumRptId nVarChar(100) Summary Report ID
  SumRptDate Date(8) Summary Report Date
  BPLId Int(11) Business Place ID
  FromDate Date(8) From Date
  ToDate Date(8) To Date
  RptType VarChar(1) Report Type default=C [V=Vendor, C=Customer]
  version nVarChar(50) Report Generation Version
  SumSubId nVarChar(254) Summary Report Sub ID
  SumRptType nVarChar(254) Summary Report Type
