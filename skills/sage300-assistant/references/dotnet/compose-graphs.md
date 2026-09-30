<!-- source: Sage 300 2026 (7.3A) AOM export, view composition lists | version: 7.3A = Sage 300 2026 | verified: 2026-09-25 -->

# Sage 300 core transaction documents - verified view-composition graphs

Machine-extracted from the 7.3A AOM view definitions (the ordered `Compositions` list per view). Use these to emit correct `OpenView(...)` + `Compose(...)` C# for the core documents without guessing or macro-recording. Composition of core OE/IC/AR/AP/PO/GL documents is stable across 7.0A-7.3A; confirm on the client's install if in doubt. For any document NOT listed here, macro-record the UI (view-api.md section 7).

How to read a block: open every view in the list, then for each `rotoID: [slots]` line call that view's `.Compose(new View[]{ ... })` passing, in the given order, the View variable for each opened rotoID and `null` for every `-` or `*` slot. Verify field names in `references/dictionary/7.3A/dict/<MODULE>.md`.

### OE Order - root `OE0520` (OE, verified 7.3A / Sage 300 2026)
Header view `OE0520` Orders (protocol: Header, Key auto generate; tables OEORDH, OEORDH1).

Open these views (rotoID - main table - title):
  OE0520  OEORDH    Orders
  OE0500            Order Details
  OE0180            Order Comments/Instructions
  OE0740            Order Payment Schedules
  OE0526            Order from Quotes
  OE0522            Order Optional Fields
  OE0501            Order Detail Optional Fields
  OE0503            Order BOM Details
  OE0502            Order Kitting Details
  OE0508            Order Detail Serial Numbers
  OE0507            Order Detail Lot Numbers
  OE0504            Order Kitting Serial Numbers
  OE0506            Order Kitting Detail Lot Numbers

Compose slots (array order = `Compose(new View[]{...})` order; `-` = GENSTUB -> null; `*` = cross-module/master, not opened -> null):
  OE0520: [OE0500, -, OE0180, OE0740, OE0526, OE0522]
  OE0500: [OE0520, OE0501, OE0503, OE0502, OE0508, OE0507]
  OE0180: [OE0520, OE0500]
  OE0740: [OE0520]
  OE0526: [OE0520]
  OE0522: [OE0520]
  OE0501: [OE0500]
  OE0503: [OE0500]
  OE0502: [OE0500, OE0504, OE0506]
  OE0508: [OE0500]
  OE0507: [OE0500]
  OE0504: [OE0502]
  OE0506: [OE0502]

### OE Invoice - root `OE0420` (OE, verified 7.3A / Sage 300 2026)
Header view `OE0420` Invoices (protocol: Header, Key auto generate; tables ).

Open these views (rotoID - main table - title):
  OE0420            Invoices
  OE0400            Invoice Details
  OE0160            Invoice Comments/Instructions
  OE0720            Invoice Payment Schedules
  OE0427            Multiple Shipments to Invoice
  OE0422            Invoice Optional Fields
  OE0401            Invoice Detail Optional Fields
  OE0403            Invoice BOM Details
  OE0402            Invoice Kitting Details
  OE0407            Invoice Detail Serial Numbers
  OE0406            Invoice Detail Lot Numbers
  OE0404            Invoice Kitting Serial Numbers
  OE0405            Invoice Kitting Detail Lot Numbers

Compose slots (array order = `Compose(new View[]{...})` order; `-` = GENSTUB -> null; `*` = cross-module/master, not opened -> null):
  OE0420: [OE0400, -, OE0160, OE0720, OE0427, OE0422]
  OE0400: [OE0420, OE0401, OE0403, OE0402, OE0407, OE0406]
  OE0160: [OE0420]
  OE0720: [OE0420]
  OE0427: [OE0420]
  OE0422: [OE0420]
  OE0401: [OE0400]
  OE0403: [OE0400]
  OE0402: [OE0400, OE0404, OE0405]
  OE0407: [OE0400]
  OE0406: [OE0400]
  OE0404: [OE0402]
  OE0405: [OE0402]

