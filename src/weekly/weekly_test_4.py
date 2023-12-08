import pandas as pd
import matplotlib.pyplot as plt
from typing import List
from src.distributions import ParetoDistribution
import numpy as np

euro12 = pd.read_csv('../data/Euro_2012_stats_TEAM.csv')


def number_of_participants(input_df: pd.DataFrame) -> int:
    """Megadja, hány csapat indult az Európa Bajnokságon."""
    return len(input_df)


def goals(input_df: pd.DataFrame) -> pd.DataFrame:
    """Visszaadja a csapatokat és az általuk lőtt gólokat egy új DataFrame-ben."""
    # Csapatok és gólok kiválasztása
    result_df = input_df[['Team', 'Goals']]

    return result_df


def sorted_by_goal(input_df: pd.DataFrame) -> pd.DataFrame:
    """
    Sorba rendezi az országokat a lőtt gólok száma alapján csökkenő sorrendben.
    Használja az előző goals függvény eredményét.
    """
    # Hívjuk meg a goals függvényt
    goals_data = goals(input_df)

    # Sorba rendezés lőtt gólok szerint csökkenő sorrendben
    sorted_df = goals_data.sort_values(by='Goals', ascending=False)

    return sorted_df


def avg_goal(input_df: pd.DataFrame) -> float:
    """Visszaadja az átlagos gól számot a megadott DataFrame alapján."""
    # Csapatok és gólok kiválasztása
    goals_data = input_df['Goals']

    # Számoljuk ki az átlagot
    average_goals = goals_data.mean()

    return average_goals


def countries_over_five(input_df: pd.DataFrame) -> pd.DataFrame:
    """Visszaadja azokat az országokat, amelyek 6 vagy több gólt rúgtak."""
    # Csapatok és gólok kiválasztása
    goals_data = goals(input_df)

    # Szűrés 6 vagy több gólra
    selected_countries = goals_data[goals_data['Goals'] >= 6]

    return selected_countries


def countries_starting_with_g(input_df: pd.DataFrame) -> pd.DataFrame:
    """Visszaadja azon országok neveit, amelyek 'G'-vel kezdődnek."""
    # Csapatok kiválasztása
    teams_data = input_df['Team']

    # Szűrés 'G'-vel kezdődő országokra
    selected_countries = teams_data[teams_data.str.startswith('G')]

    return selected_countries


def first_seven_columns(input_df: pd.DataFrame) -> pd.DataFrame:
    """Visszaadja az első 7 oszlopot a megadott DataFrame-ből."""
    # Első 7 oszlop kiválasztása
    selected_columns = input_df.iloc[:, :7]

    return selected_columns


def every_column_except_last_three(input_df: pd.DataFrame) -> pd.DataFrame:
    """Visszaadja az összes oszlopot az utolsó 3-on kívül a megadott DataFrame-ből."""
    # Oszlopok kiválasztása az elsőtől az utolsó harmadikig
    selected_columns = input_df.iloc[:, :-3]

    return selected_columns


def sliced_view(input_df: pd.DataFrame, columns_to_keep: list, column_to_filter: str, rows_to_keep: list) -> pd.DataFrame:
    """
    Visszaadja a kiválasztott oszlopokat és sorokat a bemeneti adatokból.
    A sorokat egy bemeneti oszlop alapján szűrjük.
    """
    # Oszlopok kiválasztása
    selected_columns = input_df[columns_to_keep]

    # Sorok szűrése az adott oszlop alapján
    filtered_rows = input_df[input_df[column_to_filter].isin(rows_to_keep)]

    return filtered_rows[selected_columns]


def generate_quartile(input_df: pd.DataFrame) -> pd.DataFrame:
    """
    Kiegészíti a bemeneti adatokat egy 'Quartile' oszloppal a lőtt gólok alapján.
    """
    # Lőtt gólok alapján kvartilisok kiszámolása
    input_df['Quartile'] = pd.cut(input_df['Goals'], bins=[-1, 2, 4, 5, 12], labels=[4, 3, 2, 1], right=False)

    return input_df


