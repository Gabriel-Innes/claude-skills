<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AQR4 - Inventory Opening Balance - Tracking Note Assignment - History
Module: Inventory and Production | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, ChildNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  ItemCCDNum nVarChar(20) Item CCD Number
  CntrOrigin nVarChar(3) Country of Origin
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=0
  SubLineNum Int(11) BOM Line No.
