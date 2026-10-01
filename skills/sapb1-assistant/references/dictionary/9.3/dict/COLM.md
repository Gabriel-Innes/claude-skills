<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# COLM - COLM resource
Module: General | 64 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: RevCode, ResCode, Num, Name
  UNIQUE_ID U: UniqueID, Name
Fields (name type(len) description [values] ->parent table):
  Created Date(8) Creation Date
  Updated Date(8) Update Date
  Name nVarChar(64) Table Name
  Num Int(11) Column Number
  ItemType Int(11) Item Type default=0 [0=None, 16=Edit text, 105=Bar, 113=Select popup, 116=Link button, 121=Check box, 117=Picture]
  Enabled VarChar(1) Enabled default=1 [0=No, 1=Yes]
  CellType Int(11) Cell Type default=16 [0=None, 16=Edit text, 105=Bar, 113=Select popup, 116=Link button, 121=Check box, 117=Picture]
  Font Int(11) Font Number
  FontSize Int(11) Font Size
  Attributes Int(11) Attributes
  Style Int(11) Style
  Mode Int(11) Mode
  TitleType Int(11) Title Type default=0 [0=None, 117=Picture]
  TitleEnabl VarChar(1) Title Enabled
  TitleFont Int(11) Title Font Number
  TFontSize Int(11) Title Font Size
  TitleAtt Int(11) Title Attributes
  TitleStyle Int(11) Title Style
  TitleMode Int(11) Title Mode
  VarNum Int(11) Variable Number
  LinkVar Int(11) Link Variable
  DragVar Int(11) Drag Variable
  FileCode nVarChar(20) Table Code
  FieldNum nVarChar(10) Field Alias
  Editable VarChar(1) Editable default=1 [0=No, 1=Yes]
  SuppressZe VarChar(1) Suppress Zeros default=0 [0=No, 1=Yes]
  DataRequir VarChar(1) Data Required default=0 [0=No, 1=Yes]
  ForceUpper VarChar(1) Force Upper default=0 [0=No, 1=Yes]
  RightJust VarChar(1) Right Justified default=1 [0=No, 1=Yes, 2=Language dependant]
  UserType VarChar(1) Binding Type default=0 [0=Data, 1=User Variable]
  Sentence VarChar(1) Sentencing default=0 [0=No, 1=Yes]
  ShowType VarChar(1) Show Type default=0 [0=Value + Description, 1=Value only, 2=Description only]
  DispDecr VarChar(1) Display Description default=0 [0=No, 1=Yes]
  LinkTo Int(11) Link To Item
  DragEntity Int(11) Drag Entity
  Class Int(11) Class
  TitleIndex Int(11) Title Index default=0
  DescIndex Int(11) Description Index default=0
  TxtFgRed Int(11) Text Foreground Red
  TxtFgGreen Int(11) Text Foreground Green
  TxtFgBlue Int(11) Text Foreground Blue
  TxtBgRed Int(11) Text Background Red
  TxtBgGreen Int(11) Text Background Green
  TxtBgBlue Int(11) Text Background Blue
  TtlFgRed Int(11) Title Foreground Red
  TtlFgGreen Int(11) Title Foreground Green
  TtlFgBlue Int(11) Title Foreground Blue
  TtlBgRed Int(11) Title Background Red
  TtlBgGreen Int(11) Title Background Green
  TtlBgBlue Int(11) Title Background Blue
  Width Int(11) Width
  SuppRepeat VarChar(1) Suppress Repeating default=0 [0=No, 1=Yes]
  AutoGraph VarChar(1) Auto Graph default=0 [0=No, 1=Yes]
  AutoCumm VarChar(1) Auto Cummulative default=0 [0=No, 1=Yes]
  UniqueID nVarChar(10) Unique ID
  TitleStr nVarChar(254) Title String
  ColDesc nVarChar(254) Column Description
  UsrSgnStr Int(11) User Sign For Strings Change default=-1
  UsrSgnAttr Int(11) User Sign For Attribs Change default=-1
  TtlFntName nVarChar(32) Title Font Name
  CllFntName nVarChar(32) Cell Font Name
  ResCode Int(11) Resource Code from RSBD default=-1
  RevCode Int(11) Revision Code default=-1
  BindObjId Int(11) Bind Object Id default=-1
