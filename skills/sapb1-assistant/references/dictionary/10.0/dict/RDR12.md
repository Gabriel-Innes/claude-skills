<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# RDR12 - Sales Order - Tax Extension
Module: Marketing Documents | 117 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDR
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
  NfRef nVarChar(254) Nota Fiscal Reference
  Carrier nVarChar(15) Carrier Code
  QoP Int(11) Quantity of Packs
  PackDesc nVarChar(10) Pack Description
  Brand nVarChar(20) Brand
  NoSU Int(11) Number of Shipping Unit
  NetWeight Num(19,6) Net Weight
  GrsWeight Num(19,6) Gross Weight
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=17 ->ADP1
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
  CountryS nVarChar(3) Country/Region ->OCRY
  AddrTypeS nVarChar(100) Address Type
  StreetNoS nVarChar(100) Street No.
  StreetB nVarChar(100) Street
  BlockB nVarChar(100) Block
  BuildingB Text(16) Building/Floor/Room
  CityB nVarChar(100) City
  ZipCodeB nVarChar(20) Zip Code
  CountyB nVarChar(100) County
  StateB nVarChar(3) State ->OCST
  CountryB nVarChar(3) Country/Region ->OCRY
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
  ImpExpNo nVarChar(100) Import/Export Bill No.
  ImpExpDate Date(8) Import/Export Date
  BpGSTType Int(11) GST Regn Type of BP
  BpGSTN nVarChar(15) GST Regn No of BP
  BpStateCod nVarChar(3) State Code of Business Partner ->OCST
  BPStatGSTN nVarChar(2) GST State Code of BP
  LocGSTType Int(11) GST Regn Type of Location
  LocGSTN nVarChar(15) GST Regn No of Location
  LocStatCod nVarChar(3) State Code of Location ->OCST
  LocStaGSTN nVarChar(2) GST State Code of Location
  BpCountry nVarChar(3) Country/Region Code of BP ->OCRY
  OrigImpNo nVarChar(100) Original Bill of Entry No.
  OrigImpDat Date(8) Original Bill of Entry Date
  ExportType VarChar(1) Exporting Type default=E [E=Imports/Exports, S=SEZ Developer, U=SEZ Unit, D=Deemed Imports/Exports]
  PortCode nVarChar(100) Port Code
  BoEValue Num(19,6) Bill of Entry Value
  IsIGSTAct VarChar(1) Supply under IGST Account [Y=Yes, N=No]
  ClaimRefun VarChar(1) Claim Refund [Y=Yes, N=No]
  TaxRateDif Int(11) Differential % of Tax Rate [65=, 100=]
  BPGdsIssP nVarChar(15) Goods Issue Place BP
  CNPJGIP nVarChar(100) Goods Issue Place CNPJ
  CPFGIP nVarChar(100) Goods Issue Place CPF
  StreetGIP nVarChar(100) Goods Issue Place Street
  StrtNoGIP nVarChar(100) Goods Issue Place Street No.
  BldngGIP Text(16) Goods Issue Place Building
  ZipGIP nVarChar(20) Goods Issue Place Zip Code
  BlockGIP nVarChar(100) Goods Issue Place Block
  CityGIP nVarChar(100) Goods Issue Place City
  CountyGIP nVarChar(100) Goods Issue Place County
  StateGIP nVarChar(3) Goods Issue Place State ->OCST
  CountryGIP nVarChar(3) Goods Issue Place Country/Region ->OCRY
  PhoneGIP nVarChar(20) Goods Issue Place Phone
  EMailGIP nVarChar(100) Goods Issue Place E-Mail
  DptDateGIP Date(8) Goods Issue Place Departure Date
  BPDelivryP nVarChar(15) Delivery Place BP
  CNPJDlvryP nVarChar(100) Delivery Place CNPJ
  CPFDlvryP nVarChar(100) Delivery Place CPF
  StrtDlvryP nVarChar(100) Delivery Place Street
  StrNoDlvrP nVarChar(100) Delivery Place Street No.
  BldDlvryP Text(16) Delivery Place Building
  ZipDlvryP nVarChar(20) Delivery Place Zip Code
  BlckDlvryP nVarChar(100) Delivery Place Block
  CityDlvryP nVarChar(100) Delivery Place City
  CntyDlvryP nVarChar(100) Delivery Place County
  StatDlvryP nVarChar(3) Delivery Place State ->OCST
  CtryDlvryP nVarChar(3) Delivery Place Country/Region ->OCRY
  FoneDlvryP nVarChar(20) Delivery Place Phone
  MailDlvryP nVarChar(100) Delivery Place E-Mail
  DpDtDlvryP Date(8) Delivery Place Departure Date
  AuthedCNPJ nVarChar(250) Authorized CNPJ or CPF
  TaxId14 nVarChar(250) ITR Filing
