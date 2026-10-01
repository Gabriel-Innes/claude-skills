<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# TABL - Table resource
Module: General | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Name, ResCode, RevCode
  NUM U: Num
Fields (name type(len) description [values] ->parent table):
  Created Date(8) Creation date
  Updated Date(8) Update date
  Name nVarChar(64) Table name
  Num Int(11) Table number
  DoColor VarChar(1) Use color table default=0 [0=No, 1=Yes]
  BorderRed Int(11) Border red
  BorderGrn Int(11) Border green
  BorderBlue Int(11) Border blue
  BgRed Int(11) Background red default=65535
  BgGreen Int(11) Background green default=65535
  BgBlue Int(11) Background blue default=65535
  CellHeight Int(11) Cell height
  TitleHeigt Int(11) Title height
  Width Int(11) Width
  MaxUnique Int(11) Max Unique
  UsrSgnAttr Int(11) User Sign For Attribs Change default=-1
  ResCode Int(11) Resource Code from RSBD default=-1
  RevCode Int(11) Revision Code default=-1
