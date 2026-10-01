<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AST1 - Sales Tax Codes - Rows
Module: Administration | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: STCCode, Line_ID, LogInstanc
Fields (name type(len) description [values] ->parent table):
  STCCode nVarChar(8) STC Code ->OSTC
  Line_ID Int(11) Row Number default=0
  STACode nVarChar(8) STA Code ->OSTA
  STAType Int(11) STA Type ->OSTA
  TaxOnTCode nVarChar(8) STA Tax on Tax Code ->OSTA
  TaxOnTType Int(11) STA Tax On Tax Type ->OSTA
  EfctivRate Num(19,6) Effective Rate
  FmlId Int(11) Tax Formula ID ->OFML
  CstCodeIn nVarChar(20) CST Code Incoming
  CstSuffix nVarChar(2) CST Suffix for ICMS
  LogInstanc Int(11) Log Instance default=0
