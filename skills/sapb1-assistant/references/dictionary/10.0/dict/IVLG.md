<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# IVLG - Inventory Revaluation Log File
Module: Inventory and Production | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Unique Key
  UtilVer Int(11) Inventory Revaluation Utility
  B1Ver Int(11) B1 Version
  SrcDBVer Int(11) Source Database Version
  DestDBName nVarChar(128) Destination Database Name
  DestDBPath Text(16) Destination Database Path
  FromDoc Int(11) Document From ->OINM
  FromSysDat Date(8) System Date From
  ToDoc Int(11) Last calculated document ->OINM
  ToSysDate Date(8) To System Date
  CustDbUpd VarChar(1) Customer DB was updated default=N [Y=, N=]
  HistTblCrt VarChar(1) History tables created default=N [Y=, N=]
  SuccRecalc VarChar(1) Successful recalculation default=N [Y=, N=]
  Comment nVarChar(100) Recalculation Comment
  EnblFromTo VarChar(1) Enabling From-To Function default=N
  StrFld nVarChar(50) General String Field
  NumFld Int(11) Include Custom from OIPF
  LoadCust VarChar(1) Load Customs on Item Value default=Y [Y="Load Customs on Item Value" is selected, N="Load Customs on Item Value" is not selected]
