"""Visualization utilities for plotting data."""
import matplotlib.pyplot as plt


def draw_scatter(df, x_col, y_col):
    """Plot a scatter plot of y_col vs. x_col from a dataframe, with proper labels."""
    plt.scatter(df[x_col], df[y_col])
    plt.title(f'{y_col} vs. {x_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show()
