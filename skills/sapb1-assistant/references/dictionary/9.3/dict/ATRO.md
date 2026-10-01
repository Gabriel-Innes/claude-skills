<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ATRO - Transportation Document - History
Module: Marketing Documents | 24 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, AbsEntry
  NEXT_NUM_U U: LogInstanc, IssueGate, WhsCode, NextNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  NextNum Int(11) Consecutive Number
  PostDate Date(8) Posting Date
  EDocGenTyp VarChar(1) El. Doc. Gen. Type default=N [N=Not Relevant, G=Generate, L=Generate Later]
  EDocExpFrm Int(11) Electronic Doc. Export Format
  TranspNum nVarChar(100) Transportation Number
  Expiration Date(8) Expiration Date
  Vehicle nVarChar(10) Vehicle ID
  TrailerID nVarChar(10) Trailer ID
  Carrier nVarChar(15) Carrier Code
  IssueGate Int(11) Issue Gate default=0
  AtcEntry Int(11) Attachment Entry
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature
  UserSign2 Int(6) Updating User
  CreateDate Date(8) Production Date
  UpdateTS Int(11) Update Full Time
  CANCELED VarChar(1) Canceled default=N [Y=Yes, N=No]
  Weight Num(19,6) Weight
  WghtUnit Int(6) Unit of Weight
  TotalLC Num(19,6) Row Total
  WhsCode nVarChar(8) Warehouse Code
  COTcode nVarChar(3) COT Code
