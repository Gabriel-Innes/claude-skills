<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OSDL - Sensitive Personal Data Access Log
Module: General | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  DataSubjct VarChar(1) Data Subject Type [E=OHEM, B=OCRD, U=OUSR, C=OCPR]
  SubjctKey nVarChar(100) Data Subject Key
  DataTable nVarChar(5) Data Table
  TblKeyCnt Int(11) Data Table Key Count
  KeyVal1 nVarChar(100) Key Value 1
  KeyVal2 nVarChar(100) Key Value 2
  KeyVal3 nVarChar(100) Key Value 3
  KeyVal4 nVarChar(100) Key Value 4
  Property nVarChar(50) Property Name
  UserSign Int(11) Access User Signature ->OUSR
  AccessDate Int(11) Access Date
  AccessTime Int(11) Access Time
  AccessChnl VarChar(1) Access Channel [U=UI, D=DI, B=Browser Access, W=Personal Data Management Wizard, A=Bank File]
  Version nVarChar(11) Version
