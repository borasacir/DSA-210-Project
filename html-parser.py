from bs4 import BeautifulSoup
import pandas as pd

# Load the HTML file
html_file = "history/watch-history.html"

with open(html_file, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# Extract data
watch_data = []
content_cells = soup.find_all("div", class_="content-cell")

for cell in content_cells:
    title_tag = cell.find("a")
    time_tag = cell.find("time")

    if title_tag and time_tag:
        title = title_tag.text
        url = title_tag["href"]
        timestamp = time_tag["datetime"]  # ISO 8601 format
        watch_data.append({"Title": title, "URL": url, "Timestamp": timestamp})

# Convert to DataFrame
df = pd.DataFrame(watch_data)

# Save to CSV
df["Timestamp"] = pd.to_datetime(df["Timestamp"])  # Convert timestamps to datetime
df.to_csv("youtube_watch_history.csv", index=False)
print("Watch history saved to 'youtube_watch_history.csv'")
