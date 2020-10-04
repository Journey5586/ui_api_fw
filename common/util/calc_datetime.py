# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2019-11-19 20:10
@Author: guozg 
@File：calc_datetime.py
@Description: 
1.
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""
from datetime import datetime
from datetime import date

class CalcDateTime():


    def getCurrentDate(self):
        """
        获取当前客户端的日期，格式为 2017-01-01  \n
        :return: str类型(当前日期)
        """
        # curdate = time.strftime("%Y-%m-%d")
        # return curdate
        curdate = date.strftime(datetime.now(), "%Y-%m-%d")
        return curdate

    def getCurTimeToHour(self):
        """
        获取当前客户端时间，到小时，不包括分钟和秒，格式为：2018-01-01 13  \n
        :return: str类型(不包括分钟和秒的当前客户端时间，24小时制)
        """
        # curtime = time.strftime("%Y-%m-%d %H")
        # return curtime
        curtime = datetime.strftime(datetime.now(), "%Y-%m-%d %H")
        return curtime

    def getCurTimeToMin(self):
        """
        获取当前客户端的时间,到分钟，不包含秒，格式为：2018-01-01 13:10  \n
        :return: str类型(不包含秒的当前客户端时间，24小时制)
        """
        # curtime = time.strftime("%Y-%m-%d %H:%M")
        # return curtime
        curtime = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M")
        return curtime

    def getCurTimeToSec(self):
        """
        获取当前客户端的时间，到秒，包含秒，格式为：2018-01-01 13:10:10  \n
        :return: str类型(包含秒的当前客户端时间，24小时制)
        """
        # curtime = time.strftime("%Y-%m-%d %H:%M:%S")
        # return curtime
        curtime = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        return curtime

    def strToTime(self, strtime):
        """
        将传入的时间字符串格式化为对应的时间对象,最后返回的格式为%Y-%m-%d %H:%M:%S  \n
        如：2017-01-09 12:30:40  \n
        :param strtime: 时间字符串
        :return: str类型(格式化为%Y-%m-%d %H:%M:%S(2018-01-05 21:13)的时间对象)
        """
        # 到秒钟的格式 2018-01-01 12:30:30
        if strtime.count(":") == 2 and strtime.count("-") == 2:
            Otime = datetime.strptime(strtime, "%Y-%m-%d %H:%M:%S")
        # 到分钟的格式 2018-01-01 12:30
        elif strtime.count("-") == 2 and strtime.count(":") == 1:
            Otime = datetime.strptime(strtime, "%Y-%m-%d %H:%M")
        # 到小时的格式 2018-01-01 18
        elif strtime.count("-") == 2 and strtime.count(":") == 0 and strtime.count(" ") == 1:
            Otime = datetime.strptime(strtime, "%Y-%m-%d %H")
        # 到日期的格式 2018-01-01
        elif strtime.count("-") == 2 and strtime.count(":") == 0:
            Otime = datetime.strptime(strtime, "%Y-%m-%d")
        return Otime

    def __timedelta(self, starttime, endtime):
        """
        私有方法，仅内部使用。主要是为后面求取两时间间隔时，  \n
        将时间字符串转化为时间对象后，对两个时间进行大小判断，同时进行相减  \n
        :param starttime: 时间1
        :param endtime: 时间2
        :return: datetime.timedelta类型(时间间隔)
        """
        if starttime <= endtime:
            timedelta = (endtime - starttime)
        else:
            timedelta = (starttime - endtime)
        return timedelta

    def timedelta_Secs(self, starttime, endtime):
        """
        计算两个时间之间的相差多少秒，返回的值为int类型  \n
        在进行计算之前，先要判断传入的是到小时，还是到分钟，或者是到秒，  \n
        然后再将传入的参数进行对应的时间类型转换。  \n
        :param starttime: 要比较的开始时间
        :param endtime: 要比较的结束时间
        :return: int类型(返回两个时间的差值，结果为秒)
        """
        # 进行比较之前，先进行格式转换，转换为时间对象
        start_time = self.strToTime(starttime)
        end_time = self.strToTime(endtime)
        # 调用私有方法，进行时间大小判断
        timedelta = self.__timedelta(start_time, end_time)
        # 这里必须使用total_seconds()方法，否则当秒数超过60后，就会向前进一，即转为成分钟
        # 即总共是80秒，如果使用seconds()方法，返回的值 则为20，如果使用total_seconds()则是80
        return int(timedelta.total_seconds())

    def timedelta_Mins(self, starttime, endtime):
        """
        计算两个时间之间相差多少分钟，返回的值为int类型。  \n
        在进行计算之前，先要判断传入的时间 是到小时，还是到分钟，还是到秒钟，  \n
        然后再将传入按照匹配的时间类型进行转换。  \n
        :param starttime: 要比较的开始时间
        :param endtime: 要比较的结束时间
        :return: int类型(返回两个时间的差值，结果为分钟)
        """
        # 在进行比较之前,先进行格式转换，将其转换为时间对象
        start_time = self.strToTime(starttime)
        end_time = self.strToTime(endtime)
        # 调用私有方法,进行时间大小判断，并返回相应的时间差
        timedelta = self.__timedelta(start_time, end_time)
        return int(timedelta.total_seconds() // 60)

    def timedelta_Hours(self, starttime, endtime):
        """
        计算两个时间之间相差多少小时，返回的值为int类型。  \n
        在进行计算之前，先要判断传入的时间 是到小时，还是到分钟，还是到秒钟，  \n
        然后再将传入按照匹配的时间类型进行转换。  \n
        :param starttime: 要比较的开始时间
        :param endtime: 要比较的结束时间
        :return: int类型(返回两个时间的差值，结果为小时)
        """
        # 在进行比较之前,先进行格式转换，将其转换为时间对象
        start_time = self.strToTime(starttime)
        end_time = self.strToTime(endtime)
        # 调用私有方法,进行时间大小判断，并返回相应的时间差
        timedelta = self.__timedelta(start_time, end_time)
        # return ((timedelta.seconds) // (60 * 60))
        return int(timedelta.total_seconds() // (60 * 60))

    def timedelta_Days(self, starttime, endtime):
        """
        计算两个时间之间相差多少天，返回的值为int类型。  \n
        :param starttime: 要比较的开始时间
        :param endtime: 要比较的结束时间
        :return: int类型(返回两人时间的差值，结果为天数)
        """
        # 在进行比较之前,先进行格式转换，将其转换为时间对象
        start_time = self.strToTime(starttime)
        end_time = self.strToTime(endtime)
        # 调用私有方法,进行时间大小判断，并返回相应的时间差
        timedelta = self.__timedelta(start_time, end_time)
        # return ((timedelta.seconds) // (60 * 60))
        return timedelta.days

# if __name__ == '__main__':
#     str = '2019-11-13'
#     cdt = CalcDateTime()
#     value = cdt.strToTime(str)
#     println(value,type(value))
#     value1 = cdt.getCurTimeToSec()
#     println(value1,type(value1))

# help(CalcDateTime)