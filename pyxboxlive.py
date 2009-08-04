#!/usr/bin/env python

# Copyright (c) 2009 Michael Dales (mdales@mac.com)
 
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

import datetime
import urllib
from xml.etree import ElementTree as ET

XBOXLIVEAPIPREFIX = 'http://duncanmackenzie.net/services/GetXboxInfo.aspx?GamerTag='
XBOXLIVEAVATARURLTEMPLATE = 'http://avatar.xboxlive.com/avatar/%s/avatar-body.png'



class PresenceInfo(object):
    
    ##########################################################################
    #
    def __init__(self, info_el):
        self.xml_data = info_el    
    #
    ##########################################################################
    

    ##########################################################################
    #
    def valid(self):
        return self.xml_data.find('Valid').text == 'true'
    #
    ##########################################################################
    

    ##########################################################################
    #
    def info(self):
        return self.xml_data.find('Info').text
    #
    ##########################################################################
    

    ##########################################################################
    #
    def info2(self):
        return self.xml_data.find('Info2').text
    #
    ##########################################################################
    

    ##########################################################################
    #
    def last_seen(self):    
        timestr = self.xml_data.find('LastSeen').text
        return datetime.datetime.strptime(timestr, '%Y-%m-%dT%H:%M:%S+00:00')
    #
    ##########################################################################
    

    ##########################################################################
    #
    def online(self):
        return self.xml_data.find('Online').text == 'true'
    #
    ##########################################################################
    

    ##########################################################################
    #
    def status_text(self):
        return self.xml_data.find('StatusText').text
    #
    ##########################################################################
    

    ##########################################################################
    #
    def title(self):
        return self.xml_data.find('Title').text
    #
    ##########################################################################
    


class Game(object):
    
    ##########################################################################
    #
    def __init__(self, game_el):
        self.xml_data = game_el    
    #
    ##########################################################################
    

    ##########################################################################
    #
    def game_id(self):
        return self.xml_data.find('GameID').text
    #
    ##########################################################################
    

    ##########################################################################
    #
    def name(self):
        return self.xml_data.find('Name').text
    #
    ##########################################################################
    

    ##########################################################################
    #
    def total_achievments(self):
        return int(self.xml_data.find('TotalAchievements').text)
    #
    ##########################################################################
    

    ##########################################################################
    #
    def total_gamer_score(self):
        return int(self.xml_data.find('TotalGamerScore').text)
    #
    ##########################################################################
    

    ##########################################################################
    #
    def image_32_url(self):
        return self.xml_data.find('Image32Url').text
    #
    ##########################################################################
    

    ##########################################################################
    #
    def image_64_url(self):
        return self.xml_data.find('Image64Url').text
    #
    ##########################################################################
    
    


class UserGameInfo(object):
    
    ##########################################################################
    #
    def __init__(self, game_el):
        self.xml_data = game_el    
    #
    ##########################################################################
    

    ##########################################################################
    #
    def last_played(self):    
        timestr = self.xml_data.find('LastPlayed').text
        return datetime.datetime.strptime(timestr, '%Y-%m-%dT%H:%M:%S+00:00')
    #
    ##########################################################################
    

    ##########################################################################
    #
    def achievments(self):
        return int(self.xml_data.find('Achievements').text)
    #
    ##########################################################################
    

    ##########################################################################
    #
    def gamer_score(self):
        return int(self.xml_data.find('GamerScore').text)
    #
    ##########################################################################
    

    ##########################################################################
    #
    def details_url(self):
        return self.xml_data.find('DetailsURL').text
    #
    ##########################################################################
    

    ##########################################################################
    #
    def game(self):
        return Game(self.xml_data.find('Game'))
    #
    ##########################################################################
    



class Gamer(object):
    
    ##########################################################################
    #
    def __init__(self, gamer_tag):
        self.tag = gamer_tag
        self.xml_data = None
        
        self.refresh()
    #
    ##########################################################################
    

    ##########################################################################
    #
    def refresh(self):
        
        sendable_tag = self.tag.replace(' ', '+')
        
        data = urllib.urlopen('%s%s' % (XBOXLIVEAPIPREFIX, sendable_tag))
        self.xml_data = ET.fromstring(data.read())
        data.close()    
    #
    ##########################################################################
    

    ##########################################################################
    #
    def avatar_body_image_url(self):
        # this doesn't actually come from the XML info
        return XBOXLIVEAVATARURLTEMPLATE % urllib.quote(self.tag)
    #
    ##########################################################################
    

    ##########################################################################
    #
    def presence_info(self):
        return PresenceInfo(self.xml_data.find('PresenceInfo'))
    #
    ##########################################################################
    

    ##########################################################################
    #
    def account_status(self):
        return self.xml_data.find('AccountStatus').text
    #
    ##########################################################################
    

    ##########################################################################
    #
    def state(self):
        return self.xml_data.find('State').text
    #
    ##########################################################################
    

    ##########################################################################
    #
    def gamer_tag(self):
        return self.xml_data.find('Gamertag').text
    #
    ##########################################################################
    

    ##########################################################################
    #
    def profile_url(self):
        return self.xml_data.find('ProfileUrl').text
    #
    ##########################################################################
    

    ##########################################################################
    #
    def tile_url(self):
        return self.xml_data.find('TileUrl').text
    #
    ##########################################################################
    

    ##########################################################################
    #
    def country(self):
        return self.xml_data.find('Country').text
    #
    ##########################################################################
    

    ##########################################################################
    #
    def reputation(self):
        return float(self.xml_data.find('Reputation').text)
    #
    ##########################################################################
    

    ##########################################################################
    #
    def reputation_image_url(self):
        return self.xml_data.find('ReputationImageUrl').text
    #
    ##########################################################################
    

    ##########################################################################
    #
    def gamer_score(self):
        return int(self.xml_data.find('GamerScore').text)
    #
    ##########################################################################
    

    ##########################################################################
    #
    def zone(self):
        return self.xml_data.find('Zone').text
    #
    ##########################################################################
    

    ##########################################################################
    #
    def recent_games(self):
        return [UserGameInfo(x) for x in self.xml_data.findall('RecentGames/XboxUserGameInfo')]
    #
    ##########################################################################


if __name__ == "__main__":
    # test case 
    gamer = Gamer('Michael Dales')
    
    p = gamer.presence_info()
    
    print "%s was last seen at %s playing %s" % (gamer.gamer_tag(), p.last_seen(), p.title())
    
    for game_info in gamer.recent_games():
        print "You last played %s on %s" % (game_info.game().name(), game_info.last_played())