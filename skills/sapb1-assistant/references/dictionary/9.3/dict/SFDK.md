<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SFDK - SFDK
Module: General | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
Fields (name type(len) description [values] ->parent table):
  ID Int(11) Feedback DI
  WindowID nVarChar(254) Window ID
  DBName nVarChar(100) Company DB Name
  UserSign Int(11) User Sign
  Date Date(8) Feedback Date
  Time Int(6) Feedback Time
  Version nVarChar(254) Version including patch number
  LOC nVarChar(3) Localization
  UILang nVarChar(3) UI Language
  Feedback Int(6) Feedback
  GUID nVarChar(32) GUID
  StrLID nVarChar(11) String List ID
  StrIID nVarChar(11) String Index ID
  MsgText nVarChar(254) Message text
