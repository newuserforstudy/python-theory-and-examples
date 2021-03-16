# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/16 0016 19:50
import logging

# 1 简单的日志输出：打印

# logging.debug('Debugging information')
# logging.info('Informational message')
# logging.warning('Warning:config file %s not found', 'server.conf')
# logging.error('Error occurred')
# logging.critical('Critical error -- shutting down')


# 2 日志输出到文件中
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='./my.log', level=logging.DEBUG, format=LOG_FORMAT)
#
logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")