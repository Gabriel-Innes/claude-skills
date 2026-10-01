<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CDC1 - Cash Discount - Rows
Module: Finance | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CdcCode, LineId
Fields (name type(len) description [values] ->parent table):
  CdcCode nVarChar(20) Code ->OCDC
  LineId Int(11) Row No.
  NumOfDays Int(6) Days
  Discount Num(19,6) Discount %
  Day Int(6) Day
  Month Int(6) Month
