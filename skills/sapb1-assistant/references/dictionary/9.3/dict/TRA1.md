<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# TRA1 - Transition - Rows
Module: Marketing Documents | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Entry ->OINV
  LineNum Int(11) Row Number
  BaseEntry Int(11) Base Document Internal ID
  PackQty Num(19,6) Packing Quantity
  PurPackMsr nVarChar(8) Packaging UoM Name default=Pack
  ArsnalName nVarChar(20) Storage Group Name
  ArsnalCode nVarChar(20) Storage Group Code
  UnitMsr nVarChar(5) Ref. UoM (Type) default=Unit
  Quantity Num(19,6) Quantity
  Fraction Num(19,6) Remainder
  Weight1 Num(19,6) Weight
  LineTotal Num(19,6) Row Total
  ItemCode nVarChar(50) Item No. ->OITM
