<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TranslationsInUserLanguages (Object)

TranslationsInUserLanguages is a child object of the MultiLanguageTranslations object. It enables to set, in each row, a translated content in a specified user language. Source table: MLT1.

## Properties (5)
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property KeyFromHeaderTable() As Long` [R] Returns the key of the translated field value. Field name: TranEntry.
- `Public Property LanguageCodeOfUserLanguage() As Long` [R/W] Sets or returns the user language code. This code must be one of the codes defined in the UserLanguages object. Field name: LangCode.
- `Public Property Translationscontent() As String` [R/W] Sets or returns the translated content for the specified field (KeyFromHeaderTable). Lentgh: 64,000 characters. Field name: Trans.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
