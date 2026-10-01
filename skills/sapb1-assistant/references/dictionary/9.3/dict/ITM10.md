<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ITM10 - OITM Extension
Module: Inventory and Production | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  ISCommCode Int(11) Commodity Code ->ODCI
  ISSubMasUn Int(11) Intrastat Additional Measure ->ODCI
  ISFactor Num(19,6) IS Factor Additional Measure
  ISOrCSTImp Int(11) IS Destination State for Impor. ->ODCI
  ISOrCSTExp Int(11) IS State of Origin for Export ->ODCI
  ISNaTraImp Int(11) IS Nature of Trans. Import ->ODCI
  ISNaTraExp Int(11) IS Nature of Trans. Export ->ODCI
  ISStProImp Int(11) IS Statistical Procedure Imp. ->ODCI
  ISStProExp Int(11) IS Statistical Procedure Exp. ->ODCI
  ISOriCntry nVarChar(3) Intrastat Country of Origin ->OCRY
  ISSerCode Int(11) Intrastat Service Code ->ODCI
  ISItemType VarChar(1) Intrastat Item Type default=I [I=Item, S=Service]
  ISSerSupMt nVarChar(12) IS Service Supply Method default=I [I=Immediate, R=To More Resumptions]
  ISSerPayMt nVarChar(12) IS Service Payment Method default=X [A=Accredited to Bank Account, B=Bank Transfer, X=Other]
  ISOrCRYImp nVarChar(3) IS Destination Country for Imp. ->OCRY
  ISOrCRYExp nVarChar(3) IS Origin Country for Export ->OCRY
  ISUseWeigh VarChar(1) Use Wt in Add. Measure Calc. default=Y [Y=Yes, N=No]
  ISRelevant VarChar(1) Intrastat Relevant default=N [Y=Yes, N=No]
  ISStatCode nVarChar(2) Statistical Code
