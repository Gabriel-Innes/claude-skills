<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CSV8 - A/R Correction Invoice Reversal - Items in Package
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: NumPerMsr, UomEntry, ItemCode, PackageNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSV
  PackageNum Int(11) Package Number
  ItemCode nVarChar(50) Item Number ->OITM
  Quantity Num(19,6) Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=166 ->ADP1
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value default=0
