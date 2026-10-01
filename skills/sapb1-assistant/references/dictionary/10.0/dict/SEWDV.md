<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SEWDV - 
Module: General | 59 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CompDbNam
Fields (name type(len) description [values] ->parent table):
  CompDbNam nVarChar(100) Company Db Name
  SmpTableId nVarChar(3) Smp Table ID
  EwaSentDat nVarChar(10) EWA Sent Date
  CustNumber VarChar(1) Customer Number
  DocPeriod nVarChar(32) Doc Period
  SalesOrdrs Int(11) Sales Orders
  SalDlvDocs Int(11) Sales Delivery Docs
  SalesInvs Int(11) Sales Invoices
  PurcOrders Int(11) Purchase Orders
  GoodRecpts Int(11) Good Receipts
  PurchAPInv Int(11) Purchase AP Invoices
  ServicCall Int(11) Service Calls
  MaterBills Int(11) Meterial Bills
  WorkOrders Int(11) Work Orders
  SalesOppor Int(11) Opportunities
  ItmMasterD Int(11) Item Master Data
  CustBPMasD Int(11) Customer Bp Master Data
  SuppBPMasD Int(11) Supplier Bp Master Data
  SalOrdMinR Int(11) Min Rows Of Sales Orders
  SlDlvrMinR Int(11) Min rows Of Sales DElivery
  SlsInvMinR Int(11) Min rows Of Invoices
  PrcOrdMinR Int(11) Min rows Of Purchase Orders
  GodRcpMinR Int(11) Min rows Of Good Receipts
  WrkOrdMinR Int(11) Min rows Of work orders
  QuotMinR Int(11) Min rows Of QUOT
  RetMinR Int(11) Min rows Of RETURN
  DownMinR Int(11) Min rows Of DOWN
  ARCrdMinR Int(11) Min rows Of ARCREDIT
  GodRecMinR Int(11) Min rows Of GOODREC
  APRetMinR Int(11) Min rows Of APRETURN
  APDwnMinR Int(11) Min rows Of APDOWN
  APInvMinR Int(11) Min rows Of APINVOICE
  APCrdMinR Int(11) Min rows Of APCREDIT
  SalOrdMaxR Int(11) Max Rows Of Sales Orders
  SlDlvrMaxR Int(11) Max rows Of Sales DElivery
  SlsInvMaxR Int(11) Max rows Of Invoices
  PrcOrdMaxR Int(11) Max rows Of Purchase Orders
  GodRcpMaxR Int(11) Max rows Of Good Receipts
  WrkOrdMaxR Int(11) Max rows Of work orders
  QuotMaxR Int(11) Max rows Of QUOT
  RetMaxR Int(11) Max rows Of RETURN
  DownMaxR Int(11) Max rows Of DOWN
  ARCrdMaxR Int(11) Max rows Of ARCREDIT
  GodRecMaxR Int(11) Max rows Of GOODREC
  APRetMaxR Int(11) Max rows Of APRETURN
  APDwnMaxR Int(11) Max rows Of APDOWN
  APInvMaxR Int(11) Max rows Of APINVOICE
  APCrdMaxR Int(11) Min rows Of APCREDIT
  NoPickLst Int(11) No of Picklists in system
  MaxLnPkLst Int(11) Maximum Lines in Pick List
  MinLnPkLst Int(11) Minimum Lines in Pick List
  MaxChldBm Int(11) Maximum children per BOM
  NoProdOrd Int(11) Number of Production order
  NoSrlNum Int(11) No of Serial number items
  NoBatchNum Int(11) No of Batch number items
  StockTras Int(11) Number of Stock Transfers
  MaxRStTrs Int(11) Max num of rows per stock tran
  MinRStTrs Int(11) Min num of rows per stock tran
  NoPriceLst Int(11) 'Number of Price Lists
