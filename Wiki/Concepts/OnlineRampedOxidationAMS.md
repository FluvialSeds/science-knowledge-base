---
tags:
  - "concept"
topics: []
status: stable
created: 2026-05-27
updated: 2026-05-27
sources:
  - "Raw/Sources/Bolandini-2025rad.md"
source_count: 1
aliases:
  - "ORO-AMS"
  - "Online ORO-DTI-AMS"
  - "Thermal dissection radiocarbon"
  - "Ramped oxidation AMS"
---

# Online Ramped Oxidation (ORO)-AMS for Radiocarbon Analysis

## Core Concept

Online ramped oxidation (ORO) coupled to accelerator mass spectrometry (AMS) enables rapid, sequential thermal dissection and radiocarbon dating of complex organic matter without requiring intermediate collection and offline processing steps. This advancement allows researchers to measure radiocarbon ages across a continuous temperature range, partitioning carbon pools by thermal stability and revealing how organic matter age varies with bond strength. The online ORO-AMS approach dramatically increases sample throughput while reducing contamination risks associated with offline methods.

## Instrumental Development and Design

**ORO-DTI-AMS system architecture:**
The online ORO-DTI (Direct To Injection) system couples a ramped pyrolysis-oxidation instrument directly to a gas ion source on the AMS. In this configuration:

- Sample is loaded into a precombusted reactor
- Ramped heating (typically 150–1000°C) oxidizes carbon sequentially by thermal stability
- CO₂ produced during heating is continuously quantified (via NDIR or similar detector)
- CO₂ fraction is transferred directly to the AMS ion source without offline cryogenic collection or chemical processing
- Radiocarbon measurement proceeds on the ionized CO₂

**Thermal fractionation and serial analysis:**
Unlike offline ORO where CO₂ from multiple temperature steps must be manually combined, online ORO enables measurement of individual thermal fractions or integrated multi-step fractions as needed. This provides:

- High-resolution radiocarbon ages across the entire thermal profile
- Quantification of age-versus-thermal-stability relationships
- Identification of multiple carbon pools (labile, resistant, refractory) with distinct ages

## Advantages Over Traditional Methods

**Increased throughput:**
Online ORO-AMS analysis on a single sample is 2–3 times faster than offline RPO-IRMS combined with separate radiocarbon measurement, enabling large-scale analytical programs.

**Reduced contamination:**
Elimination of offline handling reduces opportunities for blank carbon introduction. The closed-system online approach maintains sample integrity throughout analysis.

**Direct thermal-radiocarbon coupling:**
Simultaneous measurement of thermal release (CO₂ yield) and ¹⁴C/¹²C ratio reveals how radiocarbon age changes as a function of thermal stability, providing mechanistic insight into carbon preservation.

**Lower carbon requirements:**
The high efficiency of direct CO₂ ionization reduces minimum sample carbon requirements compared to some offline methods.

## Applications

**Complex organic matter characterization:**
ORO-AMS is particularly valuable for:

- **Soil and sediment**: Partitioning soil organic carbon pools by age and thermal stability to understand carbon residence times and preservation mechanisms
- **Marine sediments**: Determining ages of different lipid classes and kerogen fractions to reconstruct past carbon cycling
- **Atmospheric particulates**: Dating organic carbon components in aerosols to identify sources and atmospheric residence times
- **Archaeological materials**: Characterizing multiple carbon pools (charcoal, residual organics) separately to improve dating precision

**Coal and petrogenic carbon analysis:**
By measuring thermal fractions separately, ORO-AMS can identify whether petrogenic carbon contributions are homogeneous or heterogeneous in age, with implications for understanding exhumation and oxidation processes.

## Methodological Considerations

**Thermal fractionation kinetics:**
The order in which different organic compounds decompose depends on bond strength and activation energy. Compounds with weaker C-C or C-H bonds oxidize at lower temperatures, while highly condensed aromatics and refractory compounds oxidize only at high temperatures (>800°C). This thermal separation provides a first-order partitioning of carbon by preservation type.

**Radiocarbon interpretation across fractions:**
- **Low-temperature CO₂** (150–300°C): Typically shows modern or young radiocarbon, consistent with labile soil organics or fresh plant material
- **Intermediate-temperature CO₂** (300–600°C): Often shows intermediate ages reflecting semi-resistant carbon pools (degraded biopolymers)
- **High-temperature CO₂** (600–1000°C): Shows old radiocarbon ages, consistent with refractory carbon or petrogenic material

**Blank characterization:**
Blank carbon must be carefully quantified across the entire thermal range. Precombusted reactor blanks at NOSAMS average ~3.6 μg C with modern carbon isotope composition—adequate for most applications but critical to account for when analyzing small samples (<100 μg C total).

## Integration with Paleoclimate and Paleoceanographic Studies

Online ORO-AMS enables new approaches to understanding carbon cycling in paleoenvironmental contexts:

- **River suspended sediment**: Measuring radiocarbon ages of multiple thermal fractions reveals the relative contribution of young vegetation vs. old petrogenic carbon across discharge seasons
- **Lake sediment cores**: Age-versus-thermal-stability profiles constrain the timing and magnitude of past changes in carbon preservation and mobilization
- **Marine records**: Distinguishing ages of lipid biomarkers from different microbial sources using thermal fractionation improves paleoceanographic reconstructions

## See also

- [[RadiocarbonAnalyticalMethods]] — Overview of radiocarbon analysis techniques and blank corrections
- [[RampedPyrolysisOxidation]] — General RPO methodology and applications
- [[RadiocarbonOrganicMatter]] — Interpretation of radiocarbon ages as tracers of carbon cycling
- Source paper: [[Bolandini-2025rad]] — Development and characterization of online ORO-AMS
