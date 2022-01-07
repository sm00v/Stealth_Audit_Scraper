from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import argparse
import os, sys

def create_profile():
    profile = webdriver.FirefoxProfile()
    if args.proxy is not None:
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.socks", args.proxy)
        profile.set_preference("network.proxy.socks_port", args.proxy_port)
        profile.set_preference("network.proxy.socks_remote_dns", True)
        profile.set_preference("browser.privatebrowsing.autostart", True)
        profile.update_preferences()
        return profile
    else:
        profile.set_preference("browser.privatebrowsing.autostart", True)
        profile.update_preferences()
        return profile

def load_browser():
    profile = create_profile()
    options = Options()
    options.headless = True # Disable this if you want to watch the magic.
    driver = webdriver.Firefox(options=options, firefox_profile=profile)
    return driver

def load_website(driver):
    try:
        print(f'[+] Attempting to visit {args.url}')
        print('[+] Clearing all cookies...')
        driver.delete_all_cookies()
        driver.get(f'{args.url}')
        time.sleep(5)
        drop_down_menu(driver)
    except Exception as e:
        sys.exit(f'[-] Failed loading browser at proxy config: {e}')

def drop_down_menu(driver):
    print('[+] Dropping down menu')
    #Click Active Directory
    driver.find_element_by_xpath(
        '/html/body/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[2]/table/tbody/tr[1]/td[1]/div').click();
    time.sleep(1);
    #Click Users
    driver.find_element_by_xpath(
        '/html/body/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[2]/table/tbody/tr[3]/td[2]/table/tbody/tr[1]/td[1]/div').click();
    time.sleep(1);
    #Click User Token
    driver.find_element_by_xpath(
        '/html/body/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[2]/table/tbody/tr[3]/td[2]/table/tbody/tr[10]/td[2]/table/tbody/tr/td[4]/span').click();
    time.sleep(1)
    driver.switch_to.frame(
        driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/div[2]/iframe'))
    enumerate_users(driver)

def enumerate_users(driver):
    # print('[+] Enumerating Users:')
    user_element = 2
    for users in range(2,12):
        user = driver.find_element_by_xpath(
            f'/html/body/table[2]/tbody/tr[2]/td/div/div/div[3]/div[2]/div/div[2]/table/tbody/tr[{user_element}]/td[2]').text
        nt_acc = driver.find_element_by_xpath(
            f'/html/body/table[2]/tbody/tr[2]/td/div/div/div[3]/div[2]/div/div[2]/table/tbody/tr[{user_element}]/td[3]').text
        print(f'NT_Account:{nt_acc}\tName:{user}')
        write_accounts(user, nt_acc)
        user_element+=1
    next_page(driver)

def next_page(driver):
    stop_nexting = str(driver.find_element_by_xpath(
        f'/html/body/table[2]/tbody/tr[2]/td/div/div/div[3]/div[3]/div/div/table/tbody/tr/td[1]/div/div[4]'
    ).get_attribute("class"))
    if 'dhxtoolbar_btn_dis' not in stop_nexting:
        driver.find_element_by_xpath(
            f'/html/body/table[2]/tbody/tr[2]/td/div/div/div[3]/div[3]/div/div/table/tbody/tr/td[1]/div/div[4]'
        ).click()
        enumerate_users(driver)
    else: print('[+] Got last page!');pass

def write_accounts(user, nt_acc):
    outfile = open(args.outfile, 'a')
    outfile.write(f'{nt_acc}:{user}')
    outfile.write('\n')

def argparser():
    parser = argparse.ArgumentParser(description="StealthAUDIT Scraper >:D")
    parser.add_argument("-o", "--outfile", help="The file to write users to.", default=f'{os.getcwd()}/ad_users.txt')
    parser.add_argument("-u", "--url", help="The webserver in format {http://10.0.0.1:80}.")
    parser.add_argument("-p", "--proxy", help="The proxy ip in format {10.0.0.1}.", default=None)
    parser.add_argument("-pp", "--proxy_port", type=int, help="The proxy port in format {1080}.", default=None)
    return parser.parse_args()

if __name__ == '__main__':
    args = argparser()
    driver = load_browser()
    load_website(driver)
    driver.quit()
    sys.exit('[+] Done!')
