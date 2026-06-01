"""
RAG Knowledge Base — Water Quality Standards
Sources: BIS IS 10500:2012, CPCB 2024, EU Directive 2020/2184, US EPA SDWA
"""

# ---------------------------------------------------------------------------
# Each "chunk" is a discrete retrievable unit from the knowledge base.
# In a production RAG system these would be vector-embedded.
# Here we use keyword-based retrieval (fast, zero infra, works offline).
# ---------------------------------------------------------------------------

KNOWLEDGE_CHUNKS = [
    {
        "id": "bis_physical",
        "source": "BIS IS 10500:2012",
        "category": "Physical Parameters — Drinking Water",
        "keywords": ["color", "colour", "turbidity", "ph", "tds", "total dissolved solids",
                     "hardness", "odor", "taste", "physical"],
        "content": """
BIS IS 10500:2012 — Physical Parameters for Drinking Water (India)

| Parameter        | Desirable Limit   | Permissible Limit |
|------------------|-------------------|-------------------|
| Color            | 5 Hazen units     | 15 Hazen units    |
| Turbidity        | 1 NTU             | 5 NTU             |
| pH               | 6.5 – 8.5         | No relaxation     |
| TDS              | 500 mg/L          | 2000 mg/L         |
| Total Hardness   | 200 mg/L (CaCO3)  | 600 mg/L (CaCO3)  |
| Odor             | Unobjectionable   | Unobjectionable   |
| Taste            | Agreeable         | Agreeable         |

Note: CPCB allows turbidity up to 10 NTU for piped supply in remote areas.
Jal Jeevan Mission (2019–2024) targets 5 NTU turbidity for Har Ghar Jal connections.
"""
    },
    {
        "id": "bis_heavy_metals",
        "source": "BIS IS 10500:2012",
        "category": "Heavy Metals — Drinking Water",
        "keywords": ["arsenic", "lead", "mercury", "cadmium", "chromium", "zinc", "copper",
                     "manganese", "iron", "heavy metal", "selenium", "nickel", "barium",
                     "boron", "aluminum", "aluminium"],
        "content": """
BIS IS 10500:2012 — Heavy Metals & Inorganic Parameters (India)

| Parameter       | Desirable Limit   | Permissible Limit |
|-----------------|-------------------|-------------------|
| Arsenic (As)    | —                 | 0.01 mg/L         |
| Lead (Pb)       | —                 | 0.01 mg/L         |
| Mercury (Hg)    | —                 | 0.001 mg/L        |
| Cadmium (Cd)    | —                 | 0.003 mg/L        |
| Chromium (Cr)   | —                 | 0.05 mg/L (total) |
| Iron (Fe)       | 0.3 mg/L          | 1.0 mg/L          |
| Manganese (Mn)  | 0.1 mg/L          | 0.3 mg/L          |
| Copper (Cu)     | 0.05 mg/L         | 1.5 mg/L          |
| Zinc (Zn)       | 5 mg/L            | 15 mg/L           |
| Selenium (Se)   | —                 | 0.01 mg/L         |
| Nickel (Ni)     | —                 | 0.02 mg/L         |
| Barium (Ba)     | —                 | 0.7 mg/L          |
| Boron (B)       | —                 | 0.5 mg/L          |
| Aluminum (Al)   | 0.03 mg/L         | 0.2 mg/L          |

India-specific hotspots:
- Arsenic: West Bengal (Murshidabad, North 24 Parganas), Bihar, Jharkhand, Assam, UP (Ballia, Ghazipur) — over 1.5 crore people at risk
- Iron: West Bengal, Assam, Bihar, Odisha, Chhattisgarh
"""
    },
    {
        "id": "bis_anions",
        "source": "BIS IS 10500:2012",
        "category": "Anions & Other Chemicals",
        "keywords": ["fluoride", "fluorosis", "nitrate", "nitrite", "chloride", "sulfate",
                     "sulphate", "chlorine", "residual", "cyanide", "ammonia", "anion"],
        "content": """
BIS IS 10500:2012 — Anions & Chemical Parameters (India)

| Parameter       | Desirable Limit   | Permissible Limit |
|-----------------|-------------------|-------------------|
| Fluoride (F)    | 1.0 mg/L          | 1.5 mg/L          |
| Nitrate (NO3)   | 45 mg/L           | 45 mg/L (strict)  |
| Chloride (Cl)   | 250 mg/L          | 1000 mg/L         |
| Sulfate (SO4)   | 200 mg/L          | 400 mg/L          |
| Cyanide (CN)    | —                 | 0.05 mg/L         |
| Ammonia (NH3)   | 0.5 mg/L          | —                 |
| Residual Cl2    | 0.2 mg/L (min)    | —                 |

India-specific fluoride endemic zones:
- HIGH RISK: Rajasthan, Gujarat, Andhra Pradesh, Telangana, Haryana
- Causes: Dental fluorosis (>1.5 mg/L), Skeletal fluorosis (>3 mg/L)
- Defluoridation: Nalgonda technique used in rural India

Nitrate hotspots (agricultural runoff):
- Punjab, Haryana, Rajasthan, Madhya Pradesh
- Infant methemoglobinemia ("blue baby syndrome") risk above 45 mg/L
"""
    },
    {
        "id": "bis_microbiology",
        "source": "BIS IS 10500:2012",
        "category": "Microbiological Parameters",
        "keywords": ["e coli", "ecoli", "coliform", "fecal", "faecal", "bacteria",
                     "microbiological", "microbial", "pathogen", "total coliform",
                     "enterococci", "virus", "protozoa"],
        "content": """
BIS IS 10500:2012 — Microbiological Parameters (India)

| Parameter              | Limit                        |
|------------------------|------------------------------|
| E. coli                | ZERO / 100 mL (NO relaxation)|
| Fecal Coliforms        | ZERO / 100 mL                |
| Total Coliforms        | ≤1 CFU/100 mL (treated supply)|
| Coliform organisms     | Absent in any 100 mL sample  |

Key points:
- Zero tolerance for E. coli is absolute — no relaxation permitted under any circumstances
- Treated piped water must have residual chlorine ≥ 0.2 mg/L to ensure microbial safety
- Jal Jeevan Mission mandates monthly microbial testing at household taps
- Community water testing via Field Test Kits (FTKs) distributed by Ministry of Jal Shakti
- In India, diarrheal diseases cause ~300,000 deaths annually, mostly waterborne
"""
    },
    {
        "id": "bis_radioactivity",
        "source": "BIS IS 10500:2012",
        "category": "Radioactivity Parameters",
        "keywords": ["radioactivity", "radioactive", "alpha", "beta", "radiation",
                     "radon", "tritium", "bq", "becquerel"],
        "content": """
BIS IS 10500:2012 — Radioactivity Parameters (India)

| Parameter            | Limit       |
|----------------------|-------------|
| Gross Alpha Activity | 0.1 Bq/L   |
| Gross Beta Activity  | 1 Bq/L     |

These align with WHO 2022 guidelines. Testing mandatory in areas near nuclear plants,
uranium mines, and naturally occurring radioactive material (NORM) regions.
Relevant Indian regions: Jadugoda (Jharkhand uranium mines), Kerala (thorium-rich coastal sands).
"""
    },
    {
        "id": "cpcb_river",
        "source": "CPCB — Central Pollution Control Board",
        "category": "River Water Classification (Designated Best Use)",
        "keywords": ["river", "surface water", "bod", "do", "dissolved oxygen",
                     "class a", "class b", "class c", "class d", "class e",
                     "cpcb", "designated best use", "bathing", "irrigation",
                     "ganga", "yamuna", "kaveri"],
        "content": """
CPCB River Water Quality Classification — Designated Best Use Criteria

| Class | Designated Best Use                    | BOD (mg/L) | DO (mg/L) | Total Coliforms (MPN/100 mL) |
|-------|----------------------------------------|------------|-----------|-------------------------------|
| A     | Drinking + conventional treatment      | ≤ 2        | ≥ 6       | ≤ 50                          |
| B     | Outdoor bathing (organized)            | ≤ 3        | ≥ 5       | ≤ 500                         |
| C     | Drinking + extensive treatment         | ≤ 3        | ≥ 4       | ≤ 5000                        |
| D     | Propagation of wildlife & fisheries    | ≤ 3        | ≥ 4       | Not specified                 |
| E     | Irrigation, industrial cooling         | ≤ 6        | ≥ 4*      | Not specified                 |

*DO requirement for Class E applies only for fisheries, not irrigation.

National River Classification Status (examples):
- Ganga: Class B target (most stretches currently Class C–D)
- Yamuna (Delhi stretch): Often Class E or worse (BOD > 20 mg/L)
- Periyar (Kerala): Class C
- Namami Gange Programme: Target Class B by 2026

Real-time CPCB river monitoring: cpcb.nic.in
"""
    },
    {
        "id": "cpcb_effluent",
        "source": "CPCB — Central Pollution Control Board",
        "category": "Industrial Effluent Standards",
        "keywords": ["effluent", "discharge", "industrial", "wastewater", "sewage",
                     "bod", "cod", "tss", "suspended solids", "oil", "grease",
                     "temperature", "factory", "trade effluent", "stp", "etp"],
        "content": """
CPCB General Standards for Discharge of Environmental Pollutants (Schedule VI, EPA 1986)

Inland Surface Water Standards:
| Parameter             | Limit                    |
|-----------------------|--------------------------|
| pH                    | 6.5 – 8.5                |
| BOD5 (20°C)           | ≤ 30 mg/L                |
| COD                   | ≤ 250 mg/L               |
| Total Suspended Solids| ≤ 100 mg/L               |
| Oil & Grease          | ≤ 10 mg/L                |
| Temperature           | ≤ 40°C (≤3°C rise in river) |
| Ammoniacal Nitrogen   | ≤ 50 mg/L                |
| Total Nitrogen        | ≤ 100 mg/L               |
| Phenolic compounds    | ≤ 1 mg/L                 |
| Cyanide (as CN)       | ≤ 0.2 mg/L               |
| Arsenic               | ≤ 0.2 mg/L               |
| Chromium (hexavalent) | ≤ 0.1 mg/L               |
| Lead                  | ≤ 0.1 mg/L               |
| Mercury               | ≤ 0.01 mg/L              |

On land for irrigation: BOD ≤ 100 mg/L, COD ≤ 400 mg/L
Sewage Treatment Plants (STPs): BOD ≤ 10 mg/L (Class I cities)
Zero Liquid Discharge (ZLD) mandated for: textile dyeing, tanneries, sugar mills, distilleries
"""
    },
    {
        "id": "cpcb_groundwater",
        "source": "CPCB / CGWB",
        "category": "Groundwater Quality — India",
        "keywords": ["groundwater", "ground water", "borewell", "well", "aquifer",
                     "tube well", "cgwb", "underground water"],
        "content": """
CPCB / CGWB Groundwater Quality Parameters (India)

Groundwater tested against BIS IS 10500:2012 limits. Critical contaminants:

| Contaminant | BIS Limit   | Affected States                              |
|-------------|-------------|----------------------------------------------|
| Arsenic     | 0.01 mg/L   | West Bengal, Bihar, Jharkhand, Assam, UP     |
| Fluoride    | 1.5 mg/L    | Rajasthan, Gujarat, AP, Telangana, Haryana   |
| Nitrate     | 45 mg/L     | Punjab, Haryana, Rajasthan, MP               |
| Iron        | 1.0 mg/L    | West Bengal, Assam, Bihar, Odisha            |
| Salinity/TDS| 2000 mg/L   | Coastal Gujarat, Tamil Nadu, Rajasthan       |
| Uranium     | 0.03 mg/L*  | Punjab (Malwa), Rajasthan                   |

*WHO guideline; BIS IS 10500 does not specify uranium limit.

National Water Quality Monitoring Programme (NWMP): CPCB monitors 2,500+ stations.
Central Ground Water Board (CGWB): Monitors 15,000+ wells across India.
ATAL BHUJAL YOJANA: Community groundwater management in 7 states.

Testing recommendation for India:
- Bore/tube wells: Test for arsenic, fluoride, nitrate, iron, TDS, pH, E. coli
- Minimum annually; post-monsoon critical
- NABL-accredited labs mandatory for legal compliance
"""
    },
    {
        "id": "epa_primary_mcl",
        "source": "US EPA — Safe Drinking Water Act (SDWA)",
        "category": "Primary MCLs — Inorganic Chemicals",
        "keywords": ["epa", "us epa", "mcl", "maximum contaminant level", "sdwa",
                     "safe drinking water", "american", "united states", "action level",
                     "primary standard"],
        "content": """
US EPA — Primary Maximum Contaminant Levels (MCLs) — Inorganic Chemicals

| Contaminant         | MCL / Action Level    | Notes                              |
|---------------------|-----------------------|------------------------------------|
| Arsenic             | 0.010 mg/L            | Effective 2006 (Rule from 2001)    |
| Fluoride            | 4.0 mg/L (primary)    | Secondary: 2.0 mg/L (aesthetic)    |
| Nitrate             | 10 mg/L as N          | = ~44 mg/L as NO3                  |
| Nitrite             | 1 mg/L as N           |                                    |
| Lead                | Action Level 0.015 mg/L| 90th percentile tap samples       |
| Copper              | Action Level 1.3 mg/L |                                    |
| Mercury (inorganic) | 0.002 mg/L            |                                    |
| Cadmium             | 0.005 mg/L            |                                    |
| Chromium (total)    | 0.1 mg/L              | Cr6+ no separate federal MCL       |
| Cyanide (free CN)   | 0.2 mg/L              |                                    |
| Selenium            | 0.05 mg/L             |                                    |
| Antimony            | 0.006 mg/L            |                                    |
| Barium              | 2 mg/L                |                                    |
| Beryllium           | 0.004 mg/L            |                                    |
| Thallium            | 0.002 mg/L            |                                    |
| Uranium             | 0.030 mg/L (30 µg/L)  |                                    |
| Total Coliforms     | < 5% positive/month   | Revised Total Coliform Rule 2013   |
| E. coli             | Zero                  | Revised TCR — zero tolerance       |
| Turbidity           | ≤ 1 NTU (filter exit) | 95% of readings ≤ 0.3 NTU         |
| Radium 226+228      | 5 pCi/L               |                                    |

Disinfection Byproducts (DBPs):
- Total Trihalomethanes (TTHMs): 0.080 mg/L
- Haloacetic Acids (HAA5): 0.060 mg/L
- Bromate: 0.010 mg/L
- Chlorite: 1.0 mg/L
- Chlorine (MRDL): ≤ 4.0 mg/L

Surface Water Treatment Rule: 99.9% removal of Giardia, 99.99% of viruses.
"""
    },
    {
        "id": "eu_directive",
        "source": "EU Drinking Water Directive 2020/2184/EU",
        "category": "EU Parametric Values — Drinking Water",
        "keywords": ["eu", "european union", "directive", "europe", "european",
                     "2020/2184", "parametric value", "pfas", "bisphenol",
                     "microcystin", "eu standard"],
        "content": """
EU Drinking Water Directive 2020/2184/EU — Parametric Values
(Recast of 1998 Directive; member states complied by Jan 2023)

Chemical Parameters:
| Parameter         | Parametric Value | Notes vs 1998 Directive           |
|-------------------|------------------|-------------------------------------|
| Arsenic           | 0.010 mg/L       | Same                               |
| Fluoride          | 1.5 mg/L         | Same                               |
| Nitrate           | 50 mg/L as NO3   | Same (≈ 11 mg/L as N)             |
| Nitrite           | 0.5 mg/L (exit); 0.1 mg/L (tap) | Tightened at tap    |
| Lead              | 0.010 mg/L       | Tightened from 0.025 mg/L; 5 µg/L by 2036 |
| Mercury           | 0.001 mg/L       | Same                               |
| Cadmium           | 0.005 mg/L       | Same                               |
| Chromium          | 0.025 mg/L       | Tightened from 0.05 mg/L           |
| Copper            | 2.0 mg/L         | Same                               |
| Cyanide           | 0.05 mg/L        | Same                               |
| Selenium          | 0.020 mg/L       | Tightened from 0.010 mg/L          |
| Nickel            | 0.020 mg/L       | Same                               |
| Antimony          | 0.005 mg/L       | Same                               |
| Barium            | 0.5 mg/L         | NEW in 2020                        |
| Boron             | 1.0 mg/L         | Relaxed from 0.001 mg/L            |
| Bromate           | 0.010 mg/L       | Same                               |
| Chlorite          | 0.7 mg/L         | NEW in 2020                        |
| Chlorate          | 0.7 mg/L         | NEW in 2020                        |
| PFAS (total)      | 0.0005 mg/L      | NEW in 2020 — emerging contaminant |
| Sum of 20 PFAS    | 0.0001 mg/L      | NEW in 2020                        |
| Bisphenol A       | 0.0025 µg/L      | NEW in 2020                        |
| Microcystin-LR    | 0.001 mg/L       | NEW in 2020 — cyanobacterial toxin |

Physical/Microbiological:
| Parameter          | Value      |
|--------------------|------------|
| pH                 | 6.5 – 9.5  |
| Conductivity       | ≤ 2500 µS/cm at 20°C |
| Turbidity          | 1.0 NTU    |
| E. coli            | 0 CFU/100 mL |
| Enterococci        | 0 CFU/100 mL |
| Total Coliforms    | 0 CFU/100 mL |
| Radon              | ≤ 100 Bq/L (indicative) |
| Tritium            | ≤ 100 Bq/L |
"""
    },
    {
        "id": "comparison_table",
        "source": "Multi-standard comparison",
        "category": "Cross-Standard Comparison — Key Parameters",
        "keywords": ["compare", "comparison", "versus", "vs", "difference",
                     "all standards", "which is stricter", "stricter", "lenient",
                     "who", "world health organization"],
        "content": """
Cross-Standard Comparison — Key Drinking Water Parameters

| Parameter       | India BIS IS 10500 | US EPA SDWA          | EU 2020/2184       | WHO 2022  |
|-----------------|--------------------|----------------------|--------------------|-----------|
| Arsenic         | 0.01 mg/L          | 0.010 mg/L           | 0.010 mg/L         | 0.010 mg/L|
| Fluoride        | 1.5 mg/L (perm)    | 4.0 mg/L (primary)   | 1.5 mg/L           | 1.5 mg/L  |
| Nitrate         | 45 mg/L (as NO3)   | 10 mg/L (as N)=44 mg/L as NO3 | 50 mg/L (as NO3) | 50 mg/L |
| Lead            | 0.01 mg/L          | 0.015 mg/L (AL)      | 0.010 mg/L         | 0.010 mg/L|
| Mercury         | 0.001 mg/L         | 0.002 mg/L           | 0.001 mg/L         | 0.006 mg/L|
| Cadmium         | 0.003 mg/L         | 0.005 mg/L           | 0.005 mg/L         | 0.003 mg/L|
| Chromium        | 0.05 mg/L          | 0.1 mg/L             | 0.025 mg/L         | 0.05 mg/L |
| Selenium        | 0.01 mg/L          | 0.05 mg/L            | 0.020 mg/L         | 0.04 mg/L |
| Copper          | 1.5 mg/L (perm)    | 1.3 mg/L (AL)        | 2.0 mg/L           | 2.0 mg/L  |
| Cyanide         | 0.05 mg/L          | 0.2 mg/L             | 0.05 mg/L          | 0.05 mg/L |
| TDS             | 500/2000 mg/L      | 500 mg/L (secondary) | 2500 µS/cm (approx)| No limit  |
| pH              | 6.5 – 8.5          | 6.5 – 8.5 (secondary)| 6.5 – 9.5          | 6.5 – 8.5 |
| Turbidity       | 1 NTU / 5 NTU      | ≤ 1 NTU (filter)     | 1.0 NTU            | 1 NTU     |
| E. coli         | Zero / 100 mL      | Zero                 | 0 CFU/100 mL       | Zero      |
| Barium          | 0.7 mg/L           | 2.0 mg/L             | 0.5 mg/L           | 1.3 mg/L  |
| Boron           | 0.5 mg/L           | No federal MCL       | 1.0 mg/L           | 2.4 mg/L  |
| Nickel          | 0.02 mg/L          | No federal MCL       | 0.020 mg/L         | 0.07 mg/L |

Strictness ranking (tightest limits = safest):
- Lead: India = EU > WHO > EPA
- Fluoride: India = EU = WHO >> EPA (EPA far more lenient)
- Chromium: EU > India = WHO > EPA
- PFAS (emerging): EU 2020 has limit; India and EPA still developing rules
"""
    },
    {
        "id": "india_legislation",
        "source": "Indian Legislation & Programmes",
        "category": "Indian Water Law & Government Programmes",
        "keywords": ["law", "legislation", "act", "rule", "policy", "programme",
                     "program", "jal jeevan", "namami gange", "ministry",
                     "jal shakti", "pollution control board", "pcb", "spcb",
                     "environment protection act", "water act"],
        "content": """
Key Indian Water Quality Legislation & Programmes

Legislation:
- Water (Prevention and Control of Pollution) Act, 1974 — Established CPCB and SPCBs
- Environment Protection Act, 1986 — CPCB authority to set effluent standards
- BIS IS 10500:2012 — National drinking water specification (mandatory)
- BIS IS 10500 Amendment 2015 — Revised arsenic and lead limits
- Groundwater (Sustainable Management) Act framework — State-level
- National Green Tribunal (NGT) Act, 2010 — Environmental justice

Key Government Bodies:
- CPCB (Central Pollution Control Board) — National water quality monitoring
- State Pollution Control Boards (SPCBs) — State-level enforcement
- CGWB (Central Ground Water Board) — Groundwater regulation
- Ministry of Jal Shakti — Nodal ministry for water
- BIS (Bureau of Indian Standards) — Standards body

Major Programmes:
- Jal Jeevan Mission (2019–2024): Functional household tap connections for 19 crore rural households; mandatory water testing
- Namami Gange (2014–2027): ₹20,000 crore for Ganga cleaning; STP construction
- AMRUT 2.0 (2021–2026): Urban water supply and sewerage for 500 cities
- Atal Bhujal Yojana (2019–2024): Participatory groundwater management in 7 states
- Swachh Bharat Mission: Sanitation and groundwater protection

Testing Labs:
- NABL-accredited labs: nabl.gov.in/nabl/lab-search
- State PHE (Public Health Engineering) Department labs
- IIT labs (water quality testing)
- WaterAid India field testing kits
"""
    },
]

