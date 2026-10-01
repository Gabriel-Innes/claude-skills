<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CDC1 - Cash Discount - Rows
Module: Finance | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineId, CdcCode
Fields (name type(len) description [values] ->parent table):
  CdcCode nVarChar(20) Code ->OCDC
  LineId Int(11) Row No.
  NumOfDays Int(6) Days
  Discount Num(19,6) Discount %
  Day Int(6) Day
  Month Int(6) Month
