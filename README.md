# English Premier League

**English Premier League Project**: generates a wealth of information, from final scores to player performance metrics, creating a treasure trove for analysts, enthusiasts, and data scientists alike.
This dataset comes from a data-cleaning and transformation project, where raw, unstructured match data is turned into an organized, analysis-ready format. With it, you can uncover season-long trends, build predictive models for match outcomes, or craft rich visualizations. Whether you’re a seasoned analyst or just starting out in data science, this dataset offers a solid foundation for exploring the EPL through a data-driven lens.

---

## ⚽ Dataset Content

This project uses two cleaned datasets:

- `epl_cleaned.csv`: Contains structured data covering player attributes, match performance, and team-specific metrics.
- `epl_final.csv`: Aggregated and transformed version optimized for dashboard presentation and advanced visualizations.

---

## 📊 Business Requirements

- Enable strategic insights into player and team performance.
- Build interactive visualizations for scouting, fan engagement, or fantasy football strategy.
- Provide accessible analytics for both technical and non-technical users via an intuitive dashboard.

---
EPL
│
├── data/
│   ├── epl_cleaned.csv         # Preprocessed dataset
│   ├── epl_final.csv           # raw dataset
├── notebooks/
│   ├── Epl_analysis.ipynb       # Jupyter notebook with full workflow
│   ├── epl_visualisation.ipynb  # Additional analytics and visuals
│
├── ├── streamlit_app.py        # Streamlit dashboard
│
├── README.md                   # Project documentation
└── requirements.txt            # Python dependencies

---

## 🧪 Hypotheses and Validation

## **Hypotheses and Validation**

- **Hypothesis 1: Home teams have a scoring and winning advantage.**  
- *Validation:* The bar chart comparing total home vs away goals shows that home teams score significantly more goals. The match result distribution pie chart confirms a higher proportion of home wins, supporting the home advantage theory.

- **Hypothesis 2: Most matches have a moderate number of goals (2-3 goals).**  
*Validation:* The histogram of total goals per match reveals a peak around 2 to 3 goals per game, consistent with typical football scoring patterns.

- **Hypothesis 3: Goal-scoring rates vary across the season.**  
*Validation:* The monthly average goals line plot shows fluctuations, including a dip in winter months, confirming seasonal effects on scoring.

- **Hypothesis 4: Top scoring teams dominate both home and away matches.**  
*Validation:* The top 10 scoring teams bar chart aggregates goals from both home and away fixtures, identifying consistent high scorers.

- **Hypothesis 5: Teams have distinct tactical profiles based on scoring patterns.**  
*Validation:* The clustering analysis groups teams into high-scoring, defensive, and balanced clusters, confirming varied playing styles.

- **Hypothesis 6: Expected goals (xG) correlate closely with actual goals scored.**  
*Validation:* The scatter plot comparing synthetic xG and actual goals demonstrates a positive correlation, though some teams deviate, indicating over- or under-performance.

- **Hypothesis 7: Teams accumulate points steadily over a season with momentum fluctuations.**  
*Validation:* The cumulative points timeline for selected teams shows periods of rapid point accumulation and plateaus, reflecting form swings.

---

This structured approach helps confirm meaningful patterns while highlighting areas needing deeper analysis or data refinement.

---

## 📍 Project Plan

- **Data Flow**: Collection → Cleaning → Transformation → Analysis → Dashboard Design.
- **Management**: Modular Python scripts and reproducible workflows.
- **Methodologies**: Chosen for statistical rigor, clarity, and stakeholder relevance.

---
📌 Project Board (Trello)
- A Trello project board was used for task management and includes:
- Data preparation tasks.
- Model building steps.
- Visual insights creation.
- Final deployment plan.
---

## 📐 Mapping Business Requirements to Visualizations

