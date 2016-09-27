# -*- coding:utf-8 -*-
from bqModel import bqModel

baseURL = "http://qq.yh31.com/zjbq/"

#金馆长
jgz = bqModel('0551964', '//*[@id="fontzoom"]/p/img/@src')

#斯巴达
sbd = bqModel('0551963', '//*[@id="fontzoom"]/p/img/@src')

bqDict = {
    'jgz': jgz,
    'sbd': sbd,
    'default': ''
}