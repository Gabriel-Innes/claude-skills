<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OBCG - Bank Charge for Bank Transfers
Module: Banking | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SerialNo
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code
  BkChgAmt Num(19,6) Bank Charge
  SerialNo Int(11) Serial No.
  DocCurr nVarChar(3) Document Currency
  BcgTaxAmt Num(19,6) Bank Charge Tax
