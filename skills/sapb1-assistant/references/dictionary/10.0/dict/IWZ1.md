<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# IWZ1 - Accounts Revaluation History
Module: Finance | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, AcctCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OIWZ
  AcctCode nVarChar(15) Account Code ->OACT
  ActName nVarChar(100) Account Name
  ActFrmBlnc Num(19,6) Account From Balance
  ExecutLine VarChar(1) Executed Row default=Y [Y=Executed Row, N=Filter Line]
  ActRevCncl VarChar(1) Account Revaluation Cancel default=N [N=No, Y=Yes]
  RevToAct nVarChar(15) Revaluate To Account
  ActDiffBal Num(19,6) Account Difference Balance
  RvCaclDate Date(8) Reval. Acct Cancellation Date
  ErrReason Int(11) Error Reason
  ActLastBal Num(19,6) Account Last Reval Balance
