from enum import Enum
import streamlit as st

class Sport(Enum):
    NFL = "NFL"
    NBA = "NBA"
    NHL = "NHL"
    MLB = "MLB"
    COLLEGE_FOOTBALL = "CFB"
    COLLEGE_BASKETBALL = "CBB"
    GOLF = "PGA"
    SOCCER = "SOCC"
    UFC = "UFC"
    MIXED_MARTIAL_ARTS = "MMA"
    NASCAR = "NAS"
    LEAGUE_OF_LEGENDS = "LOL"
    CFL = "CFL"
    EUROLEAGUE_BASKETBALL = "EL"
    TENNIS = "TEN"
    ARENA_FOOTBALL_LEAGUE = "AFL"
    XFL = "XFL"
    COUNTER_STRIKE_GLOBAL_OFFENSIVE = "CS:GO"
    ROCKET_LEAGUE = "RL"
    CALL_OF_DUTY = "COD"
    AUSTRALIAN_FOOTBALL_LEAGUE = "AFL"
    IRACING = "IRACE"

class SportInfo:
    def __init__(self, sportId, eventGroupId, name, latestSeasonId, latestSeasonYear, latestStartedSeasonId, latestStartedSeasonYear, generalSportName, fullName):
        self.sportId = sportId
        self.eventGroupId = eventGroupId
        self.name = name
        self.latestSeasonId = latestSeasonId
        self.latestSeasonYear = latestSeasonYear
        self.latestStartedSeasonId = latestStartedSeasonId
        self.latestStartedSeasonYear = latestStartedSeasonYear
        self.generalSportName = generalSportName
        self.fullName = fullName

SPORT_DETAILS = {
    Sport.NFL: SportInfo(1, "88808", "NFL", 652, 2023, 652, 2023, "Football", "National Football League"),
    Sport.MLB: SportInfo(2, "84240", "MLB", 654, 2024, 641, 2023, "Baseball", "Major League Baseball"),
    Sport.NHL: SportInfo(3, "42133", "NHL", 635, 2023, 635, 2023, "Hockey", "National Hockey League"),
    Sport.NBA: SportInfo(4, "42648", "NBA", 633, 2023, 633, 2023, "Basketball", "National Basketball Association"),
    Sport.COLLEGE_FOOTBALL: SportInfo(5, "87637", "CFB", 588, 2023, 588, 2023, "Football", "College Football"),
    Sport.COLLEGE_BASKETBALL: SportInfo(6, "92483", "CBB", 614, 2023, 614, 2023, "Basketball", "Men's College Basketball"),
    Sport.GOLF: SportInfo(7, "92694", "PGA", 645, 2023, 645, 2023, "Golf", "Professional Golfer's Association"),
    Sport.SOCCER: SportInfo(8, None, "SOCC", None, None, None, None, "Soccer", "Soccer"),
    Sport.UFC: SportInfo(25, "9034", "UFC", 663, 2024, 672, 2024, "MMA", "Ultimate Fighting Championship"),
    # Additional sports
    Sport.MIXED_MARTIAL_ARTS: SportInfo(None, None, "MMA", None, None, None, None, "MMA", "Mixed Martial Arts"),
    Sport.NASCAR: SportInfo(None, None, "NAS", None, None, None, None, "Racing", "NASCAR"),
    Sport.LEAGUE_OF_LEGENDS: SportInfo(None, None, "LOL", None, None, None, None, "Esports", "League of Legends"),
    Sport.CFL: SportInfo(None, None, "CFL", None, None, None, None, "Football", "Canadian Football League"),
    Sport.EUROLEAGUE_BASKETBALL: SportInfo(None, None, "EL", None, None, None, None, "Basketball", "EuroLeague Basketball"),
    Sport.TENNIS: SportInfo(None, None, "TEN", None, None, None, None, "Tennis", "Tennis"),
    Sport.ARENA_FOOTBALL_LEAGUE: SportInfo(None, None, "AFL", None, None, None, None, "Football", "Arena Football League"),
    Sport.XFL: SportInfo(None, None, "XFL", None, None, None, None, "Football", "XFL"),
    Sport.COUNTER_STRIKE_GLOBAL_OFFENSIVE: SportInfo(None, None, "CS:GO", None, None, None, None, "Esports", "Counter-Strike: Global Offensive"),
    Sport.ROCKET_LEAGUE: SportInfo(None, None, "RL", None, None, None, None, "Esports", "Rocket League"),
    Sport.CALL_OF_DUTY: SportInfo(None, None, "COD", None, None, None, None, "Esports", "Call of Duty"),
    Sport.AUSTRALIAN_FOOTBALL_LEAGUE: SportInfo(None, None, "AFL", None, None, None, None, "Football", "Australian Football League"),
    Sport.IRACING: SportInfo(None, None, "IRACE", None, None, None, None, "Esports", "iRacing"),
    # Continue adding other sports here following the same pattern
}

# Example of accessing sport information
#print("NFL Info:", vars(SPORT_DETAILS[Sport.NFL]))
#print("Soccer Info:", vars(SPORT_DETAILS[Sport.SOCCER]))

# To list all sports details:
#for sport, info in SPORT_DETAILS.items():
#    print(f"{sport.name} Details:", vars(info))


def get_sport_details(user_selected_sport_label):
    # Find the Sport enum member based on the user-selected label
    selected_sport = None
    for sport in Sport:
        if sport.value == user_selected_sport_label:
            selected_sport = sport
            break
    
    if selected_sport is None:
        return "Invalid sport selected", None, None
    
    # Get the sport details from the SPORT_DETAILS dictionary using the selected Sport enum member
    sport_info = SPORT_DETAILS.get(selected_sport)
    
    if sport_info is not None:
        return sport_info.eventGroupId, sport_info.sportId, sport_info.name
    else:
        return None, None, "Details not found for the selected sport"
    
