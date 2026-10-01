<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# PEX1 - Payment Results Table - Rows
Module: Banking | 32 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineId
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  LineId Int(11) Row Number
  PayRunDate Date(8) Date of Payment Run
  PaymWizCod Int(11) Payment Wizard Code
  VendorNum nVarChar(15) Vendor Code ->OCRD
  CustNum nVarChar(15) Customer Code ->OCRD
  PaymMethod nVarChar(15) Payment Means ->OPYM
  PaymDocNum Int(11) Payment Document No.
  FiscalYear Date(8) Fiscal Year
  VendRefNum nVarChar(100) Vendor Ref. No.
  ObjType nVarChar(20) Document Object Type
  DocDate Date(8) Document Posting Date
  TaxDate Date(8) Document Date
  CrdGLAcct nVarChar(15) BP Accounts Receivable/Payable ->OACT
  DocCurr nVarChar(3) Document Currency
  DocRate Num(19,6) Document Rate
  DocTotal Num(19,6) Document Total (LC)
  DocTotalFC Num(19,6) Document Total (FC)
  DocTaxAmnt Num(19,6) Tax Amount per Document Amount
  DoxTxAmtFC Num(19,6) Tax Amount per Document Amount
  DocRemarks nVarChar(254) Document Remarks
  DocPrmTerm Int(6) Document Payment Terms ->OCTG
  DocPymRef nVarChar(27) Payment Document Reference
  DocLocCurr nVarChar(3) Document Local Currency
  PymTermPer Int(11) Payment Terms Period
  DocNum Int(11) Document Number
  PymNum Int(11) Payment Number (PWZ3 - PymNum)
  PayOrderNo Int(11) Payment Order Number ->OIPO
  FreeText1 nVarChar(100) Free Text 1
  FreeText2 nVarChar(100) Free Text 2
  FreeText3 nVarChar(100) Free Text 3
  vatApplied Num(19,6) VAT Applied
