# encoding: utf-8

import re
from config import *

import json
import subprocess

import logging

import requests as requests
import requests as __requests__


if allow_http_session:
    requests = requests.Session()

def http_request_get(url, body_content_workflow=False, allow_redirects=allow_redirects, custom_cookie=""):
    try:
        if custom_cookie:
            headers['Cookie']=custom_cookie
        result = requests.get(url, 
            stream=body_content_workflow, 
            headers=headers, 
            timeout=timeout, 
            proxies=proxies,
            allow_redirects=allow_redirects,
            verify=allow_ssl_verify)
        return result
    except Exception, e:
        # return empty requests object
        return __requests__.models.Response()

def http_request_post(url, payload, body_content_workflow=False, allow_redirects=allow_redirects, custom_cookie=""):
    """ payload = {'key1': 'value1', 'key2': 'value2'} """
    try:
        if custom_cookie:
            headers['Cookie']=custom_cookie
        result = requests.post(url, 
            data=payload, 
            headers=headers, 
            stream=body_content_workflow, 
            timeout=timeout, 
            proxies=proxies,
            allow_redirects=allow_redirects,
            verify=allow_ssl_verify)
        return result
    except Exception, e:
        # return empty requests object
        return __requests__.models.Response()

def curl_get_content(url):
    try:
        cmdline = 'curl "{url}"'.format(url=url)
        logging.info("subprocess call curl: {}".format(url))
        run_proc = subprocess.Popen(
            cmdline,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        (stdoutput,erroutput) = run_proc.communicate()
        response = {
            'resp': stdoutput.rstrip(),
            'err': erroutput.rstrip(),
        }
        return response
    except Exception as e:
        pass

