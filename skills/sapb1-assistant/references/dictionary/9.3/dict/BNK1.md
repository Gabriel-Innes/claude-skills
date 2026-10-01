<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# BNK1 - Bank Statement - Documents List
Module: Banking | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ListLineID, BSLine, IdNumber
Fields (name type(len) description [values] ->parent table):
  IdNumber Int(11) Bank Statement ID
  BSLine Int(11) Bank Statement Line ID
  ListLineID Int(6) List Line ID
  DocID nVarChar(27) Document Identifier
  AmntLC Num(19,6) Amount (LC)
  AmnFC Num(19,6) Amount (FC)
  IsDebit VarChar(1) Debit [Yes/No] default=Y [Y=Yes, N=No]
