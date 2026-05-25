---
tags:
  - "concept"
topics: []
status: stable
created: 2026-05-25
updated: 2026-05-25
sources:
  - "Raw/Sources/Hemingway-2022gca.md"
source_count: 1
aliases:
  - "Sulfoxyanion fractionation"
  - "Isotope fractionation factors"
  - "Sulfite fractionation"
  - "Thiosulfate fractionation"
  - "Sulfoxylate fractionation"
---

# Sulfoxyanion Isotope Effects

Many important sulfur redox reactions in both biotic and abiotic environments proceed through intermediate sulfoxyanion species—including sulfite (SO₃²⁻, SO₂(OH)⁻), sulfoxylate (SO₂²⁻), and thiosulfate (S₂O₃²⁻)—which may rapidly exchange oxygen atoms with surrounding water. These intermediate species have distinct equilibrium oxygen isotope fractionation factors (¹⁸α and ¹⁷α) relative to water, meaning they fractionate isotopes differently than the stable sulfate products typically preserved in geological records. Understanding these fractionation factors is essential for mechanistically interpreting sulfate [[TripleOxygenIsotopes|triple-oxygen isotope]] compositions in both modern and ancient sulfur-cycle processes.

## Computational Predictions of Fractionation Factors

Equilibrium oxygen isotope fractionation factors for short-lived sulfoxyanion intermediates cannot be measured directly through traditional experimentation, as these species are difficult to isolate and analyze. Instead, quantum computational chemistry—specifically density functional theory (DFT) with appropriate methodological choices—can theoretically estimate ¹⁸α and ¹⁷α values.

**Computational methodology:**
- DFT calculations using B3LYP/6-31G+(d,p) functional as the primary computational method
- Higher-order methods (CCSD/aug-cc-pVTZ and MP2/aug-cc-pVTZ) used to derive redox state-specific scaling factors
- Anharmonic zero-point energy (ZPE) corrections estimated qualitatively using gaseous sulfoxy compounds
- ZPE corrections are relatively small (≤1‰) at Earth-surface temperatures

**Methodological sensitivity:**
Computational method choice significantly impacts ¹⁸α predictions. The inclusion of appropriate scaling factors based on redox state (particularly from higher-order CCSD calculations) improves agreement with experimental data. In contrast, ZPE corrections have minimal impact at Earth-surface conditions.

## Fractionation Factors for Individual Species

Different sulfoxyanion species of the same redox state (e.g., protonated vs. deprotonated forms) exhibit distinct fractionation factors. This species-specific behavior is particularly important because oxygen isotope fractionation is often controlled by the dominant species at a given pH, rather than by the bulk solution average.

**Sulfate species:**
- Theoretical bulk-solution ¹⁸α values have RMSE = 4.5‰ compared to experimental data (n = 18 conditions)
- When comparing only to SO₃(OH), experimental agreement improves to RMSE = 1.6‰
- Indicates that a single dominant sulfate species controls fractionation rather than an average of all species

**Sulfite species:**
- Bulk-solution RMSE = 3.7‰ (n = 27 experimental conditions)
- Improves to RMSE = 2.2‰ when comparing only to SO₂(OH) predictions
- Improvement is particularly pronounced at high and low pH where SO₂(OH) is not the dominant species

**Thiosulfate species:**
- Smallest RMSE of 2.2‰ (n = 3 experimental conditions)
- Fewer experimental constraints available compared to sulfate and sulfite systems

## Triple-Oxygen Isotope Anomalies (Δ¹⁷O)

By combining ¹⁸α and ¹⁷α predictions, calculations reveal the magnitude of mass-independent Δ¹⁷O fractionation. At Earth-surface temperatures (reference line slope = 0.5305):

- **Sulfate species:** Δ¹⁷O values up to 0.199‰ more negative than equilibrated water
- **Sulfite species:** Δ¹⁷O up to 0.205‰ more negative than water
- **Sulfoxylate species:** Δ¹⁷O up to 0.101‰ more negative than water
- **Thiosulfate species:** Δ¹⁷O up to 0.186‰ more negative than water

These Δ¹⁷O offsets are crucial for interpreting sulfate triple-oxygen isotope records because different intermediate species generate different isotopic signatures during formation.

## Applications in Sulfur-Cycle Processes

Fractionation factors for sulfoxyanions are essential for interpreting sulfate isotope records in processes including:

- **Pyrite oxidation:** Formation of sulfate through oxidation of pyrite (FeS₂), a major process in continental weathering
- **Microbial sulfate reduction:** Bacterial reduction of sulfate through sulfite and other intermediate species
- **Thiosulfate disproportionation:** Microbial metabolism producing both sulfate and sulfide from thiosulfate
- **Hydrothermal anhydrite precipitation:** Formation of hydrothermal sulfate minerals

By knowing how each intermediate species fractionates oxygen isotopes, researchers can quantitatively model sulfur redox pathways and constrain the specific metabolic processes occurring in modern environments or responsible for ancient isotope records.

## See also

- [[TripleOxygenIsotopes]] — Δ¹⁷O as paleoatmospheric tracer and sulfur-cycle proxy
- [[Hemingway-2022gca]] — Computational chemistry methods for fractionation factor predictions
