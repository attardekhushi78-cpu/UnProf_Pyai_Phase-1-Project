import os
import logging
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

PDF_OUTPUT_PATH = "reports/Phase1_Final_Execution_Report.pdf"

def compile_executive_pdf(metrics, chart_file_path):
    """📄 Compiles calculated dict parameters and charts into an immutable PDF report."""
    print("📄 [PDF Engine] Programmatically assembling ReportLab file blocks...")
    os.makedirs("reports", exist_ok=True)
    
    # Initialize Document Configuration parameters
    doc = SimpleDocTemplate(PDF_OUTPUT_PATH, pagesize=letter, leftMargin=40, rightMargin=40, topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()
    story = []
    
    # Define typographic layout features
    title_layout = ParagraphStyle('DocTitle', parent=styles['Heading1'], fontSize=22, textColor=colors.HexColor("#2c3e50"), spaceAfter=12)
    body_layout = ParagraphStyle('DocBody', parent=styles['Normal'], fontSize=10, leading=14, textColor=colors.HexColor("#333333"))
    
    # Generate structural header text flows
    story.append(Paragraph("ScholarOps End-to-End Modular Report", title_layout))
    story.append(Paragraph("<b>Phase 1 Core Graduation Project Framework</b>", body_layout))
    story.append(Spacer(1, 15))
    
    # Map array indices cleanly onto a nested structure to create a tabular display grid
    grid_matrix = [
        [Paragraph("<b>Core Ingestion Parameter</b>", body_layout), Paragraph("<b>Statistical Calculation Value</b>", body_layout)],
        ["Highest Single Asset Unit Price", f"${metrics['highest_valuation']:,.2f}"],
        ["Lowest Single Asset Unit Price", f"${metrics['lowest_valuation']:,.2f}"],
        ["Overall Group Movement Mean", f"{metrics['average_market_movement']:.2f}%"],
        ["Volatility Scale Variance (StdDev)", f"{metrics['volatility_deviation']:.2f}"]
    ]
    
    report_table = Table(grid_matrix, colWidths=[240, 160])
    report_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (1, 0), colors.HexColor("#f8f9fa")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#dcdde1")),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    
    story.append(Paragraph("<h3>NumPy Analytics Summary Matrix</h3>", title_layout))
    story.append(report_table)
    story.append(Spacer(1, 20))
    
    # Embed the saved chart file directly into the layout sequence safely
    if os.path.exists(chart_file_path):
        story.append(Paragraph("<h3>Matplotlib Visual Dashboard Metrics Output</h3>", title_layout))
        story.append(Image(chart_file_path, width=500, height=180))
        
    doc.build(story)
    logging.info(f"Executive document print finalized. Compiled output saved to: {PDF_OUTPUT_PATH}")
    print(f"🏆 Success! Final report generated cleanly at path: '{PDF_OUTPUT_PATH}'")