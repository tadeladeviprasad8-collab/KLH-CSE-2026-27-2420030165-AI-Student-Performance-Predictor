# AI Ethics and Fairness

This document discusses the ethical considerations of using Machine Learning for predicting academic performance.

## Bias in Machine Learning
Machine Learning models learn from historical data. If the historical data contains biases, the model will learn and perpetuate those biases.

### Types of Bias
1. **Dataset Bias**: Occurs when the data used to train the model does not accurately represent the real-world population. 
2. **Representation Bias**: Occurs when certain groups are underrepresented in the dataset, leading the model to perform poorly for those groups.

## Fairness and the GradeMind Project
**Important Disclaimer**: The GradeMind model is **not guaranteed to be perfectly fair**. 

Because this project uses **synthetic data**, any conclusions about the fairness of the model across different demographic groups cannot be drawn. The synthetic data generation script (`generate_dataset.py`) uses a simplified mathematical formula to assign grades based strictly on academic metrics (attendance, marks, etc.). It does not include demographic features (e.g., gender, race, socioeconomic status).

While excluding demographic features prevents the model from explicitly discriminating based on those features, it does not solve underlying systemic biases. For example, if a certain group systematically has lower attendance due to external socioeconomic factors, the model will still score them lower, reflecting the systemic bias present in the real world (even though our data is synthetic, this is how it would work with real data).

## Responsible AI Practices
- **Transparency**: The model's inputs (attendance, marks, GPA, etc.) are clearly stated to the user on the prediction page.
- **Privacy**: Only necessary academic metrics are collected. No personally identifiable information (PII) is used in the prediction process.
- **Human in the Loop**: GradeMind is designed as a *decision support tool* for educators, not a fully automated decision-maker. Predictions should be used to guide interventions and support, not to automatically penalize students.
