<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# TRS2 - Tax Rpt Sav Obj Man Chgd Vals
Module: Reports | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineID, AbsEntry
  SECONDARY U: ParamCode, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ObjType nVarChar(20) Object Type
  LineID Int(11) Internal Row Number
  ParamCode nVarChar(32) Parameter Code
  PrmValAmt Num(19,6) Parameter Value Amount
  PrmValNum Int(11) Parameter Value Number
  PrmValStr nVarChar(8) Parameter Value String
  PrmValTxt Text(16) Parameter Value Text
