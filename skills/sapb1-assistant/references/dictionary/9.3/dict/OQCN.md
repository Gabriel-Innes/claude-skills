<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OQCN - Query Catagories
Module: Reports | 5 columns | ObjType: 134
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CategoryId
  CAT_NAME_K: CatName
Fields (name type(len) description [values] ->parent table):
  CategoryId Int(11) Category ID
  CatName nVarChar(50) Category Name
  PermMask nVarChar(20) Permissions default=NNNNNNNNNNNNNNN
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
