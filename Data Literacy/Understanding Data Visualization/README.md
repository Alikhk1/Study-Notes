# Data Visualization Guide

## 3 Ways of Getting Insights
1. **Calculating Summary Statistics**: Mean, Median, Standard Deviation
2. **Running Models**: Linear/Logistic Regression
3. **Drawing Plots (Visualization)**: Scatter, Bar, Histogram

## Choosing Plot Types
**Depends on whether your variables are continuous or categorical:**
- Age is continuous, but age groups are categorical
- Time is continuous, but month, year are categorical

---

# Histogram

## When to Use
1. One Continuous Variable
2. Want to know the shape of Distribution

## Key Characteristics
- **Bin-size**: Influences appearance - experiment with several values
- **Modality**: How many peaks are there (first thing to look at)
- **Skewness**: Is it Symmetric?
    - **Left Skewed**: Left side has outliers
    - **Right Skewed**: Right side has outliers
- **Kurtosis**: Shape of Distribution

---

# Box Plot

## When to Use
1. Continuous variable split by a categorical variable
2. Compare distributions of continuous variable for each category
3. Answers questions about the spread of a variable

## Components
- Lower/Upper Quartiles & IQR (Interquartile Range)
- **IQR**: Helps answer variation questions
- **Whiskers**: Anything outside is an extreme value (shown as points)

---

# Scatter Plot

## When to Use
1. Two continuous variables
2. Want to understand relationship between the two variables

## Features
- **Logarithmic Scales**: Makes multiplicative patterns look linear, reveals proportional relationships
- **Correlation**: How well you can draw a straight line through the points

---

# Line Plot

## When to Use
1. Two continuous variables
2. Understand relationship between variables
3. Consecutive observations are connected

## Variations
- Multiple Lines

---

# Bar Plot

## When to Use
1. Categorical variable
2. Display counts/percentages for each category

## Best Practices
- For percentages, stacked bar plots are effective

---

# Dot Plot

## When to Use
1. Categorical variable
2. Display numeric scores for each category on log scale (bar plots have 0, log of 0 is infinity)
3. Display multiple numeric scores for each category

---

# Higher Dimensions Visualization

## Visual Dimensions for Data Points
- Color, Size, Transparency, Shape, Line Type/Shape

## Color Theory
1. **Hue**: Actual Color (for Category)
2. **Chroma**: Intensity (for Sequential scale)
3. **Luminance**: Brightness (for Sequential scale)

---

# Advanced Plot Types
*For plotting many variables at once*

1. **Pair plots**
2. **Correlation Heatmaps**
3. **Parallel Coordinates plots**
