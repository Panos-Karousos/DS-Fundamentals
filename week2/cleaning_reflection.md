# Week 2 - Data Wrangling Workshop
For my Week 2 activity, I used Pandas to clean a dataset with missing values and duplicates.
I first used .info(), .describe() and .isnull().sum() to check the data. I then changed Age to numeric, filled missing ages and incomes with the median and replaced missing text with "Unknown".
One thing I found interesting was that filling in the missing income actually created a duplicate Peter record, which I then removed.
This showed me how one cleaning step can affect another and why it's important to keep checking the data as you go.