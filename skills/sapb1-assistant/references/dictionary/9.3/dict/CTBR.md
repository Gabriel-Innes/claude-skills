<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CTBR - Toolbars
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ToolbarId, UserSign
Fields (name type(len) description [values] ->parent table):
  UserSign Int(6) ->OUSR
  ToolbarId Int(11)
  Docking Int(6)
  LeftID Int(6)
  TopID Int(6)
  RightID Int(6)
  BottomID Int(6)
  VisibleID VarChar(1) default=N [Y=, N=]
