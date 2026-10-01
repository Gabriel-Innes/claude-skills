<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OMPF - Message Preferences
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: MessageUid, FormUid, UserSign
Fields (name type(len) description [values] ->parent table):
  MessageUid Int(11) Message UID
  FormUid Int(11) Form UID
  UserSign Int(6) User Signature ->OUSR
  SelctedBtn Int(11) Selected Button
