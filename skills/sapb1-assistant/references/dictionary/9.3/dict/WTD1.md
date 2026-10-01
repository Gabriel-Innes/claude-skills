<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# WTD1 - Withholding Tax Dates
Module: Finance | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OWTD
  LineNum Int(11) Row Number
  DateFrom Date(8) Effective From
  Rate Num(19,6) Rate
  LogInstanc Int(11) Log Instance default=0
