import signal
import logging
import datetime
import time
import json

import instrumentation

logging.basicConfig(format='%(asctime)s %(levelname)-5s: %(name)s %(funcName)-10s %(message)s',level=logging.DEBUG)
logging.info('started logging')

stats = {}
startTime = time.time()

def increment(stat, increase=1):
    try:
        stats[stat] += increase
    except KeyError:
        stats[stat] = increase

def storeMetrics():
    json_stats = json.dumps(stats)
    logging.debug(json_stats)
    with open('/tmp/servd.stats','w') as f:
        json.dumps(stats,f) 

class servd():
    def __init__(self):
        self._exit = False
        self._log = logging.getLogger(self.__class__.__name__)
    def _sigint_handler(self, signal, frame):
        self._exit = True
        self._log.debug('sig handler run')
        self._log.debug(self._exit)

    def run(self):
        signal.signal(signal.SIGINT,self._sigint_handler)
        self._log.debug("entering run...")
        while not self._exit:
            instrumentation.increment('while.count')
            self._log.debug(instrumentation.stats['while.count'])
            self._log.debug(self._exit)
            self._log.info("i'm keeping you in the loop")
            self._log.info(time.time())
            time.sleep(1)
        self._close()

    def _close(self):
        """ Cleanup """
        self._log.debug('saving metrics')
        self._log.debug(instrumentation.stats)
        instrumentation.stats['uptime'] = time.time() - startTime
        instrumentation.storeStats('/tmp/servd.stats')

if __name__ == "__main__":
    logging.debug("Starting main...")
    s = servd()
    s.run()
