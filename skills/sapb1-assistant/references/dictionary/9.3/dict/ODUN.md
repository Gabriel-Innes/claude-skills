<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ODUN - Dunning Letters
Module: Business Partners | 8 columns | ObjType: 151
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
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
