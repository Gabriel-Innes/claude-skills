<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OFRC - Financial Report Categories
Module: Finance | 87 columns | ObjType: 96
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TemplateId, CatId
Fields (name type(len) description [values] ->parent table):
  CatId Int(6) Numerator
  TemplateId Int(11) Template ->OFRT
  Name nVarChar(254) Name
  FrgnName nVarChar(254) Foreign Name
  Levels Int(6) Account Level default=1 [1=Level 1, 2=Level 2, 3=Level 3]
  FatherNum Int(6) Parent Account Key
  Active VarChar(1) Active Account default=N [Y=Yes, N=No]
  HasSons VarChar(1) Including Children default=N [Y=Yes, N=No]
  VisOrder Int(6) Display Order
  SubSum VarChar(1) Subtotal default=N [Y=Yes, N=No]
  SubName nVarChar(100) Subtotal Name
  Furmula VarChar(1) Formula default=N [Y=Yes, N=No]
  Param_1 Int(6) Parameter 1 default=0
  Param_2 Int(6) Parameter 2 default=0
  Param_3 Int(6) Parameter 3 default=0
  Param_4 Int(6) Parameter 4 default=0
  Param_5 Int(6) Parameter 5 default=0
  Param_6 Int(6) Parameter 6 default=0
  Param_7 Int(6) Parameter 7 default=0
  Param_8 Int(6) Parameter 8 default=0
  Param_9 Int(6) Parameter 9 default=0
  Param_10 Int(6) Parameter 10 default=0
  Param_11 Int(6) Parameter 11 default=0
  Param_12 Int(6) Parameter 12 default=0
  Param_13 Int(6) Parameter 13 default=0
  Param_14 Int(6) Parameter 14 default=0
  Param_15 Int(6) Parameter 15 default=0
  Param_16 Int(6) Parameter 16 default=0
  Param_17 Int(6) Parameter 17 default=0
  Param_18 Int(6) Parameter 18 default=0
  Param_19 Int(6) Parameter 19 default=0
  Param_20 Int(6) Parameter 20 default=0
  Param_21 Int(6) Parameter 21 default=0
  Param_22 Int(6) Parameter 22 default=0
  Param_23 Int(6) Parameter 23 default=0
  Param_24 Int(6) Parameter 24 default=0
  Param_25 Int(6) Parameter 25 default=0
  OP_1 VarChar(1) Operator 1 [=Without, +=Addition, -=Subtraction]
  OP_2 VarChar(1) Operator 2 [=Without, +=Addition, -=Subtraction]
  OP_3 VarChar(1) Operator 3 [=Without, +=Addition, -=Subtraction]
  OP_4 VarChar(1) Operator 4 [=Without, +=Addition, -=Subtraction]
  OP_5 VarChar(1) Operator 5 [=Without, +=Addition, -=Subtraction]
  OP_6 VarChar(1) Operator 6 [=Without, +=Addition, -=Subtraction]
  OP_7 VarChar(1) Operator 7 [=Without, +=Addition, -=Subtraction]
  OP_8 VarChar(1) Operator 8 [=Without, +=Addition, -=Subtraction]
  OP_9 VarChar(1) Operator 9 [=Without, +=Addition, -=Subtraction]
  OP_10 VarChar(1) Operator 10 [=Without, +=Addition, -=Subtraction]
  OP_11 VarChar(1) Operator 11 [=Without, +=Addition, -=Subtraction]
  OP_12 VarChar(1) Operator 12 [=Without, +=Addition, -=Subtraction]
  OP_13 VarChar(1) Operator 13 [=Without, +=Addition, -=Subtraction]
  OP_14 VarChar(1) Operator 14 [=Without, +=Addition, -=Subtraction]
  OP_15 VarChar(1) Operator 15 [=Without, +=Addition, -=Subtraction]
  OP_16 VarChar(1) Operator 16 [=Without, +=Addition, -=Subtraction]
  OP_17 VarChar(1) Operator 17 [=Without, +=Addition, -=Subtraction]
  OP_18 VarChar(1) Operator 18 [=Without, +=Addition, -=Subtraction]
  OP_19 VarChar(1) Operator 19 [=Without, +=Addition, -=Subtraction]
  OP_20 VarChar(1) Operator 20 [=Without, +=Addition, -=Subtraction]
  OP_21 VarChar(1) Operator 21 [=Without, +=Addition, -=Subtraction]
  OP_22 VarChar(1) Operator 22 [=Without, +=Addition, -=Subtraction]
  OP_23 VarChar(1) Operator 23 [=Without, +=Addition, -=Subtraction]
  OP_24 VarChar(1) Operator 24 [=Without, +=Addition, -=Subtraction]
  ProfitLoss VarChar(1) Profit and Loss default=N [Y=Yes, N=No]
  MoveNeg VarChar(1) Move if Negative default=N [Y=Yes, N=No]
  Dummy VarChar(1) Dummy Title default=N [Y=Yes, N=No]
  HideAct VarChar(1) Hide Accounts default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  ToGroup Int(6) Move to Group default=0
  ToTitle Int(6) Move to Title default=0
  LineNum nVarChar(6) Line Number
  IndentChar nVarChar(6) Indent Char.
  Reversal VarChar(1) Reversal Sign default=N [N=No, Y=Yes]
  TextTitle VarChar(1) Text Title default=N [N=No, Y=Yes]
  SumType VarChar(1) Gross/Correction/Net default=N [B=Gross, C=Correction, N=Net]
  NetIncome VarChar(1) Net Income default=N [N=No, Y=Yes]
  PLTempId Int(11) Profit & Loss Report Template
  CustName VarChar(1) Customized Account Name default=N [Y=Yes, N=No]
  ExtFromBS VarChar(1) Relevant for Bal. Sht Extract default=N [Y=Yes, N=No]
  ExtData VarChar(1) Extended Data default=N [A=Relevant for Asset History Sheet, L=Relevant for Liabilities History Sheet, N=Not Relevant]
  LegalRef nVarChar(150) Legal Reference
  PLCatId Int(6) Profit & Loss Report Category default=0
  SignAggr VarChar(1) Sign for Aggregation default=E [E=, P=Positive, N=Negative]
  Mandatory VarChar(1) Mandatory default=N [Y=Yes, N=No]
  AcctReq VarChar(1) Account Verification Required default=N [Y=Yes, N=No]
  NotPermit VarChar(1) Not Permitted for Tax default=N [Y=Yes, N=No]
  KPIFactor nVarChar(3) KPI Factor No. ->OKPF
  CatCode nVarChar(15) Category Code
  CatClass VarChar(1) Category Classification [A=Asset, L=Liabilities, E=Equity, D=Expenses, R=Revenues]
