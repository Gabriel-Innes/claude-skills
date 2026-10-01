<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OBOX - Box Definition
Module: Finance | 16 columns | ObjType: 216
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: BosCode, ReportType, BoxCode
Fields (name type(len) description [values] ->parent table):
  BoxCode nVarChar(30) Code
  BoxName nVarChar(250) Name
  BoxType VarChar(1) Type default=V [V=VAT Group, B=Box, A=Account, M=Manual Input, T=Manual Text Input, F=Formula, S=Single Choice]
  SummayFld VarChar(1) Summary Field default=S [B=Base Amount, T=Tax Amount, Q=EQ Base Amount, E=EQ Tax Amount, N=Non-Deductible Amount, S=]
  DbtCrdt VarChar(1) Debit/Credit default=S [D=Debit Side, C=Credit Side, B=Debit Side and Credit Side, S=]
  Formula nVarChar(250) Formula Syntax
  SortOrder Int(11) Sort Order
  AbsolutVa VarChar(1) Absolute Value default=N [Y=Yes, N=No]
  ReportType VarChar(1) Report Type default=B [B=Box Declaration, S=BAS Report, X=BAS Report - Empty Effective Date Holder]
  Inactive VarChar(1) Inactive default=N [Y=Yes, N=No]
  EffecDate Date(8) Effective From
  DecLoc VarChar(1) Declaration Location default=B [B=, C=Continent, M=Madeira, A=Azores]
  BosCode Int(11) Box Set Code ->OBOS
  Position nVarChar(250) Position in Report
  PostToAct nVarChar(15) Post-To Account ->OACT
  PostToOffA nVarChar(15) Post-To Offset Account ->OACT
