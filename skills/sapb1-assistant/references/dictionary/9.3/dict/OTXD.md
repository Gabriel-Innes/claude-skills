<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OTXD - Tax Invoice Draft
Module: Marketing Documents | 46 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjType, DocEntry
  NUM U: Series, PIndicator, ObjType, AltRev, DocNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  DocType VarChar(1) Document Type default=I [I=Invoice, P=Payment, J=Journal Entry, C=Correction Invoice, D=Down Payment, A=Alteration Invoice, B=Alteration Correction Invoice]
  CANCELED VarChar(1) Canceled default=N [Y=Yes, N=No]
  HandWriten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  Printed VarChar(1) Printed default=N [Y=Yes, N=No]
  Transfered VarChar(1) Year Transfer default=N [Y=Yes, N=No]
  ObjType nVarChar(20) Object Type default=194 ->ADP1
  DocDate Date(8) Posting Date
  CardCode nVarChar(15) Customer Code ->OCRD
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Date of Update
  DocDueDate Date(8) Due Date
  Series Int(11) Series default=0
  Segment Int(6) Segment default=0
  CntctCode Int(11) Contact Person ->OCPR
  VatDate Date(8) Document Date
  Comments nVarChar(254) Remarks
  TrnspCode Int(6) Shipping Type default=-1 ->OSHP
  ShipToCode nVarChar(50) Ship-to Code
  Address nVarChar(254) Bill to
  Address2 nVarChar(254) Ship To
  LogInstanc Int(11) Log Instance default=0
  CurSource VarChar(1) Base Currency default=C [L=Local Currency, S=System Currency, C=BP Currency]
  DocCur nVarChar(3) Document Currency
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  NumAtCard nVarChar(100) BP Reference No.
  CardName nVarChar(100) Customer/Vendor Name
  CancelDate Date(8) Cancel Date
  DocTotal Num(19,6) Document Total
  VatSum Num(19,6) Total Tax
  PayRefNo nVarChar(16) Payment Ref. No.
  PayRefDate Date(8) Payment Ref. Date
  TaxMethod VarChar(1) Taxation Method default=S [S=On Shipment, P=On Payment]
  AtcEntry Int(11) Attachment Entry
  IsDpm VarChar(1) IS Down Payment default=N [Y=Yes, N=No]
  AltRev Int(11) Alteration Revision default=0
  PIndicator nVarChar(10) Period Indicator ->OPID
  TransId Int(11) Transaction Number ->OJDT
  JrnlMemo nVarChar(50) Journal Remark
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  VATRegNum nVarChar(32) Branch Reg. No.
  GovContrID nVarChar(254) Gov. Contract ID
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
