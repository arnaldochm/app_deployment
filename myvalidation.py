import pandas as pd



def data_validation(my_df):
    allowed_countries = [ 'Mexico', 'Guatemala', 'Colombia', 'Brazil', 'Taiwan', 'Honduras', 'Costa Rica', 'Tanzania, United Republic Of']
    allowed_varieties = ['Caturra', 'Typica', 'Bourbon', 'Catuai', 'Yellow Bourbon']
    allowed_columns = ['country_of_origin', 'variety', 'aroma', 'aftertaste', 'acidity', 'body', 'balance', 'moisture']

    if my_df.shape[1] != 8:
        return False
    
    if my_df.shape[0] == 0:
        return False
    
    if  my_df.columns.to_list().sort() !=  allowed_columns.sort():
        return False

    if not my_df['country_of_origin'].isin(allowed_countries).any():
        return False
    
    if not my_df['variety'].isin(allowed_varieties).any():
        return False
    
    #Check	aroma	aftertaste	acidity	body	balance	moisture

    if ((my_df.aroma < 6.5) | (my_df.aroma > 8.75)).any(): #Random Forest Classifier y otros arboles no permite valores fuera del rango con el que fue entrenado. Linear Reg y Redes sí. Pueden Extrapolar
        return False
    
    if ((my_df.aftertaste < 6.17) | (my_df.aftertaste > 8.58)).any():
        return False
    
    if ((my_df.acidity < 5.25) | (my_df.acidity > 8.58)).any():
        return False
    
    if ((my_df.body < 6.42) | (my_df.body > 8.42)).any():
        return False
    
    if ((my_df.balance < 6.08) | (my_df.balance > 8.58)).any():
        return False
    
    if ((my_df.moisture < 0.0) | (my_df.moisture > 0.17)).any():
        return False
    
    return True