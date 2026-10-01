<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCTG - Payment Terms
Module: Banking | 25 columns | ObjType: 40
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: GroupNum
  ABS_ENTRY U: PymntGroup
Fields (name type(len) description [values] ->parent table):
  GroupNum Int(6) Group Number
  PymntGroup nVarChar(100) Payment Terms Code
  PayDuMonth VarChar(1) Start From default=N [E=Month End, H=Half Month, Y=Month Start, N=]
  ExtraMonth Int(6) Number of Additional Months default=0
  ExtraDays Int(6) Number of Additional Days default=0
  PaymntsNum Int(6) Number of Payments
  CredLimit Num(19,6) Max. Credit
  VolumDscnt Num(19,6) Total Discount %
  LatePyChrg Num(19,6) Interest % on Receivables
  ObligLimit Num(19,6) Commitment Limit
  ListNum Int(6) Price List ->OPLN
  Payments VarChar(1) Partial Payment default=N [Y=Yes, N=No]
  NumOfPmnts Int(6) Number of Payments default=1
  Payment1 Num(19,6) First Partial Payment
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  OpenRcpt VarChar(1) Open Incoming Payment default=N [N=No, 3=Cash, 1=Checks, 4=Credit, 2=Bank Transfer, 5=Bill of Exchange]
  DiscCode nVarChar(20) Discount Code ->OCDC
  DunningCod nVarChar(20) Dunning Code ->ORIT
  BslineDate VarChar(1) Due Date Based on default=T [P=Posting Date, S=System Date, T=Document Date, C=Closing Date]
  InstNum Int(6) No. of Installments
  TolDays Int(6) No. of Tolerance Days
  VATFirst VarChar(1) Apply Tax on 1st Installment default=N [Y=Yes, N=No, T=Tax Only]
  CrdMthd VarChar(1) Credit Method default=L [F=First Installment, L=Last Installment, E=Equally]
  CshRelev VarChar(1) Cash Relevant Transaction default=N [Y=Yes, N=No]
