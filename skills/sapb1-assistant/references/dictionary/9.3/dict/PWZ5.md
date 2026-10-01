<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# PWZ5 - Payment Wizard - Rows 5
Module: Banking | 20 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: InstlmntID, Object, ErrorLine, InvID, IdEntry
Fields (name type(len) description [values] ->parent table):
  IdEntry Int(11) ID Entry ->OPWZ
  InvID Int(11) Inv ID
  Amount Num(19,6) Invoice Amount
  CardCode nVarChar(15) Card Code ->OCRD
  CardName nVarChar(100) Card Name
  PostDate Date(8) Posting Date
  ErrDisc nVarChar(254) Error Discription
  ErrorLine Int(11) ErrorLine
  WriteErr VarChar(1) WriteErr default=Y
  Object nVarChar(20) Object Type default=0
  InstlmntID Int(6) Installment ID default=1
  invNum Int(11) Invoice No.
  Currency nVarChar(3) Currency
  LineType VarChar(1) Line Type default=G
  DueBal Num(19,6) Balance Due
  DueBalFC Num(19,6) Balance Due (FC)
  DueBalSys Num(19,6) Balance Due (SC)
  ValDate Date(8) Due Date
  BPLId Int(11) Branch ->OBPL
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
