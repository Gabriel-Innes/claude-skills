<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BoConsumptionMethod (Enumeration)

Specifies the default methods for forecast consumption.

| Member | Value | Description |
|---|---|---|
| cm_BackwardForward | 0 | The system starts to subtract from the forecast of -X days (DaysBackward) and then continue with the forecast of +Y days (DaysForward). |
| cm_ForwardBackward | 1 | The system starts to subtract from the forecast of +Y days (DaysForward) and then continue with the forecast of -X days (DaysBackward). |
