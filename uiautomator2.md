# UIAutomator2

###### recode by samuel

### 1. 安装，配置环境
* 添加库
```
# 添加uiautomator2库
pip install uiautomator2

# 添加weditor工具
pip install weditor
```
* 安装adb，配置环境变量

* 连接手机，打开开发者选项，启动USB调试

* 手机安装atx-agent
```
python -m uiautomator2 init
```

* uiautomator连接手机
```python
import uiautomator2 as u2
# 默认连接
d = u2.connect()

# adb获取手机序列号: adb devices
# 通过deviceid连接设备
d = u2.connect('e7cddcd4')

# adb获取手机IP地址： adb shell netcfg
# 通过IP地址连接设备
d = u2.connect('http://172.17.99.15:24')

# 通过wifi地址连接设备
d = u2.connect_wifi('127.0.0.1:62001')

print(d.device_info)
```
##
### 2. 获取信息

* 获取设备信息（返回一个包含设备详情的字典）
```python
d.device_info
```

* 获取屏幕尺寸
```
# uiautomator2方法实现（返回一个包含屏幕尺寸数据的元组）
    d.window_size()

# adb shell wm size
```

* 获取当前设备运行中的包名和activity
```
# uiautomator2方法实现(返回一个包含package和activity的字典)
    d.app_current()

# adb shell "dumpsys window | grep mCurrentFocus"
```

* 获取所有正在运行的包名
```python
#返回一个包含package的列表
    d.app_list_running()
```
##
### 3. 基础操作

* 安装应用
```python
# 安装线上apk链接
url = 'https://dl.hdslb.com/mobile/latest/iBiliPlayer-bili.apk?t=1598337629000&spm_id_from=333.47.b_646f776e6c6f61642d6c696e6b.1'
d.app_install(url)

# 安装本地apk
from os import popen
apk_path = r"D:\test_apk\iBiliPlayer-bili.apk"
p = popen('adb install {}'.format(apk_path))
print(p.read())
```

* 卸载应用
```python
pkg = 'tv.danmaku.bili'
d.app_uninstall(pkg)
```

* 启动应用
```python
pkg = 'tv.danmaku.bili'
d.app_start(pkg)
```

* 关闭应用
```python
pkg = 'tv.danmaku.bili'
d.app_stop(pkg)

# adb shell am force-stop tv.danmaku.bili
```

* 清除应用数据
```python
pkg = 'tv.danmaku.bili'
d.app_clear(pkg)

# adb shell pm clear tv.danmaku.bili
```
##
### 4.文件操作
* 从手机提取文件
```python
save_file = r'd:/demo.txt'
file_path = '/sdcard/data/android/demo.txt'
d.pull(file_path, save_file)

#adb pull /sdcard/data/android/demo.txt d:/demo.txt
```

* 推送文件到电脑
```python
file_path = r'd:/demo.txt'
locator = '/sdcard/data/android'
d.push(file_path, locator)

# adb push d:/demo.txt /sdcard/data/android
```
##
### 5. 物理按键操作
```python
# 亮屏
d.screen_on()

# 熄屏
d.screen_off()

# 静音键
d.press('volume_mute')

# 增大音量键
d.press('volume_up')

# 减小音量键
d.press('volume_down')

# home键
d.press('home')

# back键
d.press('back')

# 电源键
d.press('power')

# camera键
d.press('camera')

# menu键
d.press('menu')

#...
```
##
### 6. 元素定位

* 根据元素属性定位
```python
element = d(resourceId="tv.danmaku.bili:id/agree")
```
* 根据层级关系定位
```python
element = d.xpath()
```

* 根据坐标点击



##
### 7. 元素操作
































