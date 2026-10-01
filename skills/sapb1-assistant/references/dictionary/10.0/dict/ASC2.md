<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ASC2 - Service Call Inventory Expenses - History
Module: Service | 19 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SrcvCallID, Line, LogInstanc
Fields (name type(len) description [values] ->parent table):
  SrcvCallID Int(11) Service Call No. - History ->OSCL
  Line Int(6) Row - History default=-1
  ItemCode nVarChar(50) Item No. - History ->OITM
  ItemName nVarChar(200) Item Description - History
  TransToTec Num(19,6) Transfer to Technician - History
  Delivered Num(19,6) Delivered - History
  RetFromTec Num(19,6) Returned from Technician - History
  Returned Num(19,6) Returned - History
  Bill VarChar(1) Bill - History default=Y [Y=Yes, N=No]
  QtyToBill Num(19,6) Quantity to Bill - History
  QtyToInv Num(19,6) Invoiced Qty - History
  ObjectType nVarChar(20) Object Type - History default=191
  LogInstanc Int(11) Log Instance - History
  UserSign Int(6) User Signature - History ->OUSR
  CreateDate Date(8) Creation Date - History
  UserSign2 Int(6) User Signature 2 - History ->OUSR
  UpdateDate Date(8) Date of Update - History
  VisOrder Int(11) Visual Order
  EncryptIV nVarChar(100) Encrypt IV
