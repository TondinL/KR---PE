import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

# local path
file_path = "put file path"


if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
    exit()

df = pd.read_excel(file_path)

def split_keywords(kw_string):
    if pd.isnull(kw_string):
        return []
    if isinstance(kw_string, str):
        keywords = [kw.strip().lower() for kw in kw_string.split(',') if kw.strip()]
        return keywords
    return []

df_filtered = df.copy()

if 'keyword' in df_filtered.columns:
    df_filtered['keyword'] = df_filtered['keyword'].apply(split_keywords)
else:
    print("'Keyword' column not found in file.")
    exit()

all_keywords = df_filtered['keyword'].explode().dropna().tolist()
keywords_text = ' '.join(all_keywords)

wordcloud = WordCloud(width=800, height=400, background_color='black', colormap='viridis').generate(keywords_text)

output_filename = "wordcloud.png"
wordcloud.to_file(output_filename)
print(f"Word cloud salvata in: {output_filename}")

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
