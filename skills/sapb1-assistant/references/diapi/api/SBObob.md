<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# SBObob (Object)

The SBObob object is raw data access object that enables you to retrieve information quickly and easily. The returned data is usually a Recordset object that enables data manipulation. See SBObob samples.

## Methods (29)
- `Public Function ConvertEnumValueToValidValue(ByVal enumName As String, ByVal enumValue As Long) As String` Converts a specified enumeration value of an enumeration name to the valid value defined in the company database. See Conversion sample.
  - param `enumName`: Enumeration name
  - param `enumValue`: Enumeration value.
- `Public Function ConvertValidValueToEnumValue(ByVal enumName As String, ByVal ValidValue As String) As Long` Converts a specified valid value of an enumeration name to the enumeration value defined in the company database. See Conversion sample.
  - param `enumName`: Enumeration name.
  - param `ValidValue`: Valid value.
- `Public Function Format_DateToString(ByVal inDate As Date) As Recordset` Converts the system date to a string. See Formatting sample.
  - param `inDate`: System date.
- `Public Function Format_MoneyToString(ByVal inMoney As Double, ByVal inPrecision As BoMoneyPrecisionTypes) As Recordset` Converts a specified amount of money to a string according to a specified precision. See Formatting sample.
  - param `inMoney`: Amount of money.
  - param `inPrecision`: one of the enumeration's values (see the enum file)
  - enum: `../enums/BoMoneyPrecisionTypes.md`
- `Public Function Format_StringToDate(ByVal inStr As String) As Recordset` Converts date string to a system date.
  - param `inStr`: Date as string.
- `Public Function GetAccountSegmentsByCode(ByVal AccountCode As String, ByVal AddSeperator As Boolean) As Recordset` Returns a Recordset object that contains the value of the FormatCode property for a specified AccountCode.
  - param `AccountCode`: Account code (Code) as assigned in SAP Business One when adding a G/L account with segments. For example, _SYS 00000000010.
  - param `AddSeperator`: Specifies whether or not to include a separator, such as - (dash), between the account segments. The separator is defined in SAP BUsiness One (Administration -->System Initialization --> General Settings --> Display tab).
- `Public Function GetBPList(ByVal CardType As BoCardTypes) As Recordset` Returns a Recordset object that contains a list of business partners keys that can be used as a parameter in many business objects. See Get Business Partners List sample.
  - param `CardType`: one of the enumeration's values (see the enum file)
  - returns: A Recordset object containing three fields : CardCode, CardName, and CardType.
  - enum: `../enums/BoCardTypes.md`
- `Public Function GetContactEmployees(ByVal CardCode As String) As Recordset` Returns a Recordset object that contains a list of contact employees for a specified business partner. See Get Contact Employees sample.
  - param `CardCode`: Specifies the business partner code for which you want to obtain contact employees.
- `Public Function GetCurrencyRate(ByVal Currency As String, ByVal Date As Date) As Recordset` Returns a Recordset object that contains the currency rate for a specified date and currency code. See Currency sample. Source table: ORTT.
  - param `Currency`: Specifies the currency code.
  - param `Date`: Specifies the date for the currency exchange rate.
  - returns: A Recordset object that contains one field named CurrencyRate that holds the rate value. SAP Business One returns 0 if the system cannot find the exchange rate. Exceptions -2000 The connection with the database has been disconnected.
  - remarks: You can use this method to query the exchange rate between any currency and the local currency. For example, if the local currency is US dollars, and you need the currency rate for EUR on January 10, 2002. Use the following line code: vObj.GetCurrencyRate("eur", Date("10.01.2002")) A result of 0.98 from the returned Recordset object means that on January 10, 2002 the exchange rate was 1 EUR = 0.98 USD.
