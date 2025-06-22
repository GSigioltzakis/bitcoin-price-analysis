import subprocess
subprocess.run(["python", "scripts/fetch_price_data.py"])
subprocess.run(["python", "scripts/process_data.py"])