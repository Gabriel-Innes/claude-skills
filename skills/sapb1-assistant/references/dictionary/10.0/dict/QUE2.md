<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# QUE2 - Queue Elements
Module: Service | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: queueID, elementNum
  OBJ_ELEM U: queueID, objType, elementId
Fields (name type(len) description [values] ->parent table):
  queueID nVarChar(20) Queue ID ->OQUE
  objType nVarChar(20) Object Type
  elementId Int(11) Element ID
  elementNum Int(11) Element Number
  priority Int(11) Priority
  createDate Date(8) Creation Date
  createTime Int(6) Creation Time
