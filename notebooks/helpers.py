import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def bivariante_analysis_cat(df, column_list, label, graph_label):
    '''
    Generate graphs comparing categorical features with a categorical label

    Parameters:
    df (pandas.DataFrame): The DataFrame
    column_list (list)   : The list with all the categorical features to consider
    label (str)          : The label used to see the distribution
    graph_label (str)    : the label of the x axis 
    '''
    for column in column_list:
        plt.figure(figsize=(30,4))
        plt.subplot(121)
        ax = sns.countplot(df, x=column, hue=df[label].astype(str))
        for i in ax.containers:
            ax.bar_label(i,)
        plt.ylabel(graph_label)
        plt.xticks(rotation=90)


def bivariante_analysis_num(df, column_list, label, graph_label):
    '''
    Generate graphs with the distribution of numerical values
    with respect to the label

    Parameters:
    df (pandas.DataFrame): The DataFrame
    column_list (list)   : The list with all the numerical features
    label (str)          : The label used to see the distribution
    graph_label (str)    : the label of the x axis
    '''
    for column in column_list:
        plt.figure(figsize=(20, 4))
        plt.subplot(121)
        sns.histplot(x=column, hue=df[label],
                     data=df, bins=30, kde=True, palette='YlOrRd')
        plt.title(column)
        plt.ylabel(graph_label)
        plt.xticks(rotation=90)