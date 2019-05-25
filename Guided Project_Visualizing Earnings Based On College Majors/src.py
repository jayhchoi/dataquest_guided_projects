# %% [markdown]
# # Visualizing Earnings Based On College Majors
# %% [markdown]
# ### 1. Explore data

# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# %%
get_ipython().run_line_magic('matplotlib', 'inline')


# %%
pd.set_option('display.max_columns', None)


# %%
recent_grads = pd.read_csv('recent-grads.csv')


# %%
recent_grads.iloc[0]


# %%
recent_grads.head()


# %%
recent_grads.tail()


# %%
recent_grads.describe()


# %%
recent_grads.info()

# %% [markdown]
# ### 2. Clean data

# %%
raw_data_count = recent_grads.shape[0]
raw_data_count


# %%
recent_grads = recent_grads.dropna()


# %%
cleaned_data_count = recent_grads.shape[0]
cleaned_data_count

# %% [markdown]
# ### 3. Draw plots
# %% [markdown]
# #### Scatter plots

# %%
recent_grads.plot(x='Sample_size', y='Median', kind='scatter')


# %%
recent_grads.plot(x='Sample_size', y='Unemployment_rate', kind='scatter')


# %%
recent_grads.plot(x='Full_time', y='Median', kind='scatter')


# %%
recent_grads.plot(x='ShareWomen', y='Unemployment_rate', kind='scatter')


# %%
recent_grads.plot(x='Men', y='Median', kind='scatter')


# %%
recent_grads.plot(x='Women', y='Median', kind='scatter')

# %% [markdown]
# #### Histograms

# %%
recent_grads['Sample_size'].hist()


# %%
recent_grads['Median'].hist()


# %%
recent_grads['Employed'].hist()


# %%
recent_grads['Full_time'].hist()


# %%
recent_grads['ShareWomen'].hist()


# %%
recent_grads['Unemployment_rate'].hist()


# %%
recent_grads['Men'].hist()


# %%
recent_grads['Women'].hist()

# %% [markdown]
# #### Scatter matrix

# %%
from pandas.plotting import scatter_matrix


# %%
scatter_matrix(recent_grads[['Sample_size', 'Median']],
               figsize=(12, 6), hist_kwds={"bins": 25})


# %%
scatter_matrix(recent_grads[['Sample_size', 'Median', 'Unemployment_rate']], figsize=(
    9, 9), hist_kwds={"bins": 25})

# %% [markdown]
# #### Bar plots

# %%
pd.concat([recent_grads.head(10), recent_grads.tail(10)]
          ).plot.bar(x='Major', y='ShareWomen')
