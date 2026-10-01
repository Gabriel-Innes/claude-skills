<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OFLT - Report - Selection Criteria
Module: Reports | 292 columns | ObjType: 54
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: FormNum, UserSign, FilterName
Fields (name type(len) description [values] ->parent table):
  FormNum nVarChar(20) Form Number
  QueryStr nVarChar(250) Query
  ItmOrCrd VarChar(1) Items or BP default=Y [Y=Yes, N=No]
  CardInclud VarChar(1) BP Area default=Y [Y=Yes, N=No]
  CardFrom1 nVarChar(15) From BP ->OCRD
  CardTo1 nVarChar(15) To BP ->OCRD
  CardExclud VarChar(1) Excluding BP default=N [Y=Yes, N=No]
  CardFrom2 nVarChar(15) BP Rejected
  CardTo2 nVarChar(15) BP Rejected
  ClienGroup Int(6) Customer Group
  VendGroup Int(6) Vendor Group
  ClntQryGrp nVarChar(250) Customer Properties
  VeQryGroup nVarChar(250) Vendor Properties
  ItmInclud VarChar(1) Item Range default=Y [Y=Yes, N=No]
  ItmFrom1 nVarChar(50) From Item ->OITM
  ItmTo1 nVarChar(50) To Item ->OITM
  ItmExclud VarChar(1) Excluding Materials default=N [Y=Yes, N=No]
  ItmFrom2 nVarChar(50) Item Rejected ->OITM
  ItmTo2 nVarChar(50) Item Rejected ->OITM
  ItmGroup Int(6) Item Group ->OITB
  ItQryGroup nVarChar(250) Item Properties
  WhsInclude VarChar(1) Warehouse Range default=Y [Y=Yes, N=No]
  WhsFrom1 nVarChar(8) From Warehouse ->OWHS
  WhsTo1 nVarChar(8) To Warehouse ->OWHS
  WhsExclude VarChar(1) Excluding Warehouses default=N [Y=Yes, N=No]
  WhsFrom2 nVarChar(8) Warehouse Rejected
  WhsTo2 nVarChar(8) Warehouse Rejected
  FromAcct nVarChar(15) From Account
  ToAcct nVarChar(15) To Account
  GroupMask nVarChar(12) Group Mask
  FromDate Date(8) From Posting Date
  ToDate Date(8) To Posting Date
  FrmDueDate Date(8) Due Date From
  ToDueDate Date(8) Due Date To
  FromDate3 Date(8) From Date 3
  ToDate3 Date(8) To Date 3
  FromDate4 Date(8) From Date 4
  ToDate4 Date(8) To Date 4
  SourceType Int(6) Original Journal default=-1 [15=Delivery, 16=Returns, 203=A/R Down Payment, 13=A/R Invoice, 14=A/R Credit Memo, 132=Correction Invoice, 20=Goods Receipt, 21=Goods Returns, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 69=Landed Costs, 163=A/P Correction Invoice, 24=Incoming Payment, 25=Deposit, 46=Vendor Payment, 57=Checks for Payment, 76=Postdated Deposit, -2=Opening Balance, -3=Closing Balance, 30=Journal Entry, 58=Stock Update, 59=Goods Receipt, 60=Goods Issue, 67=Inventory Transfers, 68=Work Instructions, 162=Inventory Valuation, -1=All Transactions]
  FrmTrnsNum Int(11) From Transaction No.
  ToTrnsNum Int(11) To Transaction No.
  FromRef1 nVarChar(100) From Reference 1
  ToRef1 nVarChar(100) To Reference 1
  FromRef2 nVarChar(100) From Reference 2
  ToRef2 nVarChar(100) To Reference 2
  FrmTrnsCod nVarChar(4) From Transaction Code
  ToTrnsCod nVarChar(4) To Transaction Code
  FromSum Num(19,6) From Amount
  ToSum Num(19,6) To Amount
  FrmFRNAmnt Num(19,6) From FC Amount
  ToFRNAmnt Num(19,6) To FC Amount
  MemoIn nVarChar(50) Details Contained
  SortField1 Int(6) Sort Field 1 default=-1
  Break1 VarChar(1) Subtotal by Sort 1 default=N [Y=Yes, N=No]
  SortField2 Int(6) Sort Field 2 default=-1
  Break2 VarChar(1) Subtotal by Sort 2 default=N [Y=Yes, N=No]
  SortField3 Int(6) Sort Field 3 default=-1
  Break3 VarChar(1) Subtotal by Sort 3 default=N [Y=Yes, N=No]
  Display VarChar(1) Display default=L [L=Postings Only, T=Totals Only, B=Postings + Totals]
  PrntCutDat VarChar(1) Print Date Selection Criteria default=Y [Y=Yes, N=No]
  CheckBox0 VarChar(1) Check box 0 default=N [Y=Yes, N=No]
  CheckBox1 VarChar(1) Check box 1 default=N [Y=Yes, N=No]
  CheckBox2 VarChar(1) Check box 2 default=N [Y=Yes, N=No]
  CheckBox3 VarChar(1) Check box 3 default=N [Y=Yes, N=No]
  CheckBox4 VarChar(1) Check box 4 default=N [Y=Yes, N=No]
  CheckBox5 VarChar(1) Check box 5 default=N [Y=Yes, N=No]
  CheckBox6 VarChar(1) Check box 6 default=N [Y=Yes, N=No]
  CheckBox7 VarChar(1) Check box 7 default=N [Y=Yes, N=No]
  CheckBox8 VarChar(1) Check box 8 default=N [Y=Yes, N=No]
  CheckBox9 VarChar(1) Check box 9 default=N [Y=Yes, N=No]
  ShowZero VarChar(1) Display Zero Balances default=N [Y=Yes, N=No]
  DateCheck VarChar(1) Confirm Date Range default=N [Y=Yes, N=No]
  DueCheck VarChar(1) Confirm Due Date Range default=N [Y=Yes, N=No]
  CutCheck VarChar(1) Confirm Date Selectn Criteria default=N [Y=Yes, N=No]
  CutByObj VarChar(1) Selection Criteria by Object default=N [Y=Yes, N=No]
  ObjectC1 VarChar(1) C1 default=N [Y=Yes, N=No]
  ObjectC2 VarChar(1) C2 default=N [Y=Yes, N=No]
  ObjectC3 VarChar(1) C3 default=N [Y=Yes, N=No]
  ObjectC4 VarChar(1) C4 default=N [Y=Yes, N=No]
  ObjectC5 VarChar(1) C5 default=N [Y=Yes, N=No]
  ObjectC6 VarChar(1) C6 default=N [Y=Yes, N=No]
  ObjectC7 VarChar(1) C7 default=N [Y=Yes, N=No]
  ObjectC8 VarChar(1) C8 default=N [Y=Yes, N=No]
  ObjectC9 VarChar(1) C9 default=N [Y=Yes, N=No]
  ObjectC10 VarChar(1) C10 default=N [Y=Yes, N=No]
  ObjectC11 VarChar(1) C11 default=N [Y=Yes, N=No]
  ObjectC12 VarChar(1) C12 default=N [Y=Yes, N=No]
  ObjectC13 VarChar(1) C13 default=N [Y=Yes, N=No]
  ObjectC14 VarChar(1) C14 default=N [Y=Yes, N=No]
  ObjectC15 VarChar(1) C15 default=N [Y=Yes, N=No]
  ObjectC16 VarChar(1) C16 default=N [Y=Yes, N=No]
  FromAmount Num(19,6) From Amount
  ToAmount Num(19,6) To Amount
  FrmSalsMan Int(6) From Sales Employee
  ToSalsMan Int(6) To Sales Employee
  USER_CHK1 VarChar(1) User CheckBox 1 default=N [Y=Yes, N=No]
  USER_CHK2 VarChar(1) User CheckBox 2 default=N [Y=Yes, N=No]
  USER_CHK3 VarChar(1) User CheckBox 3 default=N [Y=Yes, N=No]
  USER_CHK4 VarChar(1) System Currrency default=N [Y=Yes, N=No]
  USER_CHK5 VarChar(1) System and Local Currency default=N [Y=Yes, N=No]
  UseSort VarChar(1) Sort default=N [Y=Yes, N=No]
  Sort1Up VarChar(1) Sort1 default=Y [Y=Ascending, N=Descending]
  Sort2Up VarChar(1) Sort2 default=Y [Y=Ascending, N=Descending]
  Sort3Up VarChar(1) Sort3 default=Y [Y=Ascending, N=Descending]
  FromAmnt2 Num(19,6) From Quantity Release
  ToAmount2 Num(19,6) For Quantity Release
  TaxDateFro Date(8) Lower Limit for Tax Data
  TaxDateTo Date(8) Top Limit for Document Dates
  FinancYear Date(8) Start of Fiscal Year
  BdgtScenar Int(11) Budget Scenario
  CompFolder nVarChar(100) Company Database
  CheckBox10 VarChar(1) Exapan Check Box 1 default=N [Y=Yes, N=No]
  FROM_FC Num(19,6) Foreign Currency from
  TO_FC Num(19,6) Foreign Currency to
  FCCurrency nVarChar(3) Foreign Currency
  TaxCheck VarChar(1) Confirm Document Date Range default=N [Y=Yes, N=No]
  DateType VarChar(1) Selection Criteria Type default=R [R=Posting Date, D=Due Date, T=Document Date]
  DateType2 VarChar(1) Selection Criteria Type default=R [R=Posting Date, D=Due Date, T=Document Date]
  FromPrject nVarChar(20) From Project ->OPRJ
  ToProject nVarChar(20) To Project ->OPRJ
  TemplateId Int(11) Template default=0
  ShowLeads VarChar(1) Display Leads default=N [Y=Yes, N=No]
  MthDate VarChar(1) Reconciliation Date default=N [Y=Yes, N=No]
  AccntntCod VarChar(1) External Code default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  BlcNunFrom nVarChar(100) Block Number From
  BlcNunTo nVarChar(100) Block Number To
  ImpLogFrom nVarChar(20) Import Log From
  ImpLogTo nVarChar(20) Import Log To
  FolderNum VarChar(1) Folder Number default=1
  MainField Int(6) Main Field default=23
  TransMode VarChar(1) Transaction Mode default=Y [Y=Yes, N=No]
  MonthMode VarChar(1) Month Totals Mode default=N [Y=Yes, N=No]
  CheckBox11 VarChar(1) Expan Check Box 11 default=N [Y=Yes, N=No]
  FromIdc nVarChar(2) Indicator From
  ToIdc nVarChar(2) Indicator To
  IgnoreAdj VarChar(1) Ignore Adjustments default=N [Y=Yes, N=No]
  RefNumFrom nVarChar(254) From Reference No.
  RefNumTo nVarChar(254) To Reference No.
  PymNumfrom Int(11) Payment No. From
  PymNumTo Int(11) To Payment No.
  BankFrom nVarChar(30) From Bank Code
  BankTo nVarChar(30) To Bank Code
  DpstFrom Int(11) From Deposit Code
  DpstTo Int(11) To Deposit Code
  DpstType VarChar(1) Deposit Type
  ObjectC17 VarChar(1) Obj C17 default=N [Y=Yes, N=No]
  ObjectC18 VarChar(1) Obj C18 default=N [Y=Yes, N=No]
  ObjectC19 VarChar(1) Obj C19 default=N [Y=Yes, N=No]
  ObjAbs Int(11) Document Internal Number
  AddBTF VarChar(1) Add Journal Vouchers default=N [Y=Yes, N=No]
  FilePath Text(16) File Path
  DpsBnkActF nVarChar(50) From Deposit Bank Account
  DpsBnkActT nVarChar(50) To Deposit Bank Account
  FromKey Int(11) From Key
  ToKey Int(11) To Key
  ObjectC20 VarChar(1) Object C20 default=N [Y=Yes, N=No]
  ObjectC21 VarChar(1) Object C21 default=N [Y=Yes, N=No]
  ObjectC22 VarChar(1) Object C22 default=N [Y=Yes, N=No]
  ObjectC23 VarChar(1) Object C23 default=N [Y=Yes, N=No]
  ObjectC25 VarChar(1) Object C25 default=N [Y=Yes, N=No]
  USER_CHK6 VarChar(1) Include CB in P/L Accounts default=N [Y=Yes, N=No]
  OcrChkDim2 VarChar(1) Checkbox for Dimension 2 default=N [Y=Yes, N=No]
  OcrChkDim3 VarChar(1) Checkbox for Dimension 3 default=N [Y=Yes, N=No]
  OcrChkDim4 VarChar(1) Checkbox for Dimension 4 default=N [Y=Yes, N=No]
  OcrChkDim5 VarChar(1) Checkbox for Dimension 5 default=N [Y=Yes, N=No]
  OcrFrom2 nVarChar(8) From Costing Code 2 ->OOCR
  OcrFrom3 nVarChar(8) From Costing Code 3 ->OOCR
  OcrFrom4 nVarChar(8) From Costing Code 4 ->OOCR
  OcrFrom5 nVarChar(8) From Costing Code 5 ->OOCR
  OcrTo2 nVarChar(8) To Costing Code 2 ->OOCR
  OcrTo3 nVarChar(8) To Costing Code 3 ->OOCR
  OcrTo4 nVarChar(8) To Costing Code 4 ->OOCR
  OcrTo5 nVarChar(8) To Costing Code 5 ->OOCR
  TaxAdjRep Text(16) Object C24
  ObjectC26 VarChar(1) Object C26 default=N [Y=Yes, N=No]
  CBFilter VarChar(1) Closing Balances Filter default=2 [1=Closing Balance of Life-to-Date, 2=Closing Balance Before Selected Period Only]
  OBIncluded VarChar(1) Add Opening Balance for Period default=N [Y=Yes, N=No]
  OBFilter VarChar(1) Opening Balances Filter default=1 [1=Opening Balance from Start of Company Activity, 2=Opening Balance from Start of Fiscal Year]
  ExportCurr VarChar(1) Export Currency default=L [L=Local Currency, S=System Currency]
  CBIncluded VarChar(1) Add Closing Balances default=N [Y=Yes, N=No]
  SlpFrom nVarChar(155) Slp From
  SlpTo nVarChar(155) Slp To
  CBUDF VarChar(1) User-Defined Fields default=N [Y=Yes, N=No]
  CBREF VarChar(1) Reference Fields default=N [Y=Yes, N=No]
  CheckBoxB VarChar(1) Checkbox for Branch default=N [Y=Yes, N=No]
  FilterName nVarChar(30) Filter Name default=_
  JDTFixedF Int(6) JE Fixed Fields
  JDT1FixedF Int(6) JE Line Fixed Fields
  JDTUserF Int(6) JE User Fields
  JDT1UserF Int(6) JE Line User Fields
  BPFilter VarChar(1) BP Filter Enabled default=N [Y=Yes, N=No]
  AcctFltr VarChar(1) Account Filter Enabled default=N [Y=Yes, N=No]
  ZeroLCAmt VarChar(1) Show Zero LC Amount Lines default=N [Y=Yes, N=No]
  SplitByBin VarChar(1) Split By Bin Location default=N [Y=Yes, N=No]
  SplitBySnb VarChar(1) Split By Batch/Serial default=N [Y=Yes, N=No]
  CheckBox12 VarChar(1) Check Box 12 default=N [Y=Yes, N=No]
  CheckBox13 VarChar(1) Check Box 13 default=N [Y=Yes, N=No]
  CheckBox14 VarChar(1) Check Box 14 default=N [Y=Yes, N=No]
  CheckBox15 VarChar(1) Check Box 15 default=N [Y=Yes, N=No]
  CheckBox16 VarChar(1) Check Box 16 default=N [Y=Yes, N=No]
  CheckBox17 VarChar(1) Check Box 17 default=N [Y=Yes, N=No]
  CheckBox18 VarChar(1) Check Box 18 default=N [Y=Yes, N=No]
  CheckBox19 VarChar(1) Check Box 19 default=N [Y=Yes, N=No]
  CheckBox20 VarChar(1) Check Box 20 default=N [Y=Yes, N=No]
  CheckBox21 VarChar(1) Check Box 21 default=N [Y=Yes, N=No]
  CheckBox22 VarChar(1) Check Box 22 default=N [Y=Yes, N=No]
  CheckBox23 VarChar(1) Check Box 23 default=N [Y=Yes, N=No]
  CheckBox24 VarChar(1) Check Box 24 default=N [Y=Yes, N=No]
  CheckBox25 VarChar(1) Check Box 25 default=N [Y=Yes, N=No]
  CheckBox26 VarChar(1) Check Box 26 default=N [Y=Yes, N=No]
  CheckBox27 VarChar(1) Check Box 27 default=N [Y=Yes, N=No]
  CheckBox28 VarChar(1) Check Box 28 default=N [Y=Yes, N=No]
  CheckBox29 VarChar(1) Check Box 29 default=N [Y=Yes, N=No]
  CheckBox30 VarChar(1) Check Box 30 default=N [Y=Yes, N=No]
  CheckBox31 VarChar(1) Check Box 31 default=N [Y=Yes, N=No]
  CheckBox32 VarChar(1) Check Box 32 default=N [Y=Yes, N=No]
  CheckBox33 VarChar(1) Check Box 33 default=N [Y=Yes, N=No]
  BatchFrom nVarChar(36) Batch From
  BatchTo nVarChar(36) Batch To
  BatAttr1F nVarChar(36) Batch Attr. 1 From
  BatAttr1T nVarChar(36) Batch Attr. 1 To
  BatAttr2F nVarChar(36) Batch Attr. 2 From
  BatAttr2T nVarChar(36) Batch Attr. 2 To
  SerialNoF nVarChar(36) Serial Number From
  SerialNoT nVarChar(36) Serial Number To
  MfrSerailF nVarChar(36) Mfr Serial Number From
  MfrSerailT nVarChar(36) Mfr Serial Number To
  LotNumberF nVarChar(36) Lot Number From
  LotNumberT nVarChar(36) Lot Number To
  BinLocFrom nVarChar(228) Bin Location From
  BinLocTo nVarChar(228) Bin Location To
  AltSrtCodF nVarChar(50) Alternative Sort Code From
  AltSrtCodT nVarChar(50) Alternative Sort Code To
  BinSbl1F nVarChar(50) Bin Sublevel 1 From
  BinSbl1To nVarChar(50) Bin Sublevel 1 To
  BinSbl2F nVarChar(50) Bin Sublevel 2 From
  BinSbl2To nVarChar(50) Bin Sublevel 2 To
  BinSbl3F nVarChar(50) Bin Sublevel 3 From
  BinSbl3To nVarChar(50) Bin Sublevel 3 To
  BinSbl4F nVarChar(50) Bin Sublevel 4 From
  BinSbl4To nVarChar(50) Bin Sublevel 4 To
  BinAttr1F nVarChar(20) Bin Attribute 1 From
  BinAttr1To nVarChar(20) Bin Attribute 1 To
  BinAttr2F nVarChar(20) Bin Attribute 2 From
  BinAttr2To nVarChar(20) Bin Attribute 2 To
  BinAttr3F nVarChar(20) Bin Attribute 3 From
  BinAttr3To nVarChar(20) Bin Attribute 3 To
  BinAttr4F nVarChar(20) Bin Attribute 4 From
  BinAttr4To nVarChar(20) Bin Attribute 4 To
  BinAttr5F nVarChar(20) Bin Attribute 5 From
  BinAttr5To nVarChar(20) Bin Attribute 5 To
  BinAttr6F nVarChar(20) Bin Attribute 6 From
  BinAttr6To nVarChar(20) Bin Attribute 6 To
  BinAttr7F nVarChar(20) Bin Attribute 7 From
  BinAttr7To nVarChar(20) Bin Attribute 7 To
  BinAttr8F nVarChar(20) Bin Attribute 8 From
  BinAttr8To nVarChar(20) Bin Attribute 8 To
  BinAttr9F nVarChar(20) Bin Attribute 9 From
  BinAttr9To nVarChar(20) Bin Attribute 9 To
  BinAttr10F nVarChar(20) Bin Attribute 10 From
  BinAttr10T nVarChar(20) Bin Attribute 10 To
  EnfBinFltr VarChar(1) Enforced Bin Filter default=N [E=Enforced Bin Location, U=Unenforced Bin Location, B=Both, N=Bin not activated]
  ExItemFrom nVarChar(50) Expand from Item ->OITM
  ExItemTo nVarChar(50) Expand to Item ->OITM
  ExBPFrom nVarChar(15) Expand from BP ->OCRD
  ExBPTo nVarChar(15) Expand to BP ->OCRD
  CheckBox34 VarChar(1) Check Box 34 default=N [Y=Yes, N=No]
  CheckBox35 VarChar(1) Check Box 35 default=N [Y=Yes, N=No]
  BlAgreem VarChar(1) Checkbox for Blanket Agreement default=N
  BAFrom nVarChar(8) Blanket Agreement From
  BATo nVarChar(8) Blanket Agreement To
  AdjTrans VarChar(1) Adjustment Transactions default=N [Y=Yes, N=No]
  TitAcctLvl Int(11) Title Account Level default=2
  CCDFrom1 nVarChar(40) CCD Number from condition 1
  CCDTo1 nVarChar(40) CCD Number to Condition 1
  CCDFrom2 nVarChar(40) CCD Number from Condition 2
  CCDTo2 nVarChar(40) CCD Number to Condition 2
  ArchJrnal VarChar(1) Archiving Journal default=N [Y=Yes, N=No]
  CardFrom3 nVarChar(15) From BP
  CardTo3 nVarChar(15) To BP
  OBBranch VarChar(1) Divide Totals by Branch default=N [Y=Yes, N=No]
  AccumDbCr VarChar(1) Accumulated Debit/Credit default=N [Y=Yes, N=No]
  RscFrom1 nVarChar(50) From Resource ->ORSC
  RscTo1 nVarChar(50) To Resource ->ORSC
  RscGroup Int(6) Resource Group ->ORSB
  RouteStage VarChar(1) Use Route Stage default=N [Y=Yes, N=No]
  ExRSTFrom Int(11) From Route Stage ->ORST
  ExRSTTo Int(11) To Route Stage ->ORST
  StgSeqNum VarChar(1) Use Stage Sequence Number default=N [Y=Yes, N=No]
  ExSSNFrom Int(11) From Stage Sequence Number
  ExSSNTo Int(11) To Stage Sequence Number
