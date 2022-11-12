# from PIL import Image
# from PIL import Image


# def paste_frame(file):
#     img_en_path = "images/tesseract_en.png"
#     img_jpn_path = "images/tesseract_jpn.png"
#     img = Image.open(img_en_path)
#     img = Image.open(file)


#     tools = pyocr.get_available_tools()
#     tool = tools[0]
#     # print(tool)
#     # print(tool.get_name())
#     img = Image.open("tesseract_jpn.png")
#     # img.show()
#     txt = tool.image_to_string(img, lang="eng+jpn", builder=pyocr.builders.TextBuilder())

# # print(txt)
#     # resized_frame = frame.resize((img.width, img.height))
#     # img.paste(resized_frame, (0, 0), resized_frame)

#     img.save(output_path)
#     img.show()
#     return output_path
