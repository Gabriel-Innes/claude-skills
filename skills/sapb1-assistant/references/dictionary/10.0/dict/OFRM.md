<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OFRM - File Format
Module: Administration | 10 columns | ObjType: 183
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  NAME_TYPE: Name, FrmatType
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Name nVarChar(100) File Format Name
  Encoding nVarChar(100) Encoding Type
  FilePath Text(16) Format Project
  IsSystem VarChar(1) System Format default=N [Y=Yes, N=No]
  FrmatType VarChar(1) Format Type default=O [I=Bank Statements, O=Payment File, L=Legal List, P=Predefined, B=Boleto File, R=Padron File]
  FileContnt Text(16) Format Project Content
  FrmatStats VarChar(1) Format Status default=U [A=Assigned, U=Unassigned]
  PaymType VarChar(1) Payment Type default=X [O=Outgoing, I=Incoming, X=]
  Hash nVarChar(128) Binary Content Hash