### OE Credit/Debit Note - root `OE0240` (OE, verified 7.3A / Sage 300 2026)
Header view `OE0240` Credit/Debit Notes (protocol: Header, Key auto generate; tables ).

Open these views (rotoID - main table - title):
  OE0240            Credit/Debit Notes
  OE0220            Credit/Debit Details
  OE0140            Crd/Dbn Comments/Instructions
  OE0242            Credit/Debit Note Opt. Fields
  OE0221            Credit/Debit Detail Opt. Fields
  OE0223            Credit/Debit BOM Details
  OE0222            Credit/Debit Kitting Details
  OE0227            Credit/Debit Detail Serial Nos
  OE0226            Credit/Debit Detail Lot Numbers
  OE0224            Credit/Debit Kitting Serial Nos
  OE0225            Credit/Debit Kitting Detail Lot Numbers

Compose slots (array order = `Compose(new View[]{...})` order; `-` = GENSTUB -> null; `*` = cross-module/master, not opened -> null):
  OE0240: [OE0220, -, OE0140, OE0242]
  OE0220: [OE0240, OE0221, OE0223, OE0222, OE0227, OE0226]
  OE0140: [OE0240]
  OE0242: [OE0240]
  OE0221: [OE0220]
  OE0223: [OE0220]
  OE0222: [OE0220, OE0224, OE0225]
  OE0227: [OE0220]
  OE0226: [OE0220]
  OE0224: [OE0222]
  OE0225: [OE0222]

### OE Shipment - root `OE0692` (OE, verified 7.3A / Sage 300 2026)
Header view `OE0692` Shipments (protocol: Header, Key auto generate; tables ).

Open these views (rotoID - main table - title):
  OE0692            Shipments
  OE0691            Shipment Details
  OE0190            Shipment Comments/Instructions
  OE0745            Shipment Payment Schedules
  OE0694            Multiple Orders to Shipment
  OE0704            Shipment Optional Fields
  OE0697            Shipment Day End Details
  OE0702            Shipment Detail Optional Fields
  OE0705            Shipment BOM Details
  OE0703            Shipment Kitting Details
  OE0709            Shipment Detail Serial Numbers
  OE0708            Shipment Detail Lot Numbers
  OE0699            Shipment Day End Details of Details
  OE0671            Shipment Day End Serials
  OE0670            Shipment Day End Lots
  OE0706            Shipment Kitting Serial Numbers
  OE0707            Shipment Kitting Detail Lot Numbers
  OE0676            Shipment Day End Kitting Serials
  OE0675            Shipment Day End Kitting Lots

Compose slots (array order = `Compose(new View[]{...})` order; `-` = GENSTUB -> null; `*` = cross-module/master, not opened -> null):
  OE0692: [OE0691, -, OE0190, OE0745, OE0694, OE0704]
  OE0691: [OE0692, OE0697, OE0702, OE0705, OE0703, OE0709, OE0708]
  OE0190: [OE0692, OE0691]
  OE0745: [OE0692]
  OE0694: [OE0692]
  OE0704: [OE0692]
  OE0697: [OE0698*, OE0699, OE0671, OE0670]
  OE0702: [OE0691]
  OE0705: [OE0691]
  OE0703: [OE0691, OE0706, OE0699, OE0707]
  OE0709: [OE0691, OE0671]
  OE0708: [OE0691, OE0670]
  OE0699: [OE0697, OE0676, OE0675]
  OE0671: [OE0697]
  OE0670: [OE0697]
  OE0706: [OE0703, OE0676]
  OE0707: [OE0703, OE0675]
  OE0676: [OE0699]
  OE0675: [OE0699]

### PO Purchase Order - root `PO0620` (PO, verified 7.3A / Sage 300 2026)
Header view `PO0620` Purchase Orders (protocol: Header, Key auto generate; tables POPORH1, POPORH2).

