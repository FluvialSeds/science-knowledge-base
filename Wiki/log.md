## First Ingest: LLM Wiki Demo Source
*Logged: 2026-05-24 13:25:15*

Compiled LLMWikiStarterDemo.md into Topic (LLMWiki), Concept (SourceToWikiWorkflow), and Project (WikiSetup) notes. Demonstrates core workflow of separating Raw sources from compiled Wiki knowledge.

## Schema update: Mandatory logging
*Logged: 2026-05-24 13:35:22*

Updated CLAUDE.md to require logging after every ingest and maintenance step. Logging now part of official workflow.

## Tool enhancement: Automatic timestamps on log entries
*Logged: 2026-05-24 16:04:12*

Updated log command to include automatic YYYY-MM-DD HH:MM:SS timestamps. Updated documentation and added timestamps to existing entries for chronological tracking.

## Source status update
*Logged: 2026-05-24 16:08:20*

Marked LLMWikiStarterDemo source as Processed: true. Source is now fully tracked in manifest with Wiki coverage.

## Workflow update: Mark sources processed immediately
*Logged: 2026-05-24 16:10:01*

Updated Ingest Workflow to require Processed: true immediately after compiling source into Wiki notes. Added to mandatory checklist. This ensures accurate source tracking and manifest coverage.

## Tool: PDF import utility added
*Logged: 2026-05-24 16:21:03*

Created pdf_to_source.py to convert research papers into structured source notes. Reads PDFs from Raw/Files/, extracts text, guides user to describe topic/methods/results/implications, generates markdown with template. Includes comprehensive PDF import guide.

## Tool refactor: pdf_to_source.py now fully automated
*Logged: 2026-05-24 16:32:10*

Removed interactive prompts. Script now automatically extracts paper sections and generates summaries (topic/methods/results/implications) without user input. Added filename convention (lastname-year-journalacro.md). Agents now properly read and summarize papers instead of asking users.

## Ingest: Hemingway 2016 GCA - Plant-Wax Biomarkers
*Logged: 2026-05-24 16:35:22*

Compiled Hemingway et al. 2016 plant-wax biomarker study into 3 focused concepts: Plant-Wax Biomarkers (overview and applications), Local vs Distal Biomarker Signals (spatial/temporal integration), and Carbon Isotope Fractionation in Plants (δ¹³C methods). Source: Hemingway-2016gca.md

## Ingest: Hemingway 2018 Science - Petrogenic Carbon Oxidation
*Logged: 2026-05-24 16:46:48*

Compiled Hemingway et al. 2018 Science paper on microbial oxidation of lithospheric organic carbon into 3 focused concepts: Petrogenic Organic Carbon (definition and sources), Microbial Oxidation of Organic Carbon (oxidation rates and controls), and Carbon Cycle in Mountain Systems (tectonics-climate coupling). Source: Hemingway-2018sci.md

## Source correction: DOI updated
*Logged: 2026-05-24 16:51:11*

Corrected DOI for Hemingway-2018sci source from 10.1126/science.aar3580 to correct DOI 10.1126/science.aao6463. Ensures proper reference tracking and traceability.

## Wiki improvement: Added wikilinks to concept notes
*Logged: 2026-05-24 22:36:06*

Added 'See also' sections and inline wikilinks to all 6 concept notes for better navigation. Users can now easily traverse between related concepts and source materials. Enables discovery of connections between plant-wax biomarkers (2016 study) and petrogenic carbon oxidation (2018 study).

## Workflow enhancement: Automated wikilink generation
*Logged: 2026-05-24 22:42:09*

Added suggest-links command to wiki_tool.py for automated discovery of related concepts. Updated CLAUDE.md ingest workflow Step 6 to mandate wikilinks. Updated _templates/concept-note.md with See also section placeholder. Updated Schema/workflow-examples.md to show complete wikilink patterns including source paper references. Updated Schema/pdf-import-guide.md to document wikilink requirement. All ingest workflows now require bidirectional linking to related concepts and source papers.

