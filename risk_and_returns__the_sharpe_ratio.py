# -*- coding: utf-8 -*-
"""Risk and Returns_ The Sharpe Ratio.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FeI26vH7V71BGKY1jyVaq7Eatj2hP8Hw
"""

#from google.colab import files 
#up=files.upload()

"""##
<p>An investment may make sense if we expect it to return more money than it costs. But returns are only part of the story because they are risky - there may be a range of possible outcomes. How does one compare different investments that may deliver similar results on average, but exhibit different levels of risks?</p>
<p><img style="float: left ; margin: 5px 20px 5px 1px;" width="200" src="https://assets.datacamp.com/production/project_66/img/sharpe.jpeg"></p>
<p>William Sharpe. He introduced the <a href="https://web.stanford.edu/~wfsharpe/art/sr/sr.htm"><em>reward-to-variability ratio</em></a> in 1966 that soon came to be called the Sharpe Ratio. It compares the expected returns for two investment opportunities and calculates the additional return per unit of risk an investor could obtain by choosing one over the other. In particular, it looks at the difference in returns for two investments and compares the average difference to the standard deviation (as a measure of risk) of this difference. A higher Sharpe ratio means that the reward will be higher for a given amount of risk. It is common to compare a specific opportunity against a benchmark that represents an entire category of investments.</p>
<p>The Sharpe ratio has been one of the most popular risk/return measures in finance, not least because it's so simple to use. It also helped that Professor Sharpe won a Nobel Memorial Prize in Economics in 1990 for his work on the capital asset pricing model (CAPM).</p>
<p>The Sharpe ratio is usually calculated for a portfolio and uses the risk-free interest rate as benchmark. We will simplify our example and use stocks instead of a portfolio. We will also use a stock index as benchmark rather than the risk-free interest rate because both are readily available at daily frequencies and we do not have to get into converting interest rates from annual to daily frequency. Just keep in mind that you would run the same calculation with portfolio returns and your risk-free rate of choice, e.g, the <a href="https://fred.stlouisfed.org/series/TB3MS">3-month Treasury Bill Rate</a>. </p>
<p>So let's learn about the Sharpe ratio by calculating it for the stocks of the two tech giants Facebook and Amazon. As benchmark we'll use the S&amp;P 500 that measures the performance of the 500 largest stocks in the US. When we use a stock index instead of the risk-free rate, the result is called the Information Ratio and is used to benchmark the return on active portfolio management because it tells you how much more return for a given unit of risk your portfolio manager earned relative to just putting your money into a low-cost index fund.</p>
"""

# Commented out IPython magic to ensure Python compatibility.
# Importing required modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
os.chdir(r"F:\schomee\Datasets\Risk and Returns_ The Sharpe Ratio Solution\Risk and Returns_ The Sharpe Ratio\datasets")

# Settings to produce nice plots in a Jupyter notebook
plt.style.use('fivethirtyeight')
# %matplotlib inline

# Reading in the data
stock_data = pd.read_csv("stock_data",parse_dates=['Date'],index_col='Dates').dropna()
benchmark_data = pd.read_csv("benchmark_data",parse_dates=['Dates'],index_col='Dates').dropna()

"""## 2. A first glance at the data
<p>Let's take a look the data to find out how many observations and variables we have at our disposal.</p>
"""

# Display summary for stock_data
print('Stocks\n')
# ... YOUR CODE FOR TASK 2 HERE ...
print(stock_data.info())
print(stock_data.head())

# Display summary for benchmark_data
print('\nBenchmarks\n')
# ... YOUR CODE FOR TASK 2 HERE ...
print(benchmark.info())
print(benchmark.head())


"""## 3. Plot & summarize daily prices for Amazon and Facebook
<p>Before we compare an investment in either Facebook or Amazon with the index of the 500 largest companies in the US, let's visualize the data, so we better understand what we're dealing with.</p>
"""

# visualize the stock_data
# ... YOUR CODE FOR TASK 3 HERE ...


# summarize the stock_data
# ... YOUR CODE FOR TASK 3 HERE ...

"""## 4. Visualize & summarize daily values for the S&P 500
<p>Let's also take a closer look at the value of the S&amp;P 500, our benchmark.</p>
"""

# plot the benchmark_data
# ... YOUR CODE FOR TASK 4 HERE ...


# summarize the benchmark_data
# ... YOUR CODE FOR TASK 4 HERE ...

"""## 5. The inputs for the Sharpe Ratio: Starting with Daily Stock Returns
<p>The Sharpe Ratio uses the difference in returns between the two investment opportunities under consideration.</p>
<p>However, our data show the historical value of each investment, not the return. To calculate the return, we need to calculate the percentage change in value from one day to the next. We'll also take a look at the summary statistics because these will become our inputs as we calculate the Sharpe Ratio. Can you already guess the result?</p>
"""

