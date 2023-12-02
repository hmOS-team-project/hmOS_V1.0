import scipy.io as scio
import os
import shutil
import torch
def copy_dir(src_path, target_path):
  if os.path.isdir(src_path) and os.path.isdir(target_path):
    filelist_src = os.listdir(src_path)
    for file in filelist_src:
      path = os.path.join(os.path.abspath(src_path), file)
      if os.path.isdir(path):
        path1 = os.path.join(os.path.abspath(target_path), file)
        if not os.path.exists(path1):
          os.mkdir(path1)
        copy_dir(path, path1)
      else:
        with open(path, 'rb') as read_stream:
          contents = read_stream.read()
          path1 = os.path.join(target_path, file)
          with open(path1, 'wb') as write_stream:
            write_stream.write(contents)
    return True

  else:
    return False

# #处理测试视频帧及标签
# dataFile = 'C://Users/10257/Desktop/PRW-v16.04.20/frame_test.mat'
# data = scio.loadmat(dataFile)
# print(type(data))
# print(data.keys())
# print(data['img_index_test'])
# print(data['img_index_test'].shape)
# sourcepath='C://Users/10257/Desktop/PRW-v16.04.20/frames'
# targetpath='C://Users/10257/Desktop/PRW-v16.04.20/testannot'
# for index in range(data['img_index_test'].shape[0]):
#      temp=data['img_index_test'][index][0]
#      if  os.path.exists(os.path.join(sourcepath, str(temp[0])+'.jpg')) :
#          shutil.copy(os.path.join(sourcepath, str(temp[0])+'.jpg.mat'), os.path.join(targetpath, str(temp[0])+'.jpg,mat'))
#      else:
#          print(os.path.join(sourcepath, str(temp[0])+'.jpg'))

#处理测试query_box
# sourcepath='C://Users/10257/Desktop/PRW-v16.04.20/query_box'
# targetpath='C://Users/10257/Desktop/PRW-v16.04.20/test_query_box'
# dataFile = 'C://Users/10257/Desktop/PRW-v16.04.20/ID_test.mat'
# files = []
# for file in os.walk(sourcepath):
#   files.append(file)
# filenames = []
# data = scio.loadmat(dataFile)
# for index in range(data['ID_test2'].shape[1]):
#     for dir_t in files:
#         if dir_t[2]:
#             for filename in dir_t[2]:
#                 if str(data['ID_test2'][0][index])+'_c' in filename :
#                     if not os.path.exists(os.path.join(targetpath,str(data['ID_test2'][0][index]))):
#                         os.makedirs(os.path.join(targetpath,str(data['ID_test2'][0][index])))
#                         shutil.copy(os.path.join(sourcepath,filename),os.path.join(targetpath,str(data['ID_test2'][0][index]),filename))
#                     else :
#                         shutil.copy(os.path.join(sourcepath, filename),
#                                  os.path.join(targetpath, str(data['ID_test2'][0][index]), filename))
#     print(data['ID_test2'][0][index])
#
#


dataFile = 'C://Users/10257/Desktop/PRW-v16.04.20/annotations/c1s2_006041.jpg.mat'
data = scio.loadmat(dataFile)
print(type(data))
print(list(data.keys()))
print(data['anno_file'])
print(data['anno_file'].shape)

# path = 'C://Users/10257/Desktop/PRW-v16.04.20/annotations'
# sourcepath='C://Users/10257/Desktop/PRW-v16.04.20/sub_test_query_box'
# sourceframespath='C://Users/10257/Desktop/PRW-v16.04.20/frames'
# targetframespath='C://Users/10257/Desktop/PRW-v16.04.20/sub_testframes'
# dirlist = os.listdir(sourcepath)
# files = []
# for file1 in os.walk(path):
#   files.append(file1)     #11816
# filenames = []
# for index2 in range(len(dirlist)):#长度50
#     i=0
#     print(index2)
#     for dir_t in files:
#        if dir_t[2]:
#            for filename in dir_t[2]:
#            # print(os.path.join(dir_t[0], filename))
#              data = scio.loadmat(os.path.join(dir_t[0], filename))
#              for index in range(data[list(data.keys())[3]].shape[0]):
#                  if int(data[list(data.keys())[3]][index][0])==int(dirlist[index2]):
#                        i=i+1
#                        print(filename)
#                        if filename not in filenames :
#                           filenames.append(filename)
#              if i>=3 :
#                 break
# print(len(filenames))
#
#
# for filename in filenames:
#     imageID,type,_ = filename.split('.')
#     shutil.copy(os.path.join(sourceframespath,imageID+'.'+type), os.path.join(targetframespath,imageID+'.'+type))

print(torch.cuda.is_available())
import torch
print(torch.__version__)
#制作50大小的query文件夹
# targetpath='C://Users/10257/Desktop/PRW-v16.04.20/sub_test_query_box'
# ssourcepath = 'C://Users/10257/Desktop/PRW-v16.04.20/test_query_box'
# dirlist = os.listdir(ssourcepath)
# for index in range(len(dirlist)):#长度450
#     if index % 9 == 0:
#       print(index)
#       os.mkdir(os.path.join(targetpath, dirlist[index]))
#       copy_dir(os.path.join(ssourcepath, dirlist[index]),
#                os.path.join(targetpath, dirlist[index]))


