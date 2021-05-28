# -*- coding: utf-8 -*-
# @Time    : 2021/5/28 17:53
# @Author  : Lijing
# @File    : base.py

from datetime import datetime


class AbstractDataFeed:
    """
    DataFeed 的抽象类, DataFeed 应该是数据的接口，为数据的操作提供基础
    :param
    -- database_url: feed 存储的地址
    -- start_time: feed 的开始时间
    -- end_time: feed 的结束时间
    -- insert_data: 用于插入数据
    """
    _database_url: str = None
    _start_time: datetime = None
    _end_time: datetime = None

    @property
    def database_url(self):
        if self._database_url is None:
            raise RuntimeError("database的地址还没有赋值")
        else:
            return self._database_url

    @database_url.setter
    def database_url(self, url: str = None):
        if url is None:
            raise RuntimeError("请传入database的存储地址")
        else:
            self._database_url = url

    @property
    def start_time(self):
        if self._start_time is None:
            raise RuntimeError("feed的开始时间没有赋值")
        else:
            return self._start_time

    @start_time.setter
    def start_time(self, time: datetime = None):
        if time is None:
            raise RuntimeError("请传入开始时间")
        else:
            self._start_time = time

    @property
    def end_time(self):
        if self._end_time is None:
            raise RuntimeError("feed的开始时间没有赋值")
        else:
            return self._end_time

    @end_time.setter
    def end_time(self, time: datetime = None):
        if time is None:
            raise RuntimeError("请传入结束时间")
        else:
            self._end_time = time

    def insert_data(self, data):
        return NotImplemented

    def get_data(self, *args):
        return NotImplemented


