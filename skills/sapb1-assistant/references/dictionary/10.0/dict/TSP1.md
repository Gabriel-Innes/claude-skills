<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# TSP1 - Transporter - Transportations
Module: Inventory and Production | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Transporter Abs. Entry
  LineNum Int(11) Line Number
  TransMode Int(11) Mode ->OETM
  VehicleTyp nVarChar(2) Vehicle Type ->OEVT
  VehicleNo nVarChar(15) Vehicle Number
  LogInstanc Int(11) Log Instance default=0
