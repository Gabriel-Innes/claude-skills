<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OMTH - Reconciliation History
Module: Banking | 12 columns | ObjType: 26
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: MthAcctCod, IsInternal, MatchNum
Fields (name type(len) description [values] ->parent table):
  MthAcctCod nVarChar(15) Account Code
  IsInternal VarChar(1) Reconciliation Type default=E [I=Internal, E=External]
  MatchNum Int(11) Reconciliation No.
  Totals Num(19,6) Recon. Amount (One Side)
  IsCard VarChar(1) Select BP or Account default=A [A=G/L Account, C=BP]
  MatchType nVarChar(2) Reconciliation Type default=0 [0=Manual, 1=Ref. 1, 2=Ref. 2, 3=Ref. 3, 4=Posting Date, 5=Due Date, 6=Ref. 1 + Posting Date, 7=Ref. 2 + Posting Date, 8=Ref. 3 + Posting Date, 9=Ref. 1 + Due Date, 10=Ref. 2 + Due Date, 11=Ref. 3 + Due Date, 12=By Total]
  TransId Int(11) Reconciliation Transaction No. default=-1
  MatchDate Date(8) Reconciliation Date
  CurrType nVarChar(3) Currency Type
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  createDate Date(8) Creation Date
