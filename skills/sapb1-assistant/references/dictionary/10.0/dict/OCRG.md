<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OCRG - Card Groups
Module: Business Partners | 9 columns | ObjType: 10
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: GroupCode
  GROUP_TYPE: GroupType
  GROUP_NAME U: GroupName
Fields (name type(len) description [values] ->parent table):
  GroupCode Int(6) Group No.
  GroupName nVarChar(100) Group Name
  GroupType VarChar(1) Group Type default=C [C=Customer Group, S=Vendor Group]
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  PriceList Int(6) Price List ->OPLN
  DiscRel VarChar(1) Effective Discount Groups default=L [L=Lowest Discount, H=Highest Discount, A=Average, S=Total, M=Discount Multiples]
  EffecPrice VarChar(1) Effective Price default=D [D=Default Priority, L=Lowest Price, H=Highest Price]
