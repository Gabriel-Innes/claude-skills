<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ITM6 - Asset Item Distribution Rules
Module: Inventory and Production | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineNum, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  LineNum Int(11) Line Number
  ValidFrom Date(8) Valid From
  ValidTo Date(8) Valid To
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Costing Code 2 ->OOCR
  OcrCode3 nVarChar(8) Costing Code 3 ->OOCR
  OcrCode4 nVarChar(8) Costing Code 4 ->OOCR
  OcrCode5 nVarChar(8) Costing Code 5 ->OOCR
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object default=4 ->ADP1
