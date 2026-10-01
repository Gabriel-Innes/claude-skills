<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OSCN - Customer/Vendor Cat. No.
Module: Business Partners | 11 columns | ObjType: 73
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ItemCode, CardCode, Substitute
  CARD_SCN: CardCode, Substitute
  CARD: CardCode, ItemCode
  ITEM: ItemCode, CardCode
  SUBSTITUTE: Substitute
  DEFAULT: CardCode, ItemCode, IsDefault
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  CardCode nVarChar(15) BP Code ->OCRD
  Substitute nVarChar(50) BP Catalog Number
  Transfered VarChar(1) Postponed to Next Year default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  ShowSCN VarChar(1) Display BP Catalog Number default=N [Y=Yes, N=No]
  IsDefault VarChar(1) Is Default BP Catalog default=N [Y=Yes, N=No]
  Descriptio nVarChar(200) BP Catalog Description
  DataVers Int(11) Data Version default=1
