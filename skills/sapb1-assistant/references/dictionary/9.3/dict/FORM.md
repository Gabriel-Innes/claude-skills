<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# FORM - FORM resource
Module: General | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RevCode, ResCode, Name
  NUM U: Num
Fields (name type(len) description [values] ->parent table):
  Created Date(8) Creation date
  Updated Date(8) Update date
  Name nVarChar(64) Form name
  Num Int(11) Form number
  Type Int(11) Form type default=0 [0=Resize Document, 1=Dialog Box, 3=No Title Document, 4=Fixed Document, 5=Resize No Title Document, 6=Toolbar, 7=Fixed No Minimize]
  CloseBox VarChar(1) Close box default=1 [0=No, 1=Yes]
  DfltButton Int(11) Default button default=0
  _Top Int(11) Top
  _Bottom Int(11) Bottom
  _Left Int(11) Left
  _Right Int(11) Right
  MaxUnique Int(11) Max Unique
  RobjCode Int(11) ImpExp Obj Code default=0
  HelpCntxt nVarChar(32) Help Context
  UsrSgnAttr Int(11) User Sign For Attribs Change default=-1
  ResCode Int(11) Resource Code from RSBD default=-1
  RevCode Int(11) Revision Code default=-1
  UseBoBind VarChar(1) Use BO Binding default=N [Y=Yes, N=No]
