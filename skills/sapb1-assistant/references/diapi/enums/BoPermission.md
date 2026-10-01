<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BoPermission (Enumeration)

Specifies the permission type assigned to the user.

| Member | Value | Description |
|---|---|---|
| boper_Full | 1 | Full authorization (Read/Write). |
| boper_ReadOnly | 2 | Read only authorization. |
| boper_None | 3 | No authorization. |
| boper_Various | 4 | Various authorizations. Relevant when the node of the authorization tree contains few branches with different authorizations. For example, a user that has Full Authorization for Item Management form and Read Only for Price Lists form then the user permission for Inventory is Various Authorizations. |
| boper_Undefined | 6 | Authorization not defined. |
