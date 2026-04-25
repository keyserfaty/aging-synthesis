# Rapamycin

**Verdict:** Probable
**Last reviewed:** 2026-04-24
**Triangulated against anchor:** Rapamycin (this page is the canonical anchor for "Probable")

## TL;DR

Rapamycin is the most consistently lifespan-extending pharmacological intervention ever tested in mice. It is **Probable**, not Strong, because human evidence is limited to surrogate-endpoint and immunology trials with no mortality data.

## What it is

A macrolide originally developed as an antifungal, now used clinically as an immunosuppressant (post-transplant) and oncology agent (mTOR inhibitor class). In aging research, doses are far below clinical immunosuppression doses — typical mouse equivalents translated to humans land in the range of 5-10 mg weekly or 1-3 mg daily. Off-label longevity use is overwhelmingly oral (sirolimus tablets); intermittent dosing (weekly) is preferred over daily by most clinicians targeting longevity to minimize immune side effects.

## Proposed mechanism

Inhibits mTOR (mechanistic target of rapamycin) — specifically mTORC1 at typical doses, with mTORC2 inhibition emerging at high or chronic doses. mTOR integrates nutrient signaling and regulates the cellular trade-off between growth/anabolism and autophagy/maintenance. Inhibition shifts cells toward maintenance, mimicking some downstream effects of caloric restriction.

**Confidence: Established.** mTOR's role in lifespan regulation is one of the best-characterized aging mechanisms across taxa.

## Evidence ladder

### Invertebrate (T5)

Lifespan extension by mTOR inhibition replicated in S. cerevisiae, C. elegans, and D. melanogaster. Effect sizes vary 10-50% depending on organism and dose. Mechanism (TOR inhibition) is conserved across all tested species.

### Mouse / rat (T3)

This is the strongest evidence base.

- **ITP status: positive across multiple cohorts.** Harrison 2009 (Nature) was the first ITP positive — male UM-HET3 +9%, female +14% median lifespan starting at 9 months of age (later-life intervention). Miller 2011 confirmed at lower dose. Subsequent cohorts tested earlier dosing, encapsulation, and combinations.
- **Effect size range:** ~9-26% median lifespan extension; up to ~28% in recent comprehensive reviews; max lifespan extension ~9-16%.
- **Independent labs:** Multiple — ITP itself spans 3 sites (Jackson, UT Health San Antonio, U Michigan) plus replications by other groups (Wilkinson 2012, Strong 2016 with metformin combination, Strong 2022 with acarbose combination).
- **Sex dependence:** Females respond more strongly at lower doses; this is a well-documented and replicated pattern.
- **Strain dependence:** Validated in UM-HET3 (genetically heterogeneous) and several inbred strains; effect appears robust across strains.
- **Dose dependence:** Higher doses produce larger effects up to a ceiling; immunosuppression and metabolic side effects scale with dose.

### NHP (T4)

Limited data. Marmoset studies (Ross et al.) suggest tolerability and possible biomarker effects; no NHP lifespan data of comparable rigor to mouse data. Dog Aging Project's TRIAD trial (rapamycin in companion dogs) is ongoing — when reported, that data would meaningfully inform translation.

### Human (T2)

- **PEARL trial** (Participatory Evaluation of Aging with Rapamycin for Longevity) — open-label, ~~600 participants, biomarker outcomes (lean mass, frailty, cognition). Results suggest small biomarker improvements at moderate doses; not a hard-endpoint or placebo-controlled trial. Pre-registered. AgelessRx-affiliated (apply 1-tier COI discount per methodology section 5).
- **Mannick et al. RTB101/everolimus** — Novartis-funded trials in older adults showed reduced respiratory infection rates and improved vaccine response. T2 evidence on a clinically meaningful surrogate.
- **Off-label longevity use** — clinical case series exist (Kraig, Blagosklonny) but these are T0-T2 with selection bias.
- **No mortality RCT exists.** No human study has measured death as an endpoint.

## Confounds

- **Control diet adequacy:** ITP control diets are well-validated (NIH-31). Not a concern.
- **Baseline mortality of strain:** UM-HET3 is genetically heterogeneous and not pathologically short-lived; effects are not artifacts of rescuing a fragile strain.
- **Publication bias signal:** Low for the mouse data — ITP design pre-registers interventions and reports null results (e.g., NR). Higher for human off-label literature.
- **Encapsulation:** Early ITP studies used microencapsulated rapamycin in chow to bypass first-pass metabolism. Real-world human dosing differs; pharmacokinetics translation is non-trivial.

