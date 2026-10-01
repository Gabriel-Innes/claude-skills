<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BinLocation (Object)

A bin location is the smallest addressable unit of space in a warehouse where your goods are stored. To facilitate bin location management, SAP Business One lets you maintain a master data record for each bin location. Source table: OBIN.

## Properties (41)
- `Public Property AbsEntry() As Long` [R] The key of the bin location. Field name: AbsEntry.
- `Public Property AlternativeSortCode() As String` [R/W] The alternative sort code for the bin location. Field name: AltSortCod. Length: 50 characters.
- `Public Property Attribute1() As String` [R/W] The attribute that are relevant to the bin location. Field name: Attr1Val. Length: 20 characters.
- `Public Property Attribute10() As String` [R/W] The attribute that are relevant to the bin location. Field name: Attr10Val. Length: 20 characters.
- `Public Property Attribute2() As String` [R/W] The attribute that are relevant to the bin location. Field name: Attr2Val. Length: 20 characters.
- `Public Property Attribute3() As String` [R/W] The attribute that are relevant to the bin location. Field name: Attr3Val. Length: 20 characters.
- `Public Property Attribute4() As String` [R/W] The attribute that are relevant to the bin location. Field name: Attr4Val. Length: 20 characters.
- `Public Property Attribute5() As String` [R/W] The attribute that are relevant to the bin location. Field name: Attr5Val. Length: 20 characters.
- `Public Property Attribute6() As String` [R/W] The attribute that are relevant to the bin location. Field name: Attr6Val. Length: 20 characters.
- `Public Property Attribute7() As String` [R/W] The attribute that are relevant to the bin location. Field name: Attr7Val. Length: 20 characters.
- `Public Property Attribute8() As String` [R/W] The attribute that are relevant to the bin location. Field name: Attr8Val. Length: 20 characters.
- `Public Property Attribute9() As String` [R/W] The attribute that are relevant to the bin location. Field name: Attr9Val. Length: 20 characters.
- `Public Property BarCode() As String` [R/W] The bar code for the bin location. Field name: BarCode. Length: 100 characters.
- `Public Property BatchRestrictions() As BinRestrictionBatchEnum` [R/W] The batch restriction status of the bin location. Field name: SngBatch.
- `Public Property BinCode() As String` [R] The code of the bin location. Field name: BinCode. Length: 228 characters.
- `Public Property DateRestrictionChanged() As Date` [R] The last date on which you updated the transaction restrictions of the bin location. Field name: RtrictDate.
- `Public Property Description() As String` [R/W] The description of the bin location. Field name: Descr. Length: 50 characters.
- `Public Property ExcludeAutoAllocOnIssue() As BoYesNoEnum` [R/W] property ExcludeAutoAllocOnIssue
- `Public Property Inactive() As BoYesNoEnum` [R/W] Indicates whether to deactivate the bin location. Field name: Disabled.
- `Public Property IsSystemBin() As BoYesNoEnum` [R] Indicates whether the bin location is the system bin location. Field name: SysBin.
- `Public Property MaximumQty() As Double` [R/W] The maximum quantity of items for the bin location. Field name: MaxLevel.
- `Public Property MaximumWeight() As Double` [R/W] property MaximumWeight
- `Public Property MaximumWeight1() As Double` [R/W] property MaximumWeight1
- `Public Property MaximumWeightUnit() As Long` [R/W] property MaximumWeightUnit
- `Public Property MaximumWeightUnit1() As Long` [R/W] property MaximumWeightUnit1
- `Public Property MinimumQty() As Double` [R/W] The minimum quantity of items for the bin location. Field name: MinLevel.
- `Public Property ReceivingBinLocation() As BoYesNoEnum` [R/W] Indicates whether the bin location is a receiving bin location. Field name: ReceiveBin.
- `Public Property RestrictedItemType() As BinRestrictItemEnum` [R/W] The item restriction status of the bin location. Field name: ItmRtrictT.
- `Public Property RestrictedTransType() As BinRestrictTransactionEnum` [R/W] The transaction restriction status of the bin location. Field name: RtrictType.
- `Public Property RestrictedUoMType() As BinRestrictUoMEnum` [R/W] property RestrictedUoMType
- `Public Property RestrictionReason() As String` [R/W] The reason for the transaction restrictions of the bin location. Field name: RtrictResn. Length: 254 characters.
- `Public Property SpecificItem() As String` [R/W] The specific item code. Field name: SpcItmCode. Length: 20 characters.
- `Public Property SpecificItemGroup() As Long` [R/W] The specific item group. Field name: SpcItmGrpC.
- `Public Property SpecificUoM() As Long` [R/W] property SpecificUoM
- `Public Property SpecificUoMGroup() As Long` [R/W] property SpecificUoMGroup
- `Public Property Sublevel1() As String` [R/W] The sublevel codes that represent the physical location of the bin. Field name: SL1Code. Length: 50 characters.
- `Public Property Sublevel2() As String` [R/W] The sublevel codes that represent the physical location of the bin. Field name: SL2Code. Length: 50 characters.
- `Public Property Sublevel3() As String` [R/W] The sublevel codes that represent the physical location of the bin. Field name: SL3Code. Length: 50 characters.
- `Public Property Sublevel4() As String` [R/W] The sublevel codes that represent the physical location of the bin. Field name: SL4Code. Length: 50 characters.
- `Public Property UserFields() As Fields` [R] Get User Fields
- `Public Property Warehouse() As String` [R/W] The warehouse where the bin is located. Field name: WhsCode. Length: 8 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
