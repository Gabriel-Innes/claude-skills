<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# PQW1 - Purchase Quotation Generation: Line Items
Module: Administration | 24 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OPQW
  LineNum Int(11) Row Number
  ItemCode nVarChar(50) Item No. ->OITM
  Dscription nVarChar(200) Item/Service Description
  PQTReqDate Date(8) Pur Quotation: Required Date
  PQTReqQty Num(19,6) Pur Quotation: Required Qty
  BuyUnitMsr nVarChar(100) Purchasing UoM
  FreeTxt nVarChar(100) Free Text
  PQTGrpNum Int(11) Pur. Quotation Group Number
  PQTGrpSer Int(11) Pur. Quotation Group Series
  PQTGrpHW VarChar(1) Pur. Quotation Group Manual default=N [Y=Yes, N=No]
  ValidUntil Date(8) Valid Until Date
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  PQTSeries Int(11) Purchase Quotation Series ->NNM1
  PRAbsEntry Int(11) Purchase Request Number ->OPRQ
  ReqName nVarChar(155) Requester Name
  PRLineNum Int(11) Purchase Request Row Number
  PRLineStat VarChar(1) Purchase Request Row Status
  DistriRule nVarChar(8) Distribution Rule
  Project nVarChar(20) Project Code
  VendMfrNum nVarChar(17) Vendor Mfr Catalog No.
  ShipType Int(6) Shipping Type
  ItmPerUnit Num(19,6) No. of Items per Purchase Unit
  PriceMode VarChar(1) Price Mode default=N [N=Net, G=Gross]
