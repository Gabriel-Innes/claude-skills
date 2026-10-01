<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AEC7 - Export Mapping Determination
Module: Reports | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal ID
  Code nVarChar(8) Protocol Code ->OECM
  Priority Int(11) Determination Priority
  BPCode nVarChar(15) Customer/Vendor Code ->OCRD
  Country nVarChar(3) Country/Region ->OCRY
  Serie Int(11) Digital Series default=-1 ->NNM1
  DocType nVarChar(20) Document Type default=-1 [18=A/P Invoice, 19=A/P Credit Memo, 204=A/P Down Payment, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 20=Goods Receipt PO, 21=Goods Return, 24=Incoming Payment, 46=Outgoing Payment, 67=Inventory Transfers, 15=Deliveries, 16=Returns, 14=A/R Credit Memos, 13=A/R Invoices]
  DocSubType nVarChar(2) Document Subtype default=-- [--=, AR=All A/R Documents, AP=All A/P Documents]
  ExportFmt Int(11) Export Format ->OLLF
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  LogInstanc Int(6) Log Instance
  FileNP Text(16) File Name and Path
