import requests
import datetime
import hmac
import hashlib

# ===============================================
# BITTREX API CONFIG
# ===============================================

# Bittrex API version string
API_VERSION = 'v3'

# Bittrex base URL string
BITTREX_BASEURL = 'https://api.bittrex.com/' + API_VERSION

# Bittrex market API base URL string
PUBLIC_BASEURL = BITTREX_BASEURL + '/markets'

# ===============================================

class Bittrex(object):
    """Handling REST API requests to Bittrex"""
    
    def make_request(self, uri, params=None):
        """Make unauthorised request to Bittrex API
        
        Parameters:
        uri = full path to REST API,
        params (optional) = request parameters

        Return:
        requests response object
        """

        r = requests.get(uri, params=params)
        if (r.status_code == 200):
            return {"result":r.json(),"status":"OK"}
        else:
            return {"result":{},"status":"FAIL"}

    # PUBLIC REQUESTS    
    def get_market_summaries(self):
        """Used to get the last 24 hour summary of all active exchanges.
        
        Return:
        json structure
        """

        uri = PUBLIC_BASEURL + '/summaries'
        data = self.make_request(uri)
        return data

    def get_market_summary(self, market):
        """Used to get the last 24 hour summary of all active exchanges.
        
        Parameters:
        market = market name string, ex. BTC-ETH
        
        Return:
        json structure
        """

        uri = PUBLIC_BASEURL +'/{}/summary'.format(market)
        data = self.make_request(uri)
        return data
