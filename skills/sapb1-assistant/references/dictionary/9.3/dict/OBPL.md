<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OBPL - Business Place
Module: Business Partners | 55 columns | ObjType: 247
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: BPLId
  NAME U: BPLName
Fields (name type(len) description [values] ->parent table):
  BPLId Int(11) Branch ID
  BPLName nVarChar(100) Branch Name
  BPLFrName nVarChar(100) Branch Name (Foreign)
  VATRegNum nVarChar(12) VAT Reg. Number
  RepName nVarChar(15) Rep. Name
  Industry nVarChar(20) Industry
  Business nVarChar(20) Business
  Address nVarChar(254) Address
  AddressFr nVarChar(254) Address (Foreign)
  MainBPL VarChar(1) Main BPL default=N [Y=Main Business Place, N=Not Main Business Place]
  TxOffcNo nVarChar(3) Tax Office No.
  Disabled VarChar(1) Disabled default=N [Y=Disabled, N=Enabled]
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  DflCust nVarChar(15) Default Customer ID ->OCRD
  DflVendor nVarChar(15) Default Vendor ID ->OCRD
  DflWhs nVarChar(8) Default Warehouse ID ->OWHS
  DflTaxCode nVarChar(8) Default Tax Code ->OCNA
  RevOffice nVarChar(100) Tax Office
  TaxIdNum nVarChar(32) Branch Reg. No.
  TaxIdNum2 nVarChar(32) Federal Tax ID 2
  TaxIdNum3 nVarChar(32) Federal Tax ID 3
  AddtnlId nVarChar(32) Additional ID Number
  CompNature Int(11) Nature of Company default=-1 ->OBNI
  EconActT Int(11) Economic Activity Type default=-1 ->OBNI
  CredCOrig nVarChar(2) Credit Contribution Origin ->OBSI
  IPIPeriod nVarChar(2) IPI Period ->OBSI
  CoopAssocT Int(11) Cooperative Association Type default=-1 ->OBNI
  PrefState nVarChar(3) Default State
  ProfTax Int(11) Profit Taxation default=-1 ->OBNI
  CompQualif Int(11) Company Qualification default=-1 ->OBNI
  DeclType Int(11) Declarer Type default=-1 ->OBNI
  AddrType nVarChar(100) Address Type
  Street nVarChar(100) Street
  StreetNo nVarChar(100) Street No.
  Building nVarChar(100) Building/Floor/Room
  ZipCode nVarChar(20) Zip Code
  Block nVarChar(100) Block
  City nVarChar(100) City
  State nVarChar(3) State
  County nVarChar(100) County ->OCNT
  Country nVarChar(3) Country ->OCRY
  PmtClrAct nVarChar(15) Payment Clearing Account ->OACT
  CommerReg nVarChar(60) Commercial Register
  DateOfInc Date(8) Date of Incorporation
  SPEDProf nVarChar(2) SPED Profile ->OBSI
  EnvTypeNFe Int(11) Environment Type NFe default=-1 ->OBNI
  Opt4ICMS VarChar(1) Opting for ICMS 115_03 default=N
  AliasName Text(16) Alias Name
  GlblLocNum nVarChar(50) Global Location Number
  TaxRptFrm Date(8) Tax Wizard Reporting From
  Suframa nVarChar(100) SUFRAMA
  DfltResWhs nVarChar(8) Default Resource Warehouse ID ->OWHS
  SnapshotId Int(11) Snapshot ID default=0
