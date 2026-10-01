<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SCL2 - Service Call Inventory Expenses
Module: Service | 19 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SrcvCallID, Line
Fields (name type(len) description [values] ->parent table):
  SrcvCallID Int(11) Service Call No. ->OSCL
  Line Int(6) Row default=-1
  ItemCode nVarChar(50) Item No. ->OITM
  ItemName nVarChar(200) Item Description
  TransToTec Num(19,6) Transfer to Technican
  Delivered Num(19,6) Delivered
  RetFromTec Num(19,6) Returned from Technician
  Returned Num(19,6) Returned
  Bill VarChar(1) Bill default=Y [Y=Yes, N=No]
  QtyToBill Num(19,6) Quantity to Bill
  QtyToInv Num(19,6) Invoiced Qty
  ObjectType nVarChar(20) Object Type default=191
  LogInstanc Int(11) Log Instance
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) User Signature 2 ->OUSR
  UpdateDate Date(8) Date of Update
  VisOrder Int(11) Visual Order
  EncryptIV nVarChar(100) Encrypt IV
