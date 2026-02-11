"""
2026-2029 FSDS Governance Architecture (Dynamic Data Version)
=============================================================
Streamlit application that visualizes data from fsds_data.json.
Includes full-text hover and tabular data views.
"""

import streamlit as st
import plotly.graph_objects as go
import json
import os
import pandas as pd

# --- 1. SETUP & CONFIGURATION ---
st.set_page_config(
    page_title="FSDS Governance Architecture",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. DATA LOADING ---
@st.cache_data
def load_data():
    """Loads the JSON data."""
    file_path = 'fsds_data.json'
    
    if not os.path.exists(file_path):
        st.error(f"File not found: {file_path}. Please ensure the JSON file is in the same directory.")
        return None
        
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

data = load_data()

# --- 3. DATA PROCESSING LOGIC ---
def process_fsds_data(data, min_strategies=0, theme='light'):
    """
    Processes the raw JSON into Sankey nodes and links.
    Returns truncated labels for the chart AND full labels for hover.
    """
    organizations = data['organizations']
    goals = data['goals']
    qol_domains = data['qol_domains']
    
    # Filter Organizations based on strategy count
    filtered_orgs = []
    for code, org in organizations.items():
        total_strat = (len(org['chapter1_strategies']) + 
                       len(org['chapter2_strategies']) + 
                       len(org['chapter3_strategies']))
        if total_strat >= min_strategies:
            filtered_orgs.append(org)
            
    # Sort orgs alphabetically
    filtered_orgs.sort(key=lambda x: x['code'])

    # --- NODE CREATION ---
    
    # 1. ORG LABELS
    # Short: "ISC\n(Indigenous...)"
    # Full: "Indigenous Services Canada (ISC)"
    org_labels_short = [f"{org['code']}\n({org['name'].split('(')[0][:20]}...)" for org in filtered_orgs]
    org_labels_full = [f"{org['name']} ({org['code']})" for org in filtered_orgs]
    
    # 2. GOAL LABELS
    sorted_goal_keys = sorted(goals.keys())
    # Short: "Goal 1.1..."
    # Full: "Goal 1.1: Improve trust in government"
    goal_labels_short = [f"Goal {g['code']}:\n{g['title'].split(' ')[0]}..." for g in [goals[k] for k in sorted_goal_keys]]
    goal_labels_full = [f"Goal {g['code']}: {g['title']}" for g in [goals[k] for k in sorted_goal_keys]]
    
    # 3. QOL LABELS
    qol_order = ['good_governance', 'prosperity', 'environment', 'health', 'society']
    # Short & Full are usually similar for QoL, but we standardize
    valid_qol = [k for k in qol_order if k in qol_domains]
    qol_labels_short = [f"QoL:\n{qol_domains[k]['name']}" for k in valid_qol]
    qol_labels_full = [f"Quality of Life Domain: {qol_domains[k]['name']}" for k in valid_qol]
    
    # Combine all
    all_labels_short = org_labels_short + goal_labels_short + qol_labels_short
    all_labels_full = org_labels_full + goal_labels_full + qol_labels_full
    
    # Create Mapping
    node_map = {}
    current_idx = 0
    
    for org in filtered_orgs:
        node_map[f"ORG_{org['code']}"] = current_idx
        current_idx += 1
    for key in sorted_goal_keys:
        node_map[f"GOAL_{key}"] = current_idx
        current_idx += 1
    for key in valid_qol:
        node_map[f"QOL_{key}"] = current_idx
        current_idx += 1

    # --- LINK CREATION ---
    source = []
    target = []
    value = []
    link_color_indices = [] 
    
    # Links: Org -> Goal
    for org in filtered_orgs:
        org_idx = node_map.get(f"ORG_{org['code']}")
        all_strategies = (org['chapter1_strategies'] + 
                          org['chapter2_strategies'] + 
                          org['chapter3_strategies'])
        
        goal_counts = {}
        for strat in all_strategies:
            parts = strat.split('.')
            if len(parts) >= 2:
                goal_code = f"{parts[0]}.{parts[1]}"
                if goal_code in goals:
                    goal_counts[goal_code] = goal_counts.get(goal_code, 0) + 1
        
        for goal_code, count in goal_counts.items():
            goal_idx = node_map.get(f"GOAL_{goal_code}")
            if org_idx is not None and goal_idx is not None:
                source.append(org_idx)
                target.append(goal_idx)
                value.append(count)
                link_color_indices.append(org_idx)

    # Links: Goal -> QoL
    for goal_code in sorted_goal_keys:
        goal_data = goals[goal_code]
        goal_idx = node_map.get(f"GOAL_{goal_code}")
        
        for domain_code in goal_data['qol_domains']:
            qol_idx = node_map.get(f"QOL_{domain_code}")
            if goal_idx is not None and qol_idx is not None:
                source.append(goal_idx)
                target.append(qol_idx)
                value.append(5) 
                link_color_indices.append(goal_idx)

    return all_labels_short, all_labels_full, source, target, value, link_color_indices, len(filtered_orgs)

# --- 4. COLOR & STYLE LOGIC ---
def get_colors(node_count, theme):
    if theme == 'light':
        bg_color = 'white'
        text_color = '#111111'
        blues = ['#2c6e8f', '#4a6fa5', '#4a5f70', '#5c8ba3']
        greens = ['#2d7d6a', '#5ba375', '#6ca35e', '#8c8c46']
        reds = ['#c06c6c', '#a85555', '#b85555', '#8b4f4d']
        golds = ['#8B6F47', '#c9a85a', '#a3845b']
        palette = (blues + greens + reds + golds) * 5
    else:
        bg_color = '#1a1a1a'
        text_color = '#ffffff'
        palette = ['#4a7bcc', '#5a8cc4', '#4ba892', '#9bc074', '#d08080', '#e08080', '#c9a85a'] * 10
    return bg_color, text_color, palette[:node_count]

def hex_to_rgba(hex_code, opacity):
    if hex_code.startswith('#'):
        hex_code = hex_code.lstrip('#')
        rgb = tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))
        return f'rgba({rgb[0]}, {rgb[1]}, {rgb[2]}, {opacity})'
    return hex_code

