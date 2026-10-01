<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ACP3 - Campaign - Partners
Module: Business Partners | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogIns, CpnLineNum, CpnNo
Fields (name type(len) description [values] ->parent table):
  CpnNo Int(11) Campaign No. ->OCPN
  CpnLineNum Int(11) Campaign Line Number
  ParterId Int(11) Partners ->OPRT
  OrlCode Int(11) Relationship Code ->OORL
  RelatCard nVarChar(15) Related BP ->OCRD
  Memo nVarChar(50) Details
  LogIns Int(11) Log Instance - History
  VisOrder Int(11) Visual Order
