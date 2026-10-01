<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# IPF2 - Landed Costs - Costs
Module: Inventory and Production | 18 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CostType, AlcCode, DocEntry
  NUM: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Landed Costs Internal ID ->OIPF
  LineNum Int(11) Row Number
  AlcCode nVarChar(2) Cost Code ->OALC
  OhType VarChar(1) Load by [F=Cash Value Before Customs, C=Cash Value After Customs, Q=Quantity, W=Weight, V=Volume, A=Equal, L=Legal Cost]
  CostSum Num(19,6) Total Costs
  CostSumFC Num(19,6) Total Costs (FC)
  Factor Num(19,6) Factor
  CostType VarChar(1) Cost Type default=F [F=Fixed Costs, V=Variable Costs, L=Legal Costs]
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  LaCAllcAcc nVarChar(15) Landed Costs Alloc. Account
  CostSumSC Num(19,6) Total Costs (SC)
  InCustCalc VarChar(1) Included in Customs Calc default=N [Y=Yes, N=No]
  OpenCost Num(19,6) Open Costs
  OpenCostFC Num(19,6) Open Costs (FC)
  OpenCostSC Num(19,6) Open Costs (SC)
  AgentCode nVarChar(15) Subst. Code
  AgentName nVarChar(100) Subst. Name
  CostCateg VarChar(1) Cost Category [V=Customs VAT, E=Excise Cost, D=Customs Duty]
