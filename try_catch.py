try:
    f  = open("textfile", "r")
    f.write("write a TEST LINE ")
except TypeError:
    print("There was a type error")
except OSError:
    print("Hey you have an OS error")
except:
    print("All other exception")
finally:
    print("I always run")