<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SWDP - SWDP
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DeploymtID
Fields (name type(len) description [values] ->parent table):
  DeploymtID Identity(11) Workflow Deployment ID
  Name nVarChar(254) Deployment Name
  DeploymtDt Date(8) Deployment Date
