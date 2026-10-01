<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# FTT1 - Financial Template Import - Files
Module: Administration | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OFTT
  LineNum Int(11) Row Number
  FileName nVarChar(254) Data Definition File Name
  ReleaDate Date(8) Release Date
  Descript nVarChar(100) Description
  Localizat nVarChar(3) Localization
  ChartAcct nVarChar(128) Chart of Accounts
  DocType VarChar(1) Template Type default=B [B=Balance Sheet, P=Profit and Loss, C=Trial Balance, F=Statement of Cash Flows, S=Sales Unit, T=Form 6111, A=Cost Accounting, E=Asset Devalue Provision, R=Shareholder's Rights and Interests Changing, D=Profit Distribution, V=VAT Payable Detail, L=e-Balance Sheet, O=e-Profit and Loss, H=Asset History Sheet, G=Others, I=Taxable Profit and Loss, J=Appropriation of Net Profit, K=E-Asset History Sheet]
  DimCode Int(11) Dimension Code ->ODIM
