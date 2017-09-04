########################## Project Submission for Wrangle OpenStreetMap Data using MongoDB #############################################################################################

Submitted by: Shrey Marwaha

Dataset : delhi_map.osm
Source : Metro-Extracts (Mapzen)

Reason for choosing this dataset: I have been born and brought up in Delhi, and I've been living here for 22 years.
                                  		    Therefore, I'm already quite familiar with this place and can verify information based on my
                                  		    own knowledge and through people living around me. This sense of familiarity helped a lot while
                                  		    auditing the dataset, and throughout the cleaning process.

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Files Included:
                READ_ME.txt
                sample_data_submission.osm(~9MB sample of original dataset)
                Delhi_OSM_Project_Submission.pdf (Project Report)
                Code Related Files:
                                   #1 audit_script.py (Contains all the audit related functions. Run as a stand-alone file)
                                   #2 cleaning_script.py (Iterates over the file to programmatically clean the data set, and calls required functions from other files)
                                        street_clean.py (For cleaning street data, called in cleaning_script.py)
                                        number_clean.py (For cleaning phone number data, called in cleaning_script.py)
                                        extra_cleaning_funcs.py (For other cleaning functions, called in cleaning_script.py)
                                   #3 exporting_as_json.py (Run to export data from json file to MongoDB, again a standalone file. Needs the json file before being run.)
                                    sample_data.py (To create sample from complete data set, modified from as given in Course Material, for Python 3.x env)

NOTE: Please change filenames in #1,2 and 3 files as required before running the code. Thank you :)

##############################################################   THE END   #################################################################################################################