<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# TPS2 - Tax Parameter - Return Values
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TpsId, TprId
  ORDER U: TpsId, DispOrder
Fields (name type(len) description [values] ->parent table):
  TpsId Int(11) Tax Parameter Set ->OTPS
  DispOrder Int(11) Display Order
  TprId Int(11) ID of Return Values Mapping ->OTPR
