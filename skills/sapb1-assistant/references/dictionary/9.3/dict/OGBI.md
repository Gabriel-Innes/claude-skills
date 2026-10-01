<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OGBI - GB Interface: Common Info
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator
  RepNo nVarChar(20) Report Number
  RepCompany nVarChar(60) Report Company Name
  RepPeriod nVarChar(8) Report Period
  Currency nVarChar(10) Currency Unit
  UserSign Int(6) User Signature
  CreateDate nVarChar(8) Report Creation Date
  RepType Int(11) Report Type default=0 [0=, 1=Electronic Account Book, 2=G/L Account Master Records, 3=Departments, 16=Employees, 4=Business Partners, 5=Projects, 6=G/L Account Balance, 7=Accounting Vouchers, 8=Enterprise's Balance Sheet, 9=Enterprise's Profit and Loss Statement, 10=Enterprise's Cash Flow Statement, 11=Devalue Provision of Enterprise Assets, 12=Shareholder's Rights and Interests Changing Report, 13=Enterprise's Profit Distribution Report, 14=Small Enterprise's Cash Flow Statement, 15=Enterprise's VAT Payable Detail Report]
  RepEntity nVarChar(60) Report Entity
