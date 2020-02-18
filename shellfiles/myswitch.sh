#!/bin/bash
#在CASE变量小于等于20的时候一直运行
CASE=0                  #初始化变量
echo "case = $CASE"     #显示变量
while [ $CASE -le 20 ]  #while条件
do                      #while开始
CASE=`expr $CASE + 1`   #相当于CASE++
echo "case = $CASE"     #显示下CASE的值
done                    #结束