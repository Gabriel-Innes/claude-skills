<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# DUT1 - Dunning Term Array1
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LevelNum, TermCode
Fields (name type(len) description [values] ->parent table):
  TermCode nVarChar(25) Dunning Term Code ->ODUT
  LevelNum Int(11) Level No.
  LetterFrmt nVarChar(8) Letter Format
  EffctAftr nVarChar(3) Effective after
  LetterFee Num(19,6) Fee per Letter
  FeeCurr nVarChar(3) Fee Currency
  MinBalance Num(19,6) Mininum Balance
  MinBlnCurr nVarChar(3) Min Balance Currency
  CalcIntrst VarChar(1) Calc. Interest default=Y [Y=Yes, N=No]
