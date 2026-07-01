import pandas as pd
import logging

def clean_dataset(df):
    """🧹 Strips data noise, standardizes casings, and patches empty cells."""
    if df is None or df.empty:
        logging.warning("Cleaner received an empty DataFrame array.")
        return None
        
    print("🧹 [Cleaner] Initializing column filters and text wrangler tools...")
    
    # Isolate core columns
    target_fields = ['id', 'name', 'symbol', 'current_price', 'market_cap', 'price_change_percentage_24h']
    cleaned_df = df[target_fields].copy()
    
    # Text normalization: force string tokens to clean uppercase symbols
    cleaned_df['symbol'] = cleaned_df['symbol'].str.upper()
    
    # Missing value imputation: fallback safely to 0.0 if a price value is blank
    cleaned_df['price_change_percentage_24h'] = cleaned_df['price_change_percentage_24h'].fillna(0.0)
    
    # Remove duplicates
    cleaned_df = cleaned_df.drop_duplicates(subset=['id'])
    
    logging.info(f"Sanitization routines complete. Grid scaled to {len(cleaned_df)} items.")
    return cleaned_df