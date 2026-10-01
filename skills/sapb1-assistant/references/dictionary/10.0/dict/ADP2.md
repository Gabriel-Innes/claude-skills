<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ADP2 - Report Settings - History
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PrintId, RptType
  OBJECT U: RptType
Fields (name type(len) description [values] ->parent table):
  PrintId nVarChar(4) Print No. ->OADP
  RptType nVarChar(20) Report Type [1=Aging Report, 2=Dunning Wizard]
  EmailSbj nVarChar(254) E-Mail Subject
  EmailBody Text(16) E-Mail Body
