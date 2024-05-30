# Overview
Complete this 'readme.md' file when you answer the questions in Part 3 of the [Handout](https://courses.cs.washington.edu/courses/cse163/21wi/hw3/spec.html). There is no `hw3-written.txt` file (mentioned in the online directions).   

Be sure to add your answers inside a ```code block``` to make it easy for me to find your answers.

For help on using Markdown, see [Markdown](https://gist.github.com/cuonggt/9b7d08a597b167299f0d)

## Instructions
Review the source of the dataset [here](https://nces.ed.gov/programs/digest/d18/tables/dt18_104.20.asp). For the following reflection questions consider the accuracy of data collected, and how it's used as a public dataset (e.g. presentation of data, publishing in media, etc.). All of your answers should be complete sentences and show thoughtful responses. "No" or "I don't know" or any response like that are not valid responses for any questions. There is not one particularly right answer to these questions, instead, we are looking to see you use your critical thinking and justify your answers!

### #1: Plotting questions
1. Do you think the bar chart from part 1b is an effective data visualization? Explain in 1-2 sentences why or why not.
```
Yes, using a bar chart to plot the percentage of students by sex is an effective data visualization. This is because we're only looking at a single year, not a series of years, so a bar chart makes is very easy to compare the value/height for each column. Other data visualations like a scatter plot or line plot wouldn't be effective because of the limited scope of time we're looking at.
```
2. Why did you choose the type of plot that you did in part 1c? Explain in a few sentences why you chose this type of plot.
```
I chose to use a line plot because line plot are effective at analyzing data over an extended period of time and comparing trends. Looking at the graph, I can easily see how the percentage of hispanic people earning high school diplomas and bachelor's degrees has been increasing over the past 20 years. The line chart also has several benefits over other alternatives like a bar chart or scatter plot, as it has a continuous line that isn't interupted by other data like a bar chart might have, and the line shown is directly based on the data rather than an approximated trend line like what would be seen in a scatter plot.
```

### #2: Datasets
Datasets can be biased. (i.e. The data can be WRONG!)
Bias in data means it might be skewed away from or portray a wrong picture of reality. 
The data might contain inaccuracies or the methods used to collect the data may have 
been flawed. Describe a possible bias present in this dataset and why it might have 
occurred. Your answer should be about 2 or 3 sentences long. Again, describe how
the data is incorrect. (Note: incomplete is not necessarily the same as incorrect.)
```
Depending on how the data was gathered, it could have inherent biases due to underrepresentation of certain groups due to historical methods of data gathering as well as where the data was gathered from. If certain groups were polled from less affluent areas, their percentage of bachelors/high school diploma earners could be significantly less than other groups who may have been polled in more affluent areas. Additionally, due to historical underrepresentation of certain groups, particularly prior to 1980, the amount of progress shown is restricted to a shorter time frame, and may also show the inherent reasons certain groups are significantly lower than others, as if the data sets weren't willing to track them, there's a high likelihood they weren't given the same educational opprotunities historically as other groups.
```
### #3: Context
Later in the class we will talk about ethics in data science. Question #3 here is 
supposed to be a warm-up to get you thinking about our responsibilities when processing
data, to get you to think about both the intended and unintended consequences of
actions driven by data. 

Good intentions don’t insure good outcomes. Many people have good intentions yet cause very real 
harm in the world. We’ll discuss specific examples of well-intentioned algorithms 
perpetuating more harm later. In computing, that harm is magnified, 
automated, and reproduced by computers.

Describe a **policy** or **decision** motivated by this dataset with the 
intended goal of improving educational equity but which ultimately exacerbates 
the problem or causes a new one. How can the policy (or decision) lead to further 
injustice even when designed with equity in mind? In other words, we are trying 
to think of a way that we could use this data with good intentions, but actually 
would end up causing harm. 
```
This data set may have been used to dictate policy such as allocating funding to certain schools or areas with lower rates of graduation or college success. This may not solve the intended issue, as it ignores other socioeconomic or systematic factors that are causing a lower graduation, and after seeing that increased funding didn't solve the issue significantly, the funding could be reduced back to original levels, causing no positive change to be made, and leaving those at those schools even worse off than previously, exacerbating educational struggles further. 
```
