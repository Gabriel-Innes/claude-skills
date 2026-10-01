<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# BOC1 - External Bank Operation Code - Rows
Module: Banking | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ExOpCode, AbsEntry
  BY_LINE U: LineId, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OBOC
  ExOpCode nVarChar(40) External Bank Operation Code
  OPDscrpt nVarChar(40) Operation Description
  InOpCode Int(11) Internal Bank Operation Code ->OBTC
  LogInstanc Int(11) Log Instance default=0
  LineId Int(6) Row
