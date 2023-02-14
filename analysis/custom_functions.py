from matplotlib import dates as mdates

def set_timeline(ax):
    '''This function sets the major ticks of the x-axis to in the form of their months and years and the minor ticks in the form of months.'''
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b\n%Y'))
    ax.xaxis.set_minor_locator(mdates.MonthLocator())
    ax.xaxis.set_minor_formatter(mdates.DateFormatter('%b'))
    # Pad the position of the minor ticks so that the months align with each other.
    ax.tick_params(axis='x', which='minor', pad=5, labelsize=7.5)
    ax.tick_params(axis='x', which='major', labelsize=7.5)