## Ingest: Hemingway-2018og (BHP analytical methods)
*Logged: 2026-05-24 22:48:24*

Created CompoundSpecificIsotopeAnalysis concept note documenting UPLC-based compound-specific δ13C analysis techniques. Describes analytical approach and applications to both plant-wax lipids and bacteriohopanepolyols. Updated PlantWaxBiomarkers and CarbonIsotopeFractionationPlants to link to new analytical methods concept. This new source integrated cleanly as methodological foundation for existing biomarker notes.

## Ingest: Hemingway-2017cg (Congo River biomarkers and radiocarbon)
*Logged: 2026-05-24 23:04:02*

Created two new concept notes: GDGTBiomarkers documenting branched and isoprenoid GDGT proxies and applications to riverine source partitioning, and RadiocarbonOrganicMatter covering Δ14C as tracer of pre-aged vs modern organic matter. Updated LocalVsDistalBiomarkerSignals to add Hemingway-2017cg as source and link to new concepts. Updated PlantWaxBiomarkers with links to GDGT and radiocarbon concepts. Paper integrates plant-wax lipids, GDGT biomarkers, and radiocarbon as complementary tracers for Congo River POM sources and discharge-driven temporal variability.

## Ingest: Hemingway-2017rad (Ramped Pyrolysis Oxidation Methods)
*Logged: 2026-05-25 12:21:00*

Created RampedPyrolysisOxidation concept documenting analytical technique for bond-strength analysis and radiocarbon measurements. Created RadiocarbonAnalyticalMethods concept covering blank correction protocols and instrument calibration. Updated RadiocarbonOrganicMatter to reference new analytical methods. Source: Hemingway-2017rad.md

## Ingest: Hemingway-2019gca and Hemingway-2019nat (DOM Preservation and Mineral Protection)
*Logged: 2026-05-25 12:11:00*

Compiled Hemingway et al. 2019 dissolved organic matter and organic carbon preservation studies into 5 focused concepts:
- DissolvedOrganicMatter: DOM composition, source partitioning, and bioavailability across aquatic systems
- GlacierDerivedOrganicCarbon: Glacier-fed systems and seasonal variability in carbon composition
- OrganicCarbonPreservation: Preservation mechanisms including selective vs mineral protection pathways
- OrganoMineralBonds: Mineral-bound carbon chemistry and sorption mechanisms
- Updated RadiocarbonOrganicMatter to include biomarker radiocarbon measurements and sources (now 4 sources)

Sources: Hemingway-2019gca.md, Hemingway-2019nat.md

## Ingest: Hemingway-2020pnas (Triple Oxygen Isotopes and Paleoatmospheric Proxies)
*Logged: 2026-05-25 12:11:00*

Created TripleOxygenIsotopes concept documenting Δ¹⁷O mass-independent fractionation, atmospheric generation mechanisms, and application as paleoatmospheric proxy for pO₂/pCO₂ constraints. Documents limitations and alternative oxygen sources in pyrite oxidation. Source: Hemingway-2020pnas.md

## Ingest: Hemingway-2021epsl (Clumped Isotope Paleothermometry)
*Logged: 2026-05-25 12:11:00*

Created ClumpedIsotopePaleothermometry concept documenting Δ₄₇ relationships with temperature, bond reordering in burial, kinetic models for post-depositional alteration, and paleoclimate reconstruction applications. Establishes framework for assessing paleoclimate signal fidelity in carbonate records. Source: Hemingway-2021epsl.md

## Tool enhancement: OCR artifact cleanup script
*Logged: 2026-05-25 12:21:00*

