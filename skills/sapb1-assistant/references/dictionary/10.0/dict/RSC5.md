<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# RSC5 - Resources - Preferred Vendors
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ResCode, VendorCode
Fields (name type(len) description [values] ->parent table):
  ResCode nVarChar(50) Internal Resource ID ->ORSC
  VendorCode nVarChar(15) Vendor Code ->OCRD
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object default=290 ->ADP1
