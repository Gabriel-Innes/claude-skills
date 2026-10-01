<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Command (Object)

The Command object enables to run SQL stored procedures located in the company database. This object is called by the Recordset object.

## Properties (2)
- `Public Property Name() As String` [R/W] Sets or returns the name of the stored procedure.
  - remarks: After setting the Name property, the object's parameters are immediatly filled with the associated parameters of the stored procedure.
- `Public Property Parameters() As CommandParams` [R] Returns the CommandParams child object.

## Methods (1)
- `Public Sub Execute()` Executes the stored procedure with the Parameters.
  - remarks: If the stored procedure uses a SELECT statement the Recordset is filled with the returned parameters. Otherwise, the stored procedure returns an Out Parameter.