# --- 5. CHART GENERATION ---
def create_chart(min_strategies, theme):
    if not data:
        return go.Figure()

    # Get data including FULL labels
    labels_short, labels_full, source, target, value, color_indices, org_count = process_fsds_data(data, min_strategies, theme)
    
    bg_color, text_color, palette = get_colors(len(labels_short), theme)
    node_colors = [palette[i % len(palette)] for i in range(len(labels_short))]
    link_colors = [hex_to_rgba(node_colors[src_idx], 0.4) for src_idx in color_indices]
    
    node_thickness = 250 if org_count < 10 else 50

    fig = go.Figure(data=[go.Sankey(
        textfont=dict(size=12, color=text_color, family="Arial Black"),
        node=dict(
            pad=15,
            thickness=node_thickness,
            line=dict(color='white', width=0),
            label=labels_short, # Show SHORT labels on chart
            customdata=labels_full, # Store FULL labels for hover
            hovertemplate='%{customdata}<extra></extra>', # Use FULL labels on hover
            color=node_colors
        ),
        link=dict(
            source=source,
            target=target,
            value=value,
            color=link_colors
        )
    )])
    
    chart_height = max(800, org_count * 40)

    fig.update_layout(

        font=dict(size=12, color=text_color),
        plot_bgcolor=bg_color,
        paper_bgcolor=bg_color,
        height=chart_height,
        margin=dict(l=20, r=20, t=40, b=80) 
    )
    
    return fig, org_count

# --- 6. APP UI LAYOUT ---

