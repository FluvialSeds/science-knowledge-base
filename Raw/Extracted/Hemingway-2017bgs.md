![[Hemingway-2017bgs.pdf]]

> [!ocr-extractor]- Extracted text
> Biogeosciences, 14, 5099–5114, 2017
> https://doi.org/10.5194/bg-14-5099-2017
> © Author(s) 2017. This work is distributed under
> the Creative Commons Attribution 4.0 License.
> Technical note: An inverse method to relate organic carbon
> reactivity to isotope composition from serial oxidation
> Jordon D. Hemingway1,2,a, Daniel H. Rothman3, Sarah Z. Rosengard1,2,b, and Valier V. Galy1
> 1Department of Marine Chemistry and Geochemistry, Woods Hole Oceanographic Institution, 266 Woods Hole Road,
> Woods Hole, MA 02543, USA
> 2Massachusetts Institute of Technology – Woods Hole Oceanographic Institution Joint Program in Oceanography and
> Applied Ocean Science and Engineering, 77 Massachusetts Avenue, Cambridge, MA 02139, USA
> 3Lorenz Center, Department of Earth, Atmospheric, and Planetary Science, Massachusetts Institute of Technology,
> 77 Massachusetts Avenue, Cambridge, MA 02139, USA
> apresent address: Department of Earth and Planetary Sciences, Harvard University, 20 Oxford Street, Cambridge,
> MA 02138, USA
> bpresent address: Departments of Geography and Earth, Ocean, and Atmospheric Sciences, University of British Columbia,
> 2207 Main Mall, Vancouver, BC V6T 1Z4, Canada
> Correspondence to: Jordon D. Hemingway (jordon_hemingway@fas.harvard.edu)
> Received: 4 August 2017 – Discussion started: 8 August 2017
> Revised: 5 October 2017 – Accepted: 10 October 2017 – Published: 15 November 2017
> Abstract. Serial oxidation coupled with stable carbon and ra-
> diocarbon analysis of sequentially evolved CO2 is a promis-
> ing method to characterize the relationship between organic
> carbon (OC) chemical composition, source, and residence
> time in the environment. However, observed decay profiles
> depend on experimental conditions and oxidation pathway.
> It is therefore necessary to properly assess serial oxidation
> kinetics before utilizing decay profiles as a measure of OC
> reactivity. We present a regularized inverse method to esti-
> mate the distribution of OC activation energy (E), a proxy
> for bond strength, using serial oxidation. Here, we apply this
> method to ramped temperature pyrolysis or oxidation (RPO)
> analysis but note that this approach is broadly applicable to
> any serial oxidation technique. RPO analysis directly com-
> pares thermal reactivity to isotope composition by determin-
> ing the E range for OC decaying within each temperature
> interval over which CO2 is collected. By analyzing a decar-
> bonated test sample at multiple masses and oven ramp rates,
> we show that OC decay during RPO analysis follows a su-
> perposition of parallel first-order kinetics and that resulting
> E distributions are independent of experimental conditions.
> We therefore propose the E distribution as a novel proxy to
> describe OC thermal reactivity and suggest that E vs. isotope
> relationships can provide new insight into the compositional
> controls on OC source and residence time.
> 1 Introduction
> Natural organic matter present in aquatic environments, sed-
> iments, soils, and vegetation contains roughly 3-fold more
> carbon than the preindustrial atmosphere (Bianchi, 2011).
> As such, the balance between organic carbon (OC) synthe-
> sis and remineralization exerts a major control on the global
> carbon cycle and on atmospheric CO2 levels (Lasaga et al.,
> 1985). However, OC remineralization rates are spatiotempo-
> rally heterogeneous, leading to decay timescales that range
> from minutes to millions of years (Boudreau and Ruddick,
> 1991; Forney and Rothman, 2012a; Middelburg, 1989). To
> explain this variability, it has been hypothesized that reminer-
> alization depends on multiple chemical and environmental
> factors such as OC molecular structure (Burdige, 2007; Tege-
> laar et al., 1989), microbial community composition (Pedler
> et al., 2014; Schmidt et al., 2011), secondary chemical in-
> teractions (Schmidt et al., 2011), and physical protection by
> particles (Mikutta et al., 2006; Keil and Mayer, 2014). The
> relative importance of these governing mechanisms remains
> actively debated and is thought to vary depending on envi-
> ronmental setting (Hedges et al., 2001; Rothman and Forney,
> 2007; Schmidt et al., 2011), thus limiting our mechanistic un-
> derstanding of OC decay.
> Published by Copernicus Publications on behalf of the European Geosciences Union.
>
> ---
>
> 5100 J. D. Hemingway et al.: Organic carbon activation energy and isotope composition
> This limitation is partially methodological in nature; tradi-
> tional geochemical analyses often target either “bulk” OC or
> trace “biomarker” molecules such as plant-wax fatty acids
> (Galy et al., 2011; Galy and Eglinton, 2011; Hemingway
> et al., 2016). While bulk measurements include all OC con-
> tained within a sample, they offer no information on the dis-
> tribution of chemical structure or reactivity within a complex
> mixture. In contrast, biomarker analysis is highly specific but
> individual compounds nonetheless still represent the average
> of multiple sources. Furthermore, biomarkers typically con-
> stitute ≤ 1 % of total OC and can be subject to production,
> transport, and preservation biases (Hemingway et al., 2016).
> To bridge the information gained by these methods, a
> novel class of analytical techniques, termed “serial oxida-
> tion”, has emerged. Such analyses separate carbon within
> a bulk sample based on its susceptibility to decomposition
> by chemical hydrolysis (Helfrich et al., 2007), UV light
> (Beaupré et al., 2007; Follett et al., 2014), heat (Rosenheim
> et al., 2008), or microbial respiration (Beaupré et al., 2016)
> and measure the stable carbon (13C / 12C, expressed as δ13C)
> and radiocarbon (14C / 12C, here expressed as fraction mod-
> ern or Fm) content of evolved CO2. By separating CO2 into
> multiple lability intervals, isotope ratios are obtained for car-
> bon atoms exhibiting similar physical and/or chemical prop-
> erties. Because δ13C provides information on the source of
> organic matter while Fm reflects the amount of time that has
> passed since organic compounds were initially synthesized,
> serial oxidation is a promising method to directly probe the
> compositional controls on OC source and residence time.
> Still, a theoretical treatment of serial oxidation kinetics is
> lacking, hindering our ability to correlate measured isotope
> distributions with intrinsic chemical properties and reactivity.
> In this study, we relate OC thermal recalcitrance to its corre-
> sponding δ13C and Fm values using ramped-temperature py-
> rolysis or oxidation (RPO). This method involves heating OC
> at a controlled rate while continuously quantifying and col-
> lecting evolved CO2, which is binned over user-defined time
> intervals (termed “fractions”) and analyzed for δ13C and Fm
> (Rosenheim et al., 2008; Hemingway et al., 2017). We de-
> scribe non-isothermal OC decay rates as a function of E, the
> Arrhenius activation energy, using a novel inverse solution
> to the distributed activation energy model (Braun and Burn-
> ham, 1987; Burnham and Braun, 1999; Cramer, 2004; White
> et al., 2011). By conducting a set of kinetic experiments, we
> show that the E distribution within a given OC mixture does
> not depend on experimental conditions and is thus a reliable
> proxy for bond strength and OC chemical composition.
> We note that the modeling approach developed here is
> broadly applicable to any serial oxidation technique, al-
> though the resulting E distributions will differ depending
> on oxidation pathway. For example, aromatic compounds
> such as lignin have been shown to be highly photoreactive
> (Spencer et al., 2009) despite their relatively high thermal
> recalcitrance (Williams et al., 2014) and will likely be de-
> scribed by lower E values when oxidized with UV light rel-CO 2
> Time
> dG(t)
> dt (�g C s -1
> )
> Programmable T
> oven [β, T(t)]
> Constant T
> oven (800 °C)
> Quartz
> reactor with
> sample
> (G0 �g C)
> 32 mL min -1 He + 3 mL min -1 O 2
> Cu, Pt, Ni
> catalyst
> In-line infrared CO analyser2
> Switchable
> cryogenic traps
> Traditional vacuum line
> and CO 2 isotope analysis
> T(t)
> Time
> Fraction mass (mf )
> fraction isotopes
> (δ13Cf , Fmf )
> Water
> trap
> Figure 1. RPO instrument schematic. User-defined inputs are
> printed in blue, while observed measurements are printed in red (see
> Table 1 for symbol definitions).
> ative to RPO analysis. Here, we choose RPO because analy-
> sis is rapid (≈ 3 h per sample), requires little material (150–
> 250 μg C), contains minimal preparation steps, and results in
> small kinetic isotope fractionation (Hemingway et al., 2017).
> We therefore treat E as a proxy for OC chemical struc-
> ture and emphasize that thermal reactivity is not equivalent
> to microbial reactivity in the environment (Leifeld and von
> Lützow, 2014). Rather, by comparing E profiles and cor-
> responding isotope compositions across environmental sam-
> ples or experimental conditions (e.g., before and after mi-
> crobial degradation), our method provides a framework to
> probe how, if at all, OC source and turnover time (as mea-
> sured by δ13C and Fm) are related to its chemical compo-
> sition (as predicted by thermal E distributions). We begin
> in Sect. 3 by deriving the governing equations to describe
> a parallel superposition of first-order, non-isothermal decay.
> Then, in Sect. 4, we describe a method to solve for the distri-
> bution of E using a regularized inverse approach. Finally, in
> Sect. 5, we determine the subset of E that is contained within
> each RPO fraction and directly relate OC reaction energet-
> ics to corresponding isotope values. All calculations were
> performed using the accompanying “rampedpyrox” Python
> package (Hemingway, 2017).
> Biogeosciences, 14, 5099–5114, 2017 www.biogeosciences.net/14/5099/2017/
>
> ---
>
> J. D. Hemingway et al.: Organic carbon activation energy and isotope composition 5101
> Table 1. List of mathematical symbols used throughout this study.
> Symbol Parameter Units
> A Dynamic disordered kinetic design matrix kJ mol−1
> α(t) Integral of G0-normalized thermogram at time t –
> β Temperature ramp rate K s−1
> δ13Cf 13C / 12C ratio of RPO fraction f , expressed in per mill VPDB ‰
> 1E Activation energy step kJ mol−1
> 1tj Time step for point j in t s
> 13−121E E difference between 13C- and 12C-containing compounds kJ mol−1
> Ei Activation energy for component i kJ mol−1
> E Continuous form of Ei kJ mol−1
> E Vector of discretized activation energy kJ mol−1
> Fmf 14C / 12C ratio for RPO fraction f , expressed as fraction modern –
> G0 Total initial mass of carbon μg C
> gi (0) Initial mass of carbon in component i μg C
> gi (t) Mass of carbon in component i remaining at time t μg C
> G(t) Mass of total carbon remaining at time t μg C
> g(0, E) Continuous form of gi (0) μg C
> g(t, E) Continuous form of gi (t) μg C
> g Vector of G(t)/G0 at each time point –
> ki (t) First-order rate coefficient for component i at time t s−1
> k(t, E) Continuous first-order rate coefficient for energy value E at time t s−1
> κi (t) Discrete, time-integrated first-order decay coefficient for component i at time t –
> κ(t, E) Continuous, time-integrated first-order decay coefficient for energy value E at time t –
> λ Regularization weighting factor –
> mf Mass of carbon (as CO2) contained in RPO fraction f μg C
> m(t) G0-normalized decay rate at time t s−1
> nE Number of nodes in E –
> nt Number of nodes in t –
> pi (0) Fraction of G0 initially in component i –
> pi (t) Fraction of G0 remaining in component i at time t –
> p(0, E) Continuous form of pi (0) –
> p(t, E) Continuous form of pi (t) –
> p Vector of p(0, E)/1E at each energy point (kJ mol−1)−1
> 5f (E) Subset of p(0, E) contained in RPO fraction f –
> 13/12r(t) Ratio of 13C / 12C decay at time t –
> R Ideal gas constant kJ mol−1 K−1
> R First derivative operator matrix –
> T (t) Temperature at time t K
> t Vector of discretized time s
> ω Arrhenius pre-exponential (“frequency”) factor s−1
> 2 Materials and methods
> 2.1 Sample selection and preparation
> As a representative sample, we analyzed particulate organic
> carbon (POC) contained in suspended sediments from the
> surface of the Narayani River. This sample (PB-60) was col-
> lected at the base of the Himalayas (27.70◦ N, 84.43◦ E) and
> has been analyzed for bulk OC and plant-wax carbon iso-
> topes (Galy et al., 2008, 2011; Galy and Eglinton, 2011).
> Aliquots were taken for RPO analysis from freeze-dried,
> archived material and acidified under HCl fumes at 60 ◦C for
> 72 h to remove carbonates (Whiteside et al., 2011). Because
> residual chloride has been shown to interact with the RPO
> catalyst wire (Hemingway et al., 2017), acidified aliquots
> were rinsed 3 × in 18.2 M Milli-Q water and freeze-dried
> overnight at −40 ◦C prior to analysis. For consistency and
> to properly calculate RPO isotope mass balance, bulk %OC,
> δ13C, and Fm values were remeasured using fumigated and
> rinsed material (McNichol et al., 1994a, b). Resulting Fm for
> rinsed material is 0.04 lower than that for unrinsed aliquots
> (Galy et al., 2008), reflecting a minor loss of acid-soluble OC
> for this sample during the rinsing step.
> www.biogeosciences.net/14/5099/2017/ Biogeosciences, 14, 5099–5114, 2017
>
> ---
>
> 5102 J. D. Hemingway et al.: Organic carbon activation energy and isotope composition200 400 600 800 1000
> Temperature (°C)
> -20
> -32
> -30
> -28
> -26
> -24
> -22
> 1.0
> 0.0
> 0.2
> 0.4
> 0.6
> 0.8
> δ13
> C (‰ VPDB)
> Fm
> 200 400 600 800 1000
> Temperature (°C)
> 0
> -20
> -15
> -10
> -5
> δ13
> C (‰ VPDB)
> (a) (b)
> Figure 2. RPO results. Measured thermograms (gray shaded region, ppm CO2 axes not shown), δ13C values (white circles, left axes), and
> Fm values (transparent bars, right axes) for (a) Narayani POC and (b) JGOFS sediment (Fm not measured). Fm bar widths correspond to
> the temperature range of collection for each RPO fraction. Fm and δ13C analytical uncertainty is always smaller than point marker and is
> therefore not shown (see Tables 2–3 for values).
> To test if the presence of inorganic carbon (IC; e.g.,
> CaCO3) affects decay kinetics, we additionally analyzed a
> pure CaCO3 laboratory working standard (Icelandic spar;
> Hemingway et al., 2017) as well as carbonate-rich sedi-
> ment from the Southern Ocean (60.24◦ S, 170.19◦ W) col-
> lected for the Joint Global Ocean Flux Study (JGOFS; Sayles
> et al., 2001). JGOFS aliquots were taken from archived
> core-top material (0–0.5 cm, stored at −80 ◦C), freeze-dried
> overnight at −40 ◦C, and homogenized prior to RPO analy-
> sis. IC content, OC content, and bulk 13C composition were
> re-quantified at the NOSAMS facility at the Woods Hole
> Oceanographic Institution (McNichol et al., 1994a).
> 2.2 Instrumental setup
> RPO analysis has been described in detail previously (Rosen-
> heim et al., 2008; Hemingway et al., 2017). In summary, a
> solid sample containing ≈ 150–250 μg C is loaded into a pre-
> combusted (850 ◦C, 5 h) quartz reactor and placed into a two-
> stage oven, as shown in Fig. 1. The reactor is then sealed and
> the sample is exposed to an atmosphere of 92 : 8 He : O2 with
> a total flow rate of 35 mL min−1 (oxidation mode). During
> analysis, the oven surrounding the sample is programmed
> to heat at a user-defined ramp rate, termed β (see Table 1
> for symbol descriptions). Instantaneous temperature within
> the oven is measured using two thermocouples separated by
> ≈ 1 cm to monitor temperature heterogeneity, which is typi-
> cally < 5 ◦C. Following standard practice (Rosenheim et al.,
> 2008), a ramp rate of 5 ◦C min−1 was used for all experi-
> ments in which CO2 gas was collected for isotope analysis.
> In the second (downstream) oven, eluent gas is passed over a
> Cu, Pt, and Ni catalyst wire held at 800 ◦C to facilitate oxi-
> dation of reduced carbon-containing gases to CO2.
> After exiting the second oven, eluent gas is distilled
> through a water trap and passed into a flow-through infrared
> gas analyzer (IRGA) to measure CO2 concentration (in parts
> per million by volume; ppm CO2) with 1 s temporal resolu-
> tion. Resulting ppm CO2 vs. temperature plots are referred to
> as “thermograms” (Fig. 2). At each time point, the measured
> thermogram (in units of ppm CO2) can be converted to an
> instantaneous OC decay rate (in units of μg C s−1) using the
> measured gas flow rate and the ideal gas constant. “Thermo-
> gram” and “decay rate” are therefore used interchangeably
> throughout this paper. IRGA measurements were calibrated
> using a two-point calibration curve before each analysis to
> account for instrument drift and are precise to ±5 ppm CO2
> (Hemingway et al., 2017). Downstream of the IRGA, elu-
> ent gas is passed into one of two switchable traps and CO2
> is cryogenically frozen while He and O2 are vented to the
> atmosphere. Traps are switched at user-defined time points
> and CO2 is further distilled, quantified, transferred into glass
> tubes packed with ≈ 100 mg CuO and ≈ 10 mg Ag, and flame
> sealed. Finally, CO2 was re-combusted at 525 ◦C for 1 h to
> remove trace contaminant gases.
> 2.3 Isotope measurement, blank correction,
> and data analysis
> Radiocarbon compositions of all bulk samples and RPO frac-
> tions were measured at NOSAMS following standard graphi-
> tization methods (McNichol et al., 1994b). All radiocarbon
> results are expressed in fraction modern notation (Fm). We
> note that Fm used here is corrected for 13C fractionation and
> is thus identical to the F14C notation of Reimer et al. (2004).
> Bulk and RPO fraction stable carbon isotope compositions
> were measured on CO2 gas using a dual-inlet isotope ratio
> mass spectrometer (IRMS) located at NOSAMS (McNichol
> et al., 1994a), with resulting 13C content expressed in δ13C
> per mill (‰) notation relative to Vienna Pee Dee Belemnite
> (VPDB). RPO fraction masses, δ13C values, and Fm values
> Biogeosciences, 14, 5099–5114, 2017 www.biogeosciences.net/14/5099/2017/
>
> ---
>
> J. D. Hemingway et al.: Organic carbon activation energy and isotope composition 5103
> were corrected for blank carbon contribution, and δ13C was
> additionally corrected to ensure 13C mass balance as incom-
> plete oxidation to CO2 has been shown to impart a small frac-
> tionation effect (Hemingway et al., 2017). Analytical uncer-
> tainty was propagated throughout all corrections. Thermo-
> grams and isotope results for both Narayani POC and JGOFS
> sediment are plotted in Fig. 2, while temperature ranges, car-
> bon masses, and isotope values are additionally reported in
> Tables 2–3.
> 3 Deriving a model of decay kinetics
> We derive the distributed activation energy model by first
> considering the case in which OC is separated into a set of
> discrete components with unique E values. We then gener-
> alize this description to allow for a continuous E distribu-
> tion (Braun and Burnham, 1987; Burnham and Braun, 1999;
> Cramer, 2004).
> 3.1 Discrete model
> During OC remineralization, the decay rate of carbon con-
> tained in a particular component i is often described as a
> first-order process with respect to gi (t), the mass of carbon
> remaining in component i at any time t (Westrich and Berner,
> 1984; Braun and Burnham, 1987), according to
> dgi (t)
> dt = −ki gi (t), (1)
> where ki is the first-order rate coefficient associated with
> component i. Total OC decay is then treated as the sum
> over all components. Although it is possible that OC de-
> cay in the natural environment additionally depends on ox-
> idant concentration, we omit this dependency here since O2
> is provided in excess in our experimental setup (Fig. 1). In
> contrast to the “multi-G” and “reactive continuum” models
> that are often used to describe environmental OC degradation
> rates (Westrich and Berner, 1984; Boudreau and Ruddick,
> 1991; Forney and Rothman, 2012a, b), here we allow ki to
> vary with time. Because rate coefficients are related to tem-
> perature and activation energy, ki can be written as a time-
> dependent function of E following the Arrhenius equation:
> ki (t) = ω exp
> [
> − Ei
> RT (t)
> ]
> , (2)
> where ω is the empirically derived Arrhenius pre-exponential
> (“frequency”) factor, R is the ideal gas constant, Ei is the
> activation energy of carbon contained in component i, and
> T (t) is the measured temperature of the system at time t.
> For non-isothermal systems, time-dependent decay coeffi-
> cients can therefore be described by the static property Ei
> and the observed variable T (t). Although T (t) is related to
> t by a constant ramp rate β during RPO analysis, we leave
> this written as is to emphasize that our model is valid for any200 400 600 800 1000
> Temperature (°C)
> 4.0
> 0.0
> 1.0
> 2.0
> 3.0
> G0- and β -normalized decay rate ×10 3 (°C-1
> )
> β = 2 ºC min -1
> β = 5 ºC min -1
> β = 10 ºC min -1
> Figure 3. Testing the ramp-rate effect. Measured thermograms are
> shown for Narayani POC analyzed using multiple ramp rates (β).
> Decay rates have been normalized by G0 and β in order to properly
> compare y-axis values between each analysis.
> measured time–temperature history. Substituting Eq. (2) into
> Eq. (1), we write the first-order decay at time t during a non-
> isothermal process as
> dgi (t)
> dt = −ω exp
> [
> − Ei
> RT (t)
> ]
> gi (t). (3)
> The mass of carbon remaining in component i at time t can
> be determined by integrating Eq. (3) from an initial time t =
> 0:
> gi (t) = gi (0)e−κi (t), (4)
> where
> κi (t) = ω
> t∫
> 0
> exp
> [
> − Ei
> RT (t′)
> ]
> dt′ (5)
> is the time integrated decay coefficient at time t, and gi (0)
> is the initial mass of carbon contained in component i.
> Equation (5) states that gi (t) depends on the entire time–
> temperature history of the experiment. That is, the evolution
> of dgi (t)/dt reflects both a decrease in gi (t) as OC is rem-
> ineralized and an increase in ki (t) with increasing T (t) as the
> experiment progresses. This results in a predictable shift in
> RPO thermograms toward higher elution temperatures with
> increasing β (Miura and Maki, 1998), as shown in Fig. 3.
> Following Boudreau (1997) and Westrich and Berner
> (1984), an environmental sample containing a complex OC
> mixture can be described as a superposition of a finite set
> of n components, each decaying according to a unique ki (t)
> and thus corresponding to a unique Ei value. G(t), the to-
> tal carbon mass remaining at t, is then the sum of the mass
> remaining in each component:
> G(t) =
> n∑
> i=1
> gi (t). (6)
> www.biogeosciences.net/14/5099/2017/ Biogeosciences, 14, 5099–5114, 2017
>
> ---
>
> 5104 J. D. Hemingway et al.: Organic carbon activation energy and isotope composition
> Table 2. Narayani POC RPO temperature ranges, carbon masses, δ13C, Fm, and E for each fraction, f . All masses and isotope values are
> blank corrected following Hemingway et al. (2017). See Eqs. (41)–(42) for E calculations.
> f T mf δ13Cf Fmf E
> (◦C) (μg C) (‰ VPDB)a (kJ mol−1)b
> min. max. mean SD mean SD mean SD Ef σf
> 1 150 310 68.4 0.7 −29.5 0.2 0.891 0.004 134.4 8.1
> 2 310 367 105.6 1.1 −28.1 0.2 0.795 0.002 147.9 7.1
> 3 367 412 82.4 0.8 −26.7 0.2 0.676 0.003 159.0 7.5
> 4 412 475 92.6 0.9 −25.1 0.2 0.464 0.003 173.1 8.5
> 5 475 545 85.6 0.9 −25.3 0.2 0.342 0.003 190.6 10.9
> 6 545 610 98.4 1.0 −24.3 0.2 0.107 0.002 209.7 10.7
> 7 610 661 101.5 1.0 −22.9 0.2 0.022 0.002 223.4 8.0
> 8 664 725 125.6 1.3 −21.8 0.2 0.014 0.002 231.5 7.1
> 9 725 997 86.6 0.9 −23.5 0.2 0.042 0.002 260.5 17.7
> a δ13Cf is additionally corrected following Hemingway et al. (2017) to ensure that the mass-weighted mean
> matches the measured bulk value. b Assuming L-curve best-fit λ value and ω = 10 × 1010 s−1.
> Substituting Eq. (4) into Eq. (6), this can be written as
> G(t) =
> n∑
> i=1
> gi (0)e−κi (t). (7)
> We then define G0, the initial OC mass present in the entire
> sample, as the sum of initial mass contained in each compo-
> nent:
> G0 =
> n∑
> i=1
> gi (0). (8)
> Finally, we define pi (0), the fraction of total carbon initially
> contained in component i, as
> pi (0) = gi (0)
> G0
> (9)
> and note that
> n∑
> i=1
> pi (0) = 1. (10)
> Substituting Eq. (9) into Eq. (7) yields
> G(t)
> G0
> =
> n∑
> i=1
> pi (0)e−κi (t), (11)
> which describes the evolution of the fraction of initial carbon
> remaining at any time. The fraction of OC initially present
> within each component, pi (0), can be determined by fitting
> Eq. (11) to the observed G(t) profile measured by the RPO
> instrument. While informative, this discrete description of
> the model suffers from two major limitations: (i) n must be
> set a priori or determined empirically (Boudreau and Rud-
> dick, 1991) and (ii) any noise recorded in the data will result
> in large uncertainty in best-fit pi (0) and Ei values (Forney
> Table 3. JGOFS RPO temperature ranges, carbon masses, and δ13C
> for each fraction, f . All masses and isotope values are blank cor-
> rected following Hemingway et al. (2017).
> f T mf δ13Cf
> (◦C) (μg C) (‰ VPDB)∗
> min. max. mean SD mean SD
> 1 163 363 38.5 0.4 −20.1 0.2
> 2 363 435 45.9 0.5 −10.3 0.2
> 3 435 543 217.6 2.2 −0.4 0.2
> 4 543 597 154.4 1.5 0.3 0.2
> 5 597 720 497.7 5.0 0.9 0.2
> ∗ δ13Cf is additionally corrected following Hemingway et al.
> (2017) to ensure that the mass-weighted mean matches the
> measured bulk value.
> and Rothman, 2012b). To circumvent the first of these is-
> sues, we derive a more general description of non-isothermal
> first-order decay that does not assume a finite set of com-
> ponents with unique Ei , but rather allows E to vary contin-
> uously (Boudreau, 1997; Braun and Burnham, 1987; Burn-
> ham and Braun, 1999; Cramer, 2004). Limitation (ii) is then
> solved using Tikhonov regularization (Sect. 4.2; Forney and
> Rothman, 2012b; Hansen, 1994).
> 3.2 Continuous model
> In the continuous model, discrete components gi (t), κi (t),
> and Ei are replaced by continuous variables g(t, E), κ(t, E),
> and E, respectively (Table 1). Analogous to Eq. (3), we cal-
> culate the decay of OC associated with an infinitesimal range
> dE about any nonnegative value of E following first-order
> Arrhenius kinetics as
> Biogeosciences, 14, 5099–5114, 2017 www.biogeosciences.net/14/5099/2017/
>
> ---
>
> J. D. Hemingway et al.: Organic carbon activation energy and isotope composition 5105
> dg(t, E)
> dt = −ω exp
> [
> − E
> RT (t)
> ]
> g(t, E). (12)
> The mass of carbon associated with any value of E that re-
> mains unreacted at time t is then calculated by integrating
> Eq. (12) to obtain
> g(t, E) = g(0, E)e−κ(t,E), (13)
> where g(0, E) is the initial mass of carbon associated with
> activation energy value E and
> κ(t, E) = ω
> t∫
> 0
> exp
> [
> − E
> RT (t′)
> ]
> dt′. (14)
> The total carbon remaining at time t can now be written as
> the integral of g(t, E) over all possible values of E as
> G(t) =
> ∞∫
> 0
> g(t, E)dE. (15)
> Substituting Eq. (13) into Eq. (15), we obtain
> G(t) =
> ∞∫
> 0
> g(0, E)e−κ(t,E)dE. (16)
> Analogous to Eq. (9), we then define the fraction of total car-
> bon initially associated with any value of E as
> p(0, E) = g(0, E)
> G0
> , (17)
> where
> ∞∫
> 0
> p(0, E)dE = 1. (18)
> Substituting Eq. (17) into Eq. (16) yields
> G(t)
> G0
> =
> ∞∫
> 0
> p(0, E)e−κ(t,E)dE. (19)
> The distribution of p(0, E) over all values of E describes the
> initial probability density function (pdf) of E that will lead
> to the observed OC decay profile when a sample is analyzed
> in the RPO instrument. As RPO analysis proceeds, this pdf
> must evolve with time to reflect the fact that some carbon
> has been remineralized to CO2. Like g(t, E), p(t, E) follows
> first-order Arrhenius kinetics according to
> dp(t, E)
> dt = −ω exp
> [
> − E
> RT (t)
> ]
> p(t, E), (20)
> where p(t, E) is the fraction of initial carbon mass that re-
> mains associated with E at time t. This can be obtained by
> integrating Eq. (20) from an initial time t = 0:
> p(t, E) = p(0, E)e−κ(t,E). (21)
> This implies that the carbon initially remineralized to CO2
> must be associated with the lowest E values, as low E will
> lead to a κ(t, E) term in Eq. (21) that approaches zero most
> rapidly. Put differently, OC that is described by higher E val-
> ues will resist remineralization until more time has passed
> and therefore higher temperatures have been reached – i.e., it
> is more thermally recalcitrant.
> 3.3 First-order verification
> Because the distributed activation energy model is a specific
> case of nth-order non-isothermal kinetic models (Braun and
> Burnham, 1987; White et al., 2011), we must verify that
> carbon degradation within the RPO instrument behaves ac-
> cording to a superposition of parallel first-order reactions
> rather than higher-order processes. By replacing g(t, E) with
> G0p(t, E) on the right-hand side of Eq. (12), it can be seen
> that
> dg(t, E)
> dt = −G0ω exp
> [
> − E
> RT (t)
> ]
> p(t, E). (22)
> By integrating over all nonnegative values of E and utilizing
> the definition of G(t) from Eq. (15), this can be written as
> dG(t)
> dt = −G0
> ∞∫
> 0
> ω exp
> [
> − E
> RT (t)
> ]
> p(t, E)dE. (23)
> The first-order model describes dG(t)/dt as a linear function
> of G0 multiplied by an integral term that depends on p(t, E)
> but is independent of G0. In contrast, if carbon decompo-
> sition within the RPO instrument were to follow a higher-
> order process, then the relationship between dG(t)/dt and
> G0 would be nonlinear and would evolve as a function of
> time (Follett et al., 2014). If we define
> m(t) =
> ∞∫
> 0
> ω exp
> [
> − E
> RT (t)
> ]
> p(t, E)dE, (24)
> then the carbon decay at time t as predicted by parallel first-
> order kinetics simplifies to
> dG(t)
> dt = −G0m(t). (25)
> Therefore, similar to the isothermal case (Follett et al., 2014),
> a superposition of parallel first-order decay reactions will re-
> sult in a linear relationship between dG(t)/dt and G0 with a
> zero intercept and a time-dependent slope. Thus, m(t) can be
> interpreted as the G0-normalized OC decay rate at time t.
> www.biogeosciences.net/14/5099/2017/ Biogeosciences, 14, 5099–5114, 2017
>
> ---
>
> 5106 J. D. Hemingway et al.: Organic carbon activation energy and isotope composition
> We verify that OC remineralization within the RPO instru-
> ment follows parallel first-order kinetics by assessing the lin-
> earity between Narayani POC dG(t)/dt and G0 at any time
> t across a range of G0 values. For four arbitrarily chosen
> time points, this relationship is linear with an ordinary least
> squares R2 ≥ 0.999, resulting in identical G0-normalized
> thermograms within analytical uncertainty (Fig. 4a–b). Thus,
> the decay of complex OC mixtures contained in carbonate-
> free samples during RPO analysis can indeed be accurately
> described as a superposition of parallel first-order reactions.
> 3.4 A note of caution on carbonates
> While most RPO studies to date have isolated OC by acid-
> ifying to remove carbonates (e.g., Rosenheim et al., 2008,
> 2013; Rosenheim and Galy, 2012; Schreiner et al., 2014;
> Bianchi et al., 2015), it has been argued that acid hydroly-
> sis and/or dissolution of clay minerals during acid treatment
> can alter the OC chemical bonding environment and there-
> fore affect thermal stability (Plante et al., 2013). While ana-
> lyzing samples without acid treatment can circumvent these
> issues, the effect of carbonates on decay kinetics has not yet
> been considered. To test if carbonate-rich samples follow
> parallel first-order kinetics, we analyzed JGOFS sediment
> for a range of G0 values (Fig. 4c–d). Prior to T ≈ 500 ◦C
> (corresponding to t ≈ 4500 s), when δ13C values of eluted
> CO2 indicate a predominantly OC source (Table 3; Fig. 2b),
> dG(t)/dt can be accurately described as a linear function of
> G0 (R2 ≥ 0.999). However, as carbonate begins to decom-
> pose above T ≈ 500 ◦C, the relationship between dG(t)/dt
> and G0 becomes nonlinear and the carbonate peak shifts to-
> ward higher t with increasing G0 (Fig. 4d).
> To investigate if non-first-order decomposition is an in-
> trinsic property of CaCO3 or if this is due to interactions
> with other materials within the sample (so-called “matrix ef-
> fects”), we analyzed a pure Icelandic spar CaCO3 laboratory
> standard at multiple masses (G0 = 258, 492, 1014 μg C; β =
> 5 ◦C min−1; not shown). Results indicate that pure carbon-
> ate, unlike JGOFS sediment, does follow first-order kinetics
> with a maximum decomposition rate occurring at 700 ± 6 ◦C
> independent of G0. Interaction with reduced organic carbon,
> corresponding hetero-atoms (e.g., N, P, S), or trace metals
> contained within the sample matrix are therefore the likeli-
> est cause of non-first-order CaCO3 decomposition when an-
> alyzing environmental samples. Thus, while avoiding the is-
> sues of acid treatment, the presence of carbonate will result
> in thermograms that cannot be accurately described by the
> model presented here, and we therefore argue in favor of acid
> treatment when using the RPO instrument to determine reac-
> tion energetics of carbonate-containing samples.
> 4 Finding the regularized inverse solution
> Following Forney and Rothman (2012a, b), we present a
> method to estimate p(0, E) by finding an inverse solution to
> Eq. (19). In contrast to previous solutions (Braun and Burn-
> ham, 1987; Burnham and Braun, 1999; Cramer, 2004), this
> approach does not require an a priori assumption about the
> form of p(0, E) (e.g., Gaussian). Because this problem is
> sensitive to noise at the level of our analytical uncertainty
> (Forney and Rothman, 2012b), we seek a smooth solution
> using Tikhonov regularization (Sect. 4.2; Forney and Roth-
> man, 2012b; Hansen, 1994).
> To numerically calculate p(0, E), we discretize the con-
> tinuous variable t over the time course of the experiment into
> a vector t containing nt nodes such that
> 1tj = 1
> 2
> (tj +1 − tj −1
> ) , j = 2, . . ., nt − 1. (26)
> For j = 1 and j = nt , tj −1 and tj +1 in Eq. (26) are, respec-
> tively, replaced by tj since t is undefined outside of this
> range. For generality, and because the distributed activation
> energy model is frequently applied over geologic timescales
> with nonuniformly distributed time measurements (Braun
> and Burnham, 1987; Burnham and Braun, 1999; Cramer,
> 2004), Eq. (26) does not require a uniform time step (i.e., it is
> possible that 1tj 6 = 1ti6 =j ). Similarly, we generate a vector
> E containing nE nodes over the range values considered for
> the model solution such that
> 1E = Emax − Emin
> nE
> , (27)
> noting that E is uniformly spaced since this vector is not
> constrained by observations. We constrain E to be within
> 50–350 kJ mol−1 based on published biomass and petroleum
> E ranges (Braun and Burnham, 1987; Burnham and Braun,
> 1999; Cramer, 2004; White et al., 2011).
> It can be seen from Eq. (19) that the model can be sepa-
> rated into two components: (i) p(0, E) and (ii) the exponenti-
> ated, time-integrated decay coefficient, exp[κ(t, E)]. Analo-
> gous to the Laplace transform for the isothermal reactive con-
> tinuum model (Forney and Rothman, 2012b), exp[κ(t, E)]
> determines the fraction of carbon initially associated with
> an activation energy value E that has decayed by time t.
> While this integral can be calculated analytically for a con-
> stant ramp rate β, here we approximate the solution nu-
> merically so that our model can be applied to any time–
> temperature history. Thus, we populate a matrix A by cal-
> culating exp[κ(t, E)] for each tj and El contained in t and E
> as
> Aj,l = exp
> {
> −
> j∑
> u=1
> ω exp
> [
> − El
> RT (tu)
> ]
> 1tu
> }
> 1E,
> j = 1, . . ., nt ,
> l = 1, . . ., nE . (28)
> Biogeosciences, 14, 5099–5114, 2017 www.biogeosciences.net/14/5099/2017/
>
> ---
>
> J. D. Hemingway et al.: Organic carbon activation energy and isotope composition 51070.2
> 0.0
> 0.1
> Decay rate (μg s )-1
> (a)
> 0.0
> 1.0
> 2.0
> 3.0
> 0.0
> 6.0
> 4.0
> 2.0
> 8.0
> 10.0
> G0
> -normalized decay rate,m(t) ×10 4 (s-1 ) (b)
> 2000 400 600 800 1000 20000 4000 6000 8000 10 000
> G0 (μg C)
> 1.0
> 0.0
> 0.2
> 0.4
> 0.6
> 0.8
> Decay rate (μg s )-1
> (c)
> Time (s)
> G0
> -normalized decay rate, m(t) ×10 4 (s-1 ) (d)
> G0 = 268 μg C
> G0 = 533 μg C
> G0 = 828 μg C
> G0= 98 μg C
> G0 = 252 μg C
> G0 = 951 μg C
> t = 3000 s
> t = 4500 s
> t = 6000 s
> t = 6450 s
> t = 600 s
> t = 4500 s
> t = 6300 s
> t = 7500 s
> Figure 4. First-order kinetic assessment. Panels (a) and (c) show decay rate, dG(t)/dt, vs. G0 relationships at four arbitrarily chosen time
> points (including best-fit regression lines, dashed lines) and panels (b) and (d) show the mass-normalized decay rates (termed m(t) in Eqs. 24–
> 25) at all time points for (a)–(b) Narayani POC and (c–d) JGOFS sediment. Linear relationships and nearly identical normalized decay rates
> in panels (a–b) confirm the first-order nature of OC decay, while nonlinear relationships and a shifting carbonate peak in panels (c–d) indicate
> non-first-order CaCO3 decay kinetics. For each time point in panel (a), the regression slope is equivalent to m(t) for that time point as shown
> in panel (b).
> The A matrix is often termed the model “design matrix”. We
> then calculate the fraction of initial carbon remaining at each
> time point as
> G(t)
> G0
> = 1 − α(t), (29)
> where α(t) is the G0-normalized, integrated RPO thermo-
> gram at time t. We generate a discretized vector g by inter-
> polating G(t)/G0 onto each tj in t (j = 1, . . ., nt ). Our model
> can then be written in matrix form as
> g = A · p, (30)
> where p is an unknown, discretized vector of p(0, E) with
> length nE such that
> pl = 1
> 1E
> El + 1
> 2 1E
> ∫
> El − 1
> 2 1E
> p(0, E)dE, l = 1, . . ., nE . (31)
> While Eq. (30) can be solved for p by multiplying g by the
> computed inverse of A, if g contains noisy data this may re-
> sult in negative values of pl that are mathematically possible
> but physically unreasonable (Forney and Rothman, 2012b).
> Here, we find the solution that satisfies
> min
> p ‖g − A · p‖ ≡
> 
>  nt∑
> j =1
> (
> gj −
> nE∑
> l=1
> Aj,l pj
> )2
> 
> 1
> 2
> , (32)
> subject to the constraints
> pl ≥ 0, l = 1, . . ., nE (33)
> and
> nE∑
> l=1
> pl = 1, l = 1, . . ., nE (34)
> using the nonnegative least squares algorithm of Lawson and
> Hanson (1995) as implemented by the SciPy package for
> Python. Equations (32)–(34) describe the model solution that
> minimizes the norm of the residual error (i.e., the RMSE)
> while fulfilling the constraints that p is nonnegative and sums
> to unity.
> www.biogeosciences.net/14/5099/2017/ Biogeosciences, 14, 5099–5114, 2017
>
> ---
>
> 5108 J. D. Hemingway et al.: Organic carbon activation energy and isotope composition
> 4.1 Choice of frequency factor
> In order to construct the A matrix and solve for p, our method
> requires that the Arrhenius frequency factor ω is prescribed
> a priori. There exists significant discussion in the literature
> on the best choice of ω, as multiple values can describe
> laboratory results equally well but will result in drastically
> different predictions of OC degradation rates over geologic
> timescales (Braun and Burnham, 1987; Dieckmann, 2005).
> Furthermore, it has been argued that ω represents a vari-
> able change in entropy associated with the decay of specific
> organic compounds and should therefore be parameterized
> as a function of E (the so-called “kinetic compensation ef-
> fect” or KCE; Dieckmann, 2005; Lakshmanan et al., 1991;
> Tang et al., 2000). For example, a linear ω increase with
> E from ≈ 108 s−1 (E = 175 kJ mol−1) to ≈ 1026 s−1 (E =
> 400 kJ mol−1) has been utilized to better predict petroleum
> formation rates (Dieckmann, 2005). To circumvent the issue
> of multiplicity, and to account for the KCE, Miura and Maki
> (1998) developed a method to estimate the best-fit ω for each
> E value by comparing the shift in elution temperatures when
> a sample is analyzed at multiple ramp rates. However, be-
> cause this approach is based on large extrapolations in 1/T
> vs. β/T 2 space, it is highly sensitive to noise in temperature
> and β measurements (Burnham and Braun, 1989).
> To select a best-fit ω, we construct the A matrix for a range
> of ω values and determine the residual error norm between
> measured G(t)/G0 and that predicted by the resulting p vec-
> tor determined by Eqs. (32)–(34). We consider the KCE by
> calculating ω as a function of E according to
> log10ω = (KCE slope)E + (KCE intercept). (35)
> Resulting residual errors for Narayani POC using a range
> of KCE slopes and intercepts are shown in Fig. 5 (β =
> 5 ◦C min−1, E ranging from 50 to 350 kJ mol−1). By set-
> ting an “acceptable” residual error norm cutoff of ≤ 10−4,
> it can be seen that there exist multiple KCE slope and inter-
> cept combinations that can equally fit the observed data. Ad-
> ditionally, we estimate the best-fit ω using a range of ramp
> rates (β = 2, 5, and 10 ◦C min−1) following the method of
> Miura and Maki (1998) (Fig. 5, white circle). While this es-
> timate falls outside of the cutoff range, likely due to noise in
> temperature and β measurements, it results in a KCE slope
> near zero and suggests that ω is constant during RPO ox-
> idation of this sample. To accurately compare RPO results
> between samples, we therefore select a constant ω value of
> 1010 s−1, well within the cutoff range, for samples analyzed
> herein (Fig. 5, red star). While a different choice of ω will
> shift p(0, E) to higher or lower absolute values of E, we em-
> phasize that it will not affect the relative distribution of E
> and that only relative changes in E between RPO fractions
> should be interpreted.
> For example, a shift in ω from a constant value of 107 to
> 1012 s−1 results in an increase in the mean of the pdf of E,Residual error norm, ||g - A·p||
> 10-4 10-3 10-2 10-1
> 0 5 10 15 20
> KCE intercept
> 0.04
> 0.05
> 0.00
> 0.01
> 0.02
> 0.03
> KCE slope
> Figure 5. Frequency factor assessment. Model residual error norm
> using a range of KCE slopes and intercepts for Narayani POC
> (β = 5 ◦C min−1). Each pixel represents the best-fit solution to
> Eqs. (32)–(34) for a given ω as determined by Eq. (35). “Accept-
> able” fits with a residual error norm ≤ 10−4 are contained within
> the red dotted line. Estimated result using the method of Miura
> and Maki (1998) for three ramp rates (β = 2, 5, and 10 ◦C min−1)
> is plotted as a white circle, while the point corresponding to ω =
> 1010 s−1 (the value chosen for samples in this study) is plotted as a
> red star.
> termed E and calculated as
> E =
> nE∑
> l=1
> El p(0, El )1E, (36)
> from 150 to 224 kJ mol−1 for Narayani POC. However, the
> relative standard deviation of the pdf of E, calculated as σ/E,
> where
> σ 2 = E2 − (E)2, (37)
> remains constant at 20 %. A higher ω value therefore results
> in a broader p(0, E) distribution that is centered at a higher
> mean E value but has no effect on the relative shape of the
> distribution.
> 4.2 Tikhonov regularization
> In principle, after choosing ω and constructing the A ma-
> trix, the pdf of E that best describes an RPO thermogram
> can be determined by solving Eqs. (32)–(34). However, the
> inverse solution is sensitive to noise at the level of RPO in-
> strument precision (±5 ppm CO2, ±5 ◦C; Hemingway et al.,
> 2017), and is therefore ill-posed (Hansen, 1994; Lakshmanan
> et al., 1991). We address this sensitivity to data uncertainty
> using Tikhonov regularization (Hansen, 1994; Forney and
> Rothman, 2012a, b).
> Biogeosciences, 14, 5099–5114, 2017 www.biogeosciences.net/14/5099/2017/
>
> ---
>
> J. D. Hemingway et al.: Organic carbon activation energy and isotope composition 5109
> This approach finds an optimal solution that minimizes
> p(0, E) complexity (as determined by the intensity of fluctu-
> ations, or “roughness”) while maximizing solution accuracy.
> Following Forney and Rothman (2012b), we calculate rough-
> ness as the first derivative of the solution vector:
> ∥
> ∥
> ∥
> ∥
> dp(0, E)
> dE
> ∥
> ∥
> ∥
> ∥ =
> [nE −1∑
> l=2
> ( pl+1 − pl
> 1E
> )2] 1
> 2
> ≡ ‖R · p‖, (38)
> where R is the bi-diagonal first derivative operator matrix
> with dimensions [nE × nE ]. To account for p being equal
> to zero outside the range Emin < E < Emax, we set the first
> and last rows of R to be equal to [1 0] and [0 − 1], re-
> spectively, where 0 refers to a zero vector of length nE − 1.
> Similar to Eq. (32), the regularized inverse problem can then
> be solved for p by including this roughness term in the con-
> strained least squares. That is, we solve
> min
> p ‖g − A · p‖ + λ‖R · p‖, (39)
> for p subject to the constraints presented in Eqs. (33)–(34),
> where λ is a scalar that determines how much to weight the
> roughness ‖R·p‖ relative to the residual error ‖g−A·p‖. The
> best choice of λ is considered to be the value that optimizes
> this balance. As described in Hansen (1994), a common ap-
> proach is to choose the value corresponding to the point of
> maximum curvature in a log − log plot of residual error and
> roughness while allowing λ to range over many orders of
> magnitude (i.e., the so-called “L-curve”). From this point,
> increasing λ strongly increases residual error but has little
> effect on solution roughness, while decreasing λ greatly in-
> creases roughness but has little effect on residual error. Thus,
> here we choose the λ value corresponding to the corner of
> the L-curve for each sample, as exemplified in Fig. 6.
> 4.3 p(0, E): a novel proxy for chemical bond strength
> In order to interpret p(0, E) as an intrinsic property of OC
> contained within a sample, we must show that results do not
> depend on experimental conditions such as ramp rate β and
> initial carbon mass G0. To test this, we analyzed Narayani
> POC using a range of masses (G0 = 268, 533, and 828 μg C)
> and ramp rates (β = 2, 5, and 10 ◦C min−1). Figure 7 shows
> that the regularized pdf’s of E are nearly identical across all
> experimental conditions. This supports the hypothesis that
> the p(0, E) distribution is an intrinsic property of a given
> sample when exposed to a particular oxidation pathway (e.g.,
> thermal decay). Although there exist small differences be-
> tween individual analyses due to measurement uncertainty
> and variability in best-fit λ values (ranging from 0.044 to
> 0.448, n = 5), the main features of p(0, E) are robust across
> all conditions. Note that the p(0, E) distribution (Fig. 7)
> broadly resembles the initial thermogram shape (Fig. 2a), al-
> beit with more defined features and a higher roughness. This
> is a result of the fact that OC associated with each E value10-5 10-4 10-3 10-2 10-1
> Residual error norm, ||g - A·p||
> 10-1
> 10-5
> 10-4
> 10-3
> 10-2
> Roughness norm, ||Rp||
> Best-fit λ = 0.448
> log10 (resid.) = -3.910
> log10 (rough.) = -3.429
> Figure 6. Tikhonov regularization L-curve for Narayani POC (β =
> 5 ◦C min−1). The black line represents the range of roughness and
> residual error norms that are the result of solving Eq. (39) for p
> using multiple λ values ranging from 0.001 to 100. The white circle
> corresponds to the point of maximum curvature along this line, and
> is thus deemed the best-fit λ value (see Hansen, 1994, and Forney
> and Rothman, 2012b, for further details on generating the L-curve
> and theory behind Tikhonov regularization).
> will decay over a wide temperature range within the RPO in-
> strument, thus resulting in a “smoothed” thermogram relative
> to p(0, E) (Cramer, 2004).
> While further study is required to assess the general ap-
> plicability of this technique, we propose p(0, E) as a novel
> proxy to describe the distribution of carbon bond strength
> (Braun and Burnham, 1987; Burnham and Braun, 1999;
> Cramer, 2004). For example, Narayani POC is known to inte-
> grate recently fixed biomass, pre-aged soils, and eroded rock-
> derived material (Galy et al., 2008, 2011; Galy and Eglinton,
> 2011; Rosenheim and Galy, 2012). Such integration should
> lead to large chemical diversity and a broad, complex E dis-
> tribution, as is observed (Fig. 7). Furthermore, slow envi-
> ronmental turnover has been shown to enhance the diver-
> sity of chemical bonds due to a combination of microbial
> alterations (Schmidt et al., 2011), OC aggregation (Keil and
> Mayer, 2014), and stabilization by mineral surfaces (Keil
> and Mayer, 2014; Mikutta et al., 2006). Thus, OC reactivity
> within the RPO instrument and the resulting E distribution
> likely reflect both the strength of covalent bonds between
> carbon atoms and interactions with mineral surfaces (Keil
> and Mayer, 2014; Mikutta et al., 2006). We therefore pro-
> pose combining p(0, E) with serial oxidation isotope mea-
> surements to test the effects of mineral interactions and se-
> lective preservation on OC turnover time.
> www.biogeosciences.net/14/5099/2017/ Biogeosciences, 14, 5099–5114, 2017
>
> ---
>
> 5110 J. D. Hemingway et al.: Organic carbon activation energy and isotope composition100 150 200 250 300
> E (kJ mol -1
> )
> 0.020
> 0.000
> 0.005
> 0.010
> 0.015
> p(0,E)
> Mean (n = 5)
> SD (n = 5)
> Figure 7. Regularized p(0, E) distribution for Narayani POC.
> Mean (black line) and standard deviation (gray shaded region) of
> p(0, E) analyzed using a range of G0 and β values (n = 5). Narrow
> standard deviation indicates that model results are independent of
> experimental conditions.
> 5 Relating E and isotope composition
> 5.1 Determining the distribution of E within
> each RPO fraction
> To relate p(0, E) distributions to RPO isotope measure-
> ments, we calculate the subset of the pdf of E that is con-
> tained within each RPO fraction. Because we can predict the
> evolution of p(t, E) at any time t following Eq. (21), this can
> be calculated as
> 5f (E) = p(t1, E) − p(t2, E), f = 1, . . ., nf , (40)
> where nf is the number of RPO fractions collected for a
> given sample, 5f (E) is the subset of p(0, E) contained in
> RPO fraction f , and t1 and t2 are the initial and final time
> points, respectively, of CO2 collection for RPO fraction f .
> Resulting 5f (E) distributions for Narayani POC are shown
> in Fig. 8. Finally, in order to generate E vs. δ13C and E vs.
> Fm scatter plots, we calculate the mean E value contained in
> each RPO fraction as
> Ef =
> nE∑
> l=1
> El 5f (El )1E, f = 1, . . ., nf (41)
> and the standard deviation of E contained in each RPO frac-
> tion as σf , where
> σ 2
> f = E2f − (Ef
> )2, f = 1, . . ., nf . (42)
> Resulting Ef and σf values are reported in Table 2. It can
> be seen in Fig. 8 that 5f (E) distributions do not follow any
> particular form (e.g., Gaussian) and are highly overlapping,
> reflecting the fact that the CO2 isotope composition for each
> RPO fraction is itself a weighted average of multiple sources.E (kJ mol -1
> )
> 100 150 200 250 300
> Πf(E)
> 1
> 2
> 3
> 4
> 5
> 6
> 7
> 8
> 9
> f
> Figure 8. 5f (E) distributions for Narayani POC (f = 1, . . ., 9).
> Each 5f (E) represents the range of E values contained within
> RPO fraction f . The sum of all 5f (E) distributions shown here
> thus yields the p(0, E) distribution shown in Fig. 7. Distributions
> have been staggered along the y axis for visual clarity. 5f (E) dis-
> tributions do not follow any predictable functional form and are
> highly overlapping due to the fact that OC associated with a given
> E value decays over a wide time interval (Cramer, 2004).
> 5.2 Kinetic isotope fractionation
> While not necessary for Fm because it is fractionation-
> corrected by definition (Reimer et al., 2004), it is important
> to correct for any kinetic isotope effects occurring within the
> RPO instrument before interpreting δ13C as a carbon source
> tracer (Hemingway et al., 2017). If kinetic fractionation is
> large, as has been observed both during thermogenic methane
> formation (Tang et al., 2000; Cramer, 2004) and dissolved
> OC oxidation by UV light (Oba and Naraoka, 2008), then
> this effect could overprint carbon source δ13C signals. How-
> ever, when directly measured using single-compound stan-
> dards, Hemingway et al. (2017) concluded that 13C fraction-
> ation within the RPO instrument must be ≤ 2 ‰. Still, we
> correct the measured δ13C values of each RPO fraction using
> the ratio of carbon-normalized 13C and 12C decomposition
> rates at each time point according to
> 13/12r(t) =
> ( d13G(t)
> dt
> )
> ( d12G(t)
> dt
> )
> ( 12G0
> 13G0
> )
> , (43)
> where we have added a preceding 12 or 13 superscript to
> specify isotope-specific variables. Following the Arrhenius
> equation, 13/12r(t) can be written as a function of the differ-
> ence in E between 13C- and 12C-containing molecules:
> 13−121E = 13E − 12E. (44)
> Although 13−121E is likely not identical for all compounds
> due to differences in the entropy and enthalpy of isotope sub-
> Biogeosciences, 14, 5099–5114, 2017 www.biogeosciences.net/14/5099/2017/
>
> ---
>
> J. D. Hemingway et al.: Organic carbon activation energy and isotope composition 5111
> stitution (Tang et al., 2000), the estimated range of values
> for RPO analysis is small (0.3 × 10−3–1.8 × 10−3 kJ mol−1;
> Hemingway et al., 2017). We therefore assume a 13−121E
> value of 1.8 × 10−3 kJ mol−1 for all RPO fractions, noting
> that a choice of 0.3 × 10−3 kJ mol−1 would result in δ13C
> values that are identical to those calculated here within ana-
> lytical uncertainty.
> Values of 13/12r(t) can be determined using the ratio of
> carbon-normalized, isotope-specific decay rates by substitut-
> ing p(0, 12E) and p(0, 13E) for p(0, E) in Eq. (19). Because
> carbon is present as ≈ 99 % 12C, we set p(0, 12E) equal to
> p(0, E) such that
> d12G(t)
> dt = dG(t)
> dt . (45)
> Corresponding d13G(t)/dt can then be determined using
> p(0, 13E) = p(0, E + 13−121E). (46)
> 13C-containing molecules decay at rates governed by a pdf
> of E that is identical to p(0, E) but has been shifted by
> 1.8 × 10−3 kJ mol−1. We then correct the measured δ13C val-
> ues of each RPO fraction f according to
> δ13Ccorrected
> f =
> 1
> 13/12r(t)av
> f
> (
> δ13Cf + 1000
> [13/12r(t)av
> f − 1
> ])
> ,
> f = 1, . . ., nf , (47)
> where 13/12r(t)av
> f is the average 13/12r(t)f value over the
> time of collection for RPO fraction f . For the samples an-
> alyzed here, 13/12r(t) is initially ≈ 0.999, indicating slightly
> faster 12C decay at low temperatures, and gradually increases
> to ≈ 1.002 when G(t)  0.01G0, as has been described pre-
> viously (Cramer, 2004; Hemingway et al., 2017). Resulting
> kinetic fractionation corrections are near or within analytical
> uncertainty, with absolute δ13C values for all RPO fractions
> shifted by < 0.2 ‰.
> 5.3 Comparing E to δ13C and Fm
> Finally, we describe a framework to directly relate OC reac-
> tivity and isotope distributions by plotting Ef for each RPO
> fraction vs. the corresponding measured δ13C and Fm val-
> ues (Table 2). Resulting relationships, as well as plant-wax
> fatty acid isotope values (Galy et al., 2011; Galy and Eglin-
> ton, 2011), are shown in Fig. 9. Within this framework, it
> can be seen that Narayani POC must contain at least two
> end members with drastically different isotope compositions
> and unique yet overlapping E distributions. Previous studies
> have shown that ≈ 20 ± 5 % of OC contained in this sam-
> ple is derived from the erosion of carbon-rich bedrock (Galy
> et al., 2008; Rosenheim and Galy, 2012). Rock-derived OC
> is the likeliest source of high-E, low-Fm material, as this end
> member is 14C-free by definition. Plant-wax FA δ13C and Fm-20
> -32
> -24
> -22
> -26
> -30
> -28
> δ13
> C (‰ VPDB)
> (a)
> 150100 200 250 300
> E (kJ mol -1 )
> 1.0
> 0.0
> 0.2
> 0.4
> 0.6
> 0.8
> Fm
> (b)
> Plant-wax fatty acids
> Plant-wax fatty acids
> Figure 9. E vs. isotope relationships. (a) E vs. δ13C and (b) E vs.
> Fm for Narayani POC. All isotope values have been corrected for
> blank carbon contribution following Hemingway et al. (2017), and
> δ13C values have additionally been corrected for kinetic fractiona-
> tion. Gray lines and shading are the plant-wax fatty acid biomarker
> isotope values (mean ±1 SD analytical uncertainty; Galy et al.,
> 2011; Galy and Eglinton, 2011). Note that plant-wax fatty acids are
> known to contain less 13C (lower δ13C values) than corresponding
> bulk biospheric OC. Each point is plotted at E = Ef . Error bars
> in E are equal to σf , while δ13C and Fm analytical uncertainty is
> always smaller than point marker and is therefore not shown.
> values are similar to those for low-E RPO fractions (Fig. 9),
> suggesting that vascular plant OC is the source of low-E ma-
> terial. Narayani POC isotope trends are thus consistent with
> predominantly biospheric carbon below ≈ 150 kJ mol−1, a
> mixed region from ≈ 150 to 200 kJ mol−1, and exclusively
> rock-derived OC above ≈ 200 kJ mol−1. This result provides
> initial evidence for the utility of RPO E vs. isotope relation-
> ships to directly relate the distribution of OC sources, en-
> vironmental turnover times, and chemical bonding environ-
> ments.
> www.biogeosciences.net/14/5099/2017/ Biogeosciences, 14, 5099–5114, 2017
>
> ---
>
> 5112 J. D. Hemingway et al.: Organic carbon activation energy and isotope composition
> 6 Conclusions
> In this study, we present a regularized, inverse method to de-
> termine the distribution of E, a measure of OC reactivity,
> when natural organic matter is exposed to serial oxidation.
> We show that OC decay follows parallel, first-order kinetics.
> In contrast, the kinetics of carbonate oxidation cannot be con-
> strained due to matrix effects and we therefore recommend
> acidification to remove carbonates prior to RPO analysis. We
> propose that p(0, E), the distribution of E contained within
> a sample, is a useful proxy to describe the range of OC bond-
> ing environments. Importantly, our method does not require
> a priori assumptions about the distributional form of p(0, E).
> Finally, we determine the subset of E contained within each
> RPO fraction in order to directly relate reaction energetics
> with the distribution of carbon isotope compositions within
> a complex OC mixture. We suggest that E vs. isotope re-
> lationships can provide new insight into understanding the
> compositional controls on OC source and residence time, al-
> though we note that further study is required in order to test
> the general applicability of this result.
> Code and data availability. All thermogram data are available
> in the Supplement. The open-source “rampedpyrox” package
> is accessible using the Python Package Index (Hemingway,
> 2017, https://doi.org/10.5281/zenodo.839815, http://pypi.python.
> org/pypi/rampedpyrox).
> The Supplement related to this article is available online
> at https://doi.org/10.5194/bg-14-5099-2017-supplement.
> Author contributions. JDH, SZR, and VVG performed all labora-
> tory measurements; JDH, VVG, and DHR analyzed the data; JDH
> and DHR developed the inverse model; JDH wrote the paper with
> input from all authors.
> Competing interests. The authors declare that they have no conflict
> of interest.
> Acknowledgements. Constructive comments by reviewers
> David Burdige and Bernard Boudreau, as well as associate editor
> Jack Middelburg, greatly improved this paper. We thank the
> entire NOSAMS facility, especially Ann McNichol, Al Gagnon,
> Steven Beaupré, and Mary Lardie, for technical assistance with
> the RPO instrument. This research was supported by the NSF
> Graduate Research Fellowship Program grant no. 2012126152 (Jor-
> don D. Hemingway), NASA Astrobiology grant no. NNA13AA90A
> and NSF grant no. EAR-1338810 (Daniel H. Rothman), and the
> WHOI Independent Study Award (Valier V. Galy).
> Edited by: Jack Middelburg
> Reviewed by: Bernard Boudreau and David Burdige
> References
> Beaupré, S. R., Druffel, E. R., and Griffin, S.: A low-blank photo-
> chemical extraction system for concentration and isotopic anal-
> yses of marine dissolved organic carbon, Limnol. Oceanogr.-
> Meth., 5, 174–184, 2007.
> Beaupré, S. R., Mahmoudi, N., and Pearson, A.: IsoCaRB: A novel
> bioreactor system to characterize the lability and natural carbon
> isotopic (14C, 13C) signatures of microbially respired organic
> matter, Limnol. Oceanogr.-Meth., 14, 668–681, 2016.
> Bianchi, T. S.: The role of terrestrially derived organic carbon in the
> coastal ocean: A changing paradigm and the priming effect, P.
> Natl. Acad. Sci. USA, 108, 19473–19481, 2011.
> Bianchi, T. S., Galy, V. V., Rosenheim, B. E., Shields, M., Cui, X.,
> and Van Metre, P.: Paleoreconstruction of organic carbon inputs
> to an oxbow lake in the Mississippi River watershed: Effects of
> dam construction and land use change on regional inputs, Geo-
> phys. Res. Lett., 42, 7983–7991, 2015.
> Boudreau, B. P.: Diagenetic models and their implementation, Vol.
> 505, Springer, New York, NY, 1st Edn., 1997.
> Boudreau, B. P. and Ruddick, B. R.: On a reactive continuum rep-
> resentation of organic matter diagenesis, Am. J. Sci., 291, 507–
> 538, 1991.
> Braun, R. L. and Burnham, A. K.: Analysis of chemical reaction
> kinetics using a distribution of activation energies and simpler
> models, Energ. Fuel., 1, 153–611, 1987.
> Burdige, D. J.: Preservation of organic matter in marine sedi-
> ments: controls, mechanisms, and an imbalance in sediment or-
> ganic carbon budgets?, Chem. Rev., 107, 467–485, 2007.
> Burnham, A. K. and Braun, R. L.: Development of a detailed model
> of petroleum formation, destruction, and expulsion from lacus-
> trine and marine source rocks, Org. Geochem., 16, 27–39, 1989.
> Burnham, A. K. and Braun, R. L.: Global kinetic analysis of com-
> plex materials, Energ. Fuel., 13, 1–22, 1999.
> Cramer, B.: Methane generation from coal during open system py-
> rolysis investigated by isotope specific, Gaussian distributed re-
> action kinetics, Org. Geochem., 35, 379–392, 2004.
> Dieckmann, V.: Modelling petroleum formation from heteroge-
> neous source rocks: The influence of frequency factors on acti-
> vation energy distribution and geological prediction, Mar. Petrol.
> Geol., 22, 375–390, 2005.
> Follett, C. L., Repeta, D. J., Rothman, D. H., Xu, L., and Santinelli,
> C.: Hidden cycle of dissolved organic carbon in the deep ocean,
> P. Natl. Acad. Sci. USA, 111, 16706–16711, 2014.
> Forney, D. C. and Rothman, D. H.: Common structure in the hetero-
> geneity of plant-matter decay, J. R. Soc. Interf., 9, 2255–2267,
> 2012a.
> Forney, D. C. and Rothman, D. H.: Inverse method for estimat-
> ing respiration rates from decay time series, Biogeosciences, 9,
> 3601–3612, https://doi.org/10.5194/bg-9-3601-2012, 2012b.
> Galy, V. V. and Eglinton, T. I.: Protracted storage of biospheric car-
> bon in the Ganges-Brahmaputra basin, Nat. Geosci., 4, 843–847,
> 2011.
> Biogeosciences, 14, 5099–5114, 2017 www.biogeosciences.net/14/5099/2017/
>
> ---
>
> J. D. Hemingway et al.: Organic carbon activation energy and isotope composition 5113
> Galy, V. V., Beyssac, O., France-Lanord, C., and Eglinton, T. I.:
> Recycling of graphite during Himalayan erosion: A geological
> stabilization of carbon in the crust, Science, 322, 943–945, 2008.
> Galy, V. V., Eglinton, T. I., France-Lanord, C., and Sylva, S. P.: The
> provenance of vegetation and environmental signatures encoded
> in vascular plant biomarkers carried by the Ganges-Brahmaputra
> rivers, Earth Planet. Sc. Lett., 304, 1–12, 2011.
> Hansen, P. C.: Regularization tools: A Matlab package for analysis
> and solution of discrete ill-posed problems, Numer. Algorithms,
> 6, 1–35, 1994.
> Hedges, J. I., Baldock, J. A., Gelinas, Y., Lee, C., Peterson, M.,
> and Wakeham, S. G.: Evidence for non-selective preservation of
> organic matter in sinking marine particles, Nature, 409, 801–804,
> 2001.
> Helfrich, M., Flessa, H., Mikutta, R., Dreves, A., and Ludwig, B.:
> Comparison of chemical fractionation methods for isolating sta-
> ble soil organic carbon pools, Eur. J. Soil Sci., 58, 1316–1329,
> 2007.
> Hemingway, J. D.: rampedpyrox: Open-source
> tools for thermoanalytical data analysis, 2016-,
> https://doi.org/10.5281/zenodo.839815, 2017.
> Hemingway, J. D., Schefuß, E., Dinga, B. J., Pryer, H., and Galy,
> V. V.: Multiple plant-wax compounds record differential sources
> and ecosystem structure in large river catchments, Geochim.
> Cosmochim. Ac., 184, 20–40, 2016.
> Hemingway, J. D., Galy, V. V., Gagnon, A. R., Grant, K. E., Rosen-
> gard, S. Z., Soulet, G., Zigah, P. K., and McNichol, A. P.: As-
> sessing the blank carbon contribution, isotope mass balance, and
> kinetic isotope fractionation of the ramped pyrolysis/oxidation
> istrument at NOSAMS, Radiocarbon, 59, 179–193, 2017.
> Keil, R. G. and Mayer, L. M.: Mineral matrices and organic mat-
> ter, in: Treatise on Geochemistry, edited by: Holland, H. and
> Turekian, K., 337–359, Elsevier Ltd., Amsterdam, the Nether-
> lands, 2014.
> Lakshmanan, C. C., Bennett, M. L., and White, N.: Implications
> of multiplicity in kinetic parameters to petroleum exploration:
> Distributed activation energy models, Energ. Fuel., 5, 110–117,
> 1991.
> Lasaga, A. C., Berner, R. A., and Garrels, R. M.: An improved geo-
> chemical model of atmospheric CO2 fluctuations over the past
> 100 million years, in: The Carbon Cycle and Atmospheric CO2:
> Natural Variations Archean to Present, edited by: Sundquist, E. T.
> and Broecker, W. S., 397–411, American Geophysical Union,
> Washington, D.C., 1985.
> Lawson, C. and Hanson, R.: Solving Least Squares Problems,
> Prentice-Hall, Englewood Cliffs, NJ, 1st Edn., 1995.
> Leifeld, J. and von Lützow, M.: Chemical and microbial activation
> energies of soil organic matter decomposition, Biol. Fert. Soils,
> 50, 147–153, 2014.
> McNichol, A. P., Jones, G. A., Hutton, D. L., Gagnon, A., and Key,
> R. M.: The Rapid Preparation of Seawater 6CO2 for Radiocar-
> bon Analysis at the National Ocean Sciences AMS Facility, Ra-
> diocarbon, 36, 237–246, 1994a.
> McNichol, A. P., Osborne, E. A., Gagnon, A., Fry, B., and Jones,
> G. A.: TIC, TOC, DIC, DOC, PIC, POC – unique aspects in the
> preparation of oceanographic samples for 14C-AMS, Nucl. In-
> strum. Meth. B, 92, 162–165, 1994b.
> Middelburg, J. J.: A simple rate model for organic matter decom-
> position in marine sediments, Geochim. Cosmochim. Ac., 53,
> 1577–1581, 1989.
> Mikutta, R., Kleber, M., Torn, M. S., and Jahn, R.: Stabilization of
> soil organic matter: Association with minerals or chemical recal-
> citrance?, Biogeochemistry, 77, 25–56, 2006.
> Miura, K. and Maki, T.: A simple method for estimating f (E) and
> k0(E) in the distributed activation energy model, Energ. Fuel.,
> 12, 864–869, 1998.
> Oba, Y. and Naraoka, H.: Carbon and hydrogen isotopic fractiona-
> tion of low molecular weight organic compounds during ultravi-
> olet degradation, Org. Geochem., 39, 501–509, 2008.
> Pedler, B. E., Aluwihare, L. I., and Azam, F.: Single bacterial strain
> capable of significant contribution to carbon cycling in the sur-
> face ocean, P. Natl. Acad. Sci. USA, 111, 7202–7207, 2014.
> Plante, A. F., Beaupré, S. R., Roberts, M. L., and Baisden, W. T.:
> Distribution of radiocarbon ages in soil organic matter by thermal
> fractionation, Radiocarbon, 55, 1077–1083, 2013.
> Reimer, P. J., Brown, T. A., and Reimer, R. W.: Discussion: Re-
> porting and calibration of post-bomb 14C data, Radiocarbon, 46,
> 1299–1304, 2004.
> Rosenheim, B. E. and Galy, V. V.: Direct measurement of riverine
> particulate organic carbon age structure, Geophys. Res. Lett., 39,
> L19703, https://doi.org/10.1029/2012GL052883, 2012.
> Rosenheim, B. E., Day, M. B., Domack, E. W., Schrum,
> H., Benthien, A., and Hayes, J. M.: Antarctic sediment
> chronology by programmed-temperature pyrolysis: Methodol-
> ogy and data treatment, Geochem. Geophy. Geosy., 9, Q04005,
> https://doi.org/10.1029/2007GC001816, 2008.
> Rosenheim, B. E., Roe, K. M., Roberts, B. J., Kolker, A. S., Al-
> lison, M. A., and Johannesson, K. H.: River discharge influ-
> ences on particulate organic carbon age structure in the Mis-
> sissippi/Atchafalaya River System, Global Biogeochem. Cy., 27,
> 154–166, 2013.
> Rothman, D. H. and Forney, D. C.: Physical model for the decay
> and preservation of marine organic carbon, Science, 316, 1325–
> 1328, 2007.
> Sayles, F. L., Martin, W. R., Chase, Z., and Anderson, R. F.: Benthic
> remineralization and burial of biogenic SiO2, CaCO3, organic
> carbon, and detrital material in the Southern Ocean along a tran-
> sect at 170◦ West, Deep-Sea Res. Pt. II, 48, 4323–4383, 2001.
> Schmidt, M. W. I., Torn, M. S., Abiven, S., Dittmar, T., Guggen-
> berger, G., Janssens, I. A., Kleber, M., Kögel-Knabner, I.,
> Lehmann, J., Manning, D. A. C., Nannipieri, P., Rasse, D. P.,
> Weiner, S., and Trumbore, S. E.: Persistence of soil organic mat-
> ter as an ecosystem property, Nature, 478, 49–56, 2011.
> Schreiner, K. M., Bianchi, T. S., and Rosenheim, B. E.: Evidence
> for permafrost thaw and transport from an Alaskan North Slope
> watershed, Geophys. Res. Lett., 41, 3117–3126, 2014.
> Spencer, R. G., Stubbins, A., Hernes, P. J., Baker, A., Mopper,
> K., Aufdenkampe, A. K., Dyda, R. Y., Mwamba, V. L., Man-
> gangu, A. M., Wabakanghanzi, J. N., and Six, J.: Photochemi-
> cal degradation of dissolved organic matter and dissolved lignin
> phenols from the Congo River, J. Geophys. Res., 114, G03010,
> https://doi.org/10.1029/2009JG000968, 2009.
> Tang, Y., Perry, J. K., Jenden, P. D., and Schoell, M.: Mathemat-
> ical modeling of stable carbon isotope ratios in natural gases,
> Geochim. Cosmochim. Ac., 64, 2637–2687, 2000.
> www.biogeosciences.net/14/5099/2017/ Biogeosciences, 14, 5099–5114, 2017
>
> ---
>
> 5114 J. D. Hemingway et al.: Organic carbon activation energy and isotope composition
> Tegelaar, E. W., de Leeuw, J. W., Derenne, S., and Largeau, C.:
> A reappraisal of kerogen formation, Geochim. Cosmochim. Ac.,
> 53, 3103–3106, 1989.
> Westrich, J. T. and Berner, R. A.: The role of sedimentary organic
> matter in bacterial sulfate reduction: The G model tested, Lim-
> nol. Oceanogr., 29, 236–249, 1984.
> White, J. E., Catallo, W. J., and Legendre, B. L.: Biomass pyrolysis
> kinetics: A comparative critical review with relevant agricultural
> residue case studies, J. Anal. Appl. Pyrol., 91, 1–33, 2011.
> Whiteside, J. H., Olsen, P. E., Eglinton, T. I., Cornet, B., McDonald,
> N. G., and Huber, P.: Pangean great lake paleoecology on the
> cusp of the end-Triassic extinction, Palaeogeogr. Palaeocl., 301,
> 1–17, 2011.
> Williams, E. K., Rosenheim, B. E., McNichol, A. P., and Masiello,
> C. A.: Charring and non-additive chemical reactions during
> ramped pyrolysis: Applications to the characterization of sedi-
> mentary and soil organic material, Org. Geochem., 77, 106–114,
> 2014.
> Biogeosciences, 14, 5099–5114, 2017 www.biogeosciences.net/14/5099/2017/

