<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OSRC - Service App Report Configuration
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Code
  SysRptName nVarChar(120) System Report Name
  SysRptTemp Text(16) System Report Template
  CusRptName nVarChar(120) Customized Report Name
  CusRptTemp Text(16) Customized Report Template
  RptChoice VarChar(1) Report Choice [S=System, C=Customized]
