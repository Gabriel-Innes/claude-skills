<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ODUN - Dunning Letters
Module: Business Partners | 8 columns | ObjType: 151
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineNum
Fields (name type(len) description [values] ->parent table):
  LineNum Int(11) Row Number
  LetrFormat nVarChar(8) Letter Format
  EffctAftr nVarChar(3) Effective After (Days)
  LetterFee Num(19,6) Fee Per Letter
  FeeCurr nVarChar(3) Fee Currency
  MinBalance Num(19,6) Minimum Balance
  MinBlnCurr nVarChar(3) Minimum Balance Currency
  CalcIntert VarChar(1) Interest default=N [Y=Yes, N=No]
