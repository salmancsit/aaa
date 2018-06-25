# -*- coding: utf-8 -*-
"""
Created on Sat May 12 16:04:54 2018

@author: Anees Shiekh
"""

import sys, string, os
import feedparser
import urllib2
from bs4 import BeautifulSoup

IntRelFactor=0
IntSentiment=0
LocalSentiment=0
SectorRl=0
EconomyRl=0
news=[]


def EvaluateLocalFeed(rssfeedadd):
    global IntRelFactor
    feed=feedparser.parse(rssfeedadd)
    feedlen=len(feed)

    for i in range (0,feedlen-2):
        try:
            
            url = feed["entries"][i]["link"]
        except IndexError:
            print ('Local feed extraction Failed')
            return None
        Title=feed["entries"][i]["title"]
        SentimeterL(Title)
        EconomyRel(Title)
        SectorRel(Title)

def checkrelevance(sentence):
    Relcounter=0
    keywordstitle = ['pakistan',10,'Pakistan',10,'CPEC',7,'cpec',7, 'Asia',5,'asia',5,'China',4,'china',4,'EU',2,
                 'stocks',2,'Stocks',3,'markets',3,'Stock',3,'Stock market',3,'Oil',4,'oil',4,'Crude oil',4,
                 'crude oil',4,'TTP',6,'ttp',6,'taliban',6,'Tehreek-e-taliban pakistan',6,'Taliban',6,'Dollar',6,
                 'dollar',6,'USD',6,'Euro',6,'euro',6,'PKR',8,
                 'true']   
       
    titlewords = sentence.split(' ')
    for a in range (0,len(titlewords)-1):
        for t in range (0,len(keywordstitle)-1):
            #print titlewords[a]
            if titlewords[a]==keywordstitle[t]:
                if Relcounter<keywordstitle[t+1]:
                    
                    Relcounter=keywordstitle[t+1]
                    #print Relcounter     
    return Relcounter


def EconomyRel(sentence):
    global EconomyRl
    
    
  
    
    
    
    keywordEconomy = ['SBP','sbp','State','bank','Bank','state','Interest','interest','rate','Rate','rates','ECB','FED','Fed',
                      'reserve','reserves','Dollar','dollar','USD','Parity','Euro','currency','Finance','Ministry','finance','economy','Economy','GDP',
                      'G.D.P.','growth','WB','ADB','development','Asian','asian','Development','loan','repayment','default','PPIB','WAPDA','Load','Shedding',
                      'Gold','Oil','oil','prices','Economic','IMF','Fund','Exports','exports','export','Export','Import','import','Imports','imports','tax','Tax','Taxes',
            
            
            ]
    
    
    titlewords = sentence.split(' ')
    for a in range (0,len(titlewords)):
        for t in range (0,len(keywordEconomy)-1):
            if titlewords[a]==keywordEconomy[t]:
                #print keywordSectors[t]
                #sentence= sentence.replace("\r\n", "")
                #sentence = string.split(sentence, ',')
                #sentence = map(int,sentence)
                news.append(('Economy: > ')+sentence)
                           
                EconomyRl=EconomyRl+1
    return news
                        
   
