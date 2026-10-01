<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCRP - Payment Methods
Module: Administration | 11 columns | ObjType: 70
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CrTypeCode
  NAME U: CrTypeName
  CRED_CODE: CreditCard
  INSTALMENT: InstalMent
Fields (name type(len) description [values] ->parent table):
  CrTypeCode Int(6) Payment Method Code
  CrTypeName nVarChar(30) Name
  CreditCard Int(6) Assigned to Credit Card ->OCRC
  DueTerms nVarChar(8) Payment Code ->OCDT
  MinCredit Num(19,6) Minimum Credit Amount
  MinToPay Num(19,6) Minimum Payment Amount
  MaxValid Num(19,6) Max. Qty Without Approval
  InstalMent VarChar(1) Installment Payments Possible default=N [Y=Yes, N=No, C=Cr, L=Rd]
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
