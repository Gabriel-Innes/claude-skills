<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AWLS - Workflow - Task Details
Module: Administration | 34 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TaskID, LogIns
Fields (name type(len) description [values] ->parent table):
  WFInstID Int(11) Workflow Instance ID ->OWFI
  TaskID Int(11) Task ID
  WFID nVarChar(64) Workflow ID
  WFName nVarChar(100) Workflow Name
  TaskDesc nVarChar(100) Task Description
  ObjType nVarChar(20) Object Type
  Operation VarChar(1) Operation [A=Add, U=Update, D=Delete]
  ObjKey nVarChar(100) Object Key
  EnterDate Date(8) Enter Date
  EnterTime Int(6) Enter Time
  TaskType VarChar(1) Task Type
  DueDate Date(8) Due Date
  DueTime Int(6) Due Time
  UpdateDate Date(8) Update Date - History
  UpdateTime Int(6) Update Time - History
  Owner nVarChar(25) Owner
  Priority Int(6) Priority default=2 [1=High, 2=Medium, 3=Low]
  UserSign Int(6) User Signature
  Status VarChar(1) Status default=W [S=Setup, W=To Be Picked, P=Picking, G=In Progress, D=Completing, F=Completed, N=Suspended, C=Cancelling, Q=Canceled, O=Forwarding, E=Error]
  LogIns Int(11) Log Instance - History
  UserSign2 Int(6) Updating User - History
  Deleted VarChar(1) Deleted - History
  DuraDays Int(11) Duration Days
  DuraHours Int(6) Duration Hours
  TaskName nVarChar(100) Task Name
  isPicked VarChar(1) Is Picked default=N
  Attachment Text(16) Attachment
  AtcEntry Int(11) Attachment Entry
  WorkListId Int(11) Worklist ID
  ObjSubType nVarChar(64) Object Subtype
  ForwardTo nVarChar(25) User to Forward
  WasRead VarChar(1) Line Read default=N
  TrigParams Text(16) Trigger Parameters
  Key nVarChar(254) Task ID in XML
