<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ASC5 - Service Call Activities - History
Module: Service | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, Line, SrvcCallId
Fields (name type(len) description [values] ->parent table):
  SrvcCallId Int(11) Service Call No. ->OSCL
  Line Int(6) Row No. default=-1
  ClgID Int(11) Activity Code ->OCLG
  ObjectType nVarChar(20) Object Type default=191
  LogInstanc Int(11) Log Instance
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) User Signature 2 ->OUSR
  UpdateDate Date(8) Date of Update
  VisOrder Int(11) Visual Order
