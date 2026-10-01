<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AVM1 - Systems for Value Mapping Properties
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: PropID, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  PropID Int(11) Property ID
  PropDesc nVarChar(50) Property Description
  PropType VarChar(1) Property Type default=S [S=String, N=Numeric, D=Date]
  PropValue nVarChar(254) Property Value
