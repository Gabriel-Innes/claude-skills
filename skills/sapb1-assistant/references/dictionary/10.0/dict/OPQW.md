<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OPQW - Purchase Quotation Generation: Parameter Sets
Module: Administration | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SET_NAME U: SetName
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  SetName nVarChar(20) Set Name
  SetDesc nVarChar(100) Set Description
  CreateDate Date(8) Creation Date
  ModifyDate Date(8) Last Modified Date
  UserSign Int(6) User Signature ->OUSR
  CreatDraft VarChar(1) Create Drafts default=N [Y=Yes, N=No]
  GroupBy VarChar(1) Group By default=B [B=Business Partner, I=Item]
  ValidUntil Date(8) Valid Until Date
  BPLId Int(11) Branch ->OBPL
  ReqDate Date(8) Required Date
  BaseOn VarChar(1) Base On Type
