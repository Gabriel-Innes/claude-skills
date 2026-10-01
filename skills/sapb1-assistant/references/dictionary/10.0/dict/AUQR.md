<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AUQR - Queries - History
Module: Reports | 26 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: IntrnalKey, QCategory, LogInstanc
  QNAME_K U: QName, QCategory, LogInstanc
Fields (name type(len) description [values] ->parent table):
  IntrnalKey Int(11) Internal Key
  QCategory Int(11) Query Category ->OQCN
  QName nVarChar(100) Query Description
  QString Text(16) Query
  QType VarChar(1) Query Type default=W [R=Regular, W=Wizard, G=Report Generator, S=Stored Procedure]
  ColumnSize nVarChar(100) Column Size
  DBType Int(11) Database Type
  QLastDate Date(8) Last Upload Date
  QLastTime Int(6) Last Upload Time
  Xslt Text(16) XSLT Transformation
  MenuItem VarChar(1) Specify Menu Item default=N [Y=Yes, N=No]
  MenuCapt nVarChar(254) Menu Caption
  FatherMenu Int(11) Parent Menu ID
  MenuPos Int(6) Menu Position
  MenuUid nVarChar(32) Menu UID
  CommandID Int(11) Menu Command ID
  UpdateDate Date(8) Last Update Date
  LastUpdate Int(11) Last Update Time
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Created On
  ChangeDate Date(8) Change Date
  CreateTS Int(11) Creatn Time - Incl. Secs
  UpdateTS Int(11) Update Full Time
  UserSign Int(6) Created By
  UserSign2 Int(6) Updated By
  AnaActive VarChar(1) Analytics Active
