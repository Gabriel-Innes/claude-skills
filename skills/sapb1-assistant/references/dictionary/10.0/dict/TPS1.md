<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# TPS1 - Tax Parameter Attributes
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TpsId, TpaId
  ORDER U: TpsId, DispOrder
Fields (name type(len) description [values] ->parent table):
  TpsId Int(11) Tax Parameter Set ->OTPS
  DispOrder Int(11) Display Order
  TpaId Int(11) ID of Attributes Mapping ->OTPA
  Mandatory VarChar(1) Mandatory to Input default=N [Y=Yes, N=No]
