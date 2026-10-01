<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OBCD - Bar Code Master Data
Module: Inventory and Production | 11 columns | ObjType: 1470000062
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: BcdEntry
  ITEM U: BcdCode, UomEntry, ItemCode
  BCD_CODE: BcdCode
Fields (name type(len) description [values] ->parent table):
  BcdEntry Int(11) Bar Code Abs. Entry
  BcdCode nVarChar(254) Bar Code - Code
  BcdName nVarChar(100) Bar Code Name
  ItemCode nVarChar(50) Item No. ->OITM
  UomEntry Int(11) UoM Abs. Entry ->OUOM
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
