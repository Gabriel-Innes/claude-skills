<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OARG - Customs Groups
Module: Inventory and Production | 16 columns | ObjType: 56
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CstGrpCode
  GROUP_NAME U: CstGrpName
Fields (name type(len) description [values] ->parent table):
  CstGrpCode Int(6) Code
  CstGrpName nVarChar(20) Name
  GroupNum nVarChar(20) Number
  Custom Num(19,6) Customs
  BuyTax Num(19,6) Purchase
  OtherTax Num(19,6) Other
  TotalTax Num(19,6) Total
  Locked VarChar(1) Locked default=N [N=Changeable, Y=Locked]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  cstAllcAcc nVarChar(15) Customs Allocation Account ->OACT
  cstExpAcc nVarChar(15) Customs Expense Account ->OACT
  PortAddr nVarChar(50) Local Clearance - Port Address
  PortState nVarChar(3) Port State
  ExciExpAcc nVarChar(15) Excise Expense Account ->OACT
  ExciAlcAcc nVarChar(15) Excise Allocation Account ->OACT
