<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCRW - BP for IIS Annual
Module: Business Partners | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  BP_YEAR U: Year, CardCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  CardCode nVarChar(15) BP Code
  Year Int(6) Report Year
  SentMeth VarChar(1) Method of Sending [D=Doc. Date, T=Tax Date]
  SentValue Num(19,6) Sent Value
  LastAMeth VarChar(1) Last Accepted Method [D=Doc. Date, T=Tax Date]
  LastAValue Num(19,6) Last Accepted Value
  ReportID nVarChar(50) Report ID
