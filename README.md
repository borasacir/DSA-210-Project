# YouTube Viewing History Analysis

## Overview

This project analyzes personal YouTube viewing history to uncover trends and patterns in video consumption. By examining viewing activity over time and identifying frequently watched channels and keywords, the analysis provides insights into personal viewing habits.

## Data Collection

The data was obtained by exporting personal YouTube viewing history using [Google Takeout](https://takeout.google.com/). The exported data includes details such as video titles, channel names, and timestamps of views.

## Methodology

1. **Data Preprocessing**:
   - Converted timestamps to readable formats (e.g., date, day of the week, hour).
   - Handled missing values and standardized channel names.
   - Extracted keywords from video titles, filtering out common stop words.

2. **Exploratory Data Analysis (EDA)**:
   - Analyzed viewing activity trends over different time periods (daily, weekly, hourly).
   - Identified top channels and their contribution to total viewing time.
   - Generated visualizations such as word clouds for frequently occurring keywords.

3. **Machine Learning**:
   - **Daily Video Count Prediction**: Utilized a Decision Tree Regressor to predict daily video counts based on features like the day of the week and historical data.
   - **Video Clustering**: Applied K-Means clustering to group videos into thematic categories using TF-IDF features extracted from video titles.

4. **Visualization**:
   - Created line plots, bar charts, and heatmaps to visualize trends.
   - Highlighted top keywords and their trends over time.

## Results

- **Viewing Trends**: Identified peak viewing times and days with the highest activity.
- **Top Channels**: Determined the most-watched channels and their respective viewing times.
- **Keyword Analysis**: Highlighted frequently occurring keywords in video titles and their temporal trends.
- **Machine Learning Outcomes**:
  - Achieved a certain level of accuracy in predicting daily video counts.
  - Successfully clustered videos into distinct thematic groups.

## Conclusion

The analysis provides a comprehensive overview of personal YouTube viewing habits, offering insights into viewing patterns and preferences. The machine learning components further enhance the understanding by predicting future behavior and categorizing content.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
