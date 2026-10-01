<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# CommandParam (Object)

CommandParam is a child object of the Command object and used to retrieve single parameter of the stored procedure.

## Properties (4)
- `Public Property Direction() As BoRecCommParamTypes` [R] Returns the direction of the parameter, In or Out. The Command object supports single Out parameter only.
- `Public Property Name() As String` [R] Returns the parameter name.
- `Public Property Type() As BoFieldTypes` [R] Returns the parameter field type.
- `Public Property Value() As Variant` [R/W] Sets or returns the parameter value.
