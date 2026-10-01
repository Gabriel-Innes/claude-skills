<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# LLR1 - Electronic Report Generation Result - Reports
Module: Reports | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ReportNum, ResEntry
Fields (name type(len) description [values] ->parent table):
  ResEntry Int(11) Result Internal ID ->OLLR
  ReportNum Int(11) Report Number
  ReportCode nVarChar(8) Report Code ->RDOC
  Criteria Text(16) Selection Criteria
