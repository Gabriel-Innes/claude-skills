<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OAT1 - Blanket Agreement - Rows
Module: Business Partners | 36 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AgrNo, AgrLineNum
Fields (name type(len) description [values] ->parent table):
  AgrNo Int(11) Agreement No. ->OOAT
  AgrLineNum Int(11) Agreement Row Number
  ItemCode nVarChar(50) Item No. ->OITM
  ItemName nVarChar(200) Item Description
  ItemGroup Int(6) Item Group ->OITB
  PlanQty Num(19,6) Planned Quantity
  UnitPrice Num(19,6) Unit Price
  Currency nVarChar(3) Price Currency
  CumQty Num(19,6) Cumulative Quantity
  CumAmntFC Num(19,6) Cumulative Amount in FC
  CumAmntLC Num(19,6) Cumulative Amount in LC
  FreeTxt nVarChar(100) Free Text
  InvntryUom nVarChar(100) Inventory UoM
  LogInstanc Int(11) Log Instance default=0
  VisOrder Int(11) Visual Order
  RetPortion Num(19,6) Goods Return Probability
  WrrtyEnd Date(8) Date When Goods Expire
  LineStatus VarChar(1) Row Status default=O [O=Open, C=Closed]
  PlanAmtLC Num(19,6) Planned Amount (LC)
  PlanAmtFC Num(19,6) Planned Amount (FC)
  Discount Num(19,6) Line Discount
  UomEntry Int(11) UoM Entry ->OUOM
  UomCode nVarChar(20) UoM Code
  NumPerMsr Num(19,6) UoM Value default=0
  UndlvQty Num(19,6) Undeliverd Quantity
  UndlvAmntL Num(19,6) Undeliverd Amount LC
  UndlvAmntF Num(19,6) Undeliverd Amount FC
  TrnspCode Int(6) Shipping Type ->OSHP
  Project nVarChar(20) Project Code ->OPRJ
  TaxCode nVarChar(8) Tax Code
  TAXRate Num(19,6) TAX Rate
  PlVatAmtLC Num(19,6) Planned VAT Amount (LC)
  PlVatAmtFC Num(19,6) Planned VAT Amount (FC)
  CumVtAmtLC Num(19,6) Cumulative VAT Amount (LC)
  CumVtAmtFC Num(19,6) Cumulative VAT Amount (FC)
  EncryptIV nVarChar(100) Encrypt IV
