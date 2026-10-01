<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RMTX - MATX resource
Module: General | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Name, Language
  NUM U: Num, Language
  M_NAME: Name
  M_NUM: Num
Fields (name type(len) description [values] ->parent table):
  Created Date(8) Creation date
  Updated Date(8) Update date
  Language Int(11) Language code
  Name nVarChar(64) MATX name
  Num Int(11) MATX number
  DoColor VarChar(1) Use color table default=0 [0=No, 1=Yes]
  BorderRed Int(11) Border red
  BorderGrn Int(11) Border green
  BorderBlue Int(11) Border blue
  BgRed Int(11) Background red
  BgGreen Int(6) Background green
  BgBlue Int(11) Background blue
  CellHeight Int(11) Cell height
  TitleHeigt Int(11) Title height
  Width Int(11) Width
  MaxUnique Int(11) Max Unique
