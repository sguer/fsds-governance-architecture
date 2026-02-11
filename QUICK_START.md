# Quick Start Guide

## Prerequisites

- Python 3.8 or higher
- pip (comes with Python)
- Git (optional, for cloning)

## Option 1: Interactive Web Dashboard (Recommended)

### 1. Download the Files

```bash
git clone https://github.com/yourusername/fsds-governance-architecture.git
cd fsds-governance-architecture
```

Or download the ZIP file and extract it.

### 2. Run Setup Script

**On macOS/Linux:**
```bash
chmod +x setup.sh
./setup.sh
```

**On Windows:**
```cmd
setup.bat
```

### 3. Start the Dashboard

```bash
streamlit run app.py
```

Your browser should open automatically to `http://localhost:8501`

### 4. Explore the Dashboard
- Toggle between Light/Dark themes
- Hover over flows to see connections
- Read explanations in the sidebar
- Check linked resources

## Option 2: Generate Static PNG

### 1-2. (Same as above - setup)

### 3. Generate Image

```bash
python generate_chart.py
```

Output: `FSDS_Governance_Arcitecture.png`

## Manual Setup (If Scripts Don't Work)

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# 3. Install dependencies
pip install streamlit plotly kaleido pillow

# 4. Run app
streamlit run app.py
```

## Troubleshooting

### Python not found
- Install Python from [python.org](https://www.python.org/)
- Add to PATH if on Windows
- Verify: `python --version`

### Port 8501 already in use
```bash
streamlit run app.py --server.port 8502
```

### Module not found errors
```bash
# Activate virtual environment first!
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Then reinstall
pip install -r requirements.txt
```

### Kaleido errors (PNG generation)
- PNG export is optional
- Use HTML export instead (automatically generated)
- Or install: `pip install kaleido`

## What You'll See

### Dashboard Features
- **Interactive Sankey Diagram**: Flow visualization
- **Theme Toggle**: Light/Dark modes
- **Sidebar Documentation**: Data explanations
- **Responsive Layout**: Works on desktop/tablet

### Output Files
- `FSDS_Governance_Architecture.png` - Static image
- `FSDS_Governance_Architecture.html` - Standalone HTML
- Web dashboard at http://localhost:8501

## Key Files Explained

| File | Purpose |
|------|---------|
| `app.py` | Streamlit web application |
| `generate_chart.py` | Static chart generator |
| `requirements.txt` | Python dependencies |
| `README.md` | Full documentation |
| `CONTRIBUTING.md` | Contribution guidelines |

## Next Steps

1. **Read the Full Documentation**: See [README.md](README.md)
2. **Explore the Data**: Hover over chart elements
3. **Customize**: Edit colors, data, or layout
4. **Share**: Export as PNG or HTML
5. **Contribute**: See [CONTRIBUTING.md](CONTRIBUTING.md)

## Common Commands

```bash
# Start dashboard
streamlit run app.py

# Generate static image
python generate_chart.py

# Install specific version
pip install streamlit==1.28.0

# List installed packages
pip list

# Deactivate virtual environment
deactivate
```

## Tips & Tricks

### Save Output to Browser
In Streamlit: Click 3 dots menu → "Settings" → "Theme"

### Export from Dashboard
1. Right-click on chart
2. Select "Download plot as png" (with Plotly toolbar)

### Stop the Server
Press `Ctrl+C` in terminal

### Modify the Chart
Edit `app.py` or `generate_chart.py`:
- Change organizations
- Adjust colors
- Add/remove connections
- Modify layout

## Getting Help

1. **Check README.md** - Most questions answered there
2. **Review errors** - Read error messages carefully
3. **GitHub Issues** - Search for similar problems
4. **Try again** - Sometimes issues resolve on second attempt

## Uninstall / Cleanup

```bash
# Remove virtual environment
rm -rf venv  # macOS/Linux
rmdir venv   # Windows

# Remove output files
rm *.png *.html
```

## Performance

- Dashboard loads in <2 seconds
- Interactive chart renders instantly
- PNG generation takes ~10 seconds
- Works on most modern browsers

## Next: Customization

Want to modify the visualization?

### Change Colors
Edit `app.py`, find:
```python
fed_org_colors = ['#8B6F47', '#2d7d6a', ...]
```

### Add Organizations
Edit the `federal_orgs` list:
```python
federal_orgs = [
    "Your Organization",
    # ... more
]
```

### Add Connections
Edit the `connections` list:
```python
connections = [
    (0, 7, 3),  # (from, to, strength)
    # ... more
]
```

Save and restart: `streamlit run app.py`

## Questions?

- **Installation**: See [README.md](README.md#installation)
- **Usage**: See [README.md](README.md#usage)
- **Troubleshooting**: See [README.md](README.md#troubleshooting)
- **Contributing**: See [CONTRIBUTING.md](CONTRIBUTING.md)

---

**Enjoy exploring the FSDS Governance Architecture Dashboard!** 
