#Creating a general information source dictionary to tally source information
SOURCE_DICT = {"bing": "Bing",
               "Bing 2012": "Bing",
               "Bing Sat": "Bing",
               "Local_knowlwdge": "Local Knowledge",
               "yahoo": "Yahoo",
               "Yahoo hires": "Yahoo",
               "bing;gpx": "Bing",
               "gps":"GPS",
               "gps+bing for bridge": "Bing, GPS",
               "local_knowledge": "Local Knowledge",
               "local knowledge": "Local Knowledge",
               "local": "Local Knowledge",
               "survey": "Survey",
               "knowledge, source": "Local Knowledge"
               }

def modify_source(source):
    if source.strip() in SOURCE_DICT:
        correct_source_name = SOURCE_DICT.get(source)
    else:
        correct_source_name = source.strip()
    return correct_source_name

#############

STATE_DICT = {"New Delhi": "Delhi",
              "DL": "Delhi",
              "NCR": "National Capital Region",
              "u.p.": "Uttar Pradesh",
              "U.P.": "Uttar Pradesh",
              "uttar pradesh": "Uttar Pradesh",
              "haryana": "Haryana",
              "delhi": "Delhi",
              "new delhi": "Delhi"
              }
def modify_state(state):
    if state in STATE_DICT:
        correct_state = STATE_DICT.get(state)
    else:
        correct_state = state
    return correct_state