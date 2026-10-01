<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ITM4 - Package in Items
Module: Inventory and Production | 23 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: PkgCode, UomEntry, UomType, ItemCode
  PKG_CODE: PkgCode
  UOM_ENTRY: UomEntry
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  UomType VarChar(1) UoM Type default=P [P=Purchasing, S=Sales]
  UomEntry Int(11) UoM Entry ->OUOM
  PkgCode Int(11) Package Code ->OPKG
  Height1 Num(19,6) Height 1
  Hght1Unit Int(6) Height 1 UoM
  Height2 Num(19,6) Height 2
  Hght2Unit Int(6) Height 2 UoM
  Width1 Num(19,6) Width 1
  Wdth1Unit Int(6) Width 1 UoM
  Width2 Num(19,6) Width 2
  Wdth2Unit Int(6) Width 2 UoM
  Length1 Num(19,6) Length 1
  Len1Unit Int(6) Length 1 UoM
  Length2 Num(19,6) Length 2
  Len2Unit Int(6) Length 2 UoM
  Volume Num(19,6) Volume
  VolUnit Int(6) Volume UoM
  Weight1 Num(19,6) Weight 1
  Wght1Unit Int(6) Weight 1 UoM
  Weight2 Num(19,6) Weight 2
  Wght2Unit Int(6) Weight 2 UoM
  QtyPerPack Num(19,6) Quantity per Packaging UoM
