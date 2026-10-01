<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# BTA1 - Brazil - Tax Adjustment - Tax Types
Module: Reports | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: StaType, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OBTA
  StaType Int(11) Tax Authority Type ->OSTT
