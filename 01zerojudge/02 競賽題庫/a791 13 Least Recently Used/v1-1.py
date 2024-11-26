# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a791. 13. Least Recently Used
# HP CodeWars 2008


cache = []
cases_counter = 0
cache_hit_counter = 0
while True:
    try:
        data = input().split()
    
    except EOFError:
        break

    else:
        cases_counter += len(data)
        for item in data:
            if item in cache:
                cache_hit_counter += 1
                cache.remove(item)
                cache.append(item)

            else:
                cache.append(item)
                if len(cache) > 16:
                    del cache[0]
        
        print(f'cache hit rate: {cache_hit_counter / cases_counter:.2%}')
