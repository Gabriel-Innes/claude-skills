<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OOCC - BoE Occurrence Code
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CODE U: IsMovement, Code
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Code nVarChar(10) Code
  Dscription nVarChar(128) Description
  Note nVarChar(50) Note
  ReqBoeSt VarChar(1) Requested BoE Status [G=Generated, S=Sent, D=Deposited, P=Paid, C=Canceled, F=Failed]
  IsMovement VarChar(1) Is Movement default=N [Y=Yes, N=No]
