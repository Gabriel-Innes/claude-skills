<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# IMT11 - Calculated expression's constituent with sign for specifying account in specific template
Module: Inventory and Production | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: PoSt_ID, AccountId, TemplateId
Fields (name type(len) description [values] ->parent table):
  TemplateId Int(6) Template ID default=-1 ->IMT1
  AccountId Int(6) Account ID default=-1 ->IMT1
  Sign VarChar(1) Sing of the constituent default=A [A=Add, S=Sub]
  PoSt_ID Int(6) Id into Post Structure default=-1
