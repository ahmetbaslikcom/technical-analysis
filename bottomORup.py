def dipMi(a):
    ikiOnce = a[len(a) - 3]
    birOnce = a[len(a) - 2]
    once = a[len(a) - 1]
    if ikiOnce > birOnce and once > birOnce:
        return True
    else:
        return False
      
      

def tepeMi(a):
    ikiOnce = a[len(a) - 3]
    birOnce = a[len(a) - 2]
    once = a[len(a) - 1]
    if ikiOnce < birOnce and once < birOnce:
        return True
    else:
        return False
      
