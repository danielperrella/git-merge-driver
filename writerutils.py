def writeonfile(outfile,pathname,name):
    try:
        with open(pathname + name, "w") as f:
            f.write(outfile)
        f.close()
    except Exception as e:
        print(e)