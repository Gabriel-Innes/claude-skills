<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RLOG - Resource Edit Log
Module: General | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ResCode, AbsKey
  RESOURCE: SlaveNum, MasterKey, ResType
  USER: UserSign
Fields (name type(len) description [values] ->parent table):
  AbsKey Int(11) Abs Key
  UserSign Int(11) User Sign
  ResType Int(11) Resource Type
  MasterKey nVarChar(64) Master Key
  SlaveNum nVarChar(20) Slave Num
  Date Date(8) Date
  Time Int(6) Time
  FldName nVarChar(10) Field Name
  NewVal nVarChar(64) New Value
  BatchNum Int(11) Batch Change Number
  ResCode Int(11) Resource Code default=-1
