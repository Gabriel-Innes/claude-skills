<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# APMG - Project Management Document - History
Module: General | 33 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  OWNER Int(11) Owner ->OHEM
  NAME nVarChar(254) Project Name
  START Date(8) Project Start Date
  FINISHED Num(19,6) Deduction - Percentage
  DocNum Int(11) Document Number
  Series Int(11) Series
  TYP VarChar(1) Project Type default=E [E=External, I=Internal]
  CARDCODE nVarChar(15) BP Code ->OCRD
  CARDNAME nVarChar(100) BP Name
  CONTACT Int(11) Contact Person ->OCPR
  TERRITORY Int(11) Business Partner Territory ->OTER
  EMPLOYEE Int(11) Sales Employee default=-1 ->OSLP
  WithPhases VarChar(1) Project with Phases default=N [Y=Yes, N=No]
  STATUS VarChar(1) Status default=S [S=Started, P=Paused, T=Stopped, F=Finished, N=Canceled]
  DUEDATE Date(8) Due Date
  CLOSING Date(8) Closing Date
  FIPROJECT nVarChar(20) Financial Project ->OPRJ
  RISK VarChar(1) Risk Level default=L [L=Low, M=Medium, H=High]
  INDUSTRY Int(11) Industry Code ->OOND
  REASON Text(16) Comments
  Free_Text Text(16) Free Text
  BPLid Int(11) Business Place ID ->OBPL
  AtcEntry Int(11) Attachment Entry
  Attachment Text(16) Attachments
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature
  UserSign2 Int(6) Updating User
  CreateDate Date(8) Production Date
  UpdateTS Int(11) Update Full Time
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
  EncryptIV nVarChar(100) Encrypt IV
