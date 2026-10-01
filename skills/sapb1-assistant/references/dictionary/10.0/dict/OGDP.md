<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OGDP - General Data Protection Wizard
Module: Reports | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SECONDARY U: RunName
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  RunName nVarChar(100) Wizard Run Name
  RunDate Date(8) Wizard Run Date
  Status VarChar(1) Wizard Run Status default=S [S=Saved, E=Executed, P=Printed, V=Print Preview Generated]
  UserSign Int(6) User Signature
  UserSign2 Int(6) Updating User
  CreateDate Date(8) Creation Date
  CreateTS Int(11) Create Time - Incl. Secs
  UpdateDate Date(8) Date of Update
  UpdateTS Int(11) Update Full Time
  Action VarChar(1) Personal Data Management Wizard Action default=R [R=Personal Data Report, E=Personal Data Cleanup, B=Personal Data Blocking, U=Personal Data Unblocking, I=Determine Natural Persons, N=Reverse Natural Person Determination]
  BPType VarChar(1) Business Partner Type default=B [B=Business Partners, D=Default Customers]
  PostDateTo Date(8) Posting Date To
  EmpType VarChar(1) Employee Type default=E [E=Employees, S=Sales Employees and Buyers]
