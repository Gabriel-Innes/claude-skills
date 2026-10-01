<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OCRY - Countries/Regions
Module: Administration | 22 columns | ObjType: 129
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(3) Code
  Name nVarChar(100) Name
  AddrFormat Int(6) Address Format ->OADF
  UserSign Int(6) User Signature ->OUSR
  IsEC VarChar(1) EU default=N [Y=Yes, N=No]
  ReportCode nVarChar(3) Code for Reports
  TaxIdDigts Int(6) No. of Digits for Tax ID
  BnkCodDgts Int(11) No. of Digits for Bank Code
  BnkBchDgts Int(11) No. of Digits for Branch
  BnkActDgts Int(11) No. of Digits for Account No.
  BnkCtKDgts Int(11) No. of Digits for Control No.
  ValDomAcct nVarChar(3) Domestic Bank Acct. Validation default=XX [XX=, BE=Belgium, ES=Spain, FR=France, IT=Italy, NL=Netherlands, PT=Portugal]
  ValIban VarChar(1) IBAN Validation default=N [Y=Yes, N=No]
  IsBlackLst VarChar(1) On Black List default=N [Y=Yes, N=No]
  UICCode nVarChar(3) UIC Country Code
  CntCodNum nVarChar(4) Country/Region Code Number
  Siscomex nVarChar(3) SISCOMEX Country/Region Code
  IsIntraS VarChar(1) Intrastat Trans. default=N [Y=Yes, N=No]
  EAEU VarChar(1) EAEU default=N [Y=Yes, N=No]
  ISO2Code nVarChar(2) ISO Alpha-2 code
  ISO3Code nVarChar(3) ISO Alpha-3 code
  ISONumeric nVarChar(3) ISO Numeric