def SentimeterL(sentence):
    KP=0
    KN=0
    global LocalSentiment
    keywordsPositive = ['admire','welcome','appreciate','applaud','encourage','truthful',
                        'insight','insightful','progressive','better','betterment','development','developed','committed','pledged','vowed',
                        'promised','promising','fruitful','benevolent','benevolence','admire','admiring','admired','recognize',
                        'acknowledged','acknowledge','trusted','peaceful','stable','stability','stabilize','stabilizing','strengthen','strong',
                        'friendly','friendship','fellows ','fellowship','allies',
                        'vanguard','independent','democracy','democratic','freedom',
                        'institution','flourishing','flourished','talks','peace talks',
                        'stake holders','dialogue','negotiate','negotiations','trades',
                        'exports','imports','strategic','strategy','open-ended','openness',
                        'opened','diplomatic','diplomacy','opinion','rights ',
                        'financial stability','employees','employment','educated',
                        'educational','privilege','privileged','celebrate','celebrations',
                        'character','usual','permanent','beaming','sunny','fresh','wild',
                        'beautiful. amazing','striking','youthful','skill','skilled ','criticism',
                        'labor ','executive','approve','approval','drama','talent',
                        'talented','fragrance','fresco','paintings','induction','industry',
                        'introduction','introduce','debug','debunk','ancient','traditional',
                        'experience','exclusive','grouping','proceeds','procedural',
                        'rule out','adjournment','budget','appointment','leader','leadership',
                        'manageable','Flora and fauna','beaches','scene','scenic','Dawn',
                        'dusk','aspire','inspirational','inspiring','relevant','reverence',
                        'revolve','universal','cosmic','success','encouraging'
                 'true']    
       
    
    keywordsNegative= [ 'Disaster','warns','warning','warming ','deceive','decietful','murderer',
                       'murderous','assault','depreciation','depreciate','harrassment','harrass','accusations','accuser',
                       'blame','blaming','fanning','terrorism','terrorists','delusional','slow','Slow',
                       'compromised','compromise','plight','submission','submissive',
                       'under privilege','slavery','human rights violations','sink','Sink','blast','Blast','suicide','Suicide',
                       'human trafficking','atrocious','atrocities','threaten','terror','terrorist','Terror','Terrorist',
                       'threatening','dangerous','danger','endanger','sold','underhand',
                       'concealed','hurtful','malicious','malign','maligning',
                       'malignant','cancer ','cancerous','cancelled','cancel','dramatic',
                       'over taken','coup ','false','lies','cheat','cheating ','steal',
                       'stolen','dodge','double cross','untrustworthy ','wrap up',
                       'cut down. Aid','blockage','blocked','dormant','redundant',
                       'refused','refusal','started','shocked','taken aback','reeling',
                       'side affects ','low','shameful','shameless','stubborn','rigid',
                       'twisted','double standards','hypocrites','hypocrisy','unresolved',
                       'undisclosed','indecent. Indecisive','undue','apologize','sorry',
                       'unabashed','unabashedly','fraudulent','fraud','exclude','gangs',
                       'sectarianism','killing','slaughter','kidnap','rape','rapped',
                       'summoned','dragged','pulled','manhandled','unstable',
                       'odd','adjourned','uncomfortable','uncouth','unmanageable','shortage',
                       'outage','load shedding','scarcity','scarce','famine','blackmail',
                       'cybercrime','hacks','spams','hit','hit hard','low','flat','suffer',
                       'poor','poverty','tragic ','henious','horrendous','horror','massacre',
                       'hostage','bomb disposal','disposable','fanatic','frantic','extremist',
                       'extremism','fascist','dictatorship','dictated','dictatorial',
                       'deficit','crack','cracked','crime','criminal','bomb','bombing','punished','punishment'
            ]
    
    
    titlewords = sentence.split(' ')
    for a in range (0,len(titlewords)):
        for t in range (0,len(keywordsPositive)-1):
            if titlewords[a]==keywordsPositive[t]:
                           
                LocalSentiment=LocalSentiment+1
                        
    titlewords = sentence.split(' ')
    for a in range (0,len(titlewords)):
        for t in range (0,len(keywordsNegative)-1):
            if titlewords[a]==keywordsNegative[t]:
                         
                LocalSentiment=LocalSentiment-1
                
def EvaluateLocalFeed(rssfeedadd):
    global IntRelFactor
    feed=feedparser.parse(rssfeedadd)
    feedlen=len(feed)

    for i in range (0,feedlen-2):
        try:
            
            url = feed["entries"][i]["link"]
        except IndexError:
            print ('Local feed extraction Failed')
            return None
        Title=feed["entries"][i]["title"]
        SentimeterL(Title)
        EconomyRel(Title)
        #SectorRel(Title)


def main():
    EvaluateLocalFeed('https://www.geo.tv/rss/1/1')
    EvaluateLocalFeed ('https://tribune.com.pk/pakistan/feed/')
    EvaluateLocalFeed ('https://www.thenews.com.pk/rss/1/1')
    EvaluateLocalFeed ('https://www.thenews.com.pk/rss/2/15')
    EvaluateLocalFeed ('https://dailytimes.com.pk/feed/')
    EvaluateLocalFeed ('https://tribune.com.pk/business/feed/')
    EvaluateLocalFeed ('https://www.brecorder.com/feed/')
    EvaluateLocalFeed ('https://www.geo.tv/rss/1/3')
    EvaluateLocalFeed ('https://dailytimes.com.pk/feed')
    return news
