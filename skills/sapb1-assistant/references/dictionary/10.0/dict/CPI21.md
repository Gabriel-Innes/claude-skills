<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CPI21 - A/P Correction Invoice - Document Reference Information
Module: Marketing Documents | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, RefType
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjectType nVarChar(20) Object Type default=163
  LogInstanc Int(11) Log Instance default=0
  RefType VarChar(1) Reference Types default=S [S=System Document, E=External Document]
  LineNum Int(11) Line Number
  RefDocEntr Int(11) Referenced Internal Number
  RefDocNum Int(11) Referenced Document Number
  ExtDocNum nVarChar(100) External Referenced Document Number
  RefObjType nVarChar(20) Referenced Object Type [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 234000031=Return Request, 16=Return, 203=A/R Down Payment, 13=A/R Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 280=A/R Tax Invoice, 1470000113=Purchase Request, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Return Request, 21=Goods Return, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 281=A/P Tax Invoice, 69=Landed Costs, 24=Incoming Payments, 46=Outgoing Payments, 57=Checks for Payment, 321=Internal Reconciliation, 34=Recurring Posting, 30=Journal Entry, 59=Goods Receipt, 60=Goods Issue, 162=Inventory Revaluation, 1470000065=Inventory Counting, 10000071=Inventory Posting, 1250000001=Inventory Transfer Request, 67=Inventory Transfer, 202=Production Order, 13001=Original Invoice, -1=External Document, 20301=Original Down Payment Invoice]
  AccessKey nVarChar(100) Access Key
  IssueDate Date(8) Date of Issue
  IssuerCNPJ nVarChar(100) Issuer CNPJ
  IssuerCode nVarChar(10) Fiscal Document Issuer UF Code
  Model nVarChar(6) Fiscal Document Model
  Series nVarChar(3) Fiscal Document Series
  Number Int(11) Fiscal Document Number
  RefAccKey nVarChar(100) Referenced CT-e Access Key
  RefAmount Num(19,6) Referenced Amount
  SubSeries nVarChar(3) Fiscal Document Subseries
  Remark nVarChar(254) Remarks
  LinkRefTyp nVarChar(20) Link Reference Type default=00 [00=, 01=Nota de cr�dito de los documentos relacionados, 02=Nota de d�bito de los documentos relacionados, 03=Devoluci�n de mercanc�a sobre facturas o traslados previos, 04=Sustituci�n de los CFDI previos, 05=Traslados de mercancias facturados previamente, 06=Factura generada por los traslados previos, 07=CFDI por aplicaci�n de anticipo, 08=Customs, MX_08=Factura generada por pagos en parcialidades, 09=Factura generada por pagos diferidos]
