<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SCL1 - Service Call Solutions - Rows
Module: Service | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: srvcCallID, line
Fields (name type(len) description [values] ->parent table):
  srvcCallID Int(11) Service Call No. ->OSCL
  line Int(6) Row No. default=-1
  solutionID Int(11) Solution ID ->OSLT
  objType nVarChar(20) Object Type default=191
  logInstanc Int(11) Log Instance
  userSign Int(6) Creating User ->OUSR
  createDate Date(8) Creation Date
  userSign2 Int(6) Updating User ->OUSR
  updateDate Date(8) Date of Update
  VisOredr Int(11) Visual Order
  EncryptIV nVarChar(100) Encrypt IV
