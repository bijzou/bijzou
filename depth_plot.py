#This cell defines the plotting function for depth profile

def depplot(depth, vars, data, error = None,fig = None,axs= None, axs_row = None, axs_col=None, text = None, ls = None,label = None, height=None, width=None, color = None):
    """Plot a set of variables in axs of a figure.
    Parameters
    ----------
    depth : array-like
        An array containing the time axis of the model.
    vars : list of str in format ['A','B','C',...]
        A list containing the names of the variables to plot in the dataset.
    fig: fig that want to add new plots on
    *data : dicts, dataframe
        The dataset that you want to plot.
    error: dataframe or dicts have errors for data, column names should be the same as the

    axs_row : list of Axes, optional
        A list of axes to plot the variables in. If not given, a new figure and axes are created.
    axs_col:
    label : dictionary has var as key and label as value [var1:'label1', var2:'label2']
        Some custom text to add to the legend.
    height : float, optional
        Height modifier to edit the height of the figure
    width : float, optional
        Width modifier to edit the width of the figure
   """
    color = color
    figlabel ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ###plot all the var you want to plot
    if fig is None:
      fig, axs = plt.subplots(nrows = axs_row,ncols= axs_col, figsize=(width, (height * len(vars))),
                                )
    i = 0 #count of i th var in vars
    if axs_col>1 and axs_row>1:
      for var in vars:
        #if we choose to connect the line between data point
        if ls:
          axs[i//axs_col,i%axs_col].plot(data[var], depth, ls= ls,c = color,alpha=1)
        if error:
        #plot errorbar of the data
          axs[i//axs_col,i%axs_col].errorbar(data[var], depth, yerr=None, xerr=error[var],fmt='none',
                                    capsize=1.5,elinewidth=0.5,color = 'k',zorder=0)

        # i:row of var, a: col of a, plot data point
        axs[i//axs_col,i%axs_col].scatter(data[var], depth, s = 10,c = color,alpha=1)
        axs[i//axs_col,i%axs_col].tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
        axs[i//axs_col,i%axs_col].xaxis.set_label_coords(0.1, 1.12)
        axs[i//axs_col,i%axs_col].set_xlim(0, right = data[var].max()*1.5) # set a range of x axis
        if text:
          axs[i//axs_col,i%axs_col].text(0.85, 0.03,figlabel[i],transform = axs[i//axs_col,i%axs_col].transAxes, fontsize = 20)
        if label:
          axs[i//axs_col,i%axs_col].set_xlabel(label[var],loc = 'center' , fontsize = 11)

        if i%axs_col == 0:
          axs[i//axs_col,i%axs_col].set_ylabel('Depth(cm)', fontsize = 12)
        i = i+1
    else:

      for var in vars:
        #if we choose to connect the line between data point
        if ls:
            axs[i].plot(data[var], depth, ls= ls,c = color,alpha=1)
        if error:
        #plot errorbar of the data
          axs[i].errorbar(data[var], depth, yerr=None, xerr=error[var],fmt='none',
                                    capsize=1.5,elinewidth=0.5,color = 'k',zorder=0)

        # i:row of var, a: col of a, plot data point
        axs[i].scatter(data[var], depth, s = 10,c = color,alpha=1)
        axs[i].tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
        axs[i].xaxis.set_label_coords(0.1, 1.12)
        axs[i].set_xlim(0, right = data[var].max()*1.5) # set a range of x axis
        if text:
          axs[i].text(0.85, 0.03,figlabel[i],transform = axs[i].transAxes, fontsize = 20)
        if label:
          axs[i].set_xlabel(label[var],loc = 'center' , fontsize = 11)

        if i%axs_col == 0:
          axs[i].set_ylabel('Depth(cm)', fontsize = 12)
        i = i+1


        #have not finish the else section when there is only one row or one column


    ####
    return fig,axs
