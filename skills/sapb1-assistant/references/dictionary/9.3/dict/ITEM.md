<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ITEM - Item Resource
Module: General | 71 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: RevCode, ResCode, Num, Name
  STRING: StrIndex
  UNIQUE_ID U: UniqueID, Name
Fields (name type(len) description [values] ->parent table):
  Created Date(8) Creation Date
  Updated Date(8) Update Date
  Name nVarChar(64) Form Name
  Num Int(11) Item Number
  ItemType Int(11) Item Type [4=Button, 121=Check box, 114=Edit popup, 16=Edit text, 118=Extended edit, 99=Folder, 101=FwdBck button, 123=Graph, 124=Icon, 116=Link button, 127=Grid, 120=Media, 103=Multi page, 115=Pane button, 104=Pane popup, 117=Picture, 98=Pipe, 125=Popup, 119=Preview, 112=Progress, 122=Radio button, 100=Rectangle, 113=Select popup, 8=Static text, 102=ActiveX, 0=User item, 129=Button Combo]
  Enabled VarChar(1) Enabled default=1 [0=No, 1=Yes]
  _Top Int(11) Top
  _Bottom Int(11) Bottom
  _Left Int(11) Left
  _Right Int(11) Right
  Font Int(11) Font Number
  FontSize Int(11) Font Size
  Attributes Int(11) Attributes
  Style Int(11) Style
  Mode Int(11) Mode
  VarNum Int(11) Variable Number
  AttrVar Int(11) Attribute Variable
  NewLineVar Int(11) New Line Variable
  ProcVar Int(11) Proc Variable
  LinkVar Int(11) Link Variable
  DragVar Int(11) Drag Variable
  FileCode nVarChar(20) Table Name
  FieldNum nVarChar(10) Field Alias
  Editable VarChar(1) Editable default=1 [0=No, 1=Yes]
  Invisible VarChar(1) Invisible default=0 [0=No, 1=Yes]
  SuppressZe VarChar(1) Suppress Zeros default=0 [0=No, 1=Yes]
  DfltButton VarChar(1) Default Button default=0 [0=No, 1=Yes]
  DataRequir VarChar(1) Data Required default=0 [0=No, 1=Yes]
  ForceUpper VarChar(1) Force Upper default=0 [0=No, 1=Yes]
  RightJust VarChar(1) Right Justified default=1 [0=No, 1=Yes, 2=Language dependant, 3=Oppos Language]
  UserType VarChar(1) Data Binding Type default=0 [0=Data, 1=User Variable, 2=Multiple Data Type]
  ShowType VarChar(1) Show type default=0 [0=Value + Description, 1=Value only, 2=Description only]
  DispDecr VarChar(1) Display Description default=0 [0=No, 1=Yes]
  TabOrder Int(11) TAB Order
  LinkTo Int(11) Link to Item
  DragEntity Int(11) Drag Entity
  FromPane Int(11) From Pane
  ToPane Int(11) To Pane
  Class Int(11) Class
  StrIndex Int(11) String Index default=0
  HkeyIndex Int(11) Hotkey Index
  DescIndex Int(11) Description Index default=0
  FrameRed Int(11) Frame Red
  FrameGreen Int(11) Frame Green
  FrameBlue Int(11) Frame Blue
  BodyRed Int(11) Body Red
  BodyGreen Int(11) Body Green
  BodyBlue Int(11) Body Blue
  TextRed Int(11) Text Red
  TextGreen Int(11) Text Green
  TextBlue Int(11) Text Blue
  ThumbRed Int(11) Thumb Red
  ThumbGreen Int(11) Thumb Green
  ThumbBlue Int(11) Thumb Blue
  TxtFgRed Int(11) Text Foreground Red
  TxtFgGreen Int(11) Text Foreground Green
  TxtFgBlue Int(11) Text Foreground blue
  TxtBgRed Int(11) Text Background Red
  TxtBgGreen Int(11) Text Background Green
  TxtBgBlue Int(11) Text Background Blue
  UniqueID nVarChar(10) Unique ID
  ItemString nVarChar(254) Item String
  ItemDesc nVarChar(254) Item Description
  HotkeyPos Int(11) Hotkey Position
  WrapText VarChar(1) Wrap Text default=0 [0=No, 1=Yes]
  UsrSgnStr Int(11) User Sign For String Change default=-1
  UsrSgnAttr Int(11) User Sign For Attribs Change default=-1
  FontName nVarChar(32) Font Name
  ResCode Int(11) Resource Code from RSBD default=-1
  RevCode Int(11) Revision Code default=-1
  BindObjId Int(11) Bind Object Id default=-1
