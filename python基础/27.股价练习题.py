name = "天心网络"
stock_price = 19.99
stock_code = 10256
stock_price_daily_growth_factor = 1.2
growth_days = 7
print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}")
stock_price_factor = stock_price * stock_price_daily_growth_factor ** growth_days
print("每日成长系数是%s，经过%s天增长后，股价达到了：%.1f" % (stock_price_daily_growth_factor, growth_days, stock_price_factor))
