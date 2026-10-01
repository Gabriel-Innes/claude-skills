<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SCL5 - Service Call Activities
Module: Service | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SrvcCallId, Line
Fields (name type(len) description [values] ->parent table):
  SrvcCallId Int(11) Service Call No. ->OSCL
  Line Int(6) Row default=-1
  ClgID Int(11) Activity Code ->OCLG
  ObjectType nVarChar(20) Object Type default=191
  LogInstanc Int(11) Log Instance
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) User Signature 2 ->OUSR
  UpdateDate Date(8) Date of Update
  VisOrder Int(11) Visual Order
  EncryptIV nVarChar(100) Encrypt IV
