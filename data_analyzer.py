import numpy as np
import logging

def calculate_metrics(df):
    """📊 Converts active dataframe attributes into raw NumPy registers for speed math."""
    if df is None or df.empty:
        return None
        
    print("📊 [Analyzer] Handing matrix slices to NumPy vectorized math arrays...")
    
    # Extract structural series elements straight into pure NumPy arrays
    prices_array = np.array(df['current_price'])
    fluctuations_array = np.array(df['price_change_percentage_24h'])
    
    # Execute lightning-fast vector analytics computations
    summary_metrics = {
        "highest_valuation": float(np.max(prices_array)),
        "lowest_valuation": float(np.min(prices_array)),
        "average_market_movement": float(np.mean(fluctuations_array)),
        "volatility_deviation": float(np.std(fluctuations_array))
    }
    
    logging.info("NumPy statistical matrix extraction resolved successfully.")
    return summary_metrics