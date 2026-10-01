<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# RITM - Reporting Element
Module: Reports | 88 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocCode, ItemId
  CONTAINER: DocCode, Container, ContIndex, ItemGroup
  APPL_ID: DocCode, ApplID
  TYPE: DocCode, Type, ItemIndex
Fields (name type(len) description [values] ->parent table):
  DocCode nVarChar(8) Report ->RDOC
  ItemId Int(6) Item ID
  Container Int(6) Parent Type
  Type Int(6) Type [1=Page Header, 2=Start of Report, 3=Repetitive Area Header, 4=Repetitive Area, 5=Repetitive Area Footer, 6=End of Report, 7=Page Footer, 10=Text Field, 11=Picture Field, 12=User Field]
  VISIBLE VarChar(1) Visible default=Y [Y=Yes, N=No]
  SupZeros VarChar(1) Suppress Zeros default=N [Y=Yes, N=No]
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
  BGRed Int(11) Background - Red default=255
  BGGreen Int(11) Background - Green default=255
  BGBlue Int(11) Background - Blue default=255
  FGRed Int(11) Text - Red default=0
  FGGreen Int(11) Text - Green default=0
  FGBlue Int(11) Text - Blue default=0
  MrkrRed Int(11) Bold - Red default=255
  MrkrGreen Int(11) Bold - Green default=255
  MrkrBlue Int(11) Bold - Blue default=255
  BrdrRed Int(11) Border - Red default=0
  BrdrGreen Int(11) Border - Green default=0
  BrdrBlue Int(11) Border - Blue default=0
  FromPane Int(6) From Area default=0
  ToPane Int(6) To Area default=0
  ItemGroup Int(6) Group No. default=0
  FontName nVarChar(50) Font Name default=Arial
  FontSize Int(6) Font Size default=12
  TextStyle Int(11) Text Style default=0
  Justific Int(6) Horizontal Justification default=2 [1=Right, 2=Left, 3=Centralized, 4=Language-Dependent]
  WRAP Int(6) Segment default=2 [0=Allow Overflow, 1=Adjust to Cell, 2=Divide into Rows]
  PictSize Int(6) Picture Size default=0 [0=Original Size, 1=Fit Field Size Non-Proportionally, 2=Fit Field Size Proportionally, 3=Fit Field Height, 4=Fit Fields Width]
  DataSource Int(6) Data Source default=1 [1=Static, 2=Variable, 3=Data, 4=Calculation]
  ItemStr Text(16) String
  VarNum Int(6) Variable No.
  FileName nVarChar(20) File Name
  FieldNum nVarChar(52) Field No.
  ShowDescr VarChar(1) Display Description default=Y [Y=Yes, N=No]
  CalcType nVarChar(2) Calculation Type default=1 [0=Formula, 1=Page Number, 17=Total Pages, 2=Date, 3=Time, 4=Column Total, 5=Column Average, 6=General Row No., 7=Group Row No., 8=Sort Field Name, 9=Sort Field Content, 10=Continue, 11=Continued on Next Page, 12=Generation Message, 13=Column Summary for Page, 14=Column Average for Page, 15=Column Summary for Report, 16=Column Average for Report]
  ChangFlags Int(11) Changeable
  ApplID Int(6) Item No.
  CalcCol Int(6) Calculation Column
  YJustific Int(6) Vertical Alignment default=3 [1=Top, 2=Bottom, 3=Centralized]
  SortLevel Int(6) Sort Level default=0
  RevOrder VarChar(1) Reverse Sort default=N [Y=Descending, N=Ascending]
  SortType Int(6) Sort Type default=0 [0=Alpha, 1=Numeric, 2=Currency, 3=Date]
  IsUnique VarChar(1) Unique default=N [Y=Yes, N=No]
  IsGroup VarChar(1) Set as Group default=N [Y=Yes, N=No]
  NewPage VarChar(1) New Page default=N [Y=Yes, N=No]
  BarCode VarChar(1) Print as Bar Code default=N [Y=Yes, N=No]
  Condition Text(16) Condition
  LinkTo nVarChar(20) Link to Field
  Operator1 Int(6) Operator 1
  Operator2 Int(6) Operator 2
  Operation Int(6) Operation default=0 [0=, 1=+, 2=-, 3=x, 4=/, 5=%, 17=Left Part (Characters), 18=Right Part (Mantissa), 19=Round, 6=$Concat, 7=$Right, 8=$Left, 9=$Sentence, 16=$Length, 20=$Currency, 21=$Number, 10=Less than, 11=Less or Equal, 12=Equal, 13=Not equal, 14=Greater or Equal, 15=Greater than]
  BCStandard Int(6) Bar Code Standard default=0 [0=EAN-13, 1=Code 39, 2=Code 128]
  SumInWords VarChar(1) Display Total as a Word default=N [Y=Yes, N=No]
  ExcFonting VarChar(1) Block Font Change default=N [Y=Yes, N=No]
  StrIndex Int(11) String Index default=0
  ContIndex Int(6) Container Index default=0
  ItemIndex Int(6) Item Index default=0
  StrLength Int(6) String Length
  StrFiller VarChar(1) String Filler
  RelatedTo nVarChar(20) Link to Field
  NextSeg nVarChar(20) Next Segment Item Number
  HightAdjst VarChar(1) Height Adjustments default=N [Y=Yes, N=No]
  DupRpttAre VarChar(1) Duplicate Repetitive Area default=N [Y=Yes, N=No]
  LnsRpttAre Int(11) No. of Rows in Repetitive Area default=0
  RptDupDist Int(11) Distance To Rptt Dup. (pixels) default=0
  FieldId nVarChar(20) Unique ID
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
