<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ODSC - Bank Codes
Module: Banking | 20 columns | ObjType: 3
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  SECONDARY U: BankCode, CountryCod
Fields (name type(len) description [values] ->parent table):
  BankCode nVarChar(30) Bank Code
  BankName nVarChar(250) Bank Name
  DfltAcct nVarChar(50) Account for Outgoing Checks
  DfltBranch nVarChar(50) Branch for Outgoing Checks
  NextChckNo Int(11) Next Check Number
  Locked VarChar(1) Locked default=N [N=Changeable, Y=Locked]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  SwiftNum nVarChar(50) BIC/SWIFT Code
  IBAN nVarChar(50) IBAN
  CountryCod nVarChar(3) Country Code ->OCRY
  PostOffice VarChar(1) Post Office default=N [Y=Yes, N=No]
  AliasName nVarChar(50) Alias Name
  AbsEntry Int(11) Absolute entry
  DfltActKey Int(11) Default Bank Account Key ->DSC1
  NextNum Int(11) Our Number in Next Boleto
  BsPstDate VarChar(1) Posting Date Definition default=C [S=Statement Date, L=Row Date, V=Due Date, C=Current Date]
  BsValDate VarChar(1) Due Date Definition default=C [S=Statement Date, L=Row Date, V=Due Date, C=Current Date]
  BnkOpCode Int(11) Bank Operation Code List ->OBOC
  BsDocDate VarChar(1) Document Date Definition default=C [S=Statement Date, L=Row Date, V=Due Date, C=Current Date]
