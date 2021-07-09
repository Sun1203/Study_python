import pandas as pd
from selenium import webdriver 
from bs4 import BeautifulSoup 
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json



from matplotlib import font_manager, rc
import platform


def scrape():

    if platform.system() == 'Windows':
        path = 'c:/Windows/Fonts/malgun.ttf'
        font_name = font_manager.FontProperties(fname = path).get_name()
        rc('font', family = font_name)
    elif platform.system() == 'Darwin':
        rc('font', family = 'AppleGothic')
    else:
        print('Check your OS system')




    browser = webdriver.Chrome('c:/driver/chromedriver.exe')
    url = "https://youtube-rank.com/board/bbs/board.php?bo_table=youtube" 
    browser.get(url)
    browser.find_element_by_link_text("음식/요리/레시피").click()

    try:

        html = browser.page_source
        soup = BeautifulSoup(html, 'html.parser')

        channel_list = soup.select('form > table > tbody > tr')
        channel = channel_list[0]


        results = []
        lst = []
        for page in range(1,11):
            url = f"https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&sca=%EC%9D%8C%EC%8B%9D%2F%EC%9A%94%EB%A6%AC%2F%EB%A0%88%EC%8B%9C%ED%94%BC&page={page}" 
            browser.get(url)
            time.sleep(2)
            html = browser.page_source
            soup = BeautifulSoup(html, 'html.parser')
            channel_list = soup.select('form > table > tbody > tr')
            for channel in channel_list:
                title = channel.select('h1 > a')[0].text.strip() 
                category = channel.select('p.category')[0].text.strip()
                subscriber = channel.select('.subscriber_cnt')[0].text 
                view = channel.select('.view_cnt')[0].text
                video = channel.select('.video_cnt')[0].text
                data = [title, category, subscriber, view, video]
                results.append(data)
                lst.append({"타이틀":title, "구독자":subscriber, "뷰":view})
            # print(lst)
    except Exception as e:
        print("page parseing error", e)
    finally:
        time.sleep(10)
        browser.close()
        
    return lst



def js():

    df = pd.read_excel('.\\files\\youtube_rank1.xlsx')
    df = df.head(5)
    
    df['replaced_subscriber'] = df['subscriber'].str.replace('만', '0000')
    df.view = df.view.apply(lambda x : x.replace('억', ''))
    df.view = df.view.apply(lambda x : x.replace('만', ''))
    df.video = df.video.apply(lambda x : x.replace('개', ''))
    df.video = df.video.apply(lambda x : x.replace(',', ''))

    df['replaced_subscriber'] = df['replaced_subscriber'].astype('int')
    df.view = df['view'].astype(int)
    df.video = df['video'].astype(int)

    print(df)

    sns.barplot(data=df, x="title", y="replaced_subscriber")
    # plt.savefig('./static/images/chart01.png')





    pivot_df = df.pivot_table(index = 'title', values = 'replaced_subscriber', aggfunc = ['sum','count'])

    pivot_df.columns = ['subscriber_sum', 'category_count']

    pivot_df = pivot_df.reset_index()

    pivot_df = pivot_df.sort_values(by='subscriber_sum', ascending=False)
    # print(type(pivot_df))       # <class 'pandas.core.frame.DataFrame'>
    # print(pivot_df)

    pivot_df = pivot_df.to_json(orient="records")    
    # print(type(pivot_df))      # str
    
    parsed = json.loads(pivot_df)
    # print(type(parsed))       # dict
    # print(parsed)
    
    lee = json.dumps(parsed, indent=4, ensure_ascii=False)
    # print(type(lee))    # 'str'
    # print(lee)
    
    # plt.figure(figsize = (30,10))
    # plt.pie(pivot_df['subscriber_sum'], labels=pivot_df['title'], autopct='%1.1f%%')
    # plt.show()
    return lee


