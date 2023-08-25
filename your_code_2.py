import pandas as pd
df = pd.read_csv('GoogleApps.csv')

# What is the price of the cheapest paid app (type == 'Paid')?
paid_df= df[df["Type"] == "Paid"]
print(paid_df["Price"].min())

# What is the median number of installs
# for the applications from the "ART_AND_DESIGN" category?
aNd_df = df[df["Category"] == "ART_AND_DESIGN"]
print(aNd_df["Installs"].median())

# How much more is the maximum number of Reviews for free apps (type == 'Free')
# than the maximum number of Reviews for paid apps (Type == 'Paid')?
free = df[df["Type"] == "Free"]["Reviews"].max()
pAid = paid_df["Reviews"].max()
print(free-pAid)


# What is the minimum size of an application for teenagers (Content Rating == 'Teen')?​
teen = df[df["Content Rating"] == "Teen"]["Size"].min()
print(teen)


# *What is the category of an app having the most number of reviews?
most_reviews = df["Reviews"].max()
app_df = df[df["Reviews"] == most_reviews]
print(app_df["Category"].values[0])



# *What is the mean rating of applications which price exceeds $20 and 
# the number of installs is over 10,000?
pAId = df[(df["Price"] > 20) & (df["Installs"] > 10000)]["Rating"]
print(pAId.mean())