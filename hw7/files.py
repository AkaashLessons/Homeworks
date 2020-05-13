def file_error(input_file):
   with open(input_file) as f:
      content = f.readlines()
      try:
         print("this is the fifth line", content[4])
      except:
         print("there is no fifth line")
      finally:
         f = open("firstline.txt", "w")
         f.write(content[0])
         f.close()
         return "open up firstline.txt"
    
