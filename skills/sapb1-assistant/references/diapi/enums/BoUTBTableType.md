<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BoUTBTableType (Enumeration)

Specifies the table types for user defined tables.

| Member | Value | Description |
|---|---|---|
| bott_NoObject | 0 | (Default) A No Object type refers to a user table that cannot be linked to a user defined object. The default table includes Code and Name fields only. |
| bott_MasterData | 1 | A Master Data type table refers to a collection of information about a person or an object, such as a cost object, business partner, or G/L account. For example, a business partner master record contains not only general information such as the business partner's name and address, but also specific information, such as payment terms and delivery instructions. Generally for end-users, master data is reference data that you will look up and use, but not create or change. |
| bott_MasterDataLines | 2 | A Master Data Lines type refers as a child of Master Data type. For example, list of addresses related to a business partner. |
| bott_Document | 3 | A Document type table refers to transactional data, which is data related to a single business event such as a purchase requisition or a request for payment. When you create a requisition, for example, SAP creates an electronic document for that particular transaction. SAP gives the transaction a document number and adds the document to the transaction data that is already in the system. Whenever you complete a transaction in SAP, that is, when you create, change, or print a document in SAP, this document number appears at the bottom of the screen. |
| bott_DocumentLines | 4 | A Document Lines type refers as a child of Document type. For example, Content tab in Invoice document. |
| bott_NoObjectAutoIncrement | 5 |  |

**Remarks:** For each user table type, SAP Business One provides a default table. You can add user fields to the default user fields but not remove them. For the default fields provided for each table type, see User Defined Object documentation. © Copyright 2022 SAP SE or an SAP affiliate company. All rights reserved.
