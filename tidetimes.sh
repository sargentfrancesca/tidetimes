#!/bin/bash

PATH=$PATH:/usr/local/bin
export PATH
rm today.json
scrapy crawl tidespider -o today.json
