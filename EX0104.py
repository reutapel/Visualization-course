import pandas as pd
import matplotlib.pyplot as plt


def create_graph():
    data = pd.read_excel('HR.xlsx')
    dep_left = data[['Department', 'left']]
    dep_group = dep_left.groupby('Department')
    left_totals = dep_group.sum()
    # left_totals.sort(columns='left')
    my_plot = left_totals.sort_values(by='left', ascending=False).plot(kind='bar', legend=None,
                                                                           title="Number Of Employees Left By Department")
    my_plot.set_xlabel("Departments")
    my_plot.set_ylabel("Number Of Employees Left")
    plt.show()


if __name__ == '__main__':
    create_graph()
