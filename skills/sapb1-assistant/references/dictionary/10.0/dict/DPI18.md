<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# DPI18 - A/R Down Payment - Export Process
Module: Marketing Documents | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPI
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=203 ->ADP1
  ExpDocType Int(11) Type of Exportation Document default=-1 ->OBNI
  ExpDeclNum Int(11) Exportation Declaration Number
  ExpDeclDat Date(8) Exportation Declaration Date
  ExpNature Int(11) Nature of Exportation default=-1 ->OBNI
  ExpRegNum Int(11) Number of Exportation Registry
  ExpRegDate Date(8) Date of Exportation Registry
  LadBillNum nVarChar(19) Bill of Lading Number
  LadBillDat Date(8) Date of Bill of Lading
  MerchLeftD Date(8) Date Merchandise Left Customs
  LadBillTyp Int(11) Type of Bill of Lading default=-1 ->OBNI
  DrawSReg nVarChar(11) Drawback - Suspension Regime
  NatureExp nVarChar(44) Nature of Export
  QultExpItm Num(19,6) Quantity of Exported Items
  nSeqAdic Int(6) Additional Item Sequential Number
