<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ATS1 - Transporter - Transportations
Module: Inventory and Production | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, LineNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Transporter Abs. Entry
  LineNum Int(11) Line Number
  TransMode Int(11) Mode ->OETM
  VehicleTyp nVarChar(2) Vehicle Type ->OEVT
  VehicleNo nVarChar(15) Vehicle Number
  LogInstanc Int(11) Log Instance default=0
