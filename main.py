import logging
from data_fetcher import fetch_market_data
from data_cleaner import clean_dataset
from data_analyzer import calculate_metrics
from data_visualizer import generate_analytics_dashboard
from pdf_generator import compile_executive_pdf

# Setup logging properties cleanly across all modules
logging.basicConfig(
    filename="app_activity.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def run_system_pipeline():
    print("==========================================================")
    print("⚡ SCHOLAROPS MODULAR DATA PIPELINE SUITE ENGINE RUNNING")
    print("==========================================================\n")
    logging.info("--- Modular Application Session Launched ---")
    
    # 1. Fetch
    raw_df = fetch_market_data()
    if raw_df is None or raw_df.empty:
        print("❌ Fatal pipeline processing check failure. Raw data is unavailable.")
        return
        
    # 2. Clean
    clean_df = clean_dataset(raw_df)
    
    # 3. Analyze
    metrics_dict = calculate_metrics(clean_df)
    
    # 4. Visualize
    chart_output_file = generate_analytics_dashboard(clean_df)
    
    # 5. Save Report to PDF
    compile_executive_pdf(metrics_dict, chart_output_file)
    
    # 6. Save data matrix records down locally into a backup CSV file
    csv_backup_path = "data/crypto_cleansed_records.csv"
    import os
    os.makedirs("data", exist_ok=True)
    clean_df.to_csv(csv_backup_path, index=False)
    print(f"💾 [Backup Engine] Extracted rows backed up cleanly to path: '{csv_backup_path}'")
    
    print("\n==========================================================")
    print("🎉 FRAMEWORK RESOLVED: ALL PIPELINE STAGES STEP COMPLETED")
    print("==========================================================")
    logging.info("--- Modular Application Session Ended Gracefully ---")

if __name__ == "__main__":
    run_system_pipeline()