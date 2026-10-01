<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# TPW3 - Utilization and Payment
Module: Banking | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: MatType, CrTaxType, CrTaxCtgry, LineNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Absolute Entry No ->OTPW
  LineNum Int(11) Line Number ->TPW2
  CrTaxCtgry Int(11) Credit Tax Category
  CrTaxType Int(11) Credit Tax Type
  CrUtiliz Num(19,6) Credit Utilized Amount
  CrUtilizFC Num(19,6) Credit Utilized Amount FC
  CrUtilizSC Num(19,6) Credit Utilized Amount SC
  PymMeth nVarChar(15) Payment Method
  PymAmnt Num(19,6) Payment Amount
  PymAmntFC Num(19,6) Payment Amount (FC)
  PymAmntSC Num(19,6) Payment Amount (SC)
  MatType Int(11) Material Type default=0 [0=]
