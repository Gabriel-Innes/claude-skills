<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ACP3 - Campaign - Partners
Module: Business Partners | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CpnNo, CpnLineNum, LogIns
Fields (name type(len) description [values] ->parent table):
  CpnNo Int(11) Campaign No. ->OCPN
  CpnLineNum Int(11) Campaign Line Number
  ParterId Int(11) Partners ->OPRT
  OrlCode Int(11) Relationship Code ->OORL
  RelatCard nVarChar(15) Related BP ->OCRD
  Memo nVarChar(50) Details
  LogIns Int(11) Log Instance - History
  VisOrder Int(11) Visual Order
