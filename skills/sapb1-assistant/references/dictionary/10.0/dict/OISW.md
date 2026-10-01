<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OISW - Intrastat Wizard
Module: Finance | 73 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  DeclDescr nVarChar(200) Description
  DateFrom Date(8) Starting Date of Declaration
  DateTo Date(8) Ending Date of Declaration
  RunDate Date(8) Date of Run
  ImpExpInd VarChar(1) Import Export Indicator default=I [I=Import, E=Export]
  Status VarChar(1) Status [O=Open, C=Closed, D=Deleted, A=Archived]
  MsgType Int(11) Message Type default=0 [0=New Declaration, 9=Nil Declaration, 3=Correction Declaration]
  TtlDocVal Num(19,6) Total Document Value
  DocCount Int(11) Total Number of Documents
  CompName nVarChar(100) Company Name
  CompDeclID nVarChar(32) Company Declaration ID
  CompStreet nVarChar(100) Company Street
  CompCity nVarChar(100) Company City
  CompZip nVarChar(20) Company Zip Code
  CompCntry nVarChar(3) Company Country/Region ->OCRY
  DeclCntry nVarChar(3) Declaration Country/Region ->OCRY
  CntPersID Int(11) Contact Person ID ->OHEM
  CntPerson nVarChar(250) Contact Person
  CntEmail nVarChar(100) Contact E-Mail
  CntPhone nVarChar(50) Contact Phone
  CntFax nVarChar(50) Contact Fax
  VATRegNo nVarChar(100) VAT Reg. No. of Trader
  VATRegEx nVarChar(10) VAT Reg. No. Extension
  DeclNum nVarChar(14) Sequential Declaration Number
  DeclNoEx Int(11) No. of Declaration in Period
  HeaderId Int(11) Header ID
  DeclStat VarChar(1) Declaration Status
  DeclDept Int(6) Declaring Department
  DeclCurr nVarChar(3) Declaration Currency
  ObligLvl VarChar(1) Degree of Obligation
  TaxState nVarChar(3) Federal State of Tax Office
  CustOffc nVarChar(100) Customs Registration Office
  CustOffID nVarChar(2) Customs Registration Office ID
  DeclSerNo nVarChar(3) Declaration Sequence Number
  IntCtrlRef nVarChar(99) Interchange Control Reference
  Addr1_3p nVarChar(100) Third-Party Address Part 1
  Addr2_3p nVarChar(100) Third-Party Address Part 2
  Addr3_3p nVarChar(100) Third-Party Address Part 3
  Addr4_3p nVarChar(100) Third-Party Address Part 4
  CntPers_3p nVarChar(250) Third-Party Contact Person
  CntPhon_3p nVarChar(20) Third-Party Contact Phone
  CntFax_3p nVarChar(20) Third-Party Contact Fax
  FreeTxt1 nVarChar(70) Free Text Line 1
  FreeTxt2 nVarChar(70) Free Text Line 2
  FreeTxt3 nVarChar(70) Free Text Line 3
  FreeTxt4 nVarChar(70) Free Text Line 4
  FreeTxt5 nVarChar(70) Free Text Line 5
  ValidKey nVarChar(35) Validation Key Identification
  ISDeclOffc nVarChar(10) Intrastat Declaration Office
  ReleaseVer nVarChar(13) Release Version
  UserSign Int(6) Created by User
  PosCredVal VarChar(1) Positive Credit Memo Values default=Y [Y=Yes, N=No]
  IncPrevDoc VarChar(1) Include Previous Documents [Y=Yes, N=No]
  DeclPeriod VarChar(1) Declaration Period default=M [M=Monthly, Q=Quarterly]
  Box1 Int(6) Box 1: Periodicity default=0 [0=None of the Other Cases, 8=First Month of Quarter, 9=First and Second Months of Quarter]
  Box2 Int(6) Box 2: Company Activity default=0 [0=None of the Other Cases, 7=First Declaration, 8=Stop Activity/Change of Federal Tax ID, 9=First Declaration After Federal Tax ID Change]
  GroupData VarChar(1) Group Display Data default=Y [Y=Yes, N=No]
  CstRecSt nVarChar(6) Custom Section
  TaxCodeExt nVarChar(99) Tax Code Extension
  ExportPath Text(16) Export Path
  LLEFMAbs Int(11) EFM Template ID
  SimpProc VarChar(1) Simplified Procedure [Y=Yes, N=No]
  DspNMass VarChar(1) Require All Data [Y=Yes, N=No]
  ExlDocQt VarChar(1) Exclude Docs W/ Qty Less Than [Y=Yes, N=No]
  DocQtLm Num(19,6) Document Quantity Limit
  ExlDocAm VarChar(1) Exclude Docs W/ Amt Less Than [Y=Yes, N=No]
  DocAmLm Num(19,6) Document Amount Limit
  RunTime Int(6) Time of Run
  AddonRun VarChar(1) Upgraded Add-On Run default=N [Y=Yes, N=No]
  BaseDecl Int(11) Base Declaration ->ODCI
  GroupTrans VarChar(1) Group Transactions default=N [Y=Yes, N=No]
  IncGRandDL VarChar(1) Include Goods Receipt and Deliveries default=Y [Y=Yes, N=No]
