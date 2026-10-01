<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# RecordsetEx (Object)

RecordsetEx is a raw data access object that enables you to fetch data from the database table. The main method of this object is DoQuery, which lets you run SQL select queries in its query string.

**Remarks:** Browsing Mechanisms The RecordsetEx object includes two browsing mechanisms. The first mechanism applies to result sets that contain only one row (by the use of Select Top); it retrieves only one record each time. With the second mechanism, the browsing is performed on the existing result set only. Blocking DML Operations and DDL Actions The following Data Manipulation Language (DML) operations are blocked: UPDATE, INSERT, DELETE, TRUNCATE, UPSERT, REPLACE, and MERGE. The following Data Definition Language (DDL) operations are blocked: CREATE, DROP, ALTER, and RENAME. Limitation When the sub-query is not introduced with EXISTS, only one expression can be specified in the select list. As of SAP Business One 10.0, the DoQuery function can access the current logon company DB only. If you access Common DB, the DoQuery function will throw exception.

**Example:**
- C# example (from SAP's help):
  ```csharp
  SAPbobsCOM.RecordsetEx oRecordSetEx = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.BoRecordsetEx);

  oRecordSetEx.DoQuery("select \"CardCode\", \"CardName\" from OCRD");

  while (!oRecordSetEx.EoF)
   {
         SAPbobsCOM.BoFieldTypes type = oRecordSetEx. .GetColumnType(0);
         var value = oRecordSetEx.GetColumnValue(0);

         //By Alias
         //SAPbobsCOM.BoFieldTypes type = oRecordSetEx. GetColumnType("CardCode");
         //var value = oRecordSetEx. GetColumnValue("CardCode");

         oRecordSetEx.MoveNext();
   }
  ```

## Properties (3)
- `Public Property ColumnsCount() As Long` [R] Returns the column number of the result set.
- `Public Property EoF() As Boolean` [R] Returns a Boolean value that indicates whether or not the current row is the last row in the result set (End of File).
- `Public Property RecordSetAudit() As Boolean` [R/W] For security enhancement, if this flag is set to true, the querying will be logged in table RSAT. By default, the flag is set to false.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.Recordset oRecordSet = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.BoRecordset);
                SAPbobsCOM.RecordsetEx oRecordSetex = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.BoRecordsetEx);
                string query = ""select * from oitm"";
                oRecordSet.RecordSetAudit = true;
                oRecordSetex.RecordSetAudit = true;
                try
                {
                    oRecordSetex.DoQuery(query);
                    oRecordSet.DoQuery(query);
                }
                catch (Exception e)
                {
                    Console.WriteLine(e.Message);
                }
    ```

## Methods (4)
- `Public Sub DoQuery(ByVal QueryStr As String)` Runs SQL queries.
  - param `QueryStr`: Specifies a query string, which contains the SQL query commands you want to run.
- `Public Function GetColumnType(ByVal Index As Variant) As BoFieldTypes` Returns the column type by its position or by its alias.
  - param `Index`: index
- `Public Function GetColumnValue(ByVal Index As Variant) As Variant` Returns the column value by its position or by its alias.
  - param `Index`: index
- `Public Function MoveNext() As Boolean` Get next row data from query result; if it returns false, it means next row does not exist, else returns true.
