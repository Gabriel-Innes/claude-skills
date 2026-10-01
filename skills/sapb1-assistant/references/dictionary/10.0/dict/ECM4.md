<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ECM4 - Import Mapping Determination
Module: Reports | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  DOC_IMPORT U: Code, ObjType, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal ID
  Code nVarChar(8) Code ->OECM
  LineNum Int(11) Row Number
  ObjType nVarChar(20) Object Type default=-1 [18=A/P Invoice, 19=A/P Credit Memo, 204=A/P Down Payment, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 20=Goods Receipt PO, 21=Goods Return, 24=Incoming Payment, 46=Outgoing Payment]
  ObjXPath nVarChar(254) Object Type XPath
  FieldType VarChar(1) Field Type default=T [T=Federal Tax ID, A=Additional ID, U=Unified Federal Tax ID, C=CNPJ, L=Alias Name, I=IBAN, N=BP Name]
  FieldXPath nVarChar(254) Field XPath
  ImportFmt Int(11) Import Format ->OLLF
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  LogInstanc Int(6) Log Instance
  DflDSerie Int(11) Default Digital Series default=-1 ->NNM1
