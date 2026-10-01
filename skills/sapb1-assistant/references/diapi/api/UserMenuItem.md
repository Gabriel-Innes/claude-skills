<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# UserMenuItem (Object)

UserMenuItem is a Data structure related to the UserMenuService. Source table: CUMI.

## Properties (9)
- `Public Property LinkedFormMenuID() As Long` [R/W] Sets or returns the id of the Form linked to this menu item. Field name: FormMenuId.
- `Public Property LinkedFormNum() As Long` [R/W] Sets or returns the Form number of the linked Form. Field name: FormNum.
- `Public Property LinkedObjKey() As String` [R/W] Sets or returns the key of the object linked to this menu item. Field name: Key_. Length: 50 characters.
- `Public Property LinkedObjType() As String` [R/W] Sets or returns the type of the object linked to this menu item. Field name: Type_.
- `Public Property Name() As String` [R/W] Sets or returns this menu item name. Field name: Name_. Length: 100 characters.
- `Public Property Position() As Long` [R/W] Sets or returns the position of this menu item within the menu. Field name: SortNum.
- `Public Property ReportPath() As String` [R/W] Sets or returns the path of the report attached to this menu Item. Field name: RepPath.
- `Public Property Type() As UserMenuItemTypeEnum` [R/W] Returns a valid value that defines this menu item type. Field name: Type_.
- `Public Property UserMenuItems() As UserMenuItems` [R/W] Sets or returns the UserMenuItems object, a data collection of UserMenuItem data structures.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
