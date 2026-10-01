<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# DAR1 - Data Archive - Transaction Log
Module: Administration | 25 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Line_ID, ArcEntry
Fields (name type(len) description [values] ->parent table):
  ArcEntry Int(11) Data Archive Entry
  Line_ID Int(11) Row Number
  DocType nVarChar(20) Document Type
  DocNum Int(11) Document Number
  DocAbs Int(11) Document Internal ID
  Total Num(19,6) Total
  RefDate Date(8) Posting Date
  ClusterId Int(11) Cluster ID
  Remarks nVarChar(100) Remarks
  KeySeg1 nVarChar(15) Key Segment 1
  KeySeg2 nVarChar(15) Key Segment 2
  KeySeg3 nVarChar(15) Key Segment 3
  KeySeg4 nVarChar(15) Key Segment 4
  KeySeg5 nVarChar(15) Key Segment 5
  KeySeg6 nVarChar(15) Key Segment 6
  KeySeg7 nVarChar(20) Key Segment 7
  KeySeg8 nVarChar(15) Key Segment 8
  KeySeg9 nVarChar(15) Key Segment 9
  KeySeg10 nVarChar(15) Key Segment 10
  Series Int(11) Series
  DocSubType nVarChar(2) Document Sub-Type default=--
  PIndicator nVarChar(10) Period Indicator
  Instance Int(6) Instance default=0
  Segment Int(6) Segment default=0
  CardCode nVarChar(15) Card Code ->OCRD
