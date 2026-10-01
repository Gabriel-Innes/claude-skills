<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Recordset (Object)

Recordset is a raw data access object that enables you to select data from the database, navigate through the result set, and manipulate user tables, which are not exposed by the DI API. The main method of this object is DoQuery that enables you to run SQL queries with any DML action in its query string.

**Remarks:** Browsing Mechanisms The Recordset object includes two browsing mechanisms: the first mechanism applies to result sets that contain only one row (by the use of Select Top), which will retrieve only one record each time. Otherwise, the browsing will be performed on existing result set only. DML Operations on Database Tables The Recordset object allows the following Data Manipulation Language (DML) operations: UPDATE, INSERT, and DELETE. DML operations are acceptable with the Recordset object for user tables only. For other business objects use only the relevant DI objects and not the Recordset object. Any DML operations on system tables pose a high risk for data corruption, and will not be supported. Use at your own risk. Before the Recordset object executes an SQL query, it validates the user permission (same user permission as in SAP Business One). Otherwise, the SQL query is blocked. Blocking DDL Actions The following Data Definition Language (DDL) actions are blocked: CREATE, DROP, ALTER, and TRUNCATE. The reason for that is, when upgrading the SAP Business One application, it ignores user tables that are not created using the DI meta data objects (UserTablesMD and UserFieldsMD). Limitation Only one expression can be specified in the select list when the sub-query is not introduced with EXISTS. Related Topics Selecting Data Using the Recordset Object Retrieving a Field of a Recordset

## Properties (6)
- `Public Property BoF() As Boolean` [R] Returns a Boolean value that indicates whether or not the current row is the first row in the result set (Beginning of File).
  - remarks: The property indicates if there is a record before the current record. If the property returns Yes, the current record is the first record of the table. If both Bof and Eof properties return True, there are no records in the table.
- `Public Property Command() As Command` [R] Returns the Command object that enables to execute SQL stored procedures.
- `Public Property EoF() As Boolean` [R] Returns a Boolean value that indicates whether or not the current row is the last row in the result set (End of File).
  - remarks: The property indicates if there is a record after the current record. If the property returns Yes, the current record is the last record of the table. If both Bof and Eof properties return True, there are no records in the table.
- `Public Property Fields() As Fields` [R] Returns a Fields collection, which contains the fields of the result set.
- `Public Property RecordCount() As Long` [R] Returns the number of records contained in the result set.
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

## Methods (10)
- `Public Sub DoQuery(ByVal QueryStr As String)` Runs SQL queries.
  - param `QueryStr`: Specifies a query string, which contains the SQL query commands you want to run.
  - returns: -2000 ODBC Error.
  - remarks: If the method is successful, the object will contain the returned query result set. Note: As of SAP Business One 10.0, the DoQuery function can access the current logon company DB only. If you access Common DB, the DoQuery function will throw exception. Limitation: Only one expression can be specified in the select list when the subquery is not introduced with EXISTS. Other limitations includes the following query usage: - Nested Query - Query with Union and Union ALL - Using Like - Using Ali - Flow control statments (If / While / Break / Continue) - Calling procedures, fuctions, triggers and etc. - Distinct (i.e: "SELECT DISTINCT CardType FROM OCRD") - Multiple queries (i.e: Queries seperated with ; (semicolons) may not work, if there is no space before it)
  - example note: The following example shows the DoQuery and MoveNext methods.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim Count   As Long

    Dim FldName As String

    Dim FldVal  As String

    Dim i       As Long

    Dim RecSet  As SAPbobsCOM.Recordset

    Set RecSet = vCmp.GetBusinessObject(BoRecordset)

    RecSet.DoQuery ("select * from OADM")

    Count = RecSet.Fields.Count

      While RecSet.EOF = False

            'The inner loop runs over all the fields in one record (line) of the table

            For i = 0 To Count - 1

                FldName = RecSet.Fields.Item(i).Name

                FldVal = RecSet.Fields.Item(i).Value

                'Here you can manipulate the data as you want

            Next i

            'Move to the next record

            RecSet.MoveNext

      Wend
    ```
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetFixedSchema() As String` The schema for the XML returned by the GetFixedXML method.
- `Public Function GetFixedXML(ByVal xmlMode As RecordsetXMLModeEnum) As String` Returns the query data as XML based on a fixed schema. The GetAsXML also returns the data as XML, but the schema is dynamic and based on the specific query. With the GetFixedXML, the schema is fixed and is available with the GetFixedSchema method. You can use the schema, for example, to create a .NET object for handling the query XML. For more information, see Exchanging Data Using the DI API XML Capabilities.
  - param `xmlMode`: one of the enumeration's values (see the enum file)
  - enum: `../enums/RecordsetXMLModeEnum.md`
- `Public Sub MoveFirst()` Moves the curser to the first row in the result set.
  - returns: Exceptional error code: -1002 Invalid row.
- `Public Sub MoveLast()` Moves the curser to the last row in the result set.
  - returns: Exceptional error code: -1002 Invalid row.
- `Public Sub MoveNext()` Moves the curser to the next row in the result set.
  - returns: Exceptional error code: -1002 Invalid row.
- `Public Sub MovePrevious()` Moves the curser to the previous row in the result set.
  - returns: Exceptional error code: -1002 Invalid row.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the query data to an XML file or a string. For more information, see Exchanging Data Using the DI API XML Capabilities.
  - param `FileName`: Specifies the path and file name of the XML data.
  - remarks: The XML file that is created by the Recordset object can be read by any XML parser but not by the DI API. See Recordset sample.
