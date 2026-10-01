<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCRY - Countries
Module: Administration | 19 columns | ObjType: 129
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
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
  CntCodNum nVarChar(4) Country Code Number
  Siscomex nVarChar(3) SISCOMEX Country Code
  IsIntraS VarChar(1) Intrastat Trans. default=N [Y=Yes, N=No]
  EAEU VarChar(1) EAEU default=N [Y=Yes, N=No]
