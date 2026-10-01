<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OSLT - Service Call Solutions
Module: Service | 17 columns | ObjType: 189
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SltCode
Fields (name type(len) description [values] ->parent table):
  SltCode Int(11) Solution Code
  ItemCode nVarChar(50) Item No. ->OITM
  StatusNum Int(11) Status ->OSST
  Owner Int(11) Owner ->OUSR
  CreatedBy Int(11) Created By ->OUSR
  DateCreate Date(8) Creation Date
  UpdateBy Int(11) Last Update by ->OUSR
  DateUpdate Date(8) Last Update Date
  Subject nVarChar(254) Subject
  Symptom nVarChar(254) Symptom
  Cause nVarChar(254) Cause
  Descriptio Text(16) Description
  Attachment Text(16) Attachments
  AtcEntry Int(11) Attachment Entry
  Transfered VarChar(1) Year Transfer default=N
  Instance Int(6) Instance default=0
  DataVers Int(11) Data Version default=1
