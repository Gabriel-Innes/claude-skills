<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# GPA1 - Gross Profit Adjustment - Documents
Module: Marketing Documents | 54 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineId, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OGPA
  LineId Int(11) Row No.
  ItemCode nVarChar(50) Item No. ->OITM
  ItemName nVarChar(100) Item Description
  DocType nVarChar(20) Document Type
  DocNum Int(11) Document Number
  DocAbs Int(11) Document Abs. Entry
  DocLineNum Int(11) Document Line Number
  ManagedBy Int(11) Managed By default=-1 [10000044=Batch Numbers, 10000045=Serial Numbers, -1=]
  Selected VarChar(1) Choose default=Y [Y=Yes, N=No]
  DistNumber nVarChar(36) Batch Number
  PostDate Date(8) Posting Date
  WhsCode nVarChar(8) Warehouse Code
  Quantity Num(19,6) Quantity
  CogsAcct nVarChar(15) COGS Account Code
  CogsAmnt Num(19,6) COGS Amount
  SalesAmnt Num(19,6) Sales Amount
  GrssProfit Num(19,6) Row Gross Profit
  COGSByCC Num(19,6) COGS By Current Cost
  GPByCC Num(19,6) Gross Profit By Current Cost
  DeltaGP Num(19,6) Delta Gross Profit
  SalesPrice Num(19,6) Sales Price
  BatchQt Num(19,6) Batch Quantity
  SnBAbs Int(11) SnB Abs. Entry
  AccTotal Num(19,6) Acct Total
  AccQty Num(19,6) Acct Qty
  ActionType Int(11) Action Type default=5 [0=TRANSACTION_UNKNOWN, 1=TRANSACTION_IN, 2=TRANSACTION_OUT, 3=TRANSACTION_SET, 4=TRANSACTION_COMPLETE, 5=EMPTY_TRANSACTION, 6=TRANSACTION_REVALUATION, 7=TRANSACTION_REVALUATION_INCREASE, 8=TRANSACTION_REVALUATION_DECREASE, 9=TRANSACTION_CLOSE_IN, 10=TRANSACTION_CLOSE_OUT, 11=TRANSACTION_NEGATIVE_REVALUATION, 12=TRANSACTION_NULLIFY, 13=TRANSACTION_RESERVE_CI_IN, 14=TRANSACTION_RESERVE_CI_OUT, 15=TRANSACTION_RESERVE_CI_REVAL_INC, 16=TRANSACTION_RESERVE_CI_REVAL_DEC, 17=TRANSACTION_REVAL_PRICE_CHANGE_INCREASE, 18=TRANSACTION_REVAL_PRICE_CHANGE_DECREASE]
  SBAccTotal Num(19,6) SnB Acct Total
  SBAccQty Num(19,6) SnB Acct Qty
  BaseType nVarChar(20) Base Type
  Execute VarChar(1) Execute default=Y [Y=Yes, N=No]
  SBCogsAmnt Num(19,6) SnB COGS Amount
  SBSaleAmnt Num(19,6) SnB Sales Amount
  SBGrssProf Num(19,6) SnB Gross Profit
  SBGrPrPerc Num(19,6) SnB Gross Profit Percentage
  GrPrPerc Num(19,6) Gross Profit Percentage
  GPPercByCC Num(19,6) Gross Profit Percentage By Current Cost
  DeltaGPLn Num(19,6) Delta gross profit calculated for the document line
  Applied Num(19,6) Applied Adjustment
  SBAccTtAdj Num(19,6) SnB Acct Total Adjustment
  IsMixed VarChar(1) Is Mixed Based Document default=N [Y=Yes, N=No]
  CogsAmByCC Num(19,6) Total COGS Amount By Current Cost
  GrssPrByCC Num(19,6) Total Gross Profit By Current Cost
  LineType VarChar(1) Wizard Line Type default=N [N=Normal, C=Chained, I=Non Based Correction Invoice]
  ChDocType nVarChar(20) Chained Document Type
  ChDocAbs Int(11) Chained Document Abs. Entry
  WasQty Num(19,6) Was Line Quantity
  WasCogs Num(19,6) Was Line COGS Amount
  WasSales Num(19,6) Was Line Sales Amount
  WasPrice Num(19,6) Was Line Sales Price
  WasGrProf Num(19,6) Was Line Gross Profit
  BaseAbs Int(11) Base Document Abs Entry
  WasNewCogs Num(19,6) Was Line New Cogs
  ChDocLine Int(11) Chained Document Line
