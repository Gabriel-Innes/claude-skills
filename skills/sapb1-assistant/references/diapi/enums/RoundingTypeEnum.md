<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# RoundingTypeEnum (Enumeration)

Methods for rounding of withholding tax calculations.

| Member | Value | Description |
|---|---|---|
| rt_TruncatedAU | 0 | The tax amount is truncated and appears without decimals. Relevant for a penalty withholding tax. |
| rt_CommercialValues | 1 | The value is rounded according to the decimal amount as follows: - 1 to 49 cents is rounded down. - 50 to 99 cents is rounded up. Relevant for voluntary withholding tax. |
| rt_NoRounding | 2 |  |

**Remarks:** Relevant for Australia and New Zealand only. © Copyright 2022 SAP SE or an SAP affiliate company. All rights reserved.
