<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OADT - Fixed Assets Account Determination
Module: Finance | 27 columns | ObjType: 1470000002
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(15) Code
  Descr nVarChar(100) Description
  BalanceAct nVarChar(15) Asset Balance Sheet Account ->OACT
  ClrAcqAct nVarChar(15) Acquisition Clearing Account ->OACT
  RevResvAct nVarChar(15) Revaluation Reserve ->OACT
  OrdDprAct nVarChar(15) Ordinary Depreciation ->OACT
  OrdDprAcc nVarChar(15) Accumulated Ordinary Depr. ->OACT
  UnpDprAct nVarChar(15) Unplanned Depreciation ->OACT
  UnpDprAcc nVarChar(15) Accumulated Unplanned Depr. ->OACT
  SpDprAct nVarChar(15) Special Depreciation ->OACT
  SpDprAcc nVarChar(15) Accumulated Special Depr. ->OACT
  SaRevNAct nVarChar(15) Revenue from Asset Sales (Net) ->OACT
  ReExpNAct nVarChar(15) Retirement with Expense (Net) ->OACT
  ReRevNAct nVarChar(15) Retirement with Revenue (Net) ->OACT
  ReNBVeAct nVarChar(15) NBV Retirement Expense (Gross) ->OACT
  ReNBVrAct nVarChar(15) NBV Retirement Revenue (Gross) ->OACT
  ClrDscAct nVarChar(15) Cash Discount Clearing Account ->OACT
  RevReAct nVarChar(15) Revenue Account for Retirement ->OACT
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  ClearAccRe nVarChar(15) Revenue Clearing Account ->OACT
  RevResvClr nVarChar(15) Revaluation Reserve Clearing ->OACT
  SnapshotId Int(11) Snapshot ID default=0
