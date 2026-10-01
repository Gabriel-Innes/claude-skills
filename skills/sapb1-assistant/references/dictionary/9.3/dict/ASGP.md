<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ASGP - Service Group for Brazil
Module: Service | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, AbsEntry
  CODE U: LogInstanc, ServiceGrp
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Service Group ID
  ServiceGrp nVarChar(3) Service Group
  Descrip nVarChar(70) Description
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
