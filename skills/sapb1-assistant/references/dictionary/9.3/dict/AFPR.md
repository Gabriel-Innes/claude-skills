<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AFPR - Posting Period-Log
Module: Finance | 25 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AbsEntry
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
  Free2 VarChar(1) Active for Feed default=Y [Y=Yes, N=No]
  Free3 VarChar(1) Locked default=N [N=Unlocked, S=Unlocked Except Sales, C=Closing Period, Y=Locked]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
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
