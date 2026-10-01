<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BoFrequency (Enumeration)

Specifies the cycle interval options for inventory counts.

| Member | Value | Description |
|---|---|---|
| bof_Daily | 0 | Every day. |
| bof_Weekly | 1 | Every week (in a specified Day in the week). Used also for order interval planning. |
| bof_Every4Weeks | 2 | Every four weeks (in a specified Day in the week). |
| bof_Monthly | 3 | Every month (in a specified Day in the month). Used also for order interval planning. |
| bof_Quarterly | 4 | Quarterly. |
| bof_HalfYearly | 5 | Every half year. |
| bof_Annually | 6 | Every year. |
| bof_OneTime | 7 | Single time. |
| bof_EveryXDays | 8 | Every X days. You must specify also the number of days in the Day property. Used for order interval planning. |
