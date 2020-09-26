from selenium import webdriver
import time
import pandas as pd

USER = "admin"
PASS = "Pm10924sd#1"

# Google Chromeを起動
browser = webdriver.Chrome()
browser.implicitly_wait(3)

url_login = "http://takeiteasyinamerica.com/wp-login.php"
browser.get(url_login)
time.sleep(1)
print("ログインページにアクセスしました")

# ログイン２ページ目に入る
browser_link = browser.find_element_by_class_name('jetpack-sso-toggle')
time.sleep(1)
browser_link.click()

# ユーザーIDを入力
element = browser.find_element_by_id('user_login')
element.clear()
element.send_keys(USER)

# パスワードを入力
element = browser.find_element_by_id('user_pass')
element.clear()
element.send_keys(PASS)
print("フォームを送信")

# ログインボタンをクリック
browser_from = browser.find_element_by_id('wp-submit')
time.sleep(1)
browser_from.click()
print("ログインボタンをクリック")

# 投稿一覧へアクセス
url = "http://takeiteasyinamerica.com/wp-admin/edit.php"
time.sleep(1)
browser.get(url)
print(url, "アクセス完了")

