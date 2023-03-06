# %%
# Google Trends

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Set font
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']

df = pd.read_csv('data_science_topic_google_trend.csv')
df['Month'] = pd.to_datetime(df['Month'], format='%b-%y')
df = df.sort_values('Month')

df['Month'] = df['Month'].dt.strftime('%b %Y')

plt.figure(figsize=(16, 9))
sns.set_style('ticks')
sns.lineplot(x='Month', y='data_science_global', data=df, color='darkblue', linewidth=2.5)

plt.title('Interest in Data Science', fontsize=24, fontweight='bold', fontname='Arial', x=0.15)
plt.xlabel('') # remove y-axis label
plt.ylabel('') # remove y-axis label

plt.xticks(df[df['Month'].str.startswith('Jan')]['Month'], fontsize=16, fontname='Arial', rotation=45, ha='right') # show only January months
plt.yticks(fontsize=16, fontname='Arial')
sns.despine()
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.text(0.05, -0.15, 'Source: Google Trends', fontsize=16, fontname='Arial', transform=plt.gcf().transFigure) # move attribution closer to x-axis

plt.subplots_adjust(bottom=-0.01)
plt.subplots_adjust(left=-0.01)

plt.savefig('data_science_global_trends.png', dpi=300, bbox_inches='tight')

# %%
# What Data Teams spend their time on
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams
from textwrap import wrap
from matplotlib.ticker import StrMethodFormatter

# Set font
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']

def wrap_labels(labels):
    # Wrap labels to maximum two words per line
    return ['\n'.join(wrap(label, width=18)) for label in labels]

df = pd.read_csv('data_science_survey.csv')
df['value'] = df['value'] * 100

plt.figure(figsize=(16, 9))
sns.set_style('ticks')

ax = sns.barplot(x='value', y='category', data=df, dodge=1, color='darkblue', alpha=0.8, edgecolor='none', linewidth=0, saturation=1, orient='h', estimator=max)

plt.title('What data teams spend their time on', fontsize=24, fontweight='bold', fontname='Arial', x=0.15)
plt.xlabel('') # remove x-axis label
plt.ylabel('') # remove y-axis label

plt.xticks(fontsize=16, fontname='Arial')
plt.yticks(fontsize=16, fontname='Arial')

# Wrap y-axis labels to maximum two words per line
y_labels = wrap_labels(df['category'].tolist())
plt.yticks(range(len(y_labels)), y_labels)

sns.despine()

plt.gca().xaxis.set_major_formatter(StrMethodFormatter('{x:.0f}%'))

plt.text(0.05, -0.08, 'Source: Figure Eight Inc.', fontsize=16, fontname='Arial', transform=plt.gcf().transFigure) # move attribution closer to x-axis

plt.subplots_adjust(bottom=-0.01)
plt.subplots_adjust(left=-0.01)

# Add labels to the end of each bar
for i, v in enumerate(df['value']):
    ax.text(v + 1, i, '{:.0f}%'.format(v), fontsize=14, fontweight='bold', fontname='Arial', va='center')

plt.savefig('data_science_survey.png', dpi=300, bbox_inches='tight')


# %%
# AirBnB Nights Booked

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams
from textwrap import wrap
from matplotlib.ticker import FuncFormatter

# Set font
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']

def wrap_labels(labels):
    # Wrap labels to maximum two words per line
    return ['\n'.join(wrap(label, width=20)) for label in labels]

def millions_formatter(x, pos):
    # Format y-axis ticks in millions
    return '{:.0f}M'.format(x/1000000)

df = pd.read_csv('airbnb.csv')

plt.figure(figsize=(16, 9))
sns.set_style('ticks')

sns.lineplot(x='period', y='nights_booked', data=df, color='darkblue', marker='o', markersize=8, markeredgecolor='darkblue', markeredgewidth=0.5)

plt.title('AirBnB Nights Booked', fontsize=24, fontweight='bold', fontname='Arial', x=0.15)
plt.xlabel('') # remove x-axis label
plt.ylabel('') # remove y-axis label

# Wrap x-axis labels to maximum two words per line
x_labels = wrap_labels(df['period'].tolist())
plt.xticks(range(len(x_labels)), x_labels, fontsize=16)
plt.yticks(fontsize=16)

sns.despine()

plt.text(0.05, -0.08, 'Source: Airbnb Quarterly Earnings', fontsize=16, fontname='Arial', transform=plt.gcf().transFigure) # move attribution closer to x-axis

plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))

plt.subplots_adjust(bottom=-0.01)
plt.subplots_adjust(left=-0.01)

# Display y-values on the line markers
for x, y in zip(df['period'], df['nights_booked']):
    plt.text(x, y+1000000, '{:.1f}M'.format(y/1000000), fontsize=14, ha='center', va='bottom', fontname='Arial')

plt.savefig('airbnb_nights_booked.png', dpi=300, bbox_inches='tight')
