<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CUPC - Upgrade Control
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjectId
Fields (name type(len) description [values] ->parent table):
  ObjectId nVarChar(20) Object ID
  CntBefore Int(11) Before
  CntAfter Int(11) After
  Reported VarChar(1) Reported default=O [C=Reported, O=Open]
