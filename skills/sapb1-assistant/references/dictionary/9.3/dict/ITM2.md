<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ITM2 - Items - Multiple Preferred Vendors
Module: Inventory and Production | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: VendorCode, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  VendorCode nVarChar(15) Vendor Code ->OCRD
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object default=4 ->ADP1