Open these views (rotoID - main table - title):
  PO0620  POPORH1   Purchase Orders
  PO0610            Purchase Order Comments
  PO0630            Purchase Order Lines
  PO0632            Purchase Order Requisitions
  PO0619            Purchase Order Functions
  PO0623            Purchase Order Hdr Opt. Fields
  PO0633            Purchase Order Det. Opt. Fields

Compose slots (array order = `Compose(new View[]{...})` order; `-` = GENSTUB -> null; `*` = cross-module/master, not opened -> null):
  PO0620: [PO0610, PO0630, PO0632, PO0619, PO0623]
  PO0610: [PO0620, PO0630]
  PO0630: [PO0620, PO0610, PO0619, PO0621*, PO0631*, PO0633]
  PO0632: [PO0620, PO0619]
  PO0619: [PO0620, PO0610, PO0630, PO0632]
  PO0623: [PO0620]
  PO0633: [PO0630]

### PO Receipt - root `PO0700` (PO, verified 7.3A / Sage 300 2026)
Header view `PO0700` Receipts (protocol: Header, Key auto generate; tables PORCPH1, PORCPH2).

Open these views (rotoID - main table - title):
  PO0700  PORCPH1   Receipts
  PO0695            Receipt Comments
  PO0710            Receipt Lines
  PO0718            Receipt Vendors
  PO0714            Receipt Additional Costs
  PO0699            Receipt Functions
  PO0705            Receipt Purchase Orders
  PO0703            Receipt Optional Fields
  PO0696            Receipt Cost Distributions
  PO0717            Receipt Detail Optional Fields
  PO0789            Receipt Line Lots
  PO0780            Receipt Line Serials
  PO0721            Receipt Vendors Optional Fields
  PO0719            Receipt Add. Cost Opt. Field

Compose slots (array order = `Compose(new View[]{...})` order; `-` = GENSTUB -> null; `*` = cross-module/master, not opened -> null):
  PO0700: [PO0695, PO0710, PO0718, PO0714, PO0699, PO0705, PO0703, PO0696]
  PO0695: [PO0700, PO0710]
  PO0710: [PO0700, PO0695, PO0699, PO0701*, PO0711*, PO0717, PO0789, PO0780]
  PO0718: [PO0700, PO0714, PO0699, PO0721]
  PO0714: [PO0718, PO0699, PO0700, PO0701*, PO0715*, PO0719, PO0696]
  PO0699: [PO0700, PO0695, PO0710, PO0714, PO0718, PO0705, PO0696]
  PO0705: [PO0700, PO0699]
  PO0703: [PO0700]
  PO0696: [PO0714, PO0718, PO0700, PO0699, PO0697*]
  PO0717: [PO0710]
  PO0789: [PO0710, PO0711*, PO0781*]
  PO0780: [PO0710, PO0711*, PO0788*]
  PO0721: [PO0718]
  PO0719: [PO0714]

### PO Invoice - root `PO0420` (PO, verified 7.3A / Sage 300 2026)
Header view `PO0420` Invoices (protocol: Header, Key auto generate; tables POINVH1, POINVH2).

Open these views (rotoID - main table - title):
  PO0420  POINVH1   Invoices
  PO0416            Invoice Comments
  PO0430            Invoice Lines
  PO0440            Invoice Additional Costs
  PO0436            Invoice Payment Schedules
  PO0419            Invoice Functions
  PO0438            Invoice Receipts
  PO0444            Inv. Add. Costs Superview
  PO0423            Invoice Optional Fields
  PO0415            Invoice Cost Distributions
  PO0433            Invoice Detail Optional Fields
  PO0819            Invoice Line Lots
  PO0810            Invoice Line Serials
  PO0443            Invoice Add. Cost Opt. Fields

