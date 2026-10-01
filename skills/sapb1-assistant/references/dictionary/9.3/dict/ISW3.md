<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ISW3 - Declaration Rows
Module: Finance | 75 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Line, WizAbsEnt
Fields (name type(len) description [values] ->parent table):
  WizAbsEnt Int(11) Wizard Run Key ->OISW
  Line Int(11) Declaration Line
  ItemCode nVarChar(50) Item Code ->OITM
  RowStatus VarChar(1) Row Status default=O
  CardCode nVarChar(15) Business Partner Code ->OCRD
  ObjType Int(11) Document Type
  DocNum Int(11) Document Number
  DocLineNum Int(11) Document Line Number
  RecpType VarChar(1) Receipt Type
  DocBillDt Date(8) Document Billing Date
  Quantity Num(19,6) Quantity
  BPCtry nVarChar(3) Sender/Receiver Country
  TaxCodeExt nVarChar(12) Tax Code Extension
  NetMassSgn VarChar(1) Net Mass Sign default=+ [+=Positive, -=Negative]
  NetMass Num(19,6) Net Mass
  NetMassUnt nVarChar(12) Net Mass Unit
  SupMassSgn VarChar(1) Supplementary Mass Sign default=+ [+=Positive, -=Negative]
  SupplMass Num(19,6) Supplementary Mass
  SupplUnit nVarChar(50) Supplementary Unit
  ValueSgn VarChar(1) Value Sign default=+ [+=Positive, -=Negative]
  Value Num(19,6) Value
  ValueFC Num(19,6) Value in Foreign Currency
  FCCurrency nVarChar(3) Foreign Currency
  StatValSgn VarChar(1) Statistical Value Sign [+=Positive, -=Negative]
  StatVal Num(19,6) Statistical Value
  ReturnID VarChar(1) Return Identifier
  Include VarChar(1) Include Line in Report default=Y [Y=Yes, N=No]
  IsChanged VarChar(1) Changed Line Flag default=N [Y=Yes, N=No]
  DstRegCry nVarChar(3) Destination Country - Region
  DstRegSta nVarChar(12) Destination Region State
  OriRegCry nVarChar(3) Origin Region Country
  OriRegSta nVarChar(12) Origin Region State
  BpVATregNo nVarChar(32) VAT Registration No.
  CtryOrig nVarChar(3) Country of Origin
  Incoterms nVarChar(12) Incoterms
  NatOfTrans nVarChar(50) Nature of Transaction
  TransMode nVarChar(12) Transport Mode
  PortEnEx nVarChar(50) Port of Entry or Exit
  CustProc nVarChar(50) Custom Procedure
  StatProc nVarChar(50) Statistical Procedure
  DomFrgID VarChar(1) Domestic/Foreign Identifier
  ItemType VarChar(1) Item Type default=I [I=Item, S=Service, N=Item Not Relevant to Intrastat]
  CommCode nVarChar(12) Commodity Code
  SerCode nVarChar(12) Service Code
  SerSupplM VarChar(1) Service Supply Method default=I [I=Immediate, R=To More Resumptions]
  SerPymMeth VarChar(1) Service Payment Method default=A [A=Accredited to Bank Account, B=Bank Transfer, X=Other]
  CorrDate Date(8) Correction Date
  CorrSgn VarChar(1) Correction Sign default=+ [+=Positive, -=Negative]
  ReferDoc Int(11) Referenced Document
  ReferDocNo Int(11) Referenced Document No.
  ReferItem nVarChar(50) Referred Item ->OITM
  RefDocLine Int(11) Referenced Document Line
  ChgID nVarChar(16) Changed Data Record ID
  ChgUser nVarChar(50) Changed By
  ChgTimest Date(8) Time Stamp of Change
  Deleted VarChar(1) Deleted Indicator default=N [N=No, Y=Yes]
  CstSecRc nVarChar(6) Custom Section
  CorrMonth Int(6) Ref. Mo. of Summary to Correct
  CorrYear Int(6) Ref. Yr of Summary to Correct
  CorrDeclNo Int(11) No. of Declaration to Correct
  CorRowNo Int(11) Row No. Inside Sec. 3 to Correct
  DeclRowNo Int(11) Declaration File Row No.
  CorrType Int(11) Referred Type of Receipt
  CntryPay nVarChar(3) State Code for Payment
  Triangular VarChar(1) Triangular Trade default=N [N=No, Y=Yes]
  CardName nVarChar(100) Business Partner Name
  StatCode nVarChar(2) Statistical Code
  DocEntry Int(11) Document Entry
  NetValue Num(19,6) Net Value
  NetValueFC Num(19,6) Net Value in FC
  Freight Num(19,6) Freight Sum
  FreighFC Num(19,6) Freight Sum in FC
  RateFC Num(19,6) Currency Rate for FC
  Remarks nVarChar(250) Remarks
  ProtocolN Int(11) Protocol Number
