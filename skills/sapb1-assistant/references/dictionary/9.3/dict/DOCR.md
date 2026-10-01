<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# DOCR - DOCR
Module: General | 60 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RevCode, ResCode, Language, Numerator, Local, TypeCode
  TYP_LOC_NM: Numerator, Local, TypeCode
  TYPE_LOC: Local, TypeCode
  TYPE: TypeCode
Fields (name type(len) description [values] ->parent table):
  DocCode nVarChar(8) Code
  DocName nVarChar(64) Report Name
  Author nVarChar(32) Author
  Notes nVarChar(254) Remarks
  Width Int(6) Width default=595
  Height Int(6) Height default=842
  LMargin Int(6) Left Margin default=10
  RMargin Int(6) Right Margin default=30
  TMargin Int(6) Top Margin default=10
  BMargin Int(6) Bottom Margin default=10
  CanChange Int(6) Changable default=1 [1=TRUE, 0=FALSE]
  PaperSize nVarChar(100) Paper Size default=A4 210 x 297 mm
  Oreint VarChar(1) Orientation default=P [P=Vertical, L=Horizontal]
  GridSize Int(6) Grid Size default=10
  GridType VarChar(1) Grid Type default=1 [1=Compbination, 2=Continuous line, 3=Broken line, 4=Dots]
  ShowGrid VarChar(1) Display Grid default=1 [1=TRUE, 0=FALSE]
  SnapGrid VarChar(1) Next to Grid default=1 [1=TRUE, 0=FALSE]
  Picture Text(16) Picture
  TypeCode nVarChar(4) Type Code
  FrgnReport VarChar(1) Foreign Language Report default=0 [1=TRUE, 0=FALSE]
  CanSort Int(6) Sortable default=1 [1=TRUE, 0=FALSE]
  LeaderCode nVarChar(8) Leader Report
  FollowCode nVarChar(8) Follow-Up Report
  SwapOnScrn Int(6) Convert Font in Print Preview default=0 [1=Yes, 0=FALSE]
  ScreenFont nVarChar(50) Preview Printing Font default=Arial
  ScrFOffset Int(6) Change Font Size in Preview Pr default=-1
  SwpInEmail Int(6) Convert Font for E-mail default=0 [1=Yes, 0=FALSE]
  EmailFont nVarChar(50) E-Mail Font default=Arial
  EmFOffset Int(6) Change Font Size for E-Mail default=-1
  QString Text(16) Query
  QType VarChar(1) Query Type default=R [R=Regular, W=Wizard]
  Language Int(6) Language
  RobjCode Int(11) Imp Exp Obj Code default=0
  ExtName Text(16) Extension Name
  ExtOnErr VarChar(1) Action Taken On Ext Error default=S [S=Stop, I=Ignore, P=Promt]
  NumRepArs Int(6) Number of Repetitive Areas default=1
  AlgnFooter VarChar(1) Allign Footer to Buttom default=N [Y=Yes, N=No]
  Local nVarChar(2) Localization
  Numerator Int(6) Numerator
  NextAppId Int(6) Next Item AppId default=1
  Created Date(8) Creation Date
  Updated Date(8) Updated Date
  UsrSgnStr Int(11) User Sign For Strings Change default=-1
  UsrSgnAttr Int(11) User Sign For Attribs Change default=-1
  TimeFormat VarChar(1) Time Template default=0 [0=Default, 1=24H, 2=12H]
  DateFormat VarChar(1) Date Template default=0 [0=Default, 1=DD/MM/YY, 2=DD/MM/CCYY, 3=MM/DD/YY, 4=MM/DD/CCYY, 5=CCYY/MM/DD, 6=DD/Month/YYYY]
  DateSep VarChar(1) Date Separator
  DecSep VarChar(1) Decimal Separator
  ThousSep VarChar(1) Thousands Separator
  Printer nVarChar(100) Printer
  NumLayPage Int(11) Number of Layout Pages
  NumCopy Int(11) Number of Copies default=1
  GbiSupport VarChar(1) GBI settings supported default=N [Y=Yes, N=No]
  Use1stPrtr VarChar(1) Use 1st page printer default=N [Y=Yes, N=No]
  Prtr1st nVarChar(100) Printer for First Page
  Shading VarChar(1) Print item backgrounds default=Y [Y=Yes, N=No]
  ForceExpXX VarChar(1) Force Export XX Report default=N [Y=Yes, N=No]
  ResCode Int(11) Resource Code from RSBD default=-1
  RevCode Int(11) Revision Code default=-1
  UseSysPref VarChar(1) Use System Preference default=Y [Y=Yes, N=No]
