try:
    s = int('324',2)

except ValueError:
    raise ValueError('forcely created error ')
except:
    print('error handled ')