Compose slots (array order = `Compose(new View[]{...})` order; `-` = GENSTUB -> null; `*` = cross-module/master, not opened -> null):
  PO0420: [PO0416, PO0430, PO0440, PO0436, PO0419, PO0438, PO0444, PO0423, PO0415]
  PO0416: [PO0420, PO0430]
  PO0430: [PO0420, PO0419, PO0421*, PO0431*, PO0433, PO0819, PO0810]
  PO0440: [PO0420, PO0419, PO0421*, PO0441*, PO0438, PO0444, PO0443, PO0415]
  PO0436: [PO0420, PO0419]
  PO0419: [PO0420, PO0416, PO0430, PO0436, PO0440, PO0438, PO0444, PO0415]
  PO0438: [PO0420, PO0419]
  PO0444: [PO0420, PO0419, PO0421*, PO0441*, PO0440, PO0438, PO0430]
  PO0423: [PO0420]
  PO0415: [PO0440, PO0420, PO0419, PO0417*]
  PO0433: [PO0430]
  PO0819: [PO0430, PO0431*, PO0818*]
  PO0810: [PO0430, PO0431*, PO0811*]
  PO0443: [PO0440]

### PO Return - root `PO0731` (PO, verified 7.3A / Sage 300 2026)
Header view `PO0731` Returns (protocol: Header, Key auto generate; tables PORETH1, PORETH2).

Open these views (rotoID - main table - title):
  PO0731  PORETH1   Returns
  PO0729            Return Comments
  PO0735            Return Lines
  PO0730            Return Functions
  PO0738            Return Optional Fields
  PO0739            Return Detail Optional Fields
  PO0799            Return Line Lots
  PO0790            Return Line Serials

Compose slots (array order = `Compose(new View[]{...})` order; `-` = GENSTUB -> null; `*` = cross-module/master, not opened -> null):
  PO0731: [PO0729, PO0735, PO0730, PO0738]
  PO0729: [PO0731, PO0735]
  PO0735: [PO0731, PO0729, PO0730, PO0732*, PO0736*, PO0739, PO0799, PO0790]
  PO0730: [PO0731, PO0729, PO0735, PO0799, PO0790]
  PO0738: [PO0731]
  PO0739: [PO0735]
  PO0799: [PO0735, PO0736*, PO0798*]
  PO0790: [PO0735, PO0736*, PO0791*]

### PO Credit/Debit Note - root `PO0311` (PO, verified 7.3A / Sage 300 2026)
Header view `PO0311` Credit/Debit Notes (protocol: Header, Key auto generate; tables POCRNH1, POCRNH2).

Open these views (rotoID - main table - title):
  PO0311  POCRNH1   Credit/Debit Notes
  PO0309            Credit/Debit Note Comments
  PO0315            Credit/Debit Note Lines
  PO0320            CR/DR Note Additional Costs
  PO0310            Credit/Debit Note Functions
  PO0325            CR/DR Add. Costs Superview
  PO0314            Credit/Debit Note Opt. Fields
  PO0326            CR/DR Note Cost Distributions
  PO0318            CR/DR Note Line Optional Fields
  PO0829            Credit/Debit Note Line Lots
  PO0820            Credit/Debit Note Line Serials
  PO0323            CR/DR Note Add. Cost Opt. Fields

Compose slots (array order = `Compose(new View[]{...})` order; `-` = GENSTUB -> null; `*` = cross-module/master, not opened -> null):
  PO0311: [PO0309, PO0315, PO0320, PO0310, PO0325, PO0314, PO0326]
  PO0309: [PO0311, PO0315]
  PO0315: [PO0311, PO0309, PO0310, PO0312*, PO0316*, PO0318, PO0829, PO0820]
  PO0320: [PO0311, PO0310, PO0312*, PO0321*, PO0325, PO0323, PO0326]
  PO0310: [PO0311, PO0309, PO0315, PO0320, PO0316*, PO0325, PO0326, PO0829, PO0820]
  PO0325: [PO0311, PO0310, PO0312*, PO0321*, PO0320, PO0315]
  PO0314: [PO0311]
  PO0326: [PO0320, PO0311, PO0310, PO0327*]
  PO0318: [PO0315]
  PO0829: [PO0315, PO0316*, PO0828*]
  PO0820: [PO0315, PO0316*, PO0821*]
  PO0323: [PO0320]

