<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ASVM - Systems for Value Mapping
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  SysType VarChar(1) System Type default=C [C=Concur]
  SysDsc nVarChar(50) System Description
