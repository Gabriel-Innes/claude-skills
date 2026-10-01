<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OSCN - Customer/Vendor Cat. No.
Module: Business Partners | 8 columns | ObjType: 73
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Substitute, CardCode, ItemCode
  CARD_SCN: Substitute, CardCode
  CARD: ItemCode, CardCode
  ITEM: CardCode, ItemCode
  SUBSTITUTE: Substitute
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  CardCode nVarChar(15) BP Code ->OCRD
  Substitute nVarChar(50) BP Catalog Number
  Transfered VarChar(1) Postponed to Next Year default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  ShowSCN VarChar(1) Display BP Catalog Number default=N [Y=Yes, N=No]
