<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OFPR - Posting Period
Module: Finance | 25 columns | ObjType: 111
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CODE U: Code
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) System Number
  Code nVarChar(20) Period Code
  Name nVarChar(20) Period Name
  F_RefDate Date(8) Posting Date From
  T_RefDate Date(8) Posting Date To
  F_DueDate Date(8) Due Date From
  T_DueDate Date(8) Due Date To
  F_TaxDate Date(8) Document Date From
  T_TaxDate Date(8) Document Date To
  Free2 VarChar(1) Free default=Y [Y=Yes, N=No]
  Free3 VarChar(1) Free default=N [N=Unlocked, S=Unlocked Except Sales, C=Closing Period, Y=Locked]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  SubNum Int(11) No. of Sub-Period
  Free VarChar(1) Free
  Free1 VarChar(1) Free1
  Addition VarChar(1) Additional Sub-Periods default=N [Y=Yes, N=No]
  AddNum Int(11) No. of Additional
  Category nVarChar(10) Category ->OACP
  Indicator nVarChar(10) Period Indicator ->OPID
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  WasStatChd VarChar(1) Status Was Checked default=N [N=No, Y=Yes]
  PeriodStat VarChar(1) Period Status default=N [N=Unlocked, S=Unlocked Except Sales, C=Closing Period, Y=Locked, A=Archived]
  UserSign2 Int(6) Updating User ->OUSR
