import easyocr
reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
result = reader.readtext('F:\\FAHMEED ANTLER\\letter detection photo\\H9410065158.jpg')