'''
Pandas dataframe.pct_change() function calculates the percentage change 
between the current and a prior element. This function by
default calculates the percentage change from the immediately previous row.'''
# calculate daily stock_data returns
stock_returns = ...

# plot the daily returns
# ... YOUR CODE FOR TASK 5 HERE ...


# summarize the daily returns
# ... YOUR CODE FOR TASK 5 HERE ...

"""## 6. Daily S&P 500 returns
<p>For the S&amp;P 500, calculating daily returns works just the same way, we just need to make sure we select it as a <code>Series</code> using single brackets <code>[]</code> and not as a <code>DataFrame</code> to facilitate the calculations in the next step.</p>
"""

# calculate daily benchmark_data returns
# ... YOUR CODE FOR TASK 6 HERE ...
sp_returns = ...

# plot the daily returns
# ... YOUR CODE FOR TASK 6 HERE ...


# summarize the daily returns
# ... YOUR CODE FOR TASK 6 HERE ...

"""## 7. Calculating Excess Returns for Amazon and Facebook vs. S&P 500
<p>Next, we need to calculate the relative performance of stocks vs. the S&amp;P 500 benchmark. This is calculated as the difference in returns between <code>stock_returns</code> and <code>sp_returns</code> for each day.</p>
"""

'''
Pandas dataframe.sub() function is used for finding the subtraction of 
dataframe and other, element-wise. This function is essentially same as
doing dataframe - other
but with a support to substitute for missing data in one of the inputs.'''
# calculate the difference in daily returns
excess_returns = ...

# plot the excess_returns
# ... YOUR CODE FOR TASK 7 HERE ...


# summarize the excess_returns
# ... YOUR CODE FOR TASK 7 HERE ...

"""## 8. The Sharpe Ratio, Step 1: The Average Difference in Daily Returns Stocks vs S&P 500
<p>Now we can finally start computing the Sharpe Ratio. First we need to calculate the average of the <code>excess_returns</code>. This tells us how much more or less the investment yields per day compared to the benchmark.</p>
"""

# calculate the mean of excess_returns 
# ... YOUR CODE FOR TASK 8 HERE ...
avg_excess_return = ...

# plot avg_excess_returns
# ... YOUR CODE FOR TASK 8 HERE ...

"""## 9. The Sharpe Ratio, Step 2: Standard Deviation of the Return Difference
<p>It looks like there was quite a bit of a difference between average daily returns for Amazon and Facebook.</p>
<p>Next, we calculate the standard deviation of the <code>excess_returns</code>. This shows us the amount of risk an investment in the stocks implies as compared to an investment in the S&amp;P 500.</p>
"""

# calculate the standard deviations
sd_excess_return = ...

# plot the standard deviations
# ... YOUR CODE FOR TASK 9 HERE ...

"""## 10. Putting it all together
<p>Now we just need to compute the ratio of <code>avg_excess_returns</code> and <code>sd_excess_returns</code>. The result is now finally the <em>Sharpe ratio</em> and indicates how much more (or less) return the investment opportunity under consideration yields per unit of risk.</p>
<p>The Sharpe Ratio is often <em>annualized</em> by multiplying it by the square root of the number of periods. We have used daily data as input, so we'll use the square root of the number of trading days (5 days, 52 weeks, minus a few holidays): √252</p>
"""

'''
Pandas dataframe.div() is used to find the floating division of the dataframe 
and other element-wise. This function is similar to datafram/other,
but with an additional support to handle missing value in one of
the input data.'''
# calculate the daily sharpe ratio
daily_sharpe_ratio = ...

# annualize the sharpe ratio
annual_factor = ...
annual_sharpe_ratio = ...

# plot the annualized sharpe ratio
# ... YOUR CODE FOR TASK 10 HERE ...

"""## 11. Conclusion
<p>Given the two Sharpe ratios, which investment should we go for? In 2016, Amazon had a Sharpe ratio twice as high as Facebook. This means that an investment in Amazon returned twice as much compared to the S&amp;P 500 for each unit of risk an investor would have assumed. In other words, in risk-adjusted terms, the investment in Amazon would have been more attractive.</p>
<p>This difference was mostly driven by differences in return rather than risk between Amazon and Facebook. The risk of choosing Amazon over FB (as measured by the standard deviation) was only slightly higher so that the higher Sharpe ratio for Amazon ends up higher mainly due to the higher average daily returns for Amazon. </p>
<p>When faced with investment alternatives that offer both different returns and risks, the Sharpe Ratio helps to make a decision by adjusting the returns by the differences in risk and allows an investor to compare investment opportunities on equal terms, that is, on an 'apples-to-apples' basis.</p>
"""

# Uncomment your choice.
# buy_amazon = True
# buy_facebook = True
