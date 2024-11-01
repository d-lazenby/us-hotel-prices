# Junior Data Analyst at Search Intelligence - take-home task

### 1. The below table shows search volume for Passport applications by State - how would you analyse the data to determine which State passport applications are most popular in?

1. Data Preparation and Initial Review

- I'd initially sort and filter the table by search volume to quickly identify the highest search volumes, which probably indicates those with the most interest in passport applications.  
- I'd then check the top and bottom states, and calculate basic descriptive statistics (e.g. mean, standard deviation) to check average variability across states.  
- Plot a barchart of this.

2. Relative Popularity

- The next step would be to calculate each state's search volume as a percentage of total search volume across all states to indicate the relative interest and those that are substantially above/below the average. These could be ranked based on the percentages. 
- Boxplots would be helpful here.

Finally, I'd look up state population data and normalize the search volume data by population to understand interest relative to number of residents. 
	
### 2. Estimate the median age of people who live in Oxford? - provide reasoning/sources

I downloaded data from the 2021 Census from ons.gov.uk. From the download page:
    *This dataset provides 2021 Census estimates that classify all usual residents 
    in England and Wales by age. The estimates are as at census day, 21 March 2021.*

The analysis itself can be found in `notebooks/oxford_analysis.ipynb`.

### 3. If a car travels to point A at 60mph and returns from point A to it's original position at 20mph, what is the average speed of the car?

The car is travelling at two steady speeds for two equal distances, so the average speed is a simple average: (60 + 20) / 2 = 40 mph. 

### 4. Use Booking.com or similar source to scrape US hotel prices to determine and rank which US States have the cheapest winter hotels.

The code for scraping the data is in `src/main.py`. Assumptions:

- Prices don't vary from Monday to Thursday or from Friday to Saturday. As such, for speed, only Wednesdays and Saturdays were scraped. 
- Winter in the US covers December, January and February, so these were the months scraped. 

The data was saved as CSVs and then concatenated into a single dataframe for analysis; you can find this in `notebooks/hotel_analysis.ipynb`.

On average, the cheapest hotels over Winter can be found in Tennessee, Arkansas, Texas, Nebraska and Kansas.