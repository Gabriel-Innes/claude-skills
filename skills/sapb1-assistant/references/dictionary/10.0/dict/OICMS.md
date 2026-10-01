<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OICMS - Unencumbered ICMS Exemption Reason
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
Fields (name type(len) description [values] ->parent table):
  ID Int(11) ICMS Internal Key
  CstSuffix nVarChar(2) CST Suffix for ICMS
  MotDes Int(11) motDesICMS default=0
  Descrip Text(16) Description
