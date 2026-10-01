<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OFRT - Financial Report Templates
Module: Finance | 15 columns | ObjType: 95
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  SECOND U: Name, DocType
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Name nVarChar(100) Name
  DocType VarChar(1) Template Type default=B [B=Balance Sheet, P=Profit and Loss, C=Trial Balance, F=Statement of Cash Flows, S=Sales Unit, T=Form 6111, A=Cost Accounting, E=Asset Devalue Provision, R=Shareholder's Rights and Interests Changing, D=Profit Distribution, V=VAT Payable Detail, L=e-Balance Sheet, O=e-Profit and Loss, H=Asset History Sheet, G=Others, I=Taxable Profit and Loss, J=Appropriation of Net Profit, K=E-Asset History Sheet]
  FRTCounter Int(6) Financial Report Template Counter
  MoveChk1 VarChar(1) Move Chk1 default=N [Y=Yes, N=No]
  MoveChk2 VarChar(1) Move Chk2 default=N [Y=Yes, N=No]
  MoveTo_1 Int(6) Move To 1 default=0
  MoveTo_2 Int(6) Move To 2 default=0
  Title_1 nVarChar(100) Title 1
  Title_2 nVarChar(100) Title 2
  ShowMiss VarChar(1) Display Missing Accounts default=N [Y=Yes, N=No]
  ToTitle_1 Int(6) Move To Title 1 default=0
  ToTitle_2 Int(6) Move To Title 2 default=0
  UserSign Int(6) User Signature ->OUSR
  DimCode Int(11) In Which Dimension ->ODIM
