# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:49:15 2020

@author: MyFirstLaptop
"""

import requests
from bs4 import BeautifulSoup

pathOfWriteData = 'C:\\Big Data\\BD_CA_1_Output_{0}.csv'
def get_website_content():
    
    cookies = {
            'utag_main': 'v_id:017121d3ceaa00346de95bf53ec80104e003000d0086e$_sn:1$_ss:0$_st:1585412267234$ses_id:1585410461360%3Bexp-session$_pn:3%3Bexp-session',
            'CONSENTMGR': 'ts:1585410463263%7Cconsent:true',
            '_ga': 'GA1.2.297745672.1585410466',
            '_gid': 'GA1.2.351346067.1585410466',
            '_y2': '1%3AeyJjIjp7IjEzMjA1MSI6LTE0NzM5ODQwMDAsIm8iOi0xNDczOTg0MDAwfX0%3D%3ALTE0NzEzNjMxNjg%3D%3A2',
            '_yi': '1%3AeyJsaSI6bnVsbCwic2UiOnsiYyI6MSwibGEiOjE1ODU0MTA2MzMxODAsInAiOjEsInNjIjoxNTl9LCJ1Ijp7ImlkIjoiZTdmN2U1NzQtMzllZC00NmU1LWFmNjktYTc2MDNmMmZlZGJjIiwiZmwiOiIwIn19%3ALTE0MzE4NDYxMTI%3D%3A2',
    }
        
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-GB,en;q=0.5',
            'Referer': 'https://www.google.com/',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0',
            'TE': 'Trailers',
    }
        
    params = (
            ('from', 'EUR'),
            ('amount', '1'),
    )
        
    response = requests.get('https://www.x-rates.com/table/', headers=headers, params=params, cookies=cookies)
    return response
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.x-rates.com/table/?from=EUR&amount=1', headers=headers, cookies=cookies)
def save_csv(commits,title,lastUpdated):    
    csv_file = open(pathOfWriteData.format(lastUpdated.split(',')[0]), 'w')
    csv_file.write('Exchange Rate,' + title + '\n')
    csv_file.write('Updated at ,' + lastUpdated + '\n')
    csv_file.write('\n')
    csv_file.write('\n')
    csv_file.write('Country,EuroVsOtherCurrency,OtherCurrencyVsEuro\n')
    for commit in commits:        
        csv_file.write(str(commit))
    csv_file.close()

def extract_html_content():
    html = get_website_content()
    html_data = BeautifulSoup(html.content, "html.parser")
    tables = html_data.find_all("tbody")
    for table in tables:
        cells = table.find_all('td')
        currencyDetail = []
        row = ''
        for cell in cells:
            value = str(cell.text).strip().replace('\n', '')
            if len(value) == 0:
                print('"0"', end=',')
            elif value[0].lower() in 'abcdefghijklmnopqrstuvwxyz<':
                currencyDetail.append(row)
                row = ''
                row = '\n' + value + ','            
            else:
                row += value + ','
        title = html_data.find("span", {"class": "OutputHeader"})
        last_update = html_data.find("span", {"class": "ratesTimestamp"})
        save_csv(currencyDetail,title.text,last_update.text)

def main():
    extract_html_content()

main()