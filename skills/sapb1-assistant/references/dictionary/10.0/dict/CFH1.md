<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CFH1 - Cash Flow Statement Report - History - Rows
Module: Finance | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CFHId, LineId
Fields (name type(len) description [values] ->parent table):
  CFHId Int(11) Cash Flow History Identity ->OCFH
  LineId Int(11) Row Number
  DispItem nVarChar(100) Displayed Item Title
  Levels Int(6) Levels
  LineNum nVarChar(5) Cash Flow Line No.
  IndentChar nVarChar(6) Indent Char. default=4
  Amount Num(19,6) Amount
  Formula VarChar(1) Formula Flag default=N [N=Non-Formula, Y=Formula Node]
