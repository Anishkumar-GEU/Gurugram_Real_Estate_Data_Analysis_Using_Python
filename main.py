import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv')

# Data cleaning
df.columns = df.columns.str.strip().str.lower().str.replace(" ","_")

# Numerical columns cleaning
df["price"] = df["price"].astype(str).str.replace(",", "").astype(float)
df["area"] = df["area"].astype(str).str.replace(",", "").astype(int)
df["rate_per_sqft"] = df["rate_per_sqft"].astype(str).str.replace(",", "").astype(int)

#Categorial Columns cleaning
df['status'] = df['status'].str.strip().str.lower()
df['rera_approval'] = df['rera_approval'].str.strip().str.lower().map({"approved by rera":True,"not approved by rera":False})
df['flat_type'] = df['flat_type'].str.strip().str.lower()

# Removing duplicates
df= df.drop_duplicates()


# Question 1:- Which is the costliest flat in the dataset?
costliest_flat = df.loc[df['price'].idxmax()] # used loc to get the complete row whose index is returned by idxmax()
#print(costliest_flat)

# Question 2(a):- Which locality has the highest average price?
highest_avg_price_locality = df.groupby('locality')['price'].mean().idxmax()
print(highest_avg_price_locality)

# Question 2(b):- Which locality has the lowest average price?
lowest_avg_price_locality = df.groupby('locality')['price'].mean().idxmin()
print(lowest_avg_price_locality)

# Question 3:- Which locality has the highest rate per square feet?
highest_rate_per_sqft = df.groupby('locality')['rate_per_sqft'].mean().idxmax()
print(highest_rate_per_sqft)

# Question 4:- Do ready-to-move properties cost more than under-construction properties?
ready_to_move_avg_price = df[df['status']=='ready to move']['price'].mean()
under_construction_avg_price = df[df['status']=='under construction']['price'].mean()

if (ready_to_move_avg_price > under_construction_avg_price):
    print("YES, ready to move properties costs more than under construction properties")
else:
    print("NO, Ready to move properties are not costlier than under construction properties")

# Question 5:- Do RERA Approved properties command a price premium?
rera_approved_avg_price = df[df['rera_approval']==True]['price'].mean()
non_rera_approved_avg_price = df[df['rera_approval']==False]['price'].mean()

if(rera_approved_avg_price > non_rera_approved_avg_price):
    print("YES, RERA Approved properties commands a price premium")
else:
    print("NO, RERA Approved properties do not command a price premium")

# Question 6:- How does area impact price?
sns.scatterplot(x="area",y="price",data=df)
plt.title("Impact of area on price",fontsize= 16, fontweight = "bold")
plt.show()
print("As we can see the Area is not affection the Price much")

# Question 7:- Which BHK configuration is most expensive?
most_expensive_bhk = df.groupby('bhk_count')['rate_per_sqft'].mean().idxmax()
print(most_expensive_bhk)

# Question 8:- Which property type is the costliest?
costliest_property = df.groupby('flat_type')['rate_per_sqft'].mean().idxmax()
print(costliest_property)

# Question 9:- Do certain builders price higher?
print(df.groupby('company_name')['rate_per_sqft'].mean().sort_values(ascending=False).head(5))

# Question 10:- Are larger homes more expensive per square feet?
sns.scatterplot(x="area", y="rate_per_sqft",data=df)
plt.title("Rate_per_sqft dependency on Area")
plt.show()
print("No")