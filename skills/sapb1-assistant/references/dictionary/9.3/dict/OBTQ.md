<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OBTQ - Batch No. Quantities
Module: Inventory and Production | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SYSTEM_KEY U: WhsCode, SysNumber, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item Code ->OITM
  SysNumber Int(11) System Number ->OBTN
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  CommitQty Num(19,6) Committed Quantity
  CountQty Num(19,6) Counted Quantity
  AbsEntry Int(11) abs entry
  MdAbsEntry Int(11) MD Abs Entry ->OBTN
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line ->TCN1
  CCDQuant Num(19,6) CCD Quantity
