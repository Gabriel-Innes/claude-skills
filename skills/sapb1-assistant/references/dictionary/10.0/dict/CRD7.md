<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CRD7 - Fiscal IDs for BP Master Data
Module: Business Partners | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CardCode, Address, AddrType
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(25) BP Code ->OCRD
  Address nVarChar(50) Address
  TaxId0 nVarChar(100) Tax ID 0
  TaxId1 nVarChar(100) Tax ID 1
  TaxId2 nVarChar(100) Tax ID 2
  TaxId3 nVarChar(100) Tax ID 3
  TaxId4 nVarChar(100) Tax ID 4
  TaxId5 nVarChar(100) Tax ID 5
  TaxId6 nVarChar(100) Tax ID 6
  TaxId7 nVarChar(100) Tax ID 7
  TaxId8 nVarChar(100) Tax ID 8
  TaxId9 nVarChar(100) Tax ID 9
  CNAEId Int(11) Brazil CNAE Code ->OCNA
  TaxId10 nVarChar(100) Tax ID 10
  TaxId11 nVarChar(100) Tax ID 11
  AddrType VarChar(1) Address Type default=S [S=Ship To, B=Bill To]
  ECCNo nVarChar(40) E.C.C. No.
  CERegNo nVarChar(40) C.E. Registration No.
  CERange nVarChar(60) C.E. Range
  CEDivis nVarChar(60) C.E. Division
  CEComRate nVarChar(60) C.E. Commisionerate
  LogInstanc Int(11) Log Instance default=0
  SefazDate Date(8) Date of Update from SEFAZ
  TaxId12 nVarChar(50) Tax ID 12
  TaxId13 nVarChar(100) Deductee Ref. No. in India
  AToRetrNFe VarChar(1) Authorization to Retrieve NFe from SEFAZ default=N [Y=Yes, N=No]
  TaxId14 nVarChar(250) ITR Filing
