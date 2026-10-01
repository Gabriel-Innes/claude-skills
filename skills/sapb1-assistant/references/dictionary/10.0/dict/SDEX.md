<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SDEX - Dynamic Extensions
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: FormId, ItemId, ColumnId
Fields (name type(len) description [values] ->parent table):
  FormId Int(11) Form ID
  ItemId Int(11) Item ID default=0
  ColumnId Int(11) Column ID default=0
  BefAppl Text(16) Application Before
  AftAppl Text(16) Application After
  BefScript VarChar(1) Is Script Before default=Y [Y=Yes, N=No]
  AftScript VarChar(1) Is Script After default=Y [Y=Yes, N=No]
  UserSign Int(6) User Signature default=-1 ->OUSR
