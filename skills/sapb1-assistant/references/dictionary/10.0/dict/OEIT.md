<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OEIT - E-Books Invoice Type
Module: Marketing Documents | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CODE U: Code
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Unique Entry
  Code nVarChar(50) Code
  Descr nVarChar(254) Description
  Issuer VarChar(1) Issuer default=I [I=Included, E=Excluded]
  IssuerBrch VarChar(1) Branch of Issuer default=I [I=Included, E=Excluded, Z=Zero]
  Cnterpart VarChar(1) Counterpart default=I [I=Included, E=Excluded]
  VAT VarChar(1) VAT default=I [I=Included, E=Excluded]
  PaymtMthod VarChar(1) Payment Method default=I [I=Included, E=Excluded]
  SubmitedBy VarChar(1) Submitted By default=C [C=Company, A=Accountant]
  SelfPrice VarChar(1) Self-Pricing default=N [Y=Yes, N=No]
