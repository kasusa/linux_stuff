* [sumatra PDF(pdf阅读器)](https://www.sumatrapdfreader.org/free-pdf-reader.html)
* [官方培训课程](https://www.linuxprobe.com/training)
* [电子书](https://pan.baidu.com/s/1plj-7aoB7E0GF1PfjKb5qw)
提取码：65x8 

## 控制台常用快捷键
按键 | 作用
---|---
Ctrl+d | 键盘输入结束或退出终端
Ctrl+s | 暂停当前程序，暂停后按下任意键恢复运行
Ctrl+z | 将当前程序放到后台运行，恢复到前台为命令fg
Ctrl+a | 将光标移至输入行头，相当于Home键
Ctrl+e | 将光标移至输入行末，相当于End键
Ctrl+k | 删除从光标所在位置到行末
Alt+Backspace	| 向前删除一个单词
Shift+PgUp	| 将终端显示向上滚动
Shift+PgDn	| 将终端显示向下滚动

## 一次性创建多个文件
```
$ touch love_{1..10}_shiyanlou.txt
```

## 常用通配符

字符 |	含义
---|---
* |	匹配 0 或多个字符
? |	匹配任意一个字符
[list] |	匹配 list 中的任意单一字符
[^list] |	匹配 除 list 中的任意单一字符以外的字符
[c1-c2] |	匹配 c1-c2 中的任意单一字符 如：[0-9][a-z]
{string1,string2,...} |	匹配 string1 或 string2 (或更多)其一字符串
{c1..c2} |	匹配 c1-c2 中全部字符 如{1..10}

## 创建和切换用户
创建用户(默认会让输入密码)
```
sudo adduser <USERNAME>
```
修改密码
```
sudo passwd <USERNAME>
```
切换用户
```
su <USERNAME>
```
查看当前用户是谁
```
whoami
```
查看用户组
```
cat /etc/group | grep -E "<USERNAME>"
```
给新建的用户sudo权限
```
usermod -G sudo <USERNAME>
```
删除用户(把它创建时自动创建的用户目录一并删除)
```
sudo deluser lilei --remove-home
```
 **adduser 和 useradd 的区别是什么**

> 答：useradd 只创建用户，不会创建用户密码和工作目录，创建完了需要使用 passwd <username> 去设置新用户的密码。adduser 在创建用户的同时，会创建工作目录和密码（提示你设置），做这一系列的操作。其实 useradd、userdel 这类操作更像是一种命令，执行完了就返回。而 adduser 更像是一种程序，需要你输入、确定等一系列操作
## 文件和权限
![图像权限](https://doc.shiyanlou.com/linux_base/3-10.png/wm)
这个图是在使用`ls -l`时候前部的意义。
使用chmod可以修改权限。每一个数字代表对应权限
```
rwx|r-x|r-x
111|101|101 = 755
```

## 配置主机名称
`4.1.2 配置主机名称`
1. 使用 Vim 编辑器修改“/etc/hostname”主机名称文件。
2. 把原始主机名称删除后追加你想要起的名字。注意，使用 Vim 编辑器修改主机名称文件后，要在末行模式下执行:wq!命令才能保存并退出文档。
3. 保存并退出文档，然后使用 hostname 命令检查是否修改成功。
> 不好用的时候试着重新启动

## man 命令中常用按键以及用途

按键 |用途
---|---
空格键 | 向下翻一页
/ |从上至下搜索某个关键词，如“/linux”
? |从下至上搜索某个关键词，如“?linux”
n | 定位到下一个搜索到的关键词
N | 定位到上一个搜索到的关键词

# 系统状态
## ps aux命令
状态值|意义
---|---
R（运行）| 进程正在运行或在运行队列中等待。
S（中断）| 进程处于休眠中，当某个条件形成后或者接收到信号时，则脱离该状态。
D（不可中断）| 进程不响应系统异步信号，即便用 kill 命令也不能将其中断。
Z（僵死）| 进程已经终止，但进程描述符依然存在, 直到父进程调用 wait4()系统函数后将进程释放。
T（停止）| 进程收到停止信号后停止运行。

如果我们在系统终端中执行一个命令后想立即停止它，可以同时按下 ` Ctrl + C` 组合
键（生产环境中比较常用的一个快捷键），这样将立即终止该命令的进程。或者，如果
有些命令在执行时不断地在屏幕上输出信息，影响到后续命令的输入，则可以在执
行命令时在末尾添加上一个 `&` 符号，这样命令将进入系统后台来执行。

## ifconfig 命令
ifconfig 命令用于获取网卡配置与网络状态等信息，格式为“ifconfig [网络设备] [参数]”。使用 ifconfig 命令来查看本机当前的网卡配置与网络状态等信息时，其实主要查看的就是网卡名称、inet 参数后面的 IP 地址、ether 参数后面的网卡物理地址（又称为 MAC 地址）

## uptime 命令
uptime 用于查看系统的负载信息，格式为 uptime。

uptime 命令真的很棒，它可以显示当前系统时间、系统已运行时间、启用终端数量以及平均负载值等信息。平均负载值指的是系统在最近 1 分钟、5 分钟、15 分钟内的压力情况（下面加粗的信息部分）；负载值越低越好，尽量不要长期超过 1，在生产环境中不要
超过 5。

## uname -a
查看计算机的系统类型
## free -h
查看内存
## last 命令
last 命令用于查看所有系统的登录记录，格式为“last [参数]”。
## history
查看历史命令记录。
`history -c` 清空记录

# 切换目录
## pwd 命令
pwd 命令用于显示用户当前所处的工作目录，格式为“pwd [选项]”。
## cd 命令
cd| 命令用于切换工作路径，格式为“cd [目录名称]”。
---|---
`cd -` |命令返回到上一次所处的目录
`cd ..` |命令进入上级目录
`cd ~` |命令切换到当前用户的家目录，亦或使用
`cd ~username` |切换到其他用户的家目录。

## ls
命令|~
---|---
ls -a  | 查看隐藏文件
ls -l  | 查看文件详细信息
ls -la | 查看隐藏文件以及显示详细

# 查看文件
## cat 命令
用来查看比较小的文本文件

`cat -n`  查看文本内容时还想顺便显示行号

## more 命令
more 命令用于查看纯文本文件（内容较多的），格式为“more [选项]文件”。
如果需要阅读长篇小说或者非常长的配置文件，那么“小猫咪”可就真的不适合了。因
为一旦使用 cat 命令阅读长篇的文本内容，信息就会在屏幕上快速翻滚，导致自己还没有来得及看到，内容就已经翻篇了。因此对于长篇的文本内容，推荐使用 more 命令来查看。

more命令会在最下面使用百分比的形式来提示您已经阅读了多少内容。

您还可以使用空格键或回车键向下翻页：

## head 命令
head 命令用于查看纯文本文档的前 N 行，格式为“head [选项] [文件]”。
在阅读文本内容时，谁也难以保证会按照从头到尾的顺序往下看完整个文件。如果只想
查看文本中前 20 行的内容，该怎么办呢？

head 命令可以派上用场了：` head -n 20 txt` 或者 `head -20 txt`

## tail 命令
tail 命令用于查看纯文本文档的后 N 行或持续刷新内容，格式为“tail [选项] [文件]”。

比如需要查看文本内容的最后 20 行，只需要执行“`tail -n 20 文件名`”

就可以达到这样的效果。tail 命令最强悍的功能是可以持续刷新一个文件的内容，当想要实时
查看最新日志文件时，这特别有用，此时的命令格式为“`tail -f 文件名`”：

## wc 命令
wc 命令用于统计指定文本的行数、字数、字节数，格式为“wc [参数] 文本”。

` file` 命令来查看文件类型

## 压缩
`tar -czvf 压缩包名称.tar.gz 要打包的目录`

## 搜索
`grep` 命令用于在文本中执行关键词搜索，并显示匹配的结果

~|~
---|---
 -b    |将可执行文件（binary）当作文本文件（text）来搜索
 -c    |仅显示找到的行数
 -i    |忽略大小写
 -n    |显示行号
 -v    |反向选择 — 仅列出没有“关键词”的行

```
root@iZ2ze1hf17j9hv44rdpmaaZ:~# grep -n Jan you
2:-rw-r--r-- 1 root root   17 Jan 12  2000 kasusa
3:drwxr-xr-x 2 root root 4096 Jan 30 10:15 mydir
4:drwxr-xr-x 2 root root 4096 Jan 30 10:16 mydir2
5:drwxr-xr-x 2 root root 4096 Jan 30 11:47 ooo
6:-rw-r--r-- 1 root root    0 Jan 30 11:51 you 

# you是一个文件。用显示行号的模式在you里面寻找 Jan 关键字 。在控制台里面会有高亮显示

```

## 别名
可以用 `alias` 命令来创建一个属于自己的命令别名，格式为“`alias 别名=命令`”。

若要取消一个命令别名，则是用 unalias 命令，格式为“unalias 别名”。

## 变量和全局
一般来说，变量都是用大写的。

有一些|常用的全局变量：
---|---
HOME |用户的主目录（即家目录）
SHELL| 用户在使用的 Shell 解释器名称
HISTSIZE |输出的历史命令记录条数
HISTFILESIZE |保存的历史命令记录条数
MAIL |邮件保存路径
LANG |系统语言、语系名称
RANDOM |生成一个随机数字
PS1 Bash |解释器的提示符
PATH |定义解释器搜索用户执行命令的路径
EDITOR |用户默认的文本编辑器

自己创建一个变量/读取它：
```
root@iZ2ze1hf17j9hv44rdpmaaZ:~# MYVAR="hello"
root@iZ2ze1hf17j9hv44rdpmaaZ:~# echo "$MYVAR"
hello
```

提升位全局变量：
```
root@iZ2ze1hf17j9hv44rdpmaaZ:~# export MYVAR
```

# VIM

## Vim 中常用的命令

命令| 作用
---|---
dd  |删除（剪切）光标所在整行
5dd |删除（剪切）从光标处开始的 5 行
yy |复制光标所在整行
5yy |复制从光标处开始的 5 行
n |显示搜索命令定位到的下一个字符串
N |显示搜索命令定位到的上一个字符串
u |撤销上一步的操作
p |将之前删除（dd）或复制（yy）过的数据粘贴到光标后面



## 末行模式中可用的命令
**要想切换到末行模式，在命令模式中输入一个冒号就可以了。**
末行模式主要用于保存或退出文件，以及设置 Vim 编辑器的工作环境，还可以让用户执
行外部的 Linux 命令或跳转到所编写文档的特定行数。

命令 |作用
---|---
:w |保存
:q |退出
:q!|强制退出（放弃对文档的修改内容）
:wq!| 强制保存退出
:set| nu 显示行号
:set| nonu 不显示行号
:命令| 执行该命令
:整数| 跳转到该行
:s/one/two |将当前光标所在行的第一个 one 替换成 two
:s/one/two/g |将当前光标所在行的所有 one 替换成 two
:%s/one/two/g |将全文中的所有 one 替换成 two
?字符串 |在文本中从下至上搜索该字符串
/字符串 |在文本中从上至下搜索该字符串

