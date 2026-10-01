<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OTCX - Tax Code Determination
Module: Administration | 38 columns | ObjType: 540000005
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID
  LineNum Int(11) Row Number
  DocType Int(11) Document Type [0=Item, 1=Service, 2=Item & Service]
  BusArea Int(11) Business Area [0=Sales, 1=Purchase, 2=Sales & Purchase]
  Cond1 Int(11) Condition 1 [0=, 1=Federal Tax ID, 2=Ship-To Address, 3=Ship-To Street / PO Box, 4=Ship-To City, 5=Ship-To ZIP Code, 6=Ship-To County, 7=Ship-To State, 8=Ship-To Country, 9=Item, 10=Item Group, 11=Business Partner, 12=Customer Group, 13=Vendor Group, 14=Warehouse, 15=G/L Account, 16=Customer Equalization tax, 17=Tax Status, 18=Freight, 19=UDF, 20=Branch]
  UDFTable1 nVarChar(20) UDF Table Name
  NumVal1 Int(11) Numeric Value
  StrVal1 nVarChar(64) String Value
  MnyVal1 Num(19,6) Monetary Value
  Cond2 Int(11) Condition 2 [0=, 1=Federal Tax ID, 2=Ship-To Address, 3=Ship-To Street / PO Box, 4=Ship-To City, 5=Ship-To ZIP Code, 6=Ship-To County, 7=Ship-To State, 8=Ship-To Country, 9=Item, 10=Item Group, 11=Business Partner, 12=Customer Group, 13=Vendor Group, 14=Warehouse, 15=G/L Account, 16=Customer Equalization tax, 17=Tax Status, 18=Freight, 19=UDF, 20=Branch]
  UDFTable2 nVarChar(20) UDF Table Name
  NumVal2 Int(11) Numeric Value
  StrVal2 nVarChar(64) String Value
  MnyVal2 Num(19,6) Monetary Value
  Cond3 Int(11) Condition 3 [0=, 1=Federal Tax ID, 2=Ship-To Address, 3=Ship-To Street / PO Box, 4=Ship-To City, 5=Ship-To ZIP Code, 6=Ship-To County, 7=Ship-To State, 8=Ship-To Country, 9=Item, 10=Item Group, 11=Business Partner, 12=Customer Group, 13=Vendor Group, 14=Warehouse, 15=G/L Account, 16=Customer Equalization tax, 17=Tax Status, 18=Freight, 19=UDF, 20=Branch]
  UdfTable3 nVarChar(20) UDF Table Name
  NumVal3 Int(11) Numeric Value
  StrVal3 nVarChar(64) String Value
  MnyVal3 Num(19,6) Monetary Value
  Cond4 Int(11) Condition 4 [0=, 1=Federal Tax ID, 2=Ship-To Address, 3=Ship-To Street / PO Box, 4=Ship-To City, 5=Ship-To ZIP Code, 6=Ship-To County, 7=Ship-To State, 8=Ship-To Country, 9=Item, 10=Item Group, 11=Business Partner, 12=Customer Group, 13=Vendor Group, 14=Warehouse, 15=G/L Account, 16=Customer Equalization tax, 17=Tax Status, 18=Freight, 19=UDF, 20=Branch]
  UdfTable4 nVarChar(20) UDF Table Name
  NumVal4 Int(11) Numeric Value
  StrVal4 nVarChar(64) String Value
  MnyVal4 Num(19,6) Monetary Value
  Cond5 Int(11) Condition 5 [0=, 1=Federal Tax ID, 2=Ship-To Address, 3=Ship-To Street / PO Box, 4=Ship-To City, 5=Ship-To ZIP Code, 6=Ship-To County, 7=Ship-To State, 8=Ship-To Country, 9=Item, 10=Item Group, 11=Business Partner, 12=Customer Group, 13=Vendor Group, 14=Warehouse, 15=G/L Account, 16=Customer Equalization tax, 17=Tax Status, 18=Freight, 19=UDF, 20=Branch]
  UdfTable5 nVarChar(20) UDF Table Name
  NumVal5 Int(11) Numeric Value
  StrVal5 nVarChar(64) String Value
  MnyVal5 Num(19,6) Monetary Value
  Descr nVarChar(250) Description
  LnTaxCode nVarChar(8) Line Tax Code
  FrLnTax nVarChar(8) Line Freight Tax
  FrHdrTax nVarChar(8) Header Freight Tax
  UDFAlias1 nVarChar(18) UDF Field Alias
  UDFAlias2 nVarChar(18) UDF Field Alias
  UDFAlias3 nVarChar(18) UDF Field Alias
  UDFAlias4 nVarChar(18) UDF Field Alias
  UDFAlias5 nVarChar(18) UDF Field Alias
