<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# LTF1 - Legal Text Format Lines
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Format ID ->OLTF
  LineNum Int(11) Line No.
  LineCode nVarChar(30) Format Code ->OLTI
