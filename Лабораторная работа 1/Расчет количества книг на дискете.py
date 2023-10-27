# TODO Найдите количество книг, которое можно разместить на дискете
size = 1.44
page = 100
line = 50
symbols = 25
size_symbol = 4
size_ = size*1024*1024
symbols_ = symbols*line*page
results_ = size_symbol*symbols_
results = round(size_/results_)
print("Количество книг, помещающихся на дискету:", results)
