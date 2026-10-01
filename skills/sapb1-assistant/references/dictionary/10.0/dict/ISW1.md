<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ISW1 - Reported Business Partners
Module: Finance | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WizAbsEnt, CardCode
Fields (name type(len) description [values] ->parent table):
  WizAbsEnt Int(11) Wizard Run Key ->OISW
  CardCode nVarChar(15) Business Partner Code ->OCRD
  CardName nVarChar(100) Business Partner Name
  CardType VarChar(1) Business Partner Type
  NatOfTrans nVarChar(50) Nature of Transaction
  StatProc nVarChar(50) Statistical Procedure
  CustProc nVarChar(50) Customs Procedure
  TransMode nVarChar(12) Transport Mode
  Incoterms nVarChar(12) Incoterms
  PortEnEx nVarChar(50) Port of Entry or Exit
  BPVATRegNo nVarChar(32) Business Partner VAT Reg. No.
  DomFrgID VarChar(1) Domestic/Foreign Identifier
  CtryOrig nVarChar(3) Country/Region of Origin
  BPCountry nVarChar(3) Business Partner Country/Region
