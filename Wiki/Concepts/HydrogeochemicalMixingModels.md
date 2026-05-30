---
tags:
  - "concept"
topics:
  - "AquaticAndFluvialCarbonCycling"
status: stable
created: 2026-05-26
updated: 2026-05-30
sources:
  - "Raw/Sources/Boral-2021epsl.md"
  - "Raw/Sources/Caraco-2010ecol.md"
  - "Raw/Sources/Hossler-2012jgr.md"
  - "Raw/Sources/Genereux-2009wrr.md"
  - "Raw/Sources/Doran-2014lo.md"
  - "Raw/Sources/GonzalezMoguel-2021jgr.md"
source_count: 6
aliases:
  - "Geochemical mixing models"
  - "Multi-tracer mixing models"
  - "Tributary contribution modeling"
---

# Hydrogeochemical Mixing Models for Source Apportionment

## Core Concept

Hydrogeochemical mixing models combine elemental concentrations and isotope ratios to quantify the fractional contributions of multiple water sources to a mixed system. By measuring conservative tracers (elements that don't precipitate or undergo chemical transformation) and isotope ratios that vary among source waters, researchers can solve systems of linear mixing equations to determine what fraction of discharge derives from each tributary, aquifer, or seasonal source. This approach is particularly powerful when combined with spatio-temporal data, allowing scientists to track how source contributions vary on timescales from days to seasons in response to rainfall, discharge, and hydrology.

## Multi-Tracer Framework

**Traditional Dual-Tracer Systems:**
- Two independent tracers (e.g., δ¹⁸O and electrical conductivity) constrain three-component mixing
- Requires solving a system of two equations with three unknowns, necessitating simplifying assumptions
- Useful for preliminary source apportionment when end-member compositions are well-characterized

**High-Resolution Multi-Tracer Systems:**
- Strontium concentration ([Sr]) and isotope ratio (⁸⁷Sr/⁸⁶Sr) provide two independent constraints from a single element
- Each tributary has a characteristic Sr concentration derived from lithology and weathering intensity
- Each tributary has a characteristic ⁸⁷Sr/⁸⁶Sr reflecting the age and mineralogy of rocks being weathered
- Together, [Sr] and ⁸⁷Sr/⁸⁶Sr can constrain two-component mixing exactly or three-component mixing when combined with a third tracer

**Validation Through Covariance:**
- When multiple tracers are measured in the same samples, their covariation provides internal validation
- If mixing is truly linear and conservative, different tracer pairs should yield consistent source apportionments
- Discrepancies reveal non-conservative processes (e.g., in-stream chemical reactions, mineral precipitation-dissolution)

## Application to River Systems

In large rivers with multiple tributaries and high spatio-temporal variability:

**Identifying Tributary Signatures:**
- Major tributaries are sampled to establish end-member [Sr] and ⁸⁷Sr/⁸⁶Sr compositions
- Literature values can supplement field measurements where direct sampling is impractical
- Seasonal variability in end-member compositions is quantified through repeated sampling

**Modeling Discharge-Driven Source Changes:**
- Rainfall or discharge data provides a time-dependent constraint on how much water is contributed by each tributary
- High discharge in one tributary dilutes downstream Sr concentrations and shifts ⁸⁷Sr/⁸⁶Sr toward that tributary's signature
- Spatio-temporal models predict both [Sr] and ⁸⁷Sr/⁸⁶Sr as time-weighted mixtures of tributary compositions

**Detecting Secondary Processes:**
- In-stream interactions (sediment-water equilibration, mineral dissolution) can alter dissolved Sr concentrations and isotope ratios
- Depth-specific sampling reveals whether reactions occur uniformly through the water column or are concentrated at the sediment interface
- Particulate Sr measurements show whether sorption-desorption processes fractionate dissolved Sr from sediments

## Advantages Over Single-Tracer Approaches

- **Increased specificity:** Two independent constraints from one element outperform single-tracer systems
- **Reduced assumptions:** Multiple tracers allow testing whether mixing is linear and conservative
- **Sensitivity to secondary processes:** Divergence between tracer predictions reveals in-stream chemical reactions
- **Better uncertainty quantification:** Multiple tracer pairs can be compared to estimate confidence intervals

## See also

- [[StrontiumIsotopeVariabilityRivers]] — Application to Ganga-Brahmaputra river system
- [[IsotopicProxiesPaleoceanography]] — Isotopic tracers in paleoceanographic contexts
- [[CompoundSpecificIsotopeAnalysis]] — Multi-tracer approaches to compound identification
- [[LocalVsDistalBiomarkerSignals]] — Spatial integration of geochemical signals
- Source paper: [[Boral-2021epsl]] — Hydrogeochemical mixing model for dissolved strontium isotope variations; [[Caraco-2010ecol]] — Aged carbon subsidies in aquatic food webs; [[Hossler-2012jgr]] — Time-varying isotope mixing models for northeastern rivers; [[Genereux-2009wrr]] — Groundwater and magmatic carbon mixing; [[Doran-2014lo]] — Antarctic lake radiocarbon mixing; [[GonzalezMoguel-2021jgr]] — Thermokarst lake carbon source mixing
