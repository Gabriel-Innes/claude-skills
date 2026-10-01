<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SOI5 - Statement of Import - Lines
Module: Reports | 30 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocLineNum, DocEntry, DocType, SOINum, WizardId
  SOILINENUM U: SOILineNum, SOINum, WizardId
Fields (name type(len) description [values] ->parent table):
  WizardId Int(11) Wizard ID
  SOINum Int(11) Statement No.
  DocType Int(11) Document Type
  DocEntry Int(11) Document Abs Entry
  SOILineNum Int(11) SOI Line No.
  DocLineNum Int(11) Line No.
  ItemCode nVarChar(50) Item No. ->OITM
  ItemName nVarChar(100) Item Description
  unitMsr nVarChar(100) UoM Name
  Quantity Num(19,6) Quantity
  TotalFrgn Num(19,6) Total (Doc.)
  LineTotal Num(19,6) Total (LC)
  Currency nVarChar(3) Currency ->OCRN
  Rate Num(19,6) Line Rate
  BaseRate Num(19,6) Base Currency Rate
  BasNumAtCr nVarChar(100) Base Ref. Vendor Ref. No.
  BaseDocNum Int(11) Base Ref. No.
  BaseEntry Int(11) Base Entry
  BasTaxDate Date(8) Base Ref. Document Date
  FExcBasSum Num(19,6) Fixed Excise Base Amount
  AExcBasSum Num(19,6) Ad Valorem Excise Base Amount
  ExciseUoM Int(11) Excise Units of Measure [112=Liters (m3), 168=Tons, metric tons (1000 kg), 251=Horsepower (1 hp = 0.75 kW), 831=Liters of anhydrous (pure) alcohol]
  ExcRateUoM Num(19,6) Excise Rate Units of Measure
  ExcRateAdV Num(19,6) Excise Rate Ad Valorem
  ExciseSum Num(19,6) Excise Amount
  VatBaseSum Num(19,6) VAT Base Amount
  VatPrcnt Num(19,6) VAT Rate per Row
  VatSum Num(19,6) VAT Amount
  TaxCtgr VarChar(1) Tax Type (Annual List)
  VatGroup nVarChar(8) VAT Code
