<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ARC6 - Incoming Payments - WTax Rows - History
Module: Banking | 77 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ObjType, LogInstanc, Line, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->ORCT
  InvoiceId Int(11) Invoice Key
  WTCode nVarChar(4) WTax Code ->OWHT
  PymMean VarChar(1) Payment Means default=C [C=Cash, K=Checks, R=Credit Card, T=Bank Transfer, B=Bill of Exchange]
  DueDate Date(8) Due Date
  WTSum Num(19,6) WTax Amount
  WTSumFC Num(19,6) WTax Amount (SC)
  WTSumSC Num(19,6) WTax Amount (FC)
  Rate Num(19,6) Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntFC Num(19,6) Taxable Amount (FC)
  TxblAmntSC Num(19,6) Taxable Amount (SC)
  PymAmount Num(19,6) Payment Amount
  PymAmounF Num(19,6) Payment Amount (FC)
  PymAmounS Num(19,6) Payment Amount (SC)
  Line Int(11) Internal Number
  LogInstanc Int(11) Log Instance - History default=0
  ObjType nVarChar(20) Object Type default=24 ->ADP1
  TdsBAmt Num(19,6) TDS Base Amount
  TdsBAmtSC Num(19,6) TDS Base Amount (SC)
  TdsBAmtFC Num(19,6) TDS Base Amount (FC)
  SurBAmt Num(19,6) Surcharge Base Amount
  SurBAmtSC Num(19,6) Surcharge Base Amount (SC)
  SurBAmtFC Num(19,6) Surcharge Base Amount (FC)
  CessBAmt Num(19,6) Cess Base Amount
  CessBAmtSC Num(19,6) Cess Base Amount (SC)
  CessBAmtFC Num(19,6) Cess Base Amount (FC)
  HscBAmt Num(19,6) HSC Base Amount
  HscBAmtSC Num(19,6) HSC Base Amount (SC)
  HscBAmtFC Num(19,6) HSC Base Amount (FC)
  TdsAmnt Num(19,6) TDS Tax Amount
  TdsAmntSC Num(19,6) TDS Tax Amount (SC)
  TdsAmntFC Num(19,6) TDS Tax Amount (FC)
  SurAmnt Num(19,6) Surcharge Tax Amount
  SurAmntSC Num(19,6) Surcharge Tax Amount (SC)
  SurAmntFC Num(19,6) Surcharge Tax Amount (FC)
  CessAmnt Num(19,6) Cess Tax Amount
  CessAmntSC Num(19,6) Cess Tax Amount (SC)
  CessAmntFC Num(19,6) Cess Tax Amount (FC)
  HscAmnt Num(19,6) HSC Tax Amount
  HscAmntSC Num(19,6) HSC Tax Amount (SC)
  HscAmntFC Num(19,6) HSC Tax Amount (FC)
  WTTypeId Int(11) WT Type Id ->OWTT
  WTPosted Num(19,6) WT Posted
  WTPostedFC Num(19,6) WT Posted FC
  WTPostedSC Num(19,6) WT Posted SC
  IgstBAmt Num(19,6) IGST Base Amount
  IgstBAmtSC Num(19,6) IGST Base Amount (SC)
  IgstBAmtFC Num(19,6) IGST Base Amount (FC)
  CgstBAmt Num(19,6) CGST Base Amount
  CgstBAmtSC Num(19,6) CGST Base Amount (SC)
  CgstBAmtFC Num(19,6) CGST Base Amount (FC)
  SgstBAmt Num(19,6) SGST Base Amount
  SgstBAmtSC Num(19,6) SGST Base Amount (SC)
  SgstBAmtFC Num(19,6) SGST Base Amount (FC)
  IgstAmnt Num(19,6) IGST Tax Amount
  IgstAmntSC Num(19,6) IGST Tax Amount (SC)
  IgstAmntFC Num(19,6) IGST Tax Amount (FC)
  CgstAmnt Num(19,6) CGST Tax Amount
  CgstAmntSC Num(19,6) CGST Tax Amount (SC)
  CgstAmntFC Num(19,6) CGST Tax Amount (FC)
  SgstAmnt Num(19,6) SGST Tax Amount
  SgstAmntSC Num(19,6) SGST Tax Amount (SC)
  SgstAmntFC Num(19,6) SGST Tax Amount (FC)
  DepositNum Int(11) Deposit Number ->OVPM
  UtgstBAmt Num(19,6) UTGST Base Amount
  UtgstBAmtS Num(19,6) UTGST Base Amount (SC)
  UtgstBAmtC Num(19,6) UTGST Base Amount (FC)
  CsgstBAmt Num(19,6) Cess GST Base Amount
  CsgstBAmtS Num(19,6) Cess GST Base Amount (SC)
  CsgstBAmtC Num(19,6) Cess GST Base Amount (FC)
  UtgstAmt Num(19,6) UTGST Amount
  UtgstAmtSC Num(19,6) UTGST Amount (SC)
  UtgstAmtFC Num(19,6) UTGST Amount (FC)
  CsgstAmt Num(19,6) Cess GST Amount
  CsgstAmtSC Num(19,6) Cess GST Amount (SC)
  CsgstAmtFC Num(19,6) Cess GST Amount (FC)
