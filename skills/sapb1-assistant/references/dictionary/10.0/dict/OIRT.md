<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OIRT - Interest Prices
Module: Inventory and Production | 5 columns | ObjType: 92
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Numerator
Fields (name type(len) description [values] ->parent table):
  Numerator Int(11) Internal Number
  EffectDate Date(8) Expiration Date
  AnlIntrst Num(19,6) Annual Interest Rate
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
