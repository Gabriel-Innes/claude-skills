<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# GeneralDataParams (Object)

Holds the keys to rows in database tables linked to a UDO data. This object is used to pass keys to and from GeneralService methods. Because it cannot be known the names of the properties that contain the key, properties of the GeneralDataParams object are set and retrieved with the generic SetProperty and GetProperty methods

## Methods (2)
- `Public Function GetProperty(ByVal bstrPropertyName As String) As Variant` Gets a property of the GeneralDataParams object.
  - param `bstrPropertyName`: The name of the property to be retrieved.
  - returns: The value of the property.
- `Public Sub SetProperty(ByVal bstrPropertyName As String, ByVal vtValue As Variant)` Sets a property of the GeneralDataParams object.
  - param `bstrPropertyName`: The name of the property to be set.
  - param `vtValue`: The new value for the property.
