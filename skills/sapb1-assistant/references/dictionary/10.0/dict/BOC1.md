<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# BOC1 - External Bank Operation Code - Rows
Module: Banking | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, ExOpCode
  BY_LINE U: AbsEntry, LineId
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OBOC
  ExOpCode nVarChar(40) External Bank Operation Code
  OPDscrpt nVarChar(40) Operation Description
  InOpCode Int(11) Internal Bank Operation Code ->OBTC
  LogInstanc Int(11) Log Instance default=0
  LineId Int(6) Row
