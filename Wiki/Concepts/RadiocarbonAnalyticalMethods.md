---
tags:
  - "concept"
topics: []
status: stable
created: 2026-05-25
updated: 2026-05-25
sources:
  - "Raw/Sources/Hemingway-2017rad.md"
source_count: 1
aliases:
  - "Radiocarbon measurement"
  - "Blank carbon correction"
  - "Radiocarbon analysis"
---

# Radiocarbon Analytical Methods

## Core Concept

Radiocarbon dating requires careful measurement of ¹⁴C/¹²C ratios and rigorous assessment of blank carbon contamination. Blank carbon—introduced during sample preparation, combustion, or analysis—directly compromises the accuracy of radiocarbon age determinations, particularly for samples with low carbon concentrations or high ages.

## Blank Carbon Sources and Correction

**Sources of blank carbon:**
- Precombusted reaction vessels and filters (residual carbon)
- Atmospheric contamination during sample handling
- Reagent impurities
- Instrument carry-over from previous analyses

**NOSAMS blank characterization:**
The NOSAMS (National Ocean Sciences AMS Facility) facility quantifies blank carbon contribution by analyzing empty, precombusted reactor inserts across the analytical temperature range (150–1000°C for ramped pyrolysis/oxidation). The NOSAMS RPO blank averages approximately 3.6 μg C with a modern (Fm = 0) isotope composition.

**Blank correction strategies:**
- **Isotope dilution method**: Correcting for blank carbon mass and isotope composition by comparing sample measurements to standard reference materials (SRM)
- **"Modern-dead" method**: Using dual-isotope corrections for both blank mass and blank isotope values
- **Measurement-based correction**: Directly measuring blank carbon evolution during the analytical procedure and subtracting its contribution

## Blank Carbon Impact on Age Determination

The impact of blank carbon scales inversely with sample size:
- **Large samples** (>100 μg C): Blank contribution typically <1% of total carbon, minimal age bias
- **Small samples** (<10 μg C): Blank carbon can represent >10% of measured signal, causing significant age bias
- **Radiocarbon-free blanks** (Δ¹⁴C = −1000‰): Artificially age modern samples by 1,000+ years per percent of blank contamination

## Kinetic Isotope Fractionation

During thermal analysis (such as [[RampedPyrolysisOxidation|RPO]]), kinetic isotope fractionation can occur—the preferential release of ¹²C vs ¹³C at different temperatures due to differences in bond-breaking kinetics. This fractionation must be accounted for to avoid biased stable isotope and radiocarbon measurements.

## Quality Assurance

**Critical measurements for method validation:**
- Replicate analysis of standard reference materials (SRM) to verify instrumental accuracy
- Parallel blank analyses to track contamination and verify correction methods
- Isotope mass balance checks to ensure ¹²C, ¹³C, and ¹⁴C measurements are internally consistent
- Comparison of multiple blank correction strategies to assess robustness

## See also

- [[RampedPyrolysisOxidation]] — Thermal analysis technique requiring blank correction
- [[RadiocarbonOrganicMatter]] — Application of corrected radiocarbon data to source partitioning
- [[CompoundSpecificIsotopeAnalysis]] — Analytical foundations for isotope measurements
- Source paper: [[Hemingway-2017rad]] — Detailed blank carbon assessment for NOSAMS RPO