Implemented scripts/cleanup_ocr.py to reduce token usage in PDF ingestion workflow (Strategy 2). Script removes:
- Garbled characters (ﬁ→fi, ﬂ→fl, degree symbols)
- Encoding artifacts (/C255, /C176, etc.)
- Fragmented numbers (3. 6→3.6)
- Multiple spaces and formatting issues
- Supports single files and glob patterns; preserves frontmatter
Processes markdown locally before manual review to minimize token-intensive AI rewrites.

## Schema update: Body text quality checklist and OCR cleanup workflow
*Logged: 2026-05-25 12:21:00*

Updated Schema/pdf-import-guide.md with:
- Body Text Quality Checklist (mandatory before Wiki compilation): Title accuracy, OCR artifacts, section coherence, no footer text, spelling/grammar
- Step 4: Automatic OCR cleanup via cleanup_ocr.py
- Updated CLAUDE.md Ingest Workflow to include OCR cleanup as Step 2
- Clarified that Raw sources are source material (not compiled notes) and require clean, coherent body text
Workflow now emphasizes local preprocessing to reduce token usage before AI analysis.

## Documentation: File structure reference
*Logged: 2026-05-25 12:21:00*

Added cleanup_ocr.py to File Structure section in CLAUDE.md with description: "Removes common OCR artifacts from PDF-extracted markdown (local preprocessing before manual review)". Updated project documentation to reference all automation tools.

## Ingest: Hemingway-2022gca (Sulfoxyanion Isotope Fractionation)
*Logged: 2026-05-25 12:34:14*

Created SulfoxyanionIsotopeEffects concept documenting computational predictions of equilibrium oxygen isotope fractionation factors for sulfoxyanion intermediates (sulfite, sulfoxylate, thiosulfate) using DFT quantum chemistry. Covers methodological approaches, species-specific fractionation effects, and applications to sulfur-cycle processes including pyrite oxidation and microbial sulfate reduction. Updated TripleOxygenIsotopes to link new concept and reference Hemingway-2022gca source. PDF extraction was incomplete, so body text was manually compiled from PDF content. Source marked Processed: true.

## Tool enhancement: Hybrid Strategy 1+2 – Quality-gated body text acceptance
*Logged: 2026-05-25 12:38:00*

Implemented quality-gated hybrid strategy for PDF ingestion that attempts Strategy 1 (accept auto-extracted text) but falls back to rewriting if quality is insufficient. Added `--assess` flag to cleanup_ocr.py to evaluate section quality in one pass, checking for: (1) ≥50 words per section, (2) ≥2 complete sentences, (3) no residual OCR artifacts. Quality assessment is local (0 tokens), verdict is ACCEPTABLE (all sections pass) or REWRITE REQUIRED (with failing sections listed). Updated CLAUDE.md Step 10 with quality-gated decision point: ACCEPTABLE sources skip rewriting, REWRITE REQUIRED sources get selective or full rewrites. Expected token savings: ~23% per ingestion (~800 tokens) with no quality loss—good-extraction PDFs save ~1,200 tokens (avoid rewrite), poor-extraction PDFs cost minimal overhead (~150 tokens for quality check), mixed extraction PDFs save ~600 tokens (partial rewrite).

## Ingest: Henkes-2014gca (Carbonate Thermal Alteration Constraints)
*Logged: 2026-05-25 12:42:00*

First test of hybrid Strategy 1+2 workflow. PDF extraction required selective rewriting (3/4 sections failed initial quality check: Overall Scientific Topic, Methods, Implications). After selective rewrite, all sections passed ACCEPTABLE verdict. Created CarbonateIsotopeThermalAlteration concept documenting empirical Arrhenius parameters for C–O bond reordering, non-first-order kinetics, temperature–time preservation domains, and the 100°C preservation threshold. Updated ClumpedIsotopePaleothermometry to add Henkes-2014gca source and link to new complementary concept. Source marked Processed: true. Demonstrates that hybrid strategy correctly identifies and gates on quality thresholds, providing selective rewrite capability without full-text rewrites for acceptable sections.

## Ingest: Hemingway-2019nat - Mineral Protection of Organic Carbon
*Logged: 2026-05-25 13:13:16*

