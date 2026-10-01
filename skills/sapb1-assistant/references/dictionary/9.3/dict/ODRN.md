<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ODRN - Depreciation Run
Module: Finance | 17 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  DprArea nVarChar(15) Depreciation Area ID ->ODPA
  Status VarChar(1) Status default=D [S=Depreciation Posted, N=No Depreciation Posted, C=Canceled, F=Failed, D=]
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  RefDate Date(8) Posting Date
  PeriodCat nVarChar(10) Period Category ID
  PostPeriod Int(11) Posting Subperiod
  KeyDate Date(8) Key Date
  Remarks nVarChar(32) Remarks
  NumOfJEs Int(11) No. of Journal Entries
  SumOfDpr Num(19,6) Sum of Depreciation
  SumByPro VarChar(1) Summarize by Project default=N [Y=Yes, N=No]
  SumByDistr VarChar(1) Summarize by Distribution Rule default=N [Y=Yes, N=No]
  TransType nVarChar(20) Generate Document default=-1 [-1=None, 18=A/P Invoice]
  TransAbs Int(11) Generate Doc. Abs. Entry
