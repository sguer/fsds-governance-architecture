"""
FSDS Governance Architecture Chart Generator
=========================================
This script generates a Sankey diagram visualizing the governance architecture 
and framework alignment for the 2026-2029 Draft Federal Sustainable Development Strategy (FSDS).

Author: Open Source
License: GNU AGPLv3
Repository: https://github.com/sguer/fsds-governance-architecture

This code is open-source and freely available for educational and research purposes.
"""

import plotly.graph_objects as go
import plotly.io as pio
from PIL import Image
import io


def create_fsds_governance_chart():
    """
    Create the FSDS Governance Architecture chart 
   
    """
    
    # Define the data structure
    federal_orgs = [
        "ISC\n(Indigenous Services)",
        "ECCC\n(Environment & Climate)",
        "HICC\n(Housing & Infrastructure)",
        "ESDC\n(Employment & Social)",
        "JUS\n(Justice Canada)",
        "WAGE\n(Women & Gender Equity)",
        "PHAC\n(Public Health)"
    ]
    
    fsds_goals = [
        "Goal 1.1:\nConfidence\nin Gov't",
        "Goal 1.4:\nReduce\nSystemic Racism",
        "Goal 1.6:\nIndigenous\nProsperity",
        "Goal 2.1:\nLow-Carbon\nEconomy",
        "Goal 2.3:\nAcceptable\nHousing",
        "Goal 3.2:\nClimate\nAdaptation",
        "Goal 3.4:\nWater & Air\nQuality"
    ]
    
    qol_domains = [
        "QoL:\nGood\nGovernance",
        "QoL:\nProsperity",
        "QoL:\nEnvironment",
        "QoL:\nHealth"
    ]
    
    # Create node labels
    all_nodes = federal_orgs + fsds_goals + qol_domains
    node_indices = {node: i for i, node in enumerate(all_nodes)}
    
    # Define connections (source, target, value)
    connections = [
        # ISC connections
        (0, 7, 3),    # ISC -> Goal 1.1
        (0, 8, 4),    # ISC -> Goal 1.4
        (0, 9, 5),    # ISC -> Goal 1.6
        
        # ECCC connections
        (1, 10, 5),   # ECCC -> Goal 2.1
        (1, 13, 4),   # ECCC -> Goal 3.2
        (1, 14, 5),   # ECCC -> Goal 3.4
        
        # HICC connections
        (2, 10, 3),   # HICC -> Goal 2.1
        (2, 11, 5),   # HICC -> Goal 2.3
        (2, 13, 2),   # HICC -> Goal 3.2
        
        # ESDC connections
        (3, 7, 4),    # ESDC -> Goal 1.1
        (3, 11, 3),   # ESDC -> Goal 2.3
        (3, 12, 4),   # ESDC -> Goal 3.4
        
        # JUS connections
        (4, 8, 3),    # JUS -> Goal 1.4
        (4, 7, 2),    # JUS -> Goal 1.1
        
        # WAGE connections
        (5, 8, 4),    # WAGE -> Goal 1.4
        (5, 7, 2),    # WAGE -> Goal 1.1
        
        # PHAC connections
        (6, 14, 5),   # PHAC -> Goal 3.4
        (6, 12, 4),   # PHAC -> Goal 3.2
        
        # Goals to QoL connections
        (7, 15, 4),   # Goal 1.1 -> QoL: Good Governance
        (8, 15, 5),   # Goal 1.4 -> QoL: Good Governance
        (9, 15, 4),   # Goal 1.6 -> QoL: Good Governance
        (10, 16, 4),  # Goal 2.1 -> QoL: Prosperity
        (11, 16, 4),  # Goal 2.3 -> QoL: Prosperity
        (12, 18, 4),  # Goal 3.2 -> QoL: Health
        (13, 17, 5),  # Goal 3.2 -> QoL: Environment
        (14, 17, 5),  # Goal 3.4 -> QoL: Environment
    ]
    
    # Extract source, target, value
    source = [node_indices[federal_orgs[c[0]]] for c in connections]
    target = [node_indices[all_nodes[c[1]]] for c in connections]
    value = [c[2] for c in connections]
    
    # Define colours
    fed_org_colours = ['#8B6F47', '#2d7d6a', '#1f4788', '#6b7c3a', '#5c4d8f', '#a85555', '#1a5c7a']
    goal_colours = ['#4a5f7f', '#b85555', '#8b6f47', '#2b7d8b', '#458a5f', '#5b8b4d', '#2d6ba8']
    qol_colours = ['#3a4d5f', '#8b9d4d', '#4b7a8f', '#8b4f4d']
    
    # Create complete colour list
    node_colours = fed_org_colours + goal_colours + qol_colours
    
    # Create the Sankey diagram
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color='black', width=0.5),
            label=all_nodes,
            color=node_colours
        ),
        link=dict(
            source=source,
            target=target,
            value=value,
            color=['rgba(200, 150, 100, 0.4)'] * len(source)
        )
    )])
    
    # Update layout with proper centering and improved text
    fig.update_layout(
        title={
            'text': (
                "<b>Draft 2026-2029 FSDS: Governance Architecture & Framework Alignment</b><br>"
                "<sub>Mapping implementation strategy distribution from responsible federal organizations through FSDS goals to Quality of Life Framework domains</sub>"
            ),
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 16}
        },
        font=dict(size=10, family='Arial'),
        plot_bgcolor='white',
        paper_bgcolor='white',
        height=800,
        width=1512,
        margin=dict(b=150, t=100, l=50, r=50)
    )
    
    # Add corrected data source annotation
    fig.add_annotation(
        text=(
            "Data Source: Government of Canada (2026). Draft 2026-2029 Federal Sustainable Development Strategy, Annexes 2 & 3. "
            "Flow thickness represents implementation strategy count.<br>"
            "<i>Chart generated using open-source code (GNU AGPLv3 License)</i>"
        ),
        xref='paper', yref='paper',
        x=0.5, y=-0.15,
        showarrow=False,
        xanchor='center',
        yanchor='top',
        font=dict(size=9, color='#666666'),
        bgcolor='rgba(255, 255, 255, 0.8)',
        bordercolor='#cccccc',
        borderwidth=1,
        borderpad=10
    )
    
    return fig


def save_as_png(fig, output_path):
    """
    Save the Plotly figure as a PNG image.
    
    Args:
        fig: Plotly figure object
        output_path: Path where PNG should be saved
    """
    fig.write_image(output_path, width=1512, height=900, scale=2)
    print(f"Chart saved to {output_path}")


def save_as_html(fig, output_path):
    """
    Save the Plotly figure as an interactive HTML file.
    
    Args:
        fig: Plotly figure object
        output_path: Path where HTML should be saved
    """
    fig.write_html(output_path)
    print(f"Interactive chart saved to {output_path}")


if __name__ == "__main__":
    # Generate the chart
    print("Generating FSDS Governance Architecture Chart...")
    fig = create_fsds_governance_chart()
    
    # Save as PNG
    try:
        save_as_png(fig, "/mnt/user-data/outputs/FSDS_Governance_Architecture.png")
    except Exception as e:
        print(f"Note: PNG export requires kaleido library. Error: {e}")
        print("Saving as HTML instead...")
        save_as_html(fig, "/mnt/user-data/outputs/FSDS_Governance_Architecture.html")
    
    # Also save interactive version
    save_as_html(fig, "/mnt/user-data/outputs/FSDS_Governance_Architecture.html")
    
    print("Done!")
