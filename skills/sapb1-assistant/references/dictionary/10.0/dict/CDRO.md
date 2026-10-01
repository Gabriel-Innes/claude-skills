<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CDRO - Drag & Relate - Output Fields
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjectId, FieldId, UserSign
Fields (name type(len) description [values] ->parent table):
  ObjectId nVarChar(4) Object ID
  FieldId Int(6) Field ID
  DescStr nVarChar(30) Description
  VisOrder Int(6) Visual Order default=0
  UserSign Int(6) User Form default=-1 ->OUSR
