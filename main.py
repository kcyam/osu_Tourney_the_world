import sql_handler
import gui
import api_caller
import pycountry

def main_function():
    conn = sql_handler.start_sql()
    c = conn.cursor()

    window = gui.start_gui(c)

    while True:
        #adding new opponents
        info_added_list, close_window = gui.event_loop(window,conn)
        
        if close_window or close_window == None:
            break        
        
        '''
        #Not in use yet
        sql_handler.add_data(conn,
            """INSERT INTO users VALUES (:username,:osu_id,:country,
            :badges, :pp, :rank_world,:rank_country,
            :date, :team_name, :win)""",{'username':,'osu_id':,'country'
            :,'badges':,'pp':,'rank_world':,'rank_country':,
            'date':,'team_name':,'win':})
        '''

    gui.close_gui(window)


if __name__ == '__main__':
    main_function()
