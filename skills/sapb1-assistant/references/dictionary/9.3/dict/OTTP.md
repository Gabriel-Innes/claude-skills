<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OTTP - ToolTip Preview
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ObjectId, UserSign
Fields (name type(len) description [values] ->parent table):
  UserSign Int(6) User Signature ->OUSR
  ObjectId Int(11) Object ID
  IsEnabled VarChar(1) Enabled default=Y [Y=Yes, N=No]
