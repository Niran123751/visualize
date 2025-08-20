# Employee Performance Visualization (HTML Export)

Contact / verification: 24f2005647@ds.study.iitm.ac.in

This repository contains a Python script that:
- Loads the employee data (CSV)
- Calculates the frequency count for the "Operations" department
- Prints the frequency count to the console
- Creates a histogram showing the distribution of departments using matplotlib
- Saves a **self-contained HTML** report (`employee_report.html`)

## Files
- `generate_report.py` — main script
- `requirements.txt` — Python dependencies
- `sample_employees.csv` — small sample for sanity-checking (replace with your 100-row dataset)

## How to run locally

1. Create and activate a virtual environment (recommended)
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```
2. Install requirements
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script with your dataset (CSV with 100 employees)
   ```bash
   python generate_report.py employees.csv
   ```
   Replace `employees.csv` with the actual filename. The script will:
   - Print the frequency count for "Operations" to the console
   - Create `employee_report.html` in the current folder

## Publish to GitHub & get the **raw** URL

1. Create a new public GitHub repository (e.g., `employee-performance-report`).
2. Upload (commit) these files:
   - `generate_report.py`
   - `requirements.txt`
   - `employee_report.html` (generated after running the script)
   - Optionally your CSV (if allowed) or keep it private
3. After pushing to GitHub, locate the `employee_report.html` file in your repo.
4. Click the file, then click **"Raw"**. Copy the URL; it should start with:

   `https://raw.githubusercontent.com/<YOUR_USERNAME>/<YOUR_REPO>/<BRANCH>/employee_report.html`

   Example (DO NOT use this literally; replace with your details):

   `https://raw.githubusercontent.com/example-user/employee-performance-report/main/employee_report.html`

Use that raw URL in your checker submission.

---
**Note:** If you need to regenerate the HTML, re-run:
```bash
python generate_report.py employees.csv
```