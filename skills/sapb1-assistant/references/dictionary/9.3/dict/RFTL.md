<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RFTL - FITL resource
Module: General | 72 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Num, Name, Language
  M_NAME: Num, Name
  STRING: ItemString
  UNIQUE_ID U: UniqueID, Name, Language
Fields (name type(len) description [values] ->parent table):
  Created Date(8) Creation date
  Updated Date(8) Update dateS
  Language Int(11) Language code
  Name nVarChar(64) FITL name
  Num Int(11) Item number
  ItemType Int(11) Item type [4=Button, 121=Check box, 114=Edit popup, 16=Edit text, 118=Extended edit, 99=Folder, 101=FwdBck button, 123=Graph, 124=Icon, 116=Link button, 127=Matrix, 120=Media, 103=Multi page, 115=Pane button, 104=Pane popup, 117=Picture, 98=Pipe, 125=Popup, 119=Preview, 112=Progress, 122=Radio button, 100=Rectangle, 113=Select popup, 8=Static text, 102=User group, 0=User item]
  Enabled VarChar(1) Enabled default=1 [0=No, 1=Yes]
  _Top Int(11) Top
  _Bottom Int(11) Bottom
  _Left Int(11) Left
  _Right Int(11) Right
  ItemRes Int(11) Item resource
  Font Int(11) Font number
  FontSize Int(11) Font size
  Attributes Int(11) Attributes
  Style Int(11) Style
  Mode Int(11) Mode
  VarNum Int(11) Variable number
  AttrVar Int(11) Attribute variable
  NewLineVar Int(11) New line variable
  ProcVar Int(11) Proc variable
  LinkVar Int(11) Link variable
  DragVar Int(11) Drag variable
  FileCode nVarChar(8) File code
  FieldNum Int(11) Field number
  IndexType VarChar(1) Index type default=0 [0=Variable, 1=Static]
  IndexVal Int(11) Index value
  FatIdxType VarChar(1) Father index type default=0 [0=Variable, 1=Static]
  FatIdxVal Int(11) Father index value
  Editable VarChar(1) Editable default=1 [0=No, 1=Yes]
  Invisible VarChar(1) Invisible default=0 [0=No, 1=Yes]
  SuppressZe VarChar(1) Suppress zeros default=0 [0=No, 1=Yes]
  DfltButton VarChar(1) Default button default=0 [0=No, 1=Yes]
  DataRequir VarChar(1) Data required default=0 [0=No, 1=Yes]
  ForceUpper VarChar(1) Force upper default=0 [0=No, 1=Yes]
  RightJust VarChar(1) Right justified default=1 [0=No, 1=Yes]
  UserType VarChar(1) User type default=0 [0=No, 1=Yes]
  Override VarChar(1) Override validation default=0 [0=No, 1=Yes]
  Sentence VarChar(1) Sentencing default=0 [0=No, 1=Yes]
  ShowType VarChar(1) Show type default=0 [0=Value + Description, 1=Value only, 2=Description only]
  DispDecr VarChar(1) Display description default=0 [0=No, 1=Yes]
  TabOrder Int(11) TAB order
  LinkTo Int(11) Link to item
  DragEntity Int(11) Drag entity
  FromPane Int(11) From pane
  ToPane Int(11) To pane
  Class Int(11) Class
  ItemString nVarChar(64) Item string
  StringUpd Date(8) String update date
  StringLen Int(11) String length
  ItemDesc nVarChar(30) Item description
  DescUpd Date(8) Description update date
  DescLen Int(11) Description length
  FrameRed Int(11) Frame red
  FrameGreen Int(11) Frame green
  FrameBlue Int(11) Frame blue
  BodyRed Int(11) Body red
  BodyGreen Int(11) Body green
  BodyBlue Int(11) Body blue
  TextRed Int(11) Text red
  TextGreen Int(11) Text green
  TextBlue Int(11) Text blue
  ThumbRed Int(11) Thumb red
  ThumbGreen Int(11) Thumb green
  ThumbBlue Int(11) Thumb blue
  TxtFgRed Int(11) Text foreground red
  TxtFgGreen Int(11) Text foreground green
  TxtFgBlue Int(11) Text foreground blue
  TxtBgRed Int(11) Text background red
  TxtBgGreen Int(11) Text background green
  TxtBgBlue Int(11) Text background green
  UniqueID nVarChar(10) Unique ID
