<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OBOT - Bill Of Exchang Transaction
Module: Banking | 10 columns | ObjType: 182
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) BOE Transaction key
  UserSign Int(6) User Signature ->OUSR
  StatusFrom VarChar(1) Status from [S=Sent, G=Generated, D=Deposit, P=Paid, F=Failed, V=BoE to Vendor]
  StatusTo VarChar(1) Status To [C=Canceled, G=Generated, D=Deposit, P=Paid, F=Failed, L=Closed, V=BoE to Vendor]
  TranDate Date(8) Transaction Date
  TranTime Int(6) Transaction Time
  Reconciled VarChar(1) was the Boe Reconciled default=N [Y=Yes, N=No]
  TransId Int(11) Transaction Number ->OJDT
  PostDate Date(8) Posting Date
  TaxDate Date(8) Document Date
