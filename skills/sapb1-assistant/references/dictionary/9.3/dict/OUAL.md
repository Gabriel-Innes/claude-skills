<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OUAL - User Action Log
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
  TIME: ActionTime, ActionDate
  ID_KEY: ObjectKey, ObjectId
Fields (name type(len) description [values] ->parent table):
  Id Identity(11) ID
  UserId Int(6) User Id ->OUSR
  ActionDate Date(8) Action Date
  ActionTime Int(11) Action Time
  ActionType VarChar(1) Action Type
  ObjectId Int(11) Object Id
  ObjectKey nVarChar(64) Object Key
