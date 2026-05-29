---
tags:
  - "concept"
topics:
  - "IsotopicProxiesPaleoceanography"
status: stable
created: 2026-05-27
updated: 2026-05-29
sources:
  - "Raw/Sources/Bolandini-2025rad.md"
source_count: 1
aliases:
  - "Thermal dissection radiocarbon"
  - "Temperature-dependent radiocarbon ages"
  - "Bond-strength fractionation"
---

# Thermal Fractionation in Radiocarbon Dating

## Core Concept

Organic matter rarely comprises a single homogeneous carbon pool. Instead, complex organic materials contain multiple carbon components with different thermal stabilities (bond strengths), chemical structures, and ages. When organic matter is analyzed using [[RampedPyrolysisOxidation|ramped pyrolysis/oxidation (RPO)]] coupled to radiocarbon measurement, the radiocarbon ages obtained from different thermal fractions reveal how carbon age varies as a function of thermal stability. This thermal fractionation approach provides a powerful window into organic matter preservation mechanisms and the relative contributions of different carbon sources.

## Physical Basis: Thermal Stability and Bond Strength

**Decomposition kinetics:**
Organic compounds decompose when the thermal energy provided by heating exceeds the activation energy of the weakest bonds in the molecule. Compounds with weaker bonds (lower activation energy) decompose at lower temperatures; compounds with stronger bonds (higher activation energy) persist to higher temperatures.

**Common thermal decomposition temperature ranges:**
- **Low-temperature region (150–300°C)**: Labile organic compounds with weak bonds—recently synthesized biopolymers (polysaccharides, proteins), amino acids, and other compounds from fresh biomass
- **Intermediate-temperature region (300–600°C)**: Semi-resistant carbon—partially degraded biopolymers, modified lipids, and some refractory biopolymers that have undergone diagenetic alteration
- **High-temperature region (600–1000°C)**: Highly condensed aromatic structures—refractory kerogen, charcoal, and geological carbon resistant to oxidation

## Radiocarbon Age Patterns Across Thermal Fractions

**Low-temperature fractions (labile carbon):**
Typically display modern to young radiocarbon ages (Δ¹⁴C ≈ 0 to −200‰), consistent with recent primary production. In soil and sediment contexts, these fractions represent recently synthesized or rapidly cycling compounds. In Arctic river systems with active permafrost carbon mobilization, low-temperature fractions may show Δ¹⁴C values near 0‰ reflecting recently fixed vegetation.

**Intermediate-temperature fractions (semi-resistant carbon):**
Often show intermediate radiocarbon ages (Δ¹⁴C ≈ −300 to −800‰), reflecting carbon that has been stored in soils or sediments for years to centuries. These fractions represent degradation-resistant compounds like cutin, suberin, and modified lignin phenols. The age increase relative to labile carbon indicates slower cycling and enhanced preservation.

**High-temperature fractions (refractory carbon):**
Display old radiocarbon ages (Δ¹⁴C < −900‰, or equivalently, ages >10,000 radiocarbon years BP). These fractions contain highly condensed aromatic structures, charcoal, and potentially exhumed geological material. In many natural samples, high-temperature fractions are old enough to be essentially indistinguishable from radiocarbon-free (Δ¹⁴C = −1000‰), indicating residence times of multiple millennia.

## Interpretation Framework

**Single-source systems:**
If all carbon in a sample derives from a single source (e.g., pure soil from a single depth horizon), thermal fractionation patterns reflect the age-versus-thermal-stability structure of that single source. For example:
- Fresh plant material shows monotonically increasing age with increasing temperature (young labile → old refractory)
- Old soil might show uniformly old ages across all thermal fractions

**Multi-source systems:**
When a sample contains carbon from multiple sources with different ages (e.g., river suspended sediment containing both young vegetation and old petrogenic carbon), thermal fractionation can partially separate them:
- Young vegetation preferentially oxidizes at low temperatures
- Old petrogenic carbon preferentially oxidizes at high temperatures
- Intermediate-temperature regions may reflect mixing

This separation is imperfect (not a true quantitative source apportionment) but provides qualitative insight into source diversity.

## Applications to Understanding Organic Matter Cycling

**Soil carbon persistence:**
Comparison of thermal fractionation patterns in soils of different ages and climates reveals which thermal fractions are preferentially preserved. Highly weathered tropical soils show relatively old radiocarbon ages across all thermal fractions, suggesting that even labile-appearing carbon is actually stabilized through mineral protection or spatial inaccessibility.

**River suspended sediment dynamics:**
Thermal fractionation of suspended sediment radiocarbon ages responds to discharge and water source changes:
- **High discharge**: Erodes fresh hillslope soils, increasing proportion of young, low-temperature carbon
- **Low discharge**: Mobilizes deep groundwater and aged floodplain carbon, enriching high-temperature fractions with old carbon

**Marine sediment source apportionment:**
Thermal fractionation of marine organic matter helps distinguish terrigenous (land-derived) from marine/autochthonous sources:
- Terrigenous material typically shows more variable thermal fractionation (young + old components)
- Marine organic matter usually shows uniform young ages across all thermal fractions

**Paleoclimate and carbon cycle reconstruction:**
Changes in thermal fractionation patterns downcore in sediment archives record shifts in organic matter sources and preservation conditions through time, enabling reconstruction of past changes in carbon cycling rates and mechanisms.

## Limitations and Caveats

**Not a perfect separation:**
Thermal fractionation is based on thermal decomposition kinetics, which correlates imperfectly with carbon age. Some old carbon may oxidize at low temperatures (if structurally simple), and some young carbon may persist to high temperatures (if in dense aggregates). Thus thermal fractionation provides a first-order separation but is not equivalent to direct age-based chromatographic separation.

**Bulk ages within fractions:**
Even within a single thermal fraction, multiple carbon compounds with different ages are typically present and mixed. The reported radiocarbon age is a weighted average of all carbon in that fraction. High-resolution separation (e.g., coupling RPO to gas chromatography before radiocarbon measurement) can improve resolution.

**Contamination within fractions:**
Each thermal fraction must be characterized for blank carbon, which may vary across the temperature range due to differences in pretreatment effectiveness.

## See also

- [[OnlineRampedOxidationAMS]] — Modern analytical approach enabling direct thermal fractionation AMS measurement
- [[RampedPyrolysisOxidation]] — RPO methodology and thermal kinetics
- [[RadiocarbonOrganicMatter]] — General radiocarbon age interpretation
- [[RadiocarbonAnalyticalMethods]] — Analytical methods and blank corrections
- Source paper: [[Bolandini-2025rad]] — Online ORO-AMS application to thermal fractionation radiocarbon dating
