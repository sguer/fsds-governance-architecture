# FSDS Governance Architecture Dashboard 

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://fsds-governance-architecture-8uwblvgftqwmjjchrg66yu.streamlit.app/)

[![Python 3.14](https://img.shields.io/badge/Python-3.14.3-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)

[![License](https://img.shields.io/badge/CC%20BY--NC--SA%204.0-FF6B35?style=for-the-badge&logo=creativecommons&logoColor=white)](LICENSE)

## License & Attribution

**CC BY-NC-SA 4.0** — © 2026 Andy Sabrina Guerrier, Brain-CE Fellow, for Brain Climate & Equity Collaborative (Brain-CE).

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).

**Non-commercial use only.** Adaptations must be shared under identical terms.

**Purpose:** Designed as a non-commercial tool to map the distribution of implementation strategies across federal organizations, this resource supports collaborative engagement with the **[Draft 2026–2029 Federal Sustainable Development Strategy (FSDS)](https://www.canada.ca/en/environment-climate-change/corporate/transparency/consultations/share-your-throughts-draft-2026-2029-federal-sustainable-development-strategy.html)** consultation process (open until May 12, 2026).

**_As an independent analytical visualization, this tool interpretive rather than authoritative and does not represent an official Government of Canada product._**



## FSDS Consultation Focus

The 2026–2029 FSDS consultation process focuses on engagement with the following rights-holders, communities, and sector partners:

- Individuals and the Canadian public

- Indigenous Peoples

- Non-governmental organizations

- Industry and professional associations

- Business and labour organizations

- Private sector

- Academic experts and think tanks

- Governments (provincial, territorial, and municipal)


By mapping the distribution of federal implementation strategies, this logic-mapped visualization serves as an independent analytical resource for interpraetive support. **The collaborative tool is not administered by Environment and Climate Change Canada (ECCC).**
  

## Overview

This project provides a static PNG graphic and Streamlit web app that visualizes how federal organizations implement sustainable development strategies through FSDS goals to achieve Quality of Life Framework outcomes.

## Key Features

- **Sankey Diagram Visualization**: Flow-based diagram showing FSDS implementation flows across federal organizations

- **Interactive Dashboard**: Hover-enabled exploration of connections  

- **Multiple Export Formats**: PNG (static), HTML (interactive), and web dashboard  

- **Fully Open-Source**: CC BY-NC-SA 4.0 licensed for non-commercial collaborative use

---


## Quick Start

### Option 1: Run the Interactive Dashboard

```bash
# Install dependencies
pip install streamlit plotly kaleido pillow

# Run the app
streamlit run app.py
```

Then open your browser to `http://localhost:8501`

### Option 2: Generate Static PNG

```bash
# Install dependencies
pip install plotly kaleido pillow

# Run the generator
python generate_chart.py
```

Output: `FSDS_Governance_Architecture.png`

## Installation

### Requirements

- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository** (or download files)
```bash
git clone https://github.com/sguer/fsds-governance-architecture.git
cd fsds-governance-architecture
```

2. **Create virtual environment** (recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## Usage

### Running the Streamlit App

```bash
streamlit run app.py
```

Features:
- **Light/Dark Theme Toggle**: Choose your preferred colour scheme
- **Interactive Exploration**: Hover over flows to see exact connections
- **Responsive Layout**: Works on desktop, tablet, and mobile
- **Full Documentation**: Inline explanations and data source

### Generating Static Images

```bash
# Generate PNG (requires kaleido)
python generate_chart.py

# Or generate manually
python -c "from generate_chart import create_fsds_governance_chart, save_as_png; fig = create_fsds_governance_chart(); save_as_png(fig, 'output.png')"
```

### Python Integration

To incorporate these visualizations into your own Python scripts or Jupyter notebooks:

```python
from generate_chart import create_fsds_governance_chart, save_as_png, save_as_html

# Create the figure
fig = create_fsds_governance_chart()

# Save as PNG
save_as_png(fig, 'chart.png')

# Save as interactive HTML
save_as_html(fig, 'chart.html')

# Display with Plotly
fig.show()
```

---


## Sample Data Hierarchy 
*Simplified overview from the comprehensive JSON data file. Full dataset available in repository: [fsds-governance-architecture/fsds_data.json](https://github.com/sguer/fsds-governance-architecture/blob/main/fsds_data.json)

### Federal Organizations (Annex 2), pp.56-62

- **ISC** - Indigenous Services Canada
- **ECCC** - Environment and Climate Change Canada
- **HICC** - Housing and Infrastructure Coordinating Committee
- **ESDC** - Employment and Social Development Canada
- **JUS** - Justice Canada
- **WAGE** - Women and Gender Equality
- **PHAC** - Public Health Agency of Canada

### FSDS Goals (Chapters 1-3)

**Chapter 1: Governance**
- 1.1: Confidence in Government
- 1.4: Reduce Systemic Racism
- 1.6: Indigenous Prosperity

**Chapter 2: Prosperity**
- 2.1: Low-Carbon Economy
- 2.3: Acceptable Housing

**Chapter 3: Environment**
- 3.2: Climate Adaptation
- 3.4: Water & Air Quality

### Quality of Life Framework Domains (Annex 3), pp.63-68

- **Good Governance** - Trust, transparency, and public participation
- **Prosperity** - Economic wellbeing and opportunity
- **Environment** - Sustainable and healthy ecosystems
- **Health** - Physical and mental wellbeing


## File Structure

```
fsds-governance-architecture/
├── README.md                           # Technical documentation and usage guide
├── LICENSE                             # CC BY-NC-SA 4.0 licensed for non-commercial use
├── requirements.txt                    # Python dependencies
├── app.py                              # Streamlit web application
├── generate_chart.py                   # Static chart generator
├── assets/                             # Documentation assets (images)
    ├── fig1_dsds_fsds_relationship.png # Official ECCC Figure 1
    └── analytical_fsds_implementation_density.png # App snapshot (Figure 2)
```

## Dependencies

```
streamlit>=1.28.0
plotly>=5.17.0
kaleido>=0.2.1
pillow>=9.0.0
```

## Installation Guide by Platform

### macOS

```bash
# Using Homebrew (optional)
brew install python3

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
```

### Windows

```powershell
# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
```

### Linux (Ubuntu/Debian)

```bash
# Install Python and pip
sudo apt-get install python3 python3-pip python3-venv

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
```

---


## How to Read the Visualization

### Federal Governance Architecture

**Figure 1** _Relationship between the DSDS and Key Components of the FSDS_

![A horizontal flowchart illustrating the structural hierarchy of federal sustainability planning. Four circular nodes are connected by a broad directional arrow. The first three nodes are blue, representing the Federal Sustainable Development Strategy (FSDS): Goals (objectives reflecting government priorities), Targets (concrete objectives contributing to goals), and Implementation Strategies (the plan of action for specific targets). These connect to a final maroon node representing Departmental Sustainable Development Strategies (DSDS): Departmental Actions (concrete activities contributing to implementation strategies). Adapted from Draft 2026–2029 Federal Sustainable Development Strategy, p. 3.](assets/fig1_dsds_fsds_relationship.png)


_Note._ This horizontal flowchart illustrates the structural hierarchy of federal sustainability planning. It maps the flow from FSDS Goals and Targets to specific Departmental Actions. Source: _Draft 2026–2029 Federal Sustainable Development Strategy_ (Environment and Climate Change Canada, 2026, p. 3).

### **Sankey Mapping: FSDS Implementation Density**

**Figure 2** _Analytical Mapping of FSDS Implementation Density across Federal Organizations_
![A Sankey diagram showing the flow of implementation strategies from federal organizations on the left, through FSDS Goals in the center, to Quality of Life domains on the right. Flow thickness indicates the number of implementation strategies, revealing the operational density of the governance architecture.](assets/analytical_fsds_implementation_density.png)



This dashboard **visually interprets** the governance hierarchy defined in **Figure 1** above. While Figure 1 establishes the **Goals, Targets, and Implementation Strategies** that define the federal government’s plan of action, this visualization maps the **volume and distribution** of those strategies across the federal ecosystem. This provides a transparent view of the scaling of sustainability **implementation** from individual departments to Quality of Life outcomes.


### Column Definitions

- **Left Column: Federal Organizations** — Federal departments and agencies responsible for identifying **Departmental Actions** that contribute to federal implementation. Width indicates relative involvement.
    
- **Middle Column: FSDS Goals** — Objectives reflecting the Government of Canada's priorities, organized by chapter: **Building an Inclusive and Resilient Society** (1), **Driving Clean Growth** (2), and **Protecting Our Environment and Well-Being** (3).
    
- **Right Column: Quality of Life Framework Domains** — Four outcome domains showing how specific **Implementation Strategies** contribute to broader societal wellbeing.


### Flow Lines
- **Thickness**: Represents the number of implementation strategies connecting each organizational level
- **Colour**: Transparency indicates flow intensity
- **Direction**: Left to right, cascading from organization through goals to outcomes.

  
    
### **Terminology & Data Units**

- **Implementation Strategy (Data Unit)** — Each "flow" line represents a specific federal plan of action designed to support an FSDS Target.
    
- **Flow Thickness** — The width of the connecting lines is determined by the _total count_ of implementation strategies mapped between two points.
    
- **Nodes** — The vertical bars representing specific Organizations, Goals, or Domains.




## Data Source

- **Authoring Body:** Environment and Climate Change Canada (ECCC)
    
- **Document:** _Draft 2026–2029 Federal Sustainable Development Strategy_
    
- **Reference Sections:** Annex 2 (Federal Organizations) & Annex 3 (Quality of Life Framework), pp. 56–68.
    
- **Consultation Window:** January 12 – May 12, 2026.
  

## Customization

### Modifying the Sankey Diagram

Edit `generate_chart.py` or `app.py` to:

1. **Change organizations**:
```python
federal_orgs = [
    "Your Organization 1",
    "Your Organization 2",
    # ... etc
]
```

2. **Adjust connections**:
```python
connections = [
    (org_index, goal_index, strength),
    # ... etc
]
```

3. **Update colours**:
```python
fed_org_colors = ['#color1', '#color2', ...]
```

4. **Modify layout**:
```python
fig.update_layout(
    height=800,
    width=1512,
    # ... other properties
)
```

## Performance Considerations

- **Browser Performance**: Interactive HTML works best on Chrome, Firefox, and Safari
- **PNG Export**: Requires kaleido library; if unavailable, falls back to HTML export

## Troubleshooting

### Issue: Kaleido import error
```
ModuleNotFoundError: No module named 'kaleido'
```
**Solution**: Install kaleido explicitly
```bash
pip install kaleido
```

### Issue: Streamlit port already in use
```
Error: Could not connect to Streamlit (port 8501 is in use)
```
**Solution**: Run on different port
```bash
streamlit run app.py --server.port 8502
```

### Issue: PNG export not working
**Solution**: Use HTML export instead
```python
from generate_chart import create_fsds_governance_chart, save_as_html
fig = create_fsds_governance_chart()
save_as_html(fig, 'chart.html')
```

---


## Contributing

Contributions welcome under AGPLv3 terms for non-commercial work:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/your-feature`
3. **Make changes** with clear, documented code
4. **Test thoroughly**
5. **Submit a pull request** with description of changes

### Areas for Contribution

- Additional themes/color schemes
- French translation 
- Enhanced documentation
- Additional export formats
- Performance optimizations
- Bug fixes



## Citation

If you use this visualization in academic work, please cite:

```
@software{fsds_governance_2026,
  author = {Guerrier, Andy Sabrina for Brain Climate \& Equity Collaborative},
  title = {FSDS Governance Architecture Dashboard},
  year = {2026},
  url = {https://github.com/sguer/fsds-governance-architecture},
  license = {CC BY-NC-SA 4.0}
}
```

---


## Contact & Support

**Primary Organizational Contact**

Brain Climate & Equity Collaborative (Brain-CE)

Email: muse@brainclimate.org

**Technical Lead & Corresponding Author**

Andy Sabrina Guerrier | Brain-CE Fellow

Email: sguer102@uottawa.ca


---


---

## Acknowledgments

- **The Brain Climate & Equity (Brain-CE) Collaborative**: For providing the **Four-Pillar Action Framework** that guided the development of this resource. This tool contributes specifically to the Collaborative’s mission of **evidence synthesis** and **health equity analysis**.
    
- **Environment and Climate Change Canada (ECCC)**: Primary source for the _Draft 2026–2029 Federal Sustainable Development Strategy_ (Annexes 2 & 3). Participation in the **Sustainability Directorate’s** webinar consultations was instrumental in inspiring the tool’s scope for mapping federal implementation data against the Strategy's high-level goals.
    
- **Technical Stack**: Developed as an **independent analytical resource** using [Plotly](https://plotly.com/python/) and [Streamlit](https://docs.streamlit.io/) to facilitate the **visualization of connections** between federal actions, sustainability mandates, and societal wellbeing outcomes.
    

---

## Related Resources

- [Federal Sustainable Development Strategy (FSDS)](https://www.canada.ca/en/environment-climate-change/services/climate-change/federal-sustainable-development-strategy.html)


- [Brain Climate & Equity (Brain-CE) Collaborative](https://brainclimate.org) — Addressing the Intersection of Brain Health, Climate Justice, and Health Equity.

- [Quality of Life Framework](https://www.canada.ca/en/government/system/government-wide-reporting-spending-operations/government-spending/quality-life-framework-canada.html)
  

---


## Version History

### v1.1.0 (2026-02-12)

- **Structural Alignment**: Added **Figure 1** (ECCC Architecture) and **Figure 2** (Analytical Sankey) to better link federal strategy to implementation data.
    
- **Asset Organization**: Moved documentation images into a dedicated `assets/` folder to separate them from script outputs.
    
- **Accessibility Progress**: Added initial ALT text for images and descriptive figure notes to improve screen-reader compatibility.
    
- **Technical Documentation**: Clarified the relationship between federal goals and departmental actions.
  

### v1.0.0 (2026-02-11)
- Initial release
- Created Streamlit dashboard
- Included static PNG generator

---


## Future Roadmap

- [ ] **Federal Sustainable Development Act (S.C. 2008, c. 33)**: Mapping visualization to the 7 Principles of the *Act*, as reflected in the Strategy:
    - *Efficient use of resources with integrated decision making*
    - *Sustainable development as a continually evolving concept*
    - *Intergenerational equity*
    - *Openness and transparency*
    - *Involving Indigenous Peoples*
    - *Collaboration*
    - *Results and delivery approach*
      
- [ ] **Environmental Justice Alignment**: Integrate the upcoming *National Strategy* required by the *National Strategy Respecting Environmental Racism and Environmental Justice Act* (S.C. 2024, c. 11).
    *Target Date:* **Summer 2026** (aligned with the statutory deadline to table and publish the strategy).
    *Current alignment focuses on the consultation pillars:*
    - *Foundation 2*: Assessing and preventing environmental racism
    - *Foundation 3*: Links between race, socio-economic status, and environmental risk
    - *Foundation 4*: Indigenous environmental justice
      
**Feature Backlog**
- [ ] *Bilingual Interface*: Full French and English support.

- [ ] *Granular Filtering*: Direct search by FSDS Target ID 

- [ ] *Export Engine*: Generate PDF artefacts and presentation-ready images.

- [ ] *Performance & UI*: Responsive mobile design, dark mode refinements, and programmatic API access.



---

Made with care for collaborative knowledge translation ❤️ 
Last Updated: 2026-02-12
