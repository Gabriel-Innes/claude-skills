<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TaxCodeDetermination (Object)

Represents the tax code determination rules according to which the application proposes tax codes in sales and purchasing document lines. Source table: OTCX.

**Remarks:** Relevant for all localizations except Brazil, India, Israel, and Puerto Rico.

## Properties (38)
- `Public Property BusinessArea() As BoBusinessAreaEnum` [R/W] The business area, for which the tax code determination rule is relevant, for example, sales, purchasing, or both. Mandatory property. Field name: BusArea.
- `Public Property Condition1() As BoTCDConditionEnum` [R/W] The condition based upon which the tax code is determined. If you select more than one condition, all conditions must be met for the tax code determination rule to be applied. Mandatory property. Field name: Cond1.
- `Public Property Condition2() As BoTCDConditionEnum` [R/W] The second condition based upon which the tax code is determined. Field name: Cond2.
- `Public Property Condition3() As BoTCDConditionEnum` [R/W] The third condition based upon which the tax code is determined. Field name: Cond3.
- `Public Property Condition4() As BoTCDConditionEnum` [R/W] The fourth condition based upon which the tax code is determined. Field name: Cond4.
- `Public Property Condition5() As BoTCDConditionEnum` [R/W] The fifth condition based upon which the tax code is determined. Field name: Cond5.
- `Public Property Description() As String` [R/W] The additional explanation for the tax code determination rule. Field name: Descr. Length: 250 characters.
- `Public Property DocEntry() As Long` [R] The internal key of the document. Field name: DocEntry.
- `Public Property DocumentType() As BoTCDDocumentTypeEnum` [R/W] The type of document, for which the tax code determination rule is relevant, for example, item, service, or both. Mandatory property. Field name: DocType.
- `Public Property FreightHeaderTax() As String` [R/W] The tax code for freight charges in sales or purchasing document headers. Field name: FrHdrTax.
  - remarks: In the SAP Business One application, this field is available only if you have selected Manage Freight in Documents on the General tab of the Document Settings window (Administration --> System Initialization --> Document Settings).
- `Public Property FreightRowTax() As String` [R/W] The tax code for freight charges in sales or purchasing document lines. Field name: FrLnTax.
- `Public Property LineNumber() As Long` [R/W] Sets or returns the row number within the hierarchy of tax code determination rules. When determining the tax code proposal in a sales or purchasing document, the application works its way through the rules, starting at the highest position. Field name: LineNum.
- `Public Property MoneyValue1() As Double` [R/W] The monetary value for condition 1. Field name: MnyVal1.
- `Public Property MoneyValue2() As Double` [R/W] The monetary value for condition 2. Field name: MnyVal2.
- `Public Property MoneyValue3() As Double` [R/W] The monetary value for condition 3. Field name: MnyVal3.
- `Public Property MoneyValue4() As Double` [R/W] The monetary value for condition 4. Field name: MnyVal4.
- `Public Property MoneyValue5() As Double` [R/W] The monetary value for condition 5. Field name: MnyVal5.
- `Public Property NumberValue1() As Long` [R/W] The numeric value for condition 1. Field name: NumVal1.
- `Public Property NumberValue2() As Long` [R/W] The numeric value for condition 2. Field name: NumVal2.
- `Public Property NumberValue3() As Long` [R/W] The numeric value for condition 3. Field name: NumVal3.
- `Public Property NumberValue4() As Long` [R/W] The numeric value for condition 4. Field name: NumVal4.
- `Public Property NumberValue5() As Long` [R/W] The numeric value for condition 5. Field name: NumVal5.
- `Public Property StringValue1() As String` [R/W] The string value for condition 1. Field name: StrVal1.
- `Public Property StringValue2() As String` [R/W] The string value for condition 2. Field name: StrVal2.
- `Public Property StringValue3() As String` [R/W] The string value for condition 3. Field name: StrVal3.
- `Public Property StringValue4() As String` [R/W] The string value for condition 4. Field name: StrVal4.
- `Public Property StringValue5() As String` [R/W] The string value for condition 5. Field name: StrVal5.
- `Public Property TaxCode() As String` [R/W] The tax code that is proposed in sales or purchasing documents, if the tax code determination rule applies. You can use one of the tax codes defined in the application or create a new one. Field name: LnTaxCode. Length: 8 characters.
- `Public Property UDFAlias1() As String` [R/W] The alias of the user-defined field for condition 1. Field name: UDFAlias1.
- `Public Property UDFAlias2() As String` [R/W] The alias of the user-defined field for condition 2. Field name: UDFAlias2.
- `Public Property UDFAlias3() As String` [R/W] The alias of the user-defined field for condition 3. Field name: UDFAlias3.
- `Public Property UDFAlias4() As String` [R/W] The alias of the user-defined field for condition 4. Field name: UDFAlias4.
- `Public Property UDFAlias5() As String` [R/W] The alias of the user-defined field for condition 5. Field name: UDFAlias5.
- `Public Property UDFTable1() As String` [R/W] The title of the user-defined field for condition 1. Field name: UdfTable1.
  - remarks: To see details of the user-defined field in SAP Business One application, choose Tools --> Customization Tools --> User-Defined Fields - Management.
- `Public Property UDFTable2() As String` [R/W] The title of the user-defined field for condition 2. Field name: UdfTable2.
- `Public Property UDFTable3() As String` [R/W] The title of the user-defined field for condition 3. Field name: UdfTable3.
- `Public Property UDFTable4() As String` [R/W] The title of the user-defined field for condition 4. Field name: UdfTable4.
- `Public Property UDFTable5() As String` [R/W] The title of the user-defined field for condition 5. Field name: UdfTable5.

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
