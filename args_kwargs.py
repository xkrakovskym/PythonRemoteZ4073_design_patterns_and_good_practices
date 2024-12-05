def function(a, b, *args, **kwargs):
    print(kwargs)


print(function(a=1, b=2, c=3))
