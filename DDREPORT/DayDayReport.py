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
import sys
import logging
from splinter import Browser
f = open("DDRPlog.txt", "a")   
sys.stdout=f

def baobao(xuehao,mima): 
   browser = Browser(driver_name='chrome',executable_path='/bin/chromedriver')   
   browser.visit('https://id.sspu.edu.cn/cas/login?service=https%3a%2f%2fhsm.sspu.edu.cn%2fselfreport%2fLoginSSO.aspx%3ftargetUrl%3d%7bbase64%7daHR0cHM6Ly9oc20uc3NwdS5lZHUuY24vc2VsZnJlcG9ydC9JbmRleC5hc3B4')
   browser.fill('username', xuehao) #你的学号
   browser.fill('password', mima) #你的密码

   button = browser.find_by_css('.submit_button')
   button.click() #登录
   links_found = browser.links.find_by_href('DayReportSelect.aspx')
   links_found.click() #进入每日一报
   button4 = browser.find_by_id('fineui_2-inputEl-icon')
   button4.click()
   browser.fill('p1$TiWen', '36') #填写体温 36
   button5 = browser.find_by_css('.f-field-body-checkboxlabel')
   button5.click(); # 我承诺，以下内容真实有效！

   button2 = browser.find_by_css('.f-btn-text')
   button2.click()#提交
   button3 = browser.find_by_id('fineui_37')
   button3.click()#本人承诺填写属实   # 指定driver为chrome浏览器,指定driver位置

   for waittime in range(30):
      time.sleep(5)

      if browser.is_element_present_by_text('提交成功(Submit successfully)') :
         print('成功：',xuehao)
         break
      elif browser.is_element_present_by_text('请求超时，请刷新页面并重试！'):
         # 遇到这种情况，刷新页面，重新填表提交
         browser.reload()
         button = browser.find_by_css('.submit_button')
         button.click() #登录
         links_found = browser.links.find_by_href('DayReportSelect.aspx')
         links_found.click() #进入每日一报
         button4 = browser.find_by_id('fineui_2-inputEl-icon')
         button4.click()
         browser.fill('p1$TiWen', '36') #填写体温 36
         button5 = browser.find_by_css('.f-field-body-checkboxlabel')
         button5.click(); # 我承诺，以下内容真实有效！
         button2 = browser.find_by_css('.f-btn-text')
         button2.click()#提交
         button3 = browser.find_by_id('fineui_37')
         button3.click()#本人承诺填写属实   # 指定driver为chrome浏览器,指定driver位置
      else :
         print('*加载',xuehao,'等待次数：', waittime+1)
   time.sleep(3)
   print("--退出浏览器--")
   
   browser.quit() #退出浏览器

if __name__ == "__main__":
   localtime = time.asctime( time.localtime(time.time()) )
   print(localtime)
   we = [
      ['20171113336','Jinghaoyang1'],
      ['20171113205','zyw981220'],
      ['20171113435','berry981013']
   ]
   for person in we:
      baobao(person[0],person[1])
      
      # f.writelines('hihihi')
   print("finish-\n")
