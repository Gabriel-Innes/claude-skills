<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# RDC1 - Multilingual Report
Module: Reports | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocCode, LineNum
  UniqueIdx U: DocCode, LangCode
Fields (name type(len) description [values] ->parent table):
  DocCode nVarChar(8) Doc. Code ->RDOC
  LineNum Int(11) Line Number
  DocName nVarChar(64) Doc. Name
  LangCode Int(11) Language Code
  Template Text(16) Report Template Data
  CreateDate Date(8) Create Date
  CreateTime Int(11) Create Time
  UpdateDate Date(8) Update Date
  UpdateTime Int(11) Update Time
