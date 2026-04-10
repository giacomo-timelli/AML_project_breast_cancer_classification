import os
import joblib
import matplotlib.pyplot as plt
import pandas as pd


# 1. Setup folders
def setup_folders():
    """Create the folder structure for the project"""
    folders = [
        'data',
        'models',
        'figures',
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Folder created: {folder}")


# 2. Function to save datasets
def save_dataset(df, name):
    """Save a dataframe in CSV format"""
    path = f'data/{name}'
    df.to_csv(f'{path}.csv', index=False)
    print(f"Dataset saved: {path}.*")


# 3. Function to save plot
def save_plot(fig, name, tight_layout=True):
    """Save a figure in PNG"""
    path = f'figures/{name}'
    if tight_layout:
        plt.tight_layout()
    fig.savefig(f'{path}.png', dpi=300, bbox_inches='tight')
    print(f"Plot saved: {path}.*")
    plt.close()


# 4. Function to save models
def save_model(model, name):
    """Save a template in joblib format"""
    path = f'models/{name}.joblib'
    joblib.dump(model, path)
    print(f"Model saved: {path}")


# 5. Function for result log
def log_metrics(metrics, name):
    """Save metrics in CSV"""
    path = f'reports/metrics/{name}'
    pd.DataFrame(metrics).to_csv(f'{path}.csv', index=False)
    print(f"Metrics saved: {path}.*")
