<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OTSP - Transporters
Module: Inventory and Production | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  TRANS_CODE U: TransCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Transporter Abs. Entry
  TransCode nVarChar(20) Transporter Code
  TransName nVarChar(25) Transporter Name
  TransID nVarChar(15) Transporter ID
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
  UserSign Int(6) User Signature
  UserSign2 Int(6) Updating User ->OUSR
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
