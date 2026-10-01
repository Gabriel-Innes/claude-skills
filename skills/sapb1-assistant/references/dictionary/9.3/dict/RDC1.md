<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RDC1 - Multilingual Report
Module: Reports | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocCode
  UniqueIdx U: LangCode, DocCode
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
