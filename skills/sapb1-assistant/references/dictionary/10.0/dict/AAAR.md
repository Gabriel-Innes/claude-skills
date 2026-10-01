<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AAAR - Substitute Authorizer
Module: General | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  AuthrID Int(11) Authorizer ID ->OUSR
  SubsttID Int(11) Substitute Authorizer ID ->OUSR
  FromDate Date(8) From Date
  ToDate Date(8) To Date
  WtmCode Int(11) Approval Template Code ->OWTM
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
  CreateDate Date(8) Date Created
  CreateTS Int(11) Creatn Time - Incl. Secs
  UserSign Int(11) User Signature ->OUSR
  UserSign2 Int(6) User Signature 2
  Applied VarChar(1) Substitute Action Performed default=N [Y=Yes, N=No]
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Update Date
