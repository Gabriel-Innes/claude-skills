<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RMTL - MITL resource
Module: General | 70 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Num, Name, Language
  M_NAME: Num, Name
  UNIQUE_ID U: UniqueID, Name, Language
Fields (name type(len) description [values] ->parent table):
  Created Date(8) Creation date
  Updated Date(8) Update date
  Language Int(11) Language code
  Name nVarChar(64) MITL name
  Num Int(11) Column number
  ItemType Int(11) Item type default=0 [0=None, 16=Edit text, 105=Bar, 113=Select popup, 116=Link button, 121=Check box, 117=Picture]
  Enabled VarChar(1) Enabled default=1 [0=No, 1=Yes]
  CellType Int(11) CellType default=16 [0=None, 16=Edit text, 105=Bar, 113=Select popup, 116=Link button, 121=Check box]
  CellRes Int(11) Cell resource
  Font Int(11) Font number
  FontSize Int(11) Font size
  Attributes Int(11) Attributes
  Style Int(11) Style
  Mode Int(11) Mode
  TitleType Int(11) Title type default=0 [0=None, 117=Picture]
  TitleEnabl VarChar(1) Title enabled
  TitleRes Int(11) Title resource
  TitleFont Int(11) Title font number
  TFontSize Int(11) Title font size
  TitleAttr Int(11) Title attributes
  TitleStyle Int(11) Title style
  TitleMode Int(11) Title mode
  VarNum Int(11) Variable number
  LinkVar Int(11) Link variable
  DragVar Int(11) Drag variable
  FileCode nVarChar(8) File code
  FieldNum Int(11) Field number
  IndexType VarChar(1) Index type default=0 [0=Variable, 1=Static]
  IndexVal Int(11) Index value
  FatIdxType VarChar(1) Father index type default=0 [0=Variable, 1=Static]
  FatIdxVal Int(11) Father index value
  Editable VarChar(1) Editable default=1 [0=No, 1=Yes]
  SuppressZe VarChar(1) Suppress zeros default=0 [0=No, 1=Yes]
  DataRequir VarChar(1) Data required default=0 [0=No, 1=Yes]
  ForceUpper VarChar(1) Force upper default=0 [0=No, 1=Yes]
  RightJust VarChar(1) Right justified default=1 [0=No, 1=Yes]
  UserType VarChar(1) User type default=0 [0=No, 1=Yes]
  Sentence VarChar(1) Sentencing default=0 [0=No, 1=Yes]
  ShowType VarChar(1) Show type default=0 [0=Value + Description, 1=Value only, 2=Description only]
  DispDecr VarChar(1) Display description default=0 [0=No, 1=Yes]
  LinkTo Int(11) Link to item
  DragEntity Int(11) Drag entity
  Class Int(11) Class
  ItemString nVarChar(64) Item string
  StringUpd Date(8) String update date
  StringLen Int(11) String length
  Title nVarChar(64) Title string
  TitleUpd Date(8) Title updated
  TitleLen Int(11) Title length
  ItemDesc nVarChar(30) Item description
  DescUpd Date(8) Description update date
  DescLen Int(11) Description length
  TxtFgRed Int(11) Text foreground red
  TxtFgGreen Int(11) Text foreground green
  TxtFgBlue Int(11) Text foreground blue
  TxtBgRed Int(11) Text background red
  TxtBgGreen Int(11) Text background green
  TxtBgBlue Int(11) Text background green
  TtlFgRed Int(11) Title foreground red
  TtlFgGreen Int(11) Title foreground green
  TtlFgBlue Int(11) Title foreground blue
  TtlBgRed Int(11) Title background red
  TtlBgGreen Int(11) Title background green
  TtlBgBlue Int(11) Title background blue
  Width Int(11) Width
  UserLen Int(11) User length
  SuppRepeat VarChar(1) Suppress repeating default=0 [0=No, 1=Yes]
  AutoGraph VarChar(1) Auto graph default=0 [0=No, 1=Yes]
  AutoCumm VarChar(1) Auto cummulative default=0 [0=No, 1=Yes]
  UniqueID nVarChar(10) Unique ID
