<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# WDD1 - Documents for Approval - Authorizers
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: UserID, StepCode, WddCode
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
