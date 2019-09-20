1、setting.py 配置一些多账户信息以及多设备匹配的手机UDID以及多线程生成的对应PORT
2、run_test.py 程序入口获取多设备 多线程分配新建appim server 4700-4900 组合allure 
3、执行结束可以使用create_allure.bat & create_allure_open.bat 执行生成报告
4、根据自己的App包名启动页修改base_driver；


项目框架内部：
driver包存放appium driver
service包含CMD获取设备 启动appuim 服务以及端口
utils包含日志和报错截图封装
test_app包存放关于APP测试的用例根据需要编写
test_case存放单独需要调试的测试方法
page包存放APP页面模块包含当前页面点击以及其他的业务需要继承base_page(可以自己拓展)
initElement文件 是懒人文件之前用来直接调用driver去执行  维护APP 所有元素属性

安装requment.txt里面的第三方包
selenium==3.14.1
Appium-Python-Client
PyYAML
pytest
allure-pytest
allure-2.7 压缩包 bin路徑需要配置path

常用命令

adb devices
adb kill-server
adb shell "dumpsys window w | grep name="  (获取当前页面的Activity)

运行appium服务器（带有日志形式,no-reset形式,多设备时指定连接设备）
appium --address 0.0.0.0 --port 4723 --log "appium.log" --log-timestamp --local-timezone --no-reset --session-override -U 192.168.56.101:5555
编写用例： 路径： 项目/test_用例组名.py
上下文：
默认必有py文件 conftest*，这是pytest运行时的上下文环境（setup、teardown）,导入的base.conftest
原理通过pytest.fixture装饰器从而不同作用域下实现setup、teardown， 已加载 初始化环境、driver的运行环境、用例日志
用例组文件下编写用例集合类(test_用例集名)，编写用例方法（test_用例名）
