<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AMD1 - Amout Differences Report Lines
Module: Reports | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PmnInvID, PmnNum, LineNum
Fields (name type(len) description [values] ->parent table):
  LineNum Int(11) Internal ID
  PmnNum Int(11) Payment Number ->ORCT
  PmnInvID Int(11) Invoice Seq. No. in Payment
  PmnDate Date(8) Payment Date
  CardCode nVarChar(15) BP Code ->OCRD
  InvType nVarChar(20) Invoice Category default=13 [13=Sales Invoice]
  InvEntry Int(11) Invoice Key ->OINV
  InstId Int(6) Installment ID
  InvTransID Int(11) Invoice Transaction Number ->OJDT
  FCCurrency nVarChar(3) Foreign Currency ->OCRN
  InvRate Num(19,6) Rate, Invoice
  PmnRate Num(19,6) Rate, Payment
  Approved VarChar(1) Confirmed default=Y [Y=Yes, N=No]
  AmountDiff Num(19,6) Amount Difference (LC)
  TaxAmtDiff Num(19,6) Tax Difference (LC)
  TMP_JE nVarChar(50) Temporary Transaction ID
