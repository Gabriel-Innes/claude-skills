<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ITMR - 
Module: General | 102 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocType, Local, Numerator, Language, ApplID, ResCode, RevCode
  TP_LC_NM_L: DocType, Local, Numerator, Language
  TYP_LOC_NM: DocType, Local, Numerator
  TYPE_LOC: DocType, Local
  TYPE: DocType
Fields (name type(len) description [values] ->parent table):
  DocCode nVarChar(8) Report
  ItemId Int(6) Item ID
  Container Int(6) Parent Type
  Type Int(6) Type [1=Page header, 2=Start of report, 3=Repetitive area header, 4=Repetitive area, 5=Repetitive area footer, 6=End of report, 7=Page footer, 10=Text field, 11=Picture field, 12=User field]
  VISIBLE VarChar(1) Visible default=1 [1=Yes, 0=No]
  SupZeros VarChar(1) Suppress Zeros default=0 [1=Yes, 0=No]
  ItemLeft Int(6) Left Item
  ItemTop Int(6) Top
  Width Int(6) Width
  Height Int(6) Height
  LMargin Int(6) Left Margin default=0
  RMargin Int(6) Right Margin default=0
  TMargin Int(6) Top Margin default=0
  BMargin Int(6) Bottom Margin default=0
  LeftLine Int(6) Left Border Line Thickness default=0
  RightLine Int(6) Right Border Line Thickness default=0
  TopLine Int(6) Top Border Line Thickness default=0
  BottomLine Int(6) Bottom Border Line Thickness default=0
  Shadow Int(6) Shadow Thickness default=0
  BGRed Int(11) Background - Red default=65535
  BGGreen Int(11) Background - Green default=65535
  BGBlue Int(11) Background - Blue default=65535
  FGRed Int(11) Text - Red default=0
  FGGreen Int(11) Text - Green default=0
  FGBlue Int(11) Text - Blue default=0
  MrkrRed Int(11) Bold - Red default=65535
  MrkrGreen Int(11) Bold - Green default=65535
  MrkrBlue Int(11) Bold - Blue default=65535
  BrdrRed Int(11) Border - Red default=0
  BrdrGreen Int(11) Border - Green default=0
  BrdrBlue Int(11) Border - Blue default=0
  FromPane Int(6) From Area default=0
  ToPane Int(6) To Area default=0
  ItemGroup Int(6) Group No. default=0
  FontName nVarChar(50) Font Name default=Arial
  FontSize Int(6) Font Size default=12
  TextStyle Int(11) Text Style
  Justific VarChar(1) Horizontal Justification default=2 [1=Right, 2=Left, 3=Center, 4=Language Dependent]
  WRAP VarChar(1) Segment default=1 [0=Allow overflow, 1=Fit to cell, 2=Devide to lines]
  PictSize VarChar(1) Picture Size default=1 [0=Original size, 1=Size of box, 2=Adjust to box, 3=Adjust to box height, 4=Adjust to box width]
  DataSource VarChar(1) Data Source default=1 [1=Static, 2=Var, 3=Data, 4=Calculation]
  ItemStr Text(16) String
  VarNum Int(6) Variable No.
  FileName nVarChar(20) File Name
  FieldNum nVarChar(10) Field No.
  ShowDescr VarChar(1) Display Description default=0 [1=Yes, 0=No]
  CalcType nVarChar(2) Calculation Type default=1 [0=Formula, 1=Page number, 17=Total Pages, 2=Date, 3=Time, 4=Column total, 5=Column average, 6=General row no., 7=Group row no., 8=Sort field name, 9=Sort field content, 10=Continue, 11=Continued on next page, 12=Generation message, 13=Column summary for page, 14=Column average for page, 15=Column summary for report, 16=Column average for report, -1=[new formula String]]
  ChangFlags Int(11) Changeable
  ApplID Int(6) Item No.
  CalcCol Int(6) Calculation Column
  YJustific VarChar(1) Vertical Alignment default=3 [1=Top, 2=Bottom, 3=Center]
  SortLevel Int(6) Sort Level default=0
  RevOrder VarChar(1) Reverse Sort default=0 [1=Descending, 0=Ascending]
  SortType VarChar(1) Sort Type default=0 [0=Alpha, 1=Numeric, 2=Money, 3=Date]
  IsUnique VarChar(1) Unique default=0 [1=Yes, 0=No]
  IsGroup VarChar(1) Set as Group default=0 [1=Yes, 0=No]
  NewPage VarChar(1) New Page default=0 [1=Yes, 0=No]
  BarCode VarChar(1) Print as Barcode default=0 [1=Yes, 0=No]
  Condition Text(16) Condition
  LinkTo Int(6) Link to Item default=0
  Operator1 Int(6) Operator 1
  Operator2 Int(6) Operator 2
  Operation Int(6) Operation default=0 [0=, 1=+, 2=-, 3=x, 4=/, 5=%, 17=Left, 18=Right, 19=Round, 6=$Concat, 7=$Right, 8=$Left, 9=$Sentence, 16=$Len, 20=$Currency, 21=$Number, 10=Less, 11=LessEq, 12=Equally, 13=Not eq, 14=GrEq, 15=Greater]
  BCStandard Int(6) Barcode Standard default=0 [0=EAN-13, 1=Code 39, 2=Code 128]
  SumInWords VarChar(1) Display Total as a Word default=0 [1=Yes, 0=No]
  ExcFonting VarChar(1) Block Font Change default=0 [1=Yes, 0=No]
  StrIndex Int(11) String Index default=0
  ContIndex Int(6) Container Index default=0
  ItemIndex Int(6) Item Index default=0
  StrLength Int(6) String Length
  StrFiller VarChar(1) String Filler
  RelatedTo Int(6) Related to Item default=0
  NextSeg Int(6) Next Segment Item Num default=0
  HightAdjst VarChar(1) Height Adjustments default=N [Y=Yes, N=No]
  DupRpttAre VarChar(1) Duplicate Repeatative Area default=N [Y=Yes, N=No]
  LnsRpttAre Int(11) Num Lines In Repeatative Area default=0
  RptDupDist Int(11) Distanse To Rptt Dup (pixels) default=0
  ItemDesc nVarChar(50) Item Description
  ExportXml VarChar(1) Export to xml default=Y [Y=Yes, N=No]
  DocType nVarChar(4) Document Type
  Local nVarChar(2) Localization
  Numerator Int(6) Numerator
  Language Int(6) Language
  Created Date(8) Creation Date
  Updated Date(8) Updated Date
  UsrSgnStr Int(11) User Sign For Strings Change default=-1
  UsrSgnAttr Int(11) User Sign For Attribs Change default=-1
  IsRef VarChar(1) Is the item refered by another default=N [Y=Yes, N=No]
  FieldId nVarChar(20) Field Identifier
  FGEnabled VarChar(1) Grid Enabled default=Y [Y=Yes, N=No]
  BGEnabled VarChar(1) Background Enabled default=Y [Y=Yes, N=No]
  MKEnabled VarChar(1) Highlight Enabled default=Y [Y=Yes, N=No]
  BDEnabled VarChar(1) Frame Enabled default=Y [Y=Yes, N=No]
  HidEmpRptt VarChar(1) Hide Empty Area default=N [Y=Yes, N=No]
  RpttFtrAll VarChar(1) Display Rep. Footer on All default=N [Y=Yes, N=No]
  GbiDataTyp Int(6) Data Type default=0 [0=, 1=C n, 2=C.. n, 3=I.. n, 4=D w.d]
  GbiDataLen nVarChar(6) Data Length
  PageBreak Int(6) Page Break default=0 [0=None, 1=Before Area, 2=After Area]
  IsLogo VarChar(1) Is Logo default=N [Y=Yes, N=No]
  VarDefName nVarChar(50) Variable Definition Name
  ResCode Int(11) Resource Code from RSBD default=-1
  RevCode Int(11) Revision Code default=-1
