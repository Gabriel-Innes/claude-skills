<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RDGP - Development Groups
Module: General | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: GroupCode
  NUM U: Num
  ID_START U: IdtRngStrt
  ID_END U: IdRngEnd
  FORM_START U: FrmRngStrt
  FORM_END U: FrmRngEnd
  MTX_START U: MtxRngStrt
  MTX_END U: MtxRngEnd
  STRL_START U: StrRngStrt
  STRL_END U: StrRngEnd
Fields (name type(len) description [values] ->parent table):
  Num Int(11) Group Number
  GroupCode nVarChar(3) Development Group Code
  GroupName nVarChar(20) Development Group Name
  Lcaliztion nVarChar(2) Localization of Dev Group
  IdtRngStrt Int(11) Unique Id Range - Start
  IdRngEnd Int(11) Unique Id Range - End
  FrmRngStrt Int(11) Forms Editing Range - Start
  FrmRngEnd Int(11) Forms Editing Range - End
  MtxRngStrt Int(11) Matrixes Editing Range - Start
  MtxRngEnd Int(11) Matrixes Editing Range - End
  StrRngStrt Int(11) String Lists Range - Start
  StrRngEnd Int(11) String Lists Range - End
