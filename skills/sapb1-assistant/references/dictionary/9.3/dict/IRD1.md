<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# IRD1 - Report Definition - Rows
Module: Reports | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Type, ReportId
Fields (name type(len) description [values] ->parent table):
  ReportId nVarChar(254) Report Id ->OIRD
  Type Int(11) Type default=1 [1=XLSX]
  Template Text(16) Template
  CreateBy nVarChar(25) Created By
  CreateDate Date(8) Creation Timestamp
  ModifyBy nVarChar(25) Modified By
  ModifyDate Date(8) Modification Timestamp
