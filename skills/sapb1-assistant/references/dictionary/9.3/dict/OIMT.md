<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OIMT - Templates for Inventory JE
Module: Inventory and Production | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TemplateId
  SECONDARY U: TmpType, Action, LocalizId, ValuatType, BaseType, TransType
Fields (name type(len) description [values] ->parent table):
  ValuatType VarChar(1) Document Valuation Type default=N [A=, F=, S=, N=unDefined]
  TransType Int(11) Transaction type default=-1
  BaseType Int(6) Base Transaction Type default=-1
  TemplateId Int(6) Template ID default=-1
  LocalizId nVarChar(2) Localization Identifier default=XX [XX=All Localizations]
  Action Int(6) Action Type default=0
  JEPosting VarChar(1) Posting Status default=N [N=None, C=Complete, P=Partial]
  LineActTyp Int(6) Line Account Type default=2 [2=LINE_ACCT_TYPE]
  TmpType Int(6) Template Type default=0
  Total VarChar(1) Total Type default=M [M=Total from Message, C=Total from Calculator, F=Total from Formula]
