<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# PWZ2 - Payment Wizard - Rows 2
Module: Banking | 24 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: PymCode, IdEntry
Fields (name type(len) description [values] ->parent table):
  IdEntry Int(11) ID Entry ->OPWZ
  PymCode nVarChar(15) Payment Method Code ->OPYM
  BnkAccount nVarChar(15) Bank Account ->OACT
  MaxIncom Num(19,6) Max. Incoming Amount
  MaxOutgo Num(19,6) Max. Outgoing Amount
  Balance Num(19,6) G/L Balance
  ExpectBal Num(19,6) Expected G/L Balance
  Checked VarChar(1) Checked
  PymDisc nVarChar(100) Payment Description
  PymType VarChar(1) Payment Type
  IntBalance Num(19,6) G/L Interim Balance
  ExpIntBal Num(19,6) Expected G/L Interim Balance
  InterimAct nVarChar(15) Interim Account ->OACT
  BnkCountry nVarChar(3) Bank Country
  BnkCode nVarChar(30) Bank Code
  BnkAccNo nVarChar(50) Bank Account Number
  FatherLn VarChar(1) Parent Line default=N [Y=Yes, N=No]
  NegativPym nVarChar(15) Negative Payment Method Code
  NegPymBnk nVarChar(30) Negative Payment Bank Code
  NegCountry nVarChar(3) Negative Payment Bank Country
  NegPymAcct nVarChar(50) Negative Payment Bank Account
  PaymenMean VarChar(1) Payment Means
  IBAN nVarChar(50) IBAN
  SwiftNum nVarChar(50) BIC/SWIFT Code
