"""金融词库映射"""

# 股票相关词汇列表
RELATE_LIST_STOCK = ['股票', 'A股', '证券', '个股', '成分股', '板块', '股市']

# 港股相关词汇列表
RELATE_LIST_HK_STOCK = ['港股']

# 美股相关词汇列表
RELATE_LIST_USA_STOCK = ['美股', '美国股市']

# 基金相关词汇列表
RELATE_LIST_FUND = ['基金', 'etf', 'ETF']

# etf相关词汇列表
RELATE_LIST_ETF = ['etf', 'ETF']

# 可转债相关词汇列表
RELATE_LIST_KEZHUANZAI = ['可转债']

# 贷款相关词汇列表
RELATE_LIST_LOAN = ['贷款']

# 融资相关词汇列表
RELATE_LIST_FINANCING = ['融资']

# 理财相关词汇列表
RELATE_LIST_LICAI = ['理财']

# 指标公式相关词汇列表
RELATE_LIST_ZHIBIAO = ['指标公式', '指标']

# 主力相关词汇列表
RELATE_LIST_ZHULI = ['主力']

# 游资相关词汇列表
RELATE_LIST_YOUZI = ['游资']

# 行情相关词汇列表
RELATE_LIST_MARKET = ['行情', '市场', '行业']

TITLE_TAG = {
    '股票': RELATE_LIST_STOCK,
    '港股': RELATE_LIST_HK_STOCK,
    '美股': RELATE_LIST_USA_STOCK,
    '基金': RELATE_LIST_FUND,
    'ETF': RELATE_LIST_ETF,
    '可转债': RELATE_LIST_KEZHUANZAI,
    '贷款': RELATE_LIST_LOAN,
    '融资': RELATE_LIST_FINANCING,
    '理财': RELATE_LIST_LICAI,
    '指标公式': RELATE_LIST_ZHIBIAO,
    '主力': RELATE_LIST_ZHULI,
    '游资': RELATE_LIST_YOUZI,
    '行情': RELATE_LIST_MARKET
}