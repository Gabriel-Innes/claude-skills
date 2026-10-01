<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# QUE2 - Queue Elements
Module: Service | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: elementNum, queueID
  OBJ_ELEM U: elementId, objType, queueID
Fields (name type(len) description [values] ->parent table):
  queueID nVarChar(20) Queue ID ->OQUE
  objType nVarChar(20) Object Type
  elementId Int(11) Element ID
  elementNum Int(11) Element Number
  priority Int(11) Priority
  createDate Date(8) Creation Date
  createTime Int(6) Creation Time
