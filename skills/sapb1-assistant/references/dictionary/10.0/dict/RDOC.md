<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# RDOC - Document
Module: Reports | 65 columns | ObjType: 232
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocCode
  TYPE: TypeCode
  TYPENAME: TypeCode, DocName
Fields (name type(len) description [values] ->parent table):
  DocCode nVarChar(8) Code
  DocName nVarChar(120) Name
  Author nVarChar(155) Author
  Notes nVarChar(254) Remarks
  Width Int(6) Width default=595
  Height Int(6) Height default=842
  LMargin Int(6) Left Margin default=10
  RMargin Int(6) Right Margin default=30
  TMargin Int(6) Top Margin default=10
  BMargin Int(6) Bottom Margin default=10
  CanChange VarChar(1) Changeable default=Y [Y=Yes, N=No]
  PaperSize nVarChar(100) Paper Size default=A4
  Oreint VarChar(1) Orientation default=P [P=Vertical, L=Horizontal]
  GridSize Int(6) Grid Size default=10
  GridType VarChar(1) Grid Type default=1 [1=Combination, 2=Continuous Line, 3=Broken Line, 4=Dots]
  ShowGrid VarChar(1) Display Grid default=Y [Y=Yes, N=No]
  SnapGrid VarChar(1) Next to Grid default=Y [Y=Yes, N=No]
  Picture Text(16) Picture
  TypeCode nVarChar(4) Type Code
  FrgnReport VarChar(1) Foreign Language Report default=N [Y=Yes, N=No]
  CanSort VarChar(1) Sortable default=Y [Y=Yes, N=No]
  LeaderCode nVarChar(8) Leader Report
  FollowCode nVarChar(8) Follow-Up Report
  SwapOnScrn VarChar(1) Convert Font in Print Preview default=N [Y=Yes, N=No]
  ScreenFont nVarChar(50) Preview Printing Font default=Arial
  ScrFOffset Int(6) Change Font Size in Print Preview default=-1
  SwpInEmail VarChar(1) Convert Font for E-Mail default=N [Y=Yes, N=No]
  EmailFont nVarChar(50) E-Mail Font default=Arial
  EmFOffset Int(6) Change Font Size for E-Mail default=-1
  QString Text(16) Query
  QType VarChar(1) Query Type default=R [R=Regular, W=Wizard]
  Language Int(11) Language ->OLNG
  RobjCode Int(11) Imp Exp Obj Code default=0
  ExtName Text(16) Extension Name
  ExtOnErr VarChar(1) Action for extension error default=S [S=Stop, I=Ignore, P=Prompt]
  NumRepArs Int(6) Number of Repetitive Areas default=1
  AlgnFooter VarChar(1) Allign Footer to Buttom default=N [Y=Yes, N=No]
  TimeFormat VarChar(1) Time Template default=0 [0=Default, 1=24H, 2=12H]
  DateFormat VarChar(1) Date Template default=0 [0=Default, 1=DD/MM/YY, 2=DD/MM/CCYY, 3=MM/DD/YY, 4=MM/DD/CCYY, 5=CCYY/MM/DD, 6=DD/Month/YYYY]
  DateSep VarChar(1) Date Separator
  DecSep VarChar(1) Decimal Separator
  ThousSep VarChar(1) Thousands Separator
  Printer nVarChar(100) Printer
  NumLayPage Int(11) Number of Layout Pages
  NumCopy Int(11) Number of Copies default=1
  GbiSupport VarChar(1) GBI Settings Supported default=N [Y=Yes, N=No]
  Use1stPrtr VarChar(1) Use 1st Page Printer default=N [Y=Yes, N=No]
  Prtr1st nVarChar(100) Printer for First Page
  Shading VarChar(1) Print Item Backgrounds default=Y [Y=Yes, N=No]
  Template Text(16) Report Binary Data
  Category VarChar(1) Category default=P [P=PLD, C=Crystal Reports, L=Legal List, A=Partner Type, E=Electronic Files]
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature
  UserSign2 Int(6) Updating User
  Status VarChar(1) Status default=A [A=Active, I=Inactive]
  B1Version nVarChar(20) Required B1 Version
  CRVersion nVarChar(20) Required Crystal Version
  Local nVarChar(2) Localization
  UseSysPref VarChar(1) Use System Preference default=Y [Y=Yes, N=No]
  ForMobile VarChar(1) Visible For Mobile default=Y [Y=Yes, N=No]
  TypeDetail nVarChar(254) Type
  IsIMCE VarChar(1) Powered by SAP HANA default=N [Y=Yes, N=No]
  CsUrl nVarChar(254) URL in Crystal Server
  RptHash nVarChar(254) Hash for Report