# ---------------------------------------------------------------------------
# Keyword-based retrieval function
# ---------------------------------------------------------------------------

def retrieve_chunks(query: str, top_k: int = 4) -> list[dict]:
    """
    Retrieve the most relevant knowledge chunks for a given query.
    Uses keyword scoring — suitable for this domain-specific use case.
    """
    query_lower = query.lower()
    query_words = set(query_lower.split())

    scored = []
    for chunk in KNOWLEDGE_CHUNKS:
        score = 0
        # Match against keywords list
        for kw in chunk["keywords"]:
            if kw in query_lower:
                score += 3  # exact phrase match
            elif any(word in kw for word in query_words):
                score += 1  # partial word match

        # Boost if category or source mentioned in query
        if any(w in query_lower for w in chunk["source"].lower().split()):
            score += 2
        if any(w in query_lower for w in chunk["category"].lower().split()):
            score += 1

        # Always include comparison chunk if comparing
        if "compar" in query_lower and chunk["id"] == "comparison_table":
            score += 5

        if score > 0:
            scored.append((score, chunk))

    # Sort by score descending, return top_k
    scored.sort(key=lambda x: x[0], reverse=True)

    # Fallback: return comparison + BIS physical if nothing matched
    if not scored:
        return [KNOWLEDGE_CHUNKS[0], KNOWLEDGE_CHUNKS[10]]

    return [chunk for _, chunk in scored[:top_k]]


def build_context(query: str) -> tuple[str, list[dict]]:
    """Build the RAG context string and return retrieved chunks for citation."""
    chunks = retrieve_chunks(query)
    context_parts = []
    for chunk in chunks:
        context_parts.append(
            f"=== SOURCE: {chunk['source']} | {chunk['category']} ===\n{chunk['content']}"
        )
    context = "\n\n".join(context_parts)
    return context, chunks
