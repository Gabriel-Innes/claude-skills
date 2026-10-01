<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# TCN1 - Tracking Note - Line Data
Module: General | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Abs. Entry ->OTCN
  LineNum Int(11) Row Number
  ItemCCDNum nVarChar(20) Item CCD Number
  ItemCode nVarChar(50) Item Code ->OITM
  Quantity Num(19,6) Quantity
  CntrOrigin nVarChar(3) Country of Origin
  AccQtyAP Num(19,6) Accumulated A/P Quantity
  AccQtyAR Num(19,6) Accumulated A/R Quantity
  AccRelQty Num(19,6) Accumulated Relocated Quantity
  CstGrpCode Int(6) Customs Group ->OARG
