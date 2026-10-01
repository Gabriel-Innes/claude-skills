<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# BNK1 - Bank Statement - Documents List
Module: Banking | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: IdNumber, BSLine, ListLineID
Fields (name type(len) description [values] ->parent table):
  IdNumber Int(11) Bank Statement ID
  BSLine Int(11) Bank Statement Line ID
  ListLineID Int(6) List Line ID
  DocID nVarChar(27) Document Identifier
  AmntLC Num(19,6) Amount (LC)
  AmnFC Num(19,6) Amount (FC)
  IsDebit VarChar(1) Debit [Yes/No] default=Y [Y=Yes, N=No]
