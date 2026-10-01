<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# NNM4 - Electronic Series
Module: Administration | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: InitialNum, ESeries
Fields (name type(len) description [values] ->parent table):
  ESeries Int(6) Electronic Series default=0
  Series Int(11) Series
  SeriesName nVarChar(8) Series Name
  InitialNum nVarChar(20) Initial Number default=0
  NextNumber nVarChar(20) Next Number for Use default=0
  LastNum nVarChar(20) Last Number Allowed
  Prefix nVarChar(10) Prefix
  ApprovYear Int(11) Approval Year
  ApprovNum Int(11) Approval Number
  Remark nVarChar(50) Remarks
