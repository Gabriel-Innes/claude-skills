<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OUDG - User Defaults
Module: Administration | 49 columns | ObjType: 93
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Code
  Name nVarChar(20) Name
  Warehouse nVarChar(8) Warehouse ->OWHS
  SalePerson Int(11) Sales Employee default=-1 ->OSLP
  ICTCard nVarChar(15) BP for Invoice + Payment ->OCRD
  CashAcct nVarChar(15) Cash Account
  CheckAcct nVarChar(15) Current Account
  CreditCard Int(6) Credit Card ->OCRC
  PrintRcpt VarChar(1) Print Receipt default=N [N=No, A=Only When Adding, Y=Always]
  ShortRcpt VarChar(1) Print Payment & Invoice in Succession default=N [Y=Yes, N=No]
  Color Int(6) Windows Color [0=Combined, 1=Classic, 2=Gray, 3=Violet, 4=Blue, 5=Green, 6=Yellow, 7=Orange, 8=Red, 9=Brown]
  Address nVarChar(254) Address
  Country nVarChar(3) Country ->OCRY
  PrintHeadr nVarChar(100) Printing Header
  Phone1 nVarChar(20) Telephone Number 1
  Phone2 nVarChar(20) Telephone Number 2
  Fax nVarChar(20) Fax Number
  E_Mail nVarChar(100) E-Mail
  FrgnAddr nVarChar(254) Address in Foreign Language
  FrnPrntHdr nVarChar(100) Printing Header in Foreign Lan
  FrgnPhone1 nVarChar(20) Telephone Number 1 (Foreign Lang.)
  FrgnPhone2 nVarChar(20) Telephone Number 2 (Foreign Lang.)
  FrgnFax nVarChar(20) Fax Number (Foreign Lang.)
  DflTaxCode nVarChar(8) Default Tax Code ->OSTC
  FreeZoneNo nVarChar(32) Additional ID Number
  UserSign Int(6) User Signature ->OUSR
  free1 VarChar(1) Free1
  UseTax VarChar(1) Use Tax [Y=Yes, N=No]
  AdrsFromWh VarChar(1) Use Warehouse Address in A/P Documents default=N [Y=Yes, N=No]
  Language Int(11) Language ->OLNG
  Font nVarChar(50) Font
  FontSize Int(11) Font Size
  BPLId Int(11) Default Branch ->OBPL
  AssetInDoc VarChar(1) Allow Creation of Asset in Doc. default=N [Y=Yes, N=No]
  AttachPath Text(16) Attachments Path
  DflPTICode nVarChar(5) Default POI Code ->OPTI
  Free4 VarChar(1) unused
  Free2 VarChar(1) unused
  Free3 VarChar(1) unused
  DflPosCR Int(11) Default POS/Cash Register ->OPCM
  TimeFormat VarChar(1) Time Template [0=24H, 1=12H]
  DateFormat VarChar(1) Date Template [0=DD/MM/YY, 1=DD/MM/YYYY, 2=MM/DD/YY, 3=MM/DD/YYYY, 4=CCYY/MM/DD, 5=DD/Month/YYYY, 6=YY/MM/DD]
  DateSep VarChar(1) Date Separator
  DecSep VarChar(1) Decimal Separator
  ThousSep VarChar(1) Thousands Separator
  WallPaper Text(16) Wallpaper
  WllPprDsp nVarChar(6) Wallpaper Display [1=Centralized, 2=Full Screen, 3=Tile]
  SkinType nVarChar(254) Skin Type
  CharMonth Int(11) Number of Characters in Month
