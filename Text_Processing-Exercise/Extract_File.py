# filepath = input().split('\\')
# filename_and_extension = filepath[-1]
# filename, extension = filename_and_extension.split('.')
# print(f'File name: {filename}')
# print(f'File extension: {extension}')

filename, extension = input().split('\\')[-1].split('.')
print(f'File name: {filename}')
print(f'File Extension: {extension}')