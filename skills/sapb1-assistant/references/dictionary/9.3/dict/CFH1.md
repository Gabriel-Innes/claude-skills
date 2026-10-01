<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CFH1 - Cash Flow Statement Report - History - Rows
Module: Finance | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineId, CFHId
Fields (name type(len) description [values] ->parent table):
  CFHId Int(11) Cash Flow History Identity ->OCFH
  LineId Int(11) Row Number
  DispItem nVarChar(100) Displayed Item Title
  Levels Int(6) Levels
  LineNum nVarChar(5) Cash Flow Line No.
  IndentChar nVarChar(6) Indent Char. default=4
  Amount Num(19,6) Amount
  Formula VarChar(1) Formula Flag default=N [N=Non-Formula, Y=Formula Node]