### IC Adjustment - root `IC0120` (IC, verified 7.3A / Sage 300 2026)
Header view `IC0120` Adjustment Headers (protocol: Header, Key auto generate; tables ).

Open these views (rotoID - main table - title):
  IC0120            Adjustment Headers
  IC0110            Adjustment Details
  IC0125            Adjustment Header Opt. Fields
  IC0370            Locations
  IC0290            Location Details
  IC0750            Units of Measure
  IC0260            Receipt Cost
  IC0115            Adjustment Detail Opt. Fields
  IC0117            Adjustment Detail Serial Numbers
  IC0113            Adjustment Detail Lot Numbers

Compose slots (array order = `Compose(new View[]{...})` order; `-` = GENSTUB -> null; `*` = cross-module/master, not opened -> null):
  IC0120: [IC0110, IC0125]
  IC0110: [IC0120, IC0310*, IC0370, IC0290, IC0750, GL0001*, IC0260, IC0115, IC0117, IC0113]
  IC0125: [IC0120]
  IC0370: [GL0021*, IC0290]
  IC0290: [IC0310*, IC0370, IC0750]
  IC0750: [IC0310*]
  IC0260: [IC0290]
  IC0115: [IC0110]
  IC0117: [IC0110]
  IC0113: [IC0110]

### IC Transfer - root `IC0740` (IC, verified 7.3A / Sage 300 2026)
Header view `IC0740` Transfer Headers (protocol: Header, Key auto generate; tables ).

Open these views (rotoID - main table - title):
  IC0740            Transfer Headers
  IC0730            Transfer Details
  IC0741            Transfer Optional Fields
  IC0750            Units of Measure
  IC0370            Locations
  IC0290            Location Details
  IC0100            Account Sets
  IC0735            Transfer Detail Optional Fields
  IC0738            Transfer Detail Serial Numbers
  IC0733            Transfer Detail Lot Numbers

Compose slots (array order = `Compose(new View[]{...})` order; `-` = GENSTUB -> null; `*` = cross-module/master, not opened -> null):
  IC0740: [IC0730, IC0741]
  IC0730: [IC0740, IC0310*, IC0750, IC0370, IC0290, IC0100, IC0735, IC0738, IC0733]
  IC0741: [IC0740]
  IC0750: [IC0310*]
  IC0370: [GL0021*, IC0290]
  IC0290: [IC0310*, IC0370, IC0750]
  IC0100: [GL0001*]
  IC0735: [IC0730]
  IC0738: [IC0730]
  IC0733: [IC0730]

### IC Inventory Shipment - root `IC0640` (IC, verified 7.3A / Sage 300 2026)
Header view `IC0640` Shipment Headers (protocol: Header, Key auto generate; tables ).

Open these views (rotoID - main table - title):
  IC0640            Shipment Headers
  IC0630            Shipment Details
  IC0390            Price List Codes
  IC0645            Shipment Optional Fields
  IC0750            Units of Measure
  IC0370            Locations
  IC0290            Location Details
  IC0635            Shipment Detail Optional Fields
  IC0632            Shipment Detail Lot Numbers
  IC0636            Shipment Detail Serial Numbers
  IC0395            Price List Code Tax Authorities
  IC0392            Price List Codes Checks

