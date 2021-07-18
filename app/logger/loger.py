import logging


logging.basicConfig(filename="./logs/distance_api.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

if __name__ == '__main__':
    logging.info("Running Urban Planning")
    logging.getLogger('urbanGUI')
