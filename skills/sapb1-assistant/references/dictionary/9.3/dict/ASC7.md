<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ASC7 - Service Call BP Address
Module: General | 66 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSCL
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
  State nVarChar(3) State Code
  County nVarChar(7) County Code
  Incoterms nVarChar(3) Incoterms
  Vehicle nVarChar(10) Vehicle ID
  VidState nVarChar(3) Vehicle ID (State)
  NfRef nVarChar(254) NF Reference
  Carrier nVarChar(15) Carrier Code ->OCRD
  QoP Int(11) Quantity of Packs
  PackDesc nVarChar(10) Pack Description
  Brand nVarChar(20) Brand
  NoSU Int(11) Number of Shipping Unit
  NetWeight Num(19,6) Net Weight
  GrsWeight Num(19,6) Gross Weight
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=191 ->ADP1
  TaxId10 nVarChar(100) Tax ID 10
  TransCat nVarChar(100) Transaction Category
  FormNo nVarChar(100) Form No.
  TaxId11 nVarChar(100) Tax ID 11
  StreetS nVarChar(100) Street
  BlockS nVarChar(100) Block
  BuildingS Text(16) Building/Floor/Room
  CityS nVarChar(100) City
  ZipCodeS nVarChar(20) Zip Code
  CountyS nVarChar(100) County
  StateS nVarChar(3) State ->OCST
  CountryS nVarChar(3) Country ->OCRY
  AddrTypeS nVarChar(100) Address Type
  StreetNoS nVarChar(100) Street No.
  StreetB nVarChar(100) Street
  BlockB nVarChar(100) Block
  BuildingB Text(16) Building/Floor/Room
  CityB nVarChar(100) City
  ZipCodeB nVarChar(20) Zip Code
  CountyB nVarChar(100) County
  StateB nVarChar(3) State ->OCST
  CountryB nVarChar(3) Country ->OCRY
  AddrTypeB nVarChar(100) Address Type
  StreetNoB nVarChar(100) Street No.
  ImpORExp VarChar(1) Import or Export [N=, Y=]
  Vat VarChar(1) VAT default=N [N=No VAT Support, Y=VAT Support]
  AltCrdNamB nVarChar(100) Alternative BP Name
  AltTaxIdB nVarChar(32) Alternative Tax ID
  Address2S nVarChar(50) Address Name 2
  Address3S nVarChar(50) Address Name 3
  Address2B nVarChar(50) Address Name 2
  Address3B nVarChar(50) Address Name 3
  MainUsage Int(11) Main Usage Code of Document ->OUSG
  GlbLocNumS nVarChar(50) Global Location Number
  GlbLocNumB nVarChar(50) Global Location Number
  CollectDT nVarChar(20) Date and Time of Collection
  TransprtDT Date(8) Transport Starting Date
  TransprtRS nVarChar(100) Transport Reason
  TaxId12 nVarChar(50) Tax ID 12
  TaxId13 nVarChar(100) Deductee Ref. No. in India
