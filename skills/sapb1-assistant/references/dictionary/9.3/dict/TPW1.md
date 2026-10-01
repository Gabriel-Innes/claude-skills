<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# TPW1 - Selection Criteria
Module: Banking | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Absolute Entry No ->OTPW
  FromPeriod Date(8) From Period
  ToPeriod Date(8) To Period
  FromDate Date(8) From Date
  ToDate Date(8) To Date
  TaxCategry Int(11) Tax Category ->ONFT
  LocCode Int(11) Location Code ->OLCT
