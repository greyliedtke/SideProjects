# imports
import matplotlib.pyplot as plt


def plot_man(df, x_data, y_data, y_2data=(), sub_y=(), legend=False, title=None, x_label=None, y_label=None,
             x_lim=None, y_lim=None, y_2lim=None, sub_y_label=None,
             grid=False, save=None, show=False):

    # initialze plots
    fig, ax = plt.subplots()

    # subplot...
    if len(sub_y) > 0:
        fig, (ax, ax_2) = plt.subplots(2, 1)
        for y_p in sub_y:
            ax_2.plot(df[x_data], df[y_p])
        ax_2.set_ylabel(sub_y_label)

    # plot 1 vs multiple things
    for y_p in y_data:
        # only feeding in y_data...
        if x_data is None:
            ax.plot(range(len(df[y_p])), df[y_p])
        else:
            ax.plot(df[x_data], df[y_p])

    ax.legend(y_data)

    # second axis plotting...
    if len(y_2data) > 0:
        ax2 = ax.twinx()
        for y_p in y_2data:
            ax2.plot(df[x_data], df[y_p], '-r')

    # formatting
    if x_lim is not None:
        ax.set_xlim(x_lim)
    if y_lim is not None:
        ax.set_ylim(y_lim)

    if title is not None:
        ax.set_title(title)
    if x_label is not None:
        ax.set_xlabel(x_label)
    if y_label is not None:
        ax.set_ylabel(y_label)
    if grid is True:
        plt.grid()
        # ax.grid()
    if save is not None:
        fig.savefig(save+'.png')
    # show = False

    if show is True:
        plt.show()