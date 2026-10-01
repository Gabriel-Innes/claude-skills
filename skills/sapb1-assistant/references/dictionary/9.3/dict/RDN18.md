<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RDN18 - Returns - Export Process
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDN
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=16 ->ADP1
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
