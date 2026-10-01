<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# BSJ1 - Backend Scheduling Sub Tasks
Module: General | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TaskID, ID
Fields (name type(len) description [values] ->parent table):
  ID Int(11) Job ID ->OBSJ
  TaskID Int(11) Sub Task ID
  Type nVarChar(50) Task Type
  Params Text(16) Parameters
  RunAs Int(6) Run As User ->OUSR
  Status VarChar(1) Status default=S [S=Scheduled, R=Running, E=Error, F=Finished, P=Pending, C=Creating]
  PostTask Int(11) Post-Task
  PreTask Int(11) Pre-Task
  LastDate Date(8) Last Running Date
  LastTime Int(6) Last Running Time
  Retry Int(11) Retry Times default=0
  TimeOut Int(11) Time out default=20
  Message nVarChar(200) Status Message