## Conflict of interest scan

- ITP: NIA-funded; no discount.
- PEARL: AgelessRx involvement → 1-tier discount; partially offset by pre-registration.
- Mannick et al.: Novartis-funded → 1-tier discount, partially offset by pre-registration and FDA-grade design.
- Net effect: T3 mouse evidence undiscounted; T2 human evidence effectively T2-T3.

## Human translation

Rapamycin extends mouse lifespan with high reproducibility. Whether it extends *human* lifespan is unknown — no trial has measured that endpoint, and no trial of sufficient size and duration is planned. What human RCTs *have* shown: improved immune function in older adults (vaccine response), tolerability at intermittent dosing, and modest biomarker movement at moderate doses. Side effects in long-term human use include mouth sores, mild hyperlipidemia, glucose dysregulation in some users, and (at higher doses) immune suppression.

The honest framing: rapamycin is the best-evidenced candidate for a human longevity drug, but "best-evidenced candidate" is not the same as "evidence it works in humans."

## Calibrated verdict

**Probable.** This page is the canonical anchor for the Probable band. The bar to claim Probable is "T3 mouse evidence with at least suggestive human data." Rapamycin clears that bar definitively on the mouse side and marginally on the human side.

Compared to **caloric restriction (in mice, Strong)**, rapamycin's mouse evidence is comparably replicated but rapamycin lacks decades of strain/diet/protocol variation; CR therefore stays one band above as the ceiling for mouse interventions.

Compared to **NMN (Suggestive)**, rapamycin has T3 ITP-replicated mouse evidence and at least T2 human surrogate evidence; NMN has neither. The gap between these two anchors is the meaningful distinction between Probable and Suggestive.

## Confidence interval on verdict

- **Could move to Strong** if a large pre-registered human RCT (e.g., a successor to PEARL with mortality or hard composite endpoints) reports positive. None is currently funded at sufficient scale.
- **Could move to Suggestive** if dog Aging Project (TRIAD) reports null and a major mouse study fails to replicate at standard doses. Both unlikely given the existing replication record.
- **Most likely 2-year trajectory:** stays at Probable; possible upgrade if TRIAD reports strongly positive.

## Open questions

- Q: What is the optimal human dosing protocol (daily low-dose vs intermittent)? Pharmacokinetic models exist but human comparative trials do not.
- Q: Does intermittent dosing preserve longevity benefits while mitigating side effects? Mouse data suggests yes; human data is anecdotal.
- Q: TRIAD (dog) results — when will they read out, and what will they show?
- Q: Does long-term rapamycin use in healthy humans cause clinically meaningful immune suppression, or is the immune effect purely "rejuvenating" (improved vaccine response, improved infection clearance)?

These will be added to `QUESTIONS.md` for the resolver agent.

## Sources

- [Harrison et al. 2009, Nature — Rapamycin fed late in life extends lifespan in genetically heterogeneous mice](https://www.nature.com/articles/nature08221)
- [Miller et al. 2011, J Gerontol — Rapamycin, but not resveratrol or simvastatin, extends life span of genetically heterogeneous mice](https://academic.oup.com/biomedgerontology/article/66A/2/191/598510)
- [Strong et al. 2016, Aging Cell — Longer lifespan in male mice treated with rapamycin alone or in combination with metformin](https://onlinelibrary.wiley.com/doi/10.1111/acel.12496)
- [Strong et al. 2022 — ITP rapamycin + acarbose combination](https://www.fightaging.org/archives/2022/10/interventions-testing-program-results-for-rapamycin-and-arcabose-in-combination/)
- [Mannick et al. 2014, 2018 — RTB101/everolimus immune function in older adults](https://pubmed.ncbi.nlm.nih.gov/30253139/)
- [PEARL trial — AgelessRx clinical evidence summary 2025 (Aging journal)](https://www.aging-us.com/article/206300/text)
- [ITP comprehensive review, J Gerontol Biol Sci, July 2025](https://news.uthscsa.edu/first-national-review-identifies-anti-aging-compounds/)
- [NIA ITP supported interventions](https://www.nia.nih.gov/research/dab/interventions-testing-program-itp/supported-interventions)

---

*Produced under methodology locked 2026-04-24. Anchor for the Probable band.*
