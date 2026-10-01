<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCCS - Cycle Count Determination
Module: Inventory and Production | 3 columns | ObjType: 1470000092
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: WhsCode
Fields (name type(len) description [values] ->parent table):
  WhsCode nVarChar(8) Warehouse Code
  CycleType VarChar(1) Cycle Type default=G [G=Item Group, S=Sublevel]
  CycleBy Int(6) Cycle By default=0 [0=Item Group, 1=Warehouse Sublevel 1, 2=Warehouse Sublevel 2, 3=Warehouse Sublevel 3, 4=Warehouse Sublevel 4]