Compose slots (array order = `Compose(new View[]{...})` order; `-` = GENSTUB -> null; `*` = cross-module/master, not opened -> null):
  IC0640: [IC0630, IC0390, IC0645]
  IC0630: [IC0640, IC0310*, IC0750, IC0210*, IC0370, IC0290, IC0390, IC0635, IC0632, IC0636]
  IC0390: [IC0395, IC0392]
  IC0645: [IC0640]
  IC0750: [IC0310*]
  IC0370: [GL0021*, IC0290]
  IC0290: [IC0310*, IC0370, IC0750]
  IC0635: [IC0630]
  IC0632: [IC0630]
  IC0636: [IC0630]
  IC0395: [IC0390, TX0002*, TX0001*]
  IC0392: [IC0390]

### IC Inventory Receipt - root `IC0590` (IC, verified 7.3A / Sage 300 2026)
Header view `IC0590` Receipt Headers (protocol: Header, Key auto generate; tables ).

Open these views (rotoID - main table - title):
  IC0590            Receipt Headers
  IC0580            Receipt Details
  IC0595            Receipt Optional Fields
  IC0750            Units of Measure
  IC0370            Locations
  IC0290            Location Details
  IC0585            Receipt Detail Optional Fields
  IC0587            Receipt Detail Serial Numbers
  IC0582            Receipt Detail Lot Numbers

Compose slots (array order = `Compose(new View[]{...})` order; `-` = GENSTUB -> null; `*` = cross-module/master, not opened -> null):
  IC0590: [IC0580, IC0595]
  IC0580: [IC0590, IC0310*, IC0750, IC0210*, IC0370, IC0290, IC0585, IC0587, IC0582]
  IC0595: [IC0590]
  IC0750: [IC0310*]
  IC0370: [GL0021*, IC0290]
  IC0290: [IC0310*, IC0370, IC0750]
  IC0585: [IC0580]
  IC0587: [IC0580]
  IC0582: [IC0580]

### IC Internal Usage - root `IC0288` (IC, verified 7.3A / Sage 300 2026)
Header view `IC0288` Internal Usage Headers (protocol: Header, Key auto generate; tables ).

Open these views (rotoID - main table - title):
  IC0288            Internal Usage Headers
  IC0286            Internal Usage Details
  IC0289            Internal Usage Optional Fields
  IC0287            Internal Usage Detail Optional Fields
  IC0284            Internal Usage Serial Numbers
  IC0750            Units of Measure
  IC0370            Locations
  IC0290            Location Details
  IC0282            Internal Usage Lot Numbers

Compose slots (array order = `Compose(new View[]{...})` order; `-` = GENSTUB -> null; `*` = cross-module/master, not opened -> null):
  IC0288: [IC0286, IC0289]
  IC0286: [IC0288, IC0287, IC0284, IC0310*, IC0750, IC0210*, IC0370, IC0290, IC0282]
  IC0289: [IC0288]
  IC0287: [IC0286]
  IC0284: [IC0286]
  IC0750: [IC0310*]
  IC0370: [GL0021*, IC0290]
  IC0290: [IC0310*, IC0370, IC0750]
  IC0282: [IC0286]

### AR Invoice Batch - root `AR0031` (AR, verified 7.3A / Sage 300 2026)
Header view `AR0031` Invoice Batches (protocol: Batch, Key auto generate; tables ).

Open these views (rotoID - main table - title):
  AR0031            Invoice Batches
  AR0032            Invoices
  AR0033            Invoice Details
  AR0034            Invoice Payment Schedules
  AR0402            Invoice Optional Fields
  AR0160            Customer Balances
  AR0401            Invoice Detail Optional Fields

Compose slots (array order = `Compose(new View[]{...})` order; `-` = GENSTUB -> null; `*` = cross-module/master, not opened -> null):
  AR0031: [AR0032]
  AR0032: [AR0031, AR0033, AR0034, AR0402, AR0160]
  AR0033: [AR0032, AR0031, AR0401]
  AR0034: [AR0032]
  AR0402: [AR0032]
  AR0160: []
  AR0401: [AR0033]

