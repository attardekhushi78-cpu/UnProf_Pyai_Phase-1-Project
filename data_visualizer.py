import os
import matplotlib.pyplot as plt
import logging

CHART_PATH = "visuals/market_summary_chart.png"

def generate_analytics_dashboard(df):
    """📈 Plots multiple matrix visualization subplots and writes them down to disk."""
    if df is None or df.empty:
        return None
        
    print("📈 [Visualizer] Rendering canvas plots utilizing Matplotlib engines...")
    
    # Ensure our target output folder exists
    os.makedirs("visuals", exist_ok=True)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle("⚡ ScholarOps Modular Pipeline Live Analytics Dashboard", fontsize=14, fontweight='bold')
    
    top_5 = df.head(5)
    
    # Chart 1: Bar layout configuration
    axes[0].bar(top_5['symbol'], top_5['market_cap'] / 1e9, color='#2c3e50', edgecolor='black')
    axes[0].set_title("Top 5 Asset Cap Scale ($ Billions)")
    axes[0].set_ylabel("Market Cap in Billions")
    
    # Chart 2: Line layout trend line
    axes[1].plot(df['symbol'], df['price_change_percentage_24h'], marker='o', linestyle='--', color='#e74c3c')
    axes[1].axhline(0, color='black', linewidth=0.8, alpha=0.5)
    axes[1].set_title("24h Flux Deviation Percentage (%)")
    axes[1].set_ylabel("Change Metric %")
    
    plt.tight_layout()
    plt.savefig(CHART_PATH, dpi=300)
    plt.close()
    
    logging.info(f"Dashboard graphics drawn and saved cleanly to path: {CHART_PATH}")
    return CHART_PATH