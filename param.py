import json
import xlrd

class Param(object):
    def __init__(self, paramConf='{}'):
        self.paramConf = json.loads(paramConf)

    def paramRowsCount(self):
        pass
    def paramColsCount(self):
        pass
    def paramHeader(self):
        pass
    def paramAllline(self):
        pass
    def paramAlllineDict(self):
        pass

class XLS(Param):
    def __init__(self, paramConf):
        try:
            self.paramConf = paramConf
            self.paramfile = self.paramConf['file']
            self.data = xlrd.open_workbook(self.paramfile)
            self.getParamSheet(self.paramConf['sheet'])
        except KeyError as e:
            print(f"配置参数中缺少必要的键 {e}")
        except FileNotFoundError:
            print(f"指定的Excel文件 {self.paramfile} 不存在")
        except xlrd.biffh.XLRDError as e:
            print(f"读取Excel文件出现错误: {e}")

    def getParamSheet(self, nsheets):
        '''
        设定参数所处的sheet
        :param nsheets: 参数在第几个sheet中
        :return:
        '''
        self.paramsheet = self.data.sheets()[nsheets]

    def getOneline(self, nRow):
        '''
        返回一行数据
        :param nRow: 行数
        :return: 一行数据 []
        '''
        return self.paramsheet.row_values(nRow)

    def getOneCol(self, nCol):
        '''
        返回一列
        :param nCol: 列数
        :return: 一列数据 []
        '''
        return self.paramsheet.col_values(nCol)

    def paramRowsCount(self):
        '''
        获取参数文件行数
        :return: 参数行数 int
        '''
        return self.paramsheet.nrows

    def paramColsCount(self):
        '''
        获取参数文件列数(参数个数)
        :return: 参数文件列数(参数个数) int
        '''
        return self.paramsheet.ncols

    def paramHeader(self):
        '''
        获取参数名称
        :return: 参数名称[]
        '''
        return self.getOneline(1)

    def paramAlllineDict(self):
        '''
        获取全部参数
        :return: {{}},其中dict的key值是header的值
        '''
        nCountRows = self.paramRowsCount()
        nCountCols = self.paramColsCount()
        ParamAllListDict = {}
        iRowStep = 2
        iColStep = 0
        ParamHeader = self.paramHeader()
        while iRowStep < nCountRows:
            ParamOneLinelist = self.getOneline(iRowStep)
            ParamOnelineDict = {}
            while iColStep < nCountCols:
                ParamOnelineDict[ParamHeader[iColStep]] = ParamOneLinelist[iColStep]
                iColStep = iColStep + 1
            iColStep = 0
            ParamAllListDict[iRowStep - 2] = ParamOnelineDict
            iRowStep = iRowStep + 1
        return ParamAllListDict

    def paramAllline(self):
        '''
        获取全部参数
        :return: 全部参数[[]]
        '''
        nCountRows = self.paramRowsCount()
        paramall = []
        iRowStep = 2
        while iRowStep < nCountRows:
            paramall.append(self.getOneline(iRowStep))
            iRowStep = iRowStep + 1
        return paramall

    def __getParamCell(self, numberRow, numberCol):
        return self.paramsheet.cell_value(numberRow, numberCol)

class ParamFactory(object):

    def chooseParam(self,type,paramConf):
        """
             根据指定的参数类型选择对应的参数读取类并进行实例化。

             :param type: 参数类型的字符串表示，目前支持 'xls' 类型，后续可扩展添加其他类型。
             :param paramConf: 参数配置信息，对于 'xls' 类型来说，期望是一个包含 'file'（Excel文件路径）和 'sheet'（工作表索引）等必要键值对的字典。
             :return: 根据参数类型实例化后的对象，用于读取和获取相应来源的参数信息。
             """
        map_ = {
        'xls': XLS(paramConf)
        }
        return map_[type]
