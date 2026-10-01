<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ASC1 - Service Call Solutions - History
Module: Service | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: srvcCallID, line, logInstanc
Fields (name type(len) description [values] ->parent table):
  srvcCallID Int(11) Service Call No. - History ->OSCL
  line Int(6) Row Number - History default=-1
  solutionID Int(11) Solution ID - History ->OSLT
  objType nVarChar(20) Object Type - History default=191
  logInstanc Int(11) Log Instance - History
  userSign Int(6) Creating User - History ->OUSR
  createDate Date(8) Creation Date - History
  userSign2 Int(6) Updating User - History ->OUSR
  updateDate Date(8) Date of Update - History
  VisOredr Int(11) Visual Order
  EncryptIV nVarChar(100) Encrypt IV
