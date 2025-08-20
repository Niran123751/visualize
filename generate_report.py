# generate_report.py
# Author contact (verification): 24f2005647@ds.study.iitm.ac.in
#
# Usage:
#   python generate_report.py employees.csv
#
# This script:
#   - Loads the employee CSV
#   - Calculates the frequency count for the "Operations" department
#   - Prints the frequency count to the console
#   - Creates a histogram (bar chart) of department counts using matplotlib
#   - Saves a self-contained HTML file with the results and the chart embedded

import sys
import base64
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from datetime import datetime

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_report.py <employees.csv>")
        sys.exit(1)

    csv_path = sys.argv[1]
    df = pd.read_csv(csv_path)

    # Ensure expected columns exist
    required_cols = {"employee_id", "department", "region", "performance_score", "years_experience", "satisfaction_rating"}
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns in CSV: {missing}")

    # Calculate department frequencies
    dept_counts = df["department"].value_counts().sort_index()
    ops_count = int(dept_counts.get("Operations", 0))

    # Print frequency count to console
    print(f"Frequency count for 'Operations' department: {ops_count}")

    # Create the bar chart for department distribution
    plt.figure(figsize=(8, 5))  # one plot, no seaborn, no specific colors per instructions
    dept_counts.plot(kind="bar")
    plt.title("Department Distribution")
    plt.xlabel("Department")
    plt.ylabel("Count of Employees")
    plt.tight_layout()

    # Save plot to a PNG buffer
    buf = BytesIO()
    plt.savefig(buf, format="png", dpi=150)
    plt.close()
    buf.seek(0)
    img_b64 = base64.b64encode(buf.read()).decode("utf-8")

    # Build a simple, self-contained HTML report
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    html = f"""        <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Employee Department Distribution Report</title>
        <style>
            body {{ font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif; margin: 2rem; }}
            h1, h2 {{ margin: 0.2rem 0; }}
            .meta {{ color: #555; font-size: 0.95rem; margin-bottom: 1rem; }}
            .card {{ border: 1px solid #e5e7eb; border-radius: 16px; padding: 1rem 1.25rem; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }}
            .codebox {{ background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 12px; padding: 0.75rem 1rem; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; font-size: 0.9rem; white-space: pre-wrap; }}
            footer {{ margin-top: 2rem; color: #666; font-size: 0.9rem; }}
            img {{ max-width: 100%; height: auto; }}
        </style>
    </head>
    <body>
        <h1>Employee Department Distribution Report</h1>
        <div class="meta">Generated: {now}</div>

        <div class="card">
            <h2>Operations Department Frequency</h2>
            <p><strong>Frequency count for 'Operations': {ops_count}</strong></p>
        </div>

        <div class="card" style="margin-top: 1rem;">
            <h2>Department Histogram</h2>
            <p>The chart below shows the distribution of employees across departments.</p>
            <img alt="Department Distribution Histogram" src="data:image/png;base64,{img_b64}" />
        </div>

        <div class="card" style="margin-top: 1rem;">
            <h2>Console Output</h2>
            <div class="codebox">Frequency count for 'Operations' department: {ops_count}</div>
        </div>

        <footer>
            Contact / verification email: 24f2005647@ds.study.iitm.ac.in
        </footer>
    </body>
    </html>
    """

    out_html = "employee_report.html"
    with open(out_html, "w", encoding="utf-8") as f:
        f.write(html)

    # Also print where we saved the file
    print(f"Saved HTML report to: {out_html}")

if __name__ == "__main__":
    main()