# Dictionary index

| Path | Covers | Sage 300 versions | Verified |
|---|---|---|---|
| `conventions.md` | How Sage stores data in SQL Server; view-writing rules; join map; worked example | all | 2026-09 |
| `7.3A/table-index.md` | 1,264 tables, one line each, by module (28 modules; adds EI eInvoicing and EC eInvoicing-Singapore, T4/W-2 2025 payroll tables) | **7.3A = Sage 300 2026** | 2026-09-23 |
| `7.3A/dict/<MODULE>.md` | Per-table fields, types, keys, enum values | as above | 2026-09-23 |
| `7.2A/table-index.md` | 1,220 tables, 26 modules (export is 2025 PU1) | **7.2A = Sage 300 2025** | 2026-09-23 |
| `7.2A/dict/<MODULE>.md` | Per-table fields, types, keys, enum values | as above | 2026-09-23 |
| `7.1A/table-index.md` | 1,220 tables, 26 modules | **7.1A = Sage 300 2024** | 2026-09-23 |
| `7.1A/dict/<MODULE>.md` | Per-table fields, types, keys, enum values | as above | 2026-09-23 |
| `7.0A/table-index.md` | 1,218 tables, one line each, by module (26 modules incl. multi-contacts ARCUSC/APVENC, TS/TW/TM tax add-ons) | **7.0A = Sage 300 2023**; use for 2023 clients (the conservative subset for 2019–2022) | 2026-09-23 |
| `7.0A/dict/<MODULE>.md` | Per-table fields, types, keys, enum values | as above | 2026-09-23 |
| `6.0A/table-index.md` | 1,265 tables incl. MF (manufacturing add-on) and CSAPP | 6.0A (2012) — for legacy 6.x clients only | 2026-09 |
| `6.0A/dict/<MODULE>.md` | Per-table fields, types, keys, enum values | as above | 2026-09 |

## Version map

| Sage 300 year | AOM version | Dictionary folder |
|---|---|---|
| 2026 | 7.3A | `7.3A/` |
| 2025 | 7.2A | `7.2A/` |
| 2024 | 7.1A | `7.1A/` |
| 2023 | 7.0A | `7.0A/` |
| 2019–2022 | 6.6A–6.9A | use 7.0A and check fields, or 6.0A for the conservative subset |
| 6.0A–6.5A (pre-2018) | 6.0A–6.5A | `6.0A/` |

Selection rule: use the folder matching the client's version; otherwise the closest **older** one and say so.
Notable 6.0A → 7.0A additions on core tables: OEORDD.REQUESDATE; ICITEM.TARIFFCODE/SEASONAL/DEFBOMNO/PREVENDTY;
ICILOC.LEADTIME/QTYMINREQ; ARCUS.BRN/CATEGORY; APVEN.BRN; new multi-contact tables ARCUSC/APVENC. 6.0A carries the
MF* manufacturing tables, which are a separate add-on and absent from the 7.0A export.

Notable 7.0A → 7.1A (2023 → 2024): 2 new tables (ASAUDT, TSEFAUD); no fields added or removed; APCLX.CATEGORY (1099
amount type) gains the 1099-INT/OID codes 3xxx; UPCOBK.BANKFORMAT drops the empty value 25.

Notable 7.1A → 7.2A (2024 → 2025): no new tables; fields added only on APVEN (FATCA, FIRSTNAME, LASTNAME, SECONDTIN,
TAXWHSTTE), CPEMPL/UPEMPL (EMPLERDENT, PAYERDENT, WLCOUNTY) and CT T4/R1 tables. **Type change:** payroll cheque and
transaction numbers widened from `BCD*5.0` to `BCD*8.0` (DECIMAL(9,0) → DECIMAL(15,0)) on CP/UP CHKH/CHKL/CHKS/ACCO/ETRN/MC*
(CHECKNUM, TRANSNUM) — payroll views/integrations that declare these as INT or DECIMAL(9,0) must be widened. CPCHKH/UPCHKH.SERIAL
type is blank (`???`) in the 2025 and 2026 exports.

Notable 7.2A → 7.3A (2025 → 2026): 44 new tables (EI*/EC* eInvoicing, payroll year-end); fields added on CP/UP ACCO/DTLM,
CTT4PD, CTTXTYMP/UTTXTYMP (W2CODE), ICOPT.ULASTDEP; UTW2PD.REPORTID1/2 widened String*16 → String*20.

Cumulative 7.0A → 7.3A (verified by field diff 2026-09-23): **additive — no tables or fields removed** (only the payroll
type widenings above).
46 new tables: EI* (16, eInvoicing — Peppol, with MSIC classification codes i.e. the Malaysia flavour) and EC* (20, eInvoicing for Singapore / AGD),
plus payroll year-end tables CTR1PH, CTT4AH, CTT4PH, TSRECONH/TSRECOND, TSEFAUD, TMEXID, UTW2PH, ASAUDT, CSCBONBD.
32 fields added on existing tables, none on the core OE/IC/AR/PO/GL transaction or master tables: APVEN.FATCA/FIRSTNAME/LASTNAME/SECONDTIN/TAXWHSTTE
(1099/vendor tax); ICOPT.ULASTDEP; payroll CP*/UP*/CT*/UT* (MAXONBEGN, ATACCMAX, EMPLERDENT, PAYERDENT, WLCOUNTY,
W2CODE, CPENSION2C/QPENSION2C ...). OEORDH, OEORDD, OESHIH, OEINVH, ICITEM, ICILOC, ARCUS, POPORH1, GLAMF are
identical between 7.0A and 7.3A, so views on those tables written against 7.0A run unchanged on 2026.

