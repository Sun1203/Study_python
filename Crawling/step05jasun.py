import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome("C:/driver/chromedriver")
driver.get("http://tour.interpark.com/")
time.sleep(3)

elem = driver.find_element_by_id("SearchGNBText")
elem.clear()
elem.send_keys("치킨")

btn_search = driver.find_element_by_css_selector("button.search-btn")
btn_search.click()


# div.searchSct > categoryAtc > li > link
# driver.find_element_by_css_selector("div.searchSct > categoryAtc > li > link").click()
driver.find_element_by_link_text("상품").click()

try:
    # for page in range(1, 6):
        # print("============================== ", page)
        # driver.execute_script("searchModule.SetCategoryList({}, '')".format(page))
    soup = BeautifulSoup(driver.page_source, "lxml" )
    goods = soup.select(".AdvertisingList > .productImgList > ul > .goods")
    # print(goods)

    for good in goods:
        img_src = good.find("img")["src"]
        # print(img_src)
        link = good.find("a")["href"]
        # print(link)
        title = good.find("img")["alt"]
        # print(title)
        price = good.find("a")["data-item_price"]




        print("썸네일=", img_src)
        print("\n")
        print("link=", link)
        print("\n")
        print("title=", title)
        print("\n")
        print("price=", price)
        print("="*100)

except Exception as e:
    print("page parseing error", e)
finally:
    time.sleep(50)
    driver.close()

