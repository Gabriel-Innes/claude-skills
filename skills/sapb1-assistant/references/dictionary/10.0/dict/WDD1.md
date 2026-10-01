<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# WDD1 - Documents for Approval - Authorizers
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WddCode, StepCode, UserID
Fields (name type(len) description [values] ->parent table):
  WddCode Int(11) Internal ID
  StepCode Int(11) Stage Key ->OWST
  UserID Int(11) Authorizer Code ->OUSR
  Status VarChar(1) Status default=W [W=Pending, Y=Approved, N=Rejected]
  Remarks nVarChar(254) Remarks
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Request Date
  CreateTime Int(6) Request Time
  UpdateDate Date(8) Date of Update
  UpdateTime Int(6) Update Time
  SortId Int(6) Sort Code
  AuthUpdDat Date(8) Authorizer last update date
  AuthUpdTim Int(11) Authorizer last update time
  Substt Int(11) Substitute Authorizer User ID ->OUSR
