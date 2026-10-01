<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ADPA - Fixed Asset Depreciation Areas - History
Module: Finance | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, LogInstanc
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(15) Code
  Descr nVarChar(100) Description
  DirectDpr VarChar(1) Direct Depreciation default=D [D=Direct Posting, I=Indirect Posting]
  RetMeth VarChar(1) Retirement Method default=G [G=Gross, N=Net]
  AreaType VarChar(1) Area Type default=O [L=Posting to G/L, O=Additional Area, D=Derived Area]
  DrvdArea nVarChar(15) Derived Area ->ODPA
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) Updating User
  UpdateDate Date(8) Date of Update
  MainArea VarChar(1) Main Booking Area default=N [Y=Yes, N=No]
  CreditCtrl VarChar(1) Tax Credit Control default=N [Y=Yes, N=No]
  TaxType Int(11) Tax Type ->OSTT
  DirRevPost VarChar(1) Direct Revenue Posting default=N [Y=Yes, N=No]
  SnapshotId Int(11) Snapshot ID default=0
  BpTaxCorr nVarChar(15) BP for Tax Correction ->OCRD
  ItmTaxCorr nVarChar(50) Item for Tax Correction ->OITM
  UsgTaxCorr Int(11) Usage for Tax Correction ->OUSG
