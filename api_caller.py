import json
import urllib.parse
import urllib.request
import urllib.error

import datetime

def call(info):
 
    url = make_url(info)

    json_data = access_data(url)

    if json_data == None:
        return None

    j = json_data[0] #Simplifies
    
    #What game mode calculated without if statement
    mode = 0*info["is_s"]+1*info["is_t"]+2*info["is_c"]+3*info["is_m"]

    #just in case the pp & rank aren't correct (old matches)
    if info["pp_curr"]:
        pp_country = float(j["pp_raw"])
        rank_c = int(j["pp_country_rank"])
        rank_w = int(j["pp_rank"])

        if info["badges"] == '':
            badge_count = 0
        else:
            badge_count = int(info["badges"])
    else:
        pp_country = "NULL"
        rank_c = "NULL"
        rank_w = "NULL"
        badge_count = "NULL"

    if info['has_date']:
        date = datetime.date(int(info["year"]),int(info["month"]),int(info["day"]))
    else:
        date = "NULL"

        
    
    #returns in this order: username, osu_id, country, badges,
    #pp, rank_world, rank_country, date, team_name, tourney_name,win, gamemode
    return {"username":j["username"],"osu_id":j["user_id"],
            "country":j["country"],"badges":badge_count,
            "pp": pp_country,"rank_world": rank_w,"rank_country":rank_c,
            "date": date,"team_name":info["team_name"],
            "tourney_name":info["tourney_name"],"my_score":int(info["my_score"]),
            "their_score":int(info["their_score"]),"win":info["win"],"mode":mode}

def make_url(info):
    if info["is_username"]:
        return "https://osu.ppy.sh/api/get_user?u={}&type=string&k={}".format(
            info["user_id"],info["password"])
    elif info["is_user_id"]:
        return "https://osu.ppy.sh/api/get_user?u={}&type=id&k={}".format(
            info["user_id"],info["password"])

    #return website_url

def access_data(url):
    #accessing the website
    response = None
    
    try:        
        response = urllib.request.urlopen(url)

    except:
        #If player doesn't exist or is restricted
        return None

    else:
        data = response.read()
        html = data.decode("UTF-8")
        return json.loads(html)
        
    finally:
        if response != None:
            response.close()