- `Public Function GetDueDate(ByVal CardCode As String, ByVal refDate As Date) As Recordset` Returns the due date for a specified business partner based on the business partner code and the reference date. See Get Due Date sample.
  - param `CardCode`: Specifies the business partner code.
  - param `refDate`: Specifies the reference date.
  - returns: A Recordset object that contains one field named DueDate that holds the due date value. Exceptions -2000 The connection with the database has been disconnected.
  - remarks: When you create a document, you can use this method to get the due date of that document using the business partner code and document date. The due date is defined in the customer payment terms, in the business partner master record. You can change the due date when you create the document.
- `Public Sub GetEwaParameters(ByVal bstrKey As String, ByRef pbstrRsltEwaUserName As String, ByRef pbstrRsltEwaPassword As String)` Returns a Recordset that defines the Early Watch Alert user parameters: - EWA Key - User Name - User PassWord
  - param `bstrKey`: Specifies the Early Warning Alert Key.
  - param `pbstrRsltEwaUserName`: Specifies the Early Warning Alert User name.
  - param `pbstrRsltEwaPassword`: Specifies the Early Warning Alert User Password.
- `Public Function GetFieldValidValues(ByVal TableName As String, ByVal FieldName As String) As Recordset` Returns a Recordset object that contains the valid values of a specified field and table in the database. Each valid value includes its name and description. For example, the valid values for CardType field in OCRD table are: C - Customer, S - Supplier, and L - Lead.
  - param `TableName`: Table name in the database.
  - param `FieldName`: Field name in the database.
  - remarks: The following is a returned recordset that is saved in XML format: <?xml version="1.0" encoding="UTF-16"?> <BOM> <BO> <AdmInfo> <Object>-1</Object> </AdmInfo> <GENREC> <row> <Value>C</Value> <Description>Customer</Description> </row> <row> <Value>S</Value> <Description>Vendor</Description> </row> <row> <Value>L</Value> <Description>Lead</Description> </row> </GENREC> </BO> </BOM>
- `Public Function GetIndexRate(ByVal Index As String, ByVal Date As Date) As Recordset` Returns a Recordset object that contains the index rate for a specified date and index code. See Get Index Rate sample.
  - param `Index`: Specifies the index code.
  - param `Date`: Specifies the reference date.
  - returns: A Recordset object that contains one field named IndexRate that holds the index rate value. If the index does not exists, the system returns 0. Exceptions -2000 The connection with database has been disconnected.
  - remarks: SAP Business One supports multiple index rates. You can use these indexes in reporting sheet to help users to analyze business data.
- `Public Function GetItemList() As Recordset` Returns a Recordset object that contains an item code and item name. To retrieve the items list, apply this method in a loop. See Get Items List sample.
  - returns: A Recordset object that contains two fields: ItemCode and ItemName. Exceptions -2000 The connection with database has been disconnected.
  - remarks: For more detailed information about the item, you can create a new instance for the Items object, and then use the GetByKey method.
- `Public Function GetItemPrice(ByVal CardCode As String, ByVal ItemCode As String, ByVal amount As Double, ByVal Date As Date) As Recordset` Returns a Recordset object that contains the item price for specified business partner and item, based on the amount and transaction date. See Get Item Price sample.
  - param `CardCode`: Specifies the business partner code.
  - param `ItemCode`: Specifies the item code.
  - param `amount`: Specifies transaction quantity (number of units).
  - param `Date`: Specifies transaction date.
  - returns: A Recordset object that contains two fields: Price and Currency. The system returns 0, if a price is not found for the specified business partner and item. Exceptions -2000 The connection with database has been disconnected.
  - remarks: The item price consists on the following four factors: business partner, item, transaction amount, and transaction date. If the currency of the returned price is not the same currency as you use, use the GetCurrencyRate method to convert between currencies.
