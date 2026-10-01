<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# TPW2 - Payable Information
Module: Banking | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNumber, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Absolute Entry No ->OTPW
  LineNumber Int(11) Line Number
  TaxCategry Int(11) Tax Category
  TaxType Int(11) Tax Type
  PyblAmnt Num(19,6) Payable Amount
  PyblAmntFC Num(19,6) Payable Amount FC
  PyblAmntSC Num(19,6) Payable Amount SC
  PLAAmnt Num(19,6) P.L.A. Amount
  PLAAmntFC Num(19,6) P.L.A. Amount (FC)
  PLAAmntSC Num(19,6) P.L.A. Amount (SC)
