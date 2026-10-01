<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ORSC - Resources
Module: General | 125 columns | ObjType: 290
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ResCode
  RES_CODE U: VisResCode
  ITEM_NAME: ResName
  SALE: PrchseRes
  PURCHASE: SellRes
  PRODUCTION: ProdRes
Fields (name type(len) description [values] ->parent table):
  ResCode nVarChar(50) Internal Code
  VisResCode nVarChar(50) Resource No.
  Series Int(11) Series ->NNM1
  Number Int(11) Number
  CodeBars nVarChar(254) Bar Code
  ResName nVarChar(100) Resource Description
  FrgnName nVarChar(100) Description in Foreign Lang.
  ResType VarChar(1) Resource Type default=M [M=Machine, L=Labor, O=Other]
  ResGrpCod Int(6) Resource Group default=1 ->ORSB
  UnitOfMsr nVarChar(100) Unit of Measure
  PrchseRes VarChar(1) Purchase Resource [Yes/No] default=Y [Y=Yes, N=No]
  SellRes VarChar(1) Sales Resource [Yes/No] default=Y [Y=Yes, N=No]
  ProdRes VarChar(1) Production Resource [Yes/No] default=Y [Y=Yes, N=No]
  CardCode nVarChar(15) Preferred Vendor ->OCRD
  NoDiscount VarChar(1) No Discounts default=N [Y=Yes, N=No]
  IssueMthd VarChar(1) Issue Method default=B [B=Backflush, M=Manual]
  StdCost1 Num(19,6) Resource Cost 1
  StdCost2 Num(19,6) Resource Cost 2
  StdCost3 Num(19,6) Resource Cost 3
  StdCost4 Num(19,6) Resource Cost 4
  StdCost5 Num(19,6) Resource Cost 5
  StdCost6 Num(19,6) Resource Cost 6
  StdCost7 Num(19,6) Resource Cost 7
  StdCost8 Num(19,6) Resource Cost 8
  StdCost9 Num(19,6) Resource Cost 9
  StdCost10 Num(19,6) Resource Cost 10
  validFor VarChar(1) Active default=N [Y=Yes, N=No]
  validFrom Date(8) Active From
  validTo Date(8) Active To
  frozenFor VarChar(1) Inactive default=N [Y=Yes, N=No]
  frozenFrom Date(8) Inactive From
  frozenTo Date(8) Inactive To
  DfltWH nVarChar(8) Default Warehouse
  QueryGroup Int(11) Properties default=0
  PicturName nVarChar(200) Picture
  UserText Text(16) Item Remarks
  QryGroup1 VarChar(1) Property 1 default=N [Y=Yes, N=No]
  QryGroup2 VarChar(1) Property 2 default=N [Y=Yes, N=No]
  QryGroup3 VarChar(1) Property 3 default=N [Y=Yes, N=No]
  QryGroup4 VarChar(1) Property 4 default=N [Y=Yes, N=No]
  QryGroup5 VarChar(1) Property 5 default=N [Y=Yes, N=No]
  QryGroup6 VarChar(1) Property 6 default=N [Y=Yes, N=No]
  QryGroup7 VarChar(1) Property 7 default=N [Y=Yes, N=No]
  QryGroup8 VarChar(1) Property 8 default=N [Y=Yes, N=No]
  QryGroup9 VarChar(1) Property 9 default=N [Y=Yes, N=No]
  QryGroup10 VarChar(1) Property 10 default=N [Y=Yes, N=No]
  QryGroup11 VarChar(1) Property 11 default=N [Y=Yes, N=No]
  QryGroup12 VarChar(1) Property 12 default=N [Y=Yes, N=No]
  QryGroup13 VarChar(1) Property 13 default=N [Y=Yes, N=No]
  QryGroup14 VarChar(1) Property 14 default=N [Y=Yes, N=No]
  QryGroup15 VarChar(1) Property 15 default=N [Y=Yes, N=No]
  QryGroup16 VarChar(1) Property 16 default=N [Y=Yes, N=No]
  QryGroup17 VarChar(1) Property 17 default=N [Y=Yes, N=No]
  QryGroup18 VarChar(1) Property 18 default=N [Y=Yes, N=No]
  QryGroup19 VarChar(1) Property 19 default=N [Y=Yes, N=No]
  QryGroup20 VarChar(1) Property 20 default=N [Y=Yes, N=No]
  QryGroup21 VarChar(1) Property 21 default=N [Y=Yes, N=No]
  QryGroup22 VarChar(1) Property 22 default=N [Y=Yes, N=No]
  QryGroup23 VarChar(1) Property 23 default=N [Y=Yes, N=No]
  QryGroup24 VarChar(1) Property 24 default=N [Y=Yes, N=No]
  QryGroup25 VarChar(1) Property 25 default=N [Y=Yes, N=No]
  QryGroup26 VarChar(1) Property 26 default=N [Y=Yes, N=No]
  QryGroup27 VarChar(1) Property 27 default=N [Y=Yes, N=No]
  QryGroup28 VarChar(1) Property 28 default=N [Y=Yes, N=No]
  QryGroup29 VarChar(1) Property 29 default=N [Y=Yes, N=No]
  QryGroup30 VarChar(1) Property 30 default=N [Y=Yes, N=No]
  QryGroup31 VarChar(1) Property 31 default=N [Y=Yes, N=No]
  QryGroup32 VarChar(1) Property 32 default=N [Y=Yes, N=No]
  QryGroup33 VarChar(1) Property 33 default=N [Y=Yes, N=No]
  QryGroup34 VarChar(1) Property 34 default=N [Y=Yes, N=No]
  QryGroup35 VarChar(1) Property 35 default=N [Y=Yes, N=No]
  QryGroup36 VarChar(1) Property 36 default=N [Y=Yes, N=No]
  QryGroup37 VarChar(1) Property 37 default=N [Y=Yes, N=No]
  QryGroup38 VarChar(1) Property 38 default=N [Y=Yes, N=No]
  QryGroup39 VarChar(1) Property 39 default=N [Y=Yes, N=No]
  QryGroup40 VarChar(1) Property 40 default=N [Y=Yes, N=No]
  QryGroup41 VarChar(1) Property 41 default=N [Y=Yes, N=No]
  QryGroup42 VarChar(1) Property 42 default=N [Y=Yes, N=No]
  QryGroup43 VarChar(1) Property 43 default=N [Y=Yes, N=No]
  QryGroup44 VarChar(1) Property 44 default=N [Y=Yes, N=No]
  QryGroup45 VarChar(1) Property 45 default=N [Y=Yes, N=No]
  QryGroup46 VarChar(1) Property 46 default=N [Y=Yes, N=No]
  QryGroup47 VarChar(1) Property 47 default=N [Y=Yes, N=No]
  QryGroup48 VarChar(1) Property 48 default=N [Y=Yes, N=No]
  QryGroup49 VarChar(1) Property 49 default=N [Y=Yes, N=No]
  QryGroup50 VarChar(1) Property 50 default=N [Y=Yes, N=No]
  QryGroup51 VarChar(1) Property 51 default=N [Y=Yes, N=No]
  QryGroup52 VarChar(1) Property 52 default=N [Y=Yes, N=No]
  QryGroup53 VarChar(1) Property 53 default=N [Y=Yes, N=No]
  QryGroup54 VarChar(1) Property 54 default=N [Y=Yes, N=No]
  QryGroup55 VarChar(1) Property 55 default=N [Y=Yes, N=No]
  QryGroup56 VarChar(1) Property 56 default=N [Y=Yes, N=No]
  QryGroup57 VarChar(1) Property 57 default=N [Y=Yes, N=No]
  QryGroup58 VarChar(1) Property 58 default=N [Y=Yes, N=No]
  QryGroup59 VarChar(1) Property 59 default=N [Y=Yes, N=No]
  QryGroup60 VarChar(1) Property 60 default=N [Y=Yes, N=No]
  QryGroup61 VarChar(1) Property 61 default=N [Y=Yes, N=No]
  QryGroup62 VarChar(1) Property 62 default=N [Y=Yes, N=No]
  QryGroup63 VarChar(1) Property 63 default=N [Y=Yes, N=No]
  QryGroup64 VarChar(1) Property 64 default=N [Y=Yes, N=No]
  CreateDate Date(8) Date of Creation
  UpdateDate Date(8) Date of Update
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  ValidComm nVarChar(30) Active Remarks
  FrozenComm nVarChar(30) Inactive Remarks
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=290
  Deleted VarChar(1) Deleted default=N [Y=Yes, N=No]
  UserSign2 Int(6) Updating User
  Attachment Text(16) Attachment
  AtcEntry Int(11) Attachment Entry
  LastPurPrc Num(19,6) Last Purchase Price
  LastPurCur nVarChar(3) Last Purchase Currency
  LastPurDat Date(8) Last Purchase Date
  LstEvlPric Num(19,6) Last Evaluated Price
  LstEvlDate Date(8) Date of Last Reval. Price
  NumResUnit Int(11) No. of Resource Units default=1
  TimeResUn Int(11) Time per Resource Units
  ResAlloc VarChar(1) Resource Allocation default=S [S=On Start Date, D=On End Date, F=Start Date Forwards, B=End Date Backwards]
  LinkItm nVarChar(50) Linked Item ->OITM
  RelCap1 VarChar(1) Relevant to single run capacity 1 default=Y [Y=Yes, N=No]
  RelCap2 VarChar(1) Relevant to single run capacity 2 default=Y [Y=Yes, N=No]
  RelCap3 VarChar(1) Relevant to single run capacity 3 default=Y [Y=Yes, N=No]
  RelCap4 VarChar(1) Relevant to single run capacity 4 default=Y [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
