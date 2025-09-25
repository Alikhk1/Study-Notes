
- **Statistics** : Practice & Study of Collecting and analyzing Data.
	- Types :
		1. Descriptive : Summarzing.
		2. Inferential : Collect Sample, apply results to population that sample represents.

--- 

#  Measures of Center :

- Average, Most common, Typical Value.

1. Mean : Average.
2. Median : Middle Value. (When data is not symmetrical it's best to use median to describe the typical value)
3. Mode : Most Frequent Value.

---

#  Measures of Spread :

- How far apart the data points are. Variety of Data.

1. Range = Max - Min
2. Variance : Average of distances from the mean. V = (Data - Mean / No. of Obs). (Sometimes the squared Distance)
3. Standard Deviation = Squareroot of Variance. (Because variance was in squared units). Square Root of average of squared distances from the mean.
4. Quartiles : Splitting Data into 4 Equal parts. Each Quartile (e.g 25%) represent of less than or equal to that number.
5. Inter Quartile Range (IQR) = 3rd Quartile - 1st Quartile (Less affected by extreme values)

---

#  Probability :

- P(Event) = Ways it can Happen / Total# Possible Outcome

- Two events are independent if the probability of the second event does not change based on the outcome of the first event.

- **CONDITIONAL PROBABILITY** : P(A|B) = P(A Intersect B) / P(B)
 
- **PROBABILITY DISTRIBUTION** : Probability of each possible outcome in a scenario. Used in Hypothesis testing (Probability results occured by chance)

- **LAW OF LARGE NUMBERS** : 
	- As Number of trials (or observations) increases, the sample mean gets closer to the true population mean.
	- Doesn't have to be a normal distribution, just reach the mean.

- **DISCRETE DISTRIBUTION** : 
	- Probability distribution of a discrete random variable—one that can take countable, separate values.
	- Discrete Uniform Distribution : When all outcomes have the same probability.

- **CONTINUOUS DISTRIBUTION**
	- Bimodal

	- Nominal - Normal, Bell Shape.

	- **Binomial Distribution*** : Probability distribution of the number of Successes in a sequence of Independent Events.
		- E.g : Probability of getting heads in a sequence of coin flips.
		- It can be used for independent events producing binary outcomes.
		- n : Total number of events being performed.
		- p : Probability of Success.
		- Expected Value = n * p 
		
	- **Normal Distribution** : 
		- Symmetrical, Looks like a bell curve.
		- Area beneath the curve 1. 
		- Probability never hits 0.
		- It's described by it's Mean and STD.
		- 68% of the area is within 1 STD of the mean. 95% of area is within 2 STD of the mean. 99.7% of area within 3 STD.
		- Lots of real world data resembles a normal distribution.
		- Normal distribution is required for statistical test.

- **INTERPRETING THE DISTRIBUTION** :

	- **Skewness** : Statistical measure that indicates the asymmetry of a probability distribution
		- It tracks the tail of the distribution.
		- Tail at right is positively skewed & Tail at left is negatively skewed.
		- Postive: Household income.
	
	- **Kurtosis** : Statistical measure that describes the shape of a probability distribution, specifically its peakedness and tailedness
		- The way of describing extreme values in a distribution.
		- Types :
			1. Positive / Leptokurtic : Large peak around the mean and smaller STD.
			2. Normal / Mesokurtic : Normal Distribution.
			3. PlatyKurtic : Lower peak, larger STD.

- **POISSON DISTRIBUTION**
	- It's the possibility of some # of events occuring over a fixed period of time or domain (space, length, area)
		- E.g : Probability of atleast 5 animals being adopted, 12 people arriving at a restaurant per hour.

	- Poisson process : Average number of events in a period is known but the time/space b/w events is random
		- E.g : Number of animals adopted from a shelter, People visitng a restaurant/Website per hour.

	- Lambda λ: Represents average number of events per time interval.
	
--- 

#  Central Limit Theorum :

- States that the sampling distribution of the sample mean approaches a normal distribution as the sample size n increases, regardless of the population’s original distribution, provided the variance is finite.
- Sample size atleast = 30.

---
#  Hypothesis Testing :

- Theories, Methods & Techniques to compare populations.

- **STEPS :**
	1. Chose target populations.
	2. Assume no difference - Null Hypothesis.
	3. Alternative Hypothesis - Suggest a difference exists, Can define what that difference maybe because of.
		- Independent Variable (X-Axis), Dependent Variable (Y-Axis)
	4. Collect sample data.
		- Look at peer-reviewed research on similar hypothesis tests to determine sample size.
	5. Perform statistical tests.
	6. Draw conclusions.


- **EXPERIMENTS :**
	- Treatment Group 
	- Control Group - Does not change
	- Blinding, participant doesn't know which group they're in.
	- Double Blind - even the person running the study doesn't know treatment is real or placebo.


- **CORRELATION :** Measure relationships
	- Pearson correlation coefficient.
		- +1/-1
		- Magnitude represents relationship
		- Sign represents direction.
			- Positive :  As x increases y increases
			- Negative : As x increase y decreases

	- Confounding variable : Not measured, but may affect the relationship between our varaibles.


- **INTERPRETING RESULTS :**
	
	- p-value : probability of achieving the result atleast as extreme as the one we have observed.

	- Significance Level α : Probability of making an error.
		- If p > α : failed to reject null hypothesis.
		- If p <= α : Reject null hypothesis (Results are statistically Significant)
		- Typical Value is 0.05

	- Type I/II Errors:
		1. Type I : Null Hypothesis is true but we rejected it (Results wrong)
		2. Type II: Null Hypothesis was false but we accepted it (Results Correct)




















