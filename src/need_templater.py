"""
Need_Templater module is used to turn templates into usable files
Functions:
templater()
"""

def templater(template_file_path, replacement_map, output_file_path):
    # open original template file
    with open(template_file_path, "r") as f:
        chunk_size = 1024  # read one kb at a time
        while True:
            chunk = f.read(chunk_size) # read in the chunk
            if not chunk: # check if anything was read
                break
            for key in replacement_map.keys(): # for each key, replace it
                chunk = chunk.replace(key, replacement_map[key])
            with open(output_file_path, "a") as output:
                output.write(chunk)  # append the chunk to the output file
