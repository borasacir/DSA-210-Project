# YouTube Viewing History Analysis: Trends and Keyword Exploration

## Project Overview
This project aims to analyze my YouTube viewing history to uncover personal trends and patterns in video consumption. By leveraging exported YouTube data, we explore viewing activity over time, identify the most-watched channels, and perform a detailed analysis of frequently occurring keywords in video titles. Additionally, we include machine learning techniques to predict daily video consumption and group videos into clusters based on their themes.

## Objectives
### Primary Objectives
1. Explore patterns in YouTube viewing activity over time (daily, hourly, and monthly trends).
2. Identify the most-watched channels and their contribution to total viewing time.

### Secondary Objectives
1. Analyze frequently occurring keywords in video titles.
2. Visualize trends for specific keywords over time.
3. Implement machine learning models to predict daily video counts and group videos into clusters.
4. Examine keyword distributions across channels.

## Data Collection
The project uses personal YouTube viewing history data exported via **Google Takeout** in JSON format. Key fields extracted include:
- Video titles
- Channel names
- Timestamps of views

## Methodology
1. **Data Cleaning and Preprocessing**:
   - Convert timestamps into a readable format (Date, Day of Week, and Hour).
   - Remove null entries and standardize channel names.
   - Extract keywords from video titles after filtering out common stop words.

2. **Exploratory Data Analysis (EDA)**:
   - Analyze trends in viewing activity across time (daily, weekly, hourly).
   - Identify top channels and visualize their contribution to viewing time.
   - Generate word clouds for frequently occurring keywords.

3. **Machine Learning**:
   - **Daily Video Count Prediction**: Use `DecisionTreeRegressor` to predict daily video counts based on the day of the week and historical data.
   - **Video Clustering**: Apply `KMeans` clustering to group videos into thematic categories using TF-IDF features extracted from video titles.

4. **Visualization**:
   - Create line plots, bar charts, and heatmaps to visualize trends.
   - Highlight top keywords and their trends over time.

## Tools and Libraries
- **Programming Language**: Python
- **Libraries**:
  - **Data Processing**: Pandas, NumPy
  - **Visualization**: Matplotlib, Seaborn, WordCloud
  - **Machine Learning**: Scikit-learn
- **Other Tools**:
  - GitHub for project hosting and collaboration.

## Machine Learning Component
### Daily Video Count Prediction
- **Model**: Decision Tree Regressor
- **Features**: Day of the week (one-hot encoded), previous trends.
- **Outcome**: Predict daily video consumption trends.

### Video Clustering
- **Model**: K-Means Clustering
- **Features**: TF-IDF matrix from video titles.
- **Outcome**: Group videos into clusters based on thematic similarity.

## Expected Outcomes
1. Visualizations of viewing trends over time (daily, monthly, and hourly).
2. Identification of the most-watched channels and patterns.
3. Insights into frequently occurring keywords and their trends.
4. Machine learning-based predictions of daily video counts.
5. Thematic clustering of videos into distinct groups.

## Challenges and Limitations
1. **Data Quality**: Inconsistencies in YouTube exports, such as missing channel names or incomplete timestamps.
2. **Machine Learning**: Predictive accuracy may be limited by the dataset's size and variability.
3. **Keyword Analysis**: Potential difficulty in removing irrelevant stop words.

## Future Enhancements
1. Develop a recommendation system for new channels based on viewing habits.
2. Scrape additional metadata (e.g., video durations, categories) for deeper analysis.
3. Deploy the project as an interactive dashboard using Streamlit or Dash.

## Deliverables
1. **GitHub Repository**: Includes all analysis scripts, visualizations, and documentation.
2. **Plots and Visualizations**:
   - Heatmaps, bar charts, line plots, and word clouds.
3. **Final Report**: A comprehensive LaTeX-based report summarizing findings and methodologies.
4. **README.md**: This file documents the project structure and purpose.

## Installation and Usage
1. Clone the GitHub repository:
   ```bash
   git clone https://github.com/your-username/youtube-analysis-project.git
