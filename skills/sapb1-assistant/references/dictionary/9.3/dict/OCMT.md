<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCMT - Competitors
Module: Sales Opportunities | 6 columns | ObjType: 109
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CompetId
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  CompetId Int(11) Sequence No.
  Name nVarChar(15) Name
  ThreatLevl Int(6) Threat Level default=1 [1=Low, 2=Medium, 3=High]
  Memo nVarChar(50) Details
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
