<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# TPW6 - Journal Entry Information
Module: Banking | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, JeId, JeLineId
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OTPW
  JeId Int(11) JE Number ->OJDT
  JeLineId Int(11) Line Number of JE
