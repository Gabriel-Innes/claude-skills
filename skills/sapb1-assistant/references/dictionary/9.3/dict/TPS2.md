<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# TPS2 - Tax Parameter - Return Values
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: TprId, TpsId
  ORDER U: DispOrder, TpsId
Fields (name type(len) description [values] ->parent table):
  TpsId Int(11) Tax Parameter Set ->OTPS
  DispOrder Int(11) Display Order
  TprId Int(11) ID of Return Values Mapping ->OTPR
