<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ORCR - Recurring Postings
Module: Finance | 25 columns | ObjType: 34
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Instance, RcurCode
  BYDATE: NextDeu
Fields (name type(len) description [values] ->parent table):
  RcurCode nVarChar(8) Recurring Postings Code
  RcurDesc nVarChar(50) Transaction Description
  Frequency VarChar(1) Frequency default=M [D=Daily, W=Weekly, M=Monthly, Q=Quarterly, S=Semi-annually, A=Annually, O=One Time, T=Template, N=Not executed yet]
  Remind Int(6) Sub-Frequency default=1
  LastPosted Date(8) Last Executed
  NextDeu Date(8) Next Execution
  EntryCount Int(6) Entries Counter default=0
  Volume Num(19,6) Transaction Amount
  VolCurr nVarChar(3) Total Currency
  FinancVol Num(19,6) Total Monetary Val. of Trans.
  Ref1 nVarChar(100) Reference 1
  Ref2 nVarChar(100) Reference 2
  TransCode nVarChar(4) Transaction Code
  Memo nVarChar(50) Details
  LimitRtrns VarChar(1) Returns Limit default=N [Y=Yes, N=No]
  Returns Int(6) No. of Returns
  LimitDate Date(8) Date Limit
  Instance Int(6) Instance default=0
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  StampTax VarChar(1) Stamp Tax default=N [Y=Yes, N=No]
  AutoVat VarChar(1) Automatic VAT default=N [Y=Yes, N=No]
  ManageWTax VarChar(1) Manage WTax default=N [Y=Yes, N=No]
  Ref3 nVarChar(27) Reference 3
  DeferedTax VarChar(1) Deferred Tax default=N [Y=Yes, N=No]
