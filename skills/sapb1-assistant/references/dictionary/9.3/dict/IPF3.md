<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# IPF3 - Landed Costs - Customs Summary
Module: Inventory and Production | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Landed Costs Internal ID ->OIPF
  LineNum Int(11) Row Number
  Dscription nVarChar(100) Summary Description
  LaCAllcAcc nVarChar(15) Landed Costs Alloc. Account
  CustSum Num(19,6) Customs Summary
  CustSumFC Num(19,6) Customs Summary FC
  CustSumSC Num(19,6) Customs Summary SC
  OpenSum Num(19,6) Open Customs Summary
  OpenSumFC Num(19,6) Open Customs Summary (FC)
  OpenSumSC Num(19,6) Open Customs Summary (SC)
  AccType Int(11) Type of Account of Summarized
  VatGroup nVarChar(8) VAT Code ->OVTG
  CstmVatStk VarChar(1) Is Customs VAT in Stock default=Y [Y=Yes, N=No]
  CCDEntry Int(11) CCD Abs. Entry
  LineNum2 Int(11) Row Number in IPF2 ->IPF2
