file_name = 'my_file'
# tex_file = open(file_name, 'w')
# text = 'Hello file world!'
# tex_file.write(text)
# tex_file.close()

# tex_file = open(file_name, 'r')
# text = tex_file.read()
# tex_file.close()
# print(text)


# with open(file_name, 'r') as tex_file:
#     text = tex_file.read()
# print(text)


file_name_2 = 'my_file_2'
# tex_file = open(file_name_2, 'w')
# text = input('Write something: ')
# tex_file.write(text)
# tex_file.close()

with open(file_name_2, 'r') as text_file:
    text = text_file.read()
print(text)
