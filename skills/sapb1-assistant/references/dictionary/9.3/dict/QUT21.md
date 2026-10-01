<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# QUT21 - Sales Quotation - Document Reference Information
Module: Marketing Documents | 21 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: RefType, LineNum, DocEntry
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjectType nVarChar(20) Object Type default=23
  LogInstanc Int(11) Log Instance default=0
  RefType VarChar(1) Reference Types default=S [S=System Document, E=External Document]
  LineNum Int(11) Line Number
  RefDocEntr Int(11) Referenced Internal Number
  RefDocNum Int(11) Referenced Document Number
  ExtDocNum nVarChar(100) External Referenced Document Number
  RefObjType nVarChar(20) Referenced Object Type [-1=External Document, 23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 234000031=Return Request, 16=Return, 203=Down Payment Incoming, 13=A/R Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 280=A/R Tax Invoice, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Return Request, 21=Goods Return, 204=Down Payment Outgoing, 18=A/P Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 281=A/P Tax Invoice, 69=Landed Costs, 24=Incoming Payments, 30=Journal Entry, 202=Production Order, 321=Internal Reconciliation]
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
  LinkRefTyp nVarChar(20) Link Reference Type default=00 [00=, 01=Nota de crédito de los documentos relacionados, 02=Nota de débito de los documentos relacionados, 03=Devolución de mercancía sobre facturas o traslados previos, 04=Sustitución de los CFDI previos, 05=Traslados de mercancias facturados previamente, 06=Factura generada por los traslados previos, 07=CFDI por aplicación de anticipo, 08=Customs, MX_08=Factura generada por pagos en parcialidades, MX_09=Factura generada por pagos diferidos]
