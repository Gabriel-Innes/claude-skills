<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OEOY - End-of-Year Transfer
Module: Administration | 124 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CompName
Fields (name type(len) description [values] ->parent table):
  GenrlDefs VarChar(1) General Definitions default=Y [Y=, N=]
  ReFiles VarChar(1) Transfer Template Designer Files default=Y [Y=, N=]
  ActIndex VarChar(1) Transfer Accounts Index default=Y [Y=, N=]
  ActFromCod nVarChar(15) From Code
  ActToCode nVarChar(15) To Code
  ActGroup nVarChar(16) ActGroup default=255
  CrdIndex VarChar(1) Transfer Credit Card Index default=Y [Y=, N=]
  CrdFromCod nVarChar(15) From Code
  CrdToCode nVarChar(15) To Code
  CrdGrpCust Int(6) Customer Group
  CrdGrpVndr Int(6) Vendor Group
  CrdToknAnd VarChar(1) CrdToknAnd
  CrdUseGrps VarChar(1) CrdUseGrps
  CrdClsRang VarChar(1) CrdClsRang
  CrdGrpData nVarChar(64) Properties
  ItmIndex VarChar(1) Transfer Item Index default=Y [Y=, N=]
  ItmFromCod nVarChar(50) From Code
  ItmToCode nVarChar(50) To Code
  ItmGroup Int(6) Item Group
  ItmToknAnd VarChar(1) ItmToknAnd
  ItmUseGrps VarChar(1) ItmUseGrps
  ItmClsRang VarChar(1) ItmClsRang
  ItmGrpData nVarChar(64) Properties
  TransfDoc VarChar(1) Documents Transfer default=N [Y=, N=]
  UnDpsChk VarChar(1) Transfer Undeposited Checks default=N [Y=, N=]
  DpsChk VarChar(1) Transfer Postdated Checks default=N [Y=, N=]
  UnDpsVouch VarChar(1) Transfer Unpaid Vouchers default=N [Y=, N=]
  DpsVouch VarChar(1) Transfer Deffered Vouchers default=N [Y=, N=]
  WorkOrder VarChar(1) Open Work Instructions default=N [Y=, N=]
  RcrTrt VarChar(1) Posting Templates & Rec. Trans default=N [Y=, N=]
  Connection VarChar(1) Activities default=N [Y=, N=]
  SpcPrice VarChar(1) Special Prices default=N [Y=, N=]
  Quotations VarChar(1) Transfer Open Sales Quotations default=N
  Orders VarChar(1) Transfer Open Orders default=N [Y=, N=]
  DlvrNotes VarChar(1) Transfer Open Delivery Notes default=N [Y=, N=]
  DlvrInvocs VarChar(1) Transfer Open Invoices default=N [Y=, N=]
  P_Orders VarChar(1) Transfer Purchase Orders default=N [Y=, N=]
  P_Invoices VarChar(1) A/P Invoices default=N [Y=, N=]
  ProdTree VarChar(1) Product Tree default=N [Y=, N=]
  Subst VarChar(1) Customer/Vendor Catalog No. default=N [Y=, N=]
  Import VarChar(1) Landed Costs default=N [Y=, N=]
  Revert VarChar(1) Returns default=N [Y=, N=]
  ActBlnc VarChar(1) Transfer Account Balances default=N [Y=, N=]
  ActRef1 nVarChar(11) Ref. 1 for Opening Bal. Trans.
  ActRef2 nVarChar(11) Ref. 2 for Opening Bal. Trans.
  ActRefDate Date(8) Posting Date for OB Transactions
  ActDueDate Date(8) Due date for OB transaction
  ActMemo nVarChar(50) Journal Entry Details
  AOpnBlnAct nVarChar(15) Opening Balances Account
  AEquetyAct nVarChar(15) Retained Earnings Account
  ActExpLine VarChar(1) Transfer Split Balances default=N [Y=Unreconciled Internally, N=, E=Unreconciled Externally]
  ActBlncFrC nVarChar(15) From Code
  ActBlncToC nVarChar(15) To Code
  ActBlncGrp nVarChar(16) ActBlncGrp default=YYY
  ActZeroBln VarChar(1) Account Transactions with Zero Balance default=Y [Y=, N=]
  CrdBlnc VarChar(1) Transfer Credit Card Balances default=N [Y=, N=]
  CrdRef1 nVarChar(11) Ref. 1 for OB Transactions
  CrdRef2 nVarChar(11) Ref. 2 for OB Transactions
  CrdRefDate Date(8) Posting Date for OB Transactions
  CrdDueDate Date(8) Due date for OB transaction
  CrdMemo nVarChar(50) Journal Entry Details
  COpnBlnAct nVarChar(15) Opening Balances Account
  CrdExpLine VarChar(1) Transfer Split Balances default=N [Y=, N=]
  CrdBlncFrC nVarChar(15) From Code
  CrdBlncToC nVarChar(15) To Code
  CrdBlncGrC Int(6) Customer Group
  CrdBlnGrpV Int(6) Vendor Group
  CrdBTknAnd VarChar(1) CrdBTknAnd
  CrdBUseGrp VarChar(1) CrdBUseGrp
  CrdBClsRng VarChar(1) CrdBClsRng
  CrdBGrpDat nVarChar(64) Properties
  CrdZeroBln VarChar(1) Card Transactions with Zero Balance default=Y [Y=, N=]
  ItmBlnc VarChar(1) Transfer Item Balances default=N [Y=, N=]
  ItmRef1 nVarChar(11) Ref. 1 for Opening Bal. Trans.
  ItmRef2 nVarChar(11) Ref. 2 for Opening Bal. Trans.
  ItmRefDate Date(8) Posting Date for OB Transaction
  ItmMemo nVarChar(50) Journal Entry Details
  ItmBlncFrC nVarChar(50) From Code
  ItmBlncToC nVarChar(50) To Code
  ItmBlncGrp Int(6) Item Group
  ItmBTknAnd VarChar(1) ItmBTknAnd
  ItmBUseGrp VarChar(1) ItmBUseGrp
  ItmBClsRng VarChar(1) ItmBClsRng
  ItmBGrpDat nVarChar(64) Properties
  ItmPlnNum Int(6) Transaction Price List default=1
  ItmZeroPr VarChar(1) Transfer Items Without Price default=N [Y=, N=]
  FileReport VarChar(1) Create Report File default=Y [Y=, N=]
  CompName nVarChar(100) Company Name for Transfering
  WasGnrlDef VarChar(1) Was general data transferred default=N [Y=, N=]
  P_DlvrNots VarChar(1) Transfer PO Del. Notes default=N [Y=, N=]
  Spg VarChar(1) Transfer Discount for Groups default=N [Y=, N=]
  Pdn VarChar(1) Purchase Delivery Notes default=N [Y=, N=]
  PdnClosed VarChar(1) Closed Purchase Delivery Notes default=N [Y=, N=]
  Rpd VarChar(1) Revert Purchase Delivery Notes default=N [Y=, N=]
  ReportTemp VarChar(1) Report Templates default=N [Y=, N=]
  Confirmat VarChar(1) Confirmation default=N [Y=, N=]
  DocDraft VarChar(1) Document Drafts default=N [Y=, N=]
  ChkOutDrft VarChar(1) Checks for Payment Drafts default=N [Y=, N=]
  OptOpen VarChar(1) Open Opportunities default=N [Y=, N=]
  OptClosed VarChar(1) Closed Opportunities default=N [Y=, N=]
  SerBtchNum VarChar(1) Batch/Serial No. default=N [Y=, N=]
  CorrInvoic VarChar(1) Correction Invoice default=N [Y=, N=]
  UserGign Int(6) User Signature ->OUSR
  PaymDraf VarChar(1) Payment Draft default=N [Y=, N=]
  PaymentWiz VarChar(1) Saved Payment Wizard default=N [N=No, Y=Yes]
  AltItems VarChar(1) Alternative Items default=N [N=No, Y=Yes]
  DPIInvoice VarChar(1) A/R Down Payment Invoice default=N
  DPIRequest VarChar(1) A/R Down Payment Request default=N [Y=Yes, N=No]
  Ctr VarChar(1) Service Contracts default=N [Y=Yes, N=No]
  Ins VarChar(1) Customer Equipment Card default=N [Y=Yes, N=No]
  CorrAPInv VarChar(1) A/P Correction Invoice default=N [Y=Yes, N=No]
  CorrAPRev VarChar(1) A/P Correction Invoice Reversal default=N [Y=Yes, N=No]
  CorrARInv VarChar(1) A/R Correction Invoice default=N [Y=Yes, N=No]
  CorrARRev VarChar(1) A/R Correction Invoice Reversal default=N [Y=Yes, N=No]
  UserObj VarChar(1) User Object default=N [N=No, Y=Yes]
  AdWrkOrdr VarChar(1) Advanced Work Order default=N [Y=Yes, N=No]
  DPOInvoice VarChar(1) A/P Down Payment Invoice default=N [Y=Yes, N=No]
  DPORequest VarChar(1) A/P Down Payment Request default=N [Y=Yes, N=No]
  P_Quotatio VarChar(1) Transfer Open Pur. Quotations default=N [Y=Yes, N=No]
  WTQ VarChar(1) Inventory Transfer Requests default=N [Y=Yes, N=No]
  Oat VarChar(1) Blanket Agreement default=N [Y=Yes, N=No]
  CPN VarChar(1) Campaign default=N [Y=Yes, N=No]
  AdvRules VarChar(1) Transfer Advanced Rules default=N [Y=Yes, N=No]
  Prq VarChar(1) Purchase Request default=N
