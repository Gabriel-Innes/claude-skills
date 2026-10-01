<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# RTPL - Translation Problems Log
Module: General | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Language, ResKey
Fields (name type(len) description [values] ->parent table):
  Language Int(11) Language Code
  ResKey nVarChar(15) Resource Key
  Created Date(8) Creation Date
  CreateTime Int(6) Generation Time
  Updated Date(8) Update Date
  UpdateTime Int(6) Update Time
  UserText Text(16) Memo
  Attachment Text(16) Attached File
  UserName nVarChar(254) User Name
  E_Mail nVarChar(100) E-Mail
