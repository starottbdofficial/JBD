import re
import requests

# সোর্স M3U প্লেলিস্ট URL
SOURCE_URL = "https://raw.githubusercontent.com/sm-monirulislam/jago_bd_auto_update_playlist-/refs/heads/main/jago_bd.m3u"
OUTPUT_FILE = "playlist.m3u"

def fetch_and_convert():
    try:
        print("Fetching source playlist...")
        response = requests.get(SOURCE_URL, timeout=15)
        response.raise_for_status()
        
        lines = response.text.splitlines()
        updated_lines = []
        
        for line in lines:
            # যদি লাইনে static.jagobd.com.bd থাকে তবে app24.jagobd.com.bd দিয়ে পরিবর্তন করবে
            if "static.jagobd.com.bd" in line:
                line = line.replace("static.jagobd.com.bd", "app24.jagobd.com.bd")
            
            # লিঙ্ক শেষের ?wmsAuthSign=|referrer=... অংশ বাদ দেওয়া
            if "?wmsAuthSign=" in line:
                line = re.sub(r'\?wmsAuthSign=.*$', '', line)
            
            updated_lines.append(line)
        
        # নতুন কন্টেন্ট playlist.m3u ফাইলে রাইট করা
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write("\n".join(updated_lines) + "\n")
            
        print(f"Successfully converted and saved to {OUTPUT_FILE}")

    except requests.RequestException as e:
        print(f"Error fetching playlist: {e}")

if __name__ == "__main__":
    fetch_and_convert()
  
