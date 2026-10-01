<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OSLD - Schedule Row Detail
Module: General | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SCHD_LINE U: ObjType, DocEntry, DocLineNum, SchdLine
  DOCLINESLD: ObjType, DocEntry, DocLineNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ObjType nVarChar(20) Object Type default=-1 [-1=, 13=A/R Reserve Invoice, 17=Sales Order, 18=A/P Reserve Invoice, 22=Purchase Order, 163=A/P Correction Reserve Invoice, 165=A/R Correction Reserve Invoice, 202=Production Order, 1250000001=Warehouse Transfer Request]
  DocEntry Int(11) Associated Doc Entry
  DocLineNum Int(11) Associated Doc Row No.
  SchdLine Int(11) Schedule Row No.
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  CfmDate Date(8) Confirmation Date
  CfmQty Num(19,6) Confirmation Quantity
  FixedCfm VarChar(1) Fixed Confirmation Data default=N [Y=Yes, N=No]
  ReqQty Num(19,6) Required Quantity
