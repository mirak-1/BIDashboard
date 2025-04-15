def filter_by_month(df, selected_month):
    if selected_month == "All":
        filtered_df_month = df
    else:
        filtered_df_month = df[df['Month'] == int(selected_month)]
    
    return filtered_df_month

def filter_by_city(df, selected_city):
    if selected_city == "All":
        filtered_df_city = df
    else:
        filtered_df_city = df[df['City'] == selected_city]
    
    return filtered_df_city