### AR Receipt/Adjustment Batch - root `AR0041` (AR, verified 7.3A / Sage 300 2026)
Header view `AR0041` Receipt and Adjustment Batches (protocol: Batch, Key auto generate; tables ).

Open these views (rotoID - main table - title):
  AR0041            Receipt and Adjustment Batches
  AR0042            Receipts/Adjustments
  AR0043            Miscellaneous Receipts
  AR0044            Applied Receipts/Adjustments
  AR0406            Receipt/Adjustment Optional Fields
  AR0170            Advance Credits
  AR0085            Receipt Tax Withholdings
  AR0045            Adjustment G/L Distributions
  AR0061            Create Open Document List

Compose slots (array order = `Compose(new View[]{...})` order; `-` = GENSTUB -> null; `*` = cross-module/master, not opened -> null):
  AR0041: [AR0042]
  AR0042: [AR0041, AR0043, AR0044, AR0406, AR0170, AR0085]
  AR0043: [AR0042]
  AR0044: [AR0042, AR0045, AR0061]
  AR0406: [AR0042]
  AR0170: [AR0042]
  AR0085: [AR0042]
  AR0045: [AR0044]
  AR0061: [AR0041, AR0042, AR0043, AR0044, AR0045]

### AP Invoice Batch - root `AP0020` (AP, verified 7.3A / Sage 300 2026)
Header view `AP0020` Invoice Batches (protocol: Batch, Key auto generate; tables ).

Open these views (rotoID - main table - title):
  AP0020            Invoice Batches
  AP0021            Invoices
  AP0022            Invoice Details
  AP0023            Invoice Payment Schedules
  AP0402            Invoice Optional Fields
  AP0401            Invoice Detail Optional Fields

Compose slots (array order = `Compose(new View[]{...})` order; `-` = GENSTUB -> null; `*` = cross-module/master, not opened -> null):
  AP0020: [AP0021]
  AP0021: [AP0020, AP0022, AP0023, AP0402]
  AP0022: [AP0021, AP0020, AP0401]
  AP0023: [AP0021]
  AP0402: [AP0021]
  AP0401: [AP0022]

### AP Payment/Adjustment Batch - root `AP0030` (AP, verified 7.3A / Sage 300 2026)
Header view `AP0030` Payment and Adjustment Batches (protocol: Batch, Key auto generate; tables ).

Open these views (rotoID - main table - title):
  AP0030            Payment and Adjustment Batches
  AP0031            Payments/Adjustments
  AP0032            Miscellaneous Payments
  AP0033            Applied Payments
  AP0406            Payment/Adjustment Optional Fields
  AP0170            Advance Credits
  AP0069            Payment Tax Withholdings
  AP0034            Adjustment G/L Distributions
  AP0048            Create Open Document List

Compose slots (array order = `Compose(new View[]{...})` order; `-` = GENSTUB -> null; `*` = cross-module/master, not opened -> null):
  AP0030: [AP0031]
  AP0031: [AP0030, AP0032, AP0033, AP0406, AP0170, AP0069]
  AP0032: [AP0031]
  AP0033: [AP0031, AP0034, AP0048]
  AP0406: [AP0031]
  AP0170: [AP0031]
  AP0069: [AP0031]
  AP0034: [AP0033]
  AP0048: [AP0030, AP0031, AP0032, AP0033, AP0034]

### GL Journal Entry Batch - root `GL0008` (GL, verified 7.3A / Sage 300 2026)
Header view `GL0008` Batches (protocol: Batch, Key auto generate; tables ).

Open these views (rotoID - main table - title):
  GL0008            Batches
  GL0006            Journal Headers
  GL0010            Journal Details
  GL0402            Journal Detail Optional Fields

Compose slots (array order = `Compose(new View[]{...})` order; `-` = GENSTUB -> null; `*` = cross-module/master, not opened -> null):
  GL0008: [GL0006]
  GL0006: [GL0008, GL0010]
  GL0010: [GL0006, GL0402]
  GL0402: [GL0010]
