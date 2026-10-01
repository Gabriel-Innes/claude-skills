<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Field (Object)

The Field object contains both standard and custom data access properties. This object enables you to manipulate the field data.

**Remarks:** All of the properties, except ValidValue and Value, are read only.

## Properties (13)
- `Public Property DefaultValue() As String` [R] Returns the field default value.
- `Public Property Description() As String` [R] Returns the field description (when available).
  - remarks: Use this property only when you link it to a UserFields object.
- `Public Property FieldID() As Long` [R] Returns the field ID.
- `Public Property LinkedTable() As String` [R] Returns the table name linked to the field.
- `Public Property Mandatory() As BoYesNoEnum` [R] Returns a valid value of BoYesNoEnum type that specifies whether or not this field is mandatory in SAP Business One.
- `Public Property Name() As String` [R] Returns the field name.
- `Public Property Size() As Long` [R] Returns the actual field size.
- `Public Property SubType() As BoFldSubTypes` [R] Returns a valid value of BoFldSubTypes type that specifies the sub-type of the field as defined in the SubType property of the UserFieldsMD object.
- `Public Property Table() As String` [R] property Table
- `Public Property Type() As BoFieldTypes` [R] Returns the field data type as defined in the Type property of the UserFieldsMD object.
- `Public Property ValidValue() As String` [R/W] Sets or returns the actual value of the field (instead of the SQL query value).
- `Public Property ValidValues() As ValidValues` [R] Returns the ValidValues object.
- `Public Property Value() As Variant` [R/W] Sets or returns the field SQL query value.

## Methods (2)
- `Public Function IsNull() As BoYesNoEnum` Returns true (Y) if the field is null and false (N) if the field contains a non-null value.
  - remarks: To get the correct value of "IsNull", it is necessary to call the property Value of SAPbobsCOM.Fields object in order to update the current row of the RecordSet.
  - C# example (from SAP's help):
    ```csharp
    string Query = "SELECT NULL UNION SELECT 'THIS IS NOT NULL'";

    SAPbobsCOM.Recordset recordSet = (SAPbobsCOM.Recordset)SBO_Company.GetBusinessObject(SAPbobsCOM.BoObjectTypes.BoRecordset);
    recordSet.DoQuery(Query);
    recordSet.MoveFirst();
    recordSet.MoveNext(); // Skip the first row, goes directly to the row that is NOT NULL

    var item = recordSet.Fields.Item("0");
    var value = item.Value; // This operation updates the current row properties and it is required before using the IsNULL property.
    SAPbobsCOM.BoYesNoEnum isNull = item.IsNull(); // It returns NO. There's a Temporal Coupling behavior for the object SAPbobsCOM.Fields when moving through a RecordSet
    ```
- `Public Function SetNullValue() As Long` Sets the field value to Null.
