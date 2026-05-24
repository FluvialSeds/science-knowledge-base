# Logs

## Schema update: Mandatory logging
*Logged: 2026-05-24 13:35:22*

Updated CLAUDE.md to require logging after every ingest and maintenance step. Logging now part of official workflow.

## First Ingest: LLM Wiki Demo Source
*Logged: 2026-05-24 13:25:15*

Compiled LLMWikiStarterDemo.md into Topic (LLMWiki), Concept (SourceToWikiWorkflow), and Project (WikiSetup) notes. Demonstrates core workflow of separating Raw sources from compiled Wiki knowledge.

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
