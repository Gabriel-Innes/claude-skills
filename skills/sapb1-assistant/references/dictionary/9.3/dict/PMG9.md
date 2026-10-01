<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# PMG9 - Project Management - Charged Document Lines Log - Used by Billing Wizard
Module: General | 19 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineID, TargetAbs, TargetType, BWRefID, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  LineID Int(11) Row No.
  BWRefID Int(11) Billing Wizard Reference ID
  TargetType Int(11) Target Document Type default=-1 [-1=, 15=Delivery, 13=A/R Invoice]
  TargetAbs Int(11) Target Document Abs. Entry
  TargetNum Int(11) Target Document Number
  TargetLine Int(11) Target Document Line Number
  SubProjID Int(11) Subproject ID default=-1
  StageID Int(11) Stage ID
  SourceType Int(11) Source Document Type default=-1 [-1=, 18=A/P Invoice, 23=Sales Quotation, 17=Sales Order, 13002=A/R Reserve Invoice, 15=Delivery, 33=Activity, 202=Work Order, 234000024=Timesheet]
  SourceAbs Int(11) Source Document Abs. Entry
  SourceNum Int(11) Source Document Number
  SourceLine Int(11) Source Document Line Number
  Charged Num(19,6) Charged
  ChargedQty Num(19,6) Charged Quantity
  DestType Int(11) Destination Table Type default=-1 [-1=, 234000021=Project Management Document, 234000022=Project Management Subproject, 234000024=Time Sheet Document]
  DestArr Int(11) Destination Table Array default=-1 [-1=, 1=Time Sheet Lines, 4=Stage Documents, 6=Stage Activities, 7=Stage Workorders]
  DestAbs Int(11) Destination Table Abs. Entry
  DestLine Int(11) Destination Table Line Number
