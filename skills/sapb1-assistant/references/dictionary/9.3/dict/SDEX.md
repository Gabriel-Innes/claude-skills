<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SDEX - Dynamic Extensions
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ColumnId, ItemId, FormId
Fields (name type(len) description [values] ->parent table):
  FormId Int(11) Form ID
  ItemId Int(11) Item ID default=0
  ColumnId Int(11) Column ID default=0
  BefAppl Text(16) Application Before
  AftAppl Text(16) Application After
  BefScript VarChar(1) Is Script Before default=Y [Y=Yes, N=No]
  AftScript VarChar(1) Is Script After default=Y [Y=Yes, N=No]
  UserSign Int(6) User Signature default=-1 ->OUSR