- `Public Function GetLicenseStatus(ByVal UserName As String, ByVal FormID As String) As Long` You can get the information whether a user has a license to access a form.
  - param `UserName`: The use name.
  - param `FormID`: The form ID. You can get the from ID from View → System Information.
  - remarks: Note: If either of the input parameter UserName or FormID is not valid, the returned value will not be accurate. This function can be called by any user. A super user can check any user, while a regular user can check his/her own user only. If a regular user tries to check a different user name, an error occurs: "You are not permitted to perform this action".
  - C# example (from SAP's help):
    ```csharp
    static void GetLicenseStatusDemo(Company oCompany)
            {
                SAPbobsCOM.SBObob oSBObob = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.BoBridge);
                try
                {
                    int retValue1 = oSBObob.GetLicenseStatus("manager", "1320000000"); //2

                }
                catch (Exception ex)
                {
                    Console.Write(ex.ToString());
                    return;
                }

            }
    ```
- `Public Function GetLocalCurrency() As Recordset` Returns the local currency defined in the company database. See Currency sample.
  - returns: A Recordset object containing one field named LocalCurrency that holds the local currency code. Exceptions -2000 The connection with database has been disconnected.
- `Public Function GetObjectKeyBySingleValue(ByVal ObjNum As BoObjectTypes, ByVal PropName As String, ByVal Value As String, ByVal Condition As BoQueryConditions) As Recordset` Returns a Recordset object that contains the object key by single value. See Get Object Key By Single Value sample.
  - param `ObjNum`: one of the enumeration's values (see the enum file)
  - param `PropName`: Property name of the selected object.
  - param `Value`: Value for the specified property.
  - param `Condition`: one of the enumeration's values (see the enum file)
  - enum: `../enums/BoObjectTypes.md`
- `Public Function GetObjectPermission(ByVal Object As BoObjectTypes) As Recordset` Returns a single record that contains the permission type (BoPermission) of a specified PermissionId and UserSignature.
  - param `Object`: one of the enumeration's values (see the enum file)
  - enum: `../enums/BoObjectTypes.md`
- `Public Function GetSystemCurrency() As Recordset` Returns the system currency defined in the company database. See Currency sample.
  - returns: A Recordset object that contains one field: SystemCurrency that holds the system currency code. Exceptions -2000 The connection with database has been disconnected.
