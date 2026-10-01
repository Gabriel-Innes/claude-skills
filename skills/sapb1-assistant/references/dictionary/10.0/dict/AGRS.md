<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AGRS - G/L Account Advanced Rules for Resources - History
Module: General | 55 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  PeriodCat nVarChar(10) Period Category
  FinancYear Date(8) Beginning of Financial Year
  Year Int(6) Financial Year
  PeriodName nVarChar(20) Period Name
  SubType VarChar(1) Sub-Period Type default=Y [Y=Year, Q=Quarters, M=Months, D=Days]
  PeriodNum Int(11) Number of Periods
  F_RefDate Date(8) Posting Date From
  T_RefDate Date(8) Posting Date To
  F_DueDate Date(8) Due Date From
  T_DueDate Date(8) Due Date To
  F_TaxDate Date(8) Document Date From
  T_TaxDate Date(8) Document Date To
  LogInstanc Int(11) Log Instance
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  ResCode nVarChar(50) Resource No. ->ORSC
  ResGrpCod Int(6) Resource Group ->ORSB
  WhsCode nVarChar(8) Warehouse Code
  BPGrpCod Int(6) BP Group
  LicTradNum nVarChar(32) Federal Tax ID default=!^| [!^|=All, !^|E=Empty, !^|F=Filled, Enter Tax ID=Enter Tax ID]
  ShipCountr nVarChar(3) Ship-to Country/Region
  ShipState nVarChar(3) Ship-To State
  Comments nVarChar(254) Remarks
  CreateDate Date(8) Creation Date
  RuleCode nVarChar(20) Advanced Rule Code
  GLMethod VarChar(1) Get G/L Account By default=A [A=General, W=Warehouse, C=Item Group]
  Transfered VarChar(1) Year Transfer [Y/N] default=N [Y=Yes, N=No]
  FromDate Date(8) From Date
  ToDate Date(8) To Date
  ResRevAct nVarChar(15) Resource Revenue Account ->OACT
  ResExpAct nVarChar(15) Resource Expense Account ->OACT
  ResSaleAct nVarChar(15) Resource Sales Credit Account ->OACT
  ResPurAct nVarChar(15) Resource Purchase Credit Acct ->OACT
  ResNInvAct nVarChar(15) Resource Received Not Inv. ->OACT
  ResStdExp1 nVarChar(15) Resource Std. Cost Expense 1 ->OACT
  ResStdExp2 nVarChar(15) Resource Std. Cost Expense 2 ->OACT
  ResStdExp3 nVarChar(15) Resource Std. Cost Expense 3 ->OACT
  ResStdExp4 nVarChar(15) Resource Std. Cost Expense 4 ->OACT
  ResStdExp5 nVarChar(15) Resource Std. Cost Expense 5 ->OACT
  ResStdExp6 nVarChar(15) Resource Std. Cost Expense 6 ->OACT
  ResStdExp7 nVarChar(15) Resource Std. Cost Expense 7 ->OACT
  ResStdExp8 nVarChar(15) Resource Std. Cost Expense 8 ->OACT
  ResStdExp9 nVarChar(15) Resource Std. Cost Expense 9 ->OACT
  ResStdEx10 nVarChar(15) Resource Std. Cost Expense 10 ->OACT
  ResWipAct nVarChar(15) Resource WIP Account ->OACT
  ResScrapAc nVarChar(15) Scrap Account ->OACT
  WipOffPlAc nVarChar(15) WIP Offset P&L Account ->OACT
  ResOffPlAc nVarChar(15) Resource Offset P&L Account ->OACT
  Active VarChar(1) Is Rule Active default=Y [Y=Yes, N=No]
  CmpPrivate VarChar(1) Company/Private default=A [A=All, C=Company, I=Private]
  VatGroup nVarChar(8) Tax Definition ->OVTG
  CardCode nVarChar(15) Customer/Vendor Code ->OCRD
  Usage Int(11) Usage Code for Document ->OUSG
