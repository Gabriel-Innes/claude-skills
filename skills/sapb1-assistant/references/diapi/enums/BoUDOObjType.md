<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BoUDOObjType (Enumeration)

Specifies the object types for user defined objects.

| Member | Value | Description |
|---|---|---|
| boud_MasterData | 1 | A Master Data type object refers to a collection of information about a person or an object, such as a cost object, business partner, or G/L account. For example, a business partner master record contains not only general information such as the business partner's name and address, but also specific information, such as payment terms and delivery instructions. Generally for end-users, master data is reference data that you will look up and use, but not create or change. |
| boud_Document | 3 | A Document type object refers to transactional data, which is data related to a single business event such as a purchase requisition or a request for payment. When you create a requisition, for example, SAP creates an electronic document for that particular transaction. SAP gives the transaction a document number and adds the document to the transaction data that is already in the system. Whenever you complete a transaction in SAP, that is, when you create, change, or print a document in SAP, this document number appears at the bottom of the screen. |

**Remarks:** For details, see User Defined Object documentation. © Copyright 2022 SAP SE or an SAP affiliate company. All rights reserved.
