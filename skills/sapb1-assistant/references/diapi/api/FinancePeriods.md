<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# FinancePeriods (Collection)

FinancePeriods is a collection of FinancePeriod objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the total number of FinancePeriod in the FinancePeriods Collection .

## Methods (5)
- `Public Function Add() As FinancePeriod` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As FinancePeriod` Retrieves an existing FinancePeriod item from the FinancePeriods collection by its index.
  - param `vtIndex`: Specifies the index of the FinancePeriod item to be retrieved.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
