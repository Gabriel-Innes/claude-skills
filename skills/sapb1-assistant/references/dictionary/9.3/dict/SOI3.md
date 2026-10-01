<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SOI3 - Statement of Import - Invoices
Module: Reports | 19 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SOINum, WizardId
Fields (name type(len) description [values] ->parent table):
  WizardId Int(11) Wizard ID
  SOINum Int(11) Statement No.
  AgrNum Int(11) Blanket Agreement No.
  AgrNo Int(11) Blanket Agreement Entry ->OOAT
  CardCode nVarChar(15) Customer/Vendor Code ->OCRD
  CardName nVarChar(100) Customer/Vendor Name
  PayToCtry nVarChar(3) BP Pay-to Country
  PmntNum Int(11) Payment No.
  PmntEntry Int(11) Payment Entry ->OVPM
  PmntType Int(11) Payment Type
  PmntDate Date(8) Payment Date
  ExcBasSum Num(19,6) Sum of Excise Base Amount
  ExciseSum Num(19,6) Sum of Excise Amount
  VatBaseSum Num(19,6) Sum of VAT Base Amount
  VatSum Num(19,6) Total of VAT
  RegNo nVarChar(18) Registration No.
  RegDate Date(8) Registration Date
  ExecStat VarChar(1) Execution Status default=S [S=Saved, E=Executed]
  BPLId Int(11) Branch ->OBPL
