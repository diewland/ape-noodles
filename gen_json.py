import json, os, glob, random
from pprint import pprint as pp
 
NAME = "Ape Noodles"
DESC = "Every 14th of the month for 48 months, donate an amount of noodles to a charity or organization of your choosing. Determine the winning number using two decimal places of the 1 Day Fees from the website cryptofees.info"
IMG = "https://diewland.github.io/ape-noodles/assets/ndxx%20pok.png"
ENGINE = "Jigsaw Engine"

OUTPUT_DIR = "./json"
MAX_SUPPLY = 100

if __name__ == "__main__":

    # craft metadata
    metadata = {
      "name": "***",
      "description": DESC,
      "image": "***",
      "attributes": [
        {
          "trait_type": "1 Day Fees",
          "value": "***",
        },
      ],
      "compiler": ENGINE,
    }

    # build json + write to file
    for id in range(0, MAX_SUPPLY):

        # update data
        metadata["name"] = "{} #XX".format(NAME)
        metadata["image"] = IMG
        metadata["attributes"][0]["value"] = ".XX"

        # debug
        #print(metadata)

        # write file
        with open("./{}/{}.json".format(OUTPUT_DIR, id), "w") as f:
            json.dump(metadata, f, ensure_ascii=False)