# Sidebar
with st.sidebar:
    st.title("Configuration")
    theme = st.radio("Theme", ["Light", "Dark"], index=0).lower()
    
    st.divider()
    st.subheader("Data Filters")
    min_strat_filter = st.slider(
        "Minimum Strategy Count",
        min_value=0, max_value=15, value=0,
        help="Filter out organizations with fewer implementation strategies."
    )
    st.info(f"Showing organizations with {min_strat_filter}+ strategies.")
    
    # --- OFFICIAL RESOURCES & LINKS ---
    st.divider()
    st.subheader("Official Resources")
    
    text_color = '#111111' if theme == 'light' else '#ffffff'
    
    st.markdown(f"""
    <div style="font-size: 13px; color: {text_color}; line-height: 1.6;">
        <p><b>FSDS Documents:</b></p>
        <ul style="padding-left: 20px;">
            <li><a href="https://www.canada.ca/en/environment-climate-change/corporate/transparency/consultations/share-your-throughts-draft-2026-2029-federal-sustainable-development-strategy/draft-strategy.html" target="_blank">Consultation Draft 2026–2029</a></li>
            <li><a href="https://www.canada.ca/en/environment-climate-change/services/climate-change/federal-sustainable-development-strategy/strategies-reports/2025-progress-report.html" target="_blank">2025 FSDS Progress Report</a></li>
        </ul>
        <p><b>Get Involved:</b></p>
        <ul style="padding-left: 20px;">
            <li><a href="https://www.canada.ca/en/environment-climate-change/corporate/transparency/consultations/share-your-throughts-draft-2026-2029-federal-sustainable-development-strategy.html" target="_blank">Consultation Process Details</a></li>
        </ul>
        <div style="background-color: rgba(139, 111, 71, 0.1); padding: 10px; border-radius: 5px; border-left: 3px solid #8B6F47; margin-top: 15px;">
            <p style="font-size: 12px; margin-bottom: 0;">
                <b>Consultation Deadline:</b><br>
                May 12, 2026
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Main Page
st.title("Consultation Draft 2026-2029 FSDS")

text_color = '#111111' if theme == 'light' else '#ffffff'

# --- HEADER BLOCK ---
st.markdown(f"""
<div style="text-align: left; padding-right: 20px;">
    <h3 style="color: {text_color}; margin-bottom: 5px; border-bottom: 2px solid #8B6F47; display: inline-block;">
        Governance Architecture & Framework Alignment
    </h3>
    <p style="font-size: 14px; color: {text_color}; margin-top: 10px; font-style: italic;">
        Visualizing the distribution of implementation strategies across federal organizations.
    </p>
    <div style="color: {text_color}; line-height: 1.6; margin-top: 20px; margin-bottom: 20px;">
        <p>This interactive dashboard visualizes the <b>whole-of-government framework</b> for sustainable development as outlined in the 
        <i>Consultation Draft 2026–2029 Federal Sustainable Development Strategy</i> (Environment and Climate Change Canada, 2026). 
        Under the <b>Federal Sustainable Development Act</b>, this strategy reflects the collective efforts of 
        <b>48 federal organizations</b> to advance shared priorities. The tool tracks how 
        departmental commitments flow through specific <b>FSDS goals</b> to support outcomes within Canada's 
        <b>Quality of Life Framework</b>.</p>
    </div>
</div>
""", unsafe_allow_html=True)
# -----------------------------


if data:
    # CREATE TABS
    tab_viz, tab_data = st.tabs(["Visualization", "Data Tables"])

    with tab_viz:
        st.markdown("Hover over nodes to see full titles. Adjust filters in the sidebar.")
        chart, org_count = create_chart(min_strat_filter, theme)
        st.plotly_chart(chart, use_container_width=True)
        
        # Footer
        stats = data['statistics']
        st.caption(f"Data Source: Government of Canada (2026). Displaying {org_count} Organizations linking to {stats['total_goals']} Goals.")

    with tab_data:
        st.header("Raw Data Explorer")
        
        # 1. Organization Table
        st.subheader("Federal Organizations & Strategy Counts")
        orgs_list = []
        for code, org in data['organizations'].items():
            count = len(org['chapter1_strategies']) + len(org['chapter2_strategies']) + len(org['chapter3_strategies'])
            if count >= min_strat_filter:
                orgs_list.append({
                    "Code": code,
                    "Organization Name": org['name'],
                    "Total Strategies": count,
                    "Ch.1 Strategies": len(org['chapter1_strategies']),
                    "Ch.2 Strategies": len(org['chapter2_strategies']),
                    "Ch.3 Strategies": len(org['chapter3_strategies']),
                })
        
        df_orgs = pd.DataFrame(orgs_list)
        st.dataframe(df_orgs, use_container_width=True, hide_index=True)
        
        st.divider()
        
        # 2. Goals Table
        st.subheader("FSDS Goals & QoL Alignment")
        goals_list = []
        for code, goal in data['goals'].items():
            goals_list.append({
                "Goal Code": code,
                "Goal Title": goal['title'],
                "Chapter": goal['chapter'],
                "QoL Domains": ", ".join([d.replace('_', ' ').title() for d in goal['qol_domains']])
            })
            
        df_goals = pd.DataFrame(goals_list)
        st.dataframe(df_goals, use_container_width=True, hide_index=True)

else:
    st.warning("Please upload 'fsds_data.json' to view the visualization.")