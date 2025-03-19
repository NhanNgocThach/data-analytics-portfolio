def load_data(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def clean_data(df):
    df.dropna(inplace=True)
    return df

def analyze_data(df):
    summary = {
        'mean': df.mean(),
        'median': df.median(),
        'std_dev': df.std(),
        'correlation': df.corr()
    }
    return summary

def visualize_data(df):
    import matplotlib.pyplot as plt
    import seaborn as sns

    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()