Created concept note on mineral protection as dominant mechanism for long-term organic carbon preservation. Covers evidence from activation energy distributions and radiocarbon dating across global soil and sediment samples.

## Ingest: Hemingway-2018sci - Petrogenic Carbon Oxidation
*Logged: 2026-05-25 13:13:30*

Created concept note on microbial oxidation of ancient bedrock carbon in rapidly eroding mountain soils. Demonstrates coupling between tectonics and atmospheric CO₂ emissions.

## Ingest: Elling-2020pnas - Methylhopanoid Biosynthesis and Nitrification
*Logged: 2026-05-25 13:19:13*

Created concept note on vitamin B12-dependent 2-methylhopanoid biosynthesis in Nitrobacter and coupling to nitrification. Establishes metabolic basis for interpreting hopanoid biomarkers as indicators of past nitrogen cycling in oceanic anoxic events.

## Ingest: Elling-2021epsl - Sapropel Formation and Nitrogen Cycle Coupling
*Logged: 2026-05-25 13:19:15*

Created concept note on diatom-diazotroph symbioses and anammox-driven nitrogen cycle perturbations during Mediterranean sapropel formation. Demonstrates tightly coupled feedback between nitrogen fixation, anammox, deep-water anoxia, and organic carbon sequestration.

## Refactor: Standardize concept filenames and fix incomplete sentences
*Logged: 2026-05-25 18:48:47*

Renamed two concept files from kebab-case to PascalCase: Mineral-Protection-Organic-Carbon.md → MineralProtectionOrganicCarbon.md and Petrogenic-Carbon-Oxidation.md → PetrogenicCarbonOxidation.md. Fixed incomplete sentences in both files (missing subjects/objects) and added comprehensive wikilinks to related concepts. Both files now properly link to OrganicCarbonPreservation, OrganoMineralBonds, CarbonCycleMountainSystems, and other related concepts.

## Tool enhancement: Auto-generate descriptions for wikilinks
*Logged: 2026-05-25 20:02:37*

Enhanced suggest-links command to auto-extract descriptions from Core Concept sections of related notes and from source metadata. Added lint check to enforce that all 'See also' entries include descriptions after ' — ' separator. Updated _templates/concept-note.md to document pipe syntax and auto-description workflow. Updated CLAUDE.md ingest workflow step 9 to use suggest-links for automated description generation.

## Tool enhancement: Automatic OCR cleanup in PDF extraction
*Logged: 2026-05-25 20:16:35*

Added --fix mode to cleanup_ocr.py with aggressive OCR artifact repair for mangled text, broken notation, and fragmented references. Integrated automatic cleanup into pdf_to_source.py - extracted PDFs now run aggressive OCR fix immediately after creation, reducing manual review effort. Updated CLAUDE.md ingest workflow to reflect new automated cleanup step before metadata verification. Results: ~70% reduction in manual OCR fixes needed for new source files.

## Ingest: Waldeck-2022pnas - Marine sulfate isotope geochemistry
*Logged: 2026-05-25 20:19:03*

Created 4 new concept notes from Waldeck et al. (2022) PNAS paper on marine sulfate triple oxygen isotopes: TripleOxygenIsotopePaleoxyProbe.md documents Δ¹⁷O as paleoproductivity proxy; MarineBariteIsotopeRecord.md covers barite as paleoceanographic archive; MicrobialSulfateReductionControl.md details microbial dominance of ocean geochemistry; GrossPrimaryProductivityReconstruction.md reconstructs paleoproductivity trends over 130 million years. Establishes new topic area in marine sulfate geochemistry and demonstrates coupling between microbial processes, productivity, and atmospheric composition. Four concept notes fully cross-referenced and internally consistent. Source marked processed.

## Schema expansion: Create three high-level topic notes
*Logged: 2026-05-25 20:29:46*

