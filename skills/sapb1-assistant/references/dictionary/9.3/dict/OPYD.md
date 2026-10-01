<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OPYD - Payment Run
Module: Banking | 8 columns | ObjType: 155
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(20) Payment Run Code
  Name nVarChar(50) Payment Run Name
  TolerDays Int(6) Tolerance Days
  MinCashDis Num(19,6) Min. Cash Discount
  UseMinPay VarChar(1) Use Minimum Payment default=N [Y=Yes, N=No]
  MinPayAR Num(19,6) Minimum Incoming Payment
  MinPayAP Num(19,6) Minimum Outgoing Payment
  ArePayMeth VarChar(1) Payment Terms default=N [Y=Yes, N=No]
