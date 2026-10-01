<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SFC25 - Self Credit Memo - Amt Per VAT Grp
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, VatGroup, Type
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODOC
  VatGroup nVarChar(8) Tax Definition ->OVTG
  VatPrcnt Num(19,6) Tax Rate
  BaseAmnt Num(19,6) Base Amount
  BaseAmntFC Num(19,6) Base Amount (FC)
  BaseAmntSC Num(19,6) Base Amount (SC)
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  Type Int(11) Type default=1 [1=Discount by Tax]
  Currency nVarChar(3) Price Currency
  Rate Num(19,6) Currency Rate
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=254000066 ->ADP1
