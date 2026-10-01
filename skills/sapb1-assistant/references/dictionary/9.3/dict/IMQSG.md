<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# IMQSG - Question Suggestions
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id Identity(11) Internal Number
  Content nVarChar(254) Suggestion Content
  Weight Int(11) Suggestion Weight
  Time Date(8) Time
  Owner nVarChar(25) Owner of Suggestion
  Language Int(11) Language of Suggestion default=3
