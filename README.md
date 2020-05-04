# 自动化测试框架搭建前提
* selenium 3.14.1
 > pip install selenium

* pytest 5.2.0
 > pip install pytest

* python 3.7.0
 > 安装步骤见博文：[python安装]()

* 浏览器驱动
 > UI自动化，需要配置浏览器驱动环境，驱动配置见博文：[浏览器驱动](https://www.cnblogs.com/hong-fithing/p/7623838.html)

* APP自动化
 > 配置APPIUM环境，详解参见博文：[appium环境搭建](https://www.cnblogs.com/hong-fithing/p/11475812.html)

## 0502新增
1. 新建项目Pytest_Auto_Test
2. 编写线性脚本，访问百度并搜索 温一壶清酒 博客园  
 > 示例代码如下：
 > 
 > ```
 >'''  
 >@author: wenyihuqingjiu  
 >@project: Pytest_Auto_Test  
 >@file: run.py  
 >@time: 2020-05-02 21:05  
 >@desc:  
 >'''  
 >
 > from selenium import webdriver  
 >import time
 > 
 > driver = webdriver.Chrome()  
 > driver.maximize_window()  
 > driver.get('https://www.baidu.com')  
 > driver.find_element_by_id('kw').send_keys('温一壶清酒 博客园')  
 > driver.find_element_by_id('su').click()  
 > time.sleep(2)  
 > driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()
 > time.sleep(3)  
 > driver.quit()  
 > ```  

## 0503新增
1. 封装BasePage基础类
2. 新增TestSearch.py文件，引入pytest运行case  
   > pytest注意点：  
   > 测试文件的文件名必须以"test_"开头，或者以"_test"结尾  
   > 测试类命名必须以"Test"开头  
   > 测试函数名必须以"test"开头  
   > 测试类里面不能使用"__init__"方法