import functools


##实现函数调用前后输出开始调用，和结束
#def log(func):
    #@functools.wraps(func)
    #def wrapper(*args, **kw):
        #print 'begin call'
        #print 'call %s():' % func.__name__
        #func(*args, **kw)
        #print 'end call'
    #return wrapper

def log(text):
    flag = False
    if callable(text):
        func = text
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if flag == True:
                print'call %s()' % func.__name__
                return func(*args, **kw)
            else:
                print'begin call %s()' % func.__name__
                func(*args, **kw)
                print'end call %s()' % func.__name__
        return wrapper
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                if flag == True:
                    print'%s %s()' % (text,func.__name__)
                    return func(*args, **kw)
                else:
                    print'begin %s %s()' % (text,func.__name__)
                    func(*args, **kw)
                    print'end %s %s()' % (text,func.__name__)
            return wrapper
        return decorator
    
    
@log('excute')
def now():
    print '2013-12-25'


if __name__ == "__main__":
    now()
    #print '版本回退'
    print 'dev'
    print 'conflic fixed'
    print 'remote dev'
    print 'test111'
    print 'ssss'
