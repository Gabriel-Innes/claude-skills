<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# DGP5 - Sort By List
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, CondNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->ODGP
  CondNum Int(11) Condition Number
  SortField nVarChar(100) Sort Field default=DocNum [-1=, DocNum=Document Number, DocDate=Posting Date, DocDueDate=Due Date, NumAtCard=BP Reference No., DocTotal=Document Amount, SlpCode=Sales Employee]
  SortOrder VarChar(1) Sort Order default=A [A=Ascending, D=Descending]
