<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OVRW - VAT Reposting Wizard
Module: Finance | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  RunName nVarChar(100) Wizard Run Name
  RunDate Date(8) Wizard Run Date
  Status VarChar(1) Status default=E [E=Executed, S=Saved, D=Draft, C=Canceled]
  UserSign Int(11) User Signature ->OUSR
  LedgerType VarChar(1) Ledger Type default=S [S=Sales, P=Purchase]
  DebitAcc nVarChar(15) Debit Account ->OACT
  PostDate Date(8) Posting Date
  JESeries nVarChar(11) Journal Entry Series default=0
  APTISeries nVarChar(11) Invoice Series default=0
  DateType VarChar(1) Date Type default=R [R=Posting Date, D=Due Date, T=Document Date]
  DateFrom Date(8) Date From
  DateTo Date(8) Date To
  IncCorAlt VarChar(1) Include Corr. and Alter. default=N [Y=Yes, N=No]
  BPLId Int(11) This field is not used anymore ->OBPL
  RunType VarChar(1) Run Type default=M [M=Manual, C=Automatic - Export - Confirmation Expected, E=Automatic - Export - Confirmed/Not Confirmed, S=Separate Accounting]
