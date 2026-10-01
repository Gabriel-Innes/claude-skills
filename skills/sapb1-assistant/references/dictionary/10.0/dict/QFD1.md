<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# QFD1 - Query Fields Definition
Module: Administration | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: IntrnalKey, LineNum
Fields (name type(len) description [values] ->parent table):
  IntrnalKey Int(11) Internal Key
  LineNum Int(11) Row Number
  FieldName nVarChar(80) Field Name
  FieldDesc nVarChar(100) Field Description
  OrigTable nVarChar(100) Original Table
  OrigField nVarChar(50) Original Field
  EditType VarChar(1) Edit Type [-=None, T=Tax, R=Rate, P=Price, S=Sum, N=Unit, Q=Quantity, %=Percent, M=Measure]
  StatType VarChar(1) Statistical Type default=D [D=Dimension, M=Measure]
  AggrType VarChar(1) Aggregation Type default=N [N=None, S=Sum, A=Average, C=Count, M=Minimum, X=Maximum]
  LinkTable nVarChar(100) Linked Table
  DeciPlace Int(6) Decimal Places default=2 [0=No Decimals, 1=One Decimal, 2=Two Decimals, 3=Three Decimals, 4=Four Decimals, 5=Five Decimals, 6=No Rounding, 7=Amounts, 8=Prices, 9=Rates, 10=Quantities, 11=Units, 12=Percent]
  DbType VarChar(1) Database Type
