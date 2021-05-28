# -*- coding: utf-8 -*-
# @Time    : 2021/5/28 18:48
# @Author  : Lijing
# @File    : akwrap.py

from backtrader.metabase import ParamsBase


class AKWrap(ParamsBase):

    params = (
            ('market', 'stock'),
            # class 采用空格隔开，通过akshare的命名规范，通过模糊匹配找出最相似的函数
            ('class', "")
        )


