<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# IGE24 - Goods Issue - Tracking Note Assignment
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ChildNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  ItemCCDNum nVarChar(40) Item CCD Number
  CntrOrigin nVarChar(3) Country of Origin
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=60 ->ADP1
  SubLineNum Int(11) BOM Line No.
