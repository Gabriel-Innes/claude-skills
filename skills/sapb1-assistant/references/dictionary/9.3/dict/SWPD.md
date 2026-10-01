<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SWPD - SWPD
Module: General | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ProcDefID
Fields (name type(len) description [values] ->parent table):
  ProcDefID Identity(11) WF process definition ID
  DeploymtID Int(11) Deployment ID ->SWDP
  ResourceID Int(11) Resource ID ->SWRS
  Key nVarChar(254) WF process definition key
  Name nVarChar(254) WF process definition name
  Desc Text(16) WF process definition
  Category nVarChar(50) WF category uri
  Version nVarChar(13) WF process definition version
  ProcType nVarChar(20) Process definition type
  Status VarChar(1) Status during import default=M [M=Importing, P=Imported, F=Import failed, I=Inactive, A=Active, E=Activate failed, D=Deleted]
  StartType VarChar(1) Start Type default=M [M=Manual Start, T=Timer Start, C=Conditional Start]
