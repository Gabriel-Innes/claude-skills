<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# WTM3 - Approval Templates - Documents
Module: Administration | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TransType, WtmCode
Fields (name type(len) description [values] ->parent table):
  WtmCode Int(11) Code ->OWTM
  TransType nVarChar(20) Original Document [23=Sales Quotation, 17=Sales Order, 15=Delivery, 234000031=Returns Request, 16=Returns, 203=A/R Down Payment, 13=A/R Invoice, 165=A/R Correction Invoice, 166=A/R Correction Invoice Reversal, 14=A/R Credit Memo, 132=Correction Invoice, 1470000113=Purchase Request, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Returns Request, 21=Goods Returns, 204=A/P Down Payment, 18=A/P Invoice, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 19=A/P Credit Memo, 59=Goods Receipt, 60=Goods Issue, 1250000001=Inventory Transfer Request, 67=Inventory Transfer, 1470000065=Inventory Counting, 310000001=Inventory Opening Balance, 10000071=Inventory Posting, 46=Outgoing Payment, 1250000026=Sales Blanket Agreements, 1250000027=Purchase Blanket Agreements]
