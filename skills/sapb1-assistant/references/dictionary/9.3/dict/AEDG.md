<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AEDG - Discount Groups
Module: Inventory and Production | 14 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Unique Entry
  Type VarChar(1) Type [A=All BPs, C=Customer Group, V=Vendor Group, S=Specific BP]
  ObjType nVarChar(20) Object Type default=-1 [-1=, 10=Card Payment Groups, 2=Cards]
  ObjCode nVarChar(15) Object Code
  DiscRel VarChar(1) Disc. Relations default=L [L=Lowest Discount, H=Highest Discount, A=Average, S=Total, M=Discount Multiples]
  ValidFor VarChar(1) Active default=Y [Y=Yes, N=No]
  ValidForm Date(8) Active From
  ValidTo Date(8) Active To
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Form ->OUSR
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Update Date
