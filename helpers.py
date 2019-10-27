def group_shows_by_date(shows: list):
    shows_by_date = {}
    if shows:
        for show in shows:
            date_str = show['datetime'].strftime('%d-%m-%Y')
            
            if not shows_by_date.get(date_str): 
                shows_by_date[date_str] = []
            
            shows_by_date[date_str].append(show)
    return shows_by_date

