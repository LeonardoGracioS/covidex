import matplotlib.pyplot as plt

def plot_death_per_date(dates, death_data, place):
    x = dates
    y = death_data

    fig, ax = plt.subplots(figsize=(20, 10))

    ax.plot(x, y)

    ax.set(xlabel='Dates', ylabel='Décès',
           title='Évolution du nombre de décès (Hors Ehpad) à ' +str(place)+ ' en fonction du temps')
    plt.xticks(rotation='vertical')
    ax.grid()

    plt.show()