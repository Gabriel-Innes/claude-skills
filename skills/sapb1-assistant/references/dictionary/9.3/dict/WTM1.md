<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# WTM1 - Approval Templates - Producers
Module: Administration | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: UserID, WtmCode
Fields (name type(len) description [values] ->parent table):
  WtmCode Int(11) Code ->OWTM
  UserID Int(11) User Code default=-1 ->OUSR
