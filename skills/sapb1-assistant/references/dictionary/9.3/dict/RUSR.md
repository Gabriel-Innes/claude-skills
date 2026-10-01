<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RUSR - Resource Users
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: UserSign
  I_USER U: IUserCode
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  IUserCode nVarChar(15) I User Code
  Name nVarChar(30) User Name
  UserGroup Int(11) Authorization Group
  Password nVarChar(20) Password
  UserSign Int(11) User Signature
