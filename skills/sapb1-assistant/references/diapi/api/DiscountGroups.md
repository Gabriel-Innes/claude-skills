<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DiscountGroups (Object)

Represents a set of item discounts for a specific business partner. Each business partner can be assigned a set of discounts, and each discount is associated with an item group, property, or manufacturer. If the business partner purchases an item that is associated with one of the specified groups, properties, or manufacturers, the business partner receives the corresponding discount. All of the ObjectEntry keys point to the same type of object -- either group (ItemGroups object), property (ItemProperties object), or manufacturer (Manufacturers object) -- depending on the DiscountBaseObject property of the BusinessPartners object. Source table: OEDG.

**Remarks:** If a business partner has one type of discount groups, for example for item groups, you can define any type of discount groups, for example for item manufacturers, as follows: - Change the DiscountBaseObject of the BusinessPartners object to the new type (for example, item manufacturers). - Add new rows to the DiscountGroups subobject of the BusinessPartners object. - Update the BusinessPartners object. All rows in the DiscountGroups subobject related to the previous type are automatically deleted. For a list of ways for setting discounts and special prices, see SpecialPrices.

## Properties (5)
- `Public Property BaseObjectType() As DiscountGroupBaseObjectEnum` [R] The value of the DiscountBaseObject property for the current object's parent business partner.
- `Public Property BPCode() As String` [R] The key to the current object's parent business partner.
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: Returns the total number of records for the current business partner. When adding a new row, the system increments the value of this property automatically.
- `Public Property DiscountPercentage() As Double` [R/W] The discount for a matching item, in percent. Field name: Discount
  - remarks: The value must be between 0 and 100.
- `Public Property ObjectEntry() As String` [R/W] The key to an item group, property, or manufacturer. Any item assigned to the group, property, or manufacturer is assigned the discount in the DiscountPercentage property. The key represents either an item group, property, or manufacturer depending on the DiscountBaseObject property of the current BusinessPartners object. Field name: ObjKey

## Methods (3)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oBP As SAPbobsCOM.BusinessPartners

    Dim oDiscountGroup As SAPbobsCOM.DiscountGroups

    oBP = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oBusinessPartners)

    oBP.GetByKey("C1")

    oBP.DiscountBaseObject = SAPbobsCOM.DiscountGroupBaseObjectEnum.dgboItemGroups

    oDiscountGroup = oBP.DiscountGroups

    oDiscountGroup.SetCurrentLine(0)

    oDiscountGroup.Delete()

    oBP.Update()
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
