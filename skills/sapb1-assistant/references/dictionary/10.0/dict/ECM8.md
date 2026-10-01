<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ECM8 - Electronic Document Import Files
Module: Reports | 24 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  ACTION U: Code, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal ID
  Code nVarChar(8) Code
  ParentID Int(11) Parent ID
  ActType VarChar(1) Action Type [S=Setup, R=Report, D=A/R Document, P=A/P Document, F=A/R Draft Document, E=A/P Draft Document, O=Other, K=Skip, C=Contingency, B=BP Check, I=Incoming Payment, U=Outgoing Payment, A=Internal Reconciliation, T=Transportation Document, W=Inventory Transfer, V=VAT Obligations, N=VAT Declarations, L=VAT Liabilities, Y=VAT Payments, d=Delivery, r=Return, i=A/R Invoice, c=A/R Credit Memo, g=Goods Receipt PO, s=Goods Return, p=A/P Invoice, m=A/P Credit Memo, H=Draft Incoming Payment, J=Draft Outgoing Payment, Q=Journal Entry]
  ActDesc nVarChar(100) Action Description
  ActStatus VarChar(1) Action Status default=N [N=New, P=Pending, E=Error, T=Temporary Error, O=OK, S=Sent, R=Document Error, W=Waiting, A=Authorized, I=In Process, J=Rejected, D=Denied, C=Canceled, B=Aborted, Q=Queued, M=Imported, G=Warning, V=Approved, F=Approving, H=Rejecting, K=Generated, Y=Ready to Process, L=Determined]
  ActMessage nVarChar(254) Action Message
  TestMode VarChar(1) Test Mode default=N [N=No, Y=Yes]
  GUID nVarChar(100) GUID
  Authority nVarChar(16) Authorities Code
  ProcSource nVarChar(20) Processing Source
  MetaData Text(16) Metadata
  MIMEType nVarChar(128) MIME Type
  FileName Text(16) File Name
  CardCode nVarChar(15) BP Code
  DocDate Date(8) Document Date
  ObjType nVarChar(20) Object Type
  CreateDate Date(8) Creation Date
  CreateTS Int(11) Creation Time - Incl. Secs.
  UpdateDate Date(8) Update Date
  UpdateTS Int(11) Update Time - Incl. Secs
  UserSign Int(6) User Signature
  UserSign2 Int(6) Updating User
  AssignedID nVarChar(50) Assigned ID
