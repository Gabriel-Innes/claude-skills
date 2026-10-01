<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ODSC - Bank Codes
Module: Banking | 21 columns | ObjType: 3
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SECONDARY U: CountryCod, BankCode
Fields (name type(len) description [values] ->parent table):
  BankCode nVarChar(30) Bank Code
  BankName nVarChar(250) Bank Name
  DfltAcct nVarChar(50) Account for Outgoing Checks
  DfltBranch nVarChar(50) Branch for Outgoing Checks
  NextChckNo Int(11) Next Check Number
  Locked VarChar(1) Locked default=N [N=Changeable, Y=Locked]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  SwiftNum nVarChar(50) BIC/SWIFT Code
  IBAN nVarChar(50) IBAN
  CountryCod nVarChar(3) Country/Region Code ->OCRY
  PostOffice VarChar(1) Post Office default=N [Y=Yes, N=No]
  AliasName nVarChar(50) Alias Name
  AbsEntry Int(11) Absolute entry
  DfltActKey Int(11) Default Bank Account Key ->DSC1
  NextNum Int(11) Our Number in Next Boleto
  BsPstDate VarChar(1) Posting Date Definition default=C [S=Statement Date, L=Row Date, V=Due Date, C=Current Date]
  BsValDate VarChar(1) Due Date Definition default=C [S=Statement Date, L=Row Date, V=Due Date, C=Current Date]
  BnkOpCode Int(11) Bank Operation Code List ->OBOC
  BsDocDate VarChar(1) Document Date Definition default=C [S=Statement Date, L=Row Date, V=Due Date, C=Current Date]
  TaxIdNum nVarChar(32) Federal Tax ID
