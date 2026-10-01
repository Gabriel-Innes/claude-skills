<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# IWZ3 - Items Last Revaluation Data
Module: Finance | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WhCode, ItemCode, AbsEntry
  ABS: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OIWZ
  ItemCode nVarChar(50) Item Number ->OITM
  WhCode nVarChar(8) Warehouse Code ->OWHS
  RevalPrice Num(19,6) Revaluated Price
  BaseCurr nVarChar(3) Item Base Currency
  RevalDate Date(8) Revaluation Date
  RevalSum Num(19,6) Revaluation Sum
  BasePrice Num(19,6) Base Price
  RealAcct nVarChar(15) Revaluation Account ->OACT
  RevalOfsac nVarChar(15) Reval. Offset Account ->OACT
  RevalType VarChar(1) Revaluation Type default=S [S=Inventory Reval. Type, C=COGS Revaluation Type]
  ExeLine VarChar(1) Executed Row default=Y [Y=Yes, N=No]
  RevCancel VarChar(1) Revaluation Cancel default=N [N=No, Y=Yes]
  RvCaclDate Date(8) Reval. Acct Cancellation Date
  Quantity Num(19,6) Quantity
  BalanceBef Num(19,6) Balance Before Revaluation