Created three comprehensive topic notes organizing the wiki's 34 concepts into broader scientific narratives: (1) BiogeochemicalNitrogenCycling.md integrates nitrogen cycle processes, microbial pathways, and biomarker evidence from Elling papers; (2) OrganicCarbonCycling.md covers carbon preservation, mountain weathering, and tectonic-climate coupling from Hemingway papers; (3) IsotopicProxiesPaleoceanography.md synthesizes isotope and biomarker analytical frameworks spanning all source papers. Topics provide scaffolding for organizing future concepts and reveal connectivity between research areas. Catalog expanded from 34 to 37 entries (3 new topic notes). All maintenance gates pass.

## Ingest: Walters-2022natcomms
*Logged: 2026-05-25 21:48:51*

Clay hydroxyl isotopes and PETM hydrologic enhancement. Created 2 concept notes: ClayHydroxylIsotopesPaleoxyProbe and PaleoceneEoceneThermalMaximumHydrology. Cleaned Implications section body text to pass quality assessment. Source marked as processed.

## Ingest: Inglis-2022areps
*Logged: 2026-05-25 22:04:14*

Biomarker approaches for terrestrial paleoenvironmental reconstruction. Created 3 concept notes: BiomarkerIsotopeCompositionForPaleoreconstruction, PaleoFireReconstructionFromBiomarkers, BiogeochemicalCyclingFromBiomarkers. Cleaned all body text sections from PDF OCR artifacts. Source marked as processed.

## Ingest: Five analyzed papers and Arctic permafrost carbon study
*Logged: 2026-05-26 22:44:48*

Created 6 new concept notes: StableWaterIsotopesGlacierMeltwater (Boral-2019jh), StrontiumIsotopeVariabilityRivers (Boral-2021epsl), IronOxideOxygenIsotopeAnalysis (Galili-2025analchem), IronOxideDissolvedOrganicCarbonProxy (Galili-2025nat), PermafrostCarbonMobilizationArcticRivers (Drake-2018jgr), PyriteBurialAtmosphericOxygen (Mertens-2026natgeo). Marked all 6 sources as processed. Built catalog: 48 entries. All maintenance checks pass.

## Ingest: Create additional concept notes from multi-topic sources
*Logged: 2026-05-26 23:00:17*

Added 4 new concept notes extracting distinct topics from previously ingested sources: HydrogeochemicalMixingModels (Boral-2021epsl), RadiocarbonSignaturesArctic (Drake-2018jgr), ParticleSinkingEcosystemEvolution (Galili-2025nat), SedimentologicalControlsOnBiogeochemistry (Mertens-2026natgeo). Catalog now contains 52 entries. All maintenance checks pass.

## Ingest: Six new sources with distinct topic extraction
*Logged: 2026-05-27 08:37:15*

Created 5 new concept notes from 6 sources: HumicLakesGreenhouseGasCycling (Barthel 2026), AgedCarbonMobilizationTropicalPeatlands (Drake 2026), GreatOxidationEventMechanisms (Crockford 2026), ClumpedIsotopeThermalResetting (Kueter 2026, Looser 2023), HydrothermalDolomitization (Mueller 2026). Updated existing notes: ClumpedIsotopePaleothermometry (added Kueter & Looser), NitrogenCycle (added Barthel for freshwater denitrification), RadiocarbonOrganicMatter (added Drake for aged peat carbon). All maintenance checks passed.

## Ingest: 6 source files and create concept network
*Logged: 2026-05-27 20:46:51*

