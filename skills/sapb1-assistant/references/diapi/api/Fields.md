<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Fields (Collection)

The Fields object is a collection of Field objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of fields in the collection.

## Methods (1)
- `Public Function Item(ByVal Index As Variant) As Field` Retrieves a Field object by its position or by its alias.
  - param `Index`: Sets the field retrieval method by position or by alias (starts from 0).
  - returns: If the index value is wrong (for example, the value does not exist), the method fails and throws an exception.