- `Public Function GetSystemPermission(ByVal UserName As String, ByVal PermissionID As String) As Recordset` Returns the permission for a type of permission for a specific user.
  - param `UserName`: A user code
  - param `PermissionID`: A permission ID A list of permissions is available at Permissions List.
  - returns: One of the following values: 1: Read/Write 2: Read only 3: Not authorized 4: Various authorizations 6: Not defined
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oSBObob As SAPbobsCOM.SBObob

    Dim oRecordSet As SAPbobsCOM.Recordset

    '// Get an initialized SBObob object

    oSBObob = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.BoBridge)

    '// return the General permission (142) for the manager

    oRecordSet = oSBObob.GetSystemPermission("manager", "142")

    '// Print permission value (Read/Write=1, ReadOnly=2, NoAuthorization=3,

    '// VariousAuthorization=4, NotDefined=6)

    Debug.WriteLine(oRecordSet.Fields.Item(0).Value())
    ```
- `Public Function GetTableFieldList(ByVal TableName As String) As Recordset` Returns a Recordset object that contains the fields list of a specified table in the database. Each field includes the following parameters (the examples in parenthesis relates to OCRD: CardCode): - Name (CardCode) - Type (nvarchar) -- a numeric value representing a BoFieldTypes enumeration value - Length (15) - Linked table name for foreign key (GroupCode) - Valid values indicator, which indicates whether or not this field uses valid values (no) - IsNullable -- specifies whether or not nulls are permitted
  - param `TableName`: Table name in the database.
  - remarks: The following is a returned recordset that is saved in XML format: <?xml version="1.0" encoding="UTF-16"?> <BOM> <BO> <AdmInfo> <Object>-1</Object> </AdmInfo> <GENREC> <row> <FieldName>CardCode</FieldName> <FieldLength>15</FieldLength> <FieldType>0</FieldType> <IsNullable>0</IsNullable> <IsValidValues>0</IsValidValues> <LinkedTo/> </row> <row> <FieldName>CardName</FieldName> <FieldLength>100</FieldLength> <FieldType>0</FieldType> <IsNullable>0</IsNullable> <IsValidValues>0</IsValidValues> <LinkedTo/> </row> </GENREC> </BO> </BOM>
- `Public Function GetTableList() As Recordset` Returns a Recordset object that contains a list of all the tables in the database. Each table includes its name and description (for example: OCRD, Business Partner.
  - remarks: The following is a returned recordset that is saved in XML format: <?xml version="1.0" encoding="UTF-16"?> <BOM> <BO> <AdmInfo> <Object>-1</Object> </AdmInfo> <GENREC> <row> <row> <Alias>ACRD</Alias> <Description>Business Partner - History</Description> </row> <row> <Alias>ADO1</Alias> <Description>A/R Invoice (Rows) - History</Description> </row> <row> . . . <row> <Alias>WTR9</Alias> <Description>Stock Transfer - Base Docs Details</Description> </row> </row> </GENREC> </BO> </BOM>
- `Public Function GetUserList() As Recordset` Returns a recordset that contains a list of user codes defined in the SAP Business One company database.
  - remarks: Exceptions -2000 The connection with database has been disconnected.
- `Public Function GetValidValueDescription(ByVal ObjNum As BoObjectTypes, ByVal ObjectName As String, ByVal PropertyName As String, ByVal enumValue As Long) As String` Returns a string that contains the valid value description of a valid value.
  - param `ObjNum`: one of the enumeration's values (see the enum file)
  - param `ObjectName`: Object name.
  - param `PropertyName`: Property name of the selected object.
  - param `enumValue`: Enumeration value.
  - enum: `../enums/BoObjectTypes.md`
- `Public Function GetWareHouseList() As Recordset` Returns a Recordset object that contains the warehouse code and name defined the company database. To retrieve a list of warehouses, apply this method in a loop. See Get Warehouse List sample.
  - returns: A Recordset object that contains two fields: WareHouseCode and WareHouseName. Exceptions -2000 The connection with database has been disconnected.
- `Public Sub PutEwaParameters(ByVal bstrKey As String, ByVal bstrEwaUserName As String, ByVal bstrEwaPassword As String)` Sets a Recordset that contains the Early Watch Alert user parameters: - EWA Key - User Name - User PassWord
  - param `bstrKey`: Sets the Early Warning Alert Key.
  - param `bstrEwaUserName`: Sets the Early Warning Alert User name.
  - param `bstrEwaPassword`: Sets the Early Warning Alert User Password.
- `Public Sub SetCurrencyRate(ByVal Currency As String, ByVal Date As Date, ByVal Value As Double, Optional ByVal Update As Boolean = False)` Sets the exchange rate for a specified date and currency in the company database. See Currency sample.
  - param `Currency`: Specifies the target currency.
  - param `Date`: Specifies the date of the currency rate.
  - param `Value`: Specifies the rate of the target currency.
  - param `Update`: Specifies a value indicating whether or not to update the currency.
- `Public Sub SetSystemPermission(ByVal UserName As String, ByVal PermissionID As String, ByVal Permission As Long)` Sets the permission for a type of permission for a specific user.
  - param `UserName`: A user code
  - param `PermissionID`: A permission ID A list of permissions is available at Permissions List.
  - param `Permission`: A permission, which is one of the following: 1: Read/Write 2: Read only 3: Not authorized 4: Various authorizations 6: Not defined
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oSBObob As SAPbobsCOM.SBObob

    Dim oRecordSet As SAPbobsCOM.Recordset

    '// Get an initialized SBObob object

    oSBObob = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.BoBridge)

    '// Get an initialized Recordset object

    oRecordSet = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.BoRecordset)

    '//set the General permission to Read/Write(Read/Write=1 ,ReadOnly=2,NoAuthorization=3,

    '//VariousAuthorization=4,NotDefined=6)

    Call oSBObob.SetSystemPermission("manager", "142", 1)
    ```
