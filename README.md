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
 > import time
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

## 0504新增
* 增加日志模块，丰富输出功能  
   > 示例如下：  
   > Mon, 04 May 2020 21:06:30-common.mainModule-TestSearch.py-[line:30]-INFO-[日志信息]: 配置初始化  
   > Mon, 04 May 2020 21:06:30-common.mainModule-TestSearch.py-[line:32]-INFO-[日志信息]: 开始运行代码  
   > Mon, 04 May 2020 21:06:35-common.mainModule-TestSearch.py-[line:19]-INFO-[日志信息]: 驱动信息：<selenium.webdriver.chrome.webdriver.WebDriver (session="5cb4a11875146327bb5e764d67736d67")>  
   > Mon, 04 May 2020 21:06:37-common.mainModule-BasePage.py-[line:77]-INFO-[日志信息]: 打开网址：https://www.baidu.com  
   > Mon, 04 May 2020 21:06:37-common.mainModule-BasePage.py-[line:64]-INFO-[日志信息]: 等待元素：id,kw  
   > Mon, 04 May 2020 21:06:37-common.mainModule-BasePage.py-[line:91]-INFO-[日志信息]: 获取元素：id,kw  
   > Mon, 04 May 2020 21:06:37-common.mainModule-BasePage.py-[line:127]-INFO-[日志信息]: 向元素 id,kw 输入文字：温一壶清酒 博客园  
   > Mon, 04 May 2020 21:06:37-common.mainModule-BasePage.py-[line:64]-INFO-[日志信息]: 等待元素：id,su  
   > Mon, 04 May 2020 21:06:37-common.mainModule-BasePage.py-[line:91]-INFO-[日志信息]: 获取元素：id,su  
   > Mon, 04 May 2020 21:06:38-common.mainModule-BasePage.py-[line:201]-INFO-[日志信息]: 点击元素：id,su  
   > Mon, 04 May 2020 21:06:40-common.mainModule-BasePage.py-[line:364]-INFO-[日志信息]: 等待2秒  
   > Mon, 04 May 2020 21:06:43-common.mainModule-BasePage.py-[line:360]-INFO-[日志信息]: 关闭页面   
     
* 增加全局配置模块，将driver设置为全局变量  
   > get_value('driver')  # 从全局变量取driver  
   > set_value('driver', driver) # 设置全局变量

* 丰富BasePage基础类，增加日志输出  
* 引入PO模式  
* 新增SearchPage.py，分离搜索页中的元素定位

## 0516新增
* 修改用例入参方式
* 增加断言

## 0523新增
* 引入conftest.py文件
  >分离用例运行前和运行后的操作  
  >
  >fixture里面有个scope参数可以控制fixture的作用范围：session>module>class>function
  >
  >-function：每一个函数或方法都会调用
  >
  >-class：每一个类调用一次，一个类中可以有多个方法
  >
  >-module：每一个.py文件调用一次，该文件内又有多个function和class
  >
  >-session：是多个文件调用一次，可以跨.py文件调用，每个.py文件就是module
  
## 0530新增
* 引入标记测试
* 引入pytest.ini配置文件

## 0531新增
* 引入pytest-html，增加测试报告展示
* 优化html测试报告样式，增加错误截图

## 0607新增
* 引入parametrize参数化
* 优化测试报告
* 解决测试报告乱码

## 0608新增
* 增加邮件发送功能

## 0621新增
* 增加读取excel文件中的测试数据，实现参数化
* 增加失败用例重跑 
> '--reruns', '1'

## 0705新增
* 单独封装参数化ids属性
* 单独封装获取excel数据类

## 0719新增
* 优化excel读取数据-----支持合并单元格数据的读取

## 0727新增
* 增加allure测试报告
* conftest文件中增加函数pytest_collection_modifyitems，解决控制台乱码问题

## 0730新增
* 增加测试报告文件支持打压缩包并发送到邮箱

## 0809新增
* 增加argprase类，支持自定义命令行参数