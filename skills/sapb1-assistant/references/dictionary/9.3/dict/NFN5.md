<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# NFN5 - NF Skipped Numbers
Module: General | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: VisOrder, SeqCode
Fields (name type(len) description [values] ->parent table):
  SeqCode Int(6) Sequence Code
  NFeNoFrom Int(11) NF-e No. From default=0
  NFeNoTo Int(11) NF-e No. To default=0
  Year Int(6) Year
  Reason nVarChar(254) Reason for Number Skipping
  Reply nVarChar(50) Reply from the Authority
  Status VarChar(1) Status default=N [N=New, S=Sent, A=Approved, E=Error]
  VisOrder Int(6) Visual Order
  CreateDate Date(8) Creation Date
  CreateTime Int(11) Creation Time
  UpdateDate Date(8) Update Date
  UpdateTime Int(11) Update Time
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
