# English Premier League

**English Premier League** is a comprehensive data analysis tool designed to streamline data exploration, analysis, and visualization. The tool supports CSV-based structured data and is ideal for analysts and enthusiasts seeking insights into player performance, match stats, and seasonal trends.

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

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

## 🧪 Hypotheses and Validation

1. **Teams with higher pressing metrics concede fewer goals.**  
   _Validation_: Correlation analysis and regression modeling.

2. **Players with high pass completion and chances created drive team wins.**  
   _Validation_: Aggregated player contributions vs. match outcomes.

3. **Early-season transfers yield higher ROI than winter signings.**  
   _Validation_: Compare pre- and post-transfer performance metrics.

---

## 📍 Project Plan

- **Data Flow**: Collection → Cleaning → Transformation → Analysis → Dashboard Design.
- **Management**: Modular Python scripts and reproducible workflows.
- **Methodologies**: Chosen for statistical rigor, clarity, and stakeholder relevance.

---

## 📐 Mapping Business Requirements to Visualizations

| Business Requirement | Visualization           | Rationale                                        |
|----------------------|--------------------------|--------------------------------------------------|
| Player effectiveness | Radar charts, bar plots  | Highlight multidimensional performance metrics   |
| Team progression     | Line graphs, heatmaps    | Show seasonal trends and match flow              |
| Tactical insights    | Pie charts, stacked bars | Simplify complex tactical analysis               |

---

## 🧠 Analysis Techniques

- **Descriptive Statistics** – Summarize key metrics like goals, assists, and tackles.
- **Trend Analysis** – Monitor progression over matchweeks and seasons.
- **Regression Modeling** – Validate predictive hypotheses.
- **Clustering** – Group similar player profiles or team styles.

**Limitations & Workarounds**:
- Handled missing data via imputation.
- Used dictionary renaming to resolve column inconsistencies.
- Modular design enhanced maintainability and interpretability.

**AI Contributions**:
- Assisted with exploratory ideation and code optimization.
- Streamlined visualization designs with feedback from generative prompts.

---

## ⚖️ Ethical Considerations

- No personal or sensitive data used; all sources are public domain.
- Bias avoided through full-season data coverage and inclusive metric tracking.
- Visualizations designed for fairness and clarity across clubs and roles.

---

## 🧩 Dashboard Design

### Features:
- Interactive filters (season, club, player role)
- Sliders for player comparisons
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

### Heroku

Live App: [https://YOUR_APP_NAME.herokuapp.com/](https://YOUR_APP_NAME.herokuapp.com/)

Deployment Steps:
1. Log into Heroku and create an App.
2. Link GitHub repository via Deploy tab.
3. Select repository branch and deploy.
4. Add `.slugignore` to exclude unused files.
5. Ensure Python version compatibility via `runtime.txt`.

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

- Tactical framework inspired by The Coaches' Voice.
- Radar chart formatting adapted from [Python Graph Gallery](https://www.python-graph-gallery.com).
- Regex solutions sourced from Stack Overflow contributors.

### Media

- Player silhouette icons from Flaticon.
- Club logos from official Premier League media kit.

---

## 🙌 Acknowledgements

Thanks to peers and mentors for providing actionable feedback, especially around dashboard features and regression logic. Appreciation also goes to the football analytics and Python communities for their resources and engagement.