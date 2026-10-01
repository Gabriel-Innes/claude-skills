<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BOEInstructionsService (Object)

This service manages instructions in SAP Business One. Mandatory properties: InstructionCode, InstructionDesc. Source table: OIST.

## Methods (8)
- `Public Function AddBOEInstruction(ByVal pIBOEInstruction As BOEInstruction) As BOEInstructionParams` Adds an Instruction with InstructionCode and InstructionDesc as specified in the BOEInstruction data structure.
  - param `pIBOEInstruction`: Specifies the BOE instruction to be added.
- `Public Sub DeleteBOEInstruction(ByVal pIBOEInstructionParams As BOEInstructionParams)` Deletes Instruction with InstructionEntry specified in BOEInstructionParams.
  - param `pIBOEInstructionParams`: BOEInstructionParams
- `Public Function GetBOEInstruction(ByVal pIBOEInstructionParams As BOEInstructionParams) As BOEInstruction` Returns an instance of the BOEInstruction data structure.
  - param `pIBOEInstructionParams`: BOEInstructionParams
- `Public Function GetBOEInstructionList() As BOEInstructionsParams` Returns a collection of instances for the BOEInstruction data structure.
- `Public Function GetDataInterface(ByVal enumMSDI As BOEInstructionsServiceDataInterfaces) As Object` Creates empty data structure. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/BOEInstructionsServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates data structure from specified XML file.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates data structure from specified XML string.
  - param `bstrXMLString`: XML string.
- `Public Sub UpdateBOEInstruction(ByVal pIBOEInstruction As BOEInstruction)` Replaces InstructionCode and InstructionDesc of Instruction with the specified BOEInstruction data structure.
  - param `pIBOEInstruction`: Specifies the BOE instruction to be updated.
