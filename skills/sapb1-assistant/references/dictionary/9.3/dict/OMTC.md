<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OMTC - Bank Statement - Matching Criteria
Module: Banking | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
  MATCH_TYPE U: RuleIndex, Round, MatchID
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  MatchID Int(6) Form Type Index default=1 [1=Documents, 2=Internal Reconciliation, 3=External Reconciliation]
  Round Int(6) Rounding [1=Round 1, 2=Round 2, 3=Round 3, =]
  MtcRule Int(6) Matching Rule default=0
  MtcAlias nVarChar(18) Matching Alias
  Differnce Int(11) Difference default=0
  DiffAmnt Num(19,6) Amount Difference
  RuleIndex Int(6) Rule Index
