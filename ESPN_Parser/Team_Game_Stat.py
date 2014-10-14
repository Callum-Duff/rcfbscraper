import re
import C

# Holds the data for a team-game stats
class Team_Game_Stat:

    # Constructor
    def __init__(self, game_code, team_code):
        self.Game_Code = game_code
        self.Team_Code = team_code
        self.Rush_Att = 0
        self.Rush_Yard = 0
        self.Rush_TD = 0
        self.Pass_Att = 0
        self.Pass_Comp = 0
        self.Pass_Yard = 0
        self.Pass_TD = 0
        self.Pass_Int = 0
        self.Pass_Conv = 0
        self.Kickoff_Ret = 0
        self.Kickoff_Ret_Yard = 0
        self.Kickoff_Ret_TD = 0
        self.Punt_Ret = 0
        self.Punt_Ret_Yard = 0
        self.Punt_Ret_TD = 0
        self.Fum_Ret = 0
        self.Fum_Ret_Yard = 0
        self.Fum_Ret_TD = 0
        self.Int_Ret = 0
        self.Int_Ret_Yard = 0
        self.Int_Ret_TD = 0
        self.Misc_Ret = 0
        self.Misc_Ret_Yard = 0
        self.Misc_Ret_TD = 0
        self.Field_Goal_Att = 0
        self.Field_Goal_Made = 0
        self.Off_XP_Kick_Att = 0
        self.Off_XP_Kick_Made = 0
        self.Off_2XP_Att = 0
        self.Off_2XP_Made = 0
        self.Def_2XP_Att = 0
        self.Def_2XP_Made = 0
        self.Safety = 0
        self.Points = 0
        self.Punt = 0
        self.Punt_Yard = 0
        self.Kickoff = 0
        self.Kickoff_Yard = 0
        self.Kickoff_Touchback = 0
        self.Kickoff_Out_Of_Bounds = 0
        self.Kickoff_Onsides = 0
        self.Fumble = 0
        self.Fum_Lost = 0
        self.Tackle_Solo = 0
        self.Tackle_Assist = 0
        self.Tackle_For_Loss = 0
        self.Tackle_For_Loss_Yard = 0
        self.Sack = 0
        self.Sack_Yard = 0
        self.QB_Hurry = 0
        self.Fum_Forced = 0
        self.Pass_Broken_Up = 0
        self.Kick_Punt_Blocked = 0
        self.First_Down_Rush = 0
        self.First_Down_Pass = 0
        self.First_Down_Penalty = 0
        self.Time_Of_Possession = 0
        self.Penalty = 0
        self.Penalty_Yard = 0
        self.Third_Down_Att = 0
        self.Third_Down_Conv = 0
        self.Fourth_Down_Att = 0
        self.Fourth_Down_Conv = 0
        self.Red_Zone_Att = 0
        self.Red_Zone_TD = 0
        self.Red_Zone_Field_Goal = 0


    # Gleans relevent data from a play
    def Extract_Play_Data(self, play):

        # Get play basics
        turnover = self.Check_Turnover(play)
        no_play = self.Check_No_Play(play)
        ptype = play[C.TYPE]

        # Get rushing stats
        if ptype == "RUSH" and no_play == 0:
            self.Rush_Att += 1



    # Checks if a turnover occurred
    def Check_Turnover(self, play):
        m = re.search(r"(?P<fum>FUMBLE)|(?P<int>INTERCEPT)", play)
        if m.group("fum"):
            return 1
        elif m.group("int"):
            return 1
        else:
            return 0


    # Checks if a turnover occurred
    def Check_No_Play(self, play):
        if len(play[C.NOPLY]) == 0:
            print 0
            return 0
        elif int(play[C.NOPLY]) == 1:
            print 1
            return 1


    # Returns an array of relavent information
    def Compile_Stats(self):
        OutputArray = []
        OutputArray.append(str(self.Team_Code))
        OutputArray.append(str(self.Game_Code))
        OutputArray.append(str(self.Rush_Att))
        OutputArray.append(str(self.Rush_Yard))
        OutputArray.append(str(self.Rush_TD))
        OutputArray.append(str(self.Pass_Att))
        OutputArray.append(str(self.Pass_Comp))
        OutputArray.append(str(self.Pass_Yard))
        OutputArray.append(str(self.Pass_TD))
        OutputArray.append(str(self.Pass_Int))
        OutputArray.append(str(self.Pass_Conv))
        OutputArray.append(str(self.Kickoff_Ret))
        OutputArray.append(str(self.Kickoff_Ret_Yard))
        OutputArray.append(str(self.Kickoff_Ret_TD))
        OutputArray.append(str(self.Punt_Ret))
        OutputArray.append(str(self.Punt_Ret_Yard))
        OutputArray.append(str(self.Punt_Ret_TD))
        OutputArray.append(str(self.Fum_Ret))
        OutputArray.append(str(self.Fum_Ret_Yard))
        OutputArray.append(str(self.Fum_Ret_TD))
        OutputArray.append(str(self.Int_Ret))
        OutputArray.append(str(self.Int_Ret_Yard))
        OutputArray.append(str(self.Int_Ret_TD))
        OutputArray.append(str(self.Misc_Ret))
        OutputArray.append(str(self.Misc_Ret_Yard))
        OutputArray.append(str(self.Misc_Ret_TD))
        OutputArray.append(str(self.Field_Goal_Att))
        OutputArray.append(str(self.Field_Goal_Made))
        OutputArray.append(str(self.Off_XP_Kick_Att))
        OutputArray.append(str(self.Off_XP_Kick_Made))
        OutputArray.append(str(self.Off_2XP_Att))
        OutputArray.append(str(self.Off_2XP_Made))
        OutputArray.append(str(self.Def_2XP_Att))
        OutputArray.append(str(self.Def_2XP_Made))
        OutputArray.append(str(self.Safety))
        OutputArray.append(str(self.Points))
        OutputArray.append(str(self.Punt))
        OutputArray.append(str(self.Punt_Yard))
        OutputArray.append(str(self.Kickoff))
        OutputArray.append(str(self.Kickoff_Yard))
        OutputArray.append(str(self.Kickoff_Touchback))
        OutputArray.append(str(self.Kickoff_Out_Of_Bounds))
        OutputArray.append(str(self.Kickoff_Onsides))
        OutputArray.append(str(self.Fumble))
        OutputArray.append(str(self.Fum_Lost))
        OutputArray.append(str(self.Tackle_Solo))
        OutputArray.append(str(self.Tackle_Assist))
        OutputArray.append(str(self.Tackle_For_Loss))
        OutputArray.append(str(self.Tackle_For_Loss_Yard))
        OutputArray.append(str(self.Sack))
        OutputArray.append(str(self.Sack_Yard))
        OutputArray.append(str(self.QB_Hurry))
        OutputArray.append(str(self.Fum_Forced))
        OutputArray.append(str(self.Pass_Broken_Up))
        OutputArray.append(str(self.Kick_Punt_Blocked))
        OutputArray.append(str(self.First_Down_Rush))
        OutputArray.append(str(self.First_Down_Pass))
        OutputArray.append(str(self.First_Down_Penalty))
        OutputArray.append(str(self.Time_Of_Possession))
        OutputArray.append(str(self.Penalty))
        OutputArray.append(str(self.Penalty_Yard))
        OutputArray.append(str(self.Third_Down_Att))
        OutputArray.append(str(self.Third_Down_Conv))
        OutputArray.append(str(self.Fourth_Down_Att))
        OutputArray.append(str(self.Fourth_Down_Conv))
        OutputArray.append(str(self.Red_Zone_Att))
        OutputArray.append(str(self.Red_Zone_Field_Goal))
        OutputArray.append(str(self.Red_Zone_TD))
        return OutputArray


    # Returns the header for a play type
    def Team_Game_Stats_Header(self):
        OutputArray = []
        OutputArray.append("Team Code")
        OutputArray.append("Game Code")
        OutputArray.append("Rush Att")
        OutputArray.append("Rush Yard")
        OutputArray.append("Rush TD")
        OutputArray.append("Pass Att")
        OutputArray.append("Pass Comp")
        OutputArray.append("Pass Yard")
        OutputArray.append("Pass TD")
        OutputArray.append("Pass Int")
        OutputArray.append("Pass Conv") 
        OutputArray.append("Kickoff Ret") 
        OutputArray.append("Kickoff Ret Yard") 
        OutputArray.append("Kickoff Ret TD") 
        OutputArray.append("Punt Ret") 
        OutputArray.append("Punt Ret Yard") 
        OutputArray.append("Punt Ret TD") 
        OutputArray.append("Fum Ret") 
        OutputArray.append("Fum Ret Yard") 
        OutputArray.append("Fum Ret TD") 
        OutputArray.append("Int Ret") 
        OutputArray.append("Int Ret Yard") 
        OutputArray.append("Int Ret TD") 
        OutputArray.append("Misc Ret") 
        OutputArray.append("Misc Ret Yard") 
        OutputArray.append("Misc Ret TD") 
        OutputArray.append("Field Goal Att") 
        OutputArray.append("Field Goal Made") 
        OutputArray.append("Off XP Kick Att") 
        OutputArray.append("Off XP Kick Made") 
        OutputArray.append("Off 2XP Att") 
        OutputArray.append("Off 2XP Made") 
        OutputArray.append("Def 2XP Att") 
        OutputArray.append("Def 2XP Made") 
        OutputArray.append("Safety")
        OutputArray.append("Points") 
        OutputArray.append("Punt") 
        OutputArray.append("Punt Yard") 
        OutputArray.append("Kickoff") 
        OutputArray.append("Kickoff Yard") 
        OutputArray.append("Kickoff Touchback") 
        OutputArray.append("Kickoff Out-Of-Bounds") 
        OutputArray.append("Kickoff Onside") 
        OutputArray.append("Fumble") 
        OutputArray.append("Fumble Lost") 
        OutputArray.append("Tackle Solo") 
        OutputArray.append("Tackle Assist") 
        OutputArray.append("Tackle For Loss") 
        OutputArray.append("Tackle For Loss Yard") 
        OutputArray.append("Sack")
        OutputArray.append("Sack Yard")
        OutputArray.append("QB Hurry") 
        OutputArray.append("Fumble Forced") 
        OutputArray.append("Pass Broken Up") 
        OutputArray.append("Kick/Punt Blocked") 
        OutputArray.append("1st Down Rush")
        OutputArray.append("1st Down Pass")
        OutputArray.append("1st Down Penalty") 
        OutputArray.append("Time Of Possession") 
        OutputArray.append("Penalty") 
        OutputArray.append("Penalty Yard") 
        OutputArray.append("Third Down Att") 
        OutputArray.append("Third Down Conv") 
        OutputArray.append("Fourth Down Att") 
        OutputArray.append("Fourth Down Conv") 
        OutputArray.append("Red Zone Att") 
        OutputArray.append("Red Zone TD") 
        OutputArray.append("Red Zone Field Goal") 
        return OutputArray