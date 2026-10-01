<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CRD3 - BP Control Account
Module: Business Partners | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CardCode, AcctType
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code ->OCRD
  AcctType VarChar(1) Account Type default=M [M=Domestic, F=Foreign, D=Down Payment, A=Assets Account, R=Bill of Exchange Accounts Receivable, P=Bill of Exchange Accounts Payable, C=Bill of Exchange on Collection, S=Bill of Exchange Presentation, Y=Assets Bill of Exchange Acct Payable, I=Bill of Exchange Discounted, U=Unpaid Bill of Exchange, O=Open Debts, H=Cash Discount Interim, E=Exchange Rate Interim]
  AcctCode nVarChar(15) Account Code ->OACT
  LogInstane Int(11) Log Instance default=0
  ObjType Int(6) Object Type default=2 ->ADP1
