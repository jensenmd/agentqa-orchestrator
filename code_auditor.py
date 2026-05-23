import os
import json
import time
from google import genai
from pydantic import BaseModel, Field
from file_scanner import scan_project_directory

class FileAuditReport(BaseModel):
    file_name: str = Field(description="The name of the file being audited")
    health_score: int = Field(description="A quality score from 1 to 100")
    test_coverage_gaps: list[str] = Field(description="List of specific edge cases missing")
    code_smells: list[str] = Field(description="List of structural flaws or bad patterns")
    recommended_refactor: str = Field(description="A concise code snippet showing how to fix the core issue")

client = genai.Client()

def run_automated_audit():
    print("====================================================================")
    print("                    AGENTIC QA AUDIT ENGINE                         ")
    print("====================================================================")
    
    target_project = "../qa-automation-showcase" 
    found_files = scan_project_directory(target_project)
    
    if not found_files:
        print("[ERROR]: No source files found to audit.")
        return

    reports_dir = "reports"
    os.makedirs(reports_dir, exist_ok=True)
    
    print(f"\n[SCAN] Found {len(found_files)} source files. Initializing analysis pipeline...")
    
    dashboard_summary = []

    for idx, file_path in enumerate(found_files, 1):
        clean_name = os.path.basename(file_path)
        print(f"\n[{idx}/{len(found_files)}] Analyzing: {clean_name}")
        
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                raw_code_text = f.read()
        except Exception as e:
            print(f"  -> Skip: Unreadable file. {e}")
            dashboard_summary.append({"file": clean_name, "score": "ERR", "status": "SKIPPED"})
            continue

        prompt = f"""
        You are a Principal Software Engineer in Quality. 
        Analyze the following Python code for structural integrity, validation completeness, 
        and testing best practices. Return your analysis strictly matching the requested schema.
        
        SOURCE CODE TO AUDIT ({clean_name}):
        {raw_code_text}
        """
        
        # Auto-Retry Loop for temporary public server traffic spikes
        max_attempts = 2
        response_text = None
        
        for attempt in range(1, max_attempts + 1):
            try:
                print(f"  -> Querying execution engine [gemini-2.5-flash] (Attempt {attempt}/{max_attempts})...")
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                    config={
                        'response_mime_type': 'application/json',
                        'response_schema': FileAuditReport,
                    },
                )
                response_text = response.text
                break # Success! Break out of the retry loop
            except Exception as e:
                if "503" in str(e) and attempt < max_attempts:
                    print("  -> [TRAFFIC ALERT]: Server busy. Pausing 5 seconds for clear path...")
                    time.sleep(5)
                    continue
                else:
                    print(f"  -> API Gateway Error: {e}")
                    break

        if response_text:
            try:
                report_filename = f"audit_{clean_name.replace('.py', '')}.json"
                destination = os.path.join(reports_dir, report_filename)
                
                json_data = json.loads(response_text)
                with open(destination, "w", encoding="utf-8") as report_file:
                    json.dump(json_data, report_file, indent=4)
                
                score = json_data.get("health_score", 0)
                status_flag = "PASS" if score >= 75 else "REVIEW"
                
                print(f"  -> Exported structured JSON to {destination}")
                dashboard_summary.append({"file": clean_name, "score": score, "status": status_flag})
                
            except Exception as json_err:
                print(f"  -> JSON Parsing Error: {json_err}")
                dashboard_summary.append({"file": clean_name, "score": "ERR", "status": "BAD_DATA"})
        else:
            dashboard_summary.append({"file": clean_name, "score": "FAIL", "status": "UNAVAILABLE"})
            
        if idx < len(found_files):
            print("  -> Cooling down API gateway to ensure clean baseline limits...")
            time.sleep(10)

    # === PRESENTATION LAYER ===
    print("\n" + "="*68)
    print("                       FINAL ENGINE METRICS                         ")
    print("="*68)
    print(f" {'FILE NAME':<30} | {'HEALTH SCORE':<12} | {'STATUS':<10}")
    print("-"*68)
    
    for row in dashboard_summary:
        score_str = f"[{row['score']} / 100]" if isinstance(row['score'], int) else row['score']
        status_icon = "🟢 PASS" if row['status'] == "PASS" else "🟡 REVIEW" if row['status'] == "REVIEW" else "🔴 FAILED"
        print(f" {row['file']:<30} | {score_str:<12} | {status_icon:<10}")
        
    print("-"*68)
    print(f"[COMPLETE] Artifact generation cycle finished. Target directory analyzed.")
    print("="*68 + "\n")

if __name__ == "__main__":
    run_automated_audit()