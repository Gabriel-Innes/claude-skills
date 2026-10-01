<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OTSH - Project Management Time Sheet - Header
Module: General | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  ProjectID Int(11) Project No. ->OPMG
  DocNum Int(11) Document Number
  Type VarChar(1) Type default=E [E=Employee, U=User, O=Other]
  UserID Int(11) User ID ->OHEM
  LastName nVarChar(50) Last Name
  FirstName nVarChar(50) First Name
  Department Int(6) Department
  DateFrom Date(8) Date From
  DateTo Date(8) Date To
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature
  UserSign2 Int(6) Updating User
  CreateDate Date(8) Production Date
  UpdateTS Int(11) Update Full Time
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
  SAPPassprt Text(16) Extended SAP Passport
