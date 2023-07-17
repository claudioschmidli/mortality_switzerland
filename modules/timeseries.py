import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def set_font_sizes(small_size: int = 13, medium_size: int = 16, big_size: int = 20):
    """Change default font size of matplotlib plots:
    Note: You can dynamically change the default rc (runtime configuration) settings in a python script or interactively from the python shell.
    All rc settings are stored in a dictionary-like variable called matplotlib.rcParams, which is global to the matplotlib package.
    See matplotlib.rcParams for a full list of configurable rcParams.

    Args:
        small_size (int, optional): _description_. Defaults to 13.
        medium_size (int, optional): _description_. Defaults to 16.
        big_size (int, optional): _description_. Defaults to 20.
    """

    small_size = 13
    medium_size = 16
    big_size = 20

    plt.rc("font", size=small_size)  # controls default text sizes
    plt.rc("axes", titlesize=medium_size)  # fontsize of the axes title
    plt.rc("axes", labelsize=medium_size)  # fontsize of the x and y labels
    plt.rc("xtick", labelsize=medium_size)  # fontsize of the tick labels
    plt.rc("ytick", labelsize=medium_size)  # fontsize of the tick labels
    plt.rc("legend", fontsize=10)  # legend fontsize
    plt.rc("figure", titlesize=big_size)  # fontsize of the figure title


def set_dual_x_axis_labels(ax: plt.Axes) -> plt.Axes:
    """Transform the x labels of the given Axes object to week/year multicategory labeling.
    Args:
        ax (plt.Axes): Axis object of a matplotlib figure, where the x axis contains the date in the format YYYYMM.
    Returns:

        plt.Axes: Axis object with the transformed x lables.
    """
    # calculate the positions of the borders between the years
    # Get the x-axis lables defined in the format YYYYMM.
    yearweek_labels_text = [int(l.get_text()) for l in ax.get_xticklabels()]

    # Extract only the month from the label
    ax.set_xticks(ax.get_xticks())  # to avoid warning
    ax.set_xticklabels(["" for ym in yearweek_labels_text])
    pos = []
    years = []
    prev = None
    # Get the positions for the year lables
    for i, ym in enumerate(yearweek_labels_text):
        # Extract year from yearmonth string
        if ym // 100 != prev:
            pos.append(i)
            prev = ym // 100
            years.append(prev)
    pos.append(len(yearweek_labels_text))
    pos = np.array(pos) - 0.5
    # vertical lines to separate the years
    ax.vlines(
        pos,
        0,
        -0.12,
        color="black",
        lw=0.8,
        clip_on=False,
        transform=ax.get_xaxis_transform(),
    )
    # years at the center of their range
    for year, pos0, pos1 in zip(years, pos[:-1], pos[1:]):
        ax.text(
            (pos0 + pos1) / 2,
            -0.07,
            year,
            ha="center",
            clip_on=False,
            transform=ax.get_xaxis_transform(),
        )
    ax.set_xlim(pos[0], pos[-1])
    ax.set_ylim(ymin=0)
    ax.set_xlabel("")
    plt.tight_layout()
    return ax


def lineplot_multi_category_ax(
    ax: plt.Axes.axes,
    data: pd.DataFrame,
    x_values: str,
    y_values: str,
    hue: str,
    title: str,
    y_axis_label=None,
    x_axis_label=None,
) -> None:
    """Add plot to ax object.

    Args:
        ax (plt.Axes.axes): ax object where the plot is added.
        data (pd.DataFrame): Pandas dataframe containing the data to be plotted.
        x_values (str): column name of data containing the x_values (format must be 'year_week'.)
        y_values (str): column name of data containing the y values.
        hue (str): Column containing the hue value (categories.)
        title (str): 'Title of the plot'
        y_axis_label (_type_, optional): Label of the y axis. Defaults to None.
        x_axis_label (_type_, optional): Label of the x axis. Defaults to None.

    Returns:
        _type_: ax object with added plot.
    """
    data = data.reset_index()
    set_font_sizes(small_size=13, medium_size=16, big_size=20)
    sns.set_style("white")

    sns.lineplot(
        x=x_values,
        y=y_values,
        data=data,
        hue=hue,
        hue_order=sorted(data[hue].unique()),
        # color='blue',
        ax=ax,
        errorbar=None,
    )

    # Show the plot
    sns.despine()
    ax = set_dual_x_axis_labels(ax)
    if y_axis_label is not None:
        ax.set_ylabel(y_axis_label)
    if x_axis_label is not None:
        ax.set_xlabel(x_axis_label, labelpad=80)
    ax.set_title(title, pad=60, fontdict={"fontsize": 30})

    ax.legend(bbox_to_anchor=(1, 1.2), loc="upper right", borderaxespad=0)
    ax.set_ylim([data[y_values].min(), data[y_values].max()])
    return ax
