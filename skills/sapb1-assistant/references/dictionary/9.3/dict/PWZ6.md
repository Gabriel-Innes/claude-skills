<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# PWZ6 - Payment Wizard Rows - 6
Module: Banking | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CondNum, IdEntry
Fields (name type(len) description [values] ->parent table):
  IdEntry Int(11) ID Number ->OPWZ
  CondNum Int(11) Condition Number
  SelFldID nVarChar(100) Selection Field ID
  FromString nVarChar(200) From String Value
  FromNumber Int(11) From Number Value
  FromMoney Num(19,6) From Amount Value
  FromDate Date(8) From Date Value
  FromMemo Text(16) From Memo Value
  ToString nVarChar(200) To String Value
  ToNumber Int(11) To Number Value
  ToMoney Num(19,6) To Amount Value
  ToDate Date(8) To Date Value
  ToMemo Text(16) To Memo Value
