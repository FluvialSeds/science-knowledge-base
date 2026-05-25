# Logs

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
