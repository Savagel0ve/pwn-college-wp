import contextlib
import ctypes
import inspect
import os
import pathlib
import sqlite3
import subprocess
import tempfile
import time
import urllib
import requests

from flask import Flask, request, session, redirect
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


challenge_host = "challenge.localhost"
hacker_host = "hacker.localhost"
app = Flask(__name__)


@app.route('/leak') 
def route():
    #with run_browser() as browser:
    return redirect(f"http://{challenge_host}/leak")

app.run(hacker_host, 8000)