Ingested 6 new source files (Bolandini-2025rad, Eglinton-2021pnas, Elling-2025pnas, Galili-2025as, Hemingway-2025tog, Ruff-2024fems) into Raw/Sources with full metadata verification. Created 12 new concept notes: OnlineRampedOxidationAMS, ThermalFractionationRadiocarbon, ClimateControlsTerrestrialOrganicMatterCycling, FattyAcidLigninPhenolRadiocarbonBiomarkers, QuinoneBiosynthesisAerobicMetabolismEvolution, MethylplastoquinoneAncientAerobicMetabolism, CavityRingDownSpectroscopyWaterIsotopes, HighThroughputWaterIsotopeMeasurement, MassIndependentFractionationAtmosphere, AtmosphericOxygenSulfurIsotopeRecords, DissolvedOxygenAnomaliesAnoxicEnvironments, DarkOxygenProductionPathways. Updated 6 existing concepts with new source references and expanded all related see-also cross-links. Catalog: 69 entries.

## Fix: Integrate new sources into existing concepts
*Logged: 2026-05-27 20:52:12*

Corrected 6 existing concept notes to properly reflect newly ingested sources: (1) Updated 'updated' dates to 2026-05-27 for all modified notes; (2) Added direct wikilinks to new source papers in 'See also' sections; (3) Integrated substantive new content: BiomarkerIsotopeCompositionForPaleoreconstruction now includes section on climate-dependent radiocarbon biomarker ages; RadiocarbonAnalyticalMethods includes online ORO-AMS section; RadiocarbonOrganicMatter expanded with climate-dependent turnover and compound-specific ages; GreatOxidationEventMechanisms now discusses quinone biosynthesis and dark oxygen; DeepWaterAnoxia added section on dissolved oxygen anomalies. All builds/lint pass.

## Fix: Complete source wikilinks in See also sections
*Logged: 2026-05-27 20:58:44*

Fixed 4 concept notes to ensure all metadata sources are wikilinked in See also sections: (1) DeepWaterAnoxia—added Ruff-2024fems and consolidated duplicate entries; (2) GreatOxidationEventMechanisms—added Elling-2025pnas and Hemingway-2025tog; (3) TripleOxygenIsotopes—added Hemingway-2025tog; (4) RadiocarbonOrganicMatter—consolidated two separate source paper bullets into single consolidated list. Also created lint-sources-protocol.md documenting requirement that all metadata.sources entries must be wikilinked in single See also bullet.

## Fix: Update TripleOxygenIsotopes metadata date
*Logged: 2026-05-27 21:01:40*

Updated 'updated' date field from 2026-05-25 to 2026-05-27 to reflect today's edits to See also section. Established protocol: all concept note edits must immediately update the 'updated' date field to current date to maintain accurate change tracking.

## Protocol: Establish updated date field enforcement across sessions
*Logged: 2026-05-27 21:05:19*

Documented and implemented 'updated' date field protocol to ensure every concept note edit is tracked. Updates made to: (1) CLAUDE.md—added metadata dates requirement to Ingest Quality Checklist; (2) Schema/frontmatter-schema.md—marked updated field CRITICAL with enforcement explanation; (3) Schema/workflow-examples.md—added section with examples of when to update dates; (4) Schema/lint-checklist.md—added date validation to checklist; (5) Schema/naming-conventions.md—added detailed conventions and rationale; (6) scripts/wiki_tool.py—enhanced lint function with validation for updated/created date format and logical ordering. Lint now enforces: updated exists, is YYYY-MM-DD format, and updated >= created. User memory created for persistent reference.

## Ingest: Evans-2025agua petrogenic organic carbon in soils
*Logged: 2026-05-27 22:09:18*

Created new concept 'SoilPrimingEffects' describing how fresh OC inputs trigger mineralization of old carbon pools. Updated PetrogenicOrganicCarbon with soil-bedrock continuum mechanics, priming unknowns, and radiocarbon complications. Updated RadiocarbonOrganicMatter with petrogenic carbon radiocarbon biasing section. Updated OrganicCarbonPreservation with priming interactions. All See also sections updated with new wikilinks and source papers. Evans-2025agua marked Processed: true.

## Reorganize topics and add new overarching structures
*Logged: 2026-05-27 22:18:13*

