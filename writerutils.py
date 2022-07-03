import logging

def writeonfile(outfile,pathname,name):
    try:
        with open(pathname + name, "w") as f:
            f.write(outfile)
        f.close()
    except :
        logging.error('Errore generico')