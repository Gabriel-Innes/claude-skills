<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BOEInstruction (Object)

A data structure object holding properties for the BOEInstructionsService.

## Properties (4)
- `Public Property InstructionCode() As String` [R/W] Sets or returns a string specifying the instruction code. Field name: InstrCode.
- `Public Property InstructionDesc() As String` [R/W] Sets or returns a string specifying the instruction description. Field name: InstrDespt.
- `Public Property InstructionEntry() As Long` [R] Returns a number specifying the instruction entry. Field name: AbsEntry.
- `Public Property IsCancelInstruction() As BoYesNoEnum` [R/W] property IsCancelInstruction

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the string of the XML data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