def average_yellow_in_quartiles(input_df: pd.DataFrame) -> pd.DataFrame:
    """
    Kiszámítja átlagosan hány passzot adtak minden kvartilis értékhez.
    """
    # Kvartilisok kiszámolása a lőtt gólok alapján
    input_df['Quartile'] = pd.cut(input_df['Goals'], bins=[-1, 2, 4, 5, 12], labels=[4, 3, 2, 1], right=False)

    # Átlagosan hány passzot adtak minden kvartilis értékhez
    result_df = input_df.groupby('Quartile')['Passes'].mean().reset_index()

    return result_df


def minmax_block_in_quartile(input_df: pd.DataFrame) -> pd.DataFrame:
    """
    Visszaadja minden kvartilis esetén a blokkok minimális és maximális értékét.
    """
    # Kvartilisok kiszámolása a lőtt gólok alapján
    input_df['Quartile'] = pd.cut(input_df['Goals'], bins=[-1, 2, 4, 5, 12], labels=[4, 3, 2, 1], right=False)

    # Blokkok minimális és maximális értékeinek meghatározása
    result_df = input_df.groupby('Quartile')['Blocks'].agg(['min', 'max']).reset_index()

    return result_df


def scatter_goals_shots(input_df: pd.DataFrame) -> plt.Figure:
    """
    Scatter plot ábrázolása a gólok és a kaput ért találatok kapcsolatáról.
    """
    # Scatter plot létrehozása
    fig, ax = plt.subplots()
    ax.scatter(input_df['Goals'], input_df['Shots on target'])

    # Tengely feliratok beállítása
    ax.set_xlabel('Goals')
    ax.set_ylabel('Shots on target')
    ax.set_title('Goals and Shot on target')

    return fig


def scatter_goals_shots_by_quartile(input_df: pd.DataFrame) -> plt.Figure:
    """
    Scatter plot ábrázolása a gólok és a kaput ért találatok kapcsolatáról különböző színekkel a kvartilisek szerint.
    """
    # Kvartilisok kiszámolása a lőtt gólok alapján
    input_df['Quartile'] = pd.cut(input_df['Goals'], bins=[-1, 2, 4, 5, 12], labels=[4, 3, 2, 1], right=False)

    # Scatter plot létrehozása különböző színekkel a kvartilisek szerint
    fig, ax = plt.subplots()
    for quartile, color in zip(range(1, 5), ['red', 'blue', 'green', 'purple']):
        quartile_data = input_df[input_df['Quartile'] == quartile]
        ax.scatter(quartile_data['Goals'], quartile_data['Shots on target'], label=f'Quartile {quartile}', color=color)

    # Tengely feliratok beállítása
    ax.set_xlabel('Goals')
    ax.set_ylabel('Shots on target')
    ax.set_title('Goals and Shot on target')

    # Jelmagyarázat hozzáadása
    ax.legend(title='Quartiles')

    return fig


def gen_pareto_mean_trajectories(pareto_distribution: ParetoDistribution, number_of_trajectories: int, length_of_trajectory: int) -> List[List[float]]:
    """
    Létrehoz egy listát kumulatív átlagokkal a Pareto eloszlás felhasználásával.
    """
    np.random.seed(42)  # Seed beállítása

    trajectories = []
    for _ in range(number_of_trajectories):
        # Pareto eloszlásból véletlen számok generálása
        random_numbers = pareto_distribution.generate_random_numbers(length_of_trajectory)

        # Kumulatív átlagok kiszámolása
        cumulative_means = np.cumsum(random_numbers) / np.arange(1, length_of_trajectory + 1)

        # Hozzáadás a listához
        trajectories.append(cumulative_means.tolist())

    return trajectories