| Business Requirement | Visualization           | Rationale                                        |
|----------------------|--------------------------|--------------------------------------------------|
| Team effectiveness   | Radar charts, bar plots  | Highlight multidimensional performance metrics   |
| Team progression     | Line graphs, heatmaps    | Show seasonal trends and match flow              |
| Tactical insights    | Pie charts, stacked bars | Simplify complex tactical analysis               |

---

## 🧠 Analysis Techniques

- **Descriptive Statistics** – Summarize key metrics like goals, assists, and tackles.
- **Trend Analysis** – Monitor progression over matchweeks and seasons.
- **Regression Modeling** – Validate predictive hypotheses.
- **Clustering** – Group similar team profiles or team styles.

**Limitations & Workarounds**:
- Handled missing data via imputation.
- Used dictionary renaming to resolve column inconsistencies.
- Modular design enhanced maintainability and interpretability.

**AI Contributions**:
- Assisted with exploratory ideation and code optimization.
- Streamlined visualization designs with feedback from generative prompts.
- Provide structured documentation and markdown formatting.
- Assisted descriptive insights for analysis results.

---

## ⚖️ Ethical Considerations

- No personal or sensitive data used; all sources are public domain.
- Bias avoided through full-season data coverage and inclusive metric tracking.
- Visualizations designed for fairness and clarity across clubs and roles.

---

## 🧩 Dashboard Design

### Features:
- ## 🖥️ Streamlit Integration

The dashboard is built using Streamlit for rapid deployment and interactivity.

### Key Streamlit Features:
- `st.slider` for dynamic player comparisons
- `st.selectbox` for filtering by club or season
- `st.plotly_chart` for interactive visuals

**User Experience Enhancements**:
- Responsive layout for desktop and mobile
- Tooltip integration for stat explanations
- Interactive filters (season, club role)
- Sliders for team comparisons
- Insight pop-ups and performance cards

### Communication Strategy:
- Technical Users: Raw metrics, regression plots
- Non-Technical Users: Intuitive visuals and high-level summaries

---

## 🐞 Unfixed Bugs

- Streamlit refresh lag with large datasets
- Real-time match sync not implemented due to API access limitations
- Tooltip logic refined after feedback but requires further optimization

**Knowledge Gaps**:
- Advanced dynamic plotting—currently under exploration
- Feedback from mentors helped clarify UX layout decisions

---

## 🔧 Development Roadmap

**Challenges**:
- Column inconsistency across CSVs
- Complex tactical plotting

**Solutions**:
- Python dictionary renaming
- Plot modularization across multiple scripts

**Next Steps**:
- Implement ML ranking models
- Add match simulation tools and forecasting

---

## 🚀 Deployment
- Streamlit
- https://english-premier-league-capstone-project-4ymqtsk9qy2cgywumaua9f.streamlit.app/
- To access the streamlit app click on the above link - click on settings(3 dots) - on the python version dropdown select version 3.12 to run the app

---

## 🧰 Main Data Analysis Libraries

| Library         | Purpose                          |
|----------------|----------------------------------|
| `pandas`       | Data cleaning and manipulation   |
| `numpy`        | Numerical operations              |
| `matplotlib`   | Basic static plots                |
| `seaborn`      | Enhanced statistical visuals      |
| `plotly`       | Interactive graphs                |
| `scikit-learn` | Predictive modeling and ML        |
| `streamlit`    | Dashboard deployment and UI       |

---

## 📝 Credits

### Content
- Dataset sourced from the kaggle site - https://www.kaggle.com/datasets/marcohuiii/english-premier-league-epl-match-data-2000-2025/data
- Tactical framework inspired by The Coaches' Voice.
- Radar chart formatting adapted from [Python Graph Gallery](https://www.python-graph-gallery.com).
- Regex solutions sourced from Stack Overflow contributors.

### Media

- Player silhouette icons from Flaticon.
- Club logos from official Premier League media kit.

---

## 🙌 Acknowledgements

Thanks to peers and mentors for providing actionable feedback, especially around dashboard features and regression logic. Appreciation also goes to the football analytics and Python communities for their resources and engagement.