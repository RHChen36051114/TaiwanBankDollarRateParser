import requests as r
from bs4 import BeautifulSoup
#import time as t


def main () :

    #date_t = t.strftime ("%Y-%m-%d %H:%M:%S")

    def get_web_page (url_) :
        resp = r.get (url = url_) # useful cmd 1

        #resp.encoding = 'gbk'
        resp.encoding = resp.apparent_encoding # useful cmd 2

        if resp.status_code != 200 :
            print ('Invalid url : ', resp.url)
            return "-1"
        else :
            return resp.text # useful cmd 3


    url = "http://rate.bot.com.tw/xrt?Lang=zh-TW"
    page = get_web_page (url)
    soup = BeautifulSoup (page, 'html.parser')

    country = []
    cashRate = []
    sightRate = []

    # Grasp needed xml contents
    updateTime = str(soup.find ('span', {'class':'time'})).split('>')[1].split('<')[0]
    cty = soup.findAll ('div', {'class':'visible-phone print_hide'})
    cash = soup.findAll ('td', {'class':'rate-content-cash text-right print_hide'})
    sight = soup.findAll ('td', {'class':'rate-content-sight text-right print_hide'})

    # Pruning labels
    for ct in cty :
        country.append (str(ct).split('>')[1].split('<')[0].strip())
    for ca, si in zip(cash, sight) :
        cashRate.append (str(ca).split('>')[1].split('<')[0])
        sightRate.append (str(si).split('>')[1].split('<')[0])

    # Output to file
    fw = open ('DollarRate.csv', 'a')

    # Only for first time
    fw.write (',')
    for cnt in country :
        fw.write (cnt)
        fw.write (',')
        fw.write (',')
        fw.write (',')
        fw.write (',')
    fw.write ('\n')
    fw.write (',')
    for cnt in range(len(country)) :
        fw.write ('Cash In')
        fw.write (',')
        fw.write ('Cash Out')
        fw.write (',')
        fw.write ('Sight In')
        fw.write (',')
        fw.write ('Sight Out')
        fw.write (',')
    fw.write ('\n')

    # For each time
    fw.write (updateTime)
    fw.write (',')
    for cnt in range(0, len(cashRate), 2) :
        fw.write (cashRate[cnt])
        fw.write (',')
        fw.write (cashRate[cnt+1])
        fw.write (',')
        fw.write (sightRate[cnt])
        fw.write (',')
        fw.write (sightRate[cnt+1])
        fw.write (',')
    fw.write ('\n')

    fw.close()


if __name__ == "__main__" :
    main ()

