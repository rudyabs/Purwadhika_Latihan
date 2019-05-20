def my_plotter(ax, data1, data2, param_dict):
    '''
    Function untuk membuat graph

    Parameters
    ----------
    ax : Axes
        Axes utk menggambar

    data1 : array
        x data

    data2 : array
        y data
    
    param_dict : dict
        dictionary dari key argument(kwargs) untuk pass ke ax.plot
    
    Returns
    -------
    out : List
        List dari artists added
    '''
    out = ax.plot(data1, data2, **param_dict)
    return out
