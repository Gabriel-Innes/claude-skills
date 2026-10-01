<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OLCT - Location
Module: Inventory and Production | 51 columns | ObjType: 144
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
  LOCATION U: Location
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Location Code
  Location nVarChar(100) Name
  UserSign Int(6) User Signature ->OUSR
  PanCirNo nVarChar(32) PAN Circle No.
  PanWardNo nVarChar(32) PAN Ward No.
  PanOfficer nVarChar(32) PAN Assessing Officer
  TanCirNo nVarChar(32) TAN Circle No.
  TanWardNo nVarChar(32) TAN Ward No.
  TanOfficer nVarChar(32) TAN Assessing Officer
  LstVatNo nVarChar(100) LST/VAT Number
  CstNo nVarChar(100) CST Number
  ExemptNo nVarChar(100) Exemption Number
  TanNo nVarChar(100) TAN Number
  ServTaxNo nVarChar(100) Service Tax Number
  AsseType nVarChar(100) Assessee Type
  CompType nVarChar(100) Company Type
  NatOfBiz nVarChar(100) Nature of Business
  TinNo nVarChar(100) TIN Number
  PanNo nVarChar(10) PAN Number
  RegType nVarChar(2) Registration Type [XM=XM, XD=XD, EM=EM, ED=ED, SD=SD]
  EccNo nVarChar(40) ECC Number
  CeRegNo nVarChar(40) CE Register Number
  CeRange nVarChar(60) CE Range
  CeDivision nVarChar(60) CE Division
  CeComRate nVarChar(60) CE Commissionerate
  ManuCode nVarChar(60) Manufaturer Code
  Jurisd nVarChar(60) Jurisdiction
  Street nVarChar(100) Street
  Block nVarChar(100) Block
  ZipCode nVarChar(20) Zip Code
  City nVarChar(100) City
  County nVarChar(100) County
  Country nVarChar(3) Country ->OCRY
  State nVarChar(3) State
  Building Text(16) Building/Floor/Room
  SSIExmpt VarChar(1) SSI Exemption default=N [Y=Yes, N=No]
  SSIExmptSt VarChar(1) SSI Exemption Status default=E [E=New Location, N=Upgrade Not Changed, C=Upgrade Changed]
  CitAddress nVarChar(254) CIT Address
  CitCity nVarChar(100) CIT City
  CitPinCode nVarChar(10) CIT Pin Code
  OnHoldAct nVarChar(15) Capital Goods On Hold Account ->OACT
  GSTRegnNo nVarChar(15) GSTIN
  GSTRelevt nVarChar(2) GST Location Relevant default=N
  GSTTDS nVarChar(30) GSTIN TDS
  GSTISD nVarChar(30) GSTIN ISD
  GSTType Int(11) GST Type [-1=, 1=Regular/TDS/ISD, 2=Casual Taxable Person, 3=Composition Levy, 4=Government Department or PSU, 5=Non-Resident Taxable Person, 6=UN Agency or Embassy] ->OGTY
  VendorCode nVarChar(15) Vendor Code ->OCRD
  CstmerCode nVarChar(15) Customer Code ->OCRD
  DropShip nVarChar(8) Drop Ship Warehouse ->OWHS
  IngClrAc nVarChar(15) Ineligible ITC Clearing A/C
  IntBrClrAc nVarChar(15) Inter-branch ITC Clearing A/C
