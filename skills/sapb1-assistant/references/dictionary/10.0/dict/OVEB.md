<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OVEB - VAT Exemptions for Business Partners
Module: Finance | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  BP_CODE U: CardCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  CardCode nVarChar(15) Customer/Vendor Code ->OCRD
  VersionNum nVarChar(13) Version Number
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Date of Update
  LogInstanc Int(11) Log Instance default=0
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UpdateTS Int(11) Update Full Time
  Comments nVarChar(254) Remarks
