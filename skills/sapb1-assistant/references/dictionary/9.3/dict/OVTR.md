<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OVTR - Tax Report
Module: Finance | 78 columns | ObjType: 180
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  NAME U: FilterType, ReportName
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Abs Entry (Numerator)
  ReportName nVarChar(50) Report Name
  RptLayout VarChar(1) Report Layout default=R [R=Tax Register Book, D=Tax Declaration, B=Black List Country - Tax Declaration, L=Black List Country - Tax Declaration 2013, A=VAT Annual List, I=Annual Invoice Declaration 2011, N=Annual Invoice Declaration 2013, P=Declaration of Purchases from San Marino, E=Electronic Tax Declaration, F=Electronic Tax Declaration 2018, M=VAT Invoice Declaration 2017]
  FirstPrint Int(11) First Printed No.
  FromDate Date(8) Date From
  ToDate Date(8) Date To
  TaxDate VarChar(1) Document Date default=N [N=No, Y=Yes]
  RoundSum VarChar(1) Round Amounts default=N [N=No, Y=Yes, =.]
  Declration VarChar(1) Declaration Type default=O [O=Original, S=Substitute, C=Complementary]
  FilterType VarChar(1) Selection Criteria Type default=N [V=Tax Report, W=Withholding Tax Report, T=Report 347, E=349 Report, R=Reconciliation Report, S=Stamp Tax, U=Sales Report, N=None, B=Box Report, O=Appendix O or P Selection, A=Annual Sales Report, F=VAT Refund Report, C=Input/Output VAT Report]
  ExcludeWT VarChar(1) Exclude Withholding Tax default=N [N=No, Y=Yes]
  CustomerIn VarChar(1) Include Customers default=Y [Y=Yes, N=No]
  VendorIn VarChar(1) Include Vendors default=Y [N=No, Y=Yes]
  Period VarChar(1) Quarter, Year or Month default=Q [Q=Quarter, Y=Year, M=Month, S=.]
  Quarter Int(11) Quarter
  Year Int(11) Year
  DocType VarChar(1) A/P or A/R default=P [P=Purchasing Documents, R=Sales Documents]
  CreditMemo VarChar(1) Credit Memos default=N [N=No, Y=Yes]
  DocTypeIn VarChar(1) Include Document Type default=N [N=No, Y=Yes]
  FirstReg Int(11) First Register Number
  AccountIn VarChar(1) Include G/L Accounts default=N [N=No, Y=Yes]
  DeferTaxIn VarChar(1) Show Pmts with Deferred Tax default=Y [Y=Yes, N=No]
  ApndxOOrP VarChar(1) Appendix O or P Selection default=Y [Y=Yes, N=No]
  DispOBCB VarChar(1) Opening & Closing Balance default=Y [N=No, Y=Yes]
  FromSeries Int(11) From Tax Series Group
  ToSeries Int(11) To Tax Series Group
  canceltn VarChar(1) For EU Sales Report default=N
  HideNTrans VarChar(1) Hide Tax Codes with no Trans. default=N [N=No, Y=Yes]
  SeriesIn VarChar(1) Include Series Filter default=N [N=No, Y=Yes]
  UserCode nVarChar(25) User Code
  FromCardCo nVarChar(15) BP Code From
  ToCardCo nVarChar(15) BP Code To
  SizeOfStru Int(11) Size of Structure
  PostFrDate Date(8) Posting Date From
  PostToDate Date(8) Posting Date To
  DocFrDate Date(8) Document Date From
  DocToDate Date(8) Document Date To
  FromDoc1Nu nVarChar(11) Document 1 - From
  ToDoc1Nu nVarChar(11) Document 1 - To
  Serie1 nVarChar(11) Invoice Numbering Series default=Y [Y=Yes, N=No]
  Serie1CB VarChar(1) Inv. Numbering Series Filter default=N [Y=Yes, N=No]
  Doc1Type Int(11) Type of Document 1
  FromDoc2Nu nVarChar(11) Document 2 - From
  ToDoc2Nu nVarChar(11) Document 2 - To
  Serie2 nVarChar(11) Credit Memo Numbering Series default=Y [Y=Yes, N=No]
  Serie2CB VarChar(1) Corr. Inv. Rev. No. Series default=N [Y=Yes, N=No]
  Doc2Type Int(11) Type of Document 2
  FromDoc3Nu nVarChar(11) Document 3 - From
  ToDoc3Nu nVarChar(11) Document 3 - To
  Serie3 nVarChar(11) Corr. Inv. Numbering Series default=Y [Y=Yes, N=No]
  Serie3CB VarChar(1) Corr. Inv. Num. Series Filter default=N [Y=Yes, N=No]
  Doc3Type Int(11) Type of Document 3
  FromDoc4Nu nVarChar(11) Document 4 - From
  ToDoc4Nu nVarChar(11) Document 4 - To
  Serie4 nVarChar(11) Corr. Inv. Rev. No. Series default=Y [Y=Yes, N=No]
  Serie4CB VarChar(1) Corr. Inv. Reversal No. Series default=N [Y=Yes, N=No]
  Doc4Type Int(11) Type of Document 4
  FromDoc5Nu nVarChar(11) Document 5 - From
  ToDoc5Nu nVarChar(11) Document 5 - To
  Serie5 nVarChar(11) Down Payment Numbering Series default=Y [Y=Yes, N=No]
  Serie5CB VarChar(1) Down Payment Numbering Series default=N [Y=Yes, N=No]
  Doc5Type Int(11) Type of Document 5
  DateRBtn VarChar(1) Report Period default=I [I=Interval, D=Date]
  MarkDocsIn VarChar(1) Include Marketing Documents default=Y [N=No, Y=Yes]
  ExRate VarChar(1) Exchange Rate default=P [P=Posting, R=For Reports]
  ExRateDate VarChar(1) Exchange Rate Date default=P [P=Posting Date, D=Document Date, V=VAT Date]
  TrsPerioTp VarChar(1) Report Period Type [Y=Year, Q=Quarter, M=Month, P=Period]
  TrsPerioNu Int(11) Report Period Number
  TrsYear Int(6) Report Year
  TrsAdjtNum Int(6) Report Adjustment Number
  DateType VarChar(1) Date Type default=P [P=Posting Date, D=Document Date, V=VAT Date, C=System Date]
  IncServDoc VarChar(1) Include Service Documents default=Y [Y=Yes, N=No]
  GrpBySCode VarChar(1) Group by Sales Code default=Y [Y=Yes, N=No]
  IncUnReDoc VarChar(1) Include Unreconciled Documents default=Y [Y=Yes, N=No]
  DoYearSum VarChar(1) Year Summary [Y=Yes, N=No]
  DefTaxOnly VarChar(1) Only Include Deferred Tax Docs default=N [Y=Yes, N=No]
  ExcElDoc VarChar(1) Exclude Electronic Documents default=N [Y=Yes, N=No]
  QtrByMnt VarChar(1) Quarter by Months default=N [Y=Yes, N=No]
