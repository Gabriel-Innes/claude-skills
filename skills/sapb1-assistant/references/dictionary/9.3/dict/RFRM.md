<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RFRM - FORM resource
Module: General | 40 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Name, Language
  NUM U: Num, Language
  M_NAME: Name
  M_NUM: Num
Fields (name type(len) description [values] ->parent table):
  Created Date(8) Creation date
  Updated Date(8) Update date
  Language Int(11) Language code
  Name nVarChar(64) Form name
  Num Int(11) Form number
  Title nVarChar(64) Title
  TitleUpd Date(8) Title update
  TitleLen Int(11) Title length
  Type Int(11) Form type default=0 [0=Resize Document, 1=Dialog Box, 3=No Title Document, 4=Fixed Document, 5=Resize No Title Document, 6=Toolbar]
  CloseBox VarChar(1) Close box default=1 [0=Yes, 1=No]
  DfltButton Int(11) Default button default=0
  _Top Int(11) Top default=1
  _Bottom Int(11) Bottom
  _Left Int(11) Left
  _Right Int(11) Right
  DoColor VarChar(1) Use color table default=1 [0=Yes, 1=No]
  CT_SEED Int(11) CT_SEED
  CT_RESERVE Int(11) CT_RESERVE
  CT_SIZE Int(11) CT_SIZE
  CT_S0_VAL Int(11) CT_S0_VALUE
  CT_S0_RED Int(11) CT_S0_RED
  CT_S0_GRN Int(11) CT_S0_GREEN
  CT_S0_BLUE Int(11) CT_S0_BLUE
  CT_S1_VAL Int(11) CT_S1_VALUE
  CT_S1_RED Int(11) CT_S1_RED
  CT_S1_GRN Int(11) CT_S1_GREEN
  CT_S1_BLUE Int(11) CT_S1_BLUE
  CT_S2_VAL Int(11) CT_S2_VALUE
  CT_S2_RED Int(11) CT_S2_RED
  CT_S2_GRN Int(11) CT_S2_GREEN
  CT_S2_BLUE Int(11) CT_S2_BLUE
  CT_S3_VAL Int(11) CT_S3_VALUE
  CT_S3_RED Int(11) CT_S3_RED
  CT_S3_GRN Int(11) CT_S3_GREEN
  CT_S3_BLUE Int(11) CT_S3_BLUE
  CT_S4_VAL Int(11) CT_S4_VALUE
  CT_S4_RED Int(11) CT_S4_RED
  CT_S4_GRN Int(11) CT_S4_GREEN
  CT_S4_BLUE Int(11) CT_S4_BLUE
  MaxUnique Int(11) Max Unique
