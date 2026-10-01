<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# VIEWS - SQL Company Views
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ViewName
Fields (name type(len) description [values] ->parent table):
  ViewName nVarChar(100) View Name
  ViewString Text(16) View String
  ViewType VarChar(1) View Type default=S [S=Static, D=Dynamic]
