<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# APHA - Project Management Subproject - History
Module: General | 22 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  OWNER Int(11) Owner ->OHEM
  NAME nVarChar(254) Name
  START Date(8) Subproject Start Date
  FINISHED Num(19,6) Deduction - Percentage
  ParentID Int(11) Parent Subproject
  ProjectID Int(11) Project No. ->OPMG
  Code Int(11) Subproject No.
  TYP Int(11) Subproject Type ->PMC1
  CONTRIB Num(19,6) Subproject Contribution - Percentage
  STATUS VarChar(1) Status default=O [O=Open, C=Closed]
  END Date(8) Subproject End Date
  COST Num(19,6) Actual Cost
  PLANNED Num(19,6) Planned Cost
  Level Int(11) Depth of Subproject within the project
  DUEDATE Date(8) Due Date
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature
  UserSign2 Int(6) Updating User
  CreateDate Date(8) Production Date
  UpdateTS Int(11) Update Full Time
