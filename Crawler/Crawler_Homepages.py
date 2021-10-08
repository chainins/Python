# -*- coding: utf-8 -*-

###############################################
#                                             #
#     Created on Sat Sep 25 13:50:17 2021     #
#         @author: Chengpi Wu                 #
#                                             #
###############################################

# Crawler, Spyder for A website.
# Find out all of the links of commodities with videos, very useful for some specific products.

from pytube import YouTube

import os

import urllib.request

import re

from bs4 import BeautifulSoup
import requests
import lxml

import asyncio
from pyppeteer import launch

import nest_asyncio

nest_asyncio.apply()


def saveFile(txt,filename = "templete.html"):
    text_file = open(filename, "w")
    text_file.write(txt)
    text_file.close()
    return txt


async def getHTML(url, filename):
    browser = await launch()
    page = await browser.newPage()
 
    await page.goto(url) #, timeout=600000
    
    await page.evaluate('window.scrollBy(0, window.innerHeight)')
    
    # Method 2: wait element showing
    SearchFoundWordsSelector = 'tiles tiles--four-wide-max'
    SingleWaitSeconds = 1
    # while not await page.querySelector(SearchFoundWordsSelector):
    while not await page.xpath("//ul[@class='tiles tiles--four-wide-max']") and  not await page.xpath("//*[@class='pagination-container']"):
      print("Still not found %s, wait %s seconds" % (SearchFoundWordsSelector, SingleWaitSeconds))
      await asyncio.sleep(SingleWaitSeconds)
    await asyncio.sleep(10)

    global htmlURL
    htmlURL = saveFile(await page.content(), filename)
    await browser.close()
    return htmlURL
    

finalLinks = []


def links3(url,filename):
    htmlURL = asyncio.get_event_loop().run_until_complete(getHTML(url, filename))
    
    empty = re.findall(r"Sorry, there's nothing here at the moment.", htmlURL)
    if len(empty) > 0:
        return []
    
    links = re.findall(r"/item/.*?\"", htmlURL)

    global finalLinks 
    for itemLink in links:
        itemLink = itemLink[:itemLink.find('?')]
        if not (itemLink in finalLinks):
            # print(itemLink)
            finalLinks.append(itemLink)
    # print(len(finalLinks))

    return finalLinks


import ssl

           

def getItemVideoLinks(itemLinks) :
    pairItems=[]
    for itemUrl in itemLinks:
        html2 = urllib.request.urlopen(itemUrl)
        htmlTxt = html2.read().decode()
        # print(html2.read().decode())
        linkYoutube = re.findall(r"www.youtube.com/embed/(\S{11})\"", htmlTxt)
        
        if len(linkYoutube)>=1:
            price1 = re.findall(r"price-with-shipping__price__amount\">(.*?)<div",htmlTxt)
            price2 = re.findall(r"price-display\">(.*?)</span>",price1[0])   # \$ if need
            itemTitle = re.findall(r"<title>(.*?)</title>", htmlTxt)
            print('pairs: ',itemUrl,linkYoutube,itemTitle)
            pairItems.append([itemUrl,linkYoutube,itemTitle,price2[0]])
    return pairItems
        
        

def getVideo(pvSearcLink):
    # how to get html.
    html = urllib.request.urlopen(pvSearcLink)
    results_ids = re.findall(r'<a class="grid-card__inner" href="(\S{})" target="_blank">', html.read().decode())
    print(results_ids)

import subprocess
import os
def downAudio(ytLink):
    filepath = os.getcwd()
    try:
        downVideo = YouTube(ytLink)
        
        audio = downVideo.streams.filter(only_audio=True, file_extension='mp4').first()

        oldfilename = audio.download(filepath)
        
        newfilename = oldfilename[:-4] + '.mp3'
        cmd = 'ffmpeg -i "{}" -vn "{}"'.format(oldfilename, newfilename)
        os.system(cmd)
        return newfilename
    
    except:
        print("Connection Error")  # to handle exception


from youtubesearchpython import VideosSearch


def getAllVideos(url):
    print(url)
    # itemLinks = links2(url,payload)
    i = 0
    # itemLinks = []
    while True : #and i < 3: # for test.
        print('i=',i)
        pageUrl = url + '&page=' + str(i)
        i += 1
        itemPageLinks = links3(pageUrl,'searchPage' + str(i) + '.html')
        global finalLinks 
        if len(itemPageLinks) == 0: # page 77, empty search result
            print('page is empty: ', pageUrl)
            break 
        else:
            print('added itemlinks:',len(itemPageLinks))
    
    
    print('itemLinks num:',len(finalLinks))
        
    startHtml = '''
        <!DOCTYPE HTML>
        <html lang="en-US">
        <head>
        	<meta charset="UTF-8">
        	<title>Table</title>
        
        
        <style type="text/css">
        /* Border styles */
        #table-1 thead, #table-1 tr {
        border-top-width: 1px;
        border-top-style: solid;
        border-top-color: rgb(230, 189, 189);
        }
        #table-1 {
        border-bottom-width: 1px;
        border-bottom-style: solid;
        border-bottom-color: rgb(230, 189, 189);
        }
        
        /* Padding and font style */
        #table-1 td, #table-1 th {
        padding: 5px 10px;
        font-size: 12px;
        font-family: Verdana;
        color: rgb(177, 106, 104);
        }
        
        /* Alternating background colors */
        #table-1 tr:nth-child(even) {
        background: rgb(238, 211, 210)
        }
        #table-1 tr:nth-child(odd) {
        background: #FFF
        }
        
        </style>
        
        
        </head>
        
        <body>
        <table id="table-1"> <!-- Replace "table-1" with any of the design numbers -->
        <thead>
        <th>No.</th>
        <th>Title</th>
        <th>Price</th>
        <th>Item Link</th>
        <th>Video Link</th>
        <th>Audio Link</th>
        </thead>
        <tbody>'''
        
    endHtml ='</tbody></table></body></html>'
    wholeHtml = startHtml
    itemPairs = getItemVideoLinks(finalLinks) 

    j = 0
    for itemPair in itemPairs:
        j +=1
        itemLink = itemPair[0]
        VideoLinkList = itemPair[1]
        priceStr = itemPair[3]
        if len(VideoLinkList) == 1:
            VideoLinks = itemPair[1][0]
            moreLinkHtml = ''
        else:
            VideoLinks = itemPair[1][0] 
            moreLink = itemPair[1][1] 
            moreLinkHtml = '  <a href="' + moreLink + '"> More </a>'
            
        link = "https://www.youtube.com/watch?v=" + VideoLinkList[0]
        newfilename = downAudio(link)
        title = itemPair[2][0]
        print(title,VideoLinks)
        
        wholeHtml += '<tr><td>' + str(j) + '</td><td>' + title + '</td><td>' + priceStr + '</td><td><a href="' + itemLink + '" target="_blank">Item Homepage</a></td><td><a href="' + "https://www.youtube.com/watch?v=" + VideoLinks + '" target="_blank" >YouTube Video</a> ' + moreLinkHtml + '</td><td><a href="' + newfilename + '" target="_blank" >YouTube Audio </a>' + '  <audio controls><source src="' + newfilename + '" type="audio/mpeg">Audio </audio>' + moreLinkHtml + '</td></tr>'
    wholeHtml += endHtml
    saveFile(wholeHtml,'VideoLink.html')
        






