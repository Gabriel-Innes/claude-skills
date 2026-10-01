<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# FNS1 - Folio Numbering - Voided Series
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: FolNumFrom, Series
  To U: FolNumTo, Series
Fields (name type(len) description [values] ->parent table):
  Series Int(11) Series ID ->OFNS
  FolNumFrom Int(11) Folio Number From
  FolNumTo Int(11) Folio Number To
  Reason nVarChar(100) Reason For Number Skipping
