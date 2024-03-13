from fastapi import FastAPI
import pandas as pd
app = FastAPI()

df_user_for_genre = pd.read_csv('./data/UserForGenre.csv')

@app.get('/UserForGenre')
def get_user_for_genre(genero: str = 'Action')-> dict:
    
    """ Gets the user with the most hours played for a given genre and the hours per year played.

    Args:
        genero (str, optional): The genre for which the user with the most hours played is searched. Default to None

    Returns:
        dict: return a dict with json data
    """
    
    df_filtered_by_genre = df_user_for_genre[df_user_for_genre['genre'] == genero]
    hours_year_list = [
        {'Año':year, 'Horas':hours} for year, hours in zip(df_filtered_by_genre['year'],df_filtered_by_genre['playtime_forever']) 
    ]

    result= {
        'Usuario con mas horas jugadas por genero {}'.format(genero): df_filtered_by_genre.top_user_id[0],
        'Horas jugadas': hours_year_list
        }


    return result 