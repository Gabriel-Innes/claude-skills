<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OUOM - UoM Master Data
Module: Inventory and Production | 34 columns | ObjType: 10000199
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: UomEntry
  CODE U: UomCode
  NAME: UomName
Fields (name type(len) description [values] ->parent table):
  UomEntry Int(11) UoM Abs. Entry
  UomCode nVarChar(20) UoM Code
  UomName nVarChar(100) UoM Name
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(6) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
  Length1 Num(19,6) Length 1
  Len1Unit Int(6) Unit of Length 1
  length2 Num(19,6) Length 2
  Len2Unit Int(6) Unit of Length 2
  Width1 Num(19,6) Width 1
  Wdth1Unit Int(6) Unit of Width 1
  Width2 Num(19,6) Width 2
  Wdth2Unit Int(6) Unit of Width 2
  Height1 Num(19,6) Height 1
  Hght1Unit Int(6) Unit of Height 1
  Height2 Num(19,6) Height 2
  Hght2Unit Int(6) Unit of Height 2
  Volume Num(19,6) Volume
  VolUnit Int(6) Volume UoM
  Weight1 Num(19,6) Weight 1
  WghtUnit Int(6) Weight UoM
  Weight2 Num(19,6) Weight 2
  Wght2Unit Int(6) Unit of Weight 2
  IntSymbol nVarChar(20) International Symbol
  EwbUnit Int(11) EWB Unit ->OEUT
  PPWeight1 Num(19,6) Plastic Package Weight1
  PPWe1Unit Int(6) Plastic Package Weight1 Unit
  PPWeight2 Num(19,6) Plastic Package Weight2
  PPWe2Unit Int(6) Plastic Package Weight2 Unit
