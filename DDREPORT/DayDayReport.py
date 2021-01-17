'''
本脚本视为自愿行为，一切连带后果自行承担
使用步骤
1. 安装好python的环境
2. 安装splinter包---在cmd使用如下语句: pip install splinter
3. 下载并chromedriver
   * 要先去chrome设置里面看看你的chrome的版本号,driver版本和机器上装的chrome版本必须一致
   * chromedriver下载地址:https://sites.google.com/a/chromium.org/chromedriver/downloads
4. 下面这一行会调用你下载的chromedriver,你可以在c盘新建文件夹mypath然后把chromedriver.exe解压后丢进去,也可以自行设置路径
   * browser = Browser(driver_name='chrome',executable_path=r'C:\mypath\chromedriver.exe')
5. 把这个py脚本设置成开机执行.
'''
import time
from splinter import Browser

def baobao(xuehao,mima): 
   # 指定driver为chrome浏览器,指定driver位置
   browser = Browser(driver_name='chrome',executable_path='/bin/chromedriver')
   browser.visit('https://id.sspu.edu.cn/cas/login?service=https%3a%2f%2fhsm.sspu.edu.cn%2fselfreport%2fLoginSSO.aspx%3ftargetUrl%3d%7bbase64%7daHR0cHM6Ly9oc20uc3NwdS5lZHUuY24vc2VsZnJlcG9ydC9JbmRleC5hc3B4')
   browser.fill('username', xuehao) #你的学号
   browser.fill('password', mima) #你的密码

   button = browser.find_by_css('.submit_button')
   button.click() #登录
   links_found = browser.find_link_by_href('DayReportSelect.aspx')
   links_found.click() #进入每日一报
   browser.fill('p1$TiWen', '36') #填写体温 36
   button4 = browser.find_by_id('fineui_2-inputEl-icon')
   button4.click()
   button5 = browser.find_by_css('.f-field-body-checkboxlabel')
   button5.click(); # 我承诺，以下内容真实有效！

   button2 = browser.find_by_css('.f-btn-text')
   button2.click()#提交
   button3 = browser.find_by_id('fineui_37')
   button3.click()#本人承诺填写属实
   time.sleep(3)
   print("报道成功",xuehao)
   browser.quit() #退出浏览器

if __name__ == "__main__":
   we = [
      ['20171113336','Jinghaoyang1'],
      ['20171113205','zyw981220'],
      ['20171113435','berry981013']
   ]
   for person in we:
      baobao(person[0],person[1])

   # print(we[0][0],we[0][1])
   #  baobao(we[1][1],we[1][2])