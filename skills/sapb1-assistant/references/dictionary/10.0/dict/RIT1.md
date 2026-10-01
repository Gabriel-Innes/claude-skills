<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# RIT1 - Interest Rates
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, LineNum
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(20) Object Code ->ORIT
  LineNum Int(11) Row Number
  Days Int(6) Number of Tolerance Days
  IntrstPrct Num(19,6) Interest %
  FixedSum Num(19,6) Fixed Interest Amount
  FixSumCurr nVarChar(3) Fixed Amount Currency
