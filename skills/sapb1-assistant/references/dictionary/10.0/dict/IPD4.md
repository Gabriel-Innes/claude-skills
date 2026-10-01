<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# IPD4 - Inventory Posting Draft - Tracking Note Assignment
Module: Inventory and Production | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIPD
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  ItemCCDNum nVarChar(20) Item CCD Number
  CntrOrigin nVarChar(3) Country/Region of Origin
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=10000071
  SubLineNum Int(11) BOM Line No.
