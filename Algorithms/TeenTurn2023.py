from pydataset import data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.cm import get_cmap

## Load data
## Load python's sleep study dataset
df = data('sleepstudy')
print(df.head(11))

def change_to_string(integer):
    word = str(integer)
    return word

df["Subject"] = df["Subject"].apply(change_to_string)

n_subjects = df.Subject.nunique()
print('We have '+ str(n_subjects) + ' unique Subjects.')

n_days = df.Days.nunique()
print('We have recordings across ' + str(n_days) + ' days.')

## Plotting using seaborn (quick overview)
## plotting each subject
plt.figure()
plt.subplot(2,1,1)
sns.lineplot(data=df, x='Days', y='Reaction', hue='Subject')
plt.legend(ncol=2)

## plotting the overall mean
plt.subplot(2,1,2)
sns.lineplot(data=df, x="Days", y="Reaction")


## Manual plotting (more intuitive and helps to understand what the data is)
plt.figure()
subject_colours = get_cmap('tab20c').colors

for idx,subject in enumerate(df.Subject.unique()):
    print(idx)
    print(subject)
    data_subject = df[df['Subject']==subject]

    x= data_subject.Days
    y= data_subject.Reaction
    # plt.plot(x,y,'b')
    plt.plot(x, y, color=subject_colours[idx], label=subject, marker='o')
plt.xlabel('Days of sleep deprivation')
plt.ylabel('Reaction time [ms]')
plt.title('Reaction times per Day by Subject')

# add the mean
x = df.Days.unique()
# groupby columns Col1 and estimate the mean of column Col2
y = df.groupby(['Days'])['Reaction'].mean()
plt.plot(x,y,'kd--', label='mean reaction time per day')
plt.legend(ncol=2)


plt.show()