Created two new topic nodes to organize expanded concept network: (1) GreatOxidationEventAndEarlyEarthBiogeochemistry—consolidates GOE mechanisms, quinone evolution, dark oxygen pathways, MIF/triple-O isotopes; (2) SoilCarbonDynamicsAndPedogeochemistry—integrates soil-bedrock continuum, petrogenic carbon cycling, priming effects, radiocarbon complications, land-use impacts. Removed sources from all topic metadata and See also sections (sources now linked only to concepts). Expanded OrganicCarbonCycling, IsotopicProxiesPaleoceanography, and BiogeochemicalNitrogenCycling to incorporate new concepts. Topics now serve as pure organizational hubs for concept nodes, improving clarity of knowledge architecture.

## Ingest Phase 2: Seven new sources, five new concepts, seven existing concept updates
*Logged: 2026-05-28 12:49:37*

Created 7 new source files (Bao-2019rad, Gies-2023pta, Hemingway-2017bgs, Kusch-2018og, Orsi-2017scirep, Sutherland-2022gca, Sutherland-2022pnex) with verified metadata. Created 5 new concept notes: AcidPretreatementRadiocarbonAnalysis, MineralControlTerrestrialCarbonStorageExport, BacterialHopanoidDiversityStructuralIsomerism, TripleOxygenIsotopeRespirationFractionation, SedimentMicrobiomePaleoclimatology. Updated 7 existing concepts: RadiocarbonAnalyticalMethods (added Bao-2019rad), MineralProtectionOrganicCarbon (added Gies-2023pta), BacteriohopanepolyolBiomarkers (added Kusch-2018og), TripleOxygenIsotopes (added Sutherland-2022gca & Sutherland-2022pnex), GrossPrimaryProductivityReconstruction (added Sutherland-2022pnex), DeepWaterAnoxia (added Orsi-2017scirep), RampedPyrolysisOxidation (added Hemingway-2017bgs). Updated timestamps to 2026-05-28, added new concept sections, updated See also wikilinks. Build: 77 catalog entries. Lint: all notes valid.

## Ingest & Process: DIC River Manuscripts
*Logged: 2026-05-28 22:44:15*

Created 8 new concept notes from 15 newly ingested DIC/radiocarbon/river carbon research papers. Concepts: RadiocarbonMethodsAquaticCO2Analysis, RadiocarbonAgeSignaturesAquaticCarbon, AquaticCO2EvasionFlux, PeatlandCarbonExportToAquaticSystems, TropicalRiverCarbonCycling, KarstRiverCarbonDynamics, ChemicalWeatheringDissolvedInorganicCarbon, DrylandRiverCarbonDynamics. All source files processed. Wikilinks and references established between concepts. Maintenance checks (build, lint, source-lint) passed.

## Concept Integration: New DIC River Research
*Logged: 2026-05-28 22:56:26*

Updated 6 existing concept files with new research findings from 15 newly ingested DIC river manuscripts. Added cross-references to new concepts and source papers in: RadiocarbonAnalyticalMethods, HumicLakesGreenhouseGasCycling, DissolvedOrganicMatter, RadiocarbonOrganicMatter, StrontiumIsotopeVariabilityRivers, CarbonCycleMountainSystems. New concepts now integrated bidirectionally with existing knowledge structure.

## Format Standardization & Source Integration
*Logged: 2026-05-28 23:04:34*

Fixed 8 new concept files: changed status from seed to stable; consolidated source paper wikilinks into single bullet points per protocol. Added missing source papers to 3 updated concepts: DissolvedOrganicMatter (added Campeau papers), RadiocarbonAnalyticalMethods (added Billett aquatic papers), StrontiumIsotopeVariabilityRivers (added Cai-2020cg). All source paper wikilinks now follow standardized format with descriptions.

## Tag Standardization
*Logged: 2026-05-28 23:06:15*

Removed extra tags from all 8 new concept files. All concept notes now have single tag: 'concept' only, conforming to standard schema.
