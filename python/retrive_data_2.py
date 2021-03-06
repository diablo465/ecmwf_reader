from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()
server.retrieve({
    "class": "ei",
    "dataset": "interim_land",
    "date": "1979-01-01/to/1979-12-31",
    "expver": "2",
    "levtype": "sfc",
    "param": "182.128/228.128",
    "step": "3/6/9/12/18/24",
    "stream": "oper",
    "time": "00:00:00",
    "type": "fc",
    "target": "CHANGEME",        # this is the name of the retrived file
})
