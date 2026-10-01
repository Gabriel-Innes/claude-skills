<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCFW - Cash Flow Line Item
Module: Finance | 14 columns | ObjType: 242
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CFWId
  INTER_KEY: FatherNum
  INDEX_KEY U: CFWName
Fields (name type(len) description [values] ->parent table):
  CFWId Int(11) Cash Flow Line Item ID
  CFWName nVarChar(100) Cash Flow Line Item Name
  LineNum nVarChar(5) Cash Flow Line No.
  Postable VarChar(1) Cash Flow Item [Active/Title] default=Y [Y=Active Item, N=Header Item]
  FatherNum Int(11) Parent Item Key ->OCFW
  Levels Int(6) Cash Flow Item Level default=3
  GroupMask Int(6) Group Mask default=1
  GroupLine Int(11) Serial No. in Group
  ExtrMatch Int(11) External Reconciliation No.
  IntrMatch Int(11) Internal Reconciliation No.
  RateDifCFW Int(11) Rate Differences CFW
  DataSource Int(6) Data Source
  Attr Int(6) Attribute
  Direction Int(6